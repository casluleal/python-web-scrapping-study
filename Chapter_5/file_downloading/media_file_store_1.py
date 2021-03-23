from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs_obj = BeautifulSoup(html)
image_location = bs_obj.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(image_location, 'logo.jpg')
