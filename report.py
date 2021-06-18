from http_request import HttpRequest

url = "http://www.nepalstock.com/uploads/files/reports/9aeb257512d41f186367273e4547d775.xlsx"

path = 'downloads/t.xlsx'

request = HttpRequest()

request.download(url, path)


