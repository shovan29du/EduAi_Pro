#!/usr/bin/env python3
"""Breadth-first pass, Grade 4: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade4.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real bone counts,
real historical dates, real Scratch stage coordinates, real Arabic number
words, real composer facts, etc.) -- nothing fabricated or presented as
fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g4-l19": {
        "data_table": table(["Type", "Example"], [
            ["Simile", "Brave as a lion"], ["Metaphor", "Time is money"],
        ]),
    },
    "english-g4-l8": {
        "data_table": table(["Word", "Synonym", "Antonym"], [
            ["Strong", "Powerful", "Weak"], ["Bright", "Shining", "Dim"],
        ]),
    },
    # ---- Science ----
    "sci-g4-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Circuit", "A closed loop path for electric current"],
            ["Conductor", "A material that allows electricity to flow (e.g. copper)"],
            ["Insulator", "A material that blocks electricity (e.g. rubber)"],
        ]),
    },
    "science-g4-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of bones in the adult human body", "206"],
            ["Longest bone", "Femur (thigh bone)"],
            ["Smallest bone", "Stapes (in the ear)"],
        ]),
    },
    # ---- Geography ----
    "geography-g4-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Latitude", "Lines running east-west, measuring distance north/south of the Equator"],
            ["Longitude", "Lines running north-south, measuring distance east/west of the Prime Meridian"],
            ["Equator", "0 degrees latitude"],
        ]),
    },
    "geography-g4-l9": {
        "data_table": table(["Desert", "Location", "Type"], [
            ["Sahara", "North Africa", "Hot desert (largest hot desert)"],
            ["Gobi", "Asia (Mongolia/China)", "Cold desert"],
            ["Antarctic Desert", "Antarctica", "Coldest and largest desert overall"],
        ]),
    },
    # ---- World History ----
    "hist-g4-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Approximate period", "8th-14th century CE"],
            ["Center of learning", "House of Wisdom, Baghdad"],
            ["Notable scholars", "Ibn al-Haytham (optics), Al-Khwarizmi (algebra)"],
        ]),
    },
    "world-history-g4-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Roman Empire declared by", "Augustus, 27 BCE"],
            ["Fall of the Western Roman Empire", "476 CE"],
            ["Famous structure", "The Colosseum, completed 80 CE"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g4-l14": {
        "data_table": table(["Islamic Month", "Significance"], [
            ["Muharram", "1st month; includes the Day of Ashura"],
            ["Ramadan", "9th month; month of fasting"],
            ["Dhul Hijjah", "12th month; month of Hajj"],
        ]),
    },
    "islamic-studies-g4-l20": {
        "data_table": table(["Scholar", "Contribution"], [
            ["Ibn Sina (Avicenna)", "The Canon of Medicine"],
            ["Al-Khwarizmi", "Founder of algebra"],
            ["Ibn al-Haytham", "Pioneering work in optics"],
        ]),
    },
    # ---- Coding ----
    "coding-g4-l4": {
        "data_table": table(["Variable", "Value Change"], [
            ["score", "0 -> 10 after +10"], ["health", "100 -> 90 after -10"],
        ]),
    },
    "coding-g4-l11": {
        "data_table": table(["Position on Scratch Stage", "Coordinate (x, y)"], [
            ["Center", "(0, 0)"], ["Right edge", "(240, 0)"], ["Top edge", "(0, 180)"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g4-l13": {
        "data_table": table(["Greek God/Goddess", "Domain"], [
            ["Zeus", "King of the gods, sky and thunder"],
            ["Athena", "Wisdom and strategy"], ["Poseidon", "The sea"],
        ]),
    },
    "world-literature-g4-l14": {
        "data_table": table(["Norse God", "Domain"], [
            ["Odin", "Wisdom and war, ruler of Asgard"],
            ["Thor", "Thunder and strength"], ["Loki", "Trickery and mischief"],
        ]),
    },
    # ---- Art ----
    "art-g4-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Famous painting", "The Starry Night (1889)"],
            ["Art movement", "Post-Impressionism"], ["Nationality", "Dutch"],
        ]),
    },
    "art-g4-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Art movement co-founded", "Cubism"],
            ["Famous painting", "Guernica (1937)"], ["Nationality", "Spanish"],
        ]),
    },
    # ---- Music ----
    "music-g4-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Full name", "Wolfgang Amadeus Mozart"],
            ["Born", "1756, Salzburg"], ["Famous work", "The Magic Flute"],
        ]),
    },
    "music-g4-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Born", "1770, Bonn"], ["Famous work", "Symphony No. 9"],
            ["Notable challenge", "Composed while losing his hearing"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g4-l2": {
        "data_table": table(["Compass Direction", "Bearing"], [
            ["North", "0 degrees / 360 degrees"], ["East", "90 degrees"],
            ["South", "180 degrees"], ["West", "270 degrees"],
        ]),
    },
    "survival-skills-g4-l15": {
        "data_table": table(["Item", "Purpose"], [
            ["Water", "Hydration (FEMA recommends 1 gallon per person per day)"],
            ["Flashlight", "Light during a power outage"],
            ["First aid kit", "Treating minor injuries"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g4-l4": {
        "data_table": table(["Ancient Wonder", "Location"], [
            ["Great Pyramid of Giza", "Egypt (only one still standing)"],
            ["Hanging Gardens of Babylon", "Mesopotamia (modern Iraq)"],
            ["Colossus of Rhodes", "Rhodes, Greece"],
            ["Lighthouse of Alexandria", "Egypt"],
        ]),
    },
    "general-knowledge-g4-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["First modern Olympics", "1896, Athens, Greece"],
            ["First ancient Olympics", "776 BCE, Olympia, Greece"],
            ["Olympic rings represent", "Five inhabited continents"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g4-l13": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"], ["2 cups", "1 pint"],
        ]),
    },
    "cooking-g4-l20": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g4-l3": {
        "data_table": table(["Number", "French"], [
            ["1", "un"], ["2", "deux"], ["3", "trois"], ["4", "quatre"], ["5", "cinq"],
            ["6", "six"], ["7", "sept"], ["8", "huit"], ["9", "neuf"], ["10", "dix"],
        ]),
    },
    "foreign-languages-g4-l12": {
        "data_table": table(["Number", "Arabic (transliteration)"], [
            ["1", "wahid"], ["2", "ithnan"], ["3", "thalatha"], ["4", "arba'a"], ["5", "khamsa"],
            ["6", "sitta"], ["7", "sab'a"], ["8", "thamaniya"], ["9", "tis'a"], ["10", "'ashara"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g4-l8": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price tends to rise"],
            ["Low demand, high supply", "Price tends to fall"],
        ]),
    },
    "social-studies-g4-l4": {
        "data_table": table(["Government Level", "Example Responsibility"], [
            ["Local", "Schools, trash collection, parks"],
            ["State / Provincial", "State highways, state parks"],
            ["National", "Defense, currency, foreign policy"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g4-l6": {
        "data_table": table(["Basketball Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"],
            ["Passing", "Moving the ball to a teammate"],
            ["Shooting", "Aiming the ball at the basket"],
        ]),
    },
    "physical-education-self-defense-g4-l7": {
        "data_table": table(["Soccer Skill", "Description"], [
            ["Dribbling", "Moving the ball with your feet"],
            ["Passing", "Kicking the ball to a teammate"],
            ["Shooting", "Kicking the ball toward the goal"],
        ]),
    },
    # ---- Health Education ----
    "hlt-g4-l1": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    "health-education-g4-l9": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g4-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["LAN", "Local Area Network - connects devices in one building"],
            ["WAN", "Wide Area Network - connects devices over a large area"],
            ["Router", "Directs data between networks"],
        ]),
    },
    "ict-g4-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"],
            ["Row / Record", "A single entry in a database"],
            ["Column / Field", "A category of data (e.g. Name, Age)"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    by_id: dict[str, dict] = {}
    for subject in data["subjects"].values():
        for lesson in subject.get("lessons", []):
            by_id[lesson["id"]] = lesson

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 4 lessons (all subjects).")


if __name__ == "__main__":
    main()
