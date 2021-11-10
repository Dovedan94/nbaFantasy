TEAMS_ABBS = [
    "ATL",
    "BRK",
    "BOS",
    "CHO",
    "CHI",
    "CLE",
    "DAL",
    "DEN",
    "DET",
    "GSW",
    "HOU",
    "IND",
    "LAC",
    "LAL",
    "MEM",
    "MIA",
    "MIL",
    "MIN",
    "NOP",
    "NYK",
    "OKC",
    "ORL",
    "PHI",
    "PHO",
    "POR",
    "SAC",
    "SAS",
    "TOR",
    "UTA",
    "WAS",
]

TEAMS_NAMES = [
    "Atlanta_Hawks",
    "Brooklyn_Nets",
    "Boston_Celtics",
    "Charlotte_Hornets",
    "Chicago_Bulls",
    "Cleveland_Cavaliers",
    "Dallas_Mavericks",
    "Denver_Nuggets",
    "Detroit_Pistons",
    "Golden_State_Warriors",
    "Houston_Rockets",
    "Indiana_Pacers",
    "Los_Angeles_Clippers",
    "Los_Angeles_Lakers",
    "Memphis_Grizzlies",
    "Miami_Heat",
    "Milwaukee_Bucks",
    "Minnesota_Timberwolves",
    "New_Orleans_Pelicans",
    "New_York_Knicks",
    "Oklahoma_City_Thunder",
    "Orlando_Magic",
    "Philadelphia_76ers",
    "Phoenix_Suns",
    "Portland_Trail_Blazers",
    "Sacramento_Kings",
    "San_Antonio_Spurs",
    "Toronto_Raptors",
    "Utah_Jazz",
    "Washington_Wizards",
]
TEAMS = zip(TEAMS_ABBS, TEAMS_NAMES)

DOVEDAN_PLAYERS_NAMES = [
    "Kevin Durant",
    "Chris Paul",
    "Mike Conley",
    "Gordon Hayward",
    "Kyle Lowry",
    "Derrick Rose",
    "Tyrese Haliburton",
    "Joe Ingles",
    "Grayson Allen",
    "Alec Burks",
]
DOVEDAN_PLAYERS_LINKS = [
    "duranke01",
    "paulch01",
    "conlemi01",
    "haywago01",
    "lowryky01",
    "rosede01",
    "halibty01",
    "inglejo01",
    "allengr01",
    "burksal01",
]
DOVEDAN_PLAYERS = {"Dovedan": list(zip(DOVEDAN_PLAYERS_NAMES, DOVEDAN_PLAYERS_LINKS))}
DOVEDAN_TEAMS = ["BRK", "PHO", "UTA", "CHO", "MIA", "NYK", "SAC", "UTA", "POR", "NYK"]

DUNJIC_PLAYERS_NAMES = [
    "Joel Embiid",
    "Jaylen Brown",
    "Cade Cunningham",
    "Deandre Ayton",
    "Christian Wood",
    "Derrick White",
    "Devonte' Graham",
    "Wendell Carter Jr.",
    "Patty Mills",
    "Luke Kennard",
]
DUNJIC_PLAYERS_LINKS = [
    "embiijo01",
    "brownja02",
    "cunnica01",
    "aytonde01",
    "woodch01",
    "whitede01",
    "grahade01",
    "cartewe01",
    "millspa02",
    "kennalu01",
]
DUNJIC_PLAYERS = {"Dunjic": list(zip(DUNJIC_PLAYERS_NAMES, DUNJIC_PLAYERS_LINKS))}
DUNJIC_TEAMS = ["PHI", "BOS", "DET", "PHO", "HOU", "SAS", "NOP", "ORL", "BRK", "LAC"]

FIZESAN_PLAYERS_NAMES = [
    "James Harden",
    "Anfernee Simons",
    "Andrew Wiggins",
    "LaMelo Ball",
    "Franz Wagner",
    "Kevin Porter Jr.",
    "Jalen Suggs",
    "Montrezl Harrell",
    "Richaun Holmes",
    "Scottie Barnes",
]
FIZESAN_PLAYERS_LINKS = [
    "hardeja01",
    "simonan01",
    "wiggian01",
    "ballla01",
    "wagnefr01",
    "porteke02",
    "suggsja01",
    "harremo01",
    "holmeri01",
    "barnesc01",
]
FIZESAN_PLAYERS = {"Fizesan": list(zip(FIZESAN_PLAYERS_NAMES, FIZESAN_PLAYERS_LINKS))}
FIZESAN_TEAMS = ["BRK", "NOP", "GSW", "CHO", "LAL", "HOU", "ORL", "WAS", "SAC", "TOR"]

