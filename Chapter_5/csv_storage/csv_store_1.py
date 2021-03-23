import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs_obj = BeautifulSoup(html)

# The main comparison table is currently the first table on the page
table = bs_obj.find_all('table', {'class': 'wikitable'})[0]
rows = table.find_all('tr')

csv_file = open('files/editors.csv', 'wt')
writer = csv.writer(csv_file)
try:
    for row in rows:
        csv_row = []
        
        for cell in row.find_all(['td', 'th']):
            csv_row.append(cell.get_text().replace('\n', ''))
        
        writer.writerow(csv_row)
finally:
    csv_file.close()
