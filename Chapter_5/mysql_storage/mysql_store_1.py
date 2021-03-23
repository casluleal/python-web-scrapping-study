from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import os
import re

conn = pymysql.connect(
    host='127.0.0.1',
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    db='mysql',
    charset='utf8'
)
cur = conn.cursor()

cur.execute('USE scraping')
random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute(f'INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")', (title, content))
    conn.commit()

def get_links(article_url):
    html = urlopen('http://en.wikipedia.org' + article_url)
    bs_obj = BeautifulSoup(html)
    title = bs_obj.find('h1').get_text()
    content = bs_obj.find('div', {'id': 'mw-content-text'}).find('p', class_=False).get_text()

    store(title, content)
    return bs_obj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = get_links('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs['href']
        print(new_article)
        links = get_links(new_article)
finally:
    cur.close()
    conn.close()
