"""Authored real-world cases used by apply_real_world_examples.py.

Each topic has three real, checkable cases. A lesson's angle (e.g. "Historical
Development") picks the case that fits it best and adds a short prompt telling
the student how to connect the case to that angle.
"""

# Generic angles -> which of the three cases fits best.
#   0 = how it works / practice, 1 = history, rules and institutions, 2 = change, risk and people
GENERIC_ANGLE_CASE = {
    "Foundations and Vocabulary": 0,
    "Core Models and Frameworks": 0,
    "Evidence and Research Methods": 0,
    "Data Interpretation": 0,
    "Professional Practice": 0,
    "Case Study Analysis": 0,
    "Historical Development": 1,
    "Law, Policy and Regulation": 1,
    "Institutions and Governance": 1,
    "Global and Comparative Perspectives": 1,
    "Ethics and Responsibility": 1,
    "Technology and Innovation": 2,
    "Risk and Resilience": 2,
    "Equity and Inclusion": 2,
    "Future Challenges and Solutions": 2,
}

GENERIC_FRAMES = {
    "Foundations and Vocabulary": "list the key terms this case depends on and define each in your own words.",
    "Historical Development": "trace which earlier events or ideas made this case possible.",
    "Core Models and Frameworks": "choose one standard model from this field and use it to explain what happened.",
    "Evidence and Research Methods": "decide what evidence you would need to check the claims made about this case, and where you would find it.",
    "Data Interpretation": "name one number or trend that would show whether this case worked, and say what could mislead you about it.",
    "Ethics and Responsibility": "identify who benefited, who bore the costs, and what duties the people involved had.",
    "Law, Policy and Regulation": "find the rules or laws that shaped what happened and ask whether they worked.",
    "Institutions and Governance": "identify the organisations that made the decisions and who held them to account.",
    "Technology and Innovation": "explain how a new tool or technology changed what was possible here.",
    "Global and Comparative Perspectives": "compare this case with a similar one in another country and explain the differences.",
    "Risk and Resilience": "list what could have gone wrong and what would have made the outcome more resilient.",
    "Equity and Inclusion": "ask who was included or left out, and how the outcome might differ for different groups.",
    "Professional Practice": "describe what a professional in this field would actually do on their first day working on this case.",
    "Case Study Analysis": "write a short case study: the situation, the options considered, the decision and the result.",
    "Future Challenges and Solutions": "predict how this case might look in twenty years and propose one improvement.",
}

