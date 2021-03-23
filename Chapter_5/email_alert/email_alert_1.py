from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import smtplib
import os

def send_mail(subject, body):
    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = os.getenv('EMAIL_USER')
    msg['To'] = os.getenv('EMAIL_USER')
    s = smtplib.SMTP(os.getenv('EMAIL_HOST'), port=os.getenv('EMAIL_PORT'))
    s.starttls()
    s.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))
    s.send_message(msg)
    s.quit()

bs_obj = BeautifulSoup(urlopen('https://isitchristmas.com/'))
while (bs_obj.find('a', {'id': 'answer'}).attrs['title'] == 'NO'):
    print('It is not Chrismas yet.')
    time.sleep(10)

bs_obj = BeautifulSoup(urlopen('https://isitchristmas.com/'))
send_mail("It's Christmas!", 'According to https://isitchristmas.com, it is Christmas!')
