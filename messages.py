import random

"""
    Template credit: nomoreracistcops.github.io
"""

# Randomly generates the subject header of the email
def gen_subject():
    s = ["Human Rights Inquiry", "Thoughts of a Concerned Citizen", "In Light of Recent Human Rights Abuses", "The Need for Police Oversight", "The Failures of Modern Law Enforcement", "Law Enforcement Must Change", "The Voice of a Troubled Citizen"]
    return random.choice(s)

# Randomly generates the body of the email, follows structure of template and swaps out select words/phrases
def gen_body(src_name, dst_name, location):
    return "%s\t%s\t%s\t%s" % (gen_greeting(dst_name), gen_intro(location), gen_curiosity(), gen_conclusion(src_name))

# Generates the greeting to the recipient of the email
def gen_greeting(person):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return "%s %s,\n\n" % (random.choice(s), person)

# Generates the first sentence of the email. Takes no assumptions about where the user is located,
# but can easily be extended to do so. For now, addresses recipients as an American citizen.
def gen_intro(location):
    #nominer = ["a resident of %s" % (location), "an American citizen", "a %s native" % (location)]
    nominer = ["As an American citizen,", "As a concerned US citizen,", "I am an American citizen and"]
    contact = ["getting in touch", "reaching out to you", "contacting you", "sending you this message"]
    adverb = ["deeply", "very", "greatly", "extremely", "especially", "immensely"]
    concern = ["troubled", "concerned", "disturbed"]
    reason = ["unfair treatment of African-Americans", "blatant racism against African-Americans"]
    scale = ["across the nation", "throughout the country", "nationwide", "across the country", "throughout the nation"]

    return "%s I am %s because I am %s %s by what I have recently seen regarding the %s by police %s.\n" % (random.choice(nominer), random.choice(contact), random.choice(adverb), random.choice(concern), random.choice(reason), random.choice(scale))

# Randomly generates a message rooted on human curiosity to expose the inadequacies of the current system
def gen_curiosity():
    verb = ["know", "inquire", "ask"]
    noun = ["safeguards", "policies", "provisions"]
    crime = ["incidents of racism", "violations of human rights", "occurrences of racism", "explotations of human rights"]

    return "I would like to %s what %s our police departments have in place to prevent %s by officers. %s\n" % (random.choice(verb), random.choice(noun), random.choice(crime), gen_rhetorical_questions())

# Randomly generates a relentless stream of hard-hitting rhetorical questions
def gen_rhetorical_questions():
    q = [
            "Are all officers required to wear body cameras to record their responses to calls on video?",
            "Does the department perform any form of anti-racism training for officers?",
            "Are new recruits screened in any way to prevent the hiring of racists, for instance: looking at their social media posts?",
            "How do internal affairs investigate and respond to reports of discrimination, racism, and unjust brutality?",
            "How can the general public be ensured that incidences of racist violence by police are not simply swepy under the rug?",
    ]
    return ' '.join(random.sample(q, k=len(q)))

def gen_conclusion(name):
    noun = ["safeguards", "policies", "provisions"]
    return "If these %s are not in place, then they certainly should be. I do not support my local taxes being used to fund police departments that perpetuate racism and violence. %s\nThank you for your attention to my concerns. I hope to hear back from you soon.\n%s" % (random.choice(noun), gen_interests(), gen_closing(name))

def gen_interests():
    preambles = [
            "Services that I would rather see funded include",
            "I would like to redirect funding to"
            "Areas that I would like funds to be redirected to include",
    ]
    i = [
            "mental health professionals,",
            "crisis de-escalators,",
            "support for victims domestic abuse and addiction,",
            "public education,",
            "scientific research,",
    ]
    return "Services that I would rather see funded include: %s to name only a few." % (' '.join(random.sample(i, k=len(i))))
    
def gen_closing(name):
    c = [
            "Signed",
            "Sincerely",
            "From",
            "Regards",
            
    ]
    return "\nSigned,\n%s" % (name)

print(gen_body("Alan", "Alan", "Alan"))
