#!/usr/bin/env python3
"""Depth pass, M1 General Knowledge: fill in real, hand-checked
data_table content for the 99 M1 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings M1 General
Knowledge to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "general-knowledge-m1-l1": {
        "data_table": table(["Skill", "Purpose"], [
            ["Media literacy", "Evaluates the credibility and bias of information sources"],
        ]),
    },
    "general-knowledge-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Interdisciplinary general studies", "Draws connections across separate fields to build integrated understanding"],
        ]),
    },
    "general-knowledge-m1-l4": {
        "data_table": table(["Tradition", "Core Belief"], [
            ["Buddhism", "The end of suffering through following the Noble Eightfold Path"],
            ["Hinduism", "Diverse traditions centered on dharma, karma, and moksha"],
        ]),
    },
    "general-knowledge-m1-l5": {
        "data_table": table(["System", "Feature"], [
            ["Market economy", "Prices set primarily by supply and demand"],
            ["Mixed economy", "Combines market mechanisms with government intervention"],
        ]),
    },
    "general-knowledge-m1-l6": {
        "data_table": table(["Innovation", "Impact"], [
            ["Printing press", "Massively expanded the spread of written knowledge"],
        ]),
    },
    "general-knowledge-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["World geography synthesis", "Connects physical features, climate, and human settlement patterns"],
        ]),
    },
    "general-knowledge-m1-l8": {
        "data_table": table(["Region", "Cultural Note"], [
            ["East Asia", "Confucian values historically shaped social and educational norms"],
        ]),
    },
    "general-knowledge-m1-l9": {
        "data_table": table(["Puzzle Type", "Skill Practiced"], [
            ["Logic grid puzzle", "Deductive reasoning from a set of constraints"],
        ]),
    },
    "general-knowledge-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["General science literacy", "Understanding basic scientific method and core findings across fields"],
        ]),
    },
    "general-knowledge-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Compound interest", "Interest calculated on both principal and previously accumulated interest"],
        ]),
    },
    "general-knowledge-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Civic knowledge", "Understanding of government structure, rights, and civic responsibility"],
        ]),
    },
    "general-knowledge-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental literacy", "Understanding of ecosystems, sustainability, and human environmental impact"],
        ]),
    },
    "general-knowledge-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Health literacy", "Ability to find, understand, and use health information effectively"],
        ]),
    },
    "general-knowledge-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Technology literacy", "Functional understanding of how digital tools and systems work"],
        ]),
    },
    "general-knowledge-m1-l16": {
        "data_table": table(["Figure", "Field"], [
            ["Marie Curie", "Physics and chemistry — pioneering research on radioactivity"],
        ]),
    },
    "general-knowledge-m1-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Trivia question design", "Balances difficulty and clarity to test recall without ambiguity"],
        ]),
    },
    "general-knowledge-m1-l18": {
        "data_table": table(["Step", "Purpose"], [
            ["Source triangulation", "Confirms a claim across multiple independent, credible sources"],
        ]),
    },
    "general-knowledge-m1-l19": {
        "data_table": table(["Organization", "Focus"], [
            ["World Health Organization", "Coordinates international public health policy and response"],
        ]),
    },
    "general-knowledge-m1-l20": {
        "data_table": table(["Fallacy", "Description"], [
            ["Ad hominem", "Attacks the person rather than the argument"],
        ]),
    },
    "general-knowledge-m1-l21": {
        "data_table": table(["Category", "Field"], [
            ["Nobel Prize categories", "Physics, Chemistry, Medicine, Literature, Peace, and Economic Sciences"],
        ]),
    },
    "general-knowledge-m1-l22": {
        "data_table": table(["Wonder", "Era"], [
            ["Great Pyramid of Giza", "The only ancient wonder still substantially standing today"],
            ["Great Wall of China", "Commonly cited among the modern wonders"],
        ]),
    },
    "general-knowledge-m1-l23": {
        "data_table": table(["Currency", "Origin"], [
            ["Pound sterling", "One of the oldest currencies still in use, dating to Anglo-Saxon England"],
        ]),
    },
    "general-knowledge-m1-l24": {
        "data_table": table(["Element", "Common Symbolism"], [
            ["Color red", "Frequently represents courage, revolution, or bloodshed on national flags"],
        ]),
    },
    "general-knowledge-m1-l25": {
        "data_table": table(["City", "Name Change"], [
            ["Istanbul", "Formerly Constantinople, renamed following Turkish nation-building"],
        ]),
    },
    "general-knowledge-m1-l26": {
        "data_table": table(["River", "Significance"], [
            ["Nile", "Historically sustained Egyptian agriculture and civilization"],
        ]),
    },
    "general-knowledge-m1-l27": {
        "data_table": table(["Range", "Notable Peak"], [
            ["Himalayas", "Home to Mount Everest, the world's highest peak above sea level"],
        ]),
    },
    "general-knowledge-m1-l28": {
        "data_table": table(["Desert", "Feature"], [
            ["Sahara", "The world's largest hot desert, spanning much of North Africa"],
        ]),
    },
    "general-knowledge-m1-l29": {
        "data_table": table(["Era", "Feature"], [
            ["Modern Olympic movement", "Revived in 1896, has grown into a major global sporting institution"],
        ]),
    },
    "general-knowledge-m1-l30": {
        "data_table": table(["Religion", "Sacred Text"], [
            ["Christianity", "The Bible"],
            ["Islam", "The Quran"],
        ]),
    },
    "general-knowledge-m1-l31": {
        "data_table": table(["Family", "Example Languages"], [
            ["Indo-European", "Includes English, Spanish, Hindi, and Russian, spoken by billions"],
        ]),
    },
    "general-knowledge-m1-l32": {
        "data_table": table(["Empire", "Territorial Peak"], [
            ["British Empire", "Once the largest empire in history by land area"],
        ]),
    },
    "general-knowledge-m1-l33": {
        "data_table": table(["Treaty", "Significance"], [
            ["Paris Agreement", "International accord targeting global climate change mitigation"],
        ]),
    },
    "general-knowledge-m1-l34": {
        "data_table": table(["Criterion", "Detail"], [
            ["UNESCO outstanding universal value", "Core standard a site must meet for World Heritage designation"],
        ]),
    },
    "general-knowledge-m1-l35": {
        "data_table": table(["Milestone", "Year"], [
            ["First human spaceflight", "1961"],
            ["First Moon landing", "1969"],
        ]),
    },
    "general-knowledge-m1-l36": {
        "data_table": table(["Contribution", "Figure"], [
            ["TCP/IP protocol", "Vint Cerf and Bob Kahn, foundational to internet architecture"],
        ]),
    },
    "general-knowledge-m1-l37": {
        "data_table": table(["Invention", "Unintended Consequence"], [
            ["Automobile", "Enabled mobility but also produced significant pollution and urban sprawl"],
        ]),
    },
    "general-knowledge-m1-l38": {
        "data_table": table(["Stage", "Feature"], [
            ["Demographic transition", "Populations shift from high to low birth and death rates over development"],
        ]),
    },
    "general-knowledge-m1-l39": {
        "data_table": table(["Exchange", "Location"], [
            ["New York Stock Exchange", "The world's largest stock exchange by market capitalization"],
        ]),
    },
    "general-knowledge-m1-l40": {
        "data_table": table(["Element", "Detail"], [
            ["National anthem", "Often composed during moments of national founding or independence"],
        ]),
    },
    "general-knowledge-m1-l41": {
        "data_table": table(["Laureate", "Contribution"], [
            ["Nelson Mandela", "Awarded for ending South African apartheid through negotiated transition"],
        ]),
    },
    "general-knowledge-m1-l42": {
        "data_table": table(["Feat", "Detail"], [
            ["Suspension bridge engineering", "Enables extremely long spans by distributing load through cables"],
        ]),
    },
    "general-knowledge-m1-l43": {
        "data_table": table(["Civilization", "River"], [
            ["Mesopotamia", "Tigris and Euphrates"],
            ["Egypt", "Nile"],
            ["Indus Valley", "Indus"],
        ]),
    },
    "general-knowledge-m1-l44": {
        "data_table": table(["Route", "Exchange"], [
            ["Silk Road", "Connected distant civilizations through goods, ideas, and disease"],
        ]),
    },
    "general-knowledge-m1-l45": {
        "data_table": table(["Pandemic", "Impact"], [
            ["Black Death", "Killed an estimated third of Europe's population in the 14th century"],
        ]),
    },
    "general-knowledge-m1-l46": {
        "data_table": table(["Museum", "Collection"], [
            ["The Louvre", "Home to the Mona Lisa and one of the world's largest art collections"],
        ]),
    },
    "general-knowledge-m1-l47": {
        "data_table": table(["Country", "Signature Dish"], [
            ["Italy", "Pasta and pizza, rooted in regional culinary tradition"],
        ]),
    },
    "general-knowledge-m1-l48": {
        "data_table": table(["Championship", "Detail"], [
            ["FIFA World Cup", "The most-watched recurring sporting event globally"],
        ]),
    },
    "general-knowledge-m1-l49": {
        "data_table": table(["Building", "Innovation"], [
            ["Burj Khalifa", "Currently the world's tallest building, using advanced structural engineering"],
        ]),
    },
    "general-knowledge-m1-l50": {
        "data_table": table(["System", "Feature"], [
            ["Gold standard", "Historically pegged a currency's value to a fixed quantity of gold"],
        ]),
    },
    "general-knowledge-m1-l51": {
        "data_table": table(["Journal", "Significance"], [
            ["Nature", "One of the oldest and most cited multidisciplinary scientific journals"],
        ]),
    },
    "general-knowledge-m1-l52": {
        "data_table": table(["Park", "Significance"], [
            ["Yellowstone", "The world's first officially designated national park"],
        ]),
    },
    "general-knowledge-m1-l53": {
        "data_table": table(["Standard", "Purpose"], [
            ["UTC/Coordinated Universal Time", "Provides a common global time reference"],
        ]),
    },
    "general-knowledge-m1-l54": {
        "data_table": table(["System", "Origin"], [
            ["Phoenician alphabet", "An ancestor of many modern alphabetic writing systems"],
        ]),
    },
    "general-knowledge-m1-l55": {
        "data_table": table(["Philosopher", "Idea"], [
            ["Socrates", "Advocated for rigorous self-examination through questioning"],
        ]),
    },
    "general-knowledge-m1-l56": {
        "data_table": table(["Movement", "Founder"], [
            ["Cubism", "Pablo Picasso and Georges Braque"],
        ]),
    },
    "general-knowledge-m1-l57": {
        "data_table": table(["Composer", "Landmark Work"], [
            ["Beethoven", "Symphony No. 9"],
        ]),
    },
    "general-knowledge-m1-l58": {
        "data_table": table(["Industry", "Note"], [
            ["Bollywood (India)", "Produces more films annually than Hollywood"],
        ]),
    },
    "general-knowledge-m1-l59": {
        "data_table": table(["Game", "Origin"], [
            ["Chess", "Traces its roots to ancient India before spreading globally"],
        ]),
    },
    "general-knowledge-m1-l60": {
        "data_table": table(["Champion", "Note"], [
            ["Garry Kasparov", "Held the world chess championship title for many years"],
        ]),
    },
    "general-knowledge-m1-l61": {
        "data_table": table(["Development", "Impact"], [
            ["Mercator projection", "Enabled reliable maritime navigation despite distorting relative land area"],
        ]),
    },
    "general-knowledge-m1-l62": {
        "data_table": table(["Eruption", "Impact"], [
            ["Mount Tambora (1815)", "Caused global cooling and the 'Year Without a Summer'"],
        ]),
    },
    "general-knowledge-m1-l63": {
        "data_table": table(["Wreck", "Significance"], [
            ["Titanic", "Its 1912 sinking led to major reforms in maritime safety regulation"],
        ]),
    },
    "general-knowledge-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Endangered language", "A language at risk of no longer being passed to new generations"],
        ]),
    },
    "general-knowledge-m1-l65": {
        "data_table": table(["Calendar", "Feature"], [
            ["Gregorian calendar", "The internationally dominant civil calendar, refined from the Julian calendar"],
        ]),
    },
    "general-knowledge-m1-l66": {
        "data_table": table(["Agency", "Country"], [
            ["NASA", "United States"],
            ["ESA", "Europe, a collaborative multinational agency"],
        ]),
    },
    "general-knowledge-m1-l67": {
        "data_table": table(["Item", "Significance"], [
            ["Penny Black", "The world's first adhesive postage stamp, issued in 1840"],
        ]),
    },
    "general-knowledge-m1-l68": {
        "data_table": table(["Airport", "Note"], [
            ["Hartsfield-Jackson Atlanta", "Historically among the busiest airports by passenger traffic"],
        ]),
    },
    "general-knowledge-m1-l69": {
        "data_table": table(["Currency", "Detail"], [
            ["Deutsche Mark", "Replaced by the euro in Germany's currency transition"],
        ]),
    },
    "general-knowledge-m1-l70": {
        "data_table": table(["Library", "Significance"], [
            ["Library of Alexandria", "One of the largest and most significant libraries of the ancient world"],
        ]),
    },
    "general-knowledge-m1-l71": {
        "data_table": table(["River", "Length Note"], [
            ["Nile/Amazon", "Compete for the title of the world's longest river depending on measurement method"],
        ]),
    },
    "general-knowledge-m1-l72": {
        "data_table": table(["Fair", "Legacy"], [
            ["1889 Paris Exposition", "Introduced the Eiffel Tower as its centerpiece"],
        ]),
    },
    "general-knowledge-m1-l73": {
        "data_table": table(["Device", "Era"], [
            ["Sundial", "One of the earliest instruments used to track time"],
        ]),
    },
    "general-knowledge-m1-l74": {
        "data_table": table(["Federation", "Role"], [
            ["International Olympic Committee", "Oversees the organization of the Olympic Games globally"],
        ]),
    },
    "general-knowledge-m1-l75": {
        "data_table": table(["Language", "Note"], [
            ["Mandarin Chinese", "The most spoken native language in the world by total speakers"],
        ]),
    },
    "general-knowledge-m1-l76": {
        "data_table": table(["Discovery", "Significance"], [
            ["Terracotta Army", "Revealed the scale of the first Qin emperor's funerary complex"],
        ]),
    },
    "general-knowledge-m1-l77": {
        "data_table": table(["Feature", "Detail"], [
            ["Nobel Prize in Literature", "Awarded since 1901 to authors of outstanding contribution in an idealistic direction"],
        ]),
    },
    "general-knowledge-m1-l78": {
        "data_table": table(["Constant", "Discoverer"], [
            ["Pi (π)", "Studied since antiquity, with Archimedes providing an early rigorous approximation"],
        ]),
    },
    "general-knowledge-m1-l79": {
        "data_table": table(["Adaptation", "Detail"], [
            ["Desert human adaptation", "Traditional communities developed water-conserving lifestyles and architecture"],
        ]),
    },
    "general-knowledge-m1-l80": {
        "data_table": table(["Organization", "Role"], [
            ["World Trade Organization", "Sets rules governing international trade between member nations"],
        ]),
    },
    "general-knowledge-m1-l81": {
        "data_table": table(["Leader", "Contribution"], [
            ["Winston Churchill", "Led Britain through World War II as a defining wartime leader"],
        ]),
    },
    "general-knowledge-m1-l82": {
        "data_table": table(["Wonder", "Feature"], [
            ["Grand Canyon", "A vast natural gorge carved by the Colorado River over millions of years"],
        ]),
    },
    "general-knowledge-m1-l83": {
        "data_table": table(["Era", "Feature"], [
            ["Silent film era", "Relied on visual storytelling and live musical accompaniment before synchronized sound"],
        ]),
    },
    "general-knowledge-m1-l84": {
        "data_table": table(["Site", "Tradition"], [
            ["Mecca", "The most significant pilgrimage site in Islam"],
        ]),
    },
    "general-knowledge-m1-l85": {
        "data_table": table(["Instrument", "Inventor"], [
            ["Telescope", "Commonly attributed to Hans Lippershey, later refined by Galileo"],
        ]),
    },
    "general-knowledge-m1-l86": {
        "data_table": table(["System", "Detail"], [
            ["Metric system", "Originated in revolutionary France and spread through global standardization efforts"],
        ]),
    },
    "general-knowledge-m1-l87": {
        "data_table": table(["University", "Founded"], [
            ["University of Bologna", "Widely considered the oldest continuously operating university"],
        ]),
    },
    "general-knowledge-m1-l88": {
        "data_table": table(["Canal", "Significance"], [
            ["Suez Canal", "Connects the Mediterranean and Red Seas, a critical global shipping route"],
        ]),
    },
    "general-knowledge-m1-l89": {
        "data_table": table(["Network", "Impact"], [
            ["International telegraph network", "Dramatically accelerated global communication before the internet"],
        ]),
    },
    "general-knowledge-m1-l90": {
        "data_table": table(["Reef", "Significance"], [
            ["Great Barrier Reef", "The world's largest coral reef system, visible even from space"],
        ]),
    },
    "general-knowledge-m1-l91": {
        "data_table": table(["Guild", "Role"], [
            ["Medieval trade guild", "Regulated craft standards, training, and pricing within a trade"],
        ]),
    },
    "general-knowledge-m1-l92": {
        "data_table": table(["Record", "Detail"], [
            ["Human achievement record", "Guinness World Records documents extremes of human capability"],
        ]),
    },
    "general-knowledge-m1-l93": {
        "data_table": table(["Feature", "Purpose"], [
            ["Currency watermark", "Anti-counterfeiting measure embedded during banknote production"],
        ]),
    },
    "general-knowledge-m1-l94": {
        "data_table": table(["Volcano", "Tectonic Setting"], [
            ["Mount Fuji", "Located along a subduction zone at a tectonic plate boundary"],
        ]),
    },
    "general-knowledge-m1-l95": {
        "data_table": table(["City", "Rediscovery"], [
            ["Machu Picchu", "Brought to wide international attention in 1911"],
        ]),
    },
    "general-knowledge-m1-l96": {
        "data_table": table(["System", "Detail"], [
            ["Modern passport", "Standardized international travel documentation developed largely after World War I"],
        ]),
    },
    "general-knowledge-m1-l97": {
        "data_table": table(["Language", "Note"], [
            ["American Sign Language", "A complete natural language distinct from spoken English"],
        ]),
    },
    "general-knowledge-m1-l98": {
        "data_table": table(["Hoax", "Exposure"], [
            ["Piltdown Man", "A fabricated fossil exposed decades later through scientific dating methods"],
        ]),
    },
    "general-knowledge-m1-l99": {
        "data_table": table(["Standard", "Detail"], [
            ["International System of Units (SI)", "Provides a globally standardized basis for scientific measurement"],
        ]),
    },
    "general-knowledge-m1-l100": {
        "data_table": table(["Incident", "Consequence"], [
            ["Diplomatic protocol breach", "Even minor incidents can strain formal relations between nations"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Intellectual Movement", "Approx. Period"], [
        ["The Renaissance", "14th-17th century"],
        ["The Enlightenment", "17th-18th century"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"general-knowledge-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"general-knowledge-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"general-knowledge-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 General Knowledge lessons (completing 120/120).")


if __name__ == "__main__":
    main()
