"""Stories of Thursday 19 November 2026, each checked against dated reporting.

Every item below is an event that happened, or was first reported, on 19 November 2026
in some time zone. The `source` string is documentation only: it is never drawn, and it
records what was read to confirm the date and the wording.

Record shapes:
    heroes/panels: (region, field, headline, deck, body, colour, illo, source)
    index:         (region, field, one-line headline)
"""

HEROES = [
    ("ASIA", "SUMMIT",
     "Xi, Trump and Putin hold a first trilateral",
     "No breakthrough, but a 'declaration toward peace'",
     "The three presidents met for over an hour on the APEC sidelines in Shenzhen and "
     "issued a joint declaration on nuclear risk, oil and UN reform. They announced no "
     "breakthrough on Ukraine.",
     "RED", "summit",
     "Guardian 19 Nov 14:32Z; CNBC 19 Nov 06:27Z; AFP/Anadolu 19 Nov; AP 19 Nov"),

    ("ASIA", "LAW",
     "World Court: Myanmar committed genocide",
     "The first such ruling against any state",
     "The ICJ held Myanmar responsible for genocide against the Rohingya in the 2017 "
     "clearance operations, and ordered it to stop, punish and make reparations. The "
     "court estimated 10,000 were killed.",
     "OCHRE", "court",
     "UN News 19 Nov; ICJ press release 2026/30, 19 Nov; AP 19 Nov 20:05Z; BBC 19 Nov"),

    ("EUROPE", "DIPLOMACY",
     "Ukraine's allies meet in Berlin",
     "Europe warns against a 'Yalta 2.0'",
     "Some 40 partners, with Zelensky, Merz and Trump's envoys Witkoff and Kushner, "
     "backed a European-led force and 'legally binding' guarantees, and urged Russia to "
     "accept a winter truce on energy.",
     "NAVY", "berlin",
     "DW live blog 19 Nov; Ukrainska Pravda 19 Nov 13:46; Reuters 19 Nov 00:03Z; AP 19 Nov"),
]

PANELS = [
    ("EUROPE", "CONFLICT",
     "Kerch Bridge struck a third time in four days",
     "Kyiv: Neptune missiles hit rail and arch",
     "Ukraine's defence ministry confirmed the hits and Russia halted all train traffic "
     "over the bridge, the third strike in four days. Putin vowed to hit back and ruled "
     "out a Black Sea truce.",
     "TEAL", "bridge",
     "Kyiv Independent 19 Nov 02:04Z; DW live 19 Nov; Politico 19 Nov 08:39Z; NBC 19 Nov"),

    ("MIDEAST", "CONFLICT",
     "Houthi missile damages Riyadh's tallest tower",
     "PIF Tower hit in the financial district",
     "Saudi civil defence reported material damage to the Public Investment Fund tower "
     "and nearby buildings, but no injuries. Saudi warplanes struck Sanaa the same day.",
     "OCHRE", "missile",
     "Reuters 19 Nov 03:19Z; Al Jazeera 19 Nov; Sky News 19 Nov 22:36Z; Arab Weekly 19 Nov"),

    ("AMERICAS", "MARKETS",
     "Anthropic's record debut closes up 17pc",
     "The largest listing on record, above its range",
     "The maker of Claude sold 980 million shares at 83 dollars, raising about 81 "
     "billion, then opened at 111.50 and closed at 97.17, above SpaceX's debut.",
     "PLUM", "ipo",
     "AP 18 Nov (pricing); NBC New York 19 Nov; Yahoo Finance 19 Nov 23:00Z; WSJ 19 Nov"),

    ("OCEANIA", "CLIMATE",
     "Tonga declares a drought emergency",
     "27 days of emergency powers, water short",
     "The acting prime minister declared a state of emergency from 19 November to 16 "
     "December, citing El Nino drought and water shortages. Schools closed early.",
     "GREEN", "drought",
     "Matangi Tonga 19 Nov 13:18; RNZ 19 Nov 01:03Z; Pacific Media Network 19 Nov"),

    ("AMERICAS", "POLITICS",
     "Senate blocks the Iran war powers resolution",
     "Defeated 51-48, three Republicans defecting",
     "The resolution would have forced Trump to end hostilities with Iran without "
     "Congress. It failed as US strikes and Iranian attacks on shipping continued.",
     "SLATE", "senate",
     "Reuters 19 Nov 21:28Z; Washington Post 19 Nov 22:49Z; Al Jazeera 19 Nov"),

    ("AFRICA", "DIPLOMACY",
     "Somalia expels the UAE ambassador",
     "72 hours to leave; Mogadishu recalls its envoy",
     "Somalia accused Abu Dhabi of undermining its sovereignty and gave the ambassador "
     "three days to go, the sharpest step since it cancelled all UAE agreements.",
     "GREEN", "embassy",
     "Al Jazeera 19 Nov 21:32Z; AP 19 Nov 14:42Z; Middle East Eye 19 Nov 17:33Z"),

    ("ASIA", "POLITICS",
     "Mongolia's parliament accepts the resignation",
     "Speaker takes over as acting president",
     "The State Great Khural accepted President Khurelsukh's resignation over railway "
     "corruption allegations. Speaker Byambatsogt holds the post until an election.",
     "RED", "parliament",
     "AP/ABC 19 Nov 11:17Z; Montsame 19 Nov 12:45; The Diplomat 19 Nov"),

    ("OCEANIA", "ECONOMY",
     "Australian unemployment jumps to 4.9pc",
     "A five-year high; 43,500 jobs lost",
     "The October jobless rate rose to 4.9 per cent, its highest since 2021, and "
     "employment fell by 43,500 where economists had expected a modest rise.",
     "TEAL", "chart",
     "ABS release 19 Nov 00:30Z; ABC 19 Nov 04:45Z; WSJ 19 Nov 02:03Z; Bloomberg 19 Nov"),

    ("WORLD", "SCIENCE",
     "Voyager 1 reaches one light-day from Earth",
     "16 billion miles, and still phoning home",
     "The 1977 probe became the first object made by people to be a full day's travel "
     "away at the speed of light. Its signal now takes 24 hours to arrive.",
     "NAVY", "probe",
     "NASA 19 Nov; PBS 19 Nov 18:51Z; Space.com 19 Nov 15:00Z"),
]

