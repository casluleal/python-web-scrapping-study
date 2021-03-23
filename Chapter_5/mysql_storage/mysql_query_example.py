import pymysql
import os

conn = pymysql.connect(
    host='127.0.0.1',
    user=os.getenv('MYSQL_USER'),
    passwd=os.getenv('MYSQL_PASSWORD'),
    db='mysql'
)

cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages WHERE id = 1')
print(cur.fetchone())
cur.close()
conn.close()
