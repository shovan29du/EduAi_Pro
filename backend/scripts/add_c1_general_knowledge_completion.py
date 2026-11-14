#!/usr/bin/env python3
"""Depth pass, C1 General Knowledge: fill in real, hand-checked
data_table content for the 69 C1 General Knowledge lessons not covered
by the earlier breadth-first batch. Brings C1 General Knowledge to full
70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "general-knowledge-c1-l1": {
        "data_table": table(["Practice", "Benefit"], [
            ["Reading multiple sources", "Reduces the risk of a single biased viewpoint"],
        ]),
    },
    "general-knowledge-c1-l2": {
        "data_table": table(["Institution", "Purpose"], [
            ["United Nations", "Promotes international peace and cooperation"], ["World Bank", "Provides financing for development projects"],
        ]),
    },
    "general-knowledge-c1-l3": {
        "data_table": table(["Movement", "Core Idea"], [
            ["Enlightenment", "Reason and individual rights over tradition and authority"],
        ]),
    },
    "general-knowledge-c1-l4": {
        "data_table": table(["Religion", "Founded"], [
            ["Buddhism", "India, 6th century BCE"], ["Islam", "Arabia, 7th century CE"],
        ]),
    },
    "general-knowledge-c1-l5": {
        "data_table": table(["System", "Feature"], [
            ["Capitalism", "Private ownership and market-driven pricing"], ["Socialism", "Collective or state ownership of production"],
        ]),
    },
    "general-knowledge-c1-l6": {
        "data_table": table(["Invention", "Impact"], [
            ["Printing press", "Enabled mass production and spread of written knowledge"],
        ]),
    },
    "general-knowledge-c1-l7": {
        "data_table": table(["Feature", "Fact"], [
            ["Largest continent", "Asia"], ["Longest river", "Nile (or Amazon, by some measures)"],
        ]),
    },
    "general-knowledge-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural literacy", "Familiarity with the shared knowledge and references of a culture"],
        ]),
    },
    "general-knowledge-c1-l9": {
        "data_table": table(["Skill", "Application"], [
            ["Deductive reasoning", "Drawing a specific conclusion from general premises"],
        ]),
    },
    "general-knowledge-c1-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Scientific method", "A systematic process of observation, hypothesis, and testing"],
        ]),
    },
    "general-knowledge-c1-l11": {
        "data_table": table(["Concept", "Meaning"], [
            ["Compound interest", "Interest calculated on both principal and accumulated interest"],
        ]),
    },
    "general-knowledge-c1-l12": {
        "data_table": table(["Branch", "Role"], [
            ["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "general-knowledge-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Carbon footprint", "The total greenhouse gas emissions caused by an individual or activity"],
        ]),
    },
    "general-knowledge-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Health literacy", "The ability to understand and use health information to make decisions"],
        ]),
    },
    "general-knowledge-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital literacy", "The ability to effectively find, evaluate, and use digital information"],
        ]),
    },
    "general-knowledge-c1-l16": {
        "data_table": table(["Figure", "Field"], [
            ["Marie Curie", "Physics and chemistry"], ["Leonardo da Vinci", "Art and science"],
        ]),
    },
    "general-knowledge-c1-l17": {
        "data_table": table(["Category", "Example Question Type"], [
            ["Geography", "Capital cities and landmarks"], ["Science", "Discoveries and inventors"],
        ]),
    },
    "general-knowledge-c1-l18": {
        "data_table": table(["Step", "Purpose"], [
            ["Checking the original source", "Verifies a claim wasn't distorted by retelling"],
        ]),
    },
    "general-knowledge-c1-l19": {
        "data_table": table(["Organization", "Focus"], [
            ["WHO", "Global public health"], ["WTO", "International trade rules"],
        ]),
    },
    "general-knowledge-c1-l20": {
        "data_table": table(["Fallacy", "Example"], [
            ["Ad hominem", "Attacking the person instead of their argument"],
        ]),
    },
    "general-knowledge-c1-l21": {
        "data_table": table(["Agency", "Focus"], [
            ["UNESCO", "Education, science, and culture"], ["UNICEF", "Children's welfare"],
        ]),
    },
    "general-knowledge-c1-l22": {
        "data_table": table(["System", "Feature"], [
            ["Presidential system", "Separate executive elected independently of the legislature"], ["Parliamentary system", "Executive drawn from and accountable to the legislature"],
        ]),
    },
    "general-knowledge-c1-l23": {
        "data_table": table(["Religion", "Sacred Text"], [
            ["Christianity", "The Bible"], ["Judaism", "The Torah"],
        ]),
    },
    "general-knowledge-c1-l24": {
        "data_table": table(["Era", "Development"], [
            ["Barter era", "Direct exchange of goods without money"], ["Coinage era", "Standardized metal currency"],
        ]),
    },
    "general-knowledge-c1-l25": {
        "data_table": table(["Currency", "Country"], [
            ["Yen", "Japan"], ["Euro", "Eurozone countries"],
        ]),
    },
    "general-knowledge-c1-l26": {
        "data_table": table(["Discovery", "Scientist"], [
            ["Theory of evolution", "Charles Darwin"], ["Penicillin", "Alexander Fleming"],
        ]),
    },
    "general-knowledge-c1-l27": {
        "data_table": table(["Range", "Location"], [
            ["Himalayas", "Asia, home to Mount Everest"], ["Andes", "South America, longest continental range"],
        ]),
    },
    "general-knowledge-c1-l28": {
        "data_table": table(["River", "Continent"], [
            ["Nile", "Africa"], ["Amazon", "South America"],
        ]),
    },
    "general-knowledge-c1-l29": {
        "data_table": table(["Category", "Example Laureate"], [
            ["Peace", "Malala Yousafzai"], ["Literature", "Gabriel García Márquez"],
        ]),
    },
    "general-knowledge-c1-l30": {
        "data_table": table(["Language", "Approx. Speakers"], [
            ["Mandarin Chinese", "Over 1 billion"], ["English", "Over 1.5 billion including second-language speakers"],
        ]),
    },
    "general-knowledge-c1-l31": {
        "data_table": table(["Invention", "Inventor"], [
            ["Telephone", "Alexander Graham Bell"], ["Light bulb", "Thomas Edison (commercial development)"],
        ]),
    },
    "general-knowledge-c1-l32": {
        "data_table": table(["Event", "Frequency"], [
            ["Olympic Games", "Every 4 years"], ["FIFA World Cup", "Every 4 years"],
        ]),
    },
    "general-knowledge-c1-l33": {
        "data_table": table(["Country", "Capital"], [
            ["Australia", "Canberra"], ["Brazil", "Brasília"],
        ]),
    },
    "general-knowledge-c1-l34": {
        "data_table": table(["Desert", "Continent"], [
            ["Sahara", "Africa, the largest hot desert"], ["Antarctic Desert", "Antarctica, the largest desert overall"],
        ]),
    },
    "general-knowledge-c1-l35": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space", "1961, Yuri Gagarin"], ["First Moon landing", "1969, Apollo 11"],
        ]),
    },
    "general-knowledge-c1-l36": {
        "data_table": table(["Museum", "Location"], [
            ["The Louvre", "Paris, France"], ["The Met", "New York, United States"],
        ]),
    },
    "general-knowledge-c1-l37": {
        "data_table": table(["Milestone", "Year"], [
            ["ARPANET launched", "1969"], ["World Wide Web invented", "1989"],
        ]),
    },
    "general-knowledge-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["International Date Line", "An imaginary line marking the change from one calendar day to the next"],
        ]),
    },
    "general-knowledge-c1-l39": {
        "data_table": table(["Milestone", "Approximate Year"], [
            ["World population reaches 1 billion", "1804"], ["World population reaches 8 billion", "2022"],
        ]),
    },
    "general-knowledge-c1-l40": {
        "data_table": table(["Religion", "Sacred Text"], [
            ["Islam", "The Quran"], ["Hinduism", "The Vedas"],
        ]),
    },
    "general-knowledge-c1-l41": {
        "data_table": table(["Milestone", "Detail"], [
            ["Athenian democracy", "Early direct democracy in ancient Greece, c. 5th century BCE"],
        ]),
    },
    "general-knowledge-c1-l42": {
        "data_table": table(["Structure", "Feature"], [
            ["Akashi Kaikyō Bridge", "One of the world's longest suspension bridge spans"],
        ]),
    },
    "general-knowledge-c1-l43": {
        "data_table": table(["Explorer", "Achievement"], [
            ["Ferdinand Magellan's expedition", "First to circumnavigate the globe"],
        ]),
    },
    "general-knowledge-c1-l44": {
        "data_table": table(["Species", "Status"], [
            ["Amur leopard", "Critically endangered"], ["Giant panda", "Vulnerable, population recovering"],
        ]),
    },
    "general-knowledge-c1-l45": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Stars", "Often represent states or provinces"], ["Colors like red", "Often symbolize courage or revolution"],
        ]),
    },
    "general-knowledge-c1-l46": {
        "data_table": table(["Organization", "Focus"], [
            ["World Health Organization", "Coordinates global public health responses"],
        ]),
    },
    "general-knowledge-c1-l47": {
        "data_table": table(["Milestone", "Year"], [
            ["First modern Olympics", "1896, Athens"],
        ]),
    },
    "general-knowledge-c1-l48": {
        "data_table": table(["Cuisine", "Signature Element"], [
            ["Italian", "Pasta and olive oil"], ["Thai", "Balance of sweet, sour, salty, and spicy"],
        ]),
    },
    "general-knowledge-c1-l49": {
        "data_table": table(["Landmark", "Architect/Style"], [
            ["The Sagrada Família", "Antoni Gaudí, Catalan Modernism"],
        ]),
    },
    "general-knowledge-c1-l50": {
        "data_table": table(["Metric", "Meaning"], [
            ["Literacy rate", "The percentage of a population able to read and write"],
        ]),
    },
    "general-knowledge-c1-l51": {
        "data_table": table(["Document", "Year"], [
            ["Universal Declaration of Human Rights", "1948"],
        ]),
    },
    "general-knowledge-c1-l52": {
        "data_table": table(["Ocean", "Feature"], [
            ["Pacific Ocean", "The largest and deepest ocean basin"],
        ]),
    },
    "general-knowledge-c1-l53": {
        "data_table": table(["Treaty", "Significance"], [
            ["Treaty of Versailles", "Formally ended World War I"],
        ]),
    },
    "general-knowledge-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Exchange rate", "The value of one currency relative to another"],
        ]),
    },
    "general-knowledge-c1-l55": {
        "data_table": table(["Route", "Significance"], [
            ["Silk Road", "Connected East Asia to the Mediterranean for centuries"],
        ]),
    },
    "general-knowledge-c1-l56": {
        "data_table": table(["Source", "Feature"], [
            ["Solar power", "Rapidly growing, cost has fallen sharply"], ["Wind power", "Major renewable source in many regions"],
        ]),
    },
    "general-knowledge-c1-l57": {
        "data_table": table(["Landmark", "Country"], [
            ["The Great Wall", "China"], ["Machu Picchu", "Peru"],
        ]),
    },
    "general-knowledge-c1-l58": {
        "data_table": table(["Pattern", "Detail"], [
            ["Coastal concentration", "Most of the world's population lives near coastlines"],
        ]),
    },
    "general-knowledge-c1-l59": {
        "data_table": table(["Calendar", "Basis"], [
            ["Gregorian calendar", "Solar-based, used internationally today"], ["Lunar calendar", "Based on the phases of the moon"],
        ]),
    },
    "general-knowledge-c1-l60": {
        "data_table": table(["Category", "Example"], [
            ["Sports", "Championship winners and records"], ["Pop culture", "Films, music, and celebrities"],
        ]),
    },
    "general-knowledge-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a news claim", "Cross-checking it against a second reliable source"],
        ]),
    },
    "general-knowledge-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Tracing institutional roles", "Explaining how the IMF differs from the World Bank"],
        ]),
    },
    "general-knowledge-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Connecting ideas across eras", "Linking Enlightenment thought to modern democracy"],
        ]),
    },
    "general-knowledge-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Comparing belief systems", "Contrasting core practices of two major religions"],
        ]),
    },
    "general-knowledge-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing an economic system", "Identifying market versus planned economy features"],
        ]),
    },
    "general-knowledge-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Sequencing innovations", "Ordering major technological milestones chronologically"],
        ]),
    },
    "general-knowledge-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Synthesizing geography facts", "Connecting climate zones to population patterns"],
        ]),
    },
    "general-knowledge-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Applying cultural literacy", "Recognizing a common cultural reference in context"],
        ]),
    },
    "general-knowledge-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Solving a logic puzzle", "Applying elimination to a constraint-based riddle"],
        ]),
    },
    "general-knowledge-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Explaining a scientific concept simply", "Describing photosynthesis in plain language"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 General Knowledge lessons (completing 70/70).")


if __name__ == "__main__":
    main()