GOSTOVIC_PLAYERS_NAMES = [
    "Damian Lillard",
    "Terry Rozier",
    "Jrue Holiday",
    "Bojan Bogdanović",
    "Joe Harris",
    "Spencer Dinwiddie",
    "Keldon Johnson",
    "Eric Gordon",
    "Darius Bazley",
    "Cam Reddish",
]
GOSTOVIC_PLAYERS_LINKS = [
    "lillada01",
    "roziete01",
    "holidjr01",
    "bogdabo02",
    "harrijo01",
    "dinwisp01",
    "johnske04",
    "gordoer01",
    "bazleda01",
    "reddica01",
]
GOSTOVIC_PLAYERS = {
    "Gostovic": list(zip(GOSTOVIC_PLAYERS_NAMES, GOSTOVIC_PLAYERS_LINKS))
}
GOSTOVIC_TEAMS = ["POR", "CHO", "MIL", "UTA", "BRK", "WAS", "SAS", "MEM", "OKC", "ATL"]

JOKANOVIC_PLAYERS_NAMES = [
    "Giannis Antetokounmpo",
    "CJ McCollum",
    "Pascal Siakam",
    "Bogdan Bogdanović",
    "John Wall",
    "Dennis Schröder",
    "Marcus Smart",
    "Steven Adams",
    "Jarrett Allen",
    "T.J. McConnell",
]
JOKANOVIC_PLAYERS_LINKS = [
    "antetgi01",
    "mccolcj01",
    "siakapa01",
    "bogdabo01",
    "walljo01",
    "schrode01",
    "smartma01",
    "adamsst01",
    "allenja01",
    "mccontj01",
]
JOKANOVIC_PLAYERS = {
    "Jokanovic": list(zip(JOKANOVIC_PLAYERS_NAMES, JOKANOVIC_PLAYERS_LINKS))
}
JOKANOVIC_TEAMS = ["MIL", "POR", "TOR", "ATL", "HOU", "BOS", "BOS", "MEM", "CLE", "IND"]

KARADZIC_PLAYERS_NAMES = [
    "Jayson Tatum",
    "Tobias Harris",
    "Jimmy Butler",
    "Tyler Herro",
    "Jordan Poole",
    "Malik Beasley",
    "Harrison Barnes",
    "Jusuf Nurkić",
    "Andre Drummond",
    "Tyrese Maxey",
]
KARADZIC_PLAYERS_LINKS = [
    "tatumja01",
    "harrito02",
    "butleji01",
    "herroty01",
    "poolejo01",
    "beaslma01",
    "barneha02",
    "nurkiju01",
    "drumman01",
    "maxeyty01",
]
KARADZIC_PLAYERS = {
    "Karadzic": list(zip(KARADZIC_PLAYERS_NAMES, KARADZIC_PLAYERS_LINKS))
}
KARADZIC_TEAMS = ["BOS", "PHI", "MIA", "MIA", "GSW", "MIN", "SAC", "POR", "PHI", "PHI"]

MANDIC_PLAYERS_NAMES = [
    "Donovan Mitchell",
    "Furkan Korkmaz",
    "Gary Trent Jr.",
    "Jerami Grant",
    "Reggie Jackson",
    "Clint Capela",
    "Terrence Ross",
    "Terance Mann",
    "Doug McDermott",
    "Rui Hachimura",
]
MANDIC_PLAYERS_LINKS = [
    "mitchdo01",
    "korkmfu01",
    "trentga02",
    "grantje01",
    "jacksre01",
    "capelca01",
    "rosste01",
    "mannte01",
    "mcderdo01",
    "hachiru01",
]
MANDIC_PLAYERS = {"Mandic": list(zip(MANDIC_PLAYERS_NAMES, MANDIC_PLAYERS_LINKS))}
MANDIC_TEAMS = ["UTA", "DEN", "TOR", "DET", "LAC", "ATL", "ORL", "LAC", "PHO", "WAS"]

