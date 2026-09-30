#!/usr/bin/env python3
"""Populate the "World Leaders & Politics" biography category with real,
verified political leaders and statespeople. See _biography_engine.py for
the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_leaders.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="abraham_lincoln", name="Abraham Lincoln", years="1809-1865", nationality="American",
        field="16th President of the United States", wiki_title="Abraham Lincoln",
        significance="he led the United States through the Civil War and issued the Emancipation Proclamation, a major step toward ending slavery in America",
        facts=[
            "Abraham Lincoln was born in a one-room log cabin in Kentucky in 1809 and was largely self-taught",
            "He served in the Illinois state legislature and one term in the US House of Representatives before becoming president",
            "He was elected president in 1860, and Southern states began seceding from the Union before he even took office",
            "He issued the Emancipation Proclamation in 1863, declaring enslaved people in Confederate territory to be free",
            "He delivered the Gettysburg Address in 1863, a two-minute speech that became one of the most quoted in American history",
            "He signed the 13th Amendment in 1865, formally abolishing slavery throughout the United States",
            "He was assassinated by John Wilkes Booth in April 1865, just days after the Confederacy's surrender",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="nelson_mandela", name="Nelson Mandela", years="1918-2013", nationality="South African",
        field="anti-apartheid leader and statesman", wiki_title="Nelson Mandela",
        significance="he spent 27 years in prison for his opposition to apartheid before becoming South Africa's first Black president and a global symbol of reconciliation",
        facts=[
            "Nelson Mandela was born in 1918 in Mvezo, in what is now South Africa's Eastern Cape",
            "He joined the African National Congress (ANC) in 1944 and became a leading figure in its resistance to apartheid",
            "He was arrested in 1962 and later sentenced to life in prison in 1964 on charges related to sabotage against the apartheid government",
            "He spent 27 years in prison, much of it on Robben Island, before being released in 1990 amid growing international pressure",
            "He and South African president F.W. de Klerk jointly won the Nobel Peace Prize in 1993 for negotiating an end to apartheid",
            "In 1994 he was elected South Africa's first Black president in the country's first fully democratic election",
            "He chose not to seek re-election after one term, and established the Truth and Reconciliation Commission to address the crimes of apartheid",
        ], related_subjects=["Civics", "World History", "World Politics"],
    ),
    dict(
        id="mahatma_gandhi", name="Mahatma Gandhi", years="1869-1948", nationality="Indian",
        field="independence leader and philosopher", wiki_title="Mahatma Gandhi",
        significance="he led India's independence movement from British rule through a philosophy of nonviolent civil disobedience, influencing civil rights movements worldwide",
        facts=[
            "Mohandas Karamchand Gandhi was born in Porbandar, India, in 1869 and trained as a lawyer in London",
            "He spent over 20 years in South Africa, where he first developed his philosophy of nonviolent resistance, called satyagraha, while fighting discrimination against Indians there",
            "He returned to India in 1915 and became a leading figure in the movement for independence from British rule",
            "In 1930 he led the Salt March, a 240-mile walk to the sea to protest the British salt tax, which drew international attention",
            "He was imprisoned by British authorities multiple times over the course of his activism",
            "India gained independence in August 1947, though it was partitioned into India and Pakistan, an outcome that deeply grieved him",
            "He was assassinated in January 1948 by a Hindu nationalist who opposed his tolerance toward Muslims",
        ], related_subjects=["Civics", "World History", "World Politics"],
    ),
    dict(
        id="winston_churchill", name="Winston Churchill", years="1874-1965", nationality="British",
        field="Prime Minister of the United Kingdom", wiki_title="Winston Churchill",
        significance="as British Prime Minister during World War II, his leadership and speeches helped rally Britain during its darkest and most isolated period of the war",
        facts=[
            "Winston Churchill was born at Blenheim Palace, England, in 1874",
            "He served as a soldier and war correspondent in his younger years, including in colonial-era conflicts in Cuba, India, Sudan, and South Africa",
            "He became Prime Minister in May 1940, just as Nazi Germany was overrunning Western Europe",
            "His wartime speeches, including 'We shall fight on the beaches' and 'Their finest hour', helped sustain British morale during the Blitz",
            "He worked closely with US President Franklin Roosevelt and Soviet leader Joseph Stalin as part of the Allied leadership during the war",
            "Despite his wartime popularity, he lost the 1945 general election shortly after the war in Europe ended",
            "He won the Nobel Prize in Literature in 1953, largely for his historical and biographical writing, including his multi-volume history of World War II",
        ], related_subjects=["World History", "Civics"],
    ),
    dict(
        id="franklin_roosevelt", name="Franklin D. Roosevelt", years="1882-1945", nationality="American",
        field="32nd President of the United States", wiki_title="Franklin D. Roosevelt",
        significance="he led the United States through the Great Depression with his New Deal programs and through most of World War II, and remains the only US president elected to four terms",
        facts=[
            "Franklin D. Roosevelt was born in Hyde Park, New York, in 1882 into a wealthy family",
            "In 1921 he contracted a paralytic illness, widely believed to be polio, which left him unable to walk unaided for the rest of his life",
            "He was elected president in 1932 during the depths of the Great Depression and launched the New Deal, a series of programs and reforms aimed at economic recovery",
            "His New Deal included the creation of Social Security in 1935, providing a retirement safety net for American workers",
            "He held regular 'fireside chats', radio addresses that helped him communicate directly with the American public",
            "He led the United States through most of World War II after the December 1941 attack on Pearl Harbor, working closely with Winston Churchill and Joseph Stalin",
            "He died in office in April 1945, just weeks before Germany's surrender, and was succeeded by Vice President Harry Truman",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="angela_merkel", name="Angela Merkel", years="1954-present", nationality="German",
        field="Chancellor of Germany", wiki_title="Angela Merkel",
        significance="she served as Chancellor of Germany from 2005 to 2021, becoming one of the most influential leaders in the European Union during a period spanning multiple major financial and geopolitical crises",
        facts=[
            "Angela Merkel was born in Hamburg, West Germany, in 1954, and grew up in East Germany, where her father was a Lutheran pastor",
            "She trained as a physicist and earned a doctorate in quantum chemistry before entering politics after the fall of the Berlin Wall in 1989",
            "In 2005 she became Germany's first female Chancellor, leading the Christian Democratic Union",
            "She played a central role in managing the European debt crisis, particularly regarding Greece, during the early 2010s",
            "In 2015 she made the controversial decision to keep German borders open to over a million refugees, mainly from Syria, during the European migrant crisis",
            "She was widely regarded as a key stabilizing figure in the European Union during her four terms in office",
            "She left office in December 2021, having served as Chancellor for just over 16 years",
        ], related_subjects=["Civics", "World Politics", "World History"],
    ),
    dict(
        id="queen_elizabeth_ii", name="Queen Elizabeth II", years="1926-2022", nationality="British",
        field="Queen of the United Kingdom", wiki_title="Elizabeth II",
        significance="she reigned as Queen of the United Kingdom for over 70 years, the longest reign of any British monarch, spanning enormous social and political change",
        facts=[
            "Elizabeth II was born in London in 1926 and was not originally expected to become queen, until her uncle King Edward VIII abdicated in 1936",
            "She served as a mechanic and truck driver in the Auxiliary Territorial Service during the final years of World War II",
            "She became queen in February 1952 upon the death of her father, King George VI, at age 25",
            "Her coronation in 1953 was the first British coronation to be televised, watched by millions worldwide",
            "During her reign she met with 13 different UK prime ministers, from Winston Churchill to Liz Truss",
            "She oversaw the transition of many British colonies to independence and the evolution of the Commonwealth of Nations",
            "She died in September 2022 at Balmoral Castle, Scotland, after a reign of just over 70 years, the longest of any British monarch",
        ], related_subjects=["World History", "Civics"],
    ),
    dict(
        id="sheikh_mujibur_rahman", name="Sheikh Mujibur Rahman", years="1920-1975", nationality="Bangladeshi",
        field="founding leader of Bangladesh", wiki_title="Sheikh Mujibur Rahman",
        significance="he led the political movement for Bangladesh's independence from Pakistan and became the country's first president, and is honored as the Father of the Nation",
        facts=[
            "Sheikh Mujibur Rahman was born in 1920 in Tungipara, in what was then British India and is now Bangladesh",
            "He became a leading figure in the Awami League and campaigned for the political and cultural rights of East Pakistan, later Bangladesh, within Pakistan",
            "In his famous March 7, 1971 speech at the Ramna Race Course in Dhaka, he called on the people to prepare for a struggle for independence",
            "He was arrested by the Pakistani military shortly after the start of the Bangladesh Liberation War in 1971 and imprisoned in West Pakistan",
            "Bangladesh achieved independence in December 1971, and he was released and returned to lead the new nation in January 1972",
            "He served as Bangladesh's first president and later as prime minister, working to rebuild the war-torn country",
            "He was assassinated along with most of his family in a military coup in August 1975",
        ], related_subjects=["Civics", "World History", "World Politics"],
    ),
    dict(
        id="mao_zedong", name="Mao Zedong", years="1893-1976", nationality="Chinese",
        field="founding leader of the People's Republic of China", wiki_title="Mao Zedong",
        significance="he led the Communist Party of China to victory in the Chinese Civil War and founded the People's Republic of China in 1949, ruling until his death in 1976",
        facts=[
            "Mao Zedong was born in Shaoshan, Hunan province, China, in 1893, to a farming family",
            "He was a founding member of the Chinese Communist Party in 1921",
            "He led the Communist forces on the Long March, a roughly 6,000-mile retreat in 1934-1935 that helped establish his leadership of the party",
            "In October 1949 he proclaimed the founding of the People's Republic of China after the Communist victory in the Chinese Civil War",
            "His Great Leap Forward campaign, launched in 1958 to rapidly industrialize China, led to a catastrophic famine that killed tens of millions of people",
            "His Cultural Revolution, launched in 1966, caused widespread social upheaval and persecution that lasted roughly a decade",
            "He died in 1976, and his body remains on public display in a mausoleum in Beijing's Tiananmen Square",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="margaret_thatcher", name="Margaret Thatcher", years="1925-2013", nationality="British",
        field="Prime Minister of the United Kingdom", wiki_title="Margaret Thatcher",
        significance="as the United Kingdom's first female Prime Minister, serving from 1979 to 1990, she pursued sweeping free-market economic reforms that became known as Thatcherism",
        facts=[
            "Margaret Thatcher was born in Grantham, England, in 1925, the daughter of a grocer, and studied chemistry at Oxford before training as a barrister",
            "She became leader of the Conservative Party in 1975 and was elected the United Kingdom's first female Prime Minister in 1979",
            "Her government privatized numerous state-owned industries, including telecommunications, gas, and British Airways",
            "She confronted and defeated a major national coal miners' strike in 1984-1985, a defining and highly divisive moment of her premiership",
            "She led Britain to victory in the 1982 Falklands War against Argentina, which significantly boosted her domestic popularity",
            "She was a close ally of US President Ronald Reagan during the final years of the Cold War",
            "She earned the nickname 'the Iron Lady' from Soviet media for her uncompromising political style, and the name stuck",
        ], related_subjects=["World History", "Civics", "World Politics"],
    ),
    dict(
        id="john_f_kennedy", name="John F. Kennedy", years="1917-1963", nationality="American",
        field="35th President of the United States", wiki_title="John F. Kennedy",
        significance="his presidency, cut short by assassination, included the Cuban Missile Crisis and the launch of the Apollo program's goal to land a man on the Moon",
        facts=[
            "John F. Kennedy was born in Brookline, Massachusetts, in 1917, into a prominent political family",
            "He served in the US Navy during World War II and was decorated for heroism after his patrol torpedo boat, PT-109, was sunk by a Japanese destroyer",
            "In 1960 he was elected president at age 43, becoming the youngest person elected to the office and the first Catholic president",
            "In 1962 he navigated the Cuban Missile Crisis, a tense 13-day standoff with the Soviet Union over nuclear missiles in Cuba that many historians consider the closest the Cold War came to nuclear conflict",
            "In a 1961 speech to Congress, he set the goal of landing a man on the Moon before the end of the decade, launching the Apollo program",
            "He supported civil rights legislation and delivered a major civil rights address to the nation in June 1963",
            "He was assassinated in Dallas, Texas, in November 1963, an event that remains one of the most examined in American history",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="indira_gandhi", name="Indira Gandhi", years="1917-1984", nationality="Indian",
        field="Prime Minister of India", wiki_title="Indira Gandhi",
        significance="she served as India's first and, to date, only female Prime Minister, leading the country through major wars, economic policy shifts, and a controversial period of emergency rule",
        facts=[
            "Indira Gandhi was born in Allahabad, India, in 1917, the daughter of India's first prime minister, Jawaharlal Nehru",
            "She became Prime Minister of India in 1966, leading the Indian National Congress party",
            "She led India during the 1971 war with Pakistan, which resulted in the independence of Bangladesh",
            "In 1974 India conducted its first successful nuclear weapons test under her government",
            "In 1975 she declared a State of Emergency, suspending many civil liberties and elections for nearly two years, a highly controversial period in Indian democracy",
            "She was voted out of office in 1977 but returned to power in 1980 after winning re-election",
            "She was assassinated by two of her own bodyguards in 1984, in the aftermath of a military operation she had ordered against Sikh separatists",
        ], related_subjects=["World History", "World Politics", "Civics"],
    ),
]

PEOPLE += [
    dict(
        id="theodore_roosevelt", name="Theodore Roosevelt", years="1858-1919", nationality="American",
        field="26th President of the United States", wiki_title="Theodore Roosevelt",
        significance="he expanded federal conservation of public land, broke up corporate monopolies through antitrust action, and won the Nobel Peace Prize for mediating the end of the Russo-Japanese War",
        facts=[
            "Theodore Roosevelt was born in New York City in 1858 and overcame severe childhood asthma through a disciplined regimen of exercise",
            "He led the Rough Riders, a volunteer cavalry regiment, in the 1898 Spanish-American War, gaining national fame",
            "He became president in 1901 at age 42 after the assassination of President William McKinley, the youngest person to hold the office",
            "He pursued 'trust-busting' antitrust actions against major corporate monopolies, including Standard Oil",
            "He established the US Forest Service and set aside roughly 230 million acres of public land for conservation, including national parks and monuments",
            "He won the Nobel Peace Prize in 1906 for mediating an end to the Russo-Japanese War, the first American to win a Nobel Prize",
            "His face is one of four presidents carved into Mount Rushmore",
        ], related_subjects=["Civics", "World History", "Environmental Science"],
    ),
    dict(
        id="otto_von_bismarck", name="Otto von Bismarck", years="1815-1898", nationality="German (Prussian)",
        field="Chancellor of Germany", wiki_title="Otto von Bismarck",
        significance="through a strategy of diplomacy and war, he engineered the unification of Germany in 1871 and became its first Chancellor",
        facts=[
            "Otto von Bismarck was born in Schonhausen, Prussia, in 1815, into a landowning aristocratic family",
            "He became Minister President of Prussia in 1862 and pursued a policy he described as being achieved through 'blood and iron'",
            "He engineered a series of wars, including against Denmark, Austria, and France between 1864 and 1871, that unified the German states under Prussian leadership",
            "In January 1871, following victory in the Franco-Prussian War, the German Empire was proclaimed with Bismarck as its first Chancellor",
            "He introduced some of the world's first modern social welfare programs in the 1880s, including health insurance and old-age pensions, partly to undercut support for socialist movements",
            "He built a complex system of European alliances designed to isolate France and maintain peace among the great powers",
            "He was dismissed from office in 1890 by the young Kaiser Wilhelm II, after nearly three decades in power",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="benazir_bhutto", name="Benazir Bhutto", years="1953-2007", nationality="Pakistani",
        field="Prime Minister of Pakistan", wiki_title="Benazir Bhutto",
        significance="she became the first woman to serve as prime minister of a Muslim-majority country when she took office in Pakistan in 1988",
        facts=[
            "Benazir Bhutto was born in Karachi, Pakistan, in 1953, the daughter of former prime minister Zulfikar Ali Bhutto",
            "She studied at Harvard University and later Oxford University, where she became president of the Oxford Union debating society",
            "Her father was overthrown in a military coup in 1977 and executed in 1979, after which she spent years under house arrest or in exile",
            "In 1988 she was elected Prime Minister of Pakistan, becoming the first woman to lead a Muslim-majority nation",
            "She served two separate terms as Prime Minister, in 1988-1990 and 1993-1996, both ending with her government's dismissal amid corruption allegations",
            "She returned to Pakistan in 2007 after years of self-imposed exile, to campaign in upcoming elections",
            "She was assassinated at a campaign rally in Rawalpindi in December 2007",
        ], related_subjects=["World History", "World Politics", "Civics"],
    ),
    dict(
        id="charles_de_gaulle", name="Charles de Gaulle", years="1890-1970", nationality="French",
        field="President of France", wiki_title="Charles de Gaulle",
        significance="he led the Free French forces during World War II and later founded France's Fifth Republic, serving as its first president",
        facts=[
            "Charles de Gaulle was born in Lille, France, in 1890, and served as a French army officer during World War I, during which he was wounded and captured",
            "After France's fall to Nazi Germany in 1940, he fled to London and led the Free French forces in exile, rallying resistance from abroad",
            "His June 18, 1940 radio broadcast calling on the French to continue resisting became a foundational moment of the French Resistance",
            "He led the provisional government of France after its liberation in 1944",
            "He founded the Fifth Republic in 1958, drafting a new constitution that greatly strengthened the presidency, and became its first president",
            "He oversaw Algeria's independence from France in 1962, ending a long and bitter colonial war",
            "He resigned the presidency in 1969 after losing a national referendum on constitutional reforms",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="golda_meir", name="Golda Meir", years="1898-1978", nationality="Israeli",
        field="Prime Minister of Israel", wiki_title="Golda Meir",
        significance="she served as Israel's fourth prime minister and its first and, to date, only female prime minister, leading the country during the 1973 Yom Kippur War",
        facts=[
            "Golda Meir was born Golda Mabovitch in Kyiv, in the Russian Empire, in 1898, and emigrated with her family to the United States as a child",
            "She moved to Palestine in 1921, then under British Mandate, and became active in the labor movement and Zionist politics",
            "She was one of the signatories of Israel's Declaration of Independence in 1948",
            "She served as Israel's foreign minister from 1956 to 1966 before becoming prime minister in 1969",
            "She led Israel through the 1973 Yom Kippur War, a surprise attack by Egypt and Syria that initially caught Israeli forces off guard",
            "A government commission later found intelligence failures ahead of the war, and public criticism contributed to her resignation in 1974",
            "She remains, as of the early 2020s, the only woman to have served as Israel's prime minister",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="jawaharlal_nehru", name="Jawaharlal Nehru", years="1889-1964", nationality="Indian",
        field="Prime Minister of India", wiki_title="Jawaharlal Nehru",
        significance="he became independent India's first prime minister in 1947 and shaped the country's early foreign policy, industrial development, and secular democratic institutions over 17 years in office",
        facts=[
            "Jawaharlal Nehru was born in Allahabad, India, in 1889, and studied law at Cambridge University in England",
            "He became a close associate of Mahatma Gandhi in the Indian independence movement and was imprisoned by British colonial authorities multiple times",
            "He became India's first prime minister when the country gained independence in August 1947",
            "He delivered the well-known 'Tryst with Destiny' speech at midnight on August 15, 1947, marking India's independence",
            "He pursued a policy of nonalignment during the Cold War, helping found the Non-Aligned Movement with leaders like Yugoslavia's Tito and Egypt's Nasser",
            "He championed industrialization and the establishment of institutions like the Indian Institutes of Technology during his time in office",
            "He served as prime minister for 17 years, until his death in office in 1964",
        ], related_subjects=["World History", "World Politics", "Civics"],
    ),
    dict(
        id="simon_bolivar", name="Simon Bolivar", years="1783-1830", nationality="Venezuelan",
        field="independence leader", wiki_title="Simon Bolivar",
        significance="he led military campaigns that won independence from Spanish colonial rule for what are now Venezuela, Colombia, Ecuador, Panama, Peru, and Bolivia, earning him the title 'the Liberator'",
        facts=[
            "Simon Bolivar was born in Caracas, in what is now Venezuela, in 1783, into a wealthy Creole family",
            "He was inspired by Enlightenment ideas of liberty while traveling and studying in Europe as a young man",
            "He led military campaigns beginning in the 1810s that liberated large parts of South America from Spanish colonial control",
            "He led the famous crossing of the Andes mountains in 1819, a surprise military maneuver that led to victory at the Battle of Boyaca",
            "He served as president of Gran Colombia, a large union of northern South American territories that later split into separate nations",
            "The country of Bolivia is named in his honor",
            "He died in 1830 in Santa Marta, in present-day Colombia, disillusioned by the political fragmentation of the territories he had helped liberate",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="lee_kuan_yew", name="Lee Kuan Yew", years="1923-2015", nationality="Singaporean",
        field="founding Prime Minister of Singapore", wiki_title="Lee Kuan Yew",
        significance="as Singapore's first prime minister, serving from 1959 to 1990, he transformed the small city-state from a poor colonial port into one of the world's wealthiest nations per capita",
        facts=[
            "Lee Kuan Yew was born in Singapore in 1923, then a British colony, and studied law at Cambridge University",
            "He co-founded the People's Action Party in 1954 and became Singapore's first prime minister in 1959",
            "Singapore briefly merged with Malaysia in 1963 before separating to become fully independent in 1965, a traumatic and unplanned transition he later described in emotional terms",
            "He pursued policies emphasizing pragmatic economic development, foreign investment, and strict anti-corruption enforcement",
            "Under his leadership, Singapore's per capita income grew from among the lowest in Asia to one of the highest in the world within a few decades",
            "His government was also criticized internationally for restrictions on press freedom and political opposition",
            "He stepped down as prime minister in 1990 after 31 years in office, remaining influential in government as senior minister and later minister mentor",
        ], related_subjects=["World History", "World Politics", "Business Studies"],
    ),
    dict(
        id="vaclav_havel", name="Vaclav Havel", years="1936-2011", nationality="Czech",
        field="playwright and statesman", wiki_title="Vaclav Havel",
        significance="a dissident playwright imprisoned under Communist rule, he became the first president of Czechoslovakia after the 1989 Velvet Revolution and later the first president of the Czech Republic",
        facts=[
            "Vaclav Havel was born in Prague, Czechoslovakia, in 1936, into a family later persecuted for its bourgeois background under Communist rule",
            "He became a prominent playwright in the 1960s before Communist authorities banned his work following the 1968 Soviet-led invasion of Czechoslovakia",
            "He co-founded Charter 77, a human rights declaration criticizing the Communist government, and was imprisoned multiple times for his activism",
            "He became a leading figure of the 1989 Velvet Revolution, the largely peaceful movement that ended over 40 years of Communist rule in Czechoslovakia",
            "He was elected president of Czechoslovakia in December 1989, less than two months after his release from prison",
            "When Czechoslovakia peacefully split into the Czech Republic and Slovakia in 1993, he became the first president of the new Czech Republic",
            "He remained a prominent international voice on human rights until his death in 2011",
        ], related_subjects=["World History", "World Politics", "Civics"],
    ),
    dict(
        id="kwame_nkrumah", name="Kwame Nkrumah", years="1909-1972", nationality="Ghanaian",
        field="independence leader and Prime Minister of Ghana", wiki_title="Kwame Nkrumah",
        significance="he led Ghana to independence from British colonial rule in 1957, becoming the first leader of a sub-Saharan African nation to do so, and was a leading advocate of Pan-Africanism",
        facts=[
            "Kwame Nkrumah was born in the Gold Coast, a British colony in West Africa now known as Ghana, around 1909",
            "He studied in the United States at Lincoln University and the University of Pennsylvania before returning to West Africa to organize for independence",
            "He founded the Convention People's Party in 1949, campaigning for immediate self-government",
            "In 1957 Ghana became independent, with Nkrumah as its first prime minister, making it the first sub-Saharan African colony to gain independence in the postwar wave of decolonization",
            "He was a founding advocate of Pan-Africanism and helped establish the Organisation of African Unity in 1963",
            "His government pursued major infrastructure projects, including the Akosombo Dam, while also increasingly consolidating single-party power",
            "He was overthrown in a military coup in 1966 while on a state visit to China, and spent his remaining years in exile",
        ], related_subjects=["World History", "World Politics", "Civics"],
    ),
    dict(
        id="george_washington", name="George Washington", years="1732-1799", nationality="American",
        field="1st President of the United States", wiki_title="George Washington",
        significance="he commanded the Continental Army to victory in the American Revolutionary War and became the first President of the United States, setting precedents that shaped the presidency for centuries",
        facts=[
            "George Washington was born in Westmoreland County, Virginia, in 1732, into a family of moderate landowning status",
            "He commanded the Continental Army during the American Revolutionary War from 1775 to 1783, leading it to eventual victory over Britain",
            "He presided over the Constitutional Convention in 1787, which drafted the US Constitution",
            "He was unanimously elected the first President of the United States in 1789 and again in 1792",
            "He voluntarily stepped down after two terms in 1797, setting an unofficial precedent for peaceful transfer of power that lasted until the 20th century",
            "His 1796 Farewell Address warned against political factionalism and long-term foreign alliances",
            "He is the only US president to have been elected unanimously by the Electoral College, and did so twice",
        ], related_subjects=["Civics", "World History"],
    ),
    dict(
        id="deng_xiaoping", name="Deng Xiaoping", years="1904-1997", nationality="Chinese",
        field="paramount leader of China", wiki_title="Deng Xiaoping",
        significance="as China's paramount leader from the late 1970s, he launched market-oriented economic reforms that transformed China into one of the world's largest economies",
        facts=[
            "Deng Xiaoping was born in Sichuan province, China, in 1904, and studied in France as a young man, where he became involved in Communist politics",
            "He was purged from power twice during Mao Zedong's rule, including during the Cultural Revolution, before returning to prominence after Mao's death in 1976",
            "By the late 1970s he had become China's paramount leader, though he never held the top formal titles of president or party chairman",
            "He launched the 'Reform and Opening Up' policy beginning in 1978, introducing market-based economic reforms while maintaining one-party political control",
            "He established Special Economic Zones, including Shenzhen, which attracted foreign investment and became major manufacturing and trade hubs",
            "Under his leadership China negotiated the 1984 Sino-British Joint Declaration, agreeing on the 1997 handover of Hong Kong",
            "His government's violent suppression of the 1989 Tiananmen Square protests remains one of the most controversial episodes of his rule",
        ], related_subjects=["World History", "World Politics", "Business Studies"],
    ),
    dict(
        id="cleopatra", name="Cleopatra VII", years="69-30 BCE", nationality="Ptolemaic Egyptian (Greek-Egyptian)",
        field="Pharaoh of Egypt", wiki_title="Cleopatra",
        significance="the last active ruler of the Ptolemaic Kingdom of Egypt, her political alliances with Roman leaders Julius Caesar and Mark Antony placed her at the center of the power struggles that ended the Roman Republic",
        facts=[
            "Cleopatra VII was born in Alexandria, Egypt, in 69 BCE, into the Ptolemaic dynasty, a Greek-speaking royal family that had ruled Egypt since Alexander the Great's conquest",
            "She became co-ruler of Egypt in 51 BCE at around age 18, alongside her younger brother, as was customary in Ptolemaic royal succession",
            "She formed a political and personal alliance with Roman general Julius Caesar, which helped secure her position on the Egyptian throne",
            "After Caesar's assassination in 44 BCE, she allied with Roman general Mark Antony, and together they opposed the Roman leader Octavian for control of the Roman world",
            "She was fluent in multiple languages, reportedly including Egyptian, a rare linguistic accomplishment among the largely Greek-speaking Ptolemaic rulers of Egypt",
            "Following Antony and Cleopatra's defeat by Octavian's forces at the Battle of Actium in 31 BCE, both took their own lives in 30 BCE rather than be captured",
            "Her death marked the end of the Ptolemaic Kingdom, and Egypt subsequently became a province of the Roman Empire under Octavian, who took the title Augustus",
        ], related_subjects=["World History"],
    ),
    dict(
        id="catherine_the_great", name="Catherine the Great", years="1729-1796", nationality="Russian",
        field="Empress of Russia", wiki_title="Catherine the Great",
        significance="she ruled Russia for over three decades, expanding its territory significantly and promoting Enlightenment-influenced reforms in education, law, and the arts, becoming one of the most significant rulers in Russian history",
        facts=[
            "Catherine the Great was born Sophie of Anhalt-Zerbst in Stettin, Prussia (now Szczecin, Poland), in 1729, and was married to the future Russian Tsar Peter III as a teenager",
            "She came to power in 1762 following a coup that deposed her husband, Peter III, shortly after he ascended the throne",
            "During her 34-year reign she significantly expanded Russian territory, including through wars against the Ottoman Empire and the partitions of Poland",
            "She corresponded extensively with Enlightenment philosophers, including Voltaire and Diderot, and sought to apply some Enlightenment ideas to Russian governance and education",
            "She founded the Smolny Institute in 1764, one of the first state-financed institutions of higher education for women in Europe",
            "She oversaw a major expansion of the Hermitage art collection in St. Petersburg, which remains one of the largest and most significant art museums in the world",
            "She died in 1796, having ruled Russia longer than any other female leader in its history",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="ho_chi_minh", name="Ho Chi Minh", years="1890-1969", nationality="Vietnamese",
        field="revolutionary leader and President of North Vietnam", wiki_title="Ho Chi Minh",
        significance="he led Vietnam's independence movement against French colonial rule and later against the United States, becoming the founding president of North Vietnam and a lasting symbol of Vietnamese national independence",
        facts=[
            "Ho Chi Minh was born Nguyen Sinh Cung in central Vietnam in 1890, then part of French Indochina",
            "He spent decades living abroad, including in France, the Soviet Union, and China, where he became involved in Communist and anti-colonial political movements",
            "He founded the Viet Minh independence movement in 1941 to resist both Japanese occupation during World War II and French colonial rule",
            "He declared Vietnamese independence in 1945, quoting portions of the American Declaration of Independence in his announcement speech",
            "He led North Vietnamese forces against France in the First Indochina War, which ended with French withdrawal in 1954 and Vietnam's division into North and South",
            "He served as president of North Vietnam and remained a central symbolic and political leader during the escalating Vietnam War against South Vietnam and the United States",
            "He died in 1969, six years before North Vietnamese forces achieved final victory and reunified the country in 1975; Vietnam's largest city, Saigon, was renamed Ho Chi Minh City in his honor",
        ], related_subjects=["World History", "World Politics"],
    ),
    dict(
        id="willy_brandt", name="Willy Brandt", years="1913-1992", nationality="German",
        field="Chancellor of West Germany", wiki_title="Willy Brandt",
        significance="as Chancellor of West Germany, his Ostpolitik policy of engagement with Eastern Bloc countries helped ease Cold War tensions, and he won the Nobel Peace Prize in 1971",
        facts=[
            "Willy Brandt was born Herbert Ernst Karl Frahm in Lubeck, Germany, in 1913, and fled to Norway in 1933 to escape Nazi persecution of his political activism, later adopting the name Willy Brandt",
            "He served as mayor of West Berlin from 1957 to 1966, a period that included the construction of the Berlin Wall in 1961",
            "He became Chancellor of West Germany in 1969, leading the Social Democratic Party",
            "He pursued a policy known as Ostpolitik, seeking greater diplomatic engagement and normalized relations with East Germany, Poland, and the Soviet Union, easing Cold War tensions in Europe",
            "In a famous 1970 gesture during a visit to Warsaw, he spontaneously knelt before a memorial to victims of the Warsaw Ghetto Uprising, a widely remembered act of acknowledgment for Nazi-era crimes",
            "He won the Nobel Peace Prize in 1971 for his efforts to reduce tensions between Eastern and Western Europe",
            "He resigned as Chancellor in 1974 after it was revealed that a close aide had been a spy for East Germany, though he remained politically active for years afterward",
        ], related_subjects=["World History", "World Politics"],
    ),
]


def main() -> None:
    upsert_section(
        "world_leaders_politics",
        "World Leaders & Politics",
        "🏛️",
        "Presidents, prime ministers, monarchs, and independence leaders who shaped nations and international politics.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
