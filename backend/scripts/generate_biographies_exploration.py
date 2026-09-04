#!/usr/bin/env python3
"""Populate the "Exploration & Military History" biography category with
real, verified explorers and military leaders. See _biography_engine.py
for the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_exploration.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="alexander_the_great", name="Alexander the Great", years="356-323 BCE", nationality="Macedonian Greek",
        field="king and military commander", wiki_title="Alexander the Great",
        significance="he built one of the largest empires of the ancient world by age 30, conquering territory stretching from Greece to northwestern India without suffering a major military defeat",
        facts=[
            "Alexander the Great was born in Pella, Macedon, in 356 BCE, and was tutored as a young man by the philosopher Aristotle",
            "He became king of Macedon in 336 BCE, at age 20, after the assassination of his father, King Philip II",
            "He led his army in a series of campaigns against the Persian Empire beginning in 334 BCE, decisively defeating King Darius III",
            "He founded more than 20 cities bearing his name across his empire, the most famous being Alexandria in Egypt",
            "He led his forces as far east as the Indus River in present-day Pakistan and India before his army, exhausted after years of campaigning, refused to advance further",
            "His empire stretched from Greece to Egypt to Central Asia, one of the largest in the ancient world",
            "He died in Babylon in 323 BCE at age 32, and his empire quickly fragmented among his generals after his death",
        ], related_subjects=["World History"],
    ),
    dict(
        id="ferdinand_magellan", name="Ferdinand Magellan", years="1480-1521", nationality="Portuguese",
        field="explorer and navigator", wiki_title="Ferdinand Magellan",
        significance="he led the first expedition to sail from the Atlantic Ocean to the Pacific Ocean, and though he died before its completion, his expedition became the first to circumnavigate the globe",
        facts=[
            "Ferdinand Magellan was born in Portugal around 1480 and initially served the Portuguese crown before sailing under the flag of Spain",
            "In 1519 he set out from Spain with a fleet of five ships to find a westward route to the Spice Islands of Southeast Asia",
            "His fleet discovered and navigated the strait at the southern tip of South America now named the Strait of Magellan",
            "His fleet was the first European expedition to cross the Pacific Ocean, a journey that took over three months and caused severe food and water shortages among the crew",
            "He was killed in April 1521 in the Battle of Mactan in the Philippines, after intervening in a local conflict",
            "One of his original five ships, the Victoria, eventually completed the journey back to Spain in 1522, becoming the first vessel to circumnavigate the globe",
            "Of the roughly 270 crew members who began the voyage, only about 18 returned to Spain aboard the Victoria",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="marco_polo", name="Marco Polo", years="1254-1324", nationality="Venetian (Italian)",
        field="merchant and explorer", wiki_title="Marco Polo",
        significance="his account of his travels along the Silk Road to the court of the Mongol emperor Kublai Khan introduced medieval Europeans to detailed knowledge of Asia and remained influential for centuries",
        facts=[
            "Marco Polo was born in the Republic of Venice in 1254, into a family of merchants",
            "At age 17 he set out with his father and uncle on an overland journey along the Silk Road to China, arriving around 1275",
            "He reportedly spent about 17 years in the service of the Mongol emperor Kublai Khan, traveling extensively across the Mongol Empire",
            "After returning to Venice, he was captured during a war with Genoa and imprisoned, during which time he dictated his travel accounts to a fellow prisoner, the writer Rustichello da Pisa",
            "The resulting book, commonly known as The Travels of Marco Polo, became one of the most widely read travel accounts in medieval Europe",
            "His descriptions of Chinese cities, wealth, and customs were so unfamiliar to European readers that some contemporaries doubted their accuracy",
            "His account is believed to have influenced later explorers, including Christopher Columbus, who reportedly owned an annotated copy",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="ernest_shackleton", name="Ernest Shackleton", years="1874-1922", nationality="Anglo-Irish",
        field="polar explorer", wiki_title="Ernest Shackleton",
        significance="his leadership during the failed 1914-1917 Imperial Trans-Antarctic Expedition, in which he saved his entire crew after their ship was crushed by ice, became one of history's most celebrated survival stories",
        facts=[
            "Ernest Shackleton was born in Kilkea, Ireland, in 1874",
            "He participated in several earlier Antarctic expeditions, including Robert Falcon Scott's Discovery Expedition of 1901-1904",
            "In 1914 he led the Imperial Trans-Antarctic Expedition aboard the ship Endurance, aiming to cross Antarctica overland for the first time",
            "The Endurance became trapped and was eventually crushed by pack ice in the Weddell Sea in late 1915, stranding the crew of 28 men",
            "He led his men across drifting ice floes and then in small lifeboats to Elephant Island, then made an 800-mile open-boat journey to South Georgia island to seek rescue",
            "He then crossed South Georgia's mountainous, previously unmapped interior on foot to reach a whaling station and organize a rescue mission",
            "Remarkably, every member of his 28-man crew survived the ordeal, and he died in 1922 during a subsequent expedition, before reaching Antarctica",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="amelia_earhart", name="Amelia Earhart", years="1897-1937", nationality="American",
        field="aviator", wiki_title="Amelia Earhart",
        significance="the first woman to fly solo across the Atlantic Ocean, she became one of the most celebrated aviators in history before disappearing during an attempt to fly around the world in 1937",
        facts=[
            "Amelia Earhart was born in Atchison, Kansas, in 1897, and took her first flying lesson in 1921",
            "In 1928 she became the first woman to fly across the Atlantic Ocean as a passenger, and in 1932 she became the first woman to fly across it solo",
            "She set numerous other aviation records during the 1920s and 1930s, including speed and distance records",
            "She was a founding member of the Ninety-Nines, an organization supporting female aviators, and served as its first president",
            "In 1937 she attempted to become the first woman to fly around the world at its equatorial route, along with navigator Fred Noonan",
            "Her aircraft disappeared over the central Pacific Ocean in July 1937 during that attempt, and despite extensive searches, neither she nor the plane were ever definitively found",
            "Her disappearance remains one of the most enduring mysteries in aviation history, and continues to be the subject of ongoing investigation and speculation",
        ], related_subjects=["World History"],
    ),
    dict(
        id="ibn_battuta", name="Ibn Battuta", years="1304-1368/1369", nationality="Moroccan",
        field="scholar and explorer", wiki_title="Ibn Battuta",
        significance="over roughly 30 years he traveled an estimated 75,000 miles across North Africa, the Middle East, Asia, and parts of Europe, producing one of the most extensive travel accounts of the medieval world",
        facts=[
            "Ibn Battuta was born in Tangier, Morocco, in 1304, into a family of Islamic legal scholars",
            "He set out in 1325 at age 21 on what was originally intended as a pilgrimage to Mecca, but which expanded into decades of continued travel",
            "Over roughly 30 years he traveled through North Africa, the Middle East, East Africa, Central Asia, South Asia, Southeast Asia, and China",
            "He is estimated to have traveled around 75,000 miles in total, far surpassing the travels of his contemporary, the Venetian Marco Polo",
            "He served as a judge (qadi) in several regions during his travels, drawing on his training in Islamic law",
            "After returning to Morocco, he dictated an account of his travels, known as the Rihla, at the request of the Sultan of Morocco",
            "The Rihla remains a major historical source for understanding the social, political, and religious life of the medieval Islamic world",
        ], related_subjects=["World History", "Geography", "World Religions"],
    ),
    dict(
        id="zheng_he", name="Zheng He", years="1371-1433/1435", nationality="Chinese",
        field="admiral and explorer", wiki_title="Zheng He",
        significance="he commanded seven major naval expeditions for the Chinese Ming dynasty, leading fleets far larger than any European fleet of the time as far as East Africa, decades before European voyages of exploration",
        facts=[
            "Zheng He was born in Yunnan province, China, around 1371, into a Muslim family, and was captured and brought into imperial service as a young boy",
            "He rose to become a trusted admiral and court official under the Ming dynasty's Yongle Emperor",
            "Between 1405 and 1433 he led seven major naval expeditions, commanding fleets that at their peak included over 300 ships and tens of thousands of sailors",
            "His fleets were vastly larger than the ships later used by European explorers such as Columbus and Vasco da Gama, which typically numbered only a few vessels",
            "His voyages reached Southeast Asia, India, the Arabian Peninsula, and the eastern coast of Africa",
            "The expeditions were intended to project Chinese power and expand tributary relationships, rather than to establish colonies",
            "After the Yongle Emperor's death, subsequent Ming rulers largely ended the voyages, and China turned toward a more inward-looking foreign policy for centuries afterward",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="george_s_patton", name="George S. Patton", years="1885-1945", nationality="American",
        field="US Army general", wiki_title="George S. Patton",
        significance="a hard-driving and controversial commander, his leadership of the US Third Army during the 1944-1945 campaign across France and Germany, including the relief of Bastogne, made him one of the most well-known American generals of World War II",
        facts=[
            "George S. Patton was born in San Gabriel, California, in 1885, and graduated from the US Military Academy at West Point",
            "He competed in the modern pentathlon at the 1912 Stockholm Olympics, representing the United States",
            "He commanded American tank forces in North Africa and Sicily during World War II, developing a reputation for aggressive, fast-moving armored warfare",
            "He commanded the US Third Army during the 1944 breakout from Normandy, driving rapidly across France after the D-Day landings",
            "His forces played a key role in relieving the besieged town of Bastogne during the Battle of the Bulge in December 1944",
            "He was known for a controversial and outspoken public persona, including a 1943 incident in which he slapped a hospitalized soldier suffering from combat stress, which drew significant public criticism",
            "He died in December 1945 from injuries sustained in a car accident in Germany, shortly after the war's end",
        ], related_subjects=["World History"],
    ),
    dict(
        id="hannibal_barca", name="Hannibal Barca", years="247-183/181 BCE", nationality="Carthaginian",
        field="military commander", wiki_title="Hannibal",
        significance="one of history's greatest military strategists, he led an army including war elephants across the Alps to invade Roman Italy during the Second Punic War, winning a series of major battles against Rome",
        facts=[
            "Hannibal Barca was born in Carthage, in present-day Tunisia, in 247 BCE, into a prominent military family",
            "He took command of Carthaginian forces in Spain at age 26, following the death of his brother-in-law",
            "In 218 BCE he led an army, including war elephants, on a famously difficult crossing of the Alps to invade Italy directly, catching Rome by surprise",
            "He won a series of major victories against Roman forces in Italy, most notably at the Battle of Cannae in 216 BCE, still studied today as a model of tactical encirclement",
            "Despite these victories, he was never able to capture the city of Rome itself, and the war eventually turned against Carthage",
            "He was recalled to Africa to defend Carthage and was defeated by the Roman general Scipio Africanus at the Battle of Zama in 202 BCE",
            "He spent his later years in exile, eventually taking his own life around 183-181 BCE to avoid capture by Roman forces",
        ], related_subjects=["World History"],
    ),
    dict(
        id="roald_amundsen", name="Roald Amundsen", years="1872-1928", nationality="Norwegian",
        field="polar explorer", wiki_title="Roald Amundsen",
        significance="he led the first expedition to reach the geographic South Pole, in December 1911, narrowly beating a rival British expedition led by Robert Falcon Scott",
        facts=[
            "Roald Amundsen was born near Oslo, Norway, in 1872",
            "He was part of the first expedition to successfully navigate the Northwest Passage through the Canadian Arctic, completed between 1903 and 1906",
            "In 1910 he set out for Antarctica, having secretly redirected an expedition originally planned for the Arctic once he learned of a rival American attempt to reach the North Pole first",
            "His team reached the South Pole on December 14, 1911, using dog sleds and detailed cold-weather planning, about five weeks ahead of the rival British expedition led by Robert Falcon Scott",
            "Scott's entire party died on the return journey, while Amundsen's team returned safely, a contrast that has been studied extensively for lessons in polar expedition planning",
            "In 1926 he was part of the first expedition verified to have reached the North Pole, aboard the airship Norge",
            "He disappeared in 1928 while participating in a rescue mission for a fellow explorer whose airship had crashed in the Arctic, and was never found",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="christopher_columbus", name="Christopher Columbus", years="1451-1506", nationality="Genoese (Italian)",
        field="explorer and navigator", wiki_title="Christopher Columbus",
        significance="his 1492 voyage, sponsored by the Spanish crown, initiated sustained European contact with the Americas, an event with enormous and lasting historical consequences, both transformative and, for indigenous peoples, deeply destructive",
        facts=[
            "Christopher Columbus was born in Genoa, in present-day Italy, in 1451",
            "He spent years seeking sponsorship for a westward voyage to reach Asia before Spain's Queen Isabella and King Ferdinand agreed to fund his expedition in 1492",
            "He set sail with three ships, the Nina, the Pinta, and the Santa Maria, in August 1492, reaching land in the Bahamas in October of that year",
            "He made three further voyages to the Caribbean and parts of Central and South America between 1493 and 1504, though he remained convinced until his death that he had reached parts of Asia",
            "His voyages initiated sustained contact between Europe and the Americas, leading to centuries of colonization that had catastrophic consequences for indigenous populations through violence, forced labor, and introduced disease",
            "He served as governor of the Spanish colony of Hispaniola, and was eventually removed from the position and briefly arrested following reports of harsh and mismanaged rule",
            "He died in Spain in 1506, and his historical legacy remains a subject of significant ongoing debate and reassessment",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="florence_nightingale", name="Florence Nightingale", years="1820-1910", nationality="British",
        field="nurse and statistician", wiki_title="Florence Nightingale",
        significance="her work reforming military hospital sanitation during the Crimean War established the foundations of modern nursing, and she was also a pioneering statistician who used data visualization to advocate for public health reform",
        facts=[
            "Florence Nightingale was born in Florence, Italy, in 1820, to a wealthy British family, and was named after the city of her birth",
            "In 1854 she led a team of nurses to military hospitals during the Crimean War, where she found appalling sanitary conditions contributing heavily to soldier deaths",
            "Her reforms to hospital hygiene and sanitation dramatically reduced death rates among wounded soldiers",
            "She became known as 'the Lady with the Lamp' for her nighttime rounds checking on patients",
            "She was a pioneering statistician, developing an early form of the pie chart, called the 'coxcomb' or polar area diagram, to visually demonstrate that most soldier deaths were from preventable disease rather than battle wounds",
            "In 1860 she founded the Nightingale Training School for Nurses at St. Thomas' Hospital in London, one of the first formal nursing schools",
            "She became the first woman awarded Britain's Order of Merit, in 1907, three years before her death in 1910",
        ], related_subjects=["World History", "Health Education"],
    ),
    dict(
        id="genghis_khan", name="Genghis Khan", years="c. 1162-1227", nationality="Mongolian",
        field="founder and ruler of the Mongol Empire", wiki_title="Genghis Khan",
        significance="he unified the Mongol tribes and founded the Mongol Empire, which became the largest contiguous land empire in history, stretching across much of Asia and into Europe",
        facts=[
            "Genghis Khan was born Temujin around 1162 in what is now Mongolia, into a difficult and impoverished early life after his father's death",
            "He gradually built alliances and defeated rival tribal leaders, and in 1206 was proclaimed ruler of a newly unified Mongol confederation, taking the title Genghis Khan",
            "He organized his military using a highly disciplined decimal system, with units of ten, and enforced strict loyalty and meritocracy among his commanders",
            "His campaigns expanded Mongol control across Central Asia, northern China, and into parts of the Middle East and Eastern Europe",
            "Under his rule and that of his successors, the Mongol Empire became the largest contiguous land empire in history, at its peak stretching from Korea to Eastern Europe",
            "His conquests also facilitated the Pax Mongolica, a period of relative stability that increased trade and cultural exchange along the Silk Road",
            "He died in 1227 during a military campaign, and the location of his burial site remains unknown, deliberately kept secret according to Mongol tradition",
        ], related_subjects=["World History"],
    ),
    dict(
        id="julius_caesar", name="Julius Caesar", years="100-44 BCE", nationality="Ancient Roman",
        field="general and statesman", wiki_title="Julius Caesar",
        significance="his military conquest of Gaul and his subsequent rise to power fundamentally transformed the Roman Republic, and his assassination in 44 BCE precipitated the transition to the Roman Empire",
        facts=[
            "Julius Caesar was born in Rome in 100 BCE into a patrician family that claimed descent from the legendary Trojan prince Aeneas",
            "He led Roman military campaigns in Gaul (roughly modern France) between 58 and 50 BCE, ultimately conquering the entire region and briefly invading Britain",
            "In 49 BCE he led his army across the Rubicon River into Italy in defiance of the Roman Senate, sparking a civil war, giving rise to the phrase 'crossing the Rubicon' to describe a point of no return",
            "He defeated his rival Pompey and became effectively the sole ruler of Rome, being declared dictator, eventually for life, in 44 BCE",
            "He implemented significant reforms during his rule, including a new calendar, the Julian calendar, which remained the basis of the Western calendar for over 1,600 years",
            "He was assassinated on March 15, 44 BCE (the 'Ides of March') by a group of Roman senators, including Brutus and Cassius, who feared his growing power threatened the Republic",
            "His death led to further civil war and the eventual rise of his adopted heir Octavian, who became Rome's first emperor as Augustus",
        ], related_subjects=["World History"],
    ),
    dict(
        id="matthew_henson", name="Matthew Henson", years="1866-1955", nationality="American",
        field="polar explorer", wiki_title="Matthew Henson",
        significance="an African American explorer who was part of the 1909 expedition widely credited as the first to reach the North Pole, his crucial contributions went largely unrecognized for decades due to racial discrimination",
        facts=[
            "Matthew Henson was born in Charles County, Maryland, in 1866, to parents who had been sharecroppers",
            "He went to sea as a cabin boy at around age 12, and later met explorer Robert Peary, who hired him as an assistant for polar expeditions",
            "He accompanied Peary on numerous Arctic expeditions over more than two decades, developing expert skills in dog-sledding and Inuit survival techniques, including learning the Inuktitut language",
            "On the 1909 expedition, historical accounts indicate Henson was actually the first of the party to reach the location identified as the North Pole, arriving slightly ahead of Peary",
            "Despite his central role, he received far less recognition and financial reward than Peary for decades afterward, largely due to the racial attitudes of the era",
            "He published a memoir, A Negro Explorer at the North Pole, in 1912, but wider public recognition did not come until much later in his life",
            "In 1954 President Dwight Eisenhower honored him at the White House, and he was posthumously awarded numerous honors recognizing his role in the historic expedition",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="sacagawea", name="Sacagawea", years="c. 1788-1812", nationality="Lemhi Shoshone (American)",
        field="guide and interpreter", wiki_title="Sacagawea",
        significance="a Lemhi Shoshone woman who served as an interpreter and guide for the Lewis and Clark Expedition, her knowledge and diplomatic presence were vital to the expedition's survival and success in traveling across western North America",
        facts=[
            "Sacagawea was born around 1788 into the Lemhi Shoshone people in what is now Idaho",
            "As a young girl she was captured by a rival tribe and later sold to a French-Canadian fur trader, Toussaint Charbonneau, who became her husband",
            "In 1804 she and Charbonneau joined the Lewis and Clark Expedition as interpreters, while she was pregnant, and gave birth to her son early in the journey",
            "Her knowledge of Shoshone language and territory proved essential when the expedition needed to trade with Shoshone people for horses to cross the Rocky Mountains",
            "Her presence, along with her infant son, is often cited by historians as having signaled to other Native groups that the expedition was peaceful, since war parties did not typically travel with women and children",
            "She helped the expedition identify edible plants and navigate portions of the journey, drawing on knowledge of the region from her childhood",
            "She died around 1812, and later became one of the most commemorated women in American history, memorialized on the US dollar coin issued beginning in 2000",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="yuri_gagarin", name="Yuri Gagarin", years="1934-1968", nationality="Soviet (Russian)",
        field="cosmonaut", wiki_title="Yuri Gagarin",
        significance="on April 12, 1961, he became the first human to travel into outer space, completing a single orbit of Earth aboard Vostok 1, a landmark achievement of the Soviet space program during the Cold War",
        facts=[
            "Yuri Gagarin was born in Klushino, in the Soviet Union, in 1934, and trained as a fighter pilot before being selected for the Soviet space program",
            "On April 12, 1961, he launched aboard the Vostok 1 spacecraft, becoming the first human being to travel into outer space",
            "His single orbit of Earth lasted 108 minutes, and he reentered the atmosphere and ejected from the capsule, landing safely by parachute in a field",
            "His flight was a major achievement in the Cold War Space Race between the Soviet Union and the United States, occurring just weeks before the first American spaceflight",
            "He became an international celebrity following his flight, touring numerous countries and receiving enormous public receptions",
            "He was appointed deputy training director of the Cosmonaut Training Centre, later named the Yuri Gagarin Cosmonaut Training Centre in his honor",
            "He died in 1968 in a jet training accident, at age 34, and April 12, the anniversary of his flight, is now celebrated internationally as the Yuri's Night and the International Day of Human Space Flight",
        ], related_subjects=["World History", "Physics"],
    ),
    dict(
        id="neil_armstrong", name="Neil Armstrong", years="1930-2012", nationality="American",
        field="astronaut", wiki_title="Neil Armstrong",
        significance="on July 20, 1969, he became the first human being to walk on the Moon, commanding NASA's Apollo 11 mission and declaring it 'one small step for man, one giant leap for mankind'",
        facts=[
            "Neil Armstrong was born in Wapakoneta, Ohio, in 1930, and earned his student pilot's license before his 16th birthday",
            "He flew combat missions as a US Navy pilot during the Korean War before becoming a test pilot and later a NASA astronaut",
            "He commanded NASA's Gemini 8 mission in 1966, successfully performing the first docking of two spacecraft in orbit despite a serious in-flight malfunction",
            "He commanded the Apollo 11 mission, which launched on July 16, 1969, aiming to fulfill President Kennedy's 1961 goal of landing astronauts on the Moon before the end of the decade",
            "On July 20, 1969, he became the first human to step onto the lunar surface, famously declaring, 'That's one small step for man, one giant leap for mankind'",
            "He and fellow astronaut Buzz Aldrin spent about two and a half hours outside the lunar module, collecting samples and conducting experiments, while Michael Collins orbited above in the command module",
            "He largely avoided public attention after his NASA career, later teaching aerospace engineering, and died in 2012",
        ], related_subjects=["World History", "Physics"],
    ),
    dict(
        id="thor_heyerdahl", name="Thor Heyerdahl", years="1914-2002", nationality="Norwegian",
        field="explorer and ethnographer", wiki_title="Thor Heyerdahl",
        significance="his 1947 Kon-Tiki expedition, crossing the Pacific Ocean on a hand-built balsa wood raft, tested his theory that ancient South Americans could have settled Polynesia, and became one of the most celebrated adventure voyages of the 20th century",
        facts=[
            "Thor Heyerdahl was born in Larvik, Norway, in 1914, and studied zoology and geography before turning to ethnographic exploration",
            "He developed a theory that pre-Columbian South Americans might have been capable of sailing to and settling Polynesian islands, a view that contradicted the prevailing academic consensus of the time",
            "To test whether such a voyage was physically possible with ancient technology, he and a small crew built a raft, the Kon-Tiki, using only materials and techniques available to ancient South Americans",
            "In 1947 he and his crew sailed the Kon-Tiki raft roughly 4,300 miles across the Pacific Ocean from Peru, reaching Polynesia after 101 days at sea",
            "His 1948 book about the voyage, Kon-Tiki, became an international bestseller, and the accompanying documentary film won the 1951 Academy Award for Best Documentary Feature",
            "He later led additional experimental voyages, including reed-boat expeditions named Ra and Ra II, testing possible ancient contact across the Atlantic Ocean",
            "Later genetic research has provided more nuanced findings on Polynesian ancestry, but his voyages remain celebrated as landmark demonstrations of ancient seafaring capability",
        ], related_subjects=["World History", "Geography"],
    ),
    dict(
        id="william_wallace", name="William Wallace", years="c. 1270-1305", nationality="Scottish",
        field="military leader", wiki_title="William Wallace",
        significance="he led Scottish forces in resistance against English rule during the Wars of Scottish Independence, becoming a lasting national symbol of Scottish independence after his execution by the English crown",
        facts=[
            "William Wallace was born around 1270 in Scotland, into a family of relatively minor gentry, though many details of his early life remain uncertain",
            "He emerged as a leader of Scottish resistance against English rule following King Edward I of England's efforts to assert direct control over Scotland in the 1290s",
            "He led Scottish forces to a major victory over a larger English army at the Battle of Stirling Bridge in 1297",
            "Following that victory he was appointed Guardian of Scotland, a title recognizing his leadership of the kingdom in the absence of an accepted king",
            "He was defeated by English forces at the Battle of Falkirk in 1298, after which he largely stepped back from formal leadership while continuing to resist English rule",
            "He was captured near Glasgow in 1305 and executed in London by hanging, drawing, and quartering, a brutal punishment reserved for those convicted of treason",
            "He became a lasting symbol of Scottish independence, and his story was popularized internationally by the 1995 film Braveheart, though historians note the film takes considerable dramatic license with the historical record",
        ], related_subjects=["World History"],
    ),
]


def main() -> None:
    upsert_section(
        "exploration_military",
        "Exploration & Military History",
        "🧭",
        "Explorers, navigators, and military leaders whose journeys and campaigns expanded the known world and reshaped its history.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
