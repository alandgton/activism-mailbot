#!/usr/bin/env python3
import messages, recipients, smtplib, ssl, time
from getpass import getpass
from email.message import EmailMessage

def prompt_login():
    print("\n")
    name = ""
    # Validate name is not blank
    while True:
        if not name:
            name = input("Type your name and press enter: ")
        else:
            break

    # Maybe add some validation for "@gmail" suffix
    email = input("Type your email and press enter: ")
    password = getpass("Type your password and press enter: ")
    return name, email, password



def prompt_email():
    print("\nWhat would you like the subject (title) of your email to be?")
    subject = input("Type here and press enter (if blank, a random one will be generated): ")
    return subject


def prompt_recipients():
    print("\nWhich state officials do you want to send emails to?\n")
    state_options = { v:k for v,k in enumerate(recipients.get_states()) }
    for idx, opt in state_options.items():
        print(idx, "->", opt)
    
    state_idx = input("\nType the number corresponding to the state here (if blank, all states will be used): ")
    
    if state_idx:
        county_options = { v:k for v,k in enumerate(recipients.get_counties(state_options[int(state_idx)])) }
        print("\nWhich county officials do you want to send emails to?\n")
        for idx, opt in county_options.items():
            print(idx, "->", opt)
        county_idx = input("\nType the number corresponding to the county here (if blank, all counties will be used): ")
    
        if county_idx:
            recv = recipients.get_county(state_options[int(state_idx)], county_options[int(county_idx)])
        else:
            recv = recipients.get_state(state_options[int(state_idx)])
    
    else:
        recv = recipients.get_all()
    return recv


port = 465 # standard port for SMTP over SSL
smtp_server = "smtp.gmail.com"

recv = prompt_recipients()
subject = prompt_email()
src_name, src_email, password = prompt_login()

while True:
    try:
        # create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(src_email, password)
            while recv:
                recipient = recv.pop()
                dst_name = recipient[0]
                location = recipient[1]
                dst_email = recipient[2]

                msg = EmailMessage()

                msg['Subject'] = subject if subject else messages.gen_subject()
                msg['From'] = src_email
                msg['To'] = dst_email
                
                body = messages.gen_body(src_name, dst_name, location)
                msg.set_content(body)
                print(msg.as_string())

                server.send_message(msg)
        break
    except smtplib.SMTPException:
        print("Unexpected error... trying again in 10 seconds.")
        time.sleep(10)
