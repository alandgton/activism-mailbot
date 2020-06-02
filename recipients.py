# (name, county, email)
# If you would like to add to this list, please let me know at alandgton@gmail.com
county_list = [
        ( "Mayor Eric Garcetti", "LA", "mayor.helpdesk@lacity.org" ),
        ( "City Attorney Mike Feuer", "LA", "mayor.garcetti@lacity.org" ),
        ( "Mayor London N. Breed", "SF", "MayorLondonBreed@sfgov.org"),
        ( "Councilmember Nury Martinez", "LA", "councilmember.martinez@lacity.org"),
        ( "Councilmember Gil Cedillo", "LA", "councilmember.cedillo@lacity.org"),
        ( "Councilmember Paul Krekorian", "LA", "councilmember.Krekorian@lacity.org"),
        ( "Councilmember Bob Blumenfield", "LA", "councilmember.blumenfield@lacity.org"),
        ( "Councilmember David E. Ryu", "LA", "david.ryu@lacity.org"),
        ( "Mayor Sam Liccardo", "SJ", "mayoremail@sanjoseca.gov"),
        ( "Vice Mayor Charles Jones", "SJ", "District1@sanjoseca.gov"),
        ( "Councilmember Sergio Jimenez", "SJ", "District2@sanjoseca.gov"),
        ( "Councilmember Raul Peralez", "SJ", "District3@sanjoseca.gov"),
        ( "Councilmember Lan Diep", "SJ", "District4@sanjoseca.gov"),
        ( "Councilmember Magdalena Carrasco", "SJ", "District5@sanjoseca.gov"),
        ( "Councilmember Devora Davis", "SJ", "District6@sanjoseca.gov"),
        ( "Councilmember Maya Esparza", "SJ", "District7@sanjoseca.gov"),
        ( "Councilmember Sylvia Arenas", "SJ", "District8@sanjoseca.gov"),
        ( "Councilmember Pam Foley", "SJ", "District9@sanjoseca.gov"),
        ( "Councilmember Johnny Khamis", "SJ", "District10@sanjoseca.gov"),
    ]

def gen_recipients(location):
    recv = []
    for c in county_list:
        recv.append(c)
    return recv
