from bs4 import BeautifulSoup
from datetime import datetime
from http_request import HttpRequest

request = HttpRequest()

url = 'http://www.nepalstock.com/reports-by-category/1'

resp = request.get(url)
html_text = resp.data
soup = BeautifulSoup(html_text, 'html.parser')

for row in soup.find_all('tr')[2:]:
  cols = row.find_all('td')
  if len(cols) != 3:
    continue
  date_string = cols[1].text
  date = datetime.strptime(date_string, '%Y.%m.%d')
  week_number = date.isocalendar().week
  link = cols[2].find('a').get('href')
  print(week_number, date, link)
