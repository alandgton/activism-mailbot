import random

"""
def ___________():
My name is [Name], and I am reaching out to demand that the Mayor and City Council redirect money away from the police department and invest into community resources. It has been proven time and time again that police brutality is a systemic issue and has racially targeted Black and Brown people for hundreds of years.

def ___________():
This is unacceptable. At this time Black people and their allies are demanding systemic change to policing, and in light of COVID19, we need to restructure funding to focus on preserving community resources instead of excessively bolstering the police.

def ___________():
This city’s funds should be redirected into programs that support the needs of our community: quality housing for all, educational enrichment, good jobs, free and quality public transportation, universal access to healthy food, climate justice, mental healthcare, and small business resources amongst others.

def ___________():
As elected officials, you have a duty to listen to your community, and focus on benefiting all of your constituents rather than overprotecting the police. We will continue to make our voice heard. 

// This is done already in messages.gen_closing()
Sincerely, 
[Your Full Name Here]
"""

def gen_message(name):
    return f"{gen_thesis('Alan')} {gen_elaborate()} {gen_more()} {gen_suggest()}"

def gen_thesis(name):
    n = [ "My name is", "I'm" ]
    contact = ["getting in touch", "reaching out", "contacting you", "sending you this message"]
    verb = ["demand for", "ask for", "request for"]
    money = ["funds", "public funds", "taxpayer money"]
    scale = ["community", "local"]
    service = ["programs", "services", "resources"]

    return f'{random.choice(n)} {name} and I am {random.choice(contact)} to {random.choice(verb)} the redirection of {random.choice(money)} away from the police department and into other {random.choice(scale)} {random.choice(service)}.'

def gen_elaborate():
    h = ["It has been proven time and time again", "History has shown", "Recent events have shown"]
    adjective = ["an institutional", "a systemic"]
    noun = ["issue", "problem"]
    adverb = ["disproportionately", "unfairly", "unevenly", "unequally"]
    verb = ["targets", "affects", "victimizes", "preys upon"]
    p = ["Black and Brown people", "the African-American and Latinx communities"]
    scale = ["across the nation", "throughout the country", "nationwide", "across the country", "throughout the nation"]

    return f"{random.choice(h)} that police brutality is {random.choice(adjective)} {random.choice(noun)} that {random.choice(adverb)} {random.choice(verb)} {random.choice(p)} {random.choice(scale)}."

def gen_more():
    i = ["This is unacceptable.", "This is intolerable.", "The status quo is failing us.", "The current system is failing us.", "The status quo needs to be reformed.", "The law enforcement system needs to be reformed."]
    n = ["desire", "need", "yearning", "craving"]
    a = ["systemic", "structural", "institutional"]
    c = ["change", "reform"]
    p = ["policing", "law enforcement"]
    r = ["manifested in", "resulted in", "brought about"]
    u = ["public unrest", "civil unrest", "protests and riots across the nation"]

    return f"{random.choice(i)} At this time, the {random.choice(n)} for {random.choice(a)} {random.choice(c)} to {random.choice(p)} has {random.choice(r)} {random.choice(u)}."

def gen_suggest():
    f = ["funds", "resources", "energy", "money"]
    a = ["must", "should", "need to"]
    v = ["redirected", "diverted"]
    s = ["services", "programs", "resources"]
    r = ["reflect", "support"]
    n = ["needs", "concerns", "desires"]

    return f"The city's {random.choice(f)} {random.choice(a)} be {random.choice(v)} to {random.choice(s)} that {random.choice(r)} the {random.choice(n)} of our community: {gen_interests()}."
    

print(gen_message("Alan"))
