import demand, inquire, random

# Randomly generates the subject header of the email
def gen_subject():
    s = ["Human Rights Inquiry", "Thoughts of a Concerned Citizen", "In Light of Recent Human Rights Abuses", "The Need for Police Oversight", "The Need for Police Accountability", "The Failures of Modern Law Enforcement", "Law Enforcement Must Change", "The Voice of a Troubled Citizen", "The Need for Law Enforcement Reform", "Reforms to Law Enforcement Needed", "Your Duty as a Public Servant", "Your Responsibility as a Public Servant"]
    return random.choice(s)

# Randomly generates the body of the email, follows structure of template and swaps out select words/phrases
def gen_body(src_name, dst_name, location):
    r = random.randint(0,100)
    return f'{gen_greeting(dst_name)}\t{inquire.gen_intro(location)}\n\t{inquire.gen_curiosity()}\n\t{inquire.gen_conclusion(src_name)}'

# Generates the greeting to the recipient of the email
def gen_greeting(person):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return f'{random.choice(s)} {person},\n\n'

# Prepends greeting statement to a user-generated message
def attach_greeting(person, body):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return f'{random.choice(s)} {person},\n\n{body}'


def gen_closing(name):
    c = [
            "Signed",
            "Sincerely",
            "From",
            "Regards",
            "Best",
    ]
    return f'\n{random.choice(c)},\n{name}'
