import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('bhavanikoduru3@gmail.com','zsgu wgpr nqnz ljvr')
    msg=EmailMessage()
    msg['FROM']='bhavanikoduru3@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

