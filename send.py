#!/usr/bin/env python3
import messages, recipients, smtplib, ssl, states, time
from getpass import getpass
from email.message import EmailMessage

def print_barrier():
    print("======================================================")

def prompt_login():
    print_barrier()
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
    print_barrier()
    return name, email, password



def prompt_email():
    print_barrier()
    print("\nWhat would you like the subject (title) of your email to be?\n")
    subject = input("Type here and press enter (if blank, a random one will be generated): ")
    print_barrier()
    return subject


def prompt_recipients():
    recv = set()
    cart = set()

    # Choose a state
    while True:
        print_barrier()
        print("Which state officials do you want to send emails to?")
        if cart: print("Cities chosen: ", cart, "\n")
        state_options = { v:k for v,k in enumerate(recipients.get_states()) }
        for idx, opt in state_options.items():
            print(idx, "->", opt)
        print("Enter blank (nothing) when done.")
        
        state_idx = input("\nType the number corresponding to the state here: ")
        print_barrier()
        # Blank -> Done
        if not state_idx:
            break
        # 0 -> All States
        elif int(state_idx) == 0:
            recv.update(recipients.get_all())
            break
        # (1 to N) -> Individual States
        elif int(state_idx) in state_options.keys():
            state = state_options[int(state_idx)]
            subcart = set()

            # Choose a city
            while True:
                city_options = { v:k for v,k in enumerate(recipients.get_cities(state)) }
                print_barrier()
                print("Which city officials do you want to send emails to?")
                if subcart: print("Cities chosen: ", subcart, "\n")
                for idx, opt in city_options.items():
                    print(idx, "->", opt)
                print("Enter blank (nothing) when done.")
                city_idx = input("\nType the number corresponding to the city here: ")
        
                if not city_idx:
                    break
                elif int(city_idx) == 0:
                    subcart.update(recipients.get_cities(state))
                    subcart.remove('Select All')
                    recv.update(recipients.get_state(state))
                    break
                elif int(city_idx) in city_options.keys():
                    subcart.add(city_options[int(city_idx)])
                    recv.update(recipients.get_city(state, city_options[int(city_idx)]))
                else:
                    print("Invalid index")
            # Add (city, state) to cart)
            for city in subcart:
                cart.add("%s, %s" % (city, states.abbreviate(state)))
            print_barrier()
        
        else:
            print("Invalid index")
    print_barrier()
    return recv


port = 465 # standard port for SMTP over SSL
smtp_server = "smtp.gmail.com"

recv = prompt_recipients()
print("\nSending emails to %d state/local officials...\n" % (len(recv)))
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