CASES = {
    "business_studies": {
        "Strategy": [
            "Netflix began in 1997 renting DVDs by mail, launched streaming in 2007 and later produced its own series such as House of Cards (2013); each step was a deliberate choice about which customers to serve and which capabilities to build.",
            "Kodak invented the first digital camera in 1975 but kept protecting its film business, and it filed for bankruptcy protection in 2012, a standard example of a firm failing to adapt its strategy to a changing industry.",
            "Nokia was the world's largest mobile-phone maker in 2007, but it fell behind after smartphones arrived and sold its phone business to Microsoft in 2014, a case of a market leader overtaken by a change it underestimated.",
        ],
        "Marketing": [
            "Coca-Cola's 'Share a Coke' campaign, which began in Australia in 2011, printed popular first names on bottles, turning a mass-market drink into a personal gift that people photographed and shared.",
            "Apple's 1984 Super Bowl advertisement introduced the Macintosh by showing what the brand stood against rather than listing features, a classic case of positioning.",
            "Dove's 'Real Beauty' campaign, launched in 2004, used everyday women instead of professional models, showing how a brand can tie marketing to a social value, and how such campaigns attract scrutiny.",
        ],
        "Operations": [
            "Toyota's production system, developed after the Second World War, lets any worker stop the line when a defect appears and builds cars just in time, cutting waste and stock.",
            "In 1913 Henry Ford introduced the moving assembly line at his Highland Park plant, dramatically cutting the time needed to build each Model T.",
            "In March 2021 the container ship Ever Given blocked the Suez Canal for about six days, holding up a route that carries around 12 per cent of world trade and showing how fragile global supply chains can be.",
        ],
        "Accounting": [
            "Enron, once one of the largest US companies, collapsed in 2001 after using off-balance-sheet entities to hide debt and inflate profits; the scandal led to the Sarbanes-Oxley Act of 2002.",
            "Luca Pacioli's 1494 book Summa de arithmetica described the double-entry bookkeeping used by Venetian merchants, the method that still underlies company accounts today.",
            "A small cafe owner who records daily sales, supplier costs and rent in a spreadsheet can see which month's cash will run short before the bank balance does, which is why cash flow matters as much as profit.",
        ],
        "Corporate Finance": [
            "When Facebook (now Meta) listed on the stock market in May 2012 it raised about $16 billion by selling shares, an example of a company financing growth with equity instead of debt.",
            "In 2008 the US government rescued the insurer AIG with an $85 billion loan because its failure threatened to spread through the whole financial system.",
            "A family deciding whether to buy solar panels compares the upfront cost with savings over twenty-five years using a discount rate, the same net-present-value logic firms use to choose projects.",
        ],
        "Human Resources": [
            "Google's 'Project Oxygen' studied its own managers and found that coaching and clear communication mattered more than technical skill, which changed how the company trains managers.",
            "Frederick Taylor's 1911 book The Principles of Scientific Management argued for measuring and standardising work, an early step toward modern HR and a lasting source of criticism for treating workers like machines.",
            "When the COVID-19 pandemic began in 2020, many firms moved to remote or hybrid work, forcing HR teams to rethink hiring, performance reviews and employee wellbeing.",
        ],
        "Entrepreneurship": [
            "Muhammad Yunus began lending very small amounts to poor villagers in Bangladesh in the 1970s; the idea grew into Grameen Bank and won him the 2006 Nobel Peace Prize, showing an entrepreneur spotting an unserved market.",
            "Airbnb's founders began in 2007 by renting out air mattresses in their San Francisco apartment during a design conference; the idea later became a global platform.",
            "Because most start-ups fail, entrepreneurs often test a minimum viable product, a basic version offered to real customers, before spending heavily, an approach popularised by the lean start-up method.",
        ],
        "Business Analytics": [
            "Supermarkets use loyalty-card purchase records to predict demand, deciding what to stock and when to offer discounts.",
            "The Netflix Prize (2006-2009) offered $1 million to anyone who could improve its movie-recommendation algorithm, showing the commercial value of prediction from data.",
            "Airlines change ticket prices many times a day using demand forecasts, a practice called revenue management that took off after US airline deregulation in 1978.",
        ],
        "Leadership": [
            "After 27 years in prison, Nelson Mandela led South Africa through the end of apartheid by negotiating with former opponents and creating the Truth and Reconciliation Commission.",
            "Alan Mulally, who became Ford's chief executive in 2006, ran weekly meetings in which managers reported problems using red, yellow and green status colours, helping the company avoid a government bailout in 2009.",
            "After the 2019 Christchurch mosque attacks, New Zealand's prime minister Jacinda Ardern moved quickly to reform gun laws and visibly supported the affected communities.",
        ],
        "International Business": [
            "McDonald's adapts its menu to local tastes, for example the McAloo Tikki burger in India where many customers do not eat beef, while keeping a single global brand.",
            "The North American Free Trade Agreement, in force from 1994, removed most tariffs between the United States, Canada and Mexico and reshaped supply chains such as car manufacturing across all three countries.",
            "Apple designs the iPhone in California but relies on parts and assembly from many countries, so changes in tariffs or exchange rates anywhere along the chain can change its costs.",
        ],
    },
    "civics": {
        "Constitutional Government": [
            "The United States Constitution, signed in 1787, divides power among Congress, the president and the courts so that no single branch can rule alone, a system of checks and balances.",
            "India's Constitution came into force on 26 January 1950; its drafting committee was chaired by B. R. Ambedkar, and it guarantees fundamental rights to every citizen.",
            "South Africa's 1996 Constitution, written after apartheid, contains a Bill of Rights and created a Constitutional Court to protect it.",
        ],
        "Democratic Participation": [
            "In Australia voting in national elections is compulsory, and turnout is typically around 90 per cent, compared with much lower figures in countries where voting is optional.",
            "Women in New Zealand won the right to vote in 1893, the first self-governing country to grant it nationally, while Saudi Arabia first allowed women to vote in local elections in 2015.",
            "Participatory budgeting began in Porto Alegre, Brazil, in 1989, letting residents decide how part of the city budget is spent.",
        ],
        "Human Rights": [
            "The Universal Declaration of Human Rights was adopted by the United Nations General Assembly on 10 December 1948, with Eleanor Roosevelt helping to lead its drafting.",
            "Malala Yousafzai campaigned for girls' education in Pakistan, survived an attack in 2012 and in 2014 became the youngest Nobel Peace Prize winner at 17.",
            "The European Court of Human Rights in Strasbourg hears cases from individuals who believe their rights under the European Convention on Human Rights have been violated.",
        ],
        "Rule of Law": [
            "Magna Carta, sealed by King John in 1215, is an early landmark in the idea that even a ruler is bound by the law.",
            "In Marbury v. Madison (1803) the US Supreme Court established its power to strike down laws that conflict with the Constitution.",
            "In 1974 the US Supreme Court ordered President Nixon to hand over White House tape recordings, and he resigned soon after, showing that no one is above the law.",
        ],
        "Public Policy": [
            "England's 5p charge on single-use plastic bags, introduced in 2015, was followed by a fall of roughly 95 per cent in bags used at the major supermarkets, an example of a small policy changing behaviour.",
            "England's smoke-free law of 2007 banned smoking in enclosed workplaces and public places to protect people from second-hand smoke.",
            "Singapore began charging drivers to enter its central area in 1975 and moved to electronic road pricing in 1998, using price to reduce congestion at busy times.",
        ],
        "Local Government": [
            "A city council decides things residents notice every day, such as bin collection, local roads, parks, libraries and planning permission for new buildings.",
            "Some small Swiss cantons, such as Glarus and Appenzell Innerrhoden, have held open-air citizens' assemblies called Landsgemeinde, a very direct form of local democracy.",
            "London's mayor, directly elected since 2000, has responsibilities for transport, policing and planning across the capital.",
        ],
        "Media and Democracy": [
            "Washington Post reporters investigated the 1972 Watergate break-in, and their reporting helped lead to President Nixon's resignation in 1974, an example of the press holding power to account.",
            "Reporters Without Borders publishes a yearly ranking of press freedom in around 180 countries, which citizens and governments use to compare how freely journalists can work.",
            "False claims can spread faster than corrections on social media, so fact-checking organisations in the International Fact-Checking Network examine viral claims during elections.",
        ],
        "Community Organising": [
            "In 1955-56 Black residents of Montgomery, Alabama, boycotted the city's buses for 381 days after Rosa Parks's arrest, organised through churches and local groups, until bus segregation was ruled unlawful.",
            "Wangari Maathai founded the Green Belt Movement in Kenya in 1977, mobilising women to plant millions of trees, and won the Nobel Peace Prize in 2004.",
            "Neighbours who set up a community garden or food bank follow the same steps as larger campaigns: identify a shared problem, recruit people, set a goal and approach decision-makers.",
        ],
        "Digital Citizenship": [
            "The European Union's General Data Protection Regulation, applying since May 2018, gives people the right to see, and in many cases ask for deletion of, personal data that companies hold about them.",
            "Estonia lets citizens vote in national elections online and use a digital ID for most public services, making it a widely studied example of e-government.",
            "If someone is cyberbullied, they can report it on the platform and to a school or the police; keeping screenshots helps the people who investigate.",
        ],
        "Global Citizenship": [
            "In 2015 all UN member states adopted the 17 Sustainable Development Goals, a shared plan to end poverty and protect the planet by 2030.",
            "The Paris Agreement of 2015 commits countries to keep global warming well below 2 degrees Celsius above pre-industrial levels.",
            "The Red Cross and Red Crescent movement began after Henri Dunant witnessed the battle of Solferino in 1859, and it now helps people in wars and disasters in nearly every country.",
        ],
    },
    "critical_thinking": {
        "Argumentation": [
            "A courtroom is a structured argument: the prosecution claims the accused is guilty and offers evidence as premises, while the defence tries to show the evidence is weak or the reasoning flawed.",
            "Socrates questioned citizens of Athens in the 5th century BCE to expose weak definitions, a method later called Socratic questioning.",
            "In a debate about school start times, a strong argument states a claim (start later), gives a reason (research on teenage sleep) and answers the best objection (bus schedules).",
        ],
        "Deductive Logic": [
            "'All humans are mortal; Socrates is human; therefore Socrates is mortal' is the classic syllogism: if the premises are true, the conclusion must be true.",
            "Euclid's Elements, written around 300 BCE, builds geometry by deducing theorems from a few basic axioms, the model for deductive proof.",
            "A computer program's 'if...then' rules, such as 'if the password is wrong, deny access', apply deductive logic step by step.",
        ],
        "Inductive Reasoning": [
            "For centuries Europeans concluded that all swans are white, until Dutch explorers saw black swans in Western Australia in 1697, a reminder that induction gives probable, not certain, conclusions.",
            "Edward Jenner noticed that milkmaids who had caught cowpox seemed protected from smallpox and tested the idea in 1796, an inductive step from observed cases to a general hypothesis.",
            "Weather forecasters use patterns from past data to say there is a 70 per cent chance of rain; the conclusion is probable, not certain.",
        ],
        "Evidence Evaluation": [
            "A 1998 paper claiming a link between the MMR vaccine and autism was retracted by The Lancet in 2010, and large studies since have found no such link, showing why sample size, method and replication matter.",
            "Cochrane reviews combine the results of many studies on a medical question and grade the quality of the evidence behind each conclusion.",
            "Before sharing a surprising statistic, check who produced it, how they measured it and whether other independent sources report the same.",
        ],
        "Cognitive Bias": [
            "After the 11 September 2001 attacks many Americans chose to drive rather than fly, and researchers estimated that extra road deaths followed, an example of availability bias, where vivid events seem more likely than they are.",
            "Confirmation bias leads people to notice news that supports what they already believe; deliberately reading one reliable source that disagrees is a simple counter.",
            "Anchoring: if a shop shows a jacket as 'was 200, now 120', the first price makes 120 look like a bargain even if the jacket is worth less.",
        ],
        "Media Literacy": [
            "Orson Welles's 1938 radio drama The War of the Worlds was presented as news bulletins and alarmed some listeners who missed that it was fiction.",
            "Professional fact-checkers use 'lateral reading': they leave an article to see what other sources say about the website or author before trusting it.",
            "A photograph can be real but misleading if it is old or from another place; a reverse-image search can show where else it has appeared.",
        ],
        "Scientific Reasoning": [
            "In 1847 Ignaz Semmelweis noticed fewer deaths from childbed fever in the Vienna ward where doctors washed their hands with chlorinated lime, and tested hand-washing as the cause.",
            "Arthur Eddington's 1919 solar eclipse expedition measured starlight bending near the Sun, a test that could have disproved Einstein's general relativity but supported it.",
            "A fair test changes one variable at a time: to see whether fertiliser helps plants grow, give two identical plants the same light and water and add fertiliser to only one.",
        ],
        "Decision Theory": [
            "Deciding whether to carry an umbrella weighs the chance of rain against the cost of getting wet and the nuisance of carrying it; formal decision theory puts numbers on the same trade-off.",
            "The prisoner's dilemma, developed in the 1950s, shows why two people acting in their own interest can both end up worse off than if they had cooperated.",
            "Daniel Kahneman and Amos Tversky's prospect theory (1979) showed that people feel losses more strongly than equal gains, and Kahneman won the Nobel Prize in Economics in 2002.",
        ],
        "Ethical Reasoning": [
            "The trolley problem asks whether it is right to divert a runaway tram so that it kills one person instead of five, separating consequence-based reasoning from rule-based reasoning.",
            "Doctors deciding who receives a scarce donor organ must balance medical need, likelihood of success and fairness, and countries publish allocation rules to make the choice transparent.",
            "Designers of self-driving cars must decide how vehicles should act in unavoidable-accident situations, a modern version of old ethical dilemmas.",
        ],
        "Systems Thinking": [
            "After wolves were reintroduced to Yellowstone National Park in 1995, researchers linked changes in elk behaviour, tree growth and even river banks to their return, showing how parts of a system are connected.",
            "Traffic jams can appear with no accident: when drivers brake slightly one after another, a wave of slowing travels backwards through the traffic.",
            "Widening a congested road can attract more drivers until it is as crowded as before, a pattern called induced demand, showing that fixing one part of a system can shift the problem elsewhere.",
        ],
    },
    "environmental_science": {
        "Ecology": [
            "Off California, sea otters eat sea urchins that graze on kelp; when otters were hunted nearly to extinction in the 1800s, urchins multiplied and kelp forests shrank.",
            "Rachel Carson's 1962 book Silent Spring described how pesticides such as DDT were harming birds and food chains, helping start the modern environmental movement.",
            "A pond ecosystem includes plants, insects, fish, microbes and the water and sunlight they depend on; removing one part, such as the insects, affects all the others.",
        ],
        "Climate Systems": [
            "The Keeling Curve, begun by Charles David Keeling at Mauna Loa in Hawaii in 1958, shows atmospheric carbon dioxide rising year after year with a seasonal wiggle as plants grow and die back.",
            "El Nino years, when the tropical Pacific warms, change rainfall patterns around the world, bringing floods to some regions and drought to others.",
            "The June 2021 heat wave in the Pacific Northwest of North America broke temperature records, and scientists concluded that human-caused warming made such an event far more likely.",
        ],
        "Biodiversity": [
            "The Amazon rainforest is estimated to hold roughly one in ten of the species known on Earth, which is why its loss matters far beyond South America.",
            "The Kunming-Montreal Global Biodiversity Framework, agreed in December 2022, aims to protect 30 per cent of the world's land and sea by 2030.",
            "Bees and other pollinators help produce many crops, so farmers in some regions now rent hives or plant flower strips beside fields to support them.",
        ],
        "Water Security": [
            "In 2018 Cape Town, South Africa, came close to 'Day Zero', when taps might have been turned off, and strict limits on household water use helped avoid it.",
            "The Aral Sea in Central Asia shrank dramatically from the 1960s after the rivers feeding it were diverted to irrigate cotton fields.",
            "Singapore reuses treated wastewater as 'NEWater' and collects rainwater, reducing its dependence on imported water.",
        ],
        "Energy Transitions": [
            "Denmark now generates close to half of its electricity from wind power, among the highest shares in the world.",
            "The Industrial Revolution moved Britain from wood and water power to coal in the 18th and 19th centuries; today's shift from fossil fuels to renewables is the next big change in energy sources.",
            "Costa Rica has produced nearly all of its electricity from renewable sources, mainly hydro, geothermal and wind, in recent years.",
        ],
        "Pollution Control": [
            "London's Great Smog of December 1952 was linked to thousands of deaths and led to the UK's Clean Air Act of 1956.",
            "The Montreal Protocol of 1987 phased out chemicals that damaged the ozone layer, and the ozone hole is expected to recover during this century.",
            "After 2013 Beijing limited coal burning and vehicle use, and average levels of fine-particle air pollution fell substantially over the following years.",
        ],
        "Sustainable Cities": [
            "Copenhagen has built extensive protected cycle lanes, and a large share of its residents travel to work or school by bike.",
            "Curitiba, Brazil, introduced a bus rapid transit system in the 1970s with dedicated lanes and raised boarding tubes, a design copied by many cities.",
            "Singapore's green roofs and Gardens by the Bay show how cities can add plants, shade buildings and cool the air.",
        ],
        "Food Systems": [
            "The UN Food and Agriculture Organization estimates that around a third of the food produced for people is lost or wasted.",
            "The Green Revolution from the 1960s used high-yield wheat and rice varieties, which Norman Borlaug helped develop, and greatly increased harvests in places such as India and Mexico.",
            "Farmers' markets and community-supported agriculture shorten the distance between growers and eaters and let shoppers ask how food was produced.",
        ],
        "Environmental Economics": [
            "British Columbia introduced a carbon tax in 2008, putting a price on emissions from burning fossil fuels.",
            "The European Union Emissions Trading System, started in 2005, caps total emissions and lets companies buy and sell permits.",
            "Since 1997 Costa Rica has paid landowners to protect forests, an example of putting a value on nature's benefits.",
        ],
        "Conservation Policy": [
            "Yellowstone, established in 1872, is generally considered the world's first national park.",
            "The Convention on International Trade in Endangered Species (CITES), in force since 1975, regulates international trade in thousands of animal and plant species.",
            "Mountain gorilla numbers in the Virunga region have increased with protected areas and tourism fees that benefit local communities.",
        ],
    },
    "health_education": {
        "Human Biology": [
            "Your heart beats roughly 100,000 times a day, pumping blood that delivers oxygen and removes waste; a nurse feeling your pulse at the wrist is counting those beats.",
            "In 1628 William Harvey showed that blood circulates around the body, replacing older ideas that the liver kept making blood that was used up.",
            "Blood groups A, B, AB and O decide who can safely donate blood to whom, a fact discovered by Karl Landsteiner in 1901.",
        ],
        "Nutrition": [
            "In 1747 the Scottish naval doctor James Lind ran a trial on sailors with scurvy and found that oranges and lemons cured them, an early demonstration that a lack of vitamin C causes disease.",
            "Many countries add iodine to table salt to prevent goitre and learning difficulties caused by iodine deficiency.",
            "Reading a food label and comparing sugar, salt and fibre per 100 grams lets shoppers choose between two breakfast cereals.",
        ],
        "Physical Activity": [
            "World Health Organization guidelines recommend at least 150 minutes of moderate activity a week for adults and an average of 60 minutes a day for children and teenagers.",
            "Parkrun began in London in 2004 with 13 runners and has grown into free weekly 5 km events in many countries.",
            "Walking or cycling to school builds activity into an ordinary day without needing a gym.",
        ],
        "Mental Health": [
            "Many schools teach children to name their emotions and use breathing exercises, because recognising feelings early makes them easier to manage.",
            "World Mental Health Day, observed every year on 10 October, is used to raise awareness and reduce stigma.",
            "Helplines such as Samaritans in the UK and 988 in the United States offer free, confidential support to people in distress.",
        ],
        "Public Health": [
            "In 1854 John Snow mapped cholera deaths in Soho, London, traced them to the Broad Street water pump and persuaded officials to remove its handle.",
            "Smallpox, which once killed millions, was declared eradicated in 1980 after a worldwide vaccination campaign led by the World Health Organization.",
            "Clean water and sanitation programmes prevent diarrhoeal disease, which is why public health agencies fund wells and toilets.",
        ],
        "Disease Prevention": [
            "Vaccination campaigns have almost eliminated polio: wild poliovirus is now found in only a few countries.",
            "Washing hands with soap for about 20 seconds removes germs and reduces infections such as colds and diarrhoea.",
            "Insecticide-treated mosquito nets have helped reduce malaria deaths in Africa.",
        ],
        "Health Systems": [
            "The UK's National Health Service was founded in 1948 and provides most care free at the point of use, paid for through taxation.",
            "Thailand's universal coverage scheme, launched in 2002, extended health insurance to most of the population.",
            "In many countries a person with a health problem first sees a general practitioner or nurse who treats common conditions and refers patients to specialists when needed.",
        ],
        "Medicines and Evidence": [
            "The 1948 Medical Research Council trial of streptomycin for tuberculosis in the UK was an early randomised controlled trial, comparing treated patients with a control group to see whether the drug really worked.",
            "Thalidomide, sold in the late 1950s for morning sickness, caused birth defects in thousands of babies and led to much stricter drug-testing rules.",
            "Alexander Fleming noticed in 1928 that mould killed bacteria on a dish, and Howard Florey and Ernst Chain later developed penicillin into a medicine.",
        ],
        "Workplace Health": [
            "Office workers can reduce back pain by adjusting chair height, keeping the screen at eye level and standing to stretch every hour.",
            "Hard hats, ear protection and safety training reduce injuries on building sites, where health and safety law requires employers to assess risks.",
            "Some employers offer employee assistance programmes so that staff can get confidential counselling for stress and personal problems.",
        ],
        "Digital Health Literacy": [
            "Before trusting a health website, look for the author's credentials, the date and whether it cites sources such as the WHO or a national health service.",
            "During the COVID-19 pandemic the WHO described an 'infodemic', an overload of information including false claims, that made reliable guidance hard to find.",
            "A smartwatch can measure heart rate but is not a medical diagnosis; unusual readings should be checked by a clinician.",
        ],
    },
    "world_politics": {
        "International Relations Theory": [
            "Realists such as Hans Morgenthau argue that states act mainly to protect their own power and security, as in the Cold War arms race between the United States and the Soviet Union.",
            "Liberal theorists point to the European Union, which grew out of the 1951 European Coal and Steel Community, as evidence that trade and shared institutions can make war between neighbours unthinkable.",
            "Constructivists such as Alexander Wendt argue that ideas shape politics: the same number of nuclear weapons means something different to an ally than to an enemy.",
        ],
        "Diplomacy": [
            "The 1978 Camp David talks, mediated by US President Jimmy Carter, led to a peace treaty between Egypt and Israel signed in 1979.",
            "The Vienna Convention on Diplomatic Relations (1961) protects ambassadors and embassies so that countries can keep talking even in times of tension.",
            "The Cuban Missile Crisis of October 1962 was resolved through secret messages and negotiations between US President Kennedy and Soviet leader Khrushchev.",
        ],
        "International Law": [
            "The International Court of Justice in The Hague settles legal disputes between states, such as disagreements over borders.",
            "The Geneva Conventions, in their current form dating from 1949, set rules for the treatment of wounded soldiers, prisoners and civilians in war.",
            "The UN Convention on the Law of the Sea (1982) lets coastal states control waters up to 12 nautical miles from shore and an exclusive economic zone of up to 200 nautical miles.",
        ],
        "Security Studies": [
            "The Nuclear Non-Proliferation Treaty, opened for signature in 1968, aims to stop the spread of nuclear weapons while promoting peaceful nuclear energy.",
            "NATO was founded in 1949; its Article 5 says an armed attack on one member is an attack on all, and it was invoked for the first time after the 11 September 2001 attacks.",
            "Cybersecurity has become part of national security: the 2017 NotPetya malware, attributed to a state by several governments, disrupted shipping and companies worldwide.",
        ],
        "Political Economy": [
            "The 2018-2019 tariff dispute between the United States and China shows how governments use trade policy to pursue political goals.",
            "The 1973 oil embargo by Arab members of OPEC sharply raised oil prices and showed that control of a resource can be political power.",
            "The Bretton Woods conference of 1944 created the International Monetary Fund and the World Bank to shape the post-war economic order.",
        ],
        "Human Rights": [
            "The International Criminal Court, which began operating in 2002, can prosecute individuals for genocide, war crimes and crimes against humanity.",
            "Amnesty International, founded in 1961 by Peter Benenson, campaigns for prisoners of conscience through letter-writing and publicity.",
            "The 1948 Genocide Convention, adopted in response to the Holocaust, made genocide a crime under international law.",
        ],
        "Global Governance": [
            "The World Health Organization coordinates responses to disease outbreaks, as when it declared COVID-19 a pandemic in March 2020.",
            "The UN Security Council has five permanent members, China, France, Russia, the United Kingdom and the United States, each able to veto resolutions.",
            "The G20, which brings together the world's major economies, meets every year to coordinate on issues such as finance and climate.",
        ],
        "Conflict Resolution": [
            "The Good Friday Agreement of 1998 largely ended decades of violence in Northern Ireland through power-sharing between unionist and nationalist parties.",
            "Truth and reconciliation commissions, such as South Africa's from 1996, let victims and perpetrators of past violence speak so that societies can move forward.",
            "UN peacekeepers, deployed since 1948, monitor ceasefires and protect civilians in places such as South Sudan and Lebanon.",
        ],
        "Regional Organisations": [
            "Many European Union members share the euro and allow citizens to live and work in any member state.",
            "ASEAN, founded in 1967, brings together Southeast Asian countries including Indonesia, Thailand and Vietnam for economic and security cooperation.",
            "The African Union, launched in 2002 to replace the Organisation of African Unity, works on peace, trade and development among African states.",
        ],
        "Foreign Policy Analysis": [
            "The Marshall Plan (1948-1951) provided more than $13 billion in US aid to rebuild Western Europe, an example of foreign policy mixing generosity with strategic interest.",
            "President Nixon's 1972 visit to China opened relations between the two countries after decades without contact.",
            "Sweden's long policy of military non-alignment ended when it joined NATO in March 2024, showing how changing security conditions can reshape a country's foreign policy.",
        ],
    },
}

