import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class Email(object):
    def __init__(self,msg,receiver):
        self.msg = msg
        self.sender = 'mayw@corp.hxqc.com'
        self.receiver = receiver
        self.mail_host = 'mail.corp.hxqc.com'
        self.mail_user = 'mayw@corp.hxqc.com'
        self.passw = 'j123456789'

    def mailtext(self):
        message = MIMEMultipart()
        '''message['From'] = Header('马援伟')
        message['To'] = Header('余洁')'''
        sub = '接口测试结果'
        message['Subject'] = Header(sub,'utf-8')

        message.attach(MIMEText(self.msg))

        attr = MIMEText(open('C:\\Users\\cpr223\\PycharmProjects\\ApiTestLearn\\TestResult\\Result.html',encoding='utf-8').read(),'base64')
        attr["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        attr["Content-Disposition"] = 'attachment;filename="result.html"'
        message.attach(attr)

        return message

    def sendmail(self):
        smtp = smtplib.SMTP()
        try:
            smtp.connect(self.mail_host)
            smtp.login(self.mail_user,self.passw)
            res = smtp.sendmail(self.sender,self.receiver,self.mailtext().as_string())
        except:
            print('邮件发送失败，请检查发送信息！')
        else:
            print('邮件发送成功！')

m = Email('我是天才','287541778@qq.com')
m.mailtext()
m.sendmail()