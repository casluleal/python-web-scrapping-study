from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def get_links(page_url):
    global pages

    html = urlopen('http://en.wikipedia.org' + page_url)
    bs_obj = BeautifulSoup(html)

    for link in bs_obj.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs and link.attrs['href'] not in pages:
            # we have encountered a new page
            new_page = link.attrs['href']
            print(new_page)
            pages.add(new_page)
            get_links(new_page)

get_links('')
