#!/usr/bin/env python3
"""Breadth-first pass, Grade 3: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade3.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real mountain
heights, real Viking Age dates, real French/Spanish number words, real
cooking measurement equivalents, etc.) -- nothing fabricated or presented
as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g3-l9": {
        "data_table": table(["Word", "Homophone", "Meaning Difference"], [
            ["Their", "There", "Belonging to them / a place"],
            ["Two", "Too", "The number 2 / also"],
            ["Bare", "Bear", "Uncovered / the animal"],
        ]),
    },
    "english-g3-l19": {
        "data_table": table(["Word", "Synonym (from a Thesaurus)"], [
            ["Happy", "Joyful"], ["Sad", "Unhappy"], ["Big", "Enormous"],
        ]),
    },
    # ---- Science ----
    "science-g3-l7": {
        "data_table": table(["Animal", "Adaptation", "Purpose"], [
            ["Camel", "Humps store fat", "Survive without water for long periods"],
            ["Polar Bear", "Thick fur and fat layer", "Stay warm in the Arctic"],
            ["Giraffe", "Long neck", "Reach leaves high in trees"],
        ]),
    },
    "science-g3-l17": {
        "data_table": table(["Planet", "Position from the Sun"], [
            ["Mercury", "1"], ["Venus", "2"], ["Earth", "3"], ["Mars", "4"],
            ["Jupiter", "5"], ["Saturn", "6"], ["Uranus", "7"], ["Neptune", "8"],
        ]),
    },
    # ---- Geography ----
    "geography-g3-l9": {
        "data_table": table(["Mountain", "Location", "Approx. Height"], [
            ["Mount Everest", "Nepal/China", "8,849 m"],
            ["Kilimanjaro", "Tanzania", "5,895 m"],
            ["Denali", "USA (Alaska)", "6,190 m"],
        ]),
    },
    "geography-g3-l16": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["Egypt", "Cairo"], ["Australia", "Canberra"],
        ]),
    },
    # ---- World History ----
    "world-history-g3-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Viking Age", "c. 793-1066 CE"],
            ["Homeland", "Scandinavia (Norway, Sweden, Denmark)"],
            ["Famous voyage", "Leif Erikson reached North America c. 1000 CE"],
        ]),
    },
    "world-history-g3-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Birthplace of democracy", "Athens, Greece"],
            ["Approximate start", "c. 508 BCE (reforms of Cleisthenes)"],
            ["Meaning of 'democracy'", "Greek for 'rule by the people'"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g3-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["The Kaaba is located in", "Mecca, Saudi Arabia"],
            ["Hajj takes place during", "Dhul Hijjah (the 12th Islamic month)"],
            ["Hajj is obligatory for", "Muslims who are able, at least once in their lifetime"],
        ]),
    },
    "islamic-studies-g3-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Ramadan is", "The 9th month of the Islamic calendar"],
            ["Main practice", "Fasting from dawn to sunset"],
            ["Ends with", "Eid al-Fitr"],
        ]),
    },
    # ---- Coding ----
    "coding-g3-l4": {
        "data_table": table(["Loop Type", "Example"], [
            ["Repeat N times", "repeat 5: move forward"],
            ["Repeat until condition", "repeat until at edge: move forward"],
        ]),
    },
    "coding-g3-l9": {
        "data_table": table(["Variable", "Starting Value", "After +1"], [
            ["score", "0", "1"], ["lives", "3", "4"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g3-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Norwegian folktale"],
            ["First published", "Collected by Asbjornsen and Moe, 1841-1844"],
            ["Main characters", "Three goats and a troll"],
        ]),
    },
    "world-literature-g3-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Collection", "One Thousand and One Nights"],
            ["Added to the collection by", "Antoine Galland (French translator, early 1700s)"],
            ["Setting in the original text", "Often depicted in China"],
        ]),
    },
    # ---- Art ----
    "art-g3-l2": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    "art-g3-l11": {
        "data_table": table(["Artist", "Known For"], [
            ["Claude Monet", "Founder of Impressionism"],
            ["Frida Kahlo", "Self-portraits"],
            ["Georgia O'Keeffe", "Large-scale flower paintings"],
        ]),
    },
    # ---- Music ----
    "mus-g3-l1": {
        "data_table": table(["Note Name", "Beats (in 4/4 time)"], [
            ["Whole note", "4 beats"], ["Half note", "2 beats"],
            ["Quarter note", "1 beat"], ["Eighth note", "1/2 beat"],
        ]),
    },
    "music-g3-l18": {
        "data_table": table(["Family", "Example Instruments"], [
            ["Strings", "Violin, Cello, Guitar"], ["Woodwinds", "Flute, Clarinet, Oboe"],
            ["Brass", "Trumpet, Trombone, Tuba"], ["Percussion", "Drums, Xylophone, Cymbals"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g3-l10": {
        "data_table": table(["Knot", "Common Use"], [
            ["Square Knot", "Joining two ropes of equal thickness"],
            ["Bowline", "Creating a secure loop that doesn't slip"],
            ["Clove Hitch", "Attaching a rope to a post or pole"],
        ]),
    },
    "survival-skills-g3-l4": {
        "data_table": table(["Step", "Action"], [
            ["1", "Stay calm"],
            ["2", "Call the local emergency number (e.g. 911 in the US, 999 in the UK)"],
            ["3", "Give your location clearly"],
            ["4", "Follow the operator's instructions"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g3-l19": {
        "data_table": table(["Ocean", "Rank by Size"], [
            ["Pacific Ocean", "1 (largest)"], ["Atlantic Ocean", "2"], ["Indian Ocean", "3"],
            ["Southern Ocean", "4"], ["Arctic Ocean", "5 (smallest)"],
        ]),
    },
    "general-knowledge-g3-l12": {
        "data_table": table(["Scientist", "Known For"], [
            ["Isaac Newton", "Laws of motion and gravity"],
            ["Marie Curie", "Research on radioactivity"],
            ["Albert Einstein", "Theory of relativity"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g3-l4": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"], ["2 cups", "1 pint"],
        ]),
    },
    "cooking-g3-l3": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g3-l3": {
        "data_table": table(["Number", "French"], [
            ["1", "un"], ["2", "deux"], ["3", "trois"], ["4", "quatre"], ["5", "cinq"],
            ["6", "six"], ["7", "sept"], ["8", "huit"], ["9", "neuf"], ["10", "dix"],
            ["11", "onze"], ["12", "douze"], ["13", "treize"], ["14", "quatorze"], ["15", "quinze"],
            ["16", "seize"], ["17", "dix-sept"], ["18", "dix-huit"], ["19", "dix-neuf"], ["20", "vingt"],
        ]),
    },
    "foreign-languages-g3-l8": {
        "data_table": table(["Number", "Spanish"], [
            ["1", "uno"], ["2", "dos"], ["3", "tres"], ["4", "cuatro"], ["5", "cinco"],
            ["6", "seis"], ["7", "siete"], ["8", "ocho"], ["9", "nueve"], ["10", "diez"],
            ["11", "once"], ["12", "doce"], ["13", "trece"], ["14", "catorce"], ["15", "quince"],
            ["16", "dieciseis"], ["17", "diecisiete"], ["18", "dieciocho"], ["19", "diecinueve"], ["20", "veinte"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g3-l3": {
        "data_table": table(["Type", "Example", "Who Makes It"], [
            ["Rule", "No running in the hallway", "School / classroom"],
            ["Law", "Wear a seatbelt while driving", "Government"],
        ]),
    },
    "social-studies-g3-l8": {
        "data_table": table(["Concept", "Meaning"], [
            ["Barter", "Trading goods directly without money"],
            ["Currency", "Money used to buy and sell goods"],
            ["Trade", "Exchanging goods and services"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g3-l17": {
        "data_table": table(["Movement", "Purpose"], [
            ["Stance", "Provides balance and stability"],
            ["Block", "Defends against a strike"],
            ["Punch / Strike", "Basic offensive technique"],
        ]),
    },
    "physical-education-self-defense-g3-l8": {
        "data_table": table(["Yoga Pose", "Sanskrit Name"], [
            ["Warrior Pose", "Virabhadrasana"], ["Triangle Pose", "Trikonasana"],
            ["Seated Forward Bend", "Paschimottanasana"],
        ]),
    },
    # ---- Health Education ----
    "hlt-g3-l2": {
        "data_table": table(["Body System", "Main Function"], [
            ["Circulatory", "Pumps blood through the body"],
            ["Respiratory", "Brings oxygen in, removes carbon dioxide"],
            ["Digestive", "Breaks down food for energy"],
            ["Skeletal", "Supports and protects the body"],
        ]),
    },
    "health-education-g3-l11": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice daily"], ["Floss", "Once daily"], ["Dentist visit", "Every 6 months"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g3-l18": {
        "data_table": table(["Spreadsheet Term", "Meaning"], [
            ["Cell", "A single box in a spreadsheet grid"],
            ["Row", "A horizontal line of cells"],
            ["Column", "A vertical line of cells"],
        ]),
    },
    "ict-computer-science-g3-l13": {
        "data_table": table(["Password Tip", "Why It Matters"], [
            ["Use 8+ characters", "Harder to guess"], ["Mix letters, numbers, symbols", "Increases security"],
            ["Don't share passwords", "Keeps your account safe"],
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
        raise SystemExit(f"Lesson ids not found in grade3.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 3 lessons (all subjects).")


if __name__ == "__main__":
    main()