MARINOVIC_PLAYERS_NAMES = [
    "LeBron James",
    "Khris Middleton",
    "Shai Gilgeous-Alexander",
    "DeMar DeRozan",
    "Ricky Rubio",
    "Danilo Gallinari",
    "Shake Milton",
    "Evan Mobley",
    "Bobby Portis",
    "Victor Oladipo",
]
MARINOVIC_PLAYERS_LINKS = [
    "jamesle01",
    "middlkh01",
    "gilgesh01",
    "derozde01",
    "rubiori01",
    "gallida01",
    "miltosh01",
    "mobleev01",
    "portibo01",
    "oladivi01",
]
MARINOVIC_PLAYERS = {
    "Marinovic": list(zip(MARINOVIC_PLAYERS_NAMES, MARINOVIC_PLAYERS_LINKS))
}
MARINOVIC_TEAMS = ["LAL", "MIL", "OKC", "CHI", "BRK", "ATL", "PHI", "CLE", "MIL", "MIA"]

MEDIC_PLAYERS_NAMES = [
    "Trae Young",
    "Karl-Anthony Towns",
    "Malcolm Brogdon",
    "John Collins",
    "OG Anunoby",
    "Mikal Bridges",
    "Chris Duarte",
    "Will Barton",
    "Miles Bridges",
    "De'Anthony Melton",
]
MEDIC_PLAYERS_LINKS = [
    "youngtr01",
    "townska01",
    "brogdma01",
    "collijo01",
    "anunoog01",
    "bridgmi01",
    "duartch01",
    "bartowi01",
    "bridgmi02",
    "meltode01",
]
MEDIC_PLAYERS = {"Medic": list(zip(MEDIC_PLAYERS_NAMES, MEDIC_PLAYERS_LINKS))}
MEDIC_TEAMS = ["ATL", "MIN", "IND", "ATL", "TOR", "PHO", "IND", "DEN", "CHO", "MEM"]

MILIC_PLAYERS_NAMES = [
    "Anthony Davis",
    "Ja Morant",
    "Klay Thompson",
    "Kemba Walker",
    "Caris LeVert",
    "Jalen Green",
    "Al Horford",
    "Brook Lopez",
    "Cole Anthony",
    "Jae'Sean Tate",
]
MILIC_PLAYERS_LINKS = [
    "davisan02",
    "moranja01",
    "thompkl01",
    "walkeke02",
    "leverca01",
    "greenja05",
    "horfoal01",
    "lopezbr01",
    "anthoco01",
    "tateja01",
]
MILIC_PLAYERS = {"Milic": list(zip(MILIC_PLAYERS_NAMES, MILIC_PLAYERS_LINKS))}
MILIC_TEAMS = ["LAL", "MEM", "GSW", "NYK", "IND", "HOU", "BOS", "MIL", "ORL", "HOU"]

MRAKOVIC_PLAYERS_NAMES = [
    "Paul George",
    "Zach LaVine",
    "Bam Adebayo",
    "Jordan Clarkson",
    "Jaren Jackson Jr.",
    "De'Andre Hunter",
    "Marcus Morris",
    "Jalen Brunson",
    "Desmond Bane",
    "Nickeil Alexander-Walker",
]
MRAKOVIC_PLAYERS_LINKS = [
    "georgpa01",
    "lavinza01",
    "adebaba01",
    "clarkjo01",
    "jacksja02",
    "huntede01",
    "morrima03",
    "brunsja01",
    "banede01",
    "alexani01",
]
MRAKOVIC_PLAYERS = {
    "Mrakovic": list(zip(MRAKOVIC_PLAYERS_NAMES, MRAKOVIC_PLAYERS_LINKS))
}
MRAKOVIC_TEAMS = ["LAC", "CHI", "MIA", "UTA", "MEM", "ATL", "LAC", "DAL", "MEM", "NOP"]

