from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs_obj = BeautifulSoup(html)

print(bs_obj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
