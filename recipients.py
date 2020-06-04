# If you would like to add to this list, please let me know at alandgton@gmail.com
# Currently mayors and city council members and police commissioners

# a dictionary that maps states to dictionaries that map counties to contacts
# contacts are tuples (name, county, email)
mailing_list = {
    "California" : {
        "Los Angeles" : [
            ( "Mayor Eric Garcetti", "LA", "mayor.helpdesk@lacity.org" ),
            ( "City Attorney Mike Feuer", "LA", "mayor.garcetti@lacity.org" ),
            ( "Councilmember Nury Martinez", "LA", "councilmember.martinez@lacity.org"),
            ( "Councilmember Gil Cedillo", "LA", "councilmember.cedillo@lacity.org"),
            ( "Councilmember Paul Krekorian", "LA", "councilmember.Krekorian@lacity.org"),
            ( "Councilmember Bob Blumenfield", "LA", "councilmember.blumenfield@lacity.org"),
            ( "Councilmember David E. Ryu", "LA", "david.ryu@lacity.org"),
            ( "LA Board of Police Commissioners", "LA", "policecommission@lapd.online"),
        ],
        "San Francisco" : [
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
            ( "San Francisco Police Commission", "SF", "sfpd.commission@sfgov.org"),
        ],
        "San Jose" : [
            ( "Mayor Sam Liccardo", "San Jose", "mayoremail@sanjoseca.gov"),
            ( "Vice Mayor Charles Jones", "San Jose", "District1@sanjoseca.gov"),
            ( "Councilmember Sergio Jimenez", "San Jose", "District2@sanjoseca.gov"),
            ( "Councilmember Raul Peralez", "San Jose", "District3@sanjoseca.gov"),
            ( "Councilmember Lan Diep", "San Jose", "District4@sanjoseca.gov"),
            ( "Councilmember Magdalena Carrasco", "San Jose", "District5@sanjoseca.gov"),
            ( "Councilmember Devora Davis", "San Jose", "District6@sanjoseca.gov"),
            ( "Councilmember Maya Esparza", "San Jose", "District7@sanjoseca.gov"),
            ( "Councilmember Sylvia Arenas", "San Jose", "District8@sanjoseca.gov"),
            ( "Councilmember Pam Foley", "San Jose", "District9@sanjoseca.gov"),
            ( "Councilmember Johnny Khamis", "San Jose", "District10@sanjoseca.gov"),
        ],
        "Santa Clara" : [
            ("Mayor Lisa Gillmore", "Santa Clara", "lgillmor@santaclaraca.gov"),
            ("Vice Mayor Karen Hardy", "Santa Clara", "khardy@santaclaraca.gov"),
            ("Councilmember Kathy Watanabe", "Santa Clara", "kwatanabe@santaclaraca.gov"),
            ("Councilmember Raj Chahal", "Santa Clara", "rchahal@santaclaraca.gov"),
            ("Councilmember Teresa O'Neill", "Santa Clara", "toneill@santaclaraca.gov"),
            ("Councilmember Karen Hardy", "Santa Clara", "khardy@santaclaraca.gov"),
            ("Councilmember Debbie Davis", "Santa Clara", "ddavis@santaclaraca.gov"),
            ("City Attorney Brian Doyle", "Santa Clara", "CityAttorney@santaclaraca.gov"),
        ],
        "Alameda" : [
            ("Mayor Marilyn Ezzy Ashcraft", "Alameda", "mezzyashcraft@alamedaca.gov"),
            ("Vice Mayor John Knox White", "Alameda", "jknoxwhite@alamedaca.gov"),
            ("Councilmember Tony Daysog", "Alameda", "tdaysog@alamedaca.gov"),
            ("Councilmember Jim Oddie", "Alameda", "joddie@alamedaca.gov"),
            ("Councilmember Malia Vella", "Alameda", "mvella@alamedaca.gov"),
            ("District Attorney Nancy E. O’Malley", "Alameda", "info@alcoda.org"),
        ],
    },
    "Massachusetts" : {
        "Boston" : [
            ( "Mayor Martin Walsh", "Boston", "mayor@boston.gov"),
            ( "Councilmember Annissa Essaibi George", "Boston", "A.E.George@boston.gov"),
            ( "Councilmember Michael Flaherty", "Boston", "Michael.F.Flaherty@boston.gov"),
            ( "Councilmember Michelle Wu", "Boston", "Michelle.Wu@boston.gov"),
            ( "Councilmember Lydia Edwards", "Boston", "lydia.edwards@boston.gov"),
            ( "Councilmember Ed Flynn", "Boston", "ed.flynn@boston.gov"),
            ( "Councilmember Frank Baker", "Boston", "Frank.Baker@boston.gov"),
            ( "Councilmember Andrea Campbell", "Boston", "Andrea.Campbell@boston.gov"),
            ( "Councilmember Ricardo Arroyo", "Boston", "ricardo.arroyo@boston.gov"),
            ( "Councilmember Matt O'Malley", "Boston", "matthew.omalley@boston.gov"),
            ( "Councilmember Kenzie Bok", "Boston", "kenzie.bok@boston.gov"),
            ( "Commissioner William Gross", "Boston", "mediarelations@pd.boston.gov"),
        ],
    },
    "Minnesota" : {
        "Minneapolis" : [
            ( "Mayor Jacob Frey", "Minneapolis", "Jacob.Frey@minneapolismn.gov"),
            ( "Councilmember Kevin Reich", "Minneapolis", "kevin.reich@minneapolismn.gov"),
            ( "Councilmember Cam Gordon", "Minneapolis", "cam.gordon@minneapolismn.gov"),
            ( "Councilmember Steve Fletcher", "Minneapolis", "steve.fletcher@minneapolismn.gov"),
            ( "Councilmember Phillipe Cunningham", "Minneapolis", "Phillipe.Cunningham@minneapolismn.gov"),
            ( "Councilmember Jeremiah Ellison", "Minneapolis", "Jeremiah.Ellison@minneapolismn.gov"),
            ( "Councilmember Lisa Goodman", "Minneapolis", "Lisa.Goodman@minneapolismn.gov"),
            ( "Councilmember Andrea Jenkins", "Minneapolis", "Andrea.Jenkins@minneapolismn.gov"),
            ( "Councilmember Alondra Cano", "Minneapolis", "Alondra.Cano@minneapolismn.gov"),
            ( "Councilmember Lisa Bender", "Minneapolis", "Lisa.Bender@minneapolismn.gov"),
            ( "Councilmember Jeremy Schroeder", "Minneapolis", "Jeremy.Schroeder@minneapolismn.gov"),
            ( "Councilmember Andrew Johnson", "Minneapolis", "Andrew.Johnson@minneapolismn.gov"),
            ( "Councilmember Linea Palmisano", "Minneapolis", "Linea.Palmisano@minneapolismn.gov"),
        ],
    },
    "New York" : {
        "NYC" : [
            ( "Mayor Bill de Blasio", "NYC", "bdeblasio@cityhall.nyc.gov"),
            ( "Manhattan Borough President Gale Brewer", "NYC", "gbrewer@manhattanbp.nyc.gov"),
            ( "Director Jeremy Unger", "NYC", "junger@council.nyc.gov"),
            ( "Councilperson Corey Johnson", "NYC", "SpeakerJohnson@council.nyc.gov"),
            ( "Councilperson Keith Powers", "NYC", "kpowers@council.nyc.gov"),
            ( "Senator Brad Hoylman", "NYC", "hoylman@nysenate.gov"),
            ( "Senator Brian Kavanaugh", "NYC", "kavanagh@nysenate.gov"),
            ( "Assemblymember Richard Gottfried", "NYC", "GottfriedR@assembly.state.ny.us"),
            ( "Assemblymember Deborah Glick", "NYC", "glickd@assembly.state.ny.us"),
        ],
    },
    "Pennsylvania" : {
        "Philadelphia" : [
            ( "Mayor Jim Kenney", "Philadelphia", "james.kenney@phila.gov"),
            ( "Council President Darrell Clarke", "Philadelphia", "darrell.clarke@phila.gov"),
            ( "Councilmember Mark Squilla", "Philadelphia", "mark.squilla@phila.gov"),
            ( "Councilmember Kenyatta Johnson", "Philadelphia", "kenyatta.johnson@phila.gov"),
            ( "Councilmember Jamie Gauthier", "Philadelphia", "jamie.gauthier@phila.gov"),
            ( "Councilmember Curtis Jones", "Philadelphia", "curtis.jones@phila.gov"),
            ( "Councilmember Bobby Henon", "Philadelphia", "bobby@bobbyhenon.com"),
            ( "Councilmember Maria Quiñones Sánchez", "Philadelphia", "maria.q.sanchez@phila.gov"),
            ( "Councilmember Cindy Bass", "Philadelphia", "cindy.bass@phila.gov"),
            ( "Councilmember Cherelle Parker", "Philadelphia", "cherelle.parker@phila.gov"),
            ( "Councilmember Brian O'Neill", "Philadelphia", "brian.o'neill@phila.gov"),
            ( "Councilmember Kendra Brooks", "Philadelphia", "Kendra.Brooks@phila.gov"),
            ( "Councilmember Allan Domb", "Philadelphia", "allan.domb@phila.gov"),
            ( "Councilmember Derek Green", "Philadelphia", "derek.green@phila.gov"),
            ( "Councilmember Helen Gym", "Philadelphia", "helen.gym@phila.gov"),
            ( "Councilmember David Oh", "Philadelphia", "david.oh@phila.gov"),
            ( "Councilmember Isaiah Thomas", "Philadelphia", "Isaiah.Thomas@phila.gov"),
            ( "Commissioner Richard Ross", "Philadelphia", "police.commissioner@phila.gov"),
        ],
    },
    "Washington DC" : {
        "DC" : [
            ( "Mayor Muriel Bowser", "DC", "eom@dc.gov"),
            ( "Chairman Phil Mendelson", "DC", "pmendelson@dccouncil.us"),
            ( "Councilmember Kenyan McDuffie", "DC", "kmcduffie@dccouncil.us"),
            ( "Councilmember Anita Bonds", "DC", "abonds@dccouncil.us"),
            ( "Councilmember David Grosso", "DC", "dgrosso@dccouncil.us"),
            ( "Councilmember Robert White", "DC", "rwhite@dccouncil.us"),
            ( "Councilmember Elissa Silverman", "DC", "esilverman@dccouncil.us"),
            ( "Councilmember Brianne Nadeau", "DC", "bnadeau@dccouncil.us"),
            ( "Councilmember Mary Cheh", "DC", "mcheh@dccouncil.us"),
            ( "Councilmember Brandon Todd", "DC", "btodd@dccouncil.us"),
            ( "Councilmember Charles Allen", "DC", "callen@dccouncil.us"),
            ( "Councilmember Vincent Gray", "DC", "vgray@dccouncil.us"),
            ( "Councilmember Trayon White", "DC", "twhite@dccouncil.us"),
        ],
    },
    "Washington State" : {
        "Seattle" : [
            ( "Mayor Jenny Durkan", "Seattle", "jenny.durkan@seattle.gov"),
            ( "Councilmember Lisa Herbold", "Seattle", "lisa.herbold@seattle.gov"),
            ( "Councilmember Tammy Morales", "Seattle", "tammy.morales@seattle.gov"),
            ( "Councilmember Kshama Sawant", "Seattle", "kshama.sawant@seattle.gov"),
            ( "Councilmember Alex Pedersen", "Seattle", "alex.pedersen@seattle.gov"),
            ( "Councilmember Debora Juerez", "Seattle", "debora.juarez@seattle.gov"),
            ( "Councilmember Dan Strauss", "Seattle", "dan.strauss@seattle.gov"),
            ( "Councilmember Andrew Lewis", "Seattle", "andrew.lewis@seattle.gov"),
            ( "Councilmember Teresa Mosqueda", "Seattle", "teresa.mosqueda@seattle.gov"),
        ],
    },
    "Texas" : {
        "Plano" : [
            ( "Mayor Harry LaRosiliere", "Plano", "mayor@plano.gov"),
            ( "Mayor Pro Tem Kayci Prince", "Plano", "kayciprince@plano.gov"),
            ( "Deputy Mayor Pro Tem Anthony Ricciardelli", "Plano", "aricciardelli@plano.gov"),
            ( "Councilmember Maria Tu", "Plano", "mariatu@plano.gov"),
            ( "Councilmember Rick Grady", "Plano", "rickgrady@plano.gov"),
            ( "Councilmember Shelby Williams", "Plano", "shelbywilliams@plano.gov"),
            ( "Councilmember Rick Smith", "Plano", "ricksmith@plano.gov"),
            ( "Councilmember Lily Bao", "Plano", "lilybao@plano.gov"),
        ],
        "Dallas" : [
            ( "Mayor Pro Tem Adam Medrano", "Dallas", "adam.medrano@dallascityhall.com"),
            ( "Deputy Mayor Pro Tem B. Adam McGough", "Dallas", "adam.mcgough@dallascityhall.com"),
            ( "Council Liaison Laura Cadena", "Dallas", "Laura.Cadena@dallascityhall.com"),
            ( "Council Assistant Yesenia Valdez", "Dallas", "Yesenia.Valdez@dallascityhall.com"),
            ( "Councilmember Chad West", "Dallas", "Chad.West@dallascityhall.com"),
            ( "Councilmember Casey Thomas, II", "Dallas", "richard.soto@dallascityhall.com"),
            ( "Councilmember Carolyn King Arnold", "Dallas", "District4@DallasCityHall.com"),
            ( "Councilmember Jaime Resendez", "Dallas", "jaime.resendez@dallascityhall.com"),
            ( "Councilmember Tennell Atkins", "Dallas", "maria.salazar2@dallascityhall.com"),
            ( "Councilmember Paula Blackmon", "Dallas", "District9@DallasCityHall.com"),
            ( "Councilmember Lee M. Kleinman", "Dallas", "sophia.figueroa@dallascityhall.com"),
            ( "Councilmember Cara Mendelsohn", "Dallas", "cara.mendelsohn@dallascityhall.com"),
        ],
    },
    "Georgia" : {
        "Atlanta" : [
            ("Mayor Keisha Lance Bottoms", "Atlanta", "kbottoms@atlantaga.gov"),
            ("Council President Felicia A. Moore", "Atlanta", "fmoore@atlantaga.gov"),
            ("Councilmember Carla Smith", "Atlanta", "csmith@atlantaga.gov"),
            ("Councilmember Amir R. Farokhi", "Atlanta", "arfarokhi@atlantaga.gov"),
            ("Councilmember Antonio Brown", "Atlanta", "antoniobrown@atlantaga.gov"),
            ("Councilmember Cleta Winslow", "Atlanta", "cwinslow@atlantaga.gov"),
            ("Councilmember Natalyn Archibong", "Atlanta", "narchibong@atlantaga.gov"),
            ("Councilmember Jennifer N. Ide", "Atlanta", "jnide@atlantaga.gov"),
            ("Councilmember Howard Shook", "Atlanta", "hshook@atlantaga.gov"),
            ("Councilmember J.P. Matzigkeit", "Atlanta", "jpmatzigkeit@atlantaga.gov"),
            ("Councilmember Dustin Hills", "Atlanta", "drhillis@atlantaga.gov"),
            ("Councilmember Andrea L. Boone", "Atlanta", "aboone@atlantaga.gov"),
            ("Councilmember Marci Collier Overstreet", "Atlanta", "mcoverstreet@atlantaga.gov"),
            ("Councilmember Joyce Sheperd", "Atlanta", "jmsheperd@atlantaga.gov"),
            ("Councilmember Michael Julian Bond", "Atlanta", "mbond@atlantaga.gov"),
            ("Councilmember Matt Westmoreland", "Atlanta", "mwestmoreland@atlantaga.gov"),
            ("Councilmember Andre Dickens", "Atlanta", "adickens@atlantaga.gov"),
        ],
    },
}

def get_all():
    recv = []
    for state in mailing_list:
        for county in mailing_list[state]:
            recv.extend(mailing_list[state][county])
    return recv

def get_state(state):
    recv = []
    for county in mailing_list[state]:
        recv.extend(mailing_list[state][county])
    return recv

def get_county(state, county):
    return mailing_list[state][county]

def get_states():
    return mailing_list.keys()

def get_counties(state):
    return mailing_list[state].keys()
