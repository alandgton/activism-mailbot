# (name, county, email)
county_list = [
        ( "Mayor Eric Garcetti", "LA", "mayor.helpdesk@lacity.org" ),
        ( "City Attorney Mike Feuer", "LA", "mayor.garcetti@lacity.org" ),
        ( "Mayor London N. Breed", "SF", "MayorLondonBreed@sfgov.org"),
        ( "Councilmember Nury Martinez", "LA", "councilmember.martinez@lacity.org"),
    ]

def gen_recipients(location):
    recv = []
    for c in county_list:
        recv.append(c)
    return recv