PEJOVIC_PLAYERS_NAMES = [
    "Devin Booker",
    "Brandon Ingram",
    "Domantas Sabonis",
    "Dillon Brooks",
    "Darius Garland",
    "Kyle Kuzma",
    "Kelly Oubre Jr.",
    "James Wiseman",
    "James Bouknight",
    "Aleksej Pokusevski",
]
PEJOVIC_PLAYERS_LINKS = [
    "bookede01",
    "ingrabr01",
    "sabondo01",
    "brookdi01",
    "garlada01",
    "kuzmaky01",
    "oubreke01",
    "wisemja01",
    "bouknja01",
    "pokusal01",
]
PEJOVIC_PLAYERS = {"Pejovic": list(zip(PEJOVIC_PLAYERS_NAMES, PEJOVIC_PLAYERS_LINKS))}
PEJOVIC_TEAMS = ["PHO", "NOP", "IND", "MEM", "CLE", "WAS", "CHO", "GSW", "CHO", "OKC"]

TUROHAN_PLAYERS_NAMES = [
    "Luka Dončić",
    "Russell Westbrook",
    "Kristaps Porziņģis",
    "Jonas Valančiūnas",
    "D'Angelo Russell",
    "Lonzo Ball",
    "Carmelo Anthony",
    "Nicolas Batum",
    "Zion Williamson",
    "Dāvis Bertāns",
]
TUROHAN_PLAYERS_LINKS = [
    "doncilu01",
    "westbru01",
    "porzikr01",
    "valanjo01",
    "russeda01",
    "balllo01",
    "anthoca01",
    "batumni01",
    "willizi01",
    "bertada01",
]
TUROHAN_PLAYERS = {"Turohan": list(zip(TUROHAN_PLAYERS_NAMES, TUROHAN_PLAYERS_LINKS))}
TUROHAN_TEAMS = ["DAL", "LAL", "DAL", "NOP", "MIN", "CHI", "LAL", "LAC", "ATL", "WAS"]

SAVCIC_PLAYERS_NAMES = [
    "Nikola Jokić",
    "Nikola Vučević",
    "LaMarcus Aldridge",
    "Buddy Hield",
    "RJ Barrett",
    "Seth Curry",
    "Lauri Markkanen",
    "Ivica Zubac",
    "Monte Morris",
    "Davion Mitchell",
]
SAVCIC_PLAYERS_LINKS = [
    "jokicni01",
    "vucevni01",
    "aldrila01",
    "hieldbu01",
    "barrerj01",
    "curryse01",
    "markkla01",
    "zubaciv01",
    "morrimo01",
    "mitchda01",
]
SAVCIC_PLAYERS = {"Savcic": list(zip(SAVCIC_PLAYERS_NAMES, SAVCIC_PLAYERS_LINKS))}
SAVCIC_TEAMS = ["DEN", "CHI", "CLE", "SAC", "NYK", "PHI", "CLE", "LAC", "DEN", "SAC"]


SAVOVIC_PLAYERS_NAMES = [
    "Bradley Beal",
    "De'Aaron Fox",
    "Fred VanVleet",
    "Dejounte Murray",
    "Rudy Gobert",
    "Ben Simmons",
    "Luguentz Dort",
    "Kevin Huerter",
    "Aaron Gordon",
    "Josh Jackson",
]
SAVOVIC_PLAYERS_LINKS = [
    "bealbr01",
    "foxde01",
    "vanvlfr01",
    "murrade01",
    "goberru01",
    "simmobe01",
    "dortlu01",
    "huertke01",
    "gordoaa01",
    "jacksjo02",
]
SAVOVIC_PLAYERS = {"Savovic": list(zip(SAVOVIC_PLAYERS_NAMES, SAVOVIC_PLAYERS_LINKS))}
SAVOVIC_TEAMS = ["WAS", "SAC", "TOR", "SAS", "UTA", "PHI", "OKC", "ATL", "TOR", "DET"]


SUBERIC_PLAYERS_NAMES = [
    "Stephen Curry",
    "Julius Randle",
    "Anthony Edwards",
    "Norman Powell",
    "Tim Hardaway Jr.",
    "Evan Fournier",
    "Duncan Robinson",
    "Saddiq Bey",
    "Myles Turner",
    "Kentavious Caldwell-Pope",
]
SUBERIC_PLAYERS_LINKS = [
    "curryst01",
    "randlju01",
    "edwaran01",
    "powelno01",
    "hardati02",
    "fournev01",
    "robindu01",
    "beysa01",
    "turnemy01",
    "caldwke01",
]
SUBERIC_PLAYERS = {"Suberic": list(zip(SUBERIC_PLAYERS_NAMES, SUBERIC_PLAYERS_LINKS))}
SUBERIC_TEAMS = ["GSW", "NYK", "MIN", "POR", "DAL", "NYK", "MIA", "DET", "IND", "WAS"]


