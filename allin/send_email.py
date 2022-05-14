import smtplib
from email.mime.text import MIMEText


def send(to_email, subject, content):
    msg_from = '1468793144@qq.com'  # 发送方邮箱
    passwd = 'ritwfsecyitujcbc'  # 填入发送方邮箱的授权码
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = to_email
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    try:
        s.login(msg_from, passwd)
        s.sendmail(msg_from, to_email, msg.as_string())
        print("发送成功")
    except smtplib.SMTPDataError as e:
        print("发送失败")
    finally:
        s.quit()


