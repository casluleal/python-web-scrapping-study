from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs_obj = BeautifulSoup(html)

name_list = bs_obj.findAll('span', {'class': 'green'})

for name in name_list:
    print(name.get_text())