# ── World religions: 6 religions x 25 angles, five cases per religion ──────────
RELIGION_ANGLE_CASE = {
    "Worship and Daily Practice": 0, "Festivals and Sacred Time": 0, "Family and Life-Cycle Rituals": 0,
    "Mysticism and Spirituality": 0, "Core Beliefs and Worldviews": 0,
    "Sources and Textual Traditions": 1, "Ethics and Moral Reasoning": 1, "Law and Religious Authority": 1,
    "Philosophy and Theology": 1, "Origins and Historical Context": 1,
    "Art, Music and Architecture": 2, "Education and Scholarship": 2,
    "Science and Intellectual History": 2, "Community and Institutions": 2,
    "Economics and Social Welfare": 3, "Gender and Society": 3, "Migration and Diaspora": 3,
    "Denominations and Internal Diversity": 3, "Religion and the State": 3,
    "Interfaith Dialogue": 4, "Peacebuilding and Conflict": 4, "Modernity and Secularisation": 4,
    "Media and Digital Religion": 4, "Comparative Perspectives": 4, "Contemporary Challenges and Futures": 4,
}

RELIGION_FRAMES = {
    "Origins and Historical Context": "place it in its historical setting: when and where did this practice, text or institution begin?",
    "Sources and Textual Traditions": "identify which texts or oral traditions this case draws on and who has preserved them.",
    "Core Beliefs and Worldviews": "state which core belief this case expresses and how it shapes the way followers see the world.",
    "Worship and Daily Practice": "describe what a follower would actually do, and how often, in connection with this case.",
    "Ethics and Moral Reasoning": "explain which moral teaching lies behind this case and how followers apply it to a real choice.",
    "Law and Religious Authority": "find who has the authority to interpret the rules in this case and how disagreements are settled.",
    "Community and Institutions": "identify the community groups or institutions that sustain this case.",
    "Festivals and Sacred Time": "explain how this case connects to the religious calendar and why those times are set apart.",
    "Art, Music and Architecture": "describe how beauty, sound or buildings carry religious meaning in this case.",
    "Philosophy and Theology": "pose one deep question this case raises about God, existence or meaning, and how thinkers have answered it.",
    "Mysticism and Spirituality": "consider how this case could support a personal, inward experience of the sacred.",
    "Family and Life-Cycle Rituals": "link the case to birth, coming of age, marriage or death rituals in the tradition.",
    "Education and Scholarship": "ask how knowledge is taught and passed on in this tradition, and what this case shows about that.",
    "Science and Intellectual History": "explore how the tradition has interacted with science and learning, using this case as a starting point.",
    "Economics and Social Welfare": "ask how this case shows the tradition caring for the poor, sharing resources or handling money.",
    "Gender and Society": "consider the roles of women and men in this case and how they have changed over time.",
    "Migration and Diaspora": "trace how the tradition travelled with people to new countries and what changed along the way.",
    "Denominations and Internal Diversity": "identify how different branches or schools within the tradition might view this case differently.",
    "Interfaith Dialogue": "ask how people of other religions could learn from, or respond to, this case respectfully.",
    "Religion and the State": "examine how governments and this tradition influence each other in this case.",
    "Peacebuilding and Conflict": "decide how this case shows the tradition working for peace, or being drawn into conflict.",
    "Modernity and Secularisation": "ask how modern life, science or secular ideas are changing how followers experience this case.",
    "Media and Digital Religion": "explore how books, broadcasting or the internet change the way this case is shared and practised.",
    "Comparative Perspectives": "compare this case with a similar practice or idea in another religion, noting both likenesses and differences.",
    "Contemporary Challenges and Futures": "identify one challenge facing followers today and how this case might help them respond.",
}

