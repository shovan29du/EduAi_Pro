#!/usr/bin/env python3
"""Breadth-first pass, Grade 5 (non-Math): add genuine, hand-checked
data_table content to a representative batch of lessons across every
non-Math subject in grade5.json. Grade 5 Math already has full pilot
coverage via add_grade5_math_lesson_charts.py -- this fills the gap for
every OTHER subject at this grade level.

Every fact here is real and independently verifiable (real river lengths,
real mountain heights, real historical dates, real number words in other
languages, CDC water-purification guidance, etc.) -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g5-l6": {
        "data_table": table(["Root", "Meaning", "Example Word"], [
            ["bio", "life", "biology"], ["photo", "light", "photograph"], ["graph", "write / draw", "autograph"],
        ]),
    },
    "english-g5-l7": {
        "data_table": table(["Idiom", "Meaning"], [
            ["Break the ice", "Start a conversation in an awkward situation"],
            ["Piece of cake", "Something very easy"],
            ["Under the weather", "Feeling sick"],
        ]),
    },
    # ---- Science ----
    "science-g5-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Organ that pumps blood", "The heart"],
            ["Average adult resting heart rate", "60-100 beats per minute"],
            ["Number of heart chambers", "4"],
        ]),
    },
    "science-g5-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Tectonic plate", "A large slab of Earth's crust that moves slowly"],
            ["Fault", "A crack where plates meet and can slip"],
            ["Magnitude scale", "Measures the energy/strength of an earthquake"],
        ]),
    },
    # ---- Geography ----
    "geography-g5-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of standard time zones worldwide", "24 (roughly one per 15 degrees of longitude)"],
            ["International Date Line location", "Roughly the 180 degree meridian, Pacific Ocean"],
        ]),
    },
    "geography-g5-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Population density", "Number of people per unit of land area (e.g. per km2)"],
            ["Sparse population", "Few people per unit area (e.g. deserts, polar regions)"],
            ["Dense population", "Many people per unit area (e.g. major cities)"],
        ]),
    },
    # ---- World History ----
    "world-history-g5-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Inventor", "Johannes Gutenberg"],
            ["Approximate date", "c. 1440 CE"],
            ["Famous printed work", "The Gutenberg Bible, c. 1455"],
        ]),
    },
    "world-history-g5-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Started by", "Martin Luther"],
            ["Key event", "Posting the 95 Theses, 1517"],
            ["Location", "Wittenberg, Germany"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g5-l2": {
        "data_table": table(["Article of Faith", "Belief In"], [
            ["1", "Allah (God)"], ["2", "Angels"], ["3", "Revealed Books"],
            ["4", "Prophets"], ["5", "The Day of Judgment"], ["6", "Divine Decree (Qadar)"],
        ]),
    },
    "islamic-studies-g5-l19": {
        "data_table": table(["Islamic Month", "Significance"], [
            ["Muharram", "1st month; includes the Day of Ashura"],
            ["Ramadan", "9th month; month of fasting"],
            ["Dhul Hijjah", "12th month; month of Hajj"],
        ]),
    },
    # ---- Coding ----
    "coding-g5-l10": {
        "data_table": table(["Key", "Value"], [
            ["'name'", "'Alice'"], ["'age'", "10"], ["'grade'", "5"],
        ]),
    },
    "coding-g5-l18": {
        "data_table": table(["Function", "Example Output Range"], [
            ["random.randint(1, 6)", "1 to 6 (like a dice roll)"], ["random.random()", "0.0 to 1.0"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g5-l15": {
        "data_table": table(["Shakespeare Play", "Genre"], [
            ["Romeo and Juliet", "Tragedy"], ["A Midsummer Night's Dream", "Comedy"], ["Hamlet", "Tragedy"],
        ]),
    },
    "world-literature-g5-l20": {
        "data_table": table(["Poetry Form", "Syllable Structure"], [
            ["Haiku", "5-7-5 (3 lines)"], ["Tanka", "5-7-5-7-7 (5 lines)"],
        ]),
    },
    # ---- Art ----
    "art-g5-l3": {
        "data_table": table(["Colour Relationship", "Example"], [
            ["Complementary (opposite on the wheel)", "Red & Green, Blue & Orange"],
            ["Analogous (next to each other)", "Blue, Blue-Green, Green"],
        ]),
    },
    "art-g5-l16": {
        "data_table": table(["Renaissance Artist", "Famous Work"], [
            ["Leonardo da Vinci", "The Mona Lisa"],
            ["Michelangelo", "The Sistine Chapel ceiling"],
            ["Raphael", "The School of Athens"],
        ]),
    },
    # ---- Music ----
    "music-g5-l4": {
        "data_table": table(["Time Signature", "Meaning"], [
            ["4/4", "4 beats per measure, quarter note = 1 beat"],
            ["3/4", "3 beats per measure (waltz time)"],
            ["6/8", "6 beats per measure, eighth note = 1 beat"],
        ]),
    },
    "music-g5-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "New Orleans, USA, late 19th / early 20th century"],
            ["Key feature", "Improvisation"],
            ["Famous musician", "Louis Armstrong"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g5-l3": {
        "data_table": table(["Compass Direction", "Bearing"], [
            ["North", "0 degrees / 360 degrees"], ["East", "90 degrees"],
            ["South", "180 degrees"], ["West", "270 degrees"],
        ]),
    },
    "survival-skills-g5-l12": {
        "data_table": table(["Method", "How It Works"], [
            ["Boiling", "Boil for at least 1 minute (3 minutes above 2,000m) to kill pathogens"],
            ["Water filter", "Physically removes bacteria and parasites"],
            ["Purification tablets", "Chemically disinfect water"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g5-l4": {
        "data_table": table(["River", "Approx. Length", "Location"], [
            ["Nile", "~6,650 km", "Africa"], ["Amazon", "~6,400 km", "South America"],
            ["Yangtze", "~6,300 km", "China"],
        ]),
    },
    "general-knowledge-g5-l5": {
        "data_table": table(["Peak", "Height", "Location"], [
            ["Mount Everest", "8,849 m", "Nepal/China"], ["K2", "8,611 m", "Pakistan/China"],
            ["Kangchenjunga", "8,586 m", "Nepal/India"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g5-l12": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooking in water at 100C (212F)"],
            ["Steaming", "Cooking with hot vapor above boiling water"],
            ["Sauteing", "Cooking quickly in a small amount of fat over high heat"],
        ]),
    },
    "cooking-g5-l4": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"], ["2 cups", "1 pint"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g5-l9": {
        "data_table": table(["Number", "Mandarin (Pinyin)"], [
            ["1", "yi"], ["2", "er"], ["3", "san"], ["4", "si"], ["5", "wu"],
            ["6", "liu"], ["7", "qi"], ["8", "ba"], ["9", "jiu"], ["10", "shi"],
        ]),
    },
    "foreign-languages-g5-l20": {
        "data_table": table(["Number", "Hindi (transliteration)"], [
            ["1", "ek"], ["2", "do"], ["3", "teen"], ["4", "chaar"], ["5", "paanch"],
            ["6", "chhah"], ["7", "saat"], ["8", "aath"], ["9", "nau"], ["10", "das"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g5-l2": {
        "data_table": table(["Branch of Government", "Main Role"], [
            ["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "social-studies-g5-l12": {
        "data_table": table(["Tax Type", "Example"], [
            ["Income tax", "Tax on money earned from work"],
            ["Sales tax", "Tax added to purchases"],
            ["Property tax", "Tax on land/buildings owned"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g5-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Average resting heart rate (adult)", "60-100 beats per minute"],
            ["Max heart rate estimate", "220 minus your age (a common formula)"],
        ]),
    },
    "physical-education-self-defense-g5-l9": {
        "data_table": table(["Volleyball Skill", "Description"], [
            ["Serve", "Hitting the ball to start a rally"],
            ["Bump / Pass", "Using forearms to control the ball"],
            ["Set", "Using fingertips to position the ball for an attack"],
        ]),
    },
    # ---- Health Education ----
    "hlt-g5-l2": {
        "data_table": table(["Body System", "Main Function"], [
            ["Circulatory", "Pumps blood through the body"],
            ["Respiratory", "Brings oxygen in, removes carbon dioxide"],
            ["Digestive", "Breaks down food for energy"],
            ["Skeletal", "Supports and protects the body"],
        ]),
    },
    "health-education-g5-l20": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g5-l18": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"], ["5", "101"],
        ]),
    },
    "ict-g5-l1": {
        "data_table": table(["Python Concept", "Example"], [
            ["Print statement", "print('Hello, world!')"],
            ["Variable assignment", "x = 5"],
            ["Comment", "# this is a comment"],
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
        raise SystemExit(f"Lesson ids not found in grade5.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 5 lessons (non-Math subjects).")


if __name__ == "__main__":
    main()
