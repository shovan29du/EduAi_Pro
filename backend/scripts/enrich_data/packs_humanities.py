from . import Tab, Case, Pack

PACKS = {
"Philosophy": Pack(
    [Tab("Major ethical theories", ["Theory", "Key thinker", "Core idea"],
         ["Consequentialism", "Bentham, Mill", "Right acts maximise good outcomes"], ["Deontology", "Kant", "Right acts follow duties and universal rules"],
         ["Virtue ethics", "Aristotle", "Right acts express good character"], ["Contractualism", "Rawls, Scanlon", "Right acts are justifiable to all affected"])],
    [Case("The trolley problem", "1967", "Philippa Foot posed a dilemma about diverting a runaway trolley; it became a standard test of consequentialist and deontological intuitions.", "Thought experiments isolate moral principles.", "Trolley problem"),
     Case("Popper and falsifiability", "1934", "Karl Popper argued that scientific theories must be falsifiable, contrasting Einstein's risky predictions with unfalsifiable doctrines.", "A theory that forbids nothing explains nothing.", "Karl Popper"),
     Case("Kuhn's paradigm shifts", "1962", "Thomas Kuhn's Structure of Scientific Revolutions described science as long periods of normal science punctuated by paradigm shifts.", "Scientific change is social as well as logical.", "The Structure of Scientific Revolutions")]),
"Art History": Pack(
    [Tab("Western art movements", ["Movement", "Period", "Example artist"],
         ["Renaissance", "14th–16th c.", "Leonardo da Vinci"], ["Baroque", "17th c.", "Caravaggio"], ["Impressionism", "1860s–1880s", "Claude Monet"],
         ["Cubism", "1907–1920s", "Pablo Picasso"], ["Abstract Expressionism", "1940s–1950s", "Jackson Pollock"])],
    [Case("Han van Meegeren forgeries", "1930s–1945", "Van Meegeren sold fake Vermeers, including one to Hermann Göring, and was exposed in 1945 after his own confession.", "Provenance and scientific analysis expose forgeries.", "Han van Meegeren"),
     Case("Theft of the Mona Lisa", "21 August 1911", "Vincenzo Peruggia stole the painting from the Louvre; it was recovered in 1913, and the publicity made it world famous.", "Fame can be made by loss.", "Theft of the Mona Lisa"),
     Case("Restoring the Sistine Chapel", "1980–1994", "A restoration removed centuries of soot and revealed Michelangelo's vivid colours, sparking debate about conservation.", "Conservation choices reshape how we see art.", "Sistine Chapel")]),
"Art": Pack(
    [Tab("Colour wheel relationships", ["Scheme", "Description"],
         ["Complementary", "Opposite hues, e.g. blue and orange"], ["Analogous", "Neighbouring hues"], ["Triadic", "Three evenly spaced hues"], ["Monochromatic", "One hue in different tints and shades"])],
    [Case("Picasso's Guernica", "1937", "Picasso painted a huge anti-war canvas after the bombing of the Basque town of Guernica.", "Art can respond to current events.", "Guernica (Picasso)"),
     Case("Duchamp's Fountain", "1917", "Marcel Duchamp submitted a signed urinal to an exhibition, asking what counts as art.", "Context and idea can define a work.", "Fountain (Duchamp)"),
     Case("Banksy's shredded painting", "5 October 2018", "Girl with Balloon self-shredded moments after selling at Sotheby's for about £1 million, and was renamed Love is in the Bin.", "Destruction can add to an artwork's value.", "Love Is in the Bin")]),
"Music": Pack(
    [Tab("Interval frequency ratios (just intonation)", ["Interval", "Ratio"],
         ["Octave", "2 : 1"], ["Perfect fifth", "3 : 2"], ["Perfect fourth", "4 : 3"], ["Major third", "5 : 4"])],
    [Case("The Rite of Spring premiere", "29 May 1913", "Stravinsky's score and Nijinsky's choreography provoked uproar at the Paris premiere.", "Radical works can shock before they are accepted.", "The Rite of Spring"),
     Case("Beethoven's Ninth Symphony", "7 May 1824", "Beethoven, almost entirely deaf, premiered a symphony adding a choir; its 'Ode to Joy' became the anthem of Europe.", "Creativity can outlast physical limits.", "Symphony No. 9 (Beethoven)"),
     Case("Napster", "1999–2001", "A peer-to-peer file-sharing service disrupted the music industry and led to legal streaming.", "Technology reshapes how music is distributed and paid for.", "Napster")]),
"English": Pack(
    [Tab("Figures of speech", ["Device", "Example"],
         ["Metaphor", "Time is a thief"], ["Simile", "As brave as a lion"], ["Hyperbole", "I've told you a million times"], ["Irony", "A fire station burns down"], ["Alliteration", "Peter Piper picked"])],
    [Case("Orwell's Politics and the English Language", "1946", "George Orwell argued vague, inflated language hides thought and enables political deceit.", "Clear writing is a civic skill.", "Politics and the English Language"),
     Case("The Oxford English Dictionary", "1857–1928", "A volunteer-driven project catalogued English words with historical quotations; its first edition was completed in 1928.", "Crowdsourcing can build great reference works.", "Oxford English Dictionary"),
     Case("Shakespeare's First Folio", "1623", "Two actors collected 36 of Shakespeare's plays; half of them might otherwise have been lost.", "Preservation shapes the canon.", "First Folio")]),
"World Literature": Pack(
    [Tab("Landmark works", ["Work", "Author", "Region and era"],
         ["Epic of Gilgamesh", "Anonymous", "Mesopotamia, c. 2100–1200 BCE"], ["The Tale of Genji", "Murasaki Shikibu", "Japan, c. 1010"],
         ["Don Quixote", "Miguel de Cervantes", "Spain, 1605 and 1615"], ["Things Fall Apart", "Chinua Achebe", "Nigeria, 1958"], ["One Hundred Years of Solitude", "Gabriel García Márquez", "Colombia, 1967"])],
    [Case("Salman Rushdie's The Satanic Verses", "1988–1989", "The novel prompted a fatwa calling for the author's death, sparking global debate on free expression.", "Literature can become a flashpoint for politics and religion.", "The Satanic Verses"),
     Case("Nobel Prize to Bob Dylan", "2016", "The Nobel Committee honoured Bob Dylan 'for having created new poetic expressions within the great American song tradition'.", "The boundaries of literature are debated.", "Bob Dylan"),
     Case("Translation of Gilgamesh", "1872", "George Smith's reading of a clay tablet revealed a Babylonian flood story older than the Bible's.", "Rediscovered texts can rewrite literary history.", "Epic of Gilgamesh")]),
"Foreign Languages": Pack(
    [Tab("CEFR levels", ["Level", "Description"],
         ["A1–A2", "Basic user"], ["B1–B2", "Independent user"], ["C1–C2", "Proficient user"])],
    [Case("Deciphering the Rosetta Stone", "1799–1822", "A decree in Greek, Demotic and hieroglyphs let Jean-François Champollion decipher hieroglyphs in 1822.", "Parallel texts unlock lost languages.", "Rosetta Stone"),
     Case("Revival of Hebrew", "Late 19th–20th century", "Eliezer Ben-Yehuda and others revived Hebrew as a spoken language.", "A language can be revived by community and institutions.", "Revival of the Hebrew language"),
     Case("Navajo code talkers", "1942–1945", "US Marines used the Navajo language as an unbroken code in the Pacific.", "Languages carry cultural and strategic value.", "Code talker")]),
"World History": Pack(
    [Tab("Turning points", ["Event", "Date"],
         ["Agricultural revolution begins", "c. 10,000 BCE"], ["Fall of the Western Roman Empire", "476 CE"], ["Printing press with movable type in Europe", "c. 1450"],
         ["French Revolution", "1789"], ["End of the Second World War", "1945"])],
    [Case("The Black Death", "1347–1351", "Plague killed an estimated third or more of Europe's population, raising wages and reshaping society.", "Demographic shocks transform economies.", "Black Death"),
     Case("The Columbian Exchange", "1492 onward", "Transfers of crops, animals and diseases between the Americas and Eurasia transformed diets and populations worldwide.", "Trade carries both benefits and catastrophe.", "Columbian exchange"),
     Case("The Industrial Revolution", "c. 1760–1840", "Steam power and factories began in Britain and transformed production, cities and living standards.", "Technology changes society in uneven ways.", "Industrial Revolution")]),
"Islamic Studies": Pack(
    [Tab("Five Pillars of Islam", ["Pillar", "Meaning"],
         ["Shahada", "Declaration of faith"], ["Salah", "Five daily prayers"], ["Zakat", "Obligatory charity"], ["Sawm", "Fasting in Ramadan"], ["Hajj", "Pilgrimage to Mecca once, if able"])],
    [Case("The Hijra", "622 CE", "The Prophet Muhammad's migration from Mecca to Medina marks the start of the Islamic calendar.", "A defining event shapes how time itself is counted.", "Hijrah"),
     Case("The House of Wisdom", "9th century", "Scholars in Baghdad translated Greek, Persian and Indian works, and al-Khwarizmi's book gave algebra its name.", "Translation and patronage drove a scientific golden age.", "House of Wisdom"),
     Case("Al-Azhar University", "970–972 CE", "Founded in Cairo, it is among the oldest continuously operating universities.", "Institutions preserve and transmit learning.", "Al-Azhar University")]),
"World Religions": Pack(
    [Tab("Share of world population, 2020 (Pew Research Center estimates)", ["Group", "Share"],
         ["Christians", "≈ 28.8%"], ["Muslims", "≈ 25.6%"], ["Religiously unaffiliated", "≈ 24.2%"], ["Hindus", "≈ 14.9%"], ["Buddhists", "≈ 4.1%"])],
    [Case("Ashoka's conversion", "c. 260 BCE", "After the bloody Kalinga war, Emperor Ashoka embraced Buddhism and promoted non-violence and tolerance.", "Religion can shape statecraft.", "Ashoka"),
     Case("The Protestant Reformation", "1517", "Martin Luther's Ninety-five Theses, spread by the printing press, split Western Christianity.", "Technology amplifies religious change.", "Reformation"),
     Case("Parliament of the World's Religions", "1893", "A Chicago gathering brought Eastern and Western religious leaders together, including Swami Vivekananda.", "Interfaith dialogue has a long history.", "Parliament of the World's Religions")]),
"Mythology": Pack(
    [Tab("Pantheon comparison", ["Domain", "Greek", "Roman", "Norse"],
         ["Sky and thunder", "Zeus", "Jupiter", "Thor"], ["Sea", "Poseidon", "Neptune", "Njord"], ["War", "Ares", "Mars", "Tyr"], ["Wisdom", "Athena", "Minerva", "Odin"])],
    [Case("Schliemann at Troy", "1870s", "Heinrich Schliemann excavated Hisarlik, convinced it was Homer's Troy, finding rich layers though dating and methods were contested.", "Myth and archaeology can inform each other.", "Troy"),
     Case("Joseph Campbell and Star Wars", "1977", "George Lucas cited Campbell's monomyth as an influence on Star Wars.", "Ancient story patterns survive in modern film.", "The Hero with a Thousand Faces"),
     Case("The Grimms' collection", "1812", "The Brothers Grimm collected German folktales, helping make folklore a field of study.", "Collecting oral stories preserves culture.", "Brothers Grimm")]),
}
