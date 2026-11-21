#!/usr/bin/env python3
"""Depth pass, Grade 10 General Knowledge: fill in real, hand-checked
data_table content for the Grade 10 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 10 General
Knowledge to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Global citizenship", "Seeing oneself as part of a worldwide community with shared responsibilities"],
        ]),
    },
    "general-knowledge-g10-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Largest continent", "Asia"], ["Largest ocean", "Pacific Ocean"],
        ]),
    },
    "general-knowledge-g10-l3": {
        "data_table": table(["River", "Continent"], [
            ["Nile", "Africa, generally considered the longest river"], ["Amazon", "South America, largest by discharge"],
        ]),
    },
    "general-knowledge-g10-l4": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia, includes Mount Everest"], ["Andes", "South America"],
        ]),
    },
    "general-knowledge-g10-l5": {
        "data_table": table(["Country", "Capital"], [
            ["Japan", "Tokyo"], ["France", "Paris"],
        ]),
    },
    "general-knowledge-g10-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["United Nations founded", "1945"], ["Purpose", "Maintain international peace and cooperation"],
        ]),
    },
    "general-knowledge-g10-l7": {
        "data_table": table(["Organization", "Role"], [
            ["WHO", "Coordinates global public health"], ["UNESCO", "Promotes education, science, and culture"], ["UNICEF", "Supports children's welfare worldwide"],
        ]),
    },
    "general-knowledge-g10-l8": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "US Dollar"], ["Japan", "Yen"],
        ]),
    },
    "general-knowledge-g10-l9": {
        "data_table": table(["Inventor", "Invention"], [
            ["Johannes Gutenberg", "Printing press"], ["Alexander Graham Bell", "Telephone"],
        ]),
    },
    "general-knowledge-g10-l11": {
        "data_table": table(["Religion", "Approx. Followers"], [
            ["Christianity", "Largest by number of adherents"], ["Islam", "Second-largest by number of adherents"],
        ]),
    },
    "general-knowledge-g10-l12": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Pyramid of Giza", "Egypt, only surviving ancient wonder"],
        ]),
    },
    "general-knowledge-g10-l13": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Wall of China", "China"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g10-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Modern Olympics began", "1896, Athens"],
        ]),
    },
    "general-knowledge-g10-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["FIFA World Cup", "Held every 4 years since 1930"],
        ]),
    },
    "general-knowledge-g10-l16": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing", "1969"],
        ]),
    },
    "general-knowledge-g10-l17": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Marie Curie", "Radioactivity"], ["Charles Darwin", "Theory of evolution"],
        ]),
    },
    "general-knowledge-g10-l18": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Flag colors", "Often represent history, land, or values of a nation"],
        ]),
    },
    "general-knowledge-g10-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["International Date Line", "Roughly follows the 180th meridian"],
        ]),
    },
    "general-knowledge-g10-l21": {
        "data_table": table(["Language", "Approx. Native Speakers"], [
            ["Mandarin Chinese", "Most native speakers worldwide"], ["Spanish", "Second-most native speakers"],
        ]),
    },
    "general-knowledge-g10-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["World population", "Passed 8 billion in 2022"],
        ]),
    },
    "general-knowledge-g10-l23": {
        "data_table": table(["Climate Zone", "Feature"], [
            ["Tropical", "Warm year-round, high rainfall"], ["Polar", "Cold year-round"],
        ]),
    },
    "general-knowledge-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Endangered species", "A species at risk of extinction"],
        ]),
    },
    "general-knowledge-g10-l25": {
        "data_table": table(["Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Non-renewable", "Coal, oil"],
        ]),
    },
    "general-knowledge-g10-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain", "The network moving goods from producer to consumer"],
        ]),
    },
    "general-knowledge-g10-l27": {
        "data_table": table(["Skill", "Purpose"], [
            ["Checking sources", "Reduces spread of misinformation"],
        ]),
    },
    "general-knowledge-g10-l28": {
        "data_table": table(["Explorer", "Known For"], [
            ["Ferdinand Magellan", "First expedition to circumnavigate the globe"],
        ]),
    },
    "general-knowledge-g10-l29": {
        "data_table": table(["Treaty", "Impact"], [
            ["Treaty of Versailles", "Ended WWI, reshaped Europe"],
        ]),
    },
    "general-knowledge-g10-l30": {
        "data_table": table(["Movement", "Region"], [
            ["Impressionism", "France, late 19th century"],
        ]),
    },
    "general-knowledge-g10-l31": {
        "data_table": table(["Author", "Famous Work"], [
            ["William Shakespeare", "Hamlet"],
        ]),
    },
    "general-knowledge-g10-l32": {
        "data_table": table(["Award", "Recognizes"], [
            ["Academy Award (Oscar)", "Excellence in film"],
        ]),
    },
    "general-knowledge-g10-l33": {
        "data_table": table(["Dish", "Origin"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"],
        ]),
    },
    "general-knowledge-g10-l34": {
        "data_table": table(["Festival", "Region"], [
            ["Diwali", "India, festival of lights"],
        ]),
    },
    "general-knowledge-g10-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Currency exchange", "Converting one country's money into another's"],
        ]),
    },
    "general-knowledge-g10-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Sustainable Development Goals", "17 goals adopted by the UN in 2015"],
        ]),
    },
    "general-knowledge-g10-l37": {
        "data_table": table(["Body", "Sport"], [
            ["FIFA", "Football/soccer"], ["IOC", "Olympic Games"],
        ]),
    },
    "general-knowledge-g10-l38": {
        "data_table": table(["Agency", "Country"], [
            ["NASA", "United States"], ["ESA", "Europe"],
        ]),
    },
    "general-knowledge-g10-l39": {
        "data_table": table(["Leader", "Known For"], [
            ["Nelson Mandela", "Ending apartheid in South Africa"],
        ]),
    },
    "general-knowledge-g10-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["UNESCO World Heritage Sites", "Recognized for outstanding cultural or natural value"],
        ]),
    },
    "general-knowledge-g10-l41": {
        "data_table": table(["Organization", "Role"], [
            ["World Health Organization", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g10-l42": {
        "data_table": table(["Bridge", "Location"], [
            ["Golden Gate Bridge", "San Francisco, USA"],
        ]),
    },
    "general-knowledge-g10-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["World records", "Recognized measurable achievements, e.g. by Guinness World Records"],
        ]),
    },
    "general-knowledge-g10-l44": {
        "data_table": table(["Milestone", "Detail"], [
            ["World Wide Web launched", "1991, by Tim Berners-Lee"],
        ]),
    },
    "general-knowledge-g10-l45": {
        "data_table": table(["Award", "Recognizes"], [
            ["Pulitzer Prize", "Journalism and letters"], ["Grammy Award", "Music"],
        ]),
    },
    "general-knowledge-g10-l46": {
        "data_table": table(["Outlet", "Country"], [
            ["The New York Times", "United States"], ["BBC", "United Kingdom"],
        ]),
    },
    "general-knowledge-g10-l47": {
        "data_table": table(["System", "Example"], [
            ["Parliamentary", "United Kingdom"], ["Presidential", "United States"],
        ]),
    },
    "general-knowledge-g10-l48": {
        "data_table": table(["Agreement", "Purpose"], [
            ["Paris Agreement", "Global commitment to limit climate change, 2015"],
        ]),
    },
    "general-knowledge-g10-l49": {
        "data_table": table(["Country", "Notable Population Fact"], [
            ["China and India", "Together account for over a third of the global population"],
        ]),
    },
    "general-knowledge-g10-l50": {
        "data_table": table(["Skill", "Purpose"], [
            ["Cross-referencing sources", "Improves accuracy when analysing the news"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 General Knowledge lessons (completing 50/50).")


if __name__ == "__main__":
    main()
