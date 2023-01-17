from email.message import EmailMessage
import password

emailSender = "hamzaamirm2001@gmail.com"
passSender = password.passKey()
emailReceiver = ""
subject = ""
body = ""

em = EmailMessage()
em['From'] = emailSender
em['To'] = ''
em['Subject'] = subject
em.set_content(body)