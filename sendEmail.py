# coding=gbk
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

msg = MIMEMultipart('related')
msg['to'] = 'zhangcm106@chinaunicom.cn'
msg['from'] = 'forisez@163.com'
msg['subject'] = '您好'

txt = MIMEText("测试", 'plain', 'gbk')
msg.attach(txt)

inpath = 'C:\Users\chmzh\Documents\测试'
for filename in os.listdir(inpath):
    att1 = MIMEText(open(os.path.join(inpath, filename), 'rb').read(), 'base64', 'gbk')
    att1["Content-Type"] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
    msg.attach(att1)

try:
    server = smtplib.SMTP()
    server.connect('smtp.163.com')
    server.starttls()
    server.login('forisez@163.com', 'xxxxx')
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()
    print "send ok"
except Exception, e:
    print str(e)
