import smtplib
from email.mime.text import MIMEText
import os

msg = MIMEText('The body of the email is here.')

msg['Subject'] = 'An Email Alert'
msg['From'] = os.getenv('EMAIL_USER')
msg['To'] = os.getenv('EMAIL_USER')
s = smtplib.SMTP(os.getenv('EMAIL_HOST'), port=os.getenv('EMAIL_PORT'))
s.starttls()
s.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))
s.send_message(msg)
s.quit()