RELIGION_CASES = {
    "Islam": [
        "During Ramadan, Muslims fast from dawn to sunset, break the fast at sunset with dates and water (iftar), and many gather for night prayers; the month ends with the festival of Eid al-Fitr.",
        "The Quran, which Muslims believe was revealed to the Prophet Muhammad over about 23 years, is memorised in full by many students called huffaz, and scholars derive rulings (fiqh) from it and the Prophet's example.",
        "The Great Mosque of Cordoba, begun in 785, and the Alhambra in Granada show Islamic architecture's use of arches, geometry and calligraphy, while the University of al-Qarawiyyin in Fez, founded in 859 by Fatima al-Fihri, is among the oldest continuously operating universities.",
        "Zakat, giving a set share of wealth to the poor each year, is one of the five pillars of Islam, and Islamic endowments called waqf have funded hospitals, schools and fountains for centuries.",
        "In 2007 a group of Muslim scholars sent the open letter 'A Common Word' to Christian leaders, proposing dialogue based on the shared commandments to love God and one's neighbour.",
    ],
    "Christianity": [
        "On Sundays many Christians attend worship with readings, prayers, hymns and Communion, and the year's main festivals are Christmas on 25 December and Easter, which marks the resurrection of Jesus.",
        "The Bible contains the Old and New Testaments; the Sermon on the Mount in the Gospel of Matthew includes the Beatitudes and the teaching to love one's neighbour.",
        "Chartres Cathedral in France, rebuilt mainly in the 13th century, uses stained glass and soaring Gothic arches to tell Bible stories, and Bach's church music such as the St Matthew Passion is still widely performed.",
        "Mother Teresa founded the Missionaries of Charity in Kolkata in 1950 to care for the poor and dying, and Christian charities such as Caritas run hospitals and schools around the world.",
        "The Taize Community in France, founded in 1940 by Brother Roger, welcomes young people from many Christian traditions each year for prayer and reconciliation.",
    ],
    "Hinduism": [
        "During Diwali, the festival of lights, families light oil lamps (diyas), share sweets and honour Lakshmi, and many homes also keep a small shrine for daily puja.",
        "The Bhagavad Gita, part of the epic Mahabharata, records a dialogue between the warrior Arjuna and Krishna on duty and action, and it inspired Mahatma Gandhi.",
        "The Brihadisvara Temple in Thanjavur, completed around 1010, and classical dance forms such as Bharatanatyam show how worship, art and music are intertwined, and ancient centres such as Takshashila taught scholars from far away.",
        "Hindu communities of the Indian diaspora, including in Fiji, Trinidad and the UK, built temples and kept festivals alive after many families migrated, often as indentured labourers, in the 19th century.",
        "Gandhi's principle of ahimsa (non-violence), drawn partly from Hindu and Jain ideas, shaped India's independence movement and later inspired Martin Luther King Jr.",
    ],
    "Buddhism": [
        "Many Buddhists practise meditation and chanting, and on Vesak they celebrate the birth, enlightenment and death of the Buddha, often with lanterns and offerings.",
        "The Four Noble Truths, taught by the Buddha after his enlightenment, explain suffering and point to the Eightfold Path as the way to end it.",
        "Borobudur in Java, built around the 9th century, is a vast Buddhist monument covered in relief carvings, and Nalanda in India was a major Buddhist centre of learning.",
        "Buddhist monks and nuns in many countries live on donated food and run temple schools, and Buddhism spread along trade routes such as the Silk Road from India to China, Korea and Japan.",
        "Thich Nhat Hanh, a Vietnamese Zen monk, taught 'engaged Buddhism' and mindfulness, and Martin Luther King Jr nominated him for the Nobel Peace Prize in 1967.",
    ],
    "Judaism": [
        "Every week Shabbat begins at sundown on Friday with candles, wine and bread and a day of rest, and the Passover seder retells the Exodus from Egypt.",
        "The Torah, the first five books of the Hebrew Bible, is read in synagogues in a yearly cycle, and the Talmud records rabbis' discussions of Jewish law.",
        "The Western Wall in Jerusalem is a place of prayer, and Maimonides, a 12th-century scholar born in Cordoba, wrote on law, philosophy and medicine.",
        "Jewish communities have lived in the diaspora since ancient times, including Sephardic Jews who left Spain after 1492 and Ashkenazi communities of Central and Eastern Europe.",
        "The Second Vatican Council's 1965 declaration Nostra Aetate changed Catholic teaching toward Judaism and began a period of formal Jewish-Christian dialogue.",
    ],
    "Sikhism": [
        "In a gurdwara the Guru Granth Sahib is treated with great respect, and every visitor, whatever their background, is served langar, a free community meal.",
        "Guru Nanak, born in 1469 in what is now Pakistan, taught that there is one God and that all people are equal; his teachings and those of later gurus are collected in the Guru Granth Sahib.",
        "The Golden Temple (Harmandir Sahib) in Amritsar has doors on four sides to welcome people from every direction, and Sikh worship includes kirtan, the singing of scripture to music.",
        "Sikh charities such as Khalsa Aid, founded in 1999, give disaster relief worldwide, and gurdwaras in Punjab, Canada and the UK run langar kitchens.",
        "After the 2012 attack on the Sikh gurdwara in Oak Creek, Wisconsin, people of many faiths joined Sikh communities in vigils and began local interfaith dialogue about understanding Sikh beliefs and practices.",
    ],
}

