from flask_mail import Message

# send_mail(subject='title', recipients=['123@qq.com'], content='body')
from entrance.extend.mail import mail


def send_mail(subject, recipients, content):
    try:
        message = Message(subject=subject, recipients=recipients, body=content)
        mail.send(message)
    except Exception as e:
        print('邮箱发送出错了')
        raise
