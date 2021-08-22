from bs4 import BeautifulSoup
from datetime import datetime
from http_request import HttpRequest


TODAY_WEEK_NUMBER = datetime.now().isocalendar().week


class WeeklyReport:

    def __init__(self, url):
        self.url = url
        self.request = HttpRequest()

    def get_page(self):
        response = self.request.get(self.url)
        html = response.data
        return html

    def parse_html(self):
        source = BeautifulSoup(self.get_page(), 'html.parser')
        return source

    def table_rows(self):
        source = self.parse_html()
        rows = source.find_all('tr')
        rows_with_valid_data = rows[2:]
        return rows_with_valid_data

    @staticmethod
    def process_data(soup_tr):
        report_detail = {}
        columns = soup_tr.find_all('td')
        if len(columns) == 3:
            date_in_string = columns[1].text
            report_link = columns[2].find('a').get('href')
            report_release_date = datetime.strptime(date_in_string, '%Y.%m.%d')
            report_detail['date'] = date_in_string
            report_detail['week_number'] = report_release_date.isocalendar().week
            report_detail['year'] = report_release_date.isocalendar().year
            report_detail['link'] = report_link
        return report_detail

    def get_latest_week(self, week_number=TODAY_WEEK_NUMBER):
        previous_week = week_number - 1
        year = datetime.now().year
        latest_reports = []
        reports = self.get_reports()
        for report in reports:
            if report['week_number'] >= previous_week and report['year'] == year:
                latest_reports.append(report)
        return latest_reports

    def get_reports(self):
        rows = []
        for soup_tr in self.table_rows():
            formatted_data = self.process_data(soup_tr)
            if formatted_data:
                rows.append(formatted_data)
        return rows

    def download(self, file_url, path):
        self.request.download(file_url, path)
