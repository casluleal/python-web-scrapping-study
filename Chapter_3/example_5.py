# Get the title, first paragraph and edit link from a given Wikipedia page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def get_links(page_url):
    global pages

    html = urlopen('http://en.wikipedia.org' + page_url)
    bs_obj = BeautifulSoup(html)

    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find(id='mw-content-text').find_all('p')[1])
        print(bs_obj.find(id='ca-edit').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries, though.')

    for link in bs_obj.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we have encountered a new page
                new_page = link.attrs['href']
                print('---------------\n' + new_page)
                pages.add(new_page)
                get_links(new_page)

get_links('/wiki/Portrait_of_a_Musician')
