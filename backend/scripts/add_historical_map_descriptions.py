#!/usr/bin/env python3
"""Add a longer, region-specific `description` field to every region marker
in the History Atlas (backend/data/historical_maps/historical_maps.json),
alongside the existing short `note`. Each entry is real, hand-written
historical content distinct per region -- not a shared template -- covering
context the short note doesn't have room for (who ruled, what the place
was like, what came before/after, why it mattered).

DESCRIPTIONS[period_id] = {region_name: description_text}

Idempotent: only fills `description` where missing.

Re-run after editing:
    python3 backend/scripts/add_historical_map_descriptions.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
HISTORICAL_MAPS_PATH = BASE_DIR / "data" / "historical_maps" / "historical_maps.json"

DESCRIPTIONS: dict[str, dict[str, str]] = {}

DESCRIPTIONS["deep_prehistory"] = {
    "Ubaid & Uruk period Mesopotamia (Uruk)": "Uruk grew from a scatter of villages into the first settlement most archaeologists call a true city, eventually housing tens of thousands of people behind a wall later legend credited to the hero-king Gilgamesh. Its temple precincts organized farming surpluses, labor, and trade on a scale no earlier society had managed, and by around 3400 BCE its accountants were pressing the first proto-cuneiform marks into clay to track it all.",
    "Naqada culture Egypt (Naqada)": "Centered on the Upper Egyptian town that gives it its name, the Naqada culture spanned roughly 4000 to 3000 BCE and left behind elaborately painted pottery, early hieroglyph-like symbols, and increasingly rich elite graves. Its gradual consolidation of smaller chiefdoms along the Nile set the political and religious template that Egypt's first pharaohs would inherit when they unified the kingdom shortly after this period.",
    "Yangshao culture China (Banpo)": "The Banpo village site near modern Xi'an preserves one of the best-studied Yangshao settlements: round semi-subterranean houses arranged around a central plaza, millet farming, and painted red pottery decorated with fish and human-face motifs. Yangshao communities like this one represent one of the earliest Neolithic farming traditions along the Yellow River, centuries before China's first dynasties.",
    "Vinca culture Europe (Vinca, near Belgrade)": "Excavated on the banks of the Danube near Belgrade, the Vinca culture built some of prehistoric Europe's largest settlements and left behind thousands of small clay and stone objects marked with repeated symbols -- the so-called Vinca signs, among the oldest systematic marking systems in Europe, though scholars still debate whether they amount to true writing. The culture also pioneered early copper smelting, among the earliest metalworking anywhere.",
    "Megalithic Atlantic Europe (Newgrange, Ireland)": "Newgrange is a vast passage tomb in Ireland's Boyne Valley, built around 3200 BCE from an estimated 200,000 tonnes of material -- centuries before the Great Pyramid or Stonehenge's famous stone circle. Its inner chamber is engineered so that sunlight floods the passage only at dawn on the winter solstice, a precise astronomical alignment that still works perfectly over 5,000 years later.",
}

DESCRIPTIONS["century_30_bce"] = {
    "Early Dynastic Sumer (Ur)": "Ur was one of several rival Sumerian city-states jockeying for influence in this era, long before its later fame for the spectacular royal tombs of the Early Dynastic III period. Like its neighbors, it was ruled by a king who claimed divine backing, organized irrigation along the Euphrates, and fought periodic wars over land and water rights with cities like Uruk and Lagash.",
    "Early Dynastic Egypt (Memphis)": "Founded around the start of Egypt's First Dynasty as the new capital of the just-unified kingdom, Memphis sat strategically at the boundary between Upper and Lower Egypt, symbolizing the joining of the two lands. Tradition credits its founding to Menes (likely the same ruler as Narmer), and the city would remain one of Egypt's most important centers for the next three thousand years.",
    "Early Harappan Indus Valley (Harappa)": "At this stage Harappa was still a cluster of growing village settlements along the Indus and its tributaries, not yet the planned city it would become. Farmers here were already cultivating wheat and barley and keeping domesticated cattle, laying the economic groundwork for the dense urban centers that would define the mature Indus Valley Civilization a few centuries later.",
}

DESCRIPTIONS["century_29_bce"] = {
    "Early Dynastic Sumer (Uruk)": "Uruk remained one of the largest and most politically influential cities in Sumer during this century, its massive temple complexes at the heart of a landscape of rival city-states. Its scribal traditions, descended from the proto-writing developed there centuries earlier, were spreading to other Sumerian cities as the standard way to record transactions, offerings, and royal deeds.",
    "Neolithic Britain (Stonehenge)": "The earliest phase of Stonehenge -- a circular ditch and bank enclosure with a ring of pits known as the Aubrey Holes -- was built around this century, long before the massive sarsen stones familiar today were raised. Even in this first form, the site's alignment with the solstices suggests its builders were already tracking the sun's yearly cycle with real precision.",
    "Old Kingdom Egypt (Memphis)": "Egypt's Early Dynastic kings, ruling from Memphis, were steadily consolidating control over the full length of the Nile Valley, standardizing administration and religious practice across a kingdom that had only recently been two separate lands. Royal tombs of this era, built at Abydos and Saqqara, show increasingly elaborate funerary architecture that would eventually give rise to the pyramids.",
}

DESCRIPTIONS["century_28_bce"] = {
    "Early Dynastic Sumer (Kish)": "Kish held a special prestige among Sumerian cities: tradition held that kingship itself had descended from heaven to Kish after a mythical great flood, and for centuries afterward the title 'King of Kish' carried symbolic authority over Sumer even for rulers based elsewhere. Its real political power rose and fell with its rivalries against Uruk, Ur, and Lagash.",
    "Old Kingdom Egypt (Memphis)": "As Egypt's Second Dynasty gave way to the Third around this time, Memphis-based kings were setting the stage for a dramatic architectural leap: within a generation or two, the step pyramid of Djoser at nearby Saqqara would transform royal tomb-building from mudbrick mastabas into the world's first large-scale cut-stone monument.",
    "Indus Valley (Mohenjo-daro, early phase)": "Long before its famous grid-planned streets and covered drains, Mohenjo-daro began as a smaller settlement on the Indus floodplain. Archaeologists have found earlier occupation layers beneath the mature city, showing a gradual build-up of population and craft specialization -- pottery, bead-making, metalworking -- that preceded the dramatic urban planning the site is best known for.",
}

DESCRIPTIONS["century_27_bce"] = {
    "Old Kingdom Egypt (Saqqara)": "At Saqqara, the architect Imhotep designed the Step Pyramid for King Djoser by stacking six mastaba-like tiers atop one another -- the world's oldest known large-scale building made entirely of cut stone. It marked a decisive break from earlier mudbrick royal tombs and set Egypt on the path toward the true pyramids of the next century.",
    "Early Dynastic Sumer (Uruk)": "Uruk's legendary status only grew in this era as the traditional home of Gilgamesh, a historical king of the city later transformed into the hero of Mesopotamia's great epic poem. Archaeology confirms Uruk's real political importance in this period even as its mythic reputation was already taking shape in oral tradition.",
    "Early Dynastic Sumer (Lagash)": "Lagash was emerging as one of Sumer's most powerful city-states, its territory bordering its smaller neighbor Umma along a stretch of disputed farmland. The two cities' quarrel over this border -- fought with both armies and, later, inscribed treaties -- would become one of the earliest territorial conflicts preserved in written record.",
}

DESCRIPTIONS["century_26_bce"] = {
    "Old Kingdom Egypt (Giza)": "The Great Pyramid, built at Giza for Pharaoh Khufu around 2560 BCE, required an estimated 2.3 million limestone blocks and remained the tallest human-made structure on Earth for nearly 3,800 years. It is the only one of the ancient world's Seven Wonders still largely intact, a testament to the organizational power of Egypt's Old Kingdom state.",
    "Mature Harappan Indus Valley (Mohenjo-daro)": "By this century Mohenjo-daro had blossomed into its famous mature phase: a meticulously grid-planned city with standardized baked-brick construction, a sophisticated covered drainage system, and a large public bathing structure whose exact purpose is still debated. Its uniformity of weights, seals, and city layout across the wider Indus Valley civilization suggests an unusually standardized society for its time.",
    "Early Dynastic Sumer (Ur)": "Ur continued to flourish as one of Sumer's leading cities in this period, its merchants trading as far as the Persian Gulf and beyond. The spectacular royal tombs that would make Ur famous to modern archaeologists -- filled with gold, lapis lazuli, and the remains of royal attendants -- belong to roughly this era.",
}

DESCRIPTIONS["century_25_bce"] = {
    "Old Kingdom Egypt (Abusir)": "Fifth Dynasty pharaohs built a cluster of pyramids and distinctive sun temples at Abusir, reflecting the growing prominence of the sun god Ra in Egyptian royal religion during this period. The site's temple reliefs and administrative papyri -- among the oldest papyrus archives to survive -- offer an unusually detailed window into how the Old Kingdom state actually functioned.",
    "Early Dynastic Sumer (Lagash)": "After a hard-fought victory over neighboring Umma, Lagash's ruler Eannatum commissioned the Stele of the Vultures, a carved limestone monument celebrating the triumph -- one of the earliest known artworks to commemorate a specific historical battle and an early milestone in the use of art as political propaganda.",
    "Early Dynastic Sumer (Umma)": "Umma's long rivalry with Lagash over fertile border farmland produced some of the earliest surviving written treaties and boundary inscriptions in human history. The conflict simmered on and off for generations, with each city's scribes carefully recording their own version of events on clay.",
}

DESCRIPTIONS["century_24_bce"] = {
    "Akkadian Empire (Akkad, exact site unknown)": "Sargon of Akkad built what historians generally consider the world's first true empire, uniting the independent Sumerian city-states under one ruler and extending Akkadian control from the Persian Gulf toward the Mediterranean. Remarkably, despite centuries of searching, archaeologists have never definitively located the ruins of Akkad itself -- it remains one of history's great lost capitals.",
    "Sumer (Uruk, now under Akkadian rule)": "Along with the other great Sumerian cities, Uruk lost its political independence to Sargon's new empire, though its temples, scribal schools, and cultural prestige continued largely undisturbed. Akkadian rulers generally preferred to absorb and govern existing Sumerian institutions rather than destroy them.",
    "Old Kingdom Egypt (Memphis)": "Egypt's Sixth Dynasty, ruling from Memphis, still presided over a comparatively stable Old Kingdom during this century, even as the increasing power of regional governors (nomarchs) was quietly setting up the political fragmentation that would follow within a few generations.",
}

DESCRIPTIONS["century_23_bce"] = {
    "Akkadian Empire (Nineveh)": "Nineveh, later famous as the capital of the Neo-Assyrian Empire over a thousand years afterward, was already an important northern city absorbed into Sargon's Akkadian state in this era. Its temple to the goddess Ishtar made it a significant religious center even under Akkadian rule.",
    "Old Kingdom Egypt (Memphis)": "Toward the end of this century, the long, stable reign of Pepi II -- traditionally said to have lasted over 90 years -- gave way to a weakening of central authority from Memphis, as regional governors grew increasingly independent and royal resources for monumental building declined.",
    "Elam (Susa)": "Centered on the city of Susa in what is now south-western Iran, the Elamite civilization was a persistent rival power to Mesopotamia, alternating between conflict and trade with Akkad throughout this period. Elam's distinct language and culture would endure for close to two thousand more years.",
}

DESCRIPTIONS["century_22_bce"] = {
    "Former Akkadian Empire (Akkad region)": "The Akkadian Empire collapsed in this century under a combination of invasions by the Gutians, a people from the Zagros Mountains, and a severe, multi-decade drought that shows up clearly in sediment and pollen records -- making it one of the earliest collapses in history with real archaeological climate evidence behind it.",
    "First Intermediate Period Egypt (Thebes)": "As royal authority centered on Memphis weakened, the southern city of Thebes rose as a rival power base, eventually producing the Theban dynasty that would reunify Egypt and launch the Middle Kingdom. This fractured era is known to Egyptologists as the First Intermediate Period.",
    "Gutian-controlled Mesopotamia (Nippur)": "Nippur, Mesopotamia's great religious capital and home to the temple of the chief god Enlil, continued to function as a center of worship and scribal learning even as Gutian rulers controlled much of the surrounding political landscape -- a reminder that religious institutions often outlasted the dynasties that patronized them.",
}

DESCRIPTIONS["century_21_bce"] = {
    "Third Dynasty of Ur (Ur)": "Under Ur-Nammu and his successors, Ur became capital of a new, highly centralized Sumerian empire often called the Ur III period. Ur-Nammu's law code, inscribed on clay tablets, predates Hammurabi's far more famous Babylonian code by roughly three centuries and is the oldest substantially preserved legal code known.",
    "Middle Kingdom Egypt (Thebes)": "From his base at Thebes, Mentuhotep II waged a decades-long campaign to reunify Egypt after the fragmentation of the First Intermediate Period, eventually succeeding and founding what Egyptologists call the Middle Kingdom -- generally remembered as a golden age of literature, art, and relative stability.",
    "Elam (Susa)": "Elam remained a formidable power on Mesopotamia's eastern frontier throughout the Ur III period, and it was ultimately Elamite forces that would deliver the fatal blow to Ur's empire within the next generation, sacking the city and carrying off its last king into captivity.",
}

DESCRIPTIONS["century_20_bce"] = {
    "Ur (falls c. 2004 BCE)": "Invading Elamite armies sacked Ur around 2004 BCE, capturing its last king, Ibbi-Sin, and ending the Third Dynasty of Ur. A Sumerian poem known as the Lament for Ur, written soon after, mourns the city's destruction in vivid, sorrowful verse -- one of the oldest surviving pieces of literature to grieve the fall of a civilization.",
    "Middle Kingdom Egypt (Thebes)": "Thebes served as the power base for Egypt's newly founded Twelfth Dynasty, widely regarded by Egyptologists as the high point of the Middle Kingdom, marked by major irrigation projects in the Faiyum region and an unusually rich body of surviving literature.",
    "Assyrian trade colony (Kanesh, Anatolia)": "At Kanesh in central Anatolia, Assyrian merchants ran one of the earliest well-documented long-distance trading networks, exchanging Mesopotamian textiles and tin for Anatolian silver and gold. Thousands of their business letters and contracts, written on clay tablets, survive -- giving historians an unusually detailed picture of Bronze Age commerce.",
}

DESCRIPTIONS["century_19_bce"] = {
    "Babylon (newly independent)": "Babylon emerged as an independent city-state under an Amorite dynasty during this century, still a relatively minor power compared to older centers like Ur or Isin. Nothing yet suggested it would soon become one of the most famous cities in the ancient world.",
    "Minoan Crete (Knossos)": "Knossos saw the construction of its first great palace complex around this time, marking the emergence of the sophisticated Bronze Age society modern scholars call Minoan civilization, after the legendary King Minos. Elaborate frescoes, advanced plumbing, and extensive trade networks across the Aegean all developed around this palace-centered society.",
    "Middle Kingdom Egypt (Thebes)": "Egypt continued to prosper under the Twelfth Dynasty, with Theban-based pharaohs overseeing extensive building projects, renewed trade with Nubia and the Levant, and a flourishing of the literary works -- including the Story of Sinuhe -- that would become classics of the Egyptian language for over a thousand years.",
}

DESCRIPTIONS["century_18_bce"] = {
    "Babylon (under Hammurabi)": "King Hammurabi transformed Babylon from a modest city-state into the dominant power in Mesopotamia, conquering rivals including Larsa, Mari, and Eshnunna. He is best remembered today for his law code, inscribed on a tall stone stele and organized around the principle of proportional justice -- 'an eye for an eye' being its most famous surviving clause.",
    "Middle Kingdom Egypt, declining (Thebes)": "The Middle Kingdom's stability eroded during this century as the Thirteenth Dynasty struggled with a rapid turnover of short-reigned kings and weakening central control, setting the stage for the political fragmentation of the Second Intermediate Period that followed.",
    "Nile Delta (early Hyksos settlement)": "Semitic-speaking migrants and traders from the Levant began settling in growing numbers in Egypt's eastern Nile Delta during this period, drawn by trade opportunities. Within a few generations their descendants, known to history as the Hyksos, would take political control of Lower Egypt entirely.",
}

DESCRIPTIONS["century_17_bce"] = {
    "Hyksos Egypt (Avaris)": "Avaris became the capital of Egypt's Fifteenth Dynasty, ruled by the Hyksos -- a dynasty of Levantine origin who controlled Lower Egypt during the Second Intermediate Period. Long cast as foreign invaders in later Egyptian propaganda, the Hyksos are now understood by most historians to have risen gradually from the earlier immigrant communities already settled in the Delta.",
    "Hittite Old Kingdom (Hattusa)": "Hattusa was founded as the capital of the emerging Hittite kingdom in central Anatolia, a state that would grow over the following centuries into one of the Near East's great empires, eventually rivaling Egypt itself for control of the Levant.",
    "Minoan Crete (Thera/Santorini)": "The volcanic island of Thera, a Minoan outpost known today as Santorini, was devastated by one of the largest volcanic eruptions in recorded history around this era. The eruption buried the town of Akrotiri in ash -- preserving it remarkably well -- while also likely weakening Minoan civilization across the wider Aegean.",
}

DESCRIPTIONS["century_16_bce"] = {
    "New Kingdom Egypt (Thebes)": "Pharaoh Ahmose I finally drove out the Hyksos rulers of Lower Egypt and reunified the country from his base at Thebes, founding the Eighteenth Dynasty and launching what Egyptologists call the New Kingdom -- the era of Egypt's greatest territorial power and wealth.",
    "Shang Dynasty China (Anyang)": "Anyang was the heartland of the Shang Dynasty, China's earliest dynasty confirmed by contemporary written records. Its royal diviners inscribed questions and answers on ox bones and turtle shells -- the oracle bones -- which preserve the oldest known form of Chinese writing.",
    "Babylon (falls to the Hittites)": "A surprise raid by the Hittite king Mursili I sacked Babylon around 1595 BCE, abruptly ending the Old Babylonian dynasty founded by Hammurabi roughly two centuries earlier. The Hittites did not stay to govern the city, and Babylon soon passed instead to the incoming Kassite dynasty.",
}

DESCRIPTIONS["century_15_bce"] = {
    "New Kingdom Egypt (Thebes)": "Hatshepsut, one of the small number of women to rule Egypt as pharaoh in her own right, presided over a prosperous and largely peaceful reign, commissioning an ambitious mortuary temple at Deir el-Bahari and sponsoring a famous trading expedition to the land of Punt.",
    "Mycenaean Greece (Mycenae)": "Mycenae rose to dominance on the Greek mainland in this era, its rulers building massive fortified palace-citadels with walls so thick that later Greeks believed only mythical Cyclopes could have built them. Mycenaean civilization would give its name to this entire phase of Bronze Age Greek history.",
    "Minoan Crete (Knossos, taken over)": "Mycenaean Greeks took control of Knossos around this period, adapting Minoan administrative practices -- including a new script, Linear B, used to write an early form of Greek -- while Minoan civilization itself gradually faded as an independent power.",
}

DESCRIPTIONS["century_14_bce"] = {
    "Amarna Period Egypt (Akhetaten)": "Pharaoh Akhenaten abandoned Egypt's traditional pantheon and capital to found Akhetaten, a new city built from scratch to honor the sun-disc god Aten as Egypt's sole deity. The experiment proved deeply unpopular and was abandoned within a generation of Akhenaten's death.",
    "New Kingdom Egypt (Thebes, restored)": "Under the young pharaoh Tutankhamun, Egypt's traditional religion and the old capital of Thebes were restored after the upheaval of the Amarna Period. Tutankhamun's own short reign would be largely forgotten by history until his nearly intact tomb was discovered in 1922.",
    "Hittite Empire (Hattusa)": "The Hittite Empire grew into Egypt's chief rival for control of the Levant during this century, its armies and diplomats contesting Syria's rich cities and trade routes in a rivalry that would culminate in one of the ancient world's largest chariot battles the following century.",
}

DESCRIPTIONS["century_13_bce"] = {
    "Battle of Kadesh site": "Fought around 1274 BCE between Pharaoh Ramesses II and Hittite king Muwatalli II, the Battle of Kadesh was one of the largest chariot battles in history, involving thousands of chariots on each side. Both empires claimed victory, but the inconclusive result eventually pushed them toward diplomacy instead.",
    "New Kingdom Egypt (Thebes)": "Ramesses II ruled for an extraordinary 66 years, presiding over Egypt's last great burst of imperial power and leaving behind more monuments -- including the temples at Abu Simbel -- than almost any other pharaoh in Egyptian history.",
    "Hittite Empire (Hattusa)": "After decades of costly rivalry, the Hittites and Egypt signed a formal peace treaty around 1259 BCE -- one of the oldest surviving international peace treaties, with copies preserved in both Egyptian hieroglyphs and Hittite cuneiform, including a provision for the mutual return of refugees.",
}

DESCRIPTIONS["century_12_bce"] = {
    "Hittite Empire (Hattusa, destroyed)": "The Hittite capital was destroyed and the empire collapsed entirely during this century, part of a wider, still-debated wave of societal breakdown across the eastern Mediterranean sometimes called the Bronze Age Collapse. Surviving Hittite successor states (the so-called Neo-Hittite kingdoms) persisted in smaller form in northern Syria.",
    "Mycenaean Greece (Mycenae, destroyed)": "Mycenaean palace centers across the Greek mainland -- including Mycenae, Pylos, and Tiryns -- were destroyed within a few decades of each other, plunging Greece into a centuries-long Dark Age during which writing itself was lost until the Greek alphabet emerged centuries later.",
    "Ugarit (destroyed)": "Ugarit, a wealthy Syrian port city and a major hub of Bronze Age Mediterranean trade, was destroyed and never resettled during this wave of collapse. Letters found in its ruins, written as the city fell, describe desperate pleas for help against seaborne raiders that never arrived in time.",
    "New Kingdom Egypt (weakened)": "Egypt successfully repelled a major invasion by a loose coalition of seafaring raiders known as the Sea Peoples under Ramesses III, but the effort permanently drained Egypt's resources and marked the beginning of the New Kingdom's long decline.",
}

DESCRIPTIONS["century_11_bce"] = {
    "Zhou Dynasty China (Fenghao, near modern Xi'an)": "After overthrowing the Shang Dynasty, the new Zhou rulers established their capital at Fenghao, near modern Xi'an, and introduced the political theory of the Mandate of Heaven -- the idea that a ruler's legitimacy depended on just governance, and could be withdrawn if a dynasty grew corrupt. This idea would shape Chinese political thought for the next three thousand years.",
    "Middle Assyrian Empire (Assur)": "Under King Tiglath-Pileser I, the Middle Assyrian state expanded its territory and military reach significantly from its capital at Assur, foreshadowing the far larger Neo-Assyrian Empire that would dominate the Near East several centuries later.",
    "Levant (Israelite kingdoms, traditional)": "Biblical tradition places the emergence of a united Israelite kingdom under Saul and later David around this era, though the archaeological evidence for its scale and unity is genuinely debated among historians -- a reminder that written religious tradition and the archaeological record don't always align neatly for this period.",
}

DESCRIPTIONS["century_10_bce"] = {
    "Phoenicia (Tyre)": "Tyre was the leading city of Phoenicia, a loose network of city-states whose sailors and merchants spread trading colonies across the Mediterranean -- eventually founding Carthage -- and whose simplified consonantal alphabet would become the direct ancestor of the Greek, Latin, and Hebrew alphabets still used today.",
    "Kingdom of Israel and Judah (Jerusalem)": "Biblical tradition credits King Solomon with building the First Temple in Jerusalem during this century, cementing the city's religious significance. As with earlier claims about a united Israelite kingdom, the exact historical scale of Solomon's realm remains a subject of ongoing scholarly debate.",
    "Neo-Assyrian Empire (Assur)": "This was a relatively quiet century for Assyria, based at its ancient capital Assur, before the dramatic military expansion of the following century would transform it into the dominant power of the ancient Near East.",
}

DESCRIPTIONS["century_9_bce"] = {
    "Neo-Assyrian Empire (Nimrud)": "King Ashurnasirpal II moved the Assyrian capital to Nimrud and began the rapid military expansion that launched the Neo-Assyrian Empire, known for both its administrative sophistication and its deliberately terrifying propaganda of conquest, recorded in detailed palace reliefs.",
    "Carthage (newly founded)": "According to tradition, Phoenician colonists from Tyre founded Carthage on the North African coast around 814 BCE, led by the legendary queen Dido. The new colony would grow over the following centuries into the dominant power of the western Mediterranean, eventually rivaling Rome itself.",
    "Kingdom of Kush (Napata)": "South of Egypt in Nubia, the kingdom of Kush rose as an independent power centered on Napata, having absorbed centuries of Egyptian cultural and religious influence even as it asserted its own political independence from its northern neighbor.",
}

DESCRIPTIONS["century_8_bce"] = {
    "Rome (traditional founding)": "Roman tradition dates the city's founding to 753 BCE, crediting the legendary twins Romulus and Remus, raised by a she-wolf, with establishing a small settlement on the Palatine Hill. Archaeology confirms genuine settlement on Rome's hills around this era, though the city that would one day rule an empire was still just one of many small Latin villages.",
    "Olympia, Greece": "The first Olympic Games, traditionally dated to 776 BCE, were held at the sanctuary of Olympia in honor of Zeus. The games became a unifying event across the otherwise fiercely independent Greek city-states, with wars even paused under a sacred truce so athletes and spectators could travel safely.",
    "Kushite Egypt (Napata)": "King Piye of Kush marched north and conquered Egypt, founding the Twenty-fifth Dynasty -- often called the 'Nubian' or 'Kushite' Dynasty -- and ruling a unified kingdom stretching from the heart of Nubia to the Mediterranean coast.",
}

DESCRIPTIONS["century_7_bce"] = {
    "Neo-Assyrian Empire (Nineveh)": "King Ashurbanipal assembled a vast library at Nineveh containing tens of thousands of cuneiform tablets -- including the most complete surviving version of the Epic of Gilgamesh -- making it the largest library of the ancient Near East. Within decades of his death, however, the empire collapsed with startling speed under combined Median and Babylonian attack.",
    "Neo-Babylonian Mesopotamia (Babylon)": "As Assyrian power crumbled, Babylon rose rapidly to fill the vacuum, soon becoming the dominant force in Mesopotamia under the Neo-Babylonian dynasty -- setting the stage for the city's later splendor under Nebuchadnezzar II.",
    "Kingdom of Media (Ecbatana)": "The Median kingdom, based at Ecbatana in what is now western Iran, allied with Babylon to help topple the Assyrian Empire, sacking Nineveh in 612 BCE. Media would itself be absorbed within the following century by its former ally Persia under Cyrus the Great.",
}

DESCRIPTIONS["century_6_bce"] = {
    "Neo-Babylonian Empire (Babylon)": "Babylon reached a spectacular final peak under Nebuchadnezzar II, who rebuilt the city with its famous Ishtar Gate and (according to later tradition) its Hanging Gardens. The empire fell abruptly to Cyrus the Great of Persia in 539 BCE, reportedly without a fight after Cyrus diverted the Euphrates to enter the city.",
    "Achaemenid Persian Empire (Pasargadae)": "Cyrus the Great built Pasargadae as the capital of his new Achaemenid Persian Empire, which at its height would stretch from the Aegean Sea to the Indus Valley -- the largest empire the world had yet seen. His tomb still stands at the site today.",
    "Roman Republic (Rome)": "Roman tradition holds that in 509 BCE the last Roman king, Tarquin the Proud, was overthrown and the monarchy replaced with a republic governed by annually elected magistrates and the Senate -- a system of government that would endure, with major adaptations, for roughly 500 years.",
}

DESCRIPTIONS["century_5_bce"] = {
    "Achaemenid Persia (Persepolis)": "Persepolis served as the ceremonial capital of the Achaemenid Persian Empire during its long and costly wars with the Greek city-states, its grand audience halls designed to receive tribute-bearing delegations from across the vast empire.",
    "Classical Athens": "Under the statesman Pericles, Athens reached its political and cultural golden age, funding the construction of the Parthenon atop the Acropolis and nurturing the playwrights, philosophers, and historians whose work still shapes Western thought -- all while governing itself through one of history's earliest experiments in direct democracy.",
    "Sparta": "Athens's great rival Sparta built its society almost entirely around military training and discipline, with citizen boys taken from their families at age seven for a harsh communal upbringing. The two cities' rivalry erupted into the decades-long Peloponnesian War, which ultimately exhausted both and reshaped the balance of power across Greece.",
}

DESCRIPTIONS["century_4_bce"] = {
    "Macedon (Pella)": "Pella was the capital of the kingdom of Macedon, a once-peripheral Greek-speaking state that King Philip II transformed into a dominant military power -- and the birthplace and childhood home of his son, Alexander the Great.",
    "Alexander's Empire (Persepolis, conquered)": "Alexander the Great's conquest of Persepolis in 330 BCE, including the ceremonial burning of its palace complex, symbolically marked the end of the two-century-old Achaemenid Persian Empire and the beginning of Alexander's own brief but vast empire stretching to India.",
    "Maurya Empire (Pataliputra)": "Chandragupta Maurya founded the Maurya Empire from his capital at Pataliputra, uniting most of the Indian subcontinent under a single government for the first time and establishing a sophisticated bureaucratic and espionage system described in detail in the contemporary treatise known as the Arthashastra.",
}

DESCRIPTIONS["century_3_bce"] = {
    "Ptolemaic Egypt (Alexandria)": "Alexandria became the capital of Ptolemaic Egypt, one of several Hellenistic kingdoms carved from Alexander the Great's empire after his death. Its famous Library and Lighthouse made it a leading center of Greek learning and science for centuries, blending Greek and Egyptian culture under a Macedonian ruling dynasty.",
    "Maurya Empire under Ashoka (Pataliputra)": "After a brutally violent conquest of the Kalinga region, Emperor Ashoka converted to Buddhism and renounced further military expansion, instead spreading Buddhist teachings across India through edicts carved on pillars and rocks -- among the earliest surviving monumental inscriptions in Indian history.",
    "Qin Dynasty China (Xianyang)": "Qin Shi Huang unified China's warring states for the first time under one centralized empire, ruling from his capital Xianyang. He standardized weights, currency, and writing across his realm, began work linking regional walls into what would become the Great Wall, and was buried with the now-famous Terracotta Army.",
    "Carthage": "Carthage fought Rome in the First Punic War over control of Sicily and the western Mediterranean during this century, the opening round of a rivalry that would eventually determine which power controlled the entire Mediterranean world.",
}

DESCRIPTIONS["century_2_bce"] = {
    "Roman Republic (Rome)": "Rome destroyed Carthage utterly at the end of the Third Punic War in 146 BCE -- the same year it also sacked Corinth and effectively absorbed Greece -- emerging as the unchallenged dominant power of the Mediterranean world.",
    "Han Dynasty China (Chang'an)": "Emperor Wu of Han dispatched the envoy Zhang Qian on a diplomatic mission westward into Central Asia; though his original mission largely failed, Zhang Qian's travels opened contact and trade routes that would later develop into the Silk Road.",
    "Seleucid Judea (Jerusalem)": "Jewish resistance to Seleucid rule and the forced imposition of Greek religious practices erupted into the Maccabean Revolt, ultimately winning Judea a period of independence and giving rise to the festival of Hanukkah, which commemorates the rededication of the Temple in Jerusalem.",
}

DESCRIPTIONS["century_1_bce"] = {
    "Roman Republic, then Empire (Rome)": "Julius Caesar's rise to power, crossing of the Rubicon, and subsequent assassination in 44 BCE plunged Rome into civil war; his adopted heir Octavian ultimately prevailed and, as Augustus, became Rome's first emperor, formally ending five centuries of republican government.",
    "Ptolemaic Egypt (Alexandria, falls to Rome)": "Cleopatra VII, the last Ptolemaic ruler of Egypt and a formidable political strategist in her own right, allied first with Julius Caesar and then with Mark Antony against Rome, but her defeat at the Battle of Actium in 31 BCE brought over three centuries of Ptolemaic rule to an end and made Egypt a Roman province.",
    "Gaul (conquered by Rome)": "Julius Caesar's multi-year campaign to conquer Gaul, documented in his own propagandistic Commentaries, brought vast new territory, wealth, and personal prestige to Caesar -- resources that would prove decisive in his subsequent bid for supreme power in Rome.",
}

DESCRIPTIONS["century_1_ce"] = {
    "Roman Judea (Jerusalem)": "Roman-controlled Judea was the setting for the ministry and crucifixion of Jesus of Nazareth around 30 CE, events central to the founding of Christianity. Jewish rebellion against Roman rule later in the century led to the destruction of the Second Temple in 70 CE, a catastrophic event that reshaped Jewish religious and communal life for the next two millennia.",
    "Roman Empire (Rome)": "Rome was ruled through this century first by the Julio-Claudian dynasty descended from Augustus, and then the Flavians, weathering the chaotic Year of the Four Emperors and the Great Fire of 64 CE, which Emperor Nero was controversially blamed for in later tradition.",
    "Roman Italy (Pompeii)": "The eruption of Mount Vesuvius in 79 CE buried the prosperous Roman town of Pompeii -- along with neighboring Herculaneum -- under volcanic ash and pumice, tragically killing many residents but also preserving an extraordinarily vivid snapshot of everyday Roman life that archaeologists are still studying today.",
}

DESCRIPTIONS["century_2_ce"] = {
    "Roman Empire, greatest extent (Rome)": "Under Emperor Trajan, the Roman Empire reached its largest territorial extent in 117 CE, stretching from Britain to Mesopotamia. His successor Hadrian would instead focus on consolidating and defending these vast borders rather than expanding them further.",
    "Roman Britain (Hadrian's Wall)": "Begun around 122 CE on the orders of Emperor Hadrian, this fortified wall marked the northernmost frontier of Roman Britain, stretching roughly 73 miles coast to coast and manned by a chain of forts and milecastles to control movement and trade across the border.",
    "Han Dynasty China (Luoyang)": "Luoyang served as the capital of the Eastern Han Dynasty, but by the century's end the dynasty was severely weakened by the Yellow Turban Rebellion, a massive peasant uprising fueled by famine, official corruption, and a new millenarian religious movement -- a crisis from which Han authority never fully recovered.",
}

DESCRIPTIONS["century_3_ce"] = {
    "Three Kingdoms China (Luoyang)": "Following the Han Dynasty's collapse, China fractured into the rival states of Wei, Shu, and Wu -- the Three Kingdoms period, later immortalized in the classic historical novel Romance of the Three Kingdoms. Luoyang, the former Han capital, became the seat of the Wei state amid this division.",
    "Sassanid Persian Empire (Ctesiphon)": "The Sassanid dynasty overthrew the Parthians and founded a new Persian empire centered on Ctesiphon, reviving Zoroastrianism as a state religion and establishing a rival power to Rome that would persist for over four centuries, until the Islamic conquests of the 7th century.",
    "Roman Empire in crisis (Rome)": "The Roman Empire nearly collapsed during the Crisis of the Third Century, cycling through dozens of short-lived emperors amid near-constant civil war, economic collapse, and invasions along almost every frontier -- a crisis the empire would only partially resolve through major administrative reforms late in the century.",
}

DESCRIPTIONS["century_4_ce"] = {
    "Roman/Byzantine Empire (Constantinople)": "Emperor Constantine founded a new imperial capital on the site of the old Greek city of Byzantium in 330 CE, naming it Constantinople. The city would remain the seat of the eastern, Greek-speaking half of the Roman Empire -- later known as the Byzantine Empire -- for over a thousand years after Rome itself fell.",
    "Gupta Empire (Pataliputra)": "Ruling from Pataliputra, the Gupta Empire presided over what many historians call India's classical golden age, marked by major advances in mathematics (including the concept of zero), astronomy, and Sanskrit literature and drama.",
    "Western Roman Empire (Rome)": "The Western Roman Empire faced mounting pressure from Gothic peoples who were themselves being displaced westward by the arrival of the Huns from Central Asia, setting in motion the chain of migrations and invasions that would ultimately bring down Roman rule in the west within the following century.",
}

DESCRIPTIONS["century_5_ce"] = {
    "Western Roman Empire (Rome, sacked)": "The Visigoths under Alaric sacked Rome in 410 CE -- the first time the city had fallen to a foreign enemy in roughly 800 years, a psychological shock across the ancient world -- and the Western Roman Empire itself formally ended in 476 CE when the Germanic general Odoacer deposed its last emperor.",
    "Hunnic Empire (territory of Attila)": "Attila the Hun led devastating campaigns across Europe from a power base near the Danube, extracting tribute from the Eastern Roman Empire and invading Gaul and Italy before his sudden death in 453 CE caused his short-lived empire to fragment almost immediately.",
    "Sub-Roman Britain": "As Roman military and administrative authority withdrew from Britain, Anglo-Saxon peoples from northern Europe began settling the island in growing numbers, gradually displacing or absorbing the existing Romano-British population and laying the linguistic and cultural foundations of later England.",
}

DESCRIPTIONS["century_6_ce"] = {
    "Byzantine Empire (Constantinople)": "Emperor Justinian I launched ambitious military campaigns to reconquer former Western Roman territory in Italy and North Africa, while also commissioning the Hagia Sophia -- an architectural masterpiece whose massive dome remained the largest in the world for nearly a thousand years -- and codifying Roman law into the Corpus Juris Civilis.",
    "Sui Dynasty China (Chang'an)": "The Sui Dynasty reunified China under one government after nearly four centuries of division following the Han collapse, undertaking massive infrastructure projects including the early Grand Canal, though the dynasty's harsh labor demands would lead to its own rapid collapse within a few decades.",
    "Byzantine Italy (Ravenna)": "Ravenna served as the Byzantine Empire's capital in Italy during Justinian's reconquest, and its churches from this era -- especially the Basilica of San Vitale -- preserve some of the finest surviving Byzantine mosaics, including famous portraits of Justinian and his wife Theodora.",
}

DESCRIPTIONS["century_7_ce"] = {
    "Islamic conquests (Mecca and Medina)": "The Prophet Muhammad received what Muslims believe were divine revelations in Mecca beginning around 610 CE, and his migration (the Hijra) to Medina in 622 CE marks the start of the Islamic calendar. Within a century of his death, Islamic armies would conquer territory stretching from Spain to the borders of India.",
    "Rashidun and Umayyad Caliphates (Damascus)": "Damascus became the new capital of the Umayyad Caliphate following the rapid wave of early Islamic conquests, administering an empire that by the century's end stretched from North Africa through the Middle East and into Central Asia.",
    "Tang Dynasty China (Chang'an)": "The newly founded Tang Dynasty made Chang'an its capital, and the city would grow into one of the largest and most cosmopolitan in the world during this era, drawing merchants, monks, and diplomats along the Silk Road from as far away as Persia and the Byzantine Empire.",
}

DESCRIPTIONS["century_8_ce"] = {
    "Umayyad al-Andalus (Córdoba)": "Following the Islamic conquest of most of the Iberian Peninsula in 711 CE, Córdoba became the capital of Umayyad al-Andalus, developing over the following centuries into one of the largest, wealthiest, and most learned cities in Europe.",
    "Abbasid Caliphate (Baghdad, founded 762 CE)": "The Abbasid dynasty overthrew the Umayyads and founded an entirely new capital at Baghdad, strategically positioned on the Tigris. The city rapidly became a thriving center of trade, science, and scholarship, launching what is often called the Islamic Golden Age.",
    "Carolingian Empire (Aachen)": "Charlemagne made Aachen his favored residence and administrative center, and on Christmas Day in 800 CE was crowned Holy Roman Emperor by Pope Leo III -- a symbolic revival of the Western Roman imperial title more than three centuries after its fall.",
}

DESCRIPTIONS["century_9_ce"] = {
    "Fragmented Carolingian Empire (Verdun)": "The 843 CE Treaty of Verdun divided Charlemagne's empire among his three grandsons into West Francia, Middle Francia, and East Francia -- a split whose rough outlines would echo, centuries later, in the eventual borders of France and Germany.",
    "Abbasid Caliphate (Baghdad)": "Baghdad's House of Wisdom became a major center for translating Greek, Persian, and Indian scientific and philosophical texts into Arabic, preserving and building on classical knowledge during a period when much of that learning was less actively studied in Western Europe.",
    "Rus' lands (Novgorod)": "According to the Primary Chronicle, the Varangian (Norse) chieftain Rurik established his rule at Novgorod in 862 CE, traditionally regarded as the founding moment of the Rus' state from which Russia, Ukraine, and Belarus all later trace their origins.",
}

DESCRIPTIONS["century_10_ce"] = {
    "Fatimid Caliphate (Cairo, founded 969 CE)": "The Shia Fatimid dynasty conquered Egypt and founded Cairo as their new capital in 969 CE, establishing a rival caliphate to the Sunni Abbasids in Baghdad and founding Al-Azhar, which would become one of the Islamic world's most important centers of learning.",
    "Song Dynasty China (Kaifeng)": "The newly founded Song Dynasty made Kaifeng its capital, presiding over an era of remarkable economic growth, urbanization, and technological innovation -- including early gunpowder weapons, paper money, and advances in printing that would later spread influence far beyond China's borders.",
    "Holy Roman Empire (Aachen)": "Otto I was crowned Holy Roman Emperor in 962 CE, reviving the imperial title in Germany and establishing a political structure -- loosely uniting German and Italian territories under an elected emperor -- that would persist, in changing form, for over 800 years.",
    "Norse Vinland (L'Anse aux Meadows)": "Norse explorer Leif Erikson reached the coast of North America around 1000 CE, establishing a short-lived settlement at what is now L'Anse aux Meadows in Newfoundland -- nearly 500 years before Columbus's voyages, though the Norse settlement did not endure.",
}

DESCRIPTIONS["century_11_ce"] = {
    "Byzantine Empire (Manzikert, battle site)": "The Byzantine army's catastrophic defeat by Seljuk Turks at the Battle of Manzikert in 1071 opened Anatolia to large-scale Turkic settlement, permanently weakening Byzantine control of the region and setting in motion a demographic and political shift that would eventually produce the later Ottoman heartland.",
    "Norman England (Hastings, battle site)": "William, Duke of Normandy, defeated King Harold II of England at the Battle of Hastings in 1066, beginning Norman rule of England and profoundly reshaping English language, law, and aristocracy with a lasting infusion of Norman French influence.",
    "Song Dynasty China (Kaifeng)": "The artisan Bi Sheng developed movable-type printing using fired clay characters around the 1040s, centuries before Johannes Gutenberg's independent invention of movable type in Europe, reflecting the Song Dynasty's broader era of technological innovation.",
}

DESCRIPTIONS["century_12_ce"] = {
    "Khmer Empire (Angkor)": "King Suryavarman II commissioned Angkor Wat as a monumental temple dedicated originally to the Hindu god Vishnu, making it the largest religious monument in the world and the architectural centerpiece of the Khmer Empire's capital at Angkor.",
    "Norman Sicily (Palermo)": "Under King Roger II, the Norman court at Palermo became a remarkably cosmopolitan center blending Norman, Byzantine, and Islamic influences; the Arab geographer al-Idrisi completed his Tabula Rogeriana there, one of the most advanced and accurate world maps of the medieval period.",
    "Ayyubid-ruled Jerusalem": "Salah ad-Din (Saladin) recaptured Jerusalem from the Crusader states in 1187, ending nearly 90 years of Crusader control and triggering the Third Crusade in response, though Saladin's famously lenient treatment of the city's Christian population contrasted sharply with the massacre that had accompanied its capture by the First Crusade in 1099.",
}

DESCRIPTIONS["century_13_ce"] = {
    "Mongol Empire (Karakorum)": "Genghis Khan united the Mongol tribes and founded an empire that his successors expanded from Korakorum into the largest contiguous land empire in world history, stretching from Korea to Eastern Europe and briefly connecting trade and communication across almost the entire Eurasian continent.",
    "England (Runnymede)": "At Runnymede in 1215, rebellious barons forced King John to seal Magna Carta, a document establishing that even the king was subject to the law -- a principle with limited immediate effect but enormous long-term influence on constitutional government in England and beyond.",
    "Yuan Dynasty China (Khanbaliq, modern Beijing)": "Kublai Khan completed the Mongol conquest of Song China and founded the Yuan Dynasty, establishing his capital at Khanbaliq -- the city that would grow into modern Beijing -- and becoming the first foreign dynasty to rule the whole of China.",
}

DESCRIPTIONS["century_14_ce"] = {
    "Mali Empire (Niani)": "Ruling from his capital at Niani, Mansa Musa led the Mali Empire to the height of its wealth and influence; his lavish 1324 pilgrimage to Mecca, during which he reportedly distributed so much gold that it temporarily disrupted regional currency values, made his empire's riches legendary across the medieval world.",
    "Plague-stricken Europe (Florence)": "The Black Death swept through Florence and across Europe in the mid-14th century, killing an estimated one-third to one-half of the continent's population. The Florentine writer Giovanni Boccaccio set his Decameron against the backdrop of the plague, as characters flee the dying city to tell stories in the countryside.",
    "Ming Dynasty China (Nanjing)": "Zhu Yuanzhang, a former peasant and Buddhist monk, led the rebellion that overthrew Mongol Yuan rule and founded the Ming Dynasty, establishing his first capital at Nanjing before his successors later moved the seat of government north to Beijing.",
}

DESCRIPTIONS["century_15_ce"] = {
    "Holy Roman Empire (Mainz)": "Johannes Gutenberg developed a practical movable-type printing press in Mainz around 1440, dramatically lowering the cost of producing books and setting the stage for an explosion in literacy, the spread of ideas, and eventually the Protestant Reformation itself.",
    "Ottoman Empire (Constantinople, conquered 1453)": "Sultan Mehmed II's forces breached Constantinople's legendary walls in 1453 using massive siege cannons, ending the Byzantine Empire after more than a thousand years and establishing the city (soon renamed Istanbul) as the new capital of the rapidly expanding Ottoman Empire.",
    "Spanish Empire (Granada, conquered 1492)": "The fall of Granada, the last Muslim-ruled emirate in Iberia, to the combined forces of Ferdinand and Isabella in January 1492 completed the centuries-long Reconquista -- in the very same year that the same monarchs funded Columbus's first voyage across the Atlantic.",
}

DESCRIPTIONS["century_16_ce"] = {
    "Aztec Empire (Tenochtitlan, conquered 1521)": "Hernán Cortés, aided by thousands of indigenous allies hostile to Aztec rule and by the devastating impact of introduced diseases like smallpox, conquered the Aztec capital Tenochtitlan in 1521, ending the Aztec Empire and beginning Spanish colonial rule over central Mexico.",
    "Inca Empire (Cusco, conquered 1533)": "Francisco Pizarro captured the Inca emperor Atahualpa and, after collecting an enormous ransom in gold and silver, had him executed anyway; Spanish forces went on to take the Inca capital Cusco in 1533, bringing down the largest empire in the pre-Columbian Americas.",
    "Mughal Empire (Agra)": "Babur, a descendant of both Genghis Khan and Timur, founded the Mughal Empire in 1526 after defeating the Sultan of Delhi, establishing a dynasty from his base near Agra that would go on to rule much of the Indian subcontinent and amass extraordinary wealth over the following two centuries.",
    "Holy Roman Empire (Wittenberg)": "In 1517, the monk Martin Luther published his Ninety-Five Theses criticizing Catholic Church practices, reportedly nailing them to the door of the Wittenberg church -- an act that ignited the Protestant Reformation and permanently fractured Western Christianity.",
}

DESCRIPTIONS["century_17_ce"] = {
    "Holy Roman Empire, war-torn (Münster)": "The Peace of Westphalia, negotiated in Münster and Osnabrück and signed in 1648, ended the devastatingly destructive Thirty Years' War, which had killed an estimated one-third of the population in parts of German-speaking Europe, and established principles of state sovereignty still influential in international relations today.",
    "Qing Dynasty China (Beijing)": "Manchu forces conquered Ming China and established the Qing Dynasty, making Beijing their capital in 1644. The Qing would go on to rule China for over 260 years, eventually presiding over one of the largest empires in Chinese history.",
    "Kingdom of England (Cambridge)": "Working largely in isolation at Cambridge during a period when the university was closed due to plague, Isaac Newton developed the core ideas of calculus, optics, and universal gravitation that he would later publish in his 1687 masterwork, the Principia Mathematica.",
}

DESCRIPTIONS["century_18_ce"] = {
    "Kingdom of Great Britain (birthplace of the Industrial Revolution)": "Beginning in the 1760s, Manchester and the surrounding region became the crucible of the Industrial Revolution, as new textile machinery, steam power, and factory organization transformed Britain from a largely agrarian society into the world's first industrial economy.",
    "United States (Philadelphia)": "Delegates from the thirteen American colonies gathered in Philadelphia and adopted the Declaration of Independence on July 4, 1776, formally announcing their break from British rule and articulating principles of natural rights and self-government that would influence revolutionary movements worldwide.",
    "Kingdom of France (Paris)": "The storming of the Bastille in Paris in July 1789 marked the dramatic start of the French Revolution, which would abolish the monarchy, execute King Louis XVI, and unleash a period of radical political upheaval that reshaped France and sent shockwaves across Europe.",
}

DESCRIPTIONS["century_19_ce"] = {
    "Napoleonic France (Paris)": "Napoleon Bonaparte crowned himself Emperor of the French in 1804, going on to dominate continental Europe militarily for over a decade through the Napoleonic Wars before his final defeat at Waterloo in 1815 and exile to the remote island of Saint Helena.",
    "United States (Washington D.C.)": "The American Civil War (1861-1865) pitted the Union against the secessionist Confederacy over slavery and states' rights; the Union's victory preserved the United States as one nation and led to the constitutional abolition of slavery, though the war's deep social and political fractures would echo for generations afterward.",
    "Empire of Japan (Tokyo)": "The Meiji Restoration of 1868 ended over two centuries of Tokugawa shogunate rule and began a rapid, deliberate program of modernization and industrialization, transforming Japan within a few decades from a largely isolated feudal society into a major industrial and military power.",
    "Partitioned Africa (Berlin, conference site)": "At the 1884-85 Berlin Conference, European powers formally negotiated and carved up claims to African territory among themselves, with African societies and leaders almost entirely excluded from the negotiations that would determine their continent's colonial borders for the following century.",
}

DESCRIPTIONS["century_20_ce"] = {
    "World War I & II Europe (Sarajevo)": "The 1914 assassination of Archduke Franz Ferdinand in Sarajevo triggered a cascade of alliance obligations that plunged Europe into the First World War; a generation later the continent was engulfed again in the even more devastating Second World War, beginning in 1939.",
    "Russian Revolution (Petrograd/Saint Petersburg)": "The 1917 Russian Revolution, beginning in Petrograd, first toppled the centuries-old Tsarist monarchy and then, in a second revolution later that year, brought Vladimir Lenin's Bolsheviks to power -- establishing the world's first communist state and reshaping twentieth-century global politics.",
    "United Nations founding (San Francisco)": "Delegates from fifty nations met in San Francisco in 1945, in the closing months of World War II, to draft and sign the United Nations Charter, establishing an international organization intended to prevent future global conflicts through diplomacy and collective security.",
    "Cold War's end (Berlin)": "The fall of the Berlin Wall in November 1989, as East German crowds poured through newly opened checkpoints, became the defining image of the Cold War's end, foreshadowing German reunification the following year and the Soviet Union's own collapse in 1991.",
}

DESCRIPTIONS["century_21_ce"] = {
    "United States (New York, September 11 attacks)": "The September 11, 2001 terrorist attacks on the World Trade Center and Pentagon killed nearly 3,000 people and fundamentally reshaped global security policy, leading to long wars in Afghanistan and Iraq and sweeping changes to surveillance, airport security, and international counterterrorism cooperation.",
    "Global financial system (New York, Wall Street)": "The 2008 financial crisis, centered on the collapse of major Wall Street institutions and the U.S. housing market, triggered the worst global economic downturn since the Great Depression, leading to massive government bailouts and lasting changes to international banking regulation.",
    "COVID-19 origin (Wuhan)": "A novel coronavirus was first identified in Wuhan, China in late 2019, and by early 2020 had spread into a global pandemic that killed millions of people worldwide, disrupted economies and education on an unprecedented scale, and accelerated the development of mRNA vaccine technology.",
    "Generative AI boom (San Francisco)": "San Francisco and the surrounding Bay Area became the epicenter of a rapid boom in generative artificial intelligence following the public launch of ChatGPT in late 2022, drawing enormous investment and sparking intense global debate over AI's economic, educational, and societal impact.",
}


def main() -> None:
    data = json.loads(HISTORICAL_MAPS_PATH.read_text(encoding="utf-8"))

    total_updated = 0
    missing_periods = []
    missing_regions = []
    for period in data["periods"]:
        period_descs = DESCRIPTIONS.get(period["id"])
        if period_descs is None:
            missing_periods.append(period["id"])
            continue
        for region in period["regions"]:
            desc = period_descs.get(region["name"])
            if desc is None:
                missing_regions.append(f"{period['id']}: {region['name']}")
                continue
            if "description" not in region or region["description"] is None:
                region["description"] = desc
                total_updated += 1

    if missing_periods:
        raise SystemExit(f"Missing DESCRIPTIONS entries for periods: {missing_periods}")
    if missing_regions:
        raise SystemExit(f"Missing DESCRIPTIONS entries for regions: {missing_regions}")

    HISTORICAL_MAPS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added description to {total_updated} region markers across {len(data['periods'])} periods.")


if __name__ == "__main__":
    main()
