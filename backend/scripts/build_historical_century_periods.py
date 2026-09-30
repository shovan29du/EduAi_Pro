#!/usr/bin/env python3
"""Rebuild historical_maps.json with per-century coverage from 3000 BCE to
2025 CE (51 individual century entries), preceded by a single "deep
prehistory" bucket for 5000-3001 BCE (that span isn't meaningfully divisible
into century-by-century content the way later, better-documented periods
are).

This REPLACES the previous 10-broad-era structure. Real content from those
eras is redistributed into the correct century buckets and supplemented with
additional real, well-documented civilizations/events per century. Famous
historical maps are only listed for a century when a specific, genuinely
well-known map is tied to roughly that century -- most centuries have none,
which is honest rather than a gap to be papered over.

Re-run after editing:
    python3 backend/scripts/build_historical_century_periods.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_PATH = BASE_DIR / "data" / "historical_maps" / "historical_maps.json"


def region(name, lat, lng, note):
    return {"name": name, "lat": lat, "lng": lng, "note": note}


def event(year, text):
    return {"year": year, "event": text}


def fmap(name, year, description, link):
    return {"name": name, "year": year, "description": description, "link": link}


def century_id(n, era):
    return f"century_{n}_{era}"


def bce_label(n):
    # century n BCE spans (n*100) down to (n-1)*100 + 1 BCE
    hi = n * 100
    lo = (n - 1) * 100 + 1
    ordinal = f"{n}{_suffix(n)}"
    return f"{ordinal} century BCE", f"{hi}–{lo} BCE"


def ce_label(n, end_year=None):
    lo = (n - 1) * 100 + 1
    hi = end_year or n * 100
    ordinal = f"{n}{_suffix(n)}"
    return f"{ordinal} century CE", f"{lo}–{hi} CE"


def _suffix(n):
    if 11 <= n % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def make_period(pid, label, years, emoji, description, regions, events, famous_maps=None):
    return {
        "id": pid,
        "label": label,
        "years": years,
        "emoji": emoji,
        "description": description,
        "regions": regions,
        "events": events,
        "famous_maps": famous_maps or [],
    }


PERIODS: list[dict] = []

# ─── Deep Prehistory: 5000-3001 BCE ────────────────────────────────────────
PERIODS.append(make_period(
    "deep_prehistory",
    "Deep Prehistory: Rise of the First Cities",
    "c. 5000–3001 BCE",
    "🏺",
    "Farming villages grow into the world's first true cities and complex societies along the Nile, Tigris-Euphrates, and Yellow River, while megalithic monument-builders are active in Atlantic Europe. Writing does not yet exist for most of this span -- the record comes from archaeology, not documents.",
    [
        region("Ubaid & Uruk period Mesopotamia (Uruk)", 31.3225, 45.6372, "Grew from a village into the world's first true city, with monumental temples by 3500 BCE."),
        region("Naqada culture Egypt (Naqada)", 26.0725, 32.7222, "Predynastic Upper Egyptian culture that laid the groundwork for the unification of Egypt."),
        region("Yangshao culture China (Banpo)", 34.2667, 108.9333, "Neolithic farming culture along the Yellow River, known for its distinctive painted pottery."),
        region("Vinca culture Europe (Vinca, near Belgrade)", 44.7583, 20.6142, "Advanced Copper Age culture in the Balkans with early proto-writing-like symbols on pottery."),
        region("Megalithic Atlantic Europe (Newgrange, Ireland)", 53.6947, -6.4753, "Passage tomb aligned to the winter solstice sunrise, older than Stonehenge or the Pyramids."),
    ],
    [
        event("c. 4500 BCE", "The Vinca culture in the Balkans develops symbol systems on pottery, among the earliest proto-writing-like marks in Europe."),
        event("c. 3500 BCE", "Sumerians in Uruk develop the first true writing system, proto-cuneiform, initially for accounting."),
        event("c. 3400 BCE", "Construction begins at Newgrange in Ireland, a passage tomb older than Stonehenge or the Great Pyramid."),
        event("c. 3200 BCE", "The Egyptian hieroglyphic writing system emerges alongside Sumerian cuneiform, one of the world's first two independent scripts."),
        event("c. 3100 BCE", "Egypt is unified under King Narmer, traditionally marking the start of Ancient Egyptian civilization."),
    ],
    [fmap(
        "Babylonian Map of the World",
        "c. 700–500 BCE (depicting older Mesopotamian cosmology)",
        "Though the surviving clay tablet is later, it encodes a much older Mesopotamian world-view rooted in this era's first cities.",
        "https://en.wikipedia.org/wiki/Babylonian_Map_of_the_World",
    )],
))

# ─── Stage A: 30th–21st century BCE (3000–2001 BCE), Early Bronze Age ──────

def add_bce(n, emoji, description, regions, events, famous_maps=None):
    label, years = bce_label(n)
    PERIODS.append(make_period(century_id(n, "bce"), label, years, emoji, description, regions, events, famous_maps))


add_bce(
    30, "🏛️",
    "Sumer's Early Dynastic city-states compete for dominance in Mesopotamia as Egypt's newly unified kingdom builds its first capital.",
    [
        region("Early Dynastic Sumer (Ur)", 30.9625, 46.1039, "One of the leading rival city-states of early Sumer, later famous for its royal tombs."),
        region("Early Dynastic Egypt (Memphis)", 29.85, 31.25, "Founded around this time as the capital of the newly unified kingdom of Egypt."),
        region("Early Harappan Indus Valley (Harappa)", 30.6301, 72.865, "Village settlements along the Indus begin growing into the towns that would become the Indus Valley Civilization."),
    ],
    [
        event("c. 2900 BCE", "The Early Dynastic Period begins in Sumer, with city-states such as Ur, Uruk, Kish, and Lagash competing for dominance."),
        event("c. 3000 BCE", "Memphis is founded as the capital of newly unified Egypt."),
        event("c. 2900 BCE", "Early Harappan culture begins developing across the Indus Valley."),
    ],
)

add_bce(
    29, "🗿",
    "Sumerian city-states continue their rivalry while, far to the northwest, Neolithic Britain begins one of prehistory's most famous monuments.",
    [
        region("Early Dynastic Sumer (Uruk)", 31.3225, 45.6372, "Still among the largest and most influential cities in the world."),
        region("Neolithic Britain (Stonehenge)", 51.1789, -1.8262, "The first phase -- a circular ditch and bank -- is built around this century."),
        region("Old Kingdom Egypt (Memphis)", 29.85, 31.25, "Egypt's Early Dynastic kings consolidate control of the Nile Valley."),
    ],
    [
        event("c. 2900 BCE", "The first phase of Stonehenge -- a circular ditch and bank earthwork -- is constructed in southern England."),
        event("c. 2890 BCE", "Egypt's Second Dynasty rules from Memphis, continuing to consolidate the unified kingdom."),
    ],
)

add_bce(
    28, "🧱",
    "Sumer's city-states build some of the world's first monumental temple towers (ziggurats), while Egypt approaches the age of pyramid-building.",
    [
        region("Early Dynastic Sumer (Kish)", 32.5442, 44.6475, "A powerful early city-state whose kings claimed a special legitimacy after the mythical Great Flood."),
        region("Old Kingdom Egypt (Memphis)", 29.85, 31.25, "Egypt's Second Dynasty gives way to the Third, setting the stage for the pyramid age."),
        region("Indus Valley (Mohenjo-daro, early phase)", 27.3294, 68.1358, "Early settlement precedes the city's later, famously planned urban layout."),
    ],
    [
        event("c. 2700 BCE", "Sumerian cities begin building the first ziggurats, stepped temple towers dedicated to their gods."),
        event("c. 2686 BCE", "Egypt's Third Dynasty begins, ushering in the Old Kingdom and the age of pyramid-building."),
    ],
)

add_bce(
    27, "🐫",
    "Egypt builds the world's first great stone monument at Saqqara, while a king later remembered as Gilgamesh is traditionally dated to Sumerian Uruk.",
    [
        region("Old Kingdom Egypt (Saqqara)", 29.8714, 31.2164, "Site of the Step Pyramid of Djoser, the world's oldest large-scale cut-stone building."),
        region("Early Dynastic Sumer (Uruk)", 31.3225, 45.6372, "Traditional home of the legendary king Gilgamesh."),
        region("Early Dynastic Sumer (Lagash)", 31.1833, 46.3167, "A powerful city-state that would soon clash with its neighbour Umma."),
    ],
    [
        event("c. 2670 BCE", "Egypt's Step Pyramid of Djoser is built at Saqqara, designed by the official Imhotep -- the world's oldest large-scale cut-stone building."),
        event("c. 2700 BCE", "Gilgamesh, later hero of the Epic of Gilgamesh, is traditionally dated as a historical king of Uruk around this era."),
    ],
)

add_bce(
    26, "🐫",
    "Egypt builds the Great Pyramid of Giza, its most famous monument, while the Indus Valley Civilization enters its mature urban phase.",
    [
        region("Old Kingdom Egypt (Giza)", 29.9792, 31.1342, "Site of the Great Pyramid, built for Pharaoh Khufu -- the last of the Seven Wonders of the Ancient World still standing."),
        region("Mature Harappan Indus Valley (Mohenjo-daro)", 27.3294, 68.1358, "Enters its famous mature phase, with grid-planned streets and advanced drainage systems."),
        region("Early Dynastic Sumer (Ur)", 30.9625, 46.1039, "Continues to flourish as one of Sumer's leading cities."),
    ],
    [
        event("c. 2560 BCE", "The Great Pyramid of Giza is completed for Pharaoh Khufu."),
        event("c. 2600 BCE", "The Indus Valley Civilization enters its mature urban phase at Mohenjo-daro and Harappa, with grid-planned streets and advanced drainage."),
    ],
)

add_bce(
    25, "⚔️",
    "Egypt's Old Kingdom continues building pyramids while Sumer's city-states fight one of history's earliest recorded wars.",
    [
        region("Old Kingdom Egypt (Abusir)", 29.8944, 31.2119, "Site of Fifth Dynasty sun temples and pyramids."),
        region("Early Dynastic Sumer (Lagash)", 31.1833, 46.3167, "Erects the Stele of the Vultures to commemorate victory over neighbouring Umma."),
        region("Early Dynastic Sumer (Umma)", 31.6167, 45.8667, "Lagash's rival in one of history's earliest recorded border wars."),
    ],
    [
        event("c. 2450 BCE", "The Stele of the Vultures commemorates a border war between the Sumerian city-states of Lagash and Umma -- the earliest known depiction of organized warfare in a historical narrative."),
        event("c. 2400 BCE", "Egypt's Fifth Dynasty pharaohs build sun temples at Abusir, reflecting the growing importance of the sun god Ra."),
    ],
)

add_bce(
    24, "👑",
    "Sargon of Akkad conquers Sumer's city-states and founds the world's first empire, unifying Mesopotamia under a single ruler for the first time.",
    [
        region("Akkadian Empire (Akkad, exact site unknown)", 32.6, 44.4, "Capital of the world's first empire, founded by Sargon -- its exact location has never been rediscovered."),
        region("Sumer (Uruk, now under Akkadian rule)", 31.3225, 45.6372, "Absorbed into the new Akkadian Empire along with the other Sumerian city-states."),
        region("Old Kingdom Egypt (Memphis)", 29.85, 31.25, "Egypt's Sixth Dynasty rules a still-stable Old Kingdom."),
    ],
    [
        event("c. 2334 BCE", "Sargon of Akkad conquers the Sumerian city-states and founds the Akkadian Empire, often called history's first empire."),
        event("c. 2300 BCE", "Sargon's empire stretches from the Persian Gulf to the Mediterranean, the largest political unit yet seen."),
    ],
)

add_bce(
    23, "📉",
    "The Akkadian Empire reaches its peak under Naram-Sin, while Egypt's Old Kingdom begins to weaken.",
    [
        region("Akkadian Empire (Nineveh)", 36.3612, 43.15, "An important northern city absorbed into the growing Akkadian Empire."),
        region("Old Kingdom Egypt (Memphis)", 29.85, 31.25, "The Old Kingdom's central authority begins to weaken toward the century's end."),
        region("Elam (Susa)", 32.1889, 48.2517, "A rival power in what is now south-western Iran, in on-and-off conflict with Akkad."),
    ],
    [
        event("c. 2250 BCE", "Naram-Sin expands the Akkadian Empire to its greatest extent and is the first Mesopotamian king to claim divine status."),
        event("c. 2181 BCE", "Egypt's Old Kingdom collapses at the end of the Sixth Dynasty, beginning the First Intermediate Period."),
    ],
)

add_bce(
    22, "🌾",
    "The Akkadian Empire collapses amid invasion and a severe, well-documented drought, while Egypt fragments into rival regional powers.",
    [
        region("Former Akkadian Empire (Akkad region)", 32.6, 44.4, "Falls to invasions by the Gutians and a severe, archaeologically documented drought."),
        region("First Intermediate Period Egypt (Thebes)", 25.6872, 32.6396, "Rises as a rival power centre as central authority in Memphis weakens."),
        region("Gutian-controlled Mesopotamia (Nippur)", 32.1181, 45.2394, "A major religious centre that endures through the turmoil of the era."),
    ],
    [
        event("c. 2154 BCE", "The Akkadian Empire collapses amid Gutian invasions and a severe, archaeologically documented regional drought."),
        event("c. 2160 BCE", "Egypt fragments into competing regional power centres during the First Intermediate Period."),
    ],
)

add_bce(
    21, "⚖️",
    "Ur-Nammu founds the Third Dynasty of Ur and issues history's oldest surviving law code, while Egypt is reunified under the Middle Kingdom.",
    [
        region("Third Dynasty of Ur (Ur)", 30.9625, 46.1039, "Capital of a new Sumerian empire and issuer of the oldest surviving written law code."),
        region("Middle Kingdom Egypt (Thebes)", 25.6872, 32.6396, "Base of Mentuhotep II, who reunifies Egypt and founds the Middle Kingdom."),
        region("Elam (Susa)", 32.1889, 48.2517, "Remains a significant regional power neighbouring Ur's new empire."),
    ],
    [
        event("c. 2112 BCE", "Ur-Nammu founds the Third Dynasty of Ur and issues the Code of Ur-Nammu, the oldest surviving written law code -- predating Hammurabi's by roughly three centuries."),
        event("c. 2055 BCE", "Mentuhotep II reunifies Egypt after the First Intermediate Period, founding the Middle Kingdom."),
    ],
)

# ─── Stage B: 20th–11th century BCE (2000–1001 BCE) ────────────────────────

add_bce(
    20, "🏺",
    "The Third Dynasty of Ur falls to Elamite invaders while Egypt's Middle Kingdom flourishes under a new dynasty and Assyrian merchants pioneer long-distance trade.",
    [
        region("Ur (falls c. 2004 BCE)", 30.9625, 46.1039, "Sacked by Elamite invaders, ending the Third Dynasty of Ur."),
        region("Middle Kingdom Egypt (Thebes)", 25.6872, 32.6396, "Base of the newly founded Twelfth Dynasty."),
        region("Assyrian trade colony (Kanesh, Anatolia)", 38.8, 35.75, "One of the earliest known long-distance trading colonies, run by Assyrian merchants."),
    ],
    [
        event("c. 2004 BCE", "Elamite invaders sack Ur, ending the Third Dynasty of Ur."),
        event("c. 1991 BCE", "Amenemhat I founds Egypt's Twelfth Dynasty, a high point of Middle Kingdom culture."),
        event("c. 1950 BCE", "Assyrian merchants establish long-distance trading colonies in Anatolia, such as Kanesh."),
    ],
)

add_bce(
    19, "🏰",
    "Babylon rises as an independent city-state under an Amorite dynasty, while Minoan Crete builds its first great palaces.",
    [
        region("Babylon (newly independent)", 32.5355, 44.4275, "Founded as an independent Amorite-ruled city-state, beginning its rise to prominence."),
        region("Minoan Crete (Knossos)", 35.298, 25.1633, "Builds its first great palace, launching the flourishing of Minoan civilization."),
        region("Middle Kingdom Egypt (Thebes)", 25.6872, 32.6396, "Continues to prosper under the Twelfth Dynasty."),
    ],
    [
        event("c. 1894 BCE", "Babylon is founded as an independent city-state under an Amorite dynasty."),
        event("c. 1900 BCE", "Minoan Crete's first palaces are built at Knossos and Phaistos, launching its Bronze Age civilization."),
    ],
)

add_bce(
    18, "📜",
    "Hammurabi unites Mesopotamia under Babylon and issues one of history's most famous law codes.",
    [
        region("Babylon (under Hammurabi)", 32.5355, 44.4275, "Becomes the dominant power in Mesopotamia under King Hammurabi."),
        region("Middle Kingdom Egypt, declining (Thebes)", 25.6872, 32.6396, "The Middle Kingdom weakens as the Thirteenth Dynasty struggles to hold power."),
        region("Nile Delta (early Hyksos settlement)", 30.8, 31.2, "Semitic-speaking settlers from the Levant begin establishing themselves, foreshadowing Hyksos rule."),
    ],
    [
        event("c. 1792 BCE", "Hammurabi becomes king of Babylon."),
        event("c. 1754 BCE", "Hammurabi issues his famous law code, one of the earliest and most complete legal codes to survive."),
    ],
)

add_bce(
    17, "🌋",
    "The Hyksos come to rule northern Egypt as the Hittite kingdom forms in Anatolia, while a massive volcanic eruption devastates the Minoan world.",
    [
        region("Hyksos Egypt (Avaris)", 30.7833, 31.8167, "Capital of the Hyksos Fifteenth Dynasty, which ruled northern Egypt during the Second Intermediate Period."),
        region("Hittite Old Kingdom (Hattusa)", 40.0181, 34.6167, "Newly founded capital of the rising Hittite kingdom in Anatolia."),
        region("Minoan Crete (Thera/Santorini)", 36.3932, 25.4615, "A catastrophic volcanic eruption devastates this Minoan outpost and weakens Crete's civilization."),
    ],
    [
        event("c. 1650 BCE", "The Hyksos establish the Fifteenth Dynasty, ruling northern Egypt during the Second Intermediate Period."),
        event("c. 1650 BCE", "Hattusili I founds the Hittite Old Kingdom in Anatolia."),
        event("c. 1600 BCE", "A massive volcanic eruption at Thera (Santorini) devastates the Minoan world (exact date debated among scholars)."),
    ],
)

add_bce(
    16, "🐉",
    "Egypt's New Kingdom begins after expelling the Hyksos, while China's Shang Dynasty -- the first with contemporary written records -- rises along the Yellow River.",
    [
        region("New Kingdom Egypt (Thebes)", 25.6872, 32.6396, "Ahmose I expels the Hyksos and founds Egypt's New Kingdom here."),
        region("Shang Dynasty China (Anyang)", 36.0997, 114.3931, "Traditional heartland of China's first dynasty with contemporary written records (oracle bones)."),
        region("Babylon (falls to the Hittites)", 32.5355, 44.4275, "Sacked by a Hittite raid around 1595 BCE, ending the Old Babylonian dynasty."),
    ],
    [
        event("c. 1600 BCE", "Traditional founding date of China's Shang Dynasty, the first Chinese dynasty documented by contemporary written records."),
        event("c. 1595 BCE", "A Hittite raid sacks Babylon, ending the Old Babylonian dynasty founded by Hammurabi."),
        event("c. 1550 BCE", "Ahmose I expels the Hyksos from Egypt and founds the New Kingdom."),
    ],
)

add_bce(
    15, "👸",
    "Egypt's New Kingdom empire reaches new heights under a powerful female pharaoh, while Mycenaean Greeks take control of Minoan Crete.",
    [
        region("New Kingdom Egypt (Thebes)", 25.6872, 32.6396, "Hatshepsut, one of history's few female pharaohs, rules a prosperous and expansive Egypt."),
        region("Mycenaean Greece (Mycenae)", 37.7307, 22.7563, "Rises to dominance on the Greek mainland, building fortified palace-citadels."),
        region("Minoan Crete (Knossos, taken over)", 35.298, 25.1633, "Comes under Mycenaean Greek control, absorbing Minoan civilization."),
    ],
    [
        event("c. 1479 BCE", "Hatshepsut becomes one of ancient Egypt's few female pharaohs, ruling a prosperous era of trade and monument-building."),
        event("c. 1450 BCE", "Mycenaean Greeks take control of Knossos, absorbing Minoan Crete into their sphere."),
    ],
)

add_bce(
    14, "☀️",
    "Pharaoh Akhenaten launches a radical religious revolution in Egypt, briefly replacing its many gods with worship of a single sun disc, before his famous successor restores tradition.",
    [
        region("Amarna Period Egypt (Akhetaten)", 27.6453, 30.902, "New capital built by Akhenaten for the worship of the sun-disc god Aten."),
        region("New Kingdom Egypt (Thebes, restored)", 25.6872, 32.6396, "Traditional religion and the old capital are restored under Tutankhamun."),
        region("Hittite Empire (Hattusa)", 40.0181, 34.6167, "Becomes a major rival power to Egypt in the Near East."),
    ],
    [
        event("c. 1353 BCE", "Pharaoh Akhenaten institutes worship of a single god, the sun disc Aten, and builds a new capital at Akhetaten."),
        event("c. 1332 BCE", "Tutankhamun becomes pharaoh and restores Egypt's traditional religion after Akhenaten's death."),
    ],
)

add_bce(
    13, "🕊️",
    "Egypt and the Hittite Empire fight one of the ancient world's best-documented battles, then sign history's oldest surviving peace treaty.",
    [
        region("Battle of Kadesh site", 34.5833, 36.5, "Site of a massive chariot battle between Egypt and the Hittite Empire."),
        region("New Kingdom Egypt (Thebes)", 25.6872, 32.6396, "Ramesses II rules during Egypt's last great imperial peak."),
        region("Hittite Empire (Hattusa)", 40.0181, 34.6167, "Signs a landmark peace treaty with Egypt after decades of rivalry."),
    ],
    [
        event("c. 1274 BCE", "The Battle of Kadesh is fought between Egypt and the Hittite Empire, one of the best-documented battles of the ancient world."),
        event("c. 1259 BCE", "Egypt and the Hittites sign the Treaty of Kadesh, the oldest known peace treaty to survive in full."),
        event("c. 1200 BCE", "The traditional (legendary) date for the Trojan War described in Homer's later epic poem the Iliad."),
    ],
)

add_bce(
    12, "💥",
    "The Bronze Age Collapse: within a few decades, the Hittite Empire falls, Mycenaean palaces are destroyed, and the eastern Mediterranean's international trade network disintegrates.",
    [
        region("Hittite Empire (Hattusa, destroyed)", 40.0181, 34.6167, "The Hittite capital is destroyed and the empire collapses entirely."),
        region("Mycenaean Greece (Mycenae, destroyed)", 37.7307, 22.7563, "Mycenaean palace centres across Greece are destroyed within a few decades."),
        region("Ugarit (destroyed)", 35.6019, 35.7797, "A major Syrian trading city, abandoned after destruction and never resettled."),
        region("New Kingdom Egypt (weakened)", 25.6872, 32.6396, "Repels an invasion of the mysterious \"Sea Peoples\" but is permanently weakened."),
    ],
    [
        event("c. 1200–1150 BCE", "The Bronze Age Collapse: the Hittite Empire falls, Mycenaean palace centres are destroyed, and Ugarit is abandoned, all within a few decades."),
        event("c. 1177 BCE", "Egypt repels an invasion by the mysterious \"Sea Peoples\" under Ramesses III, though the empire is permanently weakened."),
    ],
)

add_bce(
    11, "🏹",
    "China's Zhou Dynasty overthrows the Shang to begin the longest-reigning dynasty in Chinese history, while Assyria rebuilds its power in the wake of the Bronze Age Collapse.",
    [
        region("Zhou Dynasty China (Fenghao, near modern Xi'an)", 34.3416, 108.9398, "New capital of the Zhou Dynasty after overthrowing the Shang."),
        region("Middle Assyrian Empire (Assur)", 35.4553, 43.2601, "Expands its territory and influence under Tiglath-Pileser I."),
        region("Levant (Israelite kingdoms, traditional)", 31.7683, 35.2137, "According to biblical tradition, a united Israelite kingdom emerges around this era -- a period much debated among historians and archaeologists."),
    ],
    [
        event("c. 1100 BCE", "Assyrian king Tiglath-Pileser I expands the Middle Assyrian Empire's territory and influence."),
        event("c. 1046 BCE", "China's Zhou Dynasty overthrows the Shang at the Battle of Muye, beginning the longest-reigning dynasty in Chinese history."),
    ],
)

# ─── Stage C: 10th–1st century BCE (1000–1 BCE) ────────────────────────────

add_bce(
    10, "⛵",
    "Phoenician city-states spread trade colonies and their alphabet across the Mediterranean, the ancestor of the Greek and Latin alphabets.",
    [
        region("Phoenicia (Tyre)", 33.2704, 35.2038, "Leading Phoenician city-state, spreading trade colonies and the alphabet across the Mediterranean."),
        region("Kingdom of Israel and Judah (Jerusalem)", 31.7683, 35.2137, "According to biblical tradition, King Solomon builds the First Temple here."),
        region("Neo-Assyrian Empire (Assur)", 35.4553, 43.2601, "A relatively quiet century for Assyria before its coming imperial expansion."),
    ],
    [
        event("c. 1000–900 BCE", "Phoenician city-states such as Tyre, Sidon, and Byblos spread trade colonies and their alphabet across the Mediterranean -- the ancestor of the Greek and Latin alphabets."),
        event("c. 957 BCE", "According to biblical tradition, King Solomon builds the First Temple in Jerusalem."),
    ],
)

add_bce(
    9, "🐘",
    "The Neo-Assyrian Empire begins its rapid expansion, Phoenicians found Carthage in North Africa, and the independent Kingdom of Kush rises in Nubia.",
    [
        region("Neo-Assyrian Empire (Nimrud)", 36.0975, 43.325, "New capital as Ashurnasirpal II begins the Neo-Assyrian Empire's rapid expansion."),
        region("Carthage (newly founded)", 36.8065, 10.323, "Founded by Phoenician colonists from Tyre; would grow into a great Mediterranean power."),
        region("Kingdom of Kush (Napata)", 18.5364, 31.8228, "Rises as an independent Nubian kingdom south of Egypt."),
    ],
    [
        event("c. 883 BCE", "Ashurnasirpal II begins the Neo-Assyrian Empire's rapid expansion, moving the capital to Nimrud."),
        event("c. 814 BCE", "Phoenician colonists from Tyre found Carthage in North Africa."),
    ],
)

add_bce(
    8, "🏛️",
    "Rome and the Olympic Games are traditionally founded, Greek city-states begin colonizing the Mediterranean, and a Nubian dynasty conquers and rules Egypt.",
    [
        region("Rome (traditional founding)", 41.9028, 12.4964, "Traditionally founded in 753 BCE, beginning what would become Rome's long history."),
        region("Olympia, Greece", 37.6381, 21.6306, "Site of the first Olympic Games, traditionally dated to 776 BCE."),
        region("Kushite Egypt (Napata)", 18.5364, 31.8228, "King Piye conquers Egypt, founding its Twenty-fifth (\"Nubian\") Dynasty."),
    ],
    [
        event("c. 776 BCE", "Traditional date of the first Olympic Games in Greece."),
        event("c. 753 BCE", "Traditional founding date of Rome."),
        event("c. 730s BCE", "Kushite king Piye conquers Egypt, founding Egypt's Twenty-fifth (\"Nubian\") Dynasty."),
        event("722 BCE", "The Neo-Assyrian Empire conquers the Kingdom of Israel."),
    ],
)

add_bce(
    7, "📚",
    "The Neo-Assyrian Empire reaches its height, building the ancient world's largest library, before collapsing with startling speed at the century's end.",
    [
        region("Neo-Assyrian Empire (Nineveh)", 36.3612, 43.15, "Ashurbanipal builds a great library here, the largest in the ancient Near East, before the empire's sudden collapse."),
        region("Neo-Babylonian Mesopotamia (Babylon)", 32.5355, 44.4275, "Rises as Assyria's power fades, soon to become the region's dominant power."),
        region("Kingdom of Media (Ecbatana)", 34.7983, 48.5148, "Allies with Babylon to help bring down the Assyrian Empire."),
    ],
    [
        event("c. 668 BCE", "Ashurbanipal becomes king of Assyria and builds a great library at Nineveh, the largest in the ancient Near East."),
        event("612 BCE", "Nineveh falls to a coalition of Babylonians and Medes, effectively ending the Assyrian Empire."),
    ],
)

add_bce(
    6, "👑",
    "Babylon reaches a final peak under Nebuchadnezzar II before Cyrus the Great conquers it and founds the vast Achaemenid Persian Empire; Rome overthrows its monarchy and Confucius is born in China.",
    [
        region("Neo-Babylonian Empire (Babylon)", 32.5355, 44.4275, "Reaches a final peak under Nebuchadnezzar II before falling to Cyrus the Great."),
        region("Achaemenid Persian Empire (Pasargadae)", 30.1928, 53.1746, "Capital built by Cyrus the Great, founder of the vast Achaemenid Persian Empire."),
        region("Roman Republic (Rome)", 41.9028, 12.4964, "Overthrows its monarchy and founds the Roman Republic."),
    ],
    [
        event("586 BCE", "Nebuchadnezzar II destroys Jerusalem and the First Temple, beginning the Babylonian exile."),
        event("c. 551 BCE", "Confucius is born in China; his teachings would shape Chinese thought for millennia."),
        event("c. 550 BCE", "Cyrus the Great founds the Achaemenid Persian Empire."),
        event("539 BCE", "Cyrus the Great conquers Babylon."),
        event("509 BCE", "Rome overthrows its monarchy and founds the Roman Republic."),
    ],
)

add_bce(
    5, "⚔️",
    "Greek city-states repel the Persian Empire, Athens enters its golden age under Pericles, and Athens and Sparta then exhaust each other in a long, ruinous war.",
    [
        region("Achaemenid Persia (Persepolis)", 29.9353, 52.8916, "Ceremonial capital of the Persian Empire during its wars with Greece."),
        region("Classical Athens", 37.9838, 23.7275, "Reaches its golden age under Pericles, building the Parthenon."),
        region("Sparta", 37.0739, 22.4304, "Athens's great rival in the long, devastating Peloponnesian War."),
    ],
    [
        event("490–479 BCE", "The Greco-Persian Wars, including the battles of Marathon, Thermopylae, and Salamis."),
        event("c. 447 BCE", "Construction begins on the Parthenon in Athens."),
        event("431–404 BCE", "The Peloponnesian War between Athens and Sparta ends in Spartan victory but leaves both exhausted."),
    ],
)

add_bce(
    4, "🐎",
    "Alexander the Great conquers the Persian Empire and builds one of history's largest empires, while the Maurya Empire rises in India.",
    [
        region("Macedon (Pella)", 40.7623, 22.525, "Capital of Macedon, homeland of Alexander the Great."),
        region("Alexander's Empire (Persepolis, conquered)", 29.9353, 52.8916, "Falls to Alexander the Great, symbolizing the end of the Achaemenid Persian Empire."),
        region("Maurya Empire (Pataliputra)", 25.6127, 85.1228, "Capital of the newly founded Maurya Empire under Chandragupta Maurya."),
    ],
    [
        event("336–323 BCE", "Alexander the Great conquers the Persian Empire, creating one of history's largest empires before his early death."),
        event("c. 322 BCE", "Chandragupta Maurya founds the Maurya Empire in India."),
    ],
)

add_bce(
    3, "🏯",
    "Alexander's empire splits into rival Hellenistic kingdoms, Ashoka spreads Buddhism across India, Qin Shi Huang unifies China as its first emperor, and Rome and Carthage fight for control of the western Mediterranean.",
    [
        region("Ptolemaic Egypt (Alexandria)", 31.2001, 29.9187, "One of the great Hellenistic kingdoms formed after Alexander's empire split among his generals."),
        region("Maurya Empire under Ashoka (Pataliputra)", 25.6127, 85.1228, "Ashoka converts to Buddhism and spreads it across India after a bloody conquest."),
        region("Qin Dynasty China (Xianyang)", 34.3297, 108.7092, "Capital of Qin Shi Huang, who unifies China and becomes its first emperor."),
        region("Carthage", 36.8065, 10.323, "Rome's great rival in the Punic Wars for control of the western Mediterranean."),
    ],
    [
        event("c. 268 BCE", "Ashoka becomes emperor of the Maurya Empire and later converts to Buddhism, spreading it across India."),
        event("264–241 BCE", "Rome and Carthage fight the First Punic War."),
        event("221 BCE", "Qin Shi Huang unifies China and becomes its first emperor, standardizing writing, currency, and measurements."),
        event("218–201 BCE", "Hannibal leads Carthage in the Second Punic War against Rome, famously crossing the Alps with war elephants."),
    ],
)

add_bce(
    2, "🐫",
    "Rome destroys Carthage and conquers Greece in the same year, while Han Dynasty China opens contact with Central Asia, laying the groundwork for the Silk Road.",
    [
        region("Roman Republic (Rome)", 41.9028, 12.4964, "Destroys Carthage and conquers Greece, becoming the dominant Mediterranean power."),
        region("Han Dynasty China (Chang'an)", 34.3416, 108.9398, "Emperor Wu of Han sends envoy Zhang Qian west, opening contact with Central Asia."),
        region("Seleucid Judea (Jerusalem)", 31.7683, 35.2137, "Site of the Maccabean Revolt against Seleucid rule."),
    ],
    [
        event("c. 167 BCE", "The Maccabean Revolt begins in Judea against Seleucid rule."),
        event("c. 138 BCE", "Han Dynasty envoy Zhang Qian opens contact with Central Asia, laying the groundwork for the Silk Road."),
        event("146 BCE", "Rome destroys Carthage in the Third Punic War and conquers Greece in the same year."),
    ],
)

add_bce(
    1, "👑",
    "Julius Caesar conquers Gaul and is assassinated, Cleopatra's Egypt falls to Rome, and Augustus becomes Rome's first emperor, ending the Republic and beginning the Roman Empire.",
    [
        region("Roman Republic, then Empire (Rome)", 41.9028, 12.4964, "Julius Caesar's rise and assassination give way to Augustus becoming Rome's first emperor."),
        region("Ptolemaic Egypt (Alexandria, falls to Rome)", 31.2001, 29.9187, "Cleopatra VII's Egypt, the last major Hellenistic kingdom, becomes a Roman province."),
        region("Gaul (conquered by Rome)", 46.2276, 2.2137, "Conquered by Julius Caesar in a campaign that made his political career."),
    ],
    [
        event("58–50 BCE", "Julius Caesar conquers Gaul."),
        event("44 BCE", "Julius Caesar is assassinated in the Roman Senate."),
        event("31 BCE", "Octavian defeats Mark Antony and Cleopatra at the Battle of Actium."),
        event("27 BCE", "Octavian becomes Augustus, Rome's first emperor, beginning the Roman Empire."),
    ],
)

# ─── Stage D: 1st–10th century CE (1–1000 CE) ──────────────────────────────

def add_ce(n, emoji, description, regions, events, famous_maps=None):
    label, years = ce_label(n)
    PERIODS.append(make_period(century_id(n, "ce"), label, years, emoji, description, regions, events, famous_maps))


add_ce(
    1, "✝️",
    "Jesus of Nazareth's ministry begins the spread of Christianity, Rome burns and rebuilds under Nero, and Roman forces destroy the Second Temple in Jerusalem.",
    [
        region("Roman Judea (Jerusalem)", 31.7683, 35.2137, "Jesus of Nazareth is crucified here around 30 CE; the Second Temple is destroyed by Roman forces in 70 CE."),
        region("Roman Empire (Rome)", 41.9028, 12.4964, "Rules under the Julio-Claudian and Flavian emperors, including the Great Fire of 64 CE."),
        region("Roman Italy (Pompeii)", 40.7509, 14.4849, "Buried by the eruption of Mount Vesuvius in 79 CE, preserving a snapshot of Roman daily life."),
    ],
    [
        event("c. 30 CE", "Jesus of Nazareth is crucified in Roman Judea, and Christianity begins to spread."),
        event("64 CE", "The Great Fire of Rome devastates the city during Nero's reign."),
        event("70 CE", "Roman forces destroy the Second Temple in Jerusalem."),
        event("79 CE", "Mount Vesuvius erupts, burying Pompeii and Herculaneum."),
    ],
)

add_ce(
    2, "🗺️",
    "The Roman Empire reaches its greatest territorial extent, Ptolemy writes the most influential geography text of antiquity, and Han China begins to decline.",
    [
        region("Roman Empire, greatest extent (Rome)", 41.9028, 12.4964, "Reaches its largest territorial size under Emperor Trajan in 117 CE."),
        region("Roman Britain (Hadrian's Wall)", 55.0, -2.3, "Marks the northern frontier of Roman Britain, built starting around 122 CE."),
        region("Han Dynasty China (Luoyang)", 34.6197, 112.454, "Eastern Han capital, weakened by the Yellow Turban Rebellion late in the century."),
    ],
    [
        event("117 CE", "The Roman Empire reaches its greatest territorial extent under Emperor Trajan."),
        event("c. 122 CE", "Construction begins on Hadrian's Wall in Britain."),
        event("c. 150 CE", "Claudius Ptolemy writes his Geographia, the most influential geography text of antiquity."),
        event("184 CE", "The Yellow Turban Rebellion breaks out in Han China, hastening the dynasty's decline."),
    ],
    [fmap(
        "Ptolemy's Geographia",
        "c. 150 CE",
        "Ptolemy's coordinate-grid treatise on world geography, the most influential of the ancient world.",
        "https://en.wikipedia.org/wiki/Geography_(Ptolemy)",
    )],
)

add_ce(
    3, "💥",
    "Han China collapses into the Three Kingdoms, a new Persian empire rises, and Rome nearly falls apart in decades of civil war before Diocletian stabilizes it.",
    [
        region("Three Kingdoms China (Luoyang)", 34.6197, 112.454, "Former Han capital, now contested amid China's division into three rival kingdoms."),
        region("Sassanid Persian Empire (Ctesiphon)", 33.0959, 44.5804, "Capital of the newly founded Sassanid Empire, which replaces the Parthians."),
        region("Roman Empire in crisis (Rome)", 41.9028, 12.4964, "Nearly collapses under constant civil war and invasion during the Crisis of the Third Century."),
    ],
    [
        event("220 CE", "The Han Dynasty falls, and China enters the Three Kingdoms period."),
        event("224 CE", "Ardashir I founds the Sassanid Persian Empire."),
        event("235–284 CE", "The Crisis of the Third Century: Rome nearly collapses under constant civil war and invasion."),
        event("284 CE", "Diocletian becomes emperor, stabilizes the Roman Empire, and later divides it into a Tetrarchy."),
    ],
)

add_ce(
    4, "⛪",
    "Constantine legalizes Christianity and founds Constantinople, the Roman Empire formally splits in two, and the Gupta Empire ushers in a golden age in India.",
    [
        region("Roman/Byzantine Empire (Constantinople)", 41.0082, 28.9784, "Founded by Constantine as the new imperial capital in 330 CE."),
        region("Gupta Empire (Pataliputra)", 25.6127, 85.1228, "Capital of the Gupta Empire, beginning a golden age of Indian science, mathematics, and culture."),
        region("Western Roman Empire (Rome)", 41.9028, 12.4964, "Weakens under mounting pressure from Goths and other peoples pushed west by the Huns."),
    ],
    [
        event("313 CE", "Constantine legalizes Christianity with the Edict of Milan."),
        event("325 CE", "The Council of Nicaea establishes core Christian doctrine."),
        event("330 CE", "Constantine founds Constantinople as the new imperial capital."),
        event("c. 320 CE", "The Gupta Empire is founded in India, beginning a golden age of science and culture."),
        event("378 CE", "The Goths defeat Rome at the Battle of Adrianople, a major blow to imperial power."),
        event("395 CE", "The Roman Empire formally splits into Eastern and Western halves."),
    ],
)

add_ce(
    5, "🛡️",
    "The Western Roman Empire falls after being sacked twice and invaded by Attila the Hun, while Anglo-Saxon peoples begin settling Britain.",
    [
        region("Western Roman Empire (Rome, sacked)", 41.9028, 12.4964, "Sacked by the Visigoths in 410 CE, then falls entirely in 476 CE."),
        region("Hunnic Empire (territory of Attila)", 47.4979, 19.0402, "Attila the Hun leads devastating invasions across Europe from a base near the Danube."),
        region("Sub-Roman Britain", 51.5074, -0.1278, "Anglo-Saxon peoples begin settling Britain as Roman authority collapses."),
    ],
    [
        event("410 CE", "Visigoths under Alaric sack Rome."),
        event("c. 434–453 CE", "Attila the Hun leads devastating invasions across Europe."),
        event("476 CE", "The last Western Roman Emperor is deposed, traditionally marking the fall of the Western Roman Empire."),
        event("c. 450s CE", "Anglo-Saxon peoples begin settling Britain."),
    ],
)

add_ce(
    6, "🦠",
    "Byzantine Emperor Justinian reconquers former Roman territory and codifies Roman law, but a devastating pandemic strikes his empire as Sui China reunifies after centuries of division.",
    [
        region("Byzantine Empire (Constantinople)", 41.0082, 28.9784, "Justinian I reconquers former Western Roman territory and builds the Hagia Sophia."),
        region("Sui Dynasty China (Chang'an)", 34.3416, 108.9398, "Reunifies China after nearly four centuries of division."),
        region("Byzantine Italy (Ravenna)", 44.4184, 12.2035, "Byzantine capital in Italy, site of famous mosaics from Justinian's reign."),
    ],
    [
        event("527 CE", "Justinian I becomes Byzantine Emperor and begins reconquering former Roman territories."),
        event("529–534 CE", "Justinian's Code, a landmark compilation of Roman law, is issued."),
        event("537 CE", "The Hagia Sophia is completed in Constantinople."),
        event("541–542 CE", "The Plague of Justinian, one of history's first recorded pandemics, devastates the Byzantine world."),
        event("581 CE", "The Sui Dynasty reunifies China after centuries of division."),
    ],
)

add_ce(
    7, "☪️",
    "Muhammad's revelations found Islam, which spreads with startling speed across the Middle East and North Africa within decades, while the Tang Dynasty begins one of China's greatest eras.",
    [
        region("Islamic conquests (Mecca and Medina)", 21.4225, 39.8262, "Birthplace of Islam under Muhammad, whose migration to Medina in 622 CE begins the Islamic calendar."),
        region("Rashidun and Umayyad Caliphates (Damascus)", 33.5138, 36.2765, "New capital of the Umayyad Caliphate after the rapid Islamic conquests."),
        region("Tang Dynasty China (Chang'an)", 34.3416, 108.9398, "Capital of the newly founded Tang Dynasty, soon to become one of the largest cities in the world."),
    ],
    [
        event("610 CE", "Muhammad receives his first revelations, beginning Islam."),
        event("618 CE", "The Tang Dynasty is founded in China."),
        event("622 CE", "The Hijra: Muhammad migrates from Mecca to Medina, marking year 1 of the Islamic calendar."),
        event("632–661 CE", "The Rashidun Caliphate rapidly conquers Persia, the Levant, and Egypt after Muhammad's death."),
        event("661 CE", "The Umayyad Caliphate is founded, moving the Islamic capital to Damascus."),
    ],
)

add_ce(
    8, "🕌",
    "The Umayyad Caliphate reaches its greatest extent before an Abbasid revolution moves the Islamic capital to newly founded Baghdad, launching a golden age of science, while Charlemagne is crowned emperor in the west.",
    [
        region("Umayyad al-Andalus (Córdoba)", 37.8882, -4.7794, "Capital of Umayyad Iberia after the conquest of most of the peninsula in 711 CE."),
        region("Abbasid Caliphate (Baghdad, founded 762 CE)", 33.3152, 44.3661, "New capital founded by the Abbasids, becoming a centre of the Islamic Golden Age."),
        region("Carolingian Empire (Aachen)", 50.7753, 6.0839, "Charlemagne's capital, crowned Holy Roman Emperor by the Pope in 800 CE."),
    ],
    [
        event("711 CE", "Umayyad forces conquer most of the Iberian Peninsula."),
        event("732 CE", "The Franks halt Umayyad expansion into Western Europe at the Battle of Tours."),
        event("750 CE", "The Abbasid Revolution overthrows the Umayyad Caliphate."),
        event("762 CE", "The Abbasids found Baghdad as their new capital, launching the Islamic Golden Age."),
        event("793 CE", "A Viking raid on Lindisfarne marks the traditional start of the Viking Age."),
        event("800 CE", "Charlemagne is crowned Holy Roman Emperor by the Pope."),
    ],
)

add_ce(
    9, "⚔️",
    "Charlemagne's empire fragments into what would roughly become France and Germany, Vikings raid and settle across Europe, and Baghdad's House of Wisdom drives the Islamic Golden Age.",
    [
        region("Fragmented Carolingian Empire (Verdun)", 49.1593, 5.3814, "Site of the 843 CE treaty splitting Charlemagne's empire into three kingdoms."),
        region("Abbasid Caliphate (Baghdad)", 33.3152, 44.3661, "Home to the House of Wisdom, a major centre of translation and scholarship."),
        region("Rus' lands (Novgorod)", 58.5215, 31.2755, "Site of Rurik's founding of Rus' rule, a traditional starting point for the Russian state."),
    ],
    [
        event("843 CE", "The Treaty of Verdun splits the Carolingian Empire into three kingdoms, roughly foreshadowing modern France, Germany, and the lands between."),
        event("c. 830 CE", "The House of Wisdom is founded in Baghdad, a major centre of translation and scholarship during the Islamic Golden Age."),
        event("c. 862 CE", "Rurik establishes Rus' rule at Novgorod, a traditional starting point for the Russian state."),
    ],
)

add_ce(
    10, "🛶",
    "The Song Dynasty ushers in a golden age of Chinese technology and trade, the Holy Roman Empire is founded in Europe, and Vikings reach North America centuries before Columbus.",
    [
        region("Fatimid Caliphate (Cairo, founded 969 CE)", 30.0444, 31.2357, "Founded by the Fatimids as their new capital after conquering Egypt."),
        region("Song Dynasty China (Kaifeng)", 34.7986, 114.3416, "Capital of the newly founded Song Dynasty, ushering in an era of economic and technological flourishing."),
        region("Holy Roman Empire (Aachen)", 50.7753, 6.0839, "Otto I is crowned Holy Roman Emperor in 962 CE."),
        region("Norse Vinland (L'Anse aux Meadows)", 51.5988, -55.5305, "Leif Erikson reaches North America around 1000 CE, centuries before Columbus."),
    ],
    [
        event("909 CE", "The Fatimid Caliphate is founded in North Africa."),
        event("960 CE", "The Song Dynasty is founded in China, ushering in an era of economic and technological flourishing."),
        event("962 CE", "Otto I is crowned Holy Roman Emperor."),
        event("969 CE", "The Fatimids conquer Egypt and found Cairo as their new capital."),
        event("c. 1000 CE", "Leif Erikson reaches North America, centuries before Columbus."),
    ],
)

print(f"Stage D (1st-10th c. CE) ready. {len(PERIODS)} period(s) so far.")

# ─── Stage E: 11th–20th century CE (1001–2000 CE) ──────────────────────────

add_ce(
    11, "⛪",
    "Christianity formally splits into Catholic and Orthodox branches, the Normans conquer England, Seljuk Turks open Anatolia to Turkic settlement, and the First Crusade sets out for the Holy Land.",
    [
        region("Byzantine Empire (Manzikert, battle site)", 39.1434, 42.5372, "Seljuk Turks defeat the Byzantines here in 1071, opening Anatolia to Turkic settlement."),
        region("Norman England (Hastings, battle site)", 50.8552, 0.5729, "William the Conqueror defeats King Harold here in 1066, beginning Norman rule of England."),
        region("Song Dynasty China (Kaifeng)", 34.7986, 114.3416, "Bi Sheng invents movable-type printing here around the 1040s."),
    ],
    [
        event("c. 1040s CE", "Bi Sheng invents movable-type printing in Song China."),
        event("1054 CE", "The Great Schism splits Christianity into Catholic and Orthodox branches."),
        event("1066 CE", "The Norman Conquest of England: William the Conqueror defeats King Harold at Hastings."),
        event("1071 CE", "Seljuk Turks defeat the Byzantines at the Battle of Manzikert, opening Anatolia to Turkic settlement."),
        event("1096 CE", "The First Crusade is launched to reclaim the Holy Land."),
    ],
)

add_ce(
    12, "🛕",
    "The Khmer Empire builds the largest religious monument in the world at Angkor Wat, a Sicilian court produces one of the great works of medieval Islamic cartography, and Saladin recaptures Jerusalem from the Crusaders.",
    [
        region("Khmer Empire (Angkor)", 13.4125, 103.867, "Home to Angkor Wat, built under Suryavarman II as the largest religious monument in the world."),
        region("Norman Sicily (Palermo)", 38.1157, 13.3615, "Cosmopolitan court of King Roger II, where al-Idrisi completes the Tabula Rogeriana."),
        region("Ayyubid-ruled Jerusalem", 31.7683, 35.2137, "Recaptured from the Crusaders by Saladin in 1187."),
    ],
    [
        event("c. 1113–1150 CE", "Angkor Wat is built by the Khmer Empire, the largest religious monument in the world."),
        event("1127 CE", "The Jin dynasty conquers northern China, forcing the Song court south into the Southern Song period."),
        event("1154 CE", "Muhammad al-Idrisi completes the Tabula Rogeriana for King Roger II of Sicily."),
        event("1187 CE", "Saladin recaptures Jerusalem from the Crusaders."),
    ],
    [fmap(
        "Tabula Rogeriana",
        "1154 CE",
        "Al-Idrisi's landmark medieval world map, compiled for King Roger II of Sicily.",
        "https://en.wikipedia.org/wiki/Tabula_Rogeriana",
    )],
)

add_ce(
    13, "🐎",
    "Genghis Khan unites the Mongol tribes and builds history's largest contiguous land empire, England's king is forced to accept the Magna Carta, and the Mongols complete their conquest of China.",
    [
        region("Mongol Empire (Karakorum)", 47.1996, 102.8391, "Capital of the largest contiguous land empire in history, founded after Genghis Khan united the Mongol tribes."),
        region("England (Runnymede)", 51.4419, -0.5606, "Site where King John is forced to sign the Magna Carta in 1215, limiting royal power."),
        region("Yuan Dynasty China (Khanbaliq, modern Beijing)", 39.9042, 116.4074, "New capital founded by Kublai Khan after completing the Mongol conquest of Song China."),
    ],
    [
        event("1206 CE", "Genghis Khan unites the Mongol tribes and begins building history's largest contiguous land empire."),
        event("1215 CE", "King John of England signs the Magna Carta, limiting royal power."),
        event("1271–1295 CE", "Marco Polo travels the Silk Road to the court of Kublai Khan."),
        event("1279 CE", "The Mongols complete their conquest of Song China, founding the Yuan Dynasty."),
    ],
)

add_ce(
    14, "☠️",
    "The Black Death kills roughly a third of Europe's population, the Hundred Years' War begins between England and France, Mansa Musa's legendary pilgrimage announces the wealth of the Mali Empire, and the Ming Dynasty replaces Mongol rule in China.",
    [
        region("Mali Empire (Niani)", 11.3667, -8.6667, "Capital of the Mali Empire under Mansa Musa, whose 1324 pilgrimage to Mecca became legendary for its wealth."),
        region("Plague-stricken Europe (Florence)", 43.7696, 11.2558, "One of many European cities devastated by the Black Death, later immortalized in Boccaccio's Decameron."),
        region("Ming Dynasty China (Nanjing)", 32.0603, 118.7969, "First capital of the Ming Dynasty, founded after overthrowing Mongol Yuan rule."),
    ],
    [
        event("1324 CE", "Mansa Musa of the Mali Empire makes his famous pilgrimage to Mecca, displaying immense wealth."),
        event("1337 CE", "The Hundred Years' War begins between England and France."),
        event("1347–1351 CE", "The Black Death kills roughly a third of Europe's population."),
        event("1368 CE", "The Ming Dynasty is founded in China after overthrowing the Mongol Yuan Dynasty."),
    ],
)

add_ce(
    15, "🖨️",
    "Gutenberg's printing press transforms the spread of knowledge in Europe, the Ottomans capture Constantinople ending the Byzantine Empire, and European sailors reach the Americas and India by sea for the first time.",
    [
        region("Holy Roman Empire (Mainz)", 49.9929, 8.2473, "Johannes Gutenberg develops the movable-type printing press here around 1440."),
        region("Ottoman Empire (Constantinople, conquered 1453)", 41.0082, 28.9784, "Falls to the Ottomans, ending the Byzantine Empire after over a thousand years."),
        region("Spanish Empire (Granada, conquered 1492)", 37.1773, -3.5986, "Last Muslim stronghold in Iberia, falls the same year Columbus sails for the Americas."),
    ],
    [
        event("c. 1440 CE", "Johannes Gutenberg develops the movable-type printing press in Europe."),
        event("1453 CE", "The Ottoman Empire captures Constantinople, ending the Byzantine Empire."),
        event("1492 CE", "Christopher Columbus reaches the Americas; the same year, Spain's Reconquista concludes with the fall of Granada."),
        event("1498 CE", "Vasco da Gama reaches India by sea around Africa."),
    ],
    [fmap(
        "Waldseemüller Map",
        "1507 CE",
        "The first map to use the name \"America\", made just a few years after Columbus's voyages entered European awareness.",
        "https://en.wikipedia.org/wiki/Waldseem%C3%BCller_map",
    )],
)

add_ce(
    16, "⛪",
    "Martin Luther's protest splits Western Christianity, Spanish conquistadors topple the Aztec and Inca empires, Magellan's crew completes the first circumnavigation of the globe, and the Mughal Empire is founded in India.",
    [
        region("Aztec Empire (Tenochtitlan, conquered 1521)", 19.4326, -99.1332, "Falls to Hernán Cortés and his allies in 1521."),
        region("Inca Empire (Cusco, conquered 1533)", -13.5319, -71.9675, "Falls to Francisco Pizarro in 1533."),
        region("Mughal Empire (Agra)", 27.1767, 78.0081, "Founded by Babur in 1526, beginning one of history's wealthiest empires."),
        region("Holy Roman Empire (Wittenberg)", 51.8666, 12.6489, "Martin Luther's 1517 protest here sparks the Protestant Reformation."),
    ],
    [
        event("1517 CE", "Martin Luther's Ninety-Five Theses spark the Protestant Reformation."),
        event("1519–1522 CE", "Ferdinand Magellan's expedition completes the first circumnavigation of the globe."),
        event("1521 CE", "Hernán Cortés conquers the Aztec Empire."),
        event("1526 CE", "Babur founds the Mughal Empire in India."),
        event("1533 CE", "Francisco Pizarro conquers the Inca Empire."),
    ],
    [fmap(
        "Mercator World Map (1569)",
        "1569 CE",
        "Gerardus Mercator's projection, designed for sailors, still underlies most digital maps today.",
        "https://en.wikipedia.org/wiki/Mercator_1569_world_map",
    )],
)

add_ce(
    17, "🔭",
    "The Thirty Years' War devastates Central Europe, the Qing Dynasty replaces Ming rule in China after a Manchu conquest, and Isaac Newton's Principia lays the foundations of modern physics.",
    [
        region("Holy Roman Empire, war-torn (Münster)", 51.9607, 7.6261, "Site of the 1648 peace treaties ending the devastating Thirty Years' War."),
        region("Qing Dynasty China (Beijing)", 39.9042, 116.4074, "New Manchu-ruled capital after the conquest of Ming China in 1644."),
        region("Kingdom of England (Cambridge)", 52.2043, 0.1218, "Isaac Newton develops the ideas behind his 1687 Principia Mathematica."),
    ],
    [
        event("1618–1648 CE", "The Thirty Years' War devastates Central Europe."),
        event("1644 CE", "The Qing Dynasty is founded after Manchu forces conquer Ming China."),
        event("1687 CE", "Isaac Newton publishes the Principia Mathematica, a cornerstone of the Scientific Revolution."),
    ],
)

add_ce(
    18, "🗽",
    "Britain's Industrial Revolution begins transforming the world economy, the Seven Years' War is fought across multiple continents, the United States declares independence, and the French Revolution ends absolute monarchy in France.",
    [
        region("Kingdom of Great Britain (birthplace of the Industrial Revolution)", 53.4808, -2.2426, "Manchester and the surrounding region become the crucible of the Industrial Revolution from the 1760s."),
        region("United States (Philadelphia)", 39.9526, -75.1652, "The Declaration of Independence is signed here in 1776."),
        region("Kingdom of France (Paris)", 48.8566, 2.3522, "The French Revolution begins here in 1789, ending absolute monarchy."),
    ],
    [
        event("1756–1763 CE", "The Seven Years' War is fought across multiple continents."),
        event("1776 CE", "The United States declares independence from Britain."),
        event("1789 CE", "The French Revolution begins, ending absolute monarchy in France."),
        event("c. 1760s CE", "The Industrial Revolution begins in Britain."),
    ],
    [fmap(
        "Cassini Map of France",
        "Completed 1789 CE",
        "The first map of an entire country based on precise triangulated survey.",
        "https://en.wikipedia.org/wiki/Cassini_map",
    )],
)

add_ce(
    19, "🏭",
    "Napoleon's conquests reshape Europe, industrialization accelerates, the United States abolishes slavery after a civil war, Japan rapidly modernizes, and European powers partition nearly the entire African continent.",
    [
        region("Napoleonic France (Paris)", 48.8566, 2.3522, "Napoleon crowns himself Emperor in 1804, briefly dominating continental Europe."),
        region("United States (Washington D.C.)", 38.9072, -77.0369, "The Union prevails in the 1861-1865 Civil War, ending slavery."),
        region("Empire of Japan (Tokyo)", 35.6762, 139.6503, "The 1868 Meiji Restoration begins Japan's rapid modernization."),
        region("Partitioned Africa (Berlin, conference site)", 52.52, 13.405, "European powers formalize their colonial claims across Africa at the 1884-85 Berlin Conference."),
    ],
    [
        event("1804 CE", "Napoleon crowns himself Emperor of the French."),
        event("1861–1865 CE", "The American Civil War ends slavery in the United States."),
        event("1868 CE", "Japan's Meiji Restoration begins rapid modernization."),
        event("1871 CE", "Germany and Italy are unified as modern nation-states."),
        event("1884–1885 CE", "The Berlin Conference formalizes the European colonial partition of Africa."),
    ],
)

add_ce(
    20, "🌐",
    "Two world wars, a global pandemic, and a decades-long Cold War reshape the planet, decolonization creates dozens of new nations, humans land on the Moon, and the century ends with the Soviet Union's collapse and the birth of the World Wide Web.",
    [
        region("World War I & II Europe (Sarajevo)", 43.8563, 18.4131, "The 1914 assassination here triggers World War I; the continent is engulfed again in World War II from 1939."),
        region("Russian Revolution (Petrograd/Saint Petersburg)", 59.9311, 30.3609, "The 1917 Russian Revolution overthrows the Tsar, bringing the Bolsheviks to power."),
        region("United Nations founding (San Francisco)", 37.7749, -122.4194, "Delegates draft the UN Charter here in 1945, founding the United Nations."),
        region("Cold War's end (Berlin)", 52.52, 13.405, "The Berlin Wall falls in 1989, foreshadowing the Soviet Union's 1991 collapse."),
    ],
    [
        event("1914–1918 CE", "World War I, triggered by the assassination of Archduke Franz Ferdinand in Sarajevo."),
        event("1917 CE", "The Russian Revolution overthrows the Tsar and brings the Bolsheviks to power."),
        event("1939–1945 CE", "World War II, the deadliest conflict in human history."),
        event("1945 CE", "The United Nations is founded to promote international peace and cooperation."),
        event("1969 CE", "Apollo 11 lands the first humans on the Moon."),
        event("1989–1991 CE", "The Berlin Wall falls and the Soviet Union dissolves, ending the Cold War."),
    ],
)

# ─── Stage F: 21st century CE, partial (2001–2025) ─────────────────────────

PERIODS.append(make_period(
    "century_21_ce",
    "21st century CE (so far)",
    "2001–2025 CE",
    "🌍",
    "The century opens with a new era of global security concerns, a financial crisis, and a smartphone-and-social-media revolution, then a once-in-a-century pandemic -- and closes (so far) with the rapid rise of generative artificial intelligence.",
    [
        region("United States (New York, September 11 attacks)", 40.7128, -74.006, "The September 11, 2001 attacks reshape global security policy for decades."),
        region("Global financial system (New York, Wall Street)", 40.7069, -74.0113, "Epicentre of the 2008 financial crisis, which triggered a worldwide recession."),
        region("COVID-19 origin (Wuhan)", 30.5928, 114.3055, "Where the COVID-19 pandemic was first identified in late 2019, before spreading worldwide in 2020."),
        region("Generative AI boom (San Francisco)", 37.7749, -122.4194, "Hub of the generative AI boom that accelerated rapidly after ChatGPT's 2022 launch."),
    ],
    [
        event("2001 CE", "The September 11 attacks reshape global security policy."),
        event("2008 CE", "The global financial crisis triggers a worldwide recession."),
        event("2020–2023 CE", "The COVID-19 pandemic becomes the first truly global pandemic of the internet era."),
        event("2022 CE", "The launch of ChatGPT popularizes generative AI, beginning a rapid new wave of artificial intelligence technology."),
        event("Today", "Nearly 200 sovereign states are recognized by the United Nations -- explore them all on the World Map above."),
    ],
    [fmap(
        "Google Earth & modern satellite mapping",
        "Launched 2005",
        "For the first time, anyone with an internet connection could view detailed satellite imagery of the entire planet.",
        "https://en.wikipedia.org/wiki/Google_Earth",
    )],
))

print(f"All stages ready. {len(PERIODS)} period(s) total.")


def main() -> None:
    ids = [p["id"] for p in PERIODS]
    assert len(ids) == len(set(ids)), f"duplicate period ids: {[i for i in ids if ids.count(i) > 1]}"
    for p in PERIODS:
        assert len(p["regions"]) >= 3, p["id"]
        for r in p["regions"]:
            assert -90 <= r["lat"] <= 90 and -180 <= r["lng"] <= 180, (p["id"], r)
        assert len(p["events"]) >= 2, p["id"]
        for m in p.get("famous_maps", []):
            assert m["link"].startswith("https://"), (p["id"], m)

    OUT_PATH.write_text(json.dumps({"periods": PERIODS}, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(PERIODS)} periods to {OUT_PATH}")


if __name__ == "__main__":
    main()
