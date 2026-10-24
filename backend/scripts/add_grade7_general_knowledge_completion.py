#!/usr/bin/env python3
"""Depth pass, Grade 7 General Knowledge: fill in real, hand-checked
data_table content for the 38 Grade 7 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings Grade 7 General
Knowledge to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "gk-g7-l1": {
        "data_table": table(["Inventor", "Invention"], [
            ["Thomas Edison", "Practical light bulb"], ["Johannes Gutenberg", "Printing press"],
        ]),
    },
    "general-knowledge-g7-l2": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["Bangladesh", "Dhaka"],
        ]),
    },
    "general-knowledge-g7-l3": {
        "data_table": table(["Wonder", "Location"], [
            ["Great Pyramid of Giza", "Egypt"], ["Hanging Gardens of Babylon", "Mesopotamia (traditionally)"],
        ]),
    },
    "general-knowledge-g7-l5": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "Dollar"], ["Japan", "Yen"], ["European Union", "Euro"],
        ]),
    },
    "general-knowledge-g7-l6": {
        "data_table": table(["Religion", "Approx. Founded"], [
            ["Hinduism", "Ancient, over 4,000 years ago"], ["Buddhism", "c. 5th century BCE"],
            ["Christianity", "1st century CE"], ["Islam", "7th century CE"],
        ]),
    },
    "general-knowledge-g7-l7": {
        "data_table": table(["Explorer", "Known For"], [
            ["Marco Polo", "Travels along the Silk Road"], ["Ibn Battuta", "Extensive travels across Africa and Asia"],
        ]),
    },
    "general-knowledge-g7-l8": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "general-knowledge-g7-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["First modern Olympics", "1896, Athens"], ["Olympic values", "Excellence, friendship, respect"],
        ]),
    },
    "general-knowledge-g7-l10": {
        "data_table": table(["Sport", "Origin"], [
            ["Football (soccer)", "England (modern rules)"], ["Basketball", "United States, invented by James Naismith"],
        ]),
    },
    "general-knowledge-g7-l11": {
        "data_table": table(["Record", "Fact"], [
            ["Tallest mountain", "Mount Everest, 8,849 m"], ["Longest river", "The Nile (or Amazon, by some measures)"],
        ]),
    },
    "general-knowledge-g7-l13": {
        "data_table": table(["Organization", "Purpose"], [
            ["WHO", "Coordinates global public health"],
        ]),
    },
    "general-knowledge-g7-l14": {
        "data_table": table(["Issue", "Example"], [
            ["Climate change", "Rising global temperatures"], ["Deforestation", "Loss of forest habitats"],
        ]),
    },
    "general-knowledge-g7-l15": {
        "data_table": table(["Technology Trend", "Example"], [
            ["Artificial intelligence", "Voice assistants, recommendation systems"],
        ]),
    },
    "general-knowledge-g7-l16": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Vincent van Gogh", "The Starry Night"],
        ]),
    },
    "general-knowledge-g7-l17": {
        "data_table": table(["Composer", "Known For"], [
            ["Wolfgang Amadeus Mozart", "Classical era symphonies and operas"],
        ]),
    },
    "general-knowledge-g7-l18": {
        "data_table": table(["Language", "Spoken Mainly In"], [
            ["Mandarin", "China"], ["Spanish", "Spain, Latin America"],
        ]),
    },
    "general-knowledge-g7-l19": {
        "data_table": table(["Festival", "Region"], [
            ["Diwali", "India and Hindu communities worldwide"], ["Eid al-Fitr", "Muslim communities worldwide"],
        ]),
    },
    "general-knowledge-g7-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Global economy", "The interconnected economic activity of countries worldwide"],
        ]),
    },
    "general-knowledge-g7-l21": {
        "data_table": table(["Scientist", "Discovery"], [
            ["Isaac Newton", "Laws of motion and gravity"], ["Marie Curie", "Research on radioactivity"],
        ]),
    },
    "general-knowledge-g7-l22": {
        "data_table": table(["Animal", "Fact"], [
            ["Blue whale", "Largest animal on Earth"], ["Cheetah", "Fastest land animal"],
        ]),
    },
    "general-knowledge-g7-l23": {
        "data_table": table(["Ocean", "Fact"], [
            ["Pacific Ocean", "Largest and deepest ocean"], ["Atlantic Ocean", "Second largest ocean"],
        ]),
    },
    "general-knowledge-g7-l24": {
        "data_table": table(["River", "Approx. Length"], [
            ["Nile", "About 6,650 km"], ["Amazon", "About 6,400 km"],
        ]),
    },
    "general-knowledge-g7-l25": {
        "data_table": table(["Mountain", "Height"], [
            ["Mount Everest", "8,849 m"], ["K2", "8,611 m"],
        ]),
    },
    "general-knowledge-g7-l26": {
        "data_table": table(["Bridge", "Location"], [
            ["Golden Gate Bridge", "San Francisco, USA"], ["Akashi Kaikyo Bridge", "Japan"],
        ]),
    },
    "general-knowledge-g7-l27": {
        "data_table": table(["Milestone", "Year"], [
            ["ARPANET (early internet)", "1969"], ["World Wide Web invented", "1989-1991"],
        ]),
    },
    "general-knowledge-g7-l28": {
        "data_table": table(["Cuisine", "Signature Dish"], [
            ["Italian", "Pasta"], ["Mexican", "Tacos"], ["Indian", "Curry"],
        ]),
    },
    "general-knowledge-g7-l29": {
        "data_table": table(["Calendar", "Basis"], [
            ["Gregorian calendar", "Solar year, used internationally"], ["Islamic (Hijri) calendar", "Lunar cycles"],
        ]),
    },
    "general-knowledge-g7-l30": {
        "data_table": table(["System", "Used Mainly In"], [
            ["Metric system", "Most of the world"], ["Imperial system", "United States"],
        ]),
    },
    "general-knowledge-g7-l31": {
        "data_table": table(["Invention", "Impact"], [
            ["The airplane", "Made long-distance travel fast"], ["The automobile", "Transformed personal transport"],
        ]),
    },
    "general-knowledge-g7-l32": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["National anthem", "A patriotic song"],
        ]),
    },
    "general-knowledge-g7-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"],
        ]),
    },
    "general-knowledge-g7-l34": {
        "data_table": table(["Author", "Famous Work"], [
            ["Charles Dickens", "Oliver Twist"], ["Jane Austen", "Pride and Prejudice"],
        ]),
    },
    "general-knowledge-g7-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"], ["Fact-checking", "Verifying claims before trusting them"],
        ]),
    },
    "general-knowledge-g7-l36": {
        "data_table": table(["Holiday", "Origin"], [
            ["Thanksgiving (US)", "Rooted in early harvest celebrations"],
        ]),
    },
    "general-knowledge-g7-l37": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Burj Khalifa", "United Arab Emirates"],
        ]),
    },
    "general-knowledge-g7-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Barter", "Trading goods directly without money"], ["Coinage", "Metal money first used in ancient times"],
        ]),
    },
    "general-knowledge-g7-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Standard time zones worldwide", "24"],
        ]),
    },
    "general-knowledge-g7-l40": {
        "data_table": table(["Woman", "Known For"], [
            ["Marie Curie", "Pioneering research on radioactivity"], ["Rosa Parks", "Sparked the Montgomery bus boycott"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 General Knowledge lessons (completing 40/40).")


if __name__ == "__main__":
    main()
