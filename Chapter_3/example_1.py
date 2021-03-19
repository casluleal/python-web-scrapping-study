from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs_obj = BeautifulSoup(html)

for link in bs_obj.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
