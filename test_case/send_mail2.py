#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#发送邮箱
sender = 'xiaozhuzhu7586@126.com'
#接收邮箱
receiver = 'zwbtestpython@126.com'
#发送邮箱服务器
smtpserver = 'smtp.126.com'
#发送邮箱用户/密码
username = 'xiaozhuzhu7586@126.com'
password = 'dulizizhu2007'
msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = 'Python email test'
#构造附件
att = MIMEText(open('D:\\pytest\\test_xmlmail\\report\\log.txt', 'rb').read(), 'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.txt"'
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
