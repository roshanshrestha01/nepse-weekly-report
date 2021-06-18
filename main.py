from weekly_report import WeeklyReport
from send_email import SendgridMail

weekly_report_page = 'http://www.nepalstock.com/reports-by-category/1'

weekly_report_obj = WeeklyReport(weekly_report_page)

reports = weekly_report_obj.get_latest_week(22)

path = './downloads/'

if not reports:
    print("Not reports to email.")

attachments_path = []

for report in reports:
    filename = '{}.xlsx'.format(report['date'])
    report_path = "{}{}".format(path, filename)
    attachments_path.push(report_path)
    weekly_report_obj.download(report['link'], report_path)
    sg = SendgridMail(filename, ['roshanshrestha@whitehatengineering.com', 'roshan@zenledger.io'])
    sg.set_attachment(report_path)
    sg.send_mail()



