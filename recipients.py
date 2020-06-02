# (name, county, email)
# If you would like to add to this list, please let me know at alandgton@gmail.com
county_list = [
        ( "Mayor Eric Garcetti", "LA", "mayor.helpdesk@lacity.org" ),
        ( "City Attorney Mike Feuer", "LA", "mayor.garcetti@lacity.org" ),
        ( "Councilmember Nury Martinez", "LA", "councilmember.martinez@lacity.org"),
        ( "Councilmember Gil Cedillo", "LA", "councilmember.cedillo@lacity.org"),
        ( "Councilmember Paul Krekorian", "LA", "councilmember.Krekorian@lacity.org"),
        ( "Councilmember Bob Blumenfield", "LA", "councilmember.blumenfield@lacity.org"),
        ( "Councilmember David E. Ryu", "LA", "david.ryu@lacity.org"),

        ( "Mayor London N. Breed", "SF", "MayorLondonBreed@sfgov.org"),
        ( "Supervisor Matt Haney", "SF", "Matt.Haney@sfgov.org"),
        ( "Supervisor Rafael Mandelman", "SF", "MandelmanStaff@sfgov.org"),
        ( "Supervisor Gordon Mar", "SF", "Gordon.Mar@sfgov.org"),
        ( "Supervisor Aaron Peskin", "SF", "Aaron.Peskin@sfgov.org"),
        ( "Supervisor Dean Preston", "SF", "Dean.Preston@sfgov.org"),
        ( "Supervisor Sandra Lee Fewer", "SF", "sandra.fewer@sfgov.org"),
        ( "Supervisor Hillary Ronen", "SF", "Hillary.Ronen@sfgov.org"),
        ( "Supervisor Ahsha Safai", "SF", "Ahsha.Safai@sfgov.org"),
        ( "Supervisor Catherine Stefani", "SF", "Catherine.Stefani@sfgov.org"),
        ( "Supervisor Shamann Walton", "SF", "Shamann.Walton@sfgov.org"),
        ( "Supervisor Norman Yee", "SF", "Norman.Yee@sfgov.org"),

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

        ( "Mayor Martin Walsh", "BOS", "mayor@boston.gov"),
        ( "Councilmember Annissa Essaibi George", "BOS", "A.E.George@boston.gov"),
        ( "Councilmember Michael Flaherty", "BOS", "Michael.F.Flaherty@boston.gov"),
        ( "Councilmember Michelle Wu", "BOS", "Michelle.Wu@boston.gov"),
        ( "Councilmember Lydia Edwards", "BOS", "lydia.edwards@boston.gov"),
        ( "Councilmember Ed Flynn", "BOS", "ed.flynn@boston.gov"),
        ( "Councilmember Frank Baker", "BOS", "Frank.Baker@boston.gov"),
        ( "Councilmember Andrea Campbell", "BOS", "Andrea.Campbell@boston.gov"),
        ( "Councilmember Ricardo Arroyo", "BOS", "ricardo.arroyo@boston.gov"),
        ( "Councilmember Matt O'Malley", "BOS", "matthew.omalley@boston.gov"),
        ( "Councilmember Kenzie Bok", "BOS", "kenzie.bok@boston.gov"),

        ( "Mayor Martin Walsh", "NYC", "mayor@boston.gov"),
        ( "Councilmember Annissa Essaibi George", "BOS", "A.E.George@boston.gov"),
        ( "Councilmember Michael Flaherty", "BOS", "Michael.F.Flaherty@boston.gov"),
        ( "Councilmember Michelle Wu", "BOS", "Michelle.Wu@boston.gov"),
        ( "Councilmember Lydia Edwards", "BOS", "lydia.edwards@boston.gov"),
        ( "Councilmember Ed Flynn", "BOS", "ed.flynn@boston.gov"),
        ( "Councilmember Frank Baker", "BOS", "Frank.Baker@boston.gov"),
        ( "Councilmember Andrea Campbell", "BOS", "Andrea.Campbell@boston.gov"),
        ( "Councilmember Ricardo Arroyo", "BOS", "ricardo.arroyo@boston.gov"),
        ( "Councilmember Matt O'Malley", "BOS", "matthew.omalley@boston.gov"),
        ( "Councilmember Kenzie Bok", "BOS", "kenzie.bok@boston.gov"),
    ]

def gen_recipients(location):
    recv = []
    for c in county_list:
        recv.append(c)
    return recv
