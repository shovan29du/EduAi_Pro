#!/usr/bin/env python3
"""Breadth-first pass, Grade 7: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade7.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real periodic table
entries, real pH facts, real WWII/Cold War dates, the real New Seven
Wonders list, the standard 30:2 CPR ratio, real hiragana characters, etc.)
-- nothing fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g7-l10": {
        "data_table": table(["Type", "Example"], [
            ["Simile", "Brave as a lion"], ["Metaphor", "Time is money"],
        ]),
    },
    "english-g7-l8": {
        "data_table": table(["Affix", "Meaning", "Example"], [
            ["un-", "not", "unhappy"], ["-ful", "full of", "joyful"], ["re-", "again", "rewrite"],
        ]),
    },
    # ---- Science ----
    "science-g7-l16": {
        "data_table": table(["Element", "Symbol", "Atomic Number"], [
            ["Hydrogen", "H", "1"], ["Carbon", "C", "6"], ["Oxygen", "O", "8"], ["Iron", "Fe", "26"],
        ]),
    },
    "science-g7-l18": {
        "data_table": table(["pH Range", "Type", "Example"], [
            ["0-6", "Acidic", "Lemon juice (~2)"], ["7", "Neutral", "Pure water"],
            ["8-14", "Basic (alkaline)", "Baking soda (~9)"],
        ]),
    },
    # ---- Geography ----
    "geography-g7-l11": {
        "data_table": table(["Biome", "Average Annual Rainfall", "Example Location"], [
            ["Tropical Rainforest", "Over 2,000mm", "Amazon Basin"],
            ["Desert", "Under 250mm", "Sahara"],
            ["Tundra", "Under 250mm (very cold)", "Arctic regions"],
        ]),
    },
    "geo-g7-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["HDI (Human Development Index)", "Combines life expectancy, education, and income into one score"],
            ["Score range", "0 (lowest) to 1 (highest)"],
        ]),
    },
    # ---- World History ----
    "hist-g7-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1939-1945"],
            ["Started when", "Germany invaded Poland, September 1939"],
            ["Ended in Europe", "V-E Day, May 8, 1945"],
        ]),
    },
    "hist-g7-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Approximate period", "1947-1991"],
            ["Main powers", "United States and Soviet Union"],
            ["Ended with", "Collapse of the Soviet Union, 1991"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g7-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Compiled into a single text under", "Caliph Abu Bakr; standardized under Caliph Uthman"],
            ["Number of chapters (Surahs)", "114"],
        ]),
    },
    "islamic-studies-g7-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Muslim rule in Spain (Al-Andalus)", "711-1492 CE"],
            ["Notable center of learning", "Cordoba"],
            ["Famous structure", "The Alhambra, Granada"],
        ]),
    },
    # ---- Coding ----
    "coding-g7-l16": {
        "data_table": table(["Algorithm", "Time Complexity", "Requirement"], [
            ["Linear Search", "O(n)", "None (works on unsorted data)"],
            ["Binary Search", "O(log n)", "Data must be sorted"],
        ]),
    },
    "coding-g7-l20": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Code that might raise an error"],
            ["except", "Code that runs if an error occurs"],
            ["finally", "Code that always runs"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g7-l6": {
        "data_table": table(["Epic", "Origin", "Approx. Date"], [
            ["Epic of Gilgamesh", "Mesopotamia", "c. 2100 BCE (oldest known epic)"],
            ["The Iliad", "Ancient Greece", "c. 8th century BCE"],
        ]),
    },
    "world-literature-g7-l15": {
        "data_table": table(["Poetry Form", "Structure"], [
            ["Haiku", "5-7-5 syllables, 3 lines"], ["Sonnet", "14 lines, often iambic pentameter"],
        ]),
    },
    # ---- Art ----
    "art-g7-l9": {
        "data_table": table(["Perspective Type", "Vanishing Points"], [
            ["One-point", "1"], ["Two-point", "2"],
        ]),
    },
    "art-g7-l7": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    # ---- Music ----
    "music-g7-l5": {
        "data_table": table(["Scale", "Pattern (W = whole step, H = half step)"], [
            ["Major", "W-W-H-W-W-W-H"], ["Natural Minor", "W-H-W-W-H-W-W"],
        ]),
    },
    "music-g7-l7": {
        "data_table": table(["Interval", "Semitones"], [
            ["Minor 2nd", "1"], ["Major 2nd", "2"], ["Perfect 4th", "5"],
            ["Perfect 5th", "7"], ["Octave", "12"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g7-l17": {
        "data_table": table(["CPR Step", "Action"], [
            ["1", "Check responsiveness and call for emergency help"],
            ["2", "Give 30 chest compressions (about 2 inches deep)"],
            ["3", "Give 2 rescue breaths (if trained)"],
            ["4", "Repeat the 30:2 ratio until help arrives"],
        ]),
    },
    "survival-skills-g7-l2": {
        "data_table": table(["Compass Direction", "Bearing"], [
            ["North", "0 degrees / 360 degrees"], ["East", "90 degrees"],
            ["South", "180 degrees"], ["West", "270 degrees"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g7-l4": {
        "data_table": table(["New Seven Wonder (2007 poll)", "Location"], [
            ["Great Wall of China", "China"], ["Petra", "Jordan"],
            ["Christ the Redeemer", "Brazil"], ["Machu Picchu", "Peru"],
            ["Chichen Itza", "Mexico"], ["Colosseum", "Italy"], ["Taj Mahal", "India"],
        ]),
    },
    "general-knowledge-g7-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded", "1945"], ["Headquarters", "New York City, USA"],
            ["Number of member states", "193 (as of the 2020s)"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g7-l13": {
        "data_table": table(["Herb/Spice", "Common Use"], [
            ["Basil", "Italian dishes, pesto"], ["Cumin", "Indian and Mexican dishes"],
            ["Cinnamon", "Baking, sweet dishes"],
        ]),
    },
    "cooking-g7-l9": {
        "data_table": table(["Method", "Description"], [
            ["Sauteing", "Cooking quickly in a small amount of fat over high heat"],
            ["Deep frying", "Fully submerging food in hot oil"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g7-l4": {
        "data_table": table(["Pronoun", "Hablar (\"to speak\")"], [
            ["yo", "hablo"], ["tu", "hablas"], ["el/ella", "habla"], ["nosotros", "hablamos"],
        ]),
    },
    "foreign-languages-g7-l18": {
        "data_table": table(["Hiragana", "Romaji"], [
            ["a", "a"], ["i", "i"], ["u", "u"], ["e", "e"], ["o", "o"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g7-l2": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Citizens elect representatives or vote directly"],
            ["Monarchy", "Rule by a king or queen"],
            ["Dictatorship", "Rule by one person with total power"],
        ]),
    },
    "social-studies-g7-l12": {
        "data_table": table(["Economic System", "Key Feature"], [
            ["Market economy", "Driven by supply, demand, and private ownership"],
            ["Command economy", "Government controls production and pricing"],
            ["Mixed economy", "Combination of market and government control"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g7-l12": {
        "data_table": table(["Event Type", "Examples"], [
            ["Track", "100m sprint, 400m, 1500m, hurdles"],
            ["Field", "Long jump, high jump, shot put, javelin"],
        ]),
    },
    "physical-education-self-defense-g7-l9": {
        "data_table": table(["Basketball Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"],
            ["Passing", "Moving the ball to a teammate"],
            ["Shooting", "Aiming the ball at the basket"],
        ]),
    },
    # ---- Critical Thinking ----
    "critical-thinking-g7-l8": {
        "data_table": table(["Syllogism Part", "Example"], [
            ["Major premise", "All mammals are warm-blooded"],
            ["Minor premise", "A dog is a mammal"],
            ["Conclusion", "Therefore, a dog is warm-blooded"],
        ]),
    },
    "critical-thinking-g7-l4": {
        "data_table": table(["Logical Fallacy", "Description"], [
            ["Ad Hominem", "Attacking the person instead of the argument"],
            ["Straw Man", "Misrepresenting someone's argument to attack it easily"],
            ["Slippery Slope", "Claiming one step will lead to extreme consequences without evidence"],
        ]),
    },
    # ---- Health Education ----
    "health-education-g7-l12": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice daily"], ["Floss", "Once daily"], ["Dentist visit", "Every 6 months"],
        ]),
    },
    "health-education-g7-l9": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g7-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Encryption", "Converting data into a coded form to prevent unauthorized access"],
            ["Decryption", "Converting encrypted data back to its original form"],
            ["HTTPS", "The encrypted version of HTTP used for secure websites"],
        ]),
    },
    "ict-g7-l1": {
        "data_table": table(["OOP Concept", "Meaning"], [
            ["Class", "A blueprint for creating objects"],
            ["Object", "An instance of a class"],
            ["Method", "A function defined inside a class"],
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
        raise SystemExit(f"Lesson ids not found in grade7.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 7 lessons (all subjects).")


if __name__ == "__main__":
    main()
