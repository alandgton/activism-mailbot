import messages, random

"""
def ___________():
My name is [Name], and I am reaching out to demand that the Mayor and City Council redirect money away from the police department and invest into community resources.

def ___________():
It has been proven time and time again that police brutality is a systemic issue and has racially targeted Black and Brown people for hundreds of years.


"""

def gen_turnpoint():
	unacceptable = ["unacceptable", "indefensible", "inexcusable"]
	change = ["systemic change to policing", "upheaval of current methods when it comes to policing", "eradication of racism in policing", "fundamental change to policing"]
	covid = ["COVID19", "coronavirus", "the global pandemic"]
	community = ["preserving community resources", "protecting community assets", "bolstering community healthcare"]
	bolstering = ["excessively bolstering", "unnecessarily strengthening","toxically reinforcing", "disproportionately aiding"]

	r = random.randint(0,100)
	if r < 33:
		return f'This is {random.choice(unacceptable)}. At this time Black people and their allies are demanding {random.choice(change)}, and in light of {random.choice(covid)}, we need to restructure funding to focus on {random.choice(community)} instead of {random.choice(bolstering)} the police.\n'
	elif r < 66:
		return f'In this current political climate, while Black people and their allies are demanding {random.choice(change)}, this is {random.choice(unacceptable)}. We need to examine funding and ensure that it is {random.choice(community)}, as opposed to {random.choice(bolstering)} the police.\n'
	else:
		return f'We cannot continue to keep {random.choice(bolstering)} the police. The treatment of Black people in this country is {random.choice(unacceptable)}, and they alongside with their allies are demanding {random.choice(change)}. Especially given the extenuating circumstance of {random.choice(covid)}, we need to restructure funding to focus on {random.choice(community)}.\n'


def gen_redirect():
	programs = ["quality housing for all", "educational enrichment", "good jobs", "free and quality public transportation", "universal access to healthy food", "climate justice", "mental healthcare"]
	needs = ["needs", "wants", "desires", "goals", "demands", "requirements"]
	people = ["our community", "our society", "the people that make up our community", "the members of our community"]
	redirect = ["redirect", "divert", "channel", "pivot"]
	deserving = ["deserving", "worthy", "warranted", "commendable"]

	r = random.randint(0,100)
	if r < 50:
		return f'The budget of this city should be {random.choice(redirect)}ed into programs that support the {random.choice(needs)} of {random.choice(people)}: {", ".join(random.sample(programs, 7))}, and small business resources amongst others.\n'
	else:
		return f'There are many programs the city could invest in, like {random.choice(programs)}, {random.choice(programs)}, and {random.choice(programs)} (to name a few), that would greatly benefit {random.choice(people)}. You have the obligation to {random.choice(redirect)} the funds of your city from the police, to a more {random.choice(deserving)} cause.\n' 


def gen_final():
	nominer = ["As elected officials,", "Being that you are elected to office,", "You are elected officials and"]
	choice = ["duty, obligation, responsibility, requirement"]
	wellbeing = ["benefiting all of ", "serving ", "helping", "taking care of", "assisting"]
	people = ["your constituents", "those who elected you", "the people who put you in office", "your voters", "the members in your community"]
	protection = ["overprotecting", "unfairly aiding", "shielding", "protecting"]
	voices = ["make our voices heard", "speak out against injustice", "make our voices known", "speak up for our black community", "speak up until change is delivered"]
	seek = ["seek", "intend", "toil", "make it a priority to"]
	
	r = random.randint(0,100)
	if r < 33:
	    return f'You should understand that {random.choice(protection)} the police is no longer an option. We will continue to {random.choice(voices)}, and you should {random.choice(seek)} to take action that benfits us. We are {random.choice(people)}, and we deserve to be heard.\n'
	elif r < 66:
	    return f'As your community it is our {random.choice(choice)} to {random.choice(voices)}, and it is yours to listen. You should {random.choice(seek)} to help {random.choice(people)}, instead of {random.choice(protection)} the police.\n'
	else:
		return f'{random.choice(nominer)} you have a {random.choice(choice)} to listen to your community, and focus on {random.choice(wellbeing)} {random.choice(people)} rather than {random.choice(protection)} the police. We will continue to {random.choice(voices)}.\n'


print(gen_turnpoint())
# As elected officials, you have a duty to listen to your community, and focus on benefiting all of your constituents rather than overprotecting the police. We will continue to make our voice heard. 

# This is done already in messages.gen_closing()
# Sincerely, 
# [Your Full Name Here]

