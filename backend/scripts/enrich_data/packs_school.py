"""Subject reference sheets for school Grades 6-10: a simple table and two
real stories per subject, in plain language."""
from . import Tab, Case, Pack

PACKS_SCHOOL = {
"Art": Pack(
    [Tab("Colour mixing", ["Type", "Colours"], ["Primary (paint)", "Red, yellow, blue"], ["Secondary", "Orange (red + yellow), green (yellow + blue), purple (blue + red)"], ["Warm colours", "Reds, oranges, yellows"], ["Cool colours", "Blues, greens, purples"])],
    [Case("The Mona Lisa is stolen", "21 August 1911", "An Italian worker, Vincenzo Peruggia, took the painting from the Louvre in Paris; it was found two years later, and the news made it the most famous painting in the world.", "Fame can come from an unexpected event.", "Theft of the Mona Lisa"),
     Case("The caves of Lascaux", "12 September 1940", "Four teenagers and a dog found a cave in France full of paintings of horses, deer and bulls made about 17,000 years ago.", "People have made art for tens of thousands of years.", "Lascaux")]),
"Biology": Pack(
    [Tab("Levels of organisation in living things", ["Level", "Example"], ["Cell", "A muscle cell"], ["Tissue", "Muscle tissue"], ["Organ", "The heart"], ["Organ system", "The circulatory system"], ["Organism", "A whole person"])],
    [Case("Leeuwenhoek's tiny animals", "1676", "Antonie van Leeuwenhoek, a Dutch cloth merchant, made powerful single-lens microscopes and was the first to see bacteria, which he called 'animalcules'.", "A better tool can reveal a whole new world.", "Antonie van Leeuwenhoek"),
     Case("The shape of DNA", "1953", "James Watson and Francis Crick built a model of DNA as a double helix, using X-ray pictures taken by Rosalind Franklin and Maurice Wilkins.", "Teamwork and data from many scientists led to the discovery.", "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid")]),
"Chemistry": Pack(
    [Tab("The three common states of matter", ["State", "Shape", "Volume", "Particles"], ["Solid", "Fixed", "Fixed", "Packed tightly, vibrate in place"], ["Liquid", "Takes the shape of its container", "Fixed", "Close together, slide past each other"], ["Gas", "Fills its container", "Not fixed", "Far apart, move quickly"])],
    [Case("Mendeleev's periodic table", "1869", "Dmitri Mendeleev arranged the known elements by atomic mass and left gaps for elements not yet discovered; later discoveries, such as gallium and germanium, matched his predictions.", "A good pattern can predict the unknown.", "Dmitri Mendeleev"),
     Case("Marie Curie and radioactivity", "1898", "Marie and Pierre Curie discovered the elements polonium and radium; Marie Curie won Nobel Prizes in both physics (1903) and chemistry (1911).", "Careful, patient work can open a new field of science.", "Marie Curie")]),
"Coding": Pack(
    [Tab("Counting in binary", ["Decimal", "Binary"], ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"], ["8", "1000"], ["10", "1010"])],
    [Case("Ada Lovelace's first program", "1843", "Ada Lovelace wrote a method for Charles Babbage's planned Analytical Engine to calculate Bernoulli numbers, often called the first computer program.", "She saw that machines could work with more than numbers.", "Ada Lovelace"),
     Case("The first computer bug", "9 September 1947", "Operators of the Harvard Mark II found a moth stuck in a relay and taped it into the log book as the 'first actual case of bug being found'.", "Debugging means finding and fixing faults.", "Software bug")]),
"Cooking": Pack(
    [Tab("Safe cooking and storage temperatures", ["Item", "Safe temperature"], ["Chicken and turkey (inside)", "74 °C (165 °F)"], ["Minced meat", "71 °C (160 °F)"], ["Fridge", "4 °C (40 °F) or colder"], ["Freezer", "−18 °C (0 °F) or colder"])],
    [Case("Pasteurisation", "1860s", "Louis Pasteur showed that heating wine and milk gently kills the microbes that spoil them, which made food safer and last longer.", "Heat can make food safe.", "Pasteurization"),
     Case("James Lind and scurvy", "1747", "Ship's doctor James Lind gave different treatments to sailors with scurvy; those who ate oranges and lemons recovered fastest, and later sailors carried citrus to prevent the disease.", "A fair test can show which food helps health.", "James Lind")]),
"Critical Thinking": Pack(
    [Tab("Spotting weak arguments", ["Trick", "What it looks like"], ["Ad hominem", "Attacking the person instead of the idea"], ["Bandwagon", "'Everyone does it, so it must be right'"], ["False choice", "Pretending there are only two options"], ["Hasty generalisation", "Judging all from a few examples"])],
    [Case("The airplane armour puzzle", "1943", "Statistician Abraham Wald realised that armour should go where returning bombers had no bullet holes, because planes hit there never made it home.", "Think about what you are not seeing.", "Abraham Wald"),
     Case("The Great Moon Hoax", "August 1835", "A New York newspaper printed a series of stories claiming an astronomer had seen bat-winged creatures on the Moon; many readers believed them.", "Check the source before you believe a story.", "Great Moon Hoax")]),
"Economics": Pack(
    [Tab("Factors of production", ["Factor", "Meaning", "Example"], ["Land", "Natural resources", "Farmland, oil"], ["Labour", "People's work", "A teacher"], ["Capital", "Tools and machines used to make things", "A tractor"], ["Enterprise", "Taking a risk to start a business", "A shop owner"])],
    [Case("Tulip Mania", "1636–1637", "Prices of tulip bulbs in the Netherlands soared to enormous levels and then collapsed in February 1637, an early example of a speculative bubble.", "Prices can rise far above the real value of something.", "Tulip mania"),
     Case("The Great Depression", "1929–1939", "After the US stock market crash of 1929, banks failed, businesses closed and about a quarter of American workers lost their jobs.", "Economies can fall quickly and take years to recover.", "Great Depression")]),
"English": Pack(
    [Tab("Parts of speech", ["Part", "Job", "Example"], ["Noun", "Names a person, place or thing", "teacher, Cairo"], ["Verb", "Shows action or state", "run, is"], ["Adjective", "Describes a noun", "tall, blue"], ["Adverb", "Describes a verb", "quickly"], ["Conjunction", "Joins words or sentences", "and, but"])],
    [Case("The Gutenberg Bible", "c. 1455", "Johannes Gutenberg printed Bibles using movable metal type, making books faster and cheaper to produce; within fifty years printed books were common across Europe.", "Printing spread reading and ideas.", "Gutenberg Bible"),
     Case("Shakespeare's First Folio", "1623", "Two of Shakespeare's fellow actors collected 36 of his plays into one book, saving about half of them that might otherwise have been lost.", "Books keep stories alive.", "First Folio")]),
"Finance": Pack(
    [Tab("A simple budget (the 50/30/20 guide)", ["Share of income", "Use"], ["About 50%", "Needs: rent, food, transport"], ["About 30%", "Wants: fun, hobbies, treats"], ["About 20%", "Savings and paying off debt"])],
    [Case("The South Sea Bubble", "1720", "Shares in the South Sea Company rose from about £128 to about £1,000 in a few months and then crashed; many investors lost their savings.", "If something sounds too good to be true, be careful.", "South Sea Company"),
     Case("The Grameen Bank", "1983", "Muhammad Yunus started lending very small amounts to poor villagers in Bangladesh, mostly women, so they could start tiny businesses; he won the Nobel Peace Prize in 2006.", "Small loans can help people build a living.", "Grameen Bank")]),
"First Aid": Pack(
    [Tab("DRSABCD: what to do in an emergency", ["Step", "Action"], ["D", "Check for Danger"], ["R", "Check for Response"], ["S", "Send for help (call the emergency number)"], ["A", "Open the Airway"], ["B", "Check Breathing"], ["C", "Start CPR if not breathing normally"], ["D", "Use a Defibrillator (AED) if available"])],
    [Case("The Heimlich manoeuvre", "1974", "Dr Henry Heimlich described abdominal thrusts as a way to clear a blocked airway; the technique is still taught to help people who are choking.", "A simple skill can save a life.", "Heimlich maneuver"),
     Case("Defibrillators in public places", "2000s", "Putting automated defibrillators in airports, stations and sports halls has allowed bystanders to restart hearts in the first minutes after a cardiac arrest.", "Every minute counts, so quick action matters.", "Automated external defibrillator")]),
"Foreign Languages": Pack(
    [Tab("Saying hello", ["Language", "Hello"], ["Spanish", "Hola"], ["French", "Bonjour"], ["Arabic", "Marhaban"], ["Hindi", "Namaste"], ["Japanese", "Konnichiwa"], ["Swahili", "Jambo"])],
    [Case("The Rosetta Stone", "1799–1822", "A stone carved with the same decree in Greek and two Egyptian scripts let Jean-François Champollion work out how to read hieroglyphs in 1822.", "Comparing languages can unlock lost ones.", "Rosetta Stone"),
     Case("The Navajo code talkers", "1942–1945", "United States Marines used the Navajo language as a spoken code in the Pacific during the Second World War, and enemy codebreakers never cracked it.", "Languages carry culture and can protect messages.", "Code talker")]),
"General Knowledge": Pack(
    [Tab("The seven continents", ["Continent", "Fact"], ["Asia", "Largest continent by area and population"], ["Africa", "Second largest; contains the Sahara"], ["North America", "Includes Canada, the USA and Mexico"], ["South America", "Contains the Amazon rainforest"], ["Antarctica", "Coldest, no permanent residents"], ["Europe", "Many small countries"], ["Oceania (Australia)", "Smallest continent"])],
    [Case("The first Moon landing", "20 July 1969", "Neil Armstrong and Buzz Aldrin landed on the Moon in Apollo 11 while Michael Collins stayed in orbit; about 600 million people watched on television.", "Big goals need teamwork.", "Apollo 11"),
     Case("The fall of the Berlin Wall", "9 November 1989", "Crowds crossed from East to West Berlin after the border opened, and Germany became one country again in October 1990.", "Change can come quickly.", "Berlin Wall")]),
"Geography": Pack(
    [Tab("Major climate zones", ["Zone", "Typical weather", "Example"], ["Tropical", "Hot and wet", "Amazon rainforest"], ["Dry", "Little rain", "Sahara Desert"], ["Temperate", "Mild with four seasons", "Western Europe"], ["Cold (continental)", "Long, cold winters", "Siberia"], ["Polar", "Extremely cold", "Antarctica"])],
    [Case("The Aral Sea", "1960s–today", "Rivers feeding the Aral Sea in Central Asia were diverted to irrigate cotton, so the sea shrank to a small fraction of its size.", "Using water in one place can harm another.", "Aral Sea"),
     Case("The Panama Canal", "15 August 1914", "The 82 km canal across Panama let ships sail between the Atlantic and Pacific without going around South America, saving about 13,000 km.", "Engineering can reshape trade routes.", "Panama Canal")]),
"Health Education": Pack(
    [Tab("The main food groups", ["Group", "Main job", "Examples"], ["Carbohydrates", "Energy", "Rice, bread, potatoes"], ["Proteins", "Growth and repair", "Beans, fish, eggs"], ["Fats", "Stored energy, protect organs", "Oils, nuts"], ["Vitamins and minerals", "Keep the body working", "Fruit, vegetables"], ["Water", "Needed for every body process", "Drinking water"])],
    [Case("The end of smallpox", "1980", "After a worldwide vaccination campaign, the World Health Organization announced in 1980 that smallpox, which had killed millions of people, was gone.", "Vaccines and teamwork can wipe out a disease.", "Smallpox"),
     Case("John Snow and the water pump", "1854", "Doctor John Snow marked cholera deaths on a map of London, saw they clustered around one water pump, and persuaded officials to remove its handle.", "Careful observation can protect health.", "1854 Broad Street cholera outbreak")]),
"ICT & Computer Science": Pack(
    [Tab("Units of digital information", ["Unit", "Size"], ["Bit", "A single 0 or 1"], ["Byte", "8 bits (one letter)"], ["Kilobyte (KB)", "About 1,000 bytes"], ["Megabyte (MB)", "About 1,000 KB (a photo)"], ["Gigabyte (GB)", "About 1,000 MB (a film)"])],
    [Case("The first message on the Internet", "29 October 1969", "A student at UCLA tried to send the word 'LOGIN' to a computer at Stanford; the system crashed after the letters 'LO', but the connection worked later that night.", "Big networks start with small steps.", "ARPANET"),
     Case("The first website", "6 August 1991", "Tim Berners-Lee at CERN made the first website public, explaining the World Wide Web project.", "Sharing ideas openly helped the Web grow.", "History of the World Wide Web")]),
"Islamic Studies": Pack(
    [Tab("The Five Pillars of Islam", ["Pillar", "Meaning"], ["Shahada", "Declaration of faith"], ["Salah", "Five daily prayers"], ["Zakat", "Giving to those in need"], ["Sawm", "Fasting during Ramadan"], ["Hajj", "Pilgrimage to Mecca once in a lifetime, if able"])],
    [Case("The Hijra", "622 CE", "The Prophet Muhammad and his followers moved from Mecca to Medina; the Islamic calendar starts from this event.", "An important event can mark the start of a calendar.", "Hijrah"),
     Case("The House of Wisdom", "9th century", "In Baghdad, scholars translated books from Greek, Persian and Indian into Arabic and added their own discoveries in mathematics, astronomy and medicine.", "Sharing knowledge across cultures advances science.", "House of Wisdom")]),
"Math": Pack(
    [Tab("Types of numbers", ["Type", "Examples"], ["Natural numbers", "1, 2, 3, …"], ["Integers", "…, −2, −1, 0, 1, 2, …"], ["Rational numbers", "½, −0.75, 3"], ["Irrational numbers", "π, √2"], ["Real numbers", "All of the above together"])],
    [Case("Euclid's Elements", "c. 300 BCE", "Euclid organised geometry into definitions, rules and step-by-step proofs; his book was used to teach geometry for more than 2,000 years.", "Mathematics is built on clear reasoning.", "Euclid's Elements"),
     Case("Fibonacci brings numbers to Europe", "1202", "Leonardo of Pisa, called Fibonacci, wrote Liber Abaci, which taught Europeans the Hindu–Arabic numerals (0–9) used today.", "Good ideas travel along trade routes.", "Liber Abaci")]),
"Music": Pack(
    [Tab("Instrument families of the orchestra", ["Family", "How sound is made", "Examples"], ["Strings", "Bowing or plucking strings", "Violin, cello, harp"], ["Woodwind", "Blowing across or through a reed", "Flute, clarinet, oboe"], ["Brass", "Buzzing lips into a mouthpiece", "Trumpet, trombone, tuba"], ["Percussion", "Striking or shaking", "Drums, xylophone, cymbals"])],
    [Case("Beethoven's Ninth Symphony", "7 May 1824", "Ludwig van Beethoven, almost completely deaf, took part in the first performance of a symphony with a choir; its 'Ode to Joy' is now the anthem of Europe.", "Creativity can overcome great difficulties.", "Symphony No. 9 (Beethoven)"),
     Case("The Rite of Spring", "29 May 1913", "Stravinsky's new, rhythmic music and dance caused an uproar in the audience at its first performance in Paris, but it is now a classic.", "New art can shock before it is accepted.", "The Rite of Spring")]),
"Philosophy": Pack(
    [Tab("Branches of philosophy", ["Branch", "Asks"], ["Metaphysics", "What is real?"], ["Epistemology", "What can we know?"], ["Ethics", "What is right and wrong?"], ["Logic", "What makes an argument good?"], ["Aesthetics", "What is beauty?"])],
    [Case("The trial of Socrates", "399 BCE", "Athens put the philosopher Socrates on trial for questioning accepted beliefs; he chose to accept the death sentence rather than leave the city.", "Asking hard questions can be risky but valuable.", "Trial of Socrates"),
     Case("The trolley problem", "1967", "Philippa Foot asked whether you should divert a runaway trolley to save five people if it would harm one; it is still used to explore moral choices.", "Thought experiments test our moral ideas.", "Trolley problem")]),
"Physical Education & Self-Defense": Pack(
    [Tab("Components of fitness", ["Component", "Example activity"], ["Aerobic endurance", "Running, swimming"], ["Strength", "Push-ups, weightlifting"], ["Flexibility", "Stretching, yoga"], ["Speed", "Sprinting"], ["Coordination", "Dribbling a ball"])],
    [Case("The four-minute mile", "6 May 1954", "Roger Bannister ran a mile in 3 minutes 59.4 seconds, after many people believed it could not be done; others soon followed.", "Training and belief can break barriers.", "Roger Bannister"),
     Case("Jesse Owens in Berlin", "1936", "Jesse Owens won four gold medals at the Berlin Olympics, in front of a regime that preached racial superiority.", "Sport can challenge prejudice.", "Jesse Owens")]),
"Physics": Pack(
    [Tab("Common SI units", ["Quantity", "Unit", "Symbol"], ["Length", "metre", "m"], ["Mass", "kilogram", "kg"], ["Time", "second", "s"], ["Force", "newton", "N"], ["Energy", "joule", "J"], ["Temperature", "kelvin", "K"])],
    [Case("Galileo's telescope", "1609–1610", "Galileo pointed a telescope at the sky and saw mountains on the Moon and four moons orbiting Jupiter, evidence that not everything circles the Earth.", "Observation can change how we see the universe.", "Galileo Galilei"),
     Case("Hammer and feather on the Moon", "2 August 1971", "Astronaut David Scott dropped a hammer and a feather together on the Moon; with no air, they hit the ground at the same time.", "Without air resistance, all objects fall at the same rate.", "Apollo 15")]),
"Science": Pack(
    [Tab("Steps of the scientific method", ["Step", "What you do"], ["1", "Ask a question"], ["2", "Make a hypothesis"], ["3", "Test it with a fair experiment"], ["4", "Collect and analyse data"], ["5", "Draw a conclusion and share it"])],
    [Case("Pasteur's swan-neck flasks", "1859–1861", "Louis Pasteur boiled broth in flasks with long, curved necks that let air in but kept dust out; the broth stayed clear, showing that germs come from the air, not from nothing.", "A clever experiment can settle a long debate.", "Louis Pasteur"),
     Case("The eclipse that proved Einstein", "29 May 1919", "Arthur Eddington photographed stars near the Sun during a total eclipse; their light was bent as Einstein's theory predicted.", "Scientists test ideas with observations.", "Solar eclipse of May 29, 1919")]),
"Social Studies": Pack(
    [Tab("Three branches of government", ["Branch", "Job"], ["Legislative", "Makes the laws"], ["Executive", "Carries out the laws"], ["Judicial", "Explains the laws and settles disputes"])],
    [Case("Magna Carta", "15 June 1215", "English barons forced King John to agree that even a king must obey the law; the document inspired later ideas of rights and fair trials.", "Leaders are not above the law.", "Magna Carta"),
     Case("Rosa Parks and the bus boycott", "1955–1956", "After Rosa Parks refused to give up her bus seat in Montgomery, Alabama, African Americans boycotted the buses for 381 days until segregated seating was ended.", "Peaceful action can change unfair rules.", "Montgomery bus boycott")]),
"Survival Skills": Pack(
    [Tab("The rule of threes", ["You can survive about…", "Without"], ["3 minutes", "Air"], ["3 hours", "Shelter in harsh weather"], ["3 days", "Water"], ["3 weeks", "Food"])],
    [Case("Shackleton's Endurance expedition", "1914–1917", "When ice crushed his ship near Antarctica, Ernest Shackleton led all 28 men to safety, including a 1,300 km lifeboat journey to South Georgia.", "Good leadership and teamwork help people survive.", "Imperial Trans-Antarctic Expedition"),
     Case("Apollo 13", "April 1970", "After an explosion on the way to the Moon, the crew and engineers on the ground improvised a way to clean the air and return home safely.", "Stay calm and use what you have.", "Apollo 13")]),
"World History": Pack(
    [Tab("Early civilisations", ["Civilisation", "River", "Approximate start"], ["Mesopotamia", "Tigris and Euphrates", "c. 3500 BCE"], ["Ancient Egypt", "Nile", "c. 3100 BCE"], ["Indus Valley", "Indus", "c. 2600 BCE"], ["Ancient China", "Yellow River", "c. 1600 BCE"])],
    [Case("The Black Death", "1347–1351", "A plague spread along trade routes and killed an estimated third or more of Europe's people; with fewer workers, wages rose and old ways of life changed.", "Disease can change societies.", "Black Death"),
     Case("The fall of the Western Roman Empire", "476 CE", "The last Western Roman emperor was removed from power in 476, while the Eastern Roman (Byzantine) Empire lasted until 1453.", "Empires rise and fall.", "Fall of the Western Roman Empire")]),
"World Literature": Pack(
    [Tab("Stories from around the world", ["Work", "Where and when"], ["Epic of Gilgamesh", "Mesopotamia, over 4,000 years ago"], ["The Tale of Genji", "Japan, about 1010"], ["One Thousand and One Nights", "Collected in the Middle East over many centuries"], ["Don Quixote", "Spain, 1605"])],
    [Case("Reading the Epic of Gilgamesh", "1872", "George Smith read a clay tablet in the British Museum and found a flood story much older than the one in the Bible.", "Old stories connect cultures.", "Epic of Gilgamesh"),
     Case("The First Folio", "1623", "Shakespeare's friends printed 36 of his plays in one book, saving many that might have been lost.", "Printing preserves stories.", "First Folio")]),
}
