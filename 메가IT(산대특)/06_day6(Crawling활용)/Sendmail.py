import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendMail(from_addr,to_addr,subject,content,files=[]):
    content_type="plain" # or html
    username="dlwjdgns4128" #구글일 경우 이메일 주소
    password="dlwjdgns8342"
    smtp='dlwjdgns4128@naver.com'
    port=465 #G mail : ,587


    msg=MIMEMultipart()
    msg["Subject"]=subject
    msg["From"]=from_addr
    msg["To"]=to_addr
    msg.attach(MIMEText(content,content_type))

    if files:
        for f in files:
            with open(f,"rb") as a_file:
                basename=os.path.basename(f)
                part=MIMEApplication(a_file.read(),Name=basename)

                part['Content-Disposition']='attachment; filename="%s"' %basename
                msg.attach(part)

    mail=SMTP('dlwjdgns4128@naver.com')
    mail.ehlo()
    mail.starttls()
    mail.login(username,password)
    mail.sendmail(from_addr,to_addr,msg.as_string())
    mail.quit()

if __name__ =="__main__":
    sendMail("dlwjdgns4128@naver.com","apple032448@gmail.com","제목",'내용')