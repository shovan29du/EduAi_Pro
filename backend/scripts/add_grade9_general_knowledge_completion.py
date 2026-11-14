#!/usr/bin/env python3
"""Depth pass, Grade 9 General Knowledge: fill in real, hand-checked
data_table content for the 48 Grade 9 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 9 General
Knowledge to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet of Things", "Everyday devices connected to the internet"],
        ]),
    },
    "general-knowledge-g9-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Largest continent", "Asia"], ["Largest ocean", "Pacific Ocean"],
        ]),
    },
    "general-knowledge-g9-l3": {
        "data_table": table(["Continent/Ocean", "Fact"], [
            ["Africa", "Second-largest continent"], ["Atlantic Ocean", "Second-largest ocean"],
        ]),
    },
    "general-knowledge-g9-l5": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia, includes Mount Everest"], ["Andes", "South America"],
        ]),
    },
    "general-knowledge-g9-l6": {
        "data_table": table(["Country", "Capital"], [
            ["Japan", "Tokyo"], ["France", "Paris"],
        ]),
    },
    "general-knowledge-g9-l7": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "US Dollar"], ["Japan", "Yen"],
        ]),
    },
    "general-knowledge-g9-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["United Nations founded", "1945"], ["Purpose", "Maintain international peace and cooperation"],
        ]),
    },
    "general-knowledge-g9-l9": {
        "data_table": table(["Religion", "Approx. Followers Worldwide"], [
            ["Christianity", "Largest by number of adherents"], ["Islam", "Second-largest by number of adherents"],
        ]),
    },
    "general-knowledge-g9-l10": {
        "data_table": table(["Language", "Approx. Native Speakers"], [
            ["Mandarin Chinese", "Most native speakers worldwide"], ["Spanish", "Second-most native speakers"],
        ]),
    },
    "general-knowledge-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["UTC", "Coordinated Universal Time, the global time reference"],
        ]),
    },
    "general-knowledge-g9-l12": {
        "data_table": table(["Explorer", "Known For"], [
            ["Ferdinand Magellan", "First expedition to circumnavigate the globe"],
        ]),
    },
    "general-knowledge-g9-l13": {
        "data_table": table(["Inventor", "Invention"], [
            ["Johannes Gutenberg", "Printing press"], ["Alexander Graham Bell", "Telephone"],
        ]),
    },
    "general-knowledge-g9-l14": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing", "1969"],
        ]),
    },
    "general-knowledge-g9-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Modern Olympics began", "1896, Athens"],
        ]),
    },
    "general-knowledge-g9-l17": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Pyramid of Giza", "Egypt, only surviving ancient wonder"],
        ]),
    },
    "general-knowledge-g9-l18": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Wall of China", "China"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g9-l19": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Statue of Liberty", "United States"],
        ]),
    },
    "general-knowledge-g9-l20": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Flag colors", "Often represent history, land, or values of a nation"],
        ]),
    },
    "general-knowledge-g9-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["National anthem", "A patriotic song officially adopted by a country"],
        ]),
    },
    "general-knowledge-g9-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["World population", "Passed 8 billion in 2022"],
        ]),
    },
    "general-knowledge-g9-l23": {
        "data_table": table(["Desert", "Location"], [
            ["Sahara", "Largest hot desert, North Africa"], ["Antarctic Desert", "Largest desert overall"],
        ]),
    },
    "general-knowledge-g9-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Volcano", "An opening where magma reaches the surface"], ["Earthquake", "Shaking caused by movement of tectonic plates"],
        ]),
    },
    "general-knowledge-g9-l25": {
        "data_table": table(["Climate Zone", "Feature"], [
            ["Tropical", "Warm year-round, high rainfall"], ["Polar", "Cold year-round"],
        ]),
    },
    "general-knowledge-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Endangered species", "A species at risk of extinction"],
        ]),
    },
    "general-knowledge-g9-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Import", "Goods brought into a country"], ["Export", "Goods sent out of a country"],
        ]),
    },
    "general-knowledge-g9-l28": {
        "data_table": table(["Day", "Observance"], [
            ["Earth Day", "April 22, environmental awareness"], ["World Health Day", "April 7"],
        ]),
    },
    "general-knowledge-g9-l29": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Marie Curie", "Radioactivity"], ["Charles Darwin", "Theory of evolution"],
        ]),
    },
    "general-knowledge-g9-l30": {
        "data_table": table(["Milestone", "Detail"], [
            ["Telegraph", "19th century long-distance messaging"],
        ]),
    },
    "general-knowledge-g9-l31": {
        "data_table": table(["Milestone", "Detail"], [
            ["Wright brothers' first flight", "1903"],
        ]),
    },
    "general-knowledge-g9-l32": {
        "data_table": table(["Civilization", "Region"], [
            ["Mesopotamia", "Modern-day Iraq"], ["Ancient Egypt", "Along the Nile"],
        ]),
    },
    "general-knowledge-g9-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["World War I dates", "1914-1918"],
        ]),
    },
    "general-knowledge-g9-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["World War II dates", "1939-1945"],
        ]),
    },
    "general-knowledge-g9-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Cold War period", "1947-1991"],
        ]),
    },
    "general-knowledge-g9-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted 1948"],
        ]),
    },
    "general-knowledge-g9-l37": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"],
        ]),
    },
    "general-knowledge-g9-l38": {
        "data_table": table(["Dance", "Region"], [
            ["Flamenco", "Spain"], ["Tango", "Argentina"],
        ]),
    },
    "general-knowledge-g9-l39": {
        "data_table": table(["Dish", "Origin"], [
            ["Sushi", "Japan"], ["Pizza", "Italy"],
        ]),
    },
    "general-knowledge-g9-l40": {
        "data_table": table(["Sport", "Popular Region"], [
            ["Football/Soccer", "Worldwide, especially Europe and South America"],
        ]),
    },
    "general-knowledge-g9-l41": {
        "data_table": table(["Festival", "Region"], [
            ["Diwali", "India, festival of lights"], ["Carnival", "Brazil"],
        ]),
    },
    "general-knowledge-g9-l42": {
        "data_table": table(["Agency", "Country"], [
            ["NASA", "United States"], ["ESA", "Europe"],
        ]),
    },
    "general-knowledge-g9-l43": {
        "data_table": table(["Planet", "Order from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"],
        ]),
    },
    "general-knowledge-g9-l44": {
        "data_table": table(["Natural Wonder", "Location"], [
            ["Grand Canyon", "United States"], ["Great Barrier Reef", "Australia"],
        ]),
    },
    "general-knowledge-g9-l45": {
        "data_table": table(["Issue", "Concern"], [
            ["Climate change", "Rising global temperatures"], ["Deforestation", "Loss of forest habitats"],
        ]),
    },
    "general-knowledge-g9-l46": {
        "data_table": table(["Author", "Famous Book"], [
            ["William Shakespeare", "Hamlet"],
        ]),
    },
    "general-knowledge-g9-l47": {
        "data_table": table(["Event", "Frequency"], [
            ["Olympic Games", "Every 4 years"], ["FIFA World Cup", "Every 4 years"],
        ]),
    },
    "general-knowledge-g9-l48": {
        "data_table": table(["Organization", "Role"], [
            ["World Health Organization", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g9-l49": {
        "data_table": table(["Skill", "Purpose"], [
            ["Checking sources", "Reduces spread of misinformation"],
        ]),
    },
    "general-knowledge-g9-l50": {
        "data_table": table(["Bridge", "Location"], [
            ["Golden Gate Bridge", "San Francisco, USA"], ["Akashi Kaikyo Bridge", "Japan"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 General Knowledge lessons (completing 50/50).")


if __name__ == "__main__":
    main()
