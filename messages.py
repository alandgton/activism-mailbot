import random

"""
    Template used from nomoreracistcops.github.io
"""

def gen_subject():
    s = ["Human Rights Inquiry", "Thoughts of a Concerned Citizen", "In Light of Recent Human Rights Abuses"]
    return random.choice(s)

def gen_body(src_name, dst_name, location):
    return "%s\t%s\t%s\t%s" % (gen_salutation(dst_name), gen_intro(location), gen_curiosity(), gen_conclusion(src_name))

def gen_salutation(person):
    s = ["Dear", "Hello", "Greetings"]
    return "%s %s,\n\n" % (random.choice(s), person)

def gen_intro(location):
    #nominer = ["a resident of %s" % (location), "an American citizen", "a %s native" % (location)]
    nominer = ["an American citizen", "a concerned US citizen"]
    contact = ["getting in touch", "reaching out to you", "contacting you", "sending you this message"]
    concern = ["troubled", "concerned", "disturbed"]

    return "As %s, I am %s because I am deeply %s by what I have seen recently regarding the treatment of African-Americans and peaceful protestors by police across the nation.\n" % (random.choice(nominer), random.choice(contact), random.choice(concern))

def gen_curiosity():
    verb = ["know", "inquire", "ask"]
    noun = ["safeguards", "policies", "provisions"]
    return "I would like to %s what %s our police departments have in place to prevent incidents of racism by officers. %s\n" % (random.choice(verb), random.choice(noun), gen_rhetorical_questions())

def gen_rhetorical_questions():
    q = [
            "Are all officers required to wear body cameras to record their responses to calls on video?",
            "Does the department perform any kind of anti-racism training for officers?",
            "Are new recruits screened in any way to prevent the hiring of racists, for instance through looking at social media posts?",
            "How do internal affairs investigate and respond to reports of discrimination, racism, and unjust brutality?"
    ]
    return ' '.join(random.sample(q, k=len(q)))

body =  """
Dear Mayor,\n
If these safeguards are not in place, they certainly should be, and I do not support my local taxes paying to fund a police department that perpetuates racism and violence.
Services I would rather see funded include: mental health professionals, crisis de-escalotrs, support for those suffering domestic abuse and addiction in our community, to name only a few.\n
Thank you for your attention to my concerns. I hope to hear back from you soon.
        """

def gen_conclusion(name):
    noun = ["safeguards", "policies", "provisions"]
    return "If these %s are not in place, they certainly should be, and I do not support my local taxes being used to fund police departments that perpetuate racism and violence. %s\nThank you for your attention to my concerns. I hope to hear back from you soon.\n%s" % (random.choice(noun), gen_interests(), gen_closing(name))

def gen_interests():
    i = [
            "mental health professionals,",
            "crisis de-escalators,",
            "support for those suffering domestic abuse and addition in our community,",
            "public education,",
    ]
    return "Services that I would rather see funded include: %s to name only a few." % (' '.join(random.sample(i, k=len(i))))
    
def gen_closing(name):
    return "\nSigned,\n%s" % (name)
