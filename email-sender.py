from email.message import EmailMessage
import password
import ssl
import smtplib

emailSender = "hamzaamirm2001@gmail.com"
passSender = password.passKey()
emailReceiver = "yesago1323@usharer.com"
subject = "Hello World!"
body = "This is an auto generated email just for testing a program."

em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, passSender)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())