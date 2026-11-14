#!/usr/bin/env python3
"""Append 100 real, well-known world-cinema entries to backend/data/movies.json.

The existing library skews family/animation; this batch fills in acclaimed
adult and mature-themed cinema from around the world so the platform is no
longer positioned as children-only. age_group ranges from "13+" to "18+"
for mature titles -- nothing here is restricted from adult users, but the
age_group tag is kept so the UI can still filter for younger learners who
want it.

Re-run after editing:
    python3 backend/scripts/generate_movies_expansion.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MOVIES_PATH = BASE_DIR / "data" / "movies.json"


def yt(query: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(query)


# (title, year, country, language, genres, age_group, director, description)
MOVIES = [
    ("The Godfather", 1972, "USA", "English", ["Crime", "Drama"], "16+", "Francis Ford Coppola", "The patriarch of an organized crime dynasty transfers control to his reluctant son. A landmark of American cinema."),
    ("Schindler's List", 1993, "USA", "English", ["Drama", "History", "War"], "16+", "Steven Spielberg", "A German businessman saves over a thousand Jewish refugees during the Holocaust. A profound historical drama."),
    ("Pulp Fiction", 1994, "USA", "English", ["Crime", "Drama"], "18+", "Quentin Tarantino", "Interwoven stories of crime and redemption in Los Angeles, told in a nonlinear structure."),
    ("A Clockwork Orange", 1971, "UK", "English", ["Crime", "Drama", "Sci-Fi"], "18+", "Stanley Kubrick", "A dystopian tale exploring free will, violence, and state control. Frequently studied in film and ethics courses."),
    ("Seven Samurai", 1954, "Japan", "Japanese", ["Action", "Drama"], "13+", "Akira Kurosawa", "A village hires seven samurai to defend against bandits. One of the most influential films ever made."),
    ("Rashomon", 1950, "Japan", "Japanese", ["Drama", "Mystery"], "13+", "Akira Kurosawa", "A crime is recounted by four witnesses in contradictory ways, exploring truth and subjectivity."),
    ("City of God", 2002, "Brazil", "Portuguese", ["Crime", "Drama"], "18+", "Fernando Meirelles", "Two boys growing up in a Rio de Janeiro favela take different paths, one into crime and one into photography."),
    ("Oldboy", 2003, "South Korea", "Korean", ["Thriller", "Drama"], "18+", "Park Chan-wook", "A man seeks revenge after being mysteriously imprisoned for 15 years. A landmark of Korean cinema."),
    ("Parasite", 2019, "South Korea", "Korean", ["Thriller", "Drama", "Comedy"], "16+", "Bong Joon-ho", "A poor family schemes to become employed by a wealthy household, exposing deep class divides. Academy Award winner for Best Picture."),
    ("Amélie", 2001, "France", "French", ["Comedy", "Romance"], "13+", "Jean-Pierre Jeunet", "A shy Parisian waitress decides to change the lives of those around her for the better."),
    ("La Haine", 1995, "France", "French", ["Drama"], "16+", "Mathieu Kassovitz", "Three friends in the Paris banlieues navigate the aftermath of a police-related riot. A landmark social-realist film."),
    ("Cinema Paradiso", 1988, "Italy", "Italian", ["Drama", "Romance"], "13+", "Giuseppe Tornatore", "A filmmaker recalls his childhood friendship with a small-town cinema projectionist."),
    ("La Dolce Vita", 1960, "Italy", "Italian", ["Drama"], "16+", "Federico Fellini", "A journalist drifts through Rome's high society in search of meaning. A defining work of European art cinema."),
    ("Wild Strawberries", 1957, "Sweden", "Swedish", ["Drama"], "13+", "Ingmar Bergman", "An elderly professor reflects on his life during a road trip, confronting regret and mortality."),
    ("The Seventh Seal", 1957, "Sweden", "Swedish", ["Drama", "Fantasy"], "13+", "Ingmar Bergman", "A knight returning from the Crusades plays chess with Death, questioning faith and mortality."),
    ("Pan's Labyrinth", 2006, "Mexico", "Spanish", ["Fantasy", "Drama", "War"], "16+", "Guillermo del Toro", "A young girl escapes into a dark fantasy world during the Spanish Civil War."),
    ("Amores Perros", 2000, "Mexico", "Spanish", ["Drama"], "18+", "Alejandro G. Iñárritu", "Three interconnected stories in Mexico City converge around a car crash."),
    ("Y Tu Mamá También", 2001, "Mexico", "Spanish", ["Drama"], "18+", "Alfonso Cuarón", "Two teenage boys and an older woman take a road trip across Mexico, exploring friendship and mortality."),
    ("Pather Panchali", 1955, "India", "Bengali", ["Drama"], "13+", "Satyajit Ray", "A poor family in rural Bengal endures hardship and small joys. The first film of the acclaimed Apu Trilogy."),
    ("Lagaan", 2001, "India", "Hindi", ["Drama", "Musical", "Sport"], "13+", "Ashutosh Gowariker", "Villagers under British colonial rule wager their taxes on a cricket match to win their freedom from an unjust tax."),
    ("Dangal", 2016, "India", "Hindi", ["Biography", "Drama", "Sport"], "13+", "Nitesh Tiwari", "A former wrestler trains his daughters to become India's first world-class female wrestlers."),
    ("A Separation", 2011, "Iran", "Persian", ["Drama"], "13+", "Asghar Farhadi", "A married couple's separation entangles their families in a moral and legal dilemma. Academy Award winner."),
    ("The Salesman", 2016, "Iran", "Persian", ["Drama"], "16+", "Asghar Farhadi", "A couple's production of a play is upended by a violent incident, testing their marriage."),
    ("Children of Heaven", 1997, "Iran", "Persian", ["Drama", "Family"], "6+", "Majid Majidi", "A brother and sister share one pair of shoes after losing the other, in a gentle story of sibling love."),
    ("Wings of Desire", 1987, "Germany", "German", ["Drama", "Fantasy"], "13+", "Wim Wenders", "An angel watching over divided Berlin longs to experience human life."),
    ("Das Boot", 1981, "Germany", "German", ["War", "Drama"], "16+", "Wolfgang Petersen", "The claustrophobic, tense life aboard a German U-boat during World War II."),
    ("Run Lola Run", 1998, "Germany", "German", ["Thriller"], "13+", "Tom Tykwer", "A woman has twenty minutes to find money to save her boyfriend's life, told across three parallel timelines."),
    ("Ida", 2013, "Poland", "Polish", ["Drama"], "13+", "Paweł Pawlikowski", "A young novice nun in 1960s Poland discovers a family secret from the Holocaust before taking her vows."),
    ("Man of Iron", 1981, "Poland", "Polish", ["Drama"], "13+", "Andrzej Wajda", "A journalist investigates a strike leader during Poland's Solidarity movement."),
    ("Battleship Potemkin", 1925, "Russia", "Russian", ["Drama", "History"], "13+", "Sergei Eisenstein", "A dramatization of the 1905 mutiny aboard a Russian battleship, famous for its pioneering editing techniques."),
    ("Andrei Rublev", 1966, "Russia", "Russian", ["Drama", "History"], "16+", "Andrei Tarkovsky", "An episodic portrait of a medieval Russian icon painter navigating faith and violence."),
    ("Come and See", 1985, "Russia", "Russian", ["War", "Drama"], "18+", "Elem Klimov", "A boy witnesses the horrors of the Nazi occupation of Belarus. Considered one of the most powerful anti-war films ever made."),
    ("Volver", 2006, "Spain", "Spanish", ["Drama", "Comedy"], "13+", "Pedro Almodóvar", "Three generations of women in La Mancha confront secrets, death, and forgiveness."),
    ("Talk to Her", 2002, "Spain", "Spanish", ["Drama"], "16+", "Pedro Almodóvar", "Two men form an unlikely friendship while caring for women in comas."),
    ("Trainspotting", 1996, "UK", "English", ["Drama", "Comedy"], "18+", "Danny Boyle", "A group of friends in Edinburgh navigate heroin addiction, poverty, and their attempts to escape it."),
    ("The Full Monty", 1997, "UK", "English", ["Comedy", "Drama"], "16+", "Peter Cattaneo", "Unemployed steelworkers in Sheffield form a striptease act to make ends meet."),
    ("Rabbit-Proof Fence", 2002, "Australia", "English", ["Drama", "History"], "13+", "Phillip Noyce", "Three Aboriginal Australian girls escape a government camp and walk 1,500 miles home, based on real events of the Stolen Generations."),
    ("Samson and Delilah", 2009, "Australia", "English", ["Drama", "Romance"], "16+", "Warwick Thornton", "Two Aboriginal teenagers in a remote community face hardship and form a bond of survival."),
    ("Yi Yi", 2000, "Taiwan", "Mandarin", ["Drama"], "13+", "Edward Yang", "A Taipei family navigates midlife crisis, first love, and mortality across three generations."),
    ("Farewell My Concubine", 1993, "China", "Mandarin", ["Drama", "History"], "16+", "Chen Kaige", "Two Peking Opera performers' lives are shaped by decades of political upheaval in 20th-century China."),
    ("In the Mood for Love", 2000, "Hong Kong", "Cantonese", ["Drama", "Romance"], "13+", "Wong Kar-wai", "Two neighbors form a close bond after realizing their spouses are having an affair with each other."),
    ("Infernal Affairs", 2002, "Hong Kong", "Cantonese", ["Crime", "Thriller"], "16+", "Andrew Lau, Alan Mak", "An undercover cop and a mole in the police force race to expose each other."),
    ("Tsotsi", 2005, "South Africa", "Zulu/English", ["Drama", "Crime"], "16+", "Gavin Hood", "A young Johannesburg gang leader's life changes after he unwittingly steals a car with a baby inside."),
    ("Yesterday", 2004, "South Africa", "Zulu", ["Drama"], "13+", "Darrell Roodt", "A Zulu woman diagnosed with HIV fights to live long enough to see her daughter start school."),
    ("Moolaadé", 2004, "Senegal", "Wolof/French", ["Drama"], "16+", "Ousmane Sembène", "A woman in a West African village shelters girls fleeing forced genital cutting, defying tradition."),
    ("Timbuktu", 2014, "Mauritania", "Arabic/French", ["Drama"], "13+", "Abderrahmane Sissako", "A family's peaceful life is upended by the arrival of jihadist occupiers in northern Mali."),
    ("The Battle of Algiers", 1966, "Algeria", "Arabic/French", ["War", "Drama", "History"], "16+", "Gillo Pontecorvo", "A docudrama recreation of the Algerian struggle for independence from French colonial rule."),
    ("Cairo Station", 1958, "Egypt", "Arabic", ["Drama"], "13+", "Youssef Chahine", "A disabled newspaper vendor's obsession turns to tragedy at Cairo's central train station."),
    ("The Yacoubian Building", 2006, "Egypt", "Arabic", ["Drama"], "18+", "Marwan Hamed", "Interwoven stories of residents in a historic Cairo apartment building reflect on modern Egyptian society."),
    ("Central Station", 1998, "Brazil", "Portuguese", ["Drama"], "13+", "Walter Salles", "A retired teacher helps a boy search for his father across Brazil after his mother's death."),
    ("The Secret in Their Eyes", 2009, "Argentina", "Spanish", ["Crime", "Drama", "Romance"], "16+", "Juan José Campanella", "A retired legal counselor revisits an unsolved murder case from decades earlier. Academy Award winner."),
    ("Wild Tales", 2014, "Argentina", "Spanish", ["Comedy", "Drama"], "16+", "Damián Szifron", "Six standalone stories explore revenge and the snapping point of ordinary people."),
    ("The Death of Mr. Lazarescu", 2005, "Romania", "Romanian", ["Drama"], "16+", "Cristi Puiu", "An elderly man is shuttled between hospitals over one long night, a stark look at a failing healthcare system."),
    ("4 Months, 3 Weeks and 2 Days", 2007, "Romania", "Romanian", ["Drama"], "18+", "Cristian Mungiu", "Two university students navigate the dangers of an illegal abortion in 1980s communist Romania."),
    ("Loveless", 2017, "Russia", "Russian", ["Drama"], "16+", "Andrey Zvyagintsev", "A divorcing couple's son disappears, exposing the emotional coldness at the heart of their family."),
    ("Roma", 2018, "Mexico", "Spanish", ["Drama"], "13+", "Alfonso Cuarón", "A year in the life of a domestic worker for a middle-class family in 1970s Mexico City."),
    ("The Handmaiden", 2016, "South Korea", "Korean/Japanese", ["Thriller", "Romance"], "18+", "Park Chan-wook", "A con artist and a Japanese heiress's relationship takes unexpected turns in colonial-era Korea."),
    ("Burning", 2018, "South Korea", "Korean", ["Mystery", "Drama"], "16+", "Lee Chang-dong", "A young man's life becomes entangled with a woman and a mysterious wealthy stranger."),
    ("Spirited Away", 2001, "Japan", "Japanese", ["Fantasy", "Animation"], "6+", "Hayao Miyazaki", "A girl must work in a bathhouse for spirits to save her parents, already featured elsewhere in this library."),
    ("Grave of the Fireflies", 1988, "Japan", "Japanese", ["Animation", "War", "Drama"], "13+", "Isao Takahata", "Two siblings struggle to survive in Japan during the final months of World War II."),
    ("Tokyo Story", 1953, "Japan", "Japanese", ["Drama"], "13+", "Yasujirō Ozu", "An elderly couple visits their grown children in Tokyo and finds them too busy to spend time together."),
    ("Ugetsu", 1953, "Japan", "Japanese", ["Drama", "Fantasy"], "13+", "Kenji Mizoguchi", "Two peasants pursue wealth and glory during a civil war, with supernatural consequences."),
    ("The Battle of Chile", 1975, "Chile", "Spanish", ["Documentary", "History"], "16+", "Patricio Guzmán", "A documentary chronicling the political turmoil leading to the 1973 Chilean coup."),
    ("No", 2012, "Chile", "Spanish", ["Drama", "History"], "13+", "Pablo Larraín", "An advertising executive runs the campaign to vote 'No' in Chile's 1988 plebiscite on Pinochet's rule."),
    ("City Lights", 1931, "USA", "Silent/English", ["Comedy", "Drama", "Romance"], "6+", "Charlie Chaplin", "The Tramp falls in love with a blind flower girl and works to pay for an operation to restore her sight."),
    ("Sunset Boulevard", 1950, "USA", "English", ["Drama", "Noir"], "13+", "Billy Wilder", "A faded silent-film star lures a struggling screenwriter into her decaying Hollywood mansion."),
    ("12 Angry Men", 1957, "USA", "English", ["Drama"], "10+", "Sidney Lumet", "A single juror's doubt forces eleven others to reconsider a seemingly open-and-shut murder case."),
    ("Dr. Strangelove", 1964, "USA", "English", ["Comedy", "War"], "13+", "Stanley Kubrick", "A satirical look at Cold War nuclear paranoia as a rogue general triggers a doomsday scenario."),
    ("One Flew Over the Cuckoo's Nest", 1975, "USA", "English", ["Drama"], "16+", "Miloš Forman", "A rebellious patient clashes with a tyrannical nurse in a mental institution."),
    ("Do the Right Thing", 1989, "USA", "English", ["Drama", "Comedy"], "16+", "Spike Lee", "Racial tensions boil over on the hottest day of the summer in a Brooklyn neighborhood."),
    ("Moonlight", 2016, "USA", "English", ["Drama"], "16+", "Barry Jenkins", "A young Black man's identity and sexuality are explored across three chapters of his life. Academy Award for Best Picture."),
    ("Get Out", 2017, "USA", "English", ["Horror", "Thriller"], "16+", "Jordan Peele", "A young Black man uncovers a disturbing secret when he visits his white girlfriend's family estate."),
    ("Whiplash", 2014, "USA", "English", ["Drama", "Music"], "13+", "Damien Chazelle", "A young drummer is pushed to his limits by an abusive, perfectionist music instructor."),
    ("Requiem for a Dream", 2000, "USA", "English", ["Drama"], "18+", "Darren Aronofsky", "Four people's lives spiral into addiction, told with unflinching intensity. A frequently studied cautionary drama."),
    ("Boyhood", 2014, "USA", "English", ["Drama"], "13+", "Richard Linklater", "Filmed over twelve years, following a boy's growth from age six to eighteen."),
    ("There Will Be Blood", 2007, "USA", "English", ["Drama"], "16+", "Paul Thomas Anderson", "An oil prospector's ambition and greed consume his relationships in early 20th-century California."),
    ("No Country for Old Men", 2007, "USA", "English", ["Crime", "Thriller"], "16+", "Joel and Ethan Coen", "A hunter stumbles onto a drug deal gone wrong and is pursued by a relentless killer."),
    ("Life Is Beautiful", 1997, "Italy", "Italian", ["Comedy", "Drama", "War"], "13+", "Roberto Benigni", "A father uses humor and imagination to shield his son from the horrors of a Nazi concentration camp."),
    ("Persepolis", 2007, "France/Iran", "French/Persian", ["Animation", "Drama", "History"], "13+", "Marjane Satrapi, Vincent Paronnaud", "An animated memoir of growing up in Iran during and after the Islamic Revolution."),
    ("The Intouchables", 2011, "France", "French", ["Comedy", "Drama"], "13+", "Olivier Nakache, Éric Toledano", "A wealthy quadriplegic man hires a caregiver from the projects, forming an unlikely friendship."),
    ("Amour", 2012, "France/Austria", "French", ["Drama"], "16+", "Michael Haneke", "An elderly couple's devotion is tested as one partner's health declines. Academy Award winner for Best Foreign Language Film."),
    ("The Lives of Others", 2006, "Germany", "German", ["Drama", "Thriller"], "13+", "Florian Henckel von Donnersmarck", "An East German secret police officer surveils a playwright and is transformed by what he observes."),
    ("Downfall", 2004, "Germany", "German", ["War", "Drama", "History"], "16+", "Oliver Hirschbiegel", "A dramatization of Hitler's final days in the Berlin bunker, told partly through his secretary's eyes."),
    ("Metropolis", 1927, "Germany", "Silent/German", ["Sci-Fi", "Drama"], "10+", "Fritz Lang", "A pioneering silent science-fiction film depicting a divided futuristic city of workers and elites."),
    ("Nosferatu", 1922, "Germany", "Silent/German", ["Horror"], "13+", "F. W. Murnau", "An unauthorized but hugely influential silent adaptation of Dracula, foundational to horror cinema."),
    ("The Lunchbox", 2013, "India", "Hindi", ["Drama", "Romance"], "10+", "Ritesh Batra", "A misdelivered lunchbox connects a lonely housewife and a widower approaching retirement in Mumbai."),
    ("Gangs of Wasseypur", 2012, "India", "Hindi", ["Crime", "Drama"], "18+", "Anurag Kashyap", "A multi-generational saga of coal-mafia rivalry and revenge in Jharkhand, India."),
    ("Bicycle Thieves", 1948, "Italy", "Italian", ["Drama"], "10+", "Vittorio De Sica", "A father and son search post-war Rome for a stolen bicycle needed for the father's job. A cornerstone of Italian neorealism."),
    ("Rome, Open City", 1945, "Italy", "Italian", ["Drama", "War"], "13+", "Roberto Rossellini", "Resistance fighters and civilians navigate Nazi-occupied Rome near the end of World War II."),
    ("Ashes and Diamonds", 1958, "Poland", "Polish", ["Drama", "War"], "13+", "Andrzej Wajda", "A young resistance fighter is assigned one last assassination on the final day of World War II in Poland."),
    ("Waltz with Bashir", 2008, "Israel", "Hebrew", ["Animation", "War", "Documentary"], "16+", "Ari Folman", "An animated documentary in which a veteran pieces together his suppressed memories of the 1982 Lebanon War."),
    ("Footnote", 2011, "Israel", "Hebrew", ["Drama", "Comedy"], "13+", "Joseph Cedar", "A father and son, both Talmudic scholars, are caught in a rivalry over the same prestigious prize."),
    ("Wadjda", 2012, "Saudi Arabia", "Arabic", ["Drama"], "10+", "Haifaa al-Mansour", "A young Saudi girl schemes to buy a bicycle in a society that discourages girls from riding one. The first feature film shot entirely in Saudi Arabia."),
    ("Capernaum", 2018, "Lebanon", "Arabic", ["Drama"], "16+", "Nadine Labaki", "A boy sues his parents for giving him life, in a searing look at poverty and neglect in Beirut."),
    ("Theeb", 2014, "Jordan", "Arabic", ["Drama", "Adventure"], "13+", "Naji Abu Nowar", "A young Bedouin boy guides a British officer across the desert during the Arab Revolt of World War I."),
    ("Nowhere in Africa", 2001, "Germany/Kenya", "German/Swahili", ["Drama"], "13+", "Caroline Link", "A Jewish family flees Nazi Germany for a new life on a Kenyan farm."),
    ("Rafiki", 2018, "Kenya", "Swahili/English", ["Drama", "Romance"], "16+", "Wanuri Kahiu", "Two young women's friendship blossoms into romance despite their families' rivalry and social pressure."),
    ("Sarafina!", 1992, "South Africa", "English/Zulu", ["Drama", "Musical", "History"], "13+", "Darrell Roodt", "A teenage girl in Soweto is swept into the 1976 student uprisings against apartheid education."),
    ("Hotel Rwanda", 2004, "Rwanda", "English/French", ["Drama", "History"], "16+", "Terry George", "A hotel manager shelters over a thousand refugees during the Rwandan genocide."),
    ("The Wave", 2015, "Norway", "Norwegian", ["Thriller", "Disaster"], "13+", "Roar Uthaug", "A geologist races to warn his town of an incoming tsunami triggered by a mountainside collapse."),
    ("Force Majeure", 2014, "Sweden", "Swedish", ["Drama", "Comedy"], "13+", "Ruben Östlund", "A family's dynamics unravel after the father instinctively flees from a controlled avalanche at a ski resort."),
    ("Cría Cuervos", 1976, "Spain", "Spanish", ["Drama"], "13+", "Carlos Saura", "A young girl copes with grief and family secrets in the final years of Franco's Spain."),
    ("The Sea Inside", 2004, "Spain", "Spanish", ["Drama"], "16+", "Alejandro Amenábar", "A quadriplegic man's decades-long campaign for the right to end his life. Academy Award winner."),
    ("Water", 2005, "India/Canada", "Hindi", ["Drama"], "13+", "Deepa Mehta", "Widows confined to an ashram in 1930s India confront tradition, poverty, and hope."),
    ("Monsoon Wedding", 2001, "India", "Hindi/English/Punjabi", ["Comedy", "Drama", "Romance"], "13+", "Mira Nair", "An arranged marriage in Delhi brings a sprawling family together, unearthing joy and long-held secrets."),
]


def build_records() -> list[dict]:
    records = []
    for i, (title, year, country, language, genre, age_group, director, description) in enumerate(MOVIES, start=1):
        slug = "".join(c.lower() if c.isalnum() else "-" for c in title).strip("-")
        while "--" in slug:
            slug = slug.replace("--", "-")
        records.append({
            "id": f"{slug}-{year}",
            "title": title,
            "year": year,
            "country": country,
            "language": language,
            "genre": genre,
            "age_group": age_group,
            "director": director,
            "description": description,
            "watch_url": yt(f"{title} {year} full movie"),
            "source": "Curated world cinema list / YouTube search",
        })
    return records


def main() -> None:
    with open(MOVIES_PATH, encoding="utf-8") as f:
        data = json.load(f)
    existing = data.get("movies", data) if isinstance(data, dict) else data
    existing_ids = {m["id"] for m in existing}

    new_records = [r for r in build_records() if r["id"] not in existing_ids]
    existing.extend(new_records)

    if isinstance(data, dict):
        data["movies"] = existing
    else:
        data = existing

    with open(MOVIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added {len(new_records)} movies. Library now has {len(existing)} movies.")


if __name__ == "__main__":
    main()
