from bs4 import BeautifulSoup
from urllib.request import urlopen
get = BeautifulSoup(urlopen("http://www.epsdistribucija.rs/Dan_3_Iskljucenja.htm"),'lxml')
#tables = get.findChildren('table')
table = get.find_all('table')[0]
row_marker=0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    print(row)
