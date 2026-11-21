from . import Tab, Case, Pack

PACKS = {
"Economics": Pack(
    [Tab("Key macroeconomic indicators", ["Indicator", "Measures", "Watch for"],
         ["GDP growth", "Change in real output", "Two quarters of decline = recession (rule of thumb)"], ["CPI inflation", "Change in consumer prices", "Central banks often target about 2%"],
         ["Unemployment rate", "Jobless share of the labour force", "Lagging indicator"], ["Policy interest rate", "Central bank's key rate", "Moves credit and exchange rates"],
         ["Current-account balance", "Trade plus income flows", "Persistent deficits need financing"])],
    [Case("Weimar hyperinflation", "1921–1923", "Germany printed money to meet reparations and war debts; by November 1923 one US dollar was worth trillions of marks.", "Monetising deficits can destroy a currency.", "Hyperinflation in the Weimar Republic"),
     Case("2007–2008 financial crisis", "2007–2009", "A US housing bust exposed leveraged mortgage-backed securities; Lehman Brothers failed on 15 September 2008 and credit markets froze.", "Leverage and interconnection turn local losses into systemic crises.", "Financial crisis of 2007–2008"),
     Case("Asian financial crisis", "1997–1998", "Thailand floated the baht in July 1997; currency collapses spread across East Asia and led to IMF programmes.", "Fixed exchange rates plus short-term foreign debt are fragile.", "1997 Asian financial crisis")]),
"Finance": Pack(
    [Tab("Common financial ratios", ["Ratio", "Formula", "Reads as"],
         ["Current ratio", "Current assets ÷ current liabilities", "Short-term liquidity"], ["Debt-to-equity", "Total debt ÷ equity", "Leverage"],
         ["Return on equity", "Net income ÷ equity", "Profit for owners"], ["P/E ratio", "Price ÷ earnings per share", "Market pricing of earnings"])],
    [Case("Long-Term Capital Management", "1998", "A hedge fund with Nobel-winning partners and about 25× leverage lost billions after Russia's default; the Fed organised a private rescue.", "Models fail in tails, and leverage multiplies the damage.", "Long-Term Capital Management"),
     Case("Lehman Brothers collapse", "15 September 2008", "The largest bankruptcy in US history, Lehman's failure froze interbank lending worldwide.", "Funding liquidity can vanish overnight.", "Bankruptcy of Lehman Brothers"),
     Case("GameStop short squeeze", "January 2021", "Retail traders coordinated on Reddit and drove GameStop's price up many-fold, forcing short sellers to cover.", "Crowded short positions carry unbounded risk.", "GameStop short squeeze")]),
"MBA": Pack(
    [Tab("Porter's five forces", ["Force", "Question"],
         ["Rivalry among competitors", "How intense is competition?"], ["Threat of new entrants", "How easy is entry?"], ["Threat of substitutes", "What else meets the need?"],
         ["Buyer power", "Can customers push prices down?"], ["Supplier power", "Can suppliers push costs up?"])],
    [Case("Kodak and digital photography", "1975–2012", "Kodak engineers invented the digital camera in 1975, but the company protected its film business and filed for bankruptcy in January 2012.", "Disrupting yourself beats being disrupted.", "Eastman Kodak"),
     Case("Netflix versus Blockbuster", "2000–2010", "Netflix moved from DVDs by mail to streaming while Blockbuster, which declined to buy Netflix in 2000, filed for bankruptcy in 2010.", "Business-model shifts beat incremental improvement.", "Blockbuster LLC"),
     Case("Nokia and the smartphone", "2007–2013", "Nokia led mobile phones in 2007 but lost ground to iOS and Android before selling its handset unit to Microsoft in 2014.", "Platform ecosystems can outweigh hardware leadership.", "Nokia")]),
"Business Studies": Pack(
    [Tab("Business structures", ["Structure", "Liability", "Typical use"],
         ["Sole trader", "Unlimited", "Individual-run small business"], ["Partnership", "Often joint and unlimited", "Professional firms"],
         ["Limited company", "Limited to shares", "Growing firms seeking investors"], ["Co-operative", "Limited to members' stakes", "Member-owned enterprises"])],
    [Case("Enron collapse", "2001", "Enron hid debt in off-balance-sheet entities and filed for bankruptcy in December 2001; its auditor Arthur Andersen collapsed.", "Governance and honest reporting protect stakeholders.", "Enron scandal"),
     Case("Toyota Production System", "1950s–present", "Toyota's just-in-time and continuous-improvement methods cut waste and became a model for lean manufacturing.", "Eliminating waste raises quality and lowers cost.", "Toyota Production System")]),
"Operations Management": Pack(
    [Tab("Lean's seven wastes (TIMWOOD)", ["Waste", "Example"],
         ["Transport", "Moving parts between distant stations"], ["Inventory", "Stock waiting to be used"], ["Motion", "Walking to fetch tools"],
         ["Waiting", "Idle machines or people"], ["Over-production", "Making more than demanded"], ["Over-processing", "Unneeded finishing steps"], ["Defects", "Rework and scrap"])],
    [Case("Toyota Production System", "1950s–present", "Taiichi Ohno built just-in-time flow, kanban and 'stop the line' quality at Toyota.", "Pull systems expose problems early.", "Toyota Production System"),
     Case("Zara fast fashion", "1990s–present", "Zara produces many items near its markets in short lead times so stores can restock within days.", "Speed can beat forecast accuracy.", "Zara (retailer)"),
     Case("2011 Thailand floods", "October–December 2011", "Floods shut factories that made hard-disk parts and cars, disrupting global supply chains.", "Concentrated suppliers are single points of failure.", "2011 Thailand floods")]),
"Project Management": Pack(
    [Tab("Project constraints", ["Constraint", "Typical trade-off"],
         ["Scope", "More scope needs more time or money"], ["Time", "Compressing needs crashing or fast-tracking"], ["Cost", "Cutting cost reduces scope or quality"], ["Quality", "Rework costs time and money"])],
    [Case("Sydney Opera House", "1959–1973", "Planned for 1963 at A$7 million, it opened in 1973 at about A$102 million after design changes and engineering challenges.", "Starting construction before design is settled drives overruns.", "Sydney Opera House"),
     Case("Denver airport baggage system", "1990s", "An automated baggage system delayed Denver International Airport's opening by about 16 months and added hundreds of millions in cost.", "Over-ambitious scope and late integration cause failure.", "Denver International Airport"),
     Case("Apollo 13 crisis response", "April 1970", "Ground teams improvised a CO₂ scrubber adaptation and a new return plan, bringing the crew home.", "Strong teams and contingency planning rescue projects.", "Apollo 13")]),
"Math": Pack(
    [Tab("Famous problems", ["Problem", "Status"],
         ["Fermat's Last Theorem", "Proved by Andrew Wiles (1994–95)"], ["Poincaré conjecture", "Proved by Grigori Perelman (2002–03)"],
         ["Four colour theorem", "Proved by computer in 1976 (Appel and Haken)"], ["Riemann hypothesis", "Open"], ["P versus NP", "Open"])],
    [Case("Fermat's Last Theorem", "1637–1995", "Fermat's margin note went unproven for 358 years until Andrew Wiles proved it using elliptic curves and modular forms.", "Deep problems connect distant fields.", "Fermat's Last Theorem"),
     Case("The four colour theorem", "1976", "Kenneth Appel and Wolfgang Haken proved any map needs at most four colours, using a computer check of many cases.", "Computers can be part of a proof.", "Four color theorem"),
     Case("PageRank", "1998", "Google's founders modelled the web as a Markov chain and ranked pages by its stationary distribution.", "Linear algebra can power a search engine.", "PageRank")]),
"Social Studies": Pack(
    [Tab("The demographic transition", ["Stage", "Birth and death rates"],
         ["1", "Both high; population stable"], ["2", "Death rate falls; population grows rapidly"], ["3", "Birth rate falls; growth slows"], ["4", "Both low; population stable"])],
    [Case("Marienthal unemployment study", "1930–1933", "Researchers studied an Austrian village after its factory closed and documented how long-term unemployment led to apathy.", "Social research can show the human cost of economic shocks.", "Marienthal"),
     Case("Bowling Alone", "1995–2000", "Robert Putnam documented a US decline in civic participation and trust.", "Social capital shapes community outcomes.", "Bowling Alone")]),
"Civics": Pack(
    [Tab("Electoral systems", ["System", "Example", "Tendency"],
         ["First-past-the-post", "United Kingdom, United States", "Two-party competition"], ["Proportional representation", "Netherlands, Sweden", "Many parties, coalitions"],
         ["Mixed-member", "Germany, New Zealand", "Balances local and proportional"], ["Ranked choice", "Australia (House), Ireland", "Preference-based"])],
    [Case("Marbury v. Madison", "1803", "The US Supreme Court asserted the power of judicial review by striking down part of a federal law.", "Courts can check the legislature.", "Marbury v. Madison"),
     Case("Brown v. Board of Education", "1954", "The Court ruled racial segregation in public schools unconstitutional.", "Constitutional interpretation can transform society.", "Brown v. Board of Education"),
     Case("Bush v. Gore", "2000", "The Supreme Court halted the Florida recount, effectively deciding the presidential election.", "Close elections test legal institutions.", "Bush v. Gore")]),
"World Politics": Pack(
    [Tab("UN Security Council", ["Feature", "Detail"],
         ["Permanent members", "China, France, Russia, United Kingdom, United States"], ["Elected members", "10, two-year terms"], ["Resolution threshold", "9 votes and no permanent-member veto"])],
    [Case("Cuban Missile Crisis", "October 1962", "A 13-day standoff over Soviet missiles in Cuba brought the US and USSR close to nuclear war and ended with a negotiated withdrawal.", "Back-channels and face-saving exits prevent escalation.", "Cuban Missile Crisis"),
     Case("Treaty of Westphalia", "1648", "The agreements ending the Thirty Years' War are often cited as the origin of state sovereignty in international relations.", "Sovereignty underpins the modern state system.", "Peace of Westphalia"),
     Case("Brexit referendum", "23 June 2016", "UK voters chose to leave the EU by 51.9% to 48.1%, beginning a long withdrawal process.", "Referendums can reshape alliances.", "Brexit")]),
"Critical Thinking": Pack(
    [Tab("Common fallacies", ["Fallacy", "Pattern"],
         ["Ad hominem", "Attacks the person, not the argument"], ["Straw man", "Misrepresents then refutes"], ["Post hoc", "After, therefore because"],
         ["Base-rate neglect", "Ignores prior probability"], ["Survivorship bias", "Studies only the winners"])],
    [Case("Wald and the bomber armour", "1943", "Abraham Wald showed that armour should go where returning planes were not hit, since those that were hit there never came back.", "Beware survivorship bias.", "Abraham Wald"),
     Case("Semmelweis and handwashing", "1847", "Ignaz Semmelweis cut deaths from childbed fever by requiring handwashing, but was rejected by peers who lacked a mechanism.", "Good evidence can meet resistance; keep testing.", "Ignaz Semmelweis"),
     Case("Sally Clark case", "1999", "A mother was wrongly convicted after an expert misapplied probability to two infant deaths, ignoring dependence.", "Misusing statistics can convict the innocent.", "Sally Clark")]),
"Geography": Pack(
    [Tab("Earth facts", ["Fact", "Value"],
         ["Mean radius", "≈ 6,371 km"], ["Highest point", "Mount Everest, ≈ 8,849 m"], ["Deepest point", "Challenger Deep, ≈ 10,900 m below sea level"], ["Ocean share of surface", "≈ 71%"])],
    [Case("Aral Sea shrinkage", "1960s–present", "Soviet irrigation diverted the Amu Darya and Syr Darya rivers, shrinking the Aral Sea to a fraction of its former size.", "Water diversion can cause regional disaster.", "Aral Sea"),
     Case("Three Gorges Dam", "1994–2012", "China built the world's largest hydropower station, displacing over a million people while providing flood control and power.", "Large infrastructure trades benefits against displacement.", "Three Gorges Dam"),
     Case("Dutch Delta Works", "1950s–1997", "After the 1953 North Sea flood killed over 1,800 people, the Netherlands built a vast system of dams and barriers.", "Disasters can drive long-term adaptation.", "Delta Works")]),
}
