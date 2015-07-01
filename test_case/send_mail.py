#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱
sender = 'xiaozhuzhu7586@126.com'
#接收邮箱
receiver = 'zwbtestpython@126.com'
#发送邮件主题
subject = 'Python email test'
#发送邮箱服务器
smtpserver = 'smtp.126.com'
#发送邮箱用户/密码
username = 'xiaozhuzhu7586@126.com'
password = 'dulizizhu2007'
#编写text 类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