DOVEDAN_ROSTER = {"Dovedan": list(zip(DOVEDAN_TEAMS, DOVEDAN_PLAYERS_NAMES))}
TUROHAN_ROSTER = {"Turohan": list(zip(TUROHAN_TEAMS, TUROHAN_PLAYERS_NAMES))}
SAVCIC_ROSTER = {"Savcic": list(zip(SAVCIC_TEAMS, SAVCIC_PLAYERS_NAMES))}
JOKANOVIC_ROSTER = {"Jokanovic": list(zip(JOKANOVIC_TEAMS, JOKANOVIC_PLAYERS_NAMES))}
KARADZIC_ROSTER = {"Karadzic": list(zip(KARADZIC_TEAMS, KARADZIC_PLAYERS_NAMES))}
PEJOVIC_ROSTER = {"Pejovic": list(zip(PEJOVIC_TEAMS, PEJOVIC_PLAYERS_NAMES))}
SUBERIC_ROSTER = {"Suberic": list(zip(SUBERIC_TEAMS, SUBERIC_PLAYERS_NAMES))}
DUNJIC_ROSTER = {"Dunjic": list(zip(DUNJIC_TEAMS, DUNJIC_PLAYERS_NAMES))}
GOSTOVIC_ROSTER = {"Gostovic": list(zip(GOSTOVIC_TEAMS, GOSTOVIC_PLAYERS_NAMES))}
MARINOVIC_ROSTER = {"Marinovic": list(zip(MARINOVIC_TEAMS, MARINOVIC_PLAYERS_NAMES))}
MEDIC_ROSTER = {"Medic": list(zip(MEDIC_TEAMS, MEDIC_PLAYERS_NAMES))}
MANDIC_ROSTER = {"Mandic": list(zip(MANDIC_TEAMS, MANDIC_PLAYERS_NAMES))}
MILIC_ROSTER = {"Milic": list(zip(MILIC_TEAMS, MILIC_PLAYERS_NAMES))}
SAVOVIC_ROSTER = {"Savovic": list(zip(SAVOVIC_TEAMS, SAVOVIC_PLAYERS_NAMES))}
FIZESAN_ROSTER = {"Fizesan": list(zip(FIZESAN_TEAMS, FIZESAN_PLAYERS_NAMES))}
MRAKOVIC_ROSTER = {"Mrakovic": list(zip(MRAKOVIC_TEAMS, MRAKOVIC_PLAYERS_NAMES))}

ALL_ROSTERS = [
    MRAKOVIC_ROSTER,
    MILIC_ROSTER,
    MEDIC_ROSTER,
    MANDIC_ROSTER,
    MARINOVIC_ROSTER,
    DUNJIC_ROSTER,
    TUROHAN_ROSTER,
    SAVCIC_ROSTER,
    SAVOVIC_ROSTER,
    FIZESAN_ROSTER,
    DOVEDAN_ROSTER,
    SUBERIC_ROSTER,
    PEJOVIC_ROSTER,
    JOKANOVIC_ROSTER,
    GOSTOVIC_ROSTER,
    KARADZIC_ROSTER,
]

ALL_PLAYERS_PTS_LOGS = [
    MRAKOVIC_PLAYERS,
    MILIC_PLAYERS,
    MEDIC_PLAYERS,
    MANDIC_PLAYERS,
    MARINOVIC_PLAYERS,
    DUNJIC_PLAYERS,
    TUROHAN_PLAYERS,
    SAVCIC_PLAYERS,
    SAVOVIC_PLAYERS,
    FIZESAN_PLAYERS,
    DOVEDAN_PLAYERS,
    SUBERIC_PLAYERS,
    PEJOVIC_PLAYERS,
    JOKANOVIC_PLAYERS,
    GOSTOVIC_PLAYERS,
    KARADZIC_PLAYERS,
]
