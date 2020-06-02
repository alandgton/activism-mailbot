import messages, recipients, smtplib, ssl
from getpass import getpass
from email.message import EmailMessage

port = 465 # standard port for SMTP over SSL
smtp_server = "smtp.gmail.com"

src_name = input("Type your name and press enter: ")
src_email = input("Type your email and press enter: ")
password = getpass("Type your password and press enter: ")

# create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(src_email, password)

    recv = recipients.gen_recipients("LA")
    for r in recv:
        dst_name = r[0]
        location = r[1]
        dst_email = r[2]

        msg = EmailMessage()

        msg['Subject'] = messages.gen_subject()
        msg['From'] = src_email
        msg['To'] = dst_email
        
        body = messages.gen_body(src_name, dst_name, location)
        msg.set_content(body)
        print(msg.as_string())

        server.send_message(msg)
