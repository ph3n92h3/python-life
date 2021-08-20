import os  # 用于获取程序名
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # 创建邮件对象
from email.utils import formataddr  # 创建发件人addresser、收件人addressee


# do some other tasks
# do some other tasks
# do some other tasks


email_addresser = '##########@qq.com'  # 发件人邮箱账号
email_password = '****************'  # 发件人邮箱授权码
email_addressee = ['##########@qq.com']  # 收件人邮箱账号，我这边发送给自己

# 创建邮件对象
message = MIMEMultipart()
message['Subject'] = "您的程序 "+os.path.basename(__file__)+" 已执行完成"  # 邮件主题
message['From'] = 'python小精灵'  # 发件人邮箱昵称

message['To'] = email_addressee[0]  # 收件人邮箱昵称
# 创建邮件正文内容
message.attach(MIMEText('您好，您的程序 '+os.path.basename(__file__) +
                        ' 已执行完成,请注意查看。', 'plain', 'utf-8'))

# 创建附件对象
att = MIMEText(open('email_test.txt', 'rb').read(), 'base64', 'utf-8')
att.add_header('Content-type', 'application/octet-stream')
att.add_header('Content-Disposition', 'attachment', filename="email_test.txt")
message.attach(att)

# 登录并发送邮件
try:
    # 创建发送对象
    server = smtplib.SMTP('smtp.qq.com')  # 请选择适用于你的SMTP
    server.login(email_addresser, email_password)  # 发件人邮箱账号、邮箱密码
    server.sendmail(email_addresser, email_addressee,
                    message.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送的邮件
    print('邮件发送成功👌')
    server.quit()  # 关闭连接
except smtplib.SMTPException as e:
    print("error:", e)