INDEX = [
    ("ASIA", "SUMMIT", "Xi pledges 20m dollars and a Shenzhen centre"),
    ("ASIA", "DIPLOMACY", "Takaichi and Putin meet on the APEC sidelines"),
    ("ASIA", "SOCIETY", "South Korea cuts exam-hall wifi to foil AI cheating"),
    ("ASIA", "DISASTER", "Magnitude 5.7 quake shakes Kumamoto; two injured"),
    ("ASIA", "HUMANITARIAN", "UNHCR halts refugee registration in Malaysia"),
    ("ASIA", "SECURITY", "Indonesia arrests 15 suspects in six provinces"),
    ("ASIA", "DEFENCE", "India and Japan widen drills at 2+2 talks"),
    ("ASIA", "TECH", "Alibaba tops forecasts as AI cloud revenue climbs"),
    ("ASIA", "POLITICS", "Bangladesh arson spreads across ten districts"),

    ("EUROPE", "DEFENCE", "Denmark ratifies the US-Greenland defence deal"),
    ("EUROPE", "HEALTH", "France raises its bird flu risk level to high"),
    ("EUROPE", "DIPLOMACY", "Macron wants the question of NATO entry reopened"),
    ("EUROPE", "SOCIETY", "EU health chief pelted with ashes by protesters"),
    ("EUROPE", "POLITICS", "Leasehold reform bill enters the UK Parliament"),
    ("EUROPE", "DISASTER", "Bayesian inquiry: crew 'unaware of risks'"),
    ("EUROPE", "SECURITY", "EU Commission confirms AI-assisted cyberattack"),

    ("MIDEAST", "DEFENCE", "France to put a post-UNIFIL plan to the UN"),
    ("MIDEAST", "DEFENCE", "CENTCOM chief meets the Saudi crown prince"),
    ("MIDEAST", "CONFLICT", "Israeli tanks quit central Gaza; families return"),
    ("MIDEAST", "CONFLICT", "Iraq compromises with Kataib Hezbollah"),
    ("MIDEAST", "CONFLICT", "Houthis push toward Aden; shipping is warned"),
    ("MIDEAST", "CONFLICT", "Israel strikes a Hezbollah bunker in the Bekaa"),
    ("MIDEAST", "ENERGY", "Iran says a tanker hit a mine east of Hormuz"),
    ("MIDEAST", "SANCTIONS", "Trump says Iran may be seeking chemical arms"),

    ("AFRICA", "ECONOMY", "Kenya's milk shortage deepens as drought bites"),
    ("AFRICA", "CONFLICT", "Drone and artillery fire reported near Badme"),
    ("AFRICA", "ECONOMY", "Senegal's parliament rejects the 2027 budget"),
    ("AFRICA", "CONFLICT", "An RSF commander defects to Sudan's army"),
    ("AFRICA", "LAW", "Nigeria moves to decriminalise attempted suicide"),
    ("AFRICA", "DEFENCE", "Kenya takes a 20m-euro EU defence package"),
    ("AFRICA", "JUSTICE", "Six of one family shot dead near Botshabelo"),
    ("AFRICA", "LAW", "Somali Supreme Court defies the president"),
    ("AFRICA", "CONFLICT", "Amnesty seeks war crimes inquiry into RSF drones"),

    ("AMERICAS", "DISASTER", "Third day of floods shuts South Florida roads"),
    ("AMERICAS", "MARKETS", "The Mexican peso slips past 19 to the dollar"),
    ("AMERICAS", "DIPLOMACY", "Report: US official floated ceding Guyana land"),
    ("AMERICAS", "POLITICS", "Canada's Liberal budget passes the Commons"),

    ("OCEANIA", "SOCIETY", "A priest is murdered in Papua New Guinea"),

    ("WORLD", "CLIMATE", "COP31 draft drops fossil-fuel language; outcry"),
    ("WORLD", "CULTURE", "GTA VI goes on sale after a 13-year wait"),
]

NUMBERS = [("4.9pc", "Australian jobless rate"),
           ("83", "dollars a share: Anthropic's IPO price"),
           ("51-48", "the Senate's Iran war powers vote"),
           ("10,000", "Rohingya the ICJ says were killed")]
