import os
from datetime import datetime
from weekly_report import WeeklyReport
from send_email import SendgridMail
from dotenv import load_dotenv

load_dotenv()

weekly_report_page = 'http://www.nepalstock.com/reports-by-category/1'

weekly_report_obj = WeeklyReport(weekly_report_page)

reports = weekly_report_obj.get_latest_week()

path = './downloads/'

if not reports:
    print("Not reports to email.", datetime.now())

for report in reports:
    filename = '{}.xlsx'.format(report['date'])
    report_path = "{}{}".format(path, filename)
    weekly_report_obj.download(report['link'], report_path)
    sg = SendgridMail(filename, os.getenv('TO_EMAIL').split(', '))
    sg.set_attachment(report_path)
    sg.send_mail()