# ── Hand-written examples for core topics that had none ────────────────────────
CORE_EXAMPLES = {
    "what_is_ecosystem": "A school pond is a small ecosystem: water lilies and algae (producers) feed snails and tadpoles, dragonfly larvae eat those, and bacteria in the mud break down dead material, all depending on sunlight, water and temperature.",
    "food_chains": "On the African savanna, grass is eaten by zebra and zebra are hunted by lions; if disease cut the zebra population, lions would have less food and the grass would be grazed less.",
    "biodiversity": "Coral reefs cover less than 1 per cent of the ocean floor yet are home to roughly a quarter of marine species; when heat bleaches a reef, the fish and the fishing communities that rely on it are affected.",
    "water_cycle": "When steam from a boiling kettle fogs a cold window and runs down it as droplets, you are watching evaporation, condensation and precipitation on a small scale.",
    "greenhouse_effect": "A car parked in the sun with its windows shut warms up inside because sunlight comes in and the heat cannot easily escape, a small-scale picture of how greenhouse gases trap heat around the Earth.",
    "renewable_vs_fossil": "Denmark's offshore wind farms in the North Sea supply a large share of its electricity, while a coal power station burns fuel formed over millions of years and releases the carbon stored in it.",
    "reduce_reuse_recycle": "Taking a refillable water bottle to school (reduce), using a jar as a pencil holder (reuse) and putting paper in the recycling bin (recycle) show the three Rs in a single day.",
    "ocean_plastics": "The Great Pacific Garbage Patch, a region of the North Pacific where currents gather floating plastic, is mostly small fragments rather than an island of rubbish; organisations such as The Ocean Cleanup try to remove plastic from rivers before it reaches the sea.",
    "body_systems": "When you run for a bus, your muscular system moves your legs, your respiratory system makes you breathe faster, your circulatory system pumps more blood to your muscles and your nervous system coordinates it all.",
    "heart_health": "Counting your pulse at the wrist for 15 seconds and multiplying by four estimates your heart rate; comparing it at rest and after exercise shows how fitness affects the heart.",
    "puberty_growth": "Classmates start puberty at different ages, roughly between 8 and 14, so a student who has grown taller than friends, or not yet, is within the normal range and comparing says little about health.",
    "macronutrients": "A school lunch of wholegrain pasta (carbohydrate), chicken or lentils (protein) and a dressing made with olive oil (fat), served with vegetables, provides all three macronutrients.",
    "micronutrients": "Sailors on long voyages once got scurvy from lacking vitamin C; today a piece of citrus fruit or a pepper provides enough, and some breakfast cereals are fortified with iron and B vitamins.",
    "what_is_mental_health": "A student who feels nervous before an exam but copes with breathing exercises and a study plan is using good mental-health skills; if worry lasts for weeks and affects sleep and daily life, talking to a trusted adult or doctor is the right step.",
    "stress_management": "Before a big exam, five slow breaths, a short walk and a full night's sleep can lower stress better than staying up late to cram.",
    "cpr_basics": "If someone collapses in a shopping centre and is not breathing normally, a bystander who calls the emergency number and starts chest compressions at about 100-120 a minute until an AED or ambulance arrives can double the person's chance of survival.",
    "common_emergencies": "If a friend burns a hand on a hot pan, hold it under cool running water for at least 20 minutes; do not use ice or butter.",
}
