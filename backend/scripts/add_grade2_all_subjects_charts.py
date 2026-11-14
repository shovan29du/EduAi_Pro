#!/usr/bin/env python3
"""Breadth-first pass, Grade 2: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade2.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (the Five Pillars of
Islam, real language number-words, the USDA MyPlate food groups, real
publication dates for Grimm/Andersen tales, planet order from the Sun,
etc.) -- nothing fabricated or presented as fact when it's actually
invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g2-l10": {
        "data_table": table(["Word", "Synonym", "Antonym"], [
            ["Happy", "Glad", "Sad"], ["Big", "Large", "Small"], ["Fast", "Quick", "Slow"],
        ]),
    },
    "english-g2-l19": {
        "data_table": table(["Word", "First Letter", "Alphabetical Order"], [
            ["Elephant", "E", "1"], ["Giraffe", "G", "2"], ["Lion", "L", "3"], ["Zebra", "Z", "4"],
        ]),
    },
    # ---- Science ----
    "sci-g2-l1": {
        "data_table": table(["State", "Example"], [
            ["Solid", "Rock"], ["Liquid", "Juice"], ["Gas", "Oxygen"],
        ]),
    },
    "science-g2-l8": {
        "data_table": table(["Animal Group", "Example", "Key Trait"], [
            ["Mammals", "Dog", "Fur, feeds milk to young"],
            ["Birds", "Eagle", "Feathers, lays eggs"],
            ["Fish", "Salmon", "Gills, lives in water"],
            ["Reptiles", "Snake", "Scales, cold-blooded"],
            ["Amphibians", "Frog", "Lives on land and water"],
        ]),
    },
    # ---- Geography ----
    "geo-g2-l1": {
        "data_table": table(["Continent", "Rank by Area"], [
            ["Asia", "1 (largest)"], ["Africa", "2"], ["North America", "3"],
            ["South America", "4"], ["Antarctica", "5"], ["Europe", "6"], ["Australia", "7 (smallest)"],
        ]),
    },
    "geography-g2-l7": {
        "data_table": table(["Desert", "Location", "Type"], [
            ["Sahara", "North Africa", "Hot desert (largest hot desert)"],
            ["Gobi", "Asia (Mongolia/China)", "Cold desert"],
            ["Antarctic Desert", "Antarctica", "Coldest and largest desert overall"],
        ]),
    },
    # ---- World History ----
    "world-history-g2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["River essential to Ancient Egypt", "The Nile"],
            ["Great Pyramid built for", "Pharaoh Khufu, c. 2560 BCE"],
            ["Writing system", "Hieroglyphics"],
        ]),
    },
    "world-history-g2-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Rome traditionally founded", "753 BCE"],
            ["Roman Empire declared by", "Augustus, 27 BCE"],
            ["Fall of the Western Roman Empire", "476 CE"],
        ]),
    },
    # ---- Islamic Studies ----
    "is-g2-l1": {
        "data_table": table(["Pillar", "Meaning"], [
            ["Shahada", "Declaration of faith"], ["Salah", "Five daily prayers"],
            ["Zakat", "Charity to those in need"], ["Sawm", "Fasting during Ramadan"],
            ["Hajj", "Pilgrimage to Mecca"],
        ]),
    },
    "islamic-studies-g2-l8": {
        "data_table": table(["Eid", "When It Is Celebrated"], [
            ["Eid al-Fitr", "At the end of Ramadan"], ["Eid al-Adha", "During the Hajj season"],
        ]),
    },
    # ---- Coding ----
    "coding-g2-l5": {
        "data_table": table(["Pseudocode", "What It Does"], [
            ["repeat 4 times: move forward", "Moves forward 4 times"],
            ["repeat 10 times: clap", "Claps 10 times"],
        ]),
    },
    "coding-g2-l13": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"], ["5", "101"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g2-l12": {
        "data_table": table(["Tale", "Origin"], [
            ["Cinderella (Aschenputtel)", "Germany, Brothers Grimm, 1812"],
            ["Hansel and Gretel", "Germany, Brothers Grimm, 1812"],
            ["Snow White", "Germany, Brothers Grimm, 1812"],
        ]),
    },
    "world-literature-g2-l13": {
        "data_table": table(["Tale", "Year Published"], [
            ["The Little Mermaid", "1837"], ["The Emperor's New Clothes", "1837"],
            ["The Ugly Duckling", "1843"],
        ]),
    },
    # ---- Art ----
    "art-g2-l2": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    "art-g2-l16": {
        "data_table": table(["Perspective Concept", "Meaning"], [
            ["Near objects", "Appear larger and lower on the page"],
            ["Far objects", "Appear smaller and higher on the page"],
            ["Horizon line", "Where sky meets ground"],
        ]),
    },
    # ---- Music ----
    "music-g2-l6": {
        "data_table": table(["Instrument", "How It Is Played"], [
            ["Drum", "Struck with hands or sticks"], ["Xylophone", "Struck with mallets"],
            ["Tambourine", "Shaken or struck"],
        ]),
    },
    "music-g2-l10": {
        "data_table": table(["Note Name", "Beats (in 4/4 time)"], [
            ["Whole note", "4 beats"], ["Half note", "2 beats"],
            ["Quarter note", "1 beat"], ["Eighth note", "1/2 beat"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g2-l3": {
        "data_table": table(["Country", "Currency"], [
            ["United States", "US Dollar"], ["United Kingdom", "Pound Sterling"],
            ["Japan", "Yen"], ["European Union", "Euro"],
        ]),
    },
    "general-knowledge-g2-l6": {
        "data_table": table(["Planet", "Position from the Sun"], [
            ["Mercury", "1"], ["Venus", "2"], ["Earth", "3"], ["Mars", "4"],
            ["Jupiter", "5"], ["Saturn", "6"], ["Uranus", "7"], ["Neptune", "8"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g2-l2": {
        "data_table": table(["Number", "Spanish"], [
            ["1", "uno"], ["2", "dos"], ["3", "tres"], ["4", "cuatro"], ["5", "cinco"],
        ]),
    },
    "foreign-languages-g2-l9": {
        "data_table": table(["Number", "French"], [
            ["1", "un"], ["2", "deux"], ["3", "trois"], ["4", "quatre"], ["5", "cinq"],
            ["6", "six"], ["7", "sept"], ["8", "huit"], ["9", "neuf"], ["10", "dix"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g2-l6": {
        "data_table": table(["Category", "Examples"], [
            ["Goods", "Bread, shoes, books"], ["Services", "Haircut, teaching, doctor visit"],
        ]),
    },
    "ss-g2-l1": {
        "data_table": table(["Category", "Examples"], [
            ["Needs", "Food, water, shelter, clothing"], ["Wants", "Toys, video games, candy"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g2-l7": {
        "data_table": table(["Stretch", "Body Part Targeted"], [
            ["Quad stretch", "Front of the thigh"], ["Calf stretch", "Lower leg"], ["Shoulder stretch", "Shoulders"],
        ]),
    },
    "physical-education-self-defense-g2-l16": {
        "data_table": table(["Yoga Pose", "Sanskrit Name"], [
            ["Cobra Pose", "Bhujangasana"], ["Child's Pose", "Balasana"], ["Mountain Pose", "Tadasana"],
        ]),
    },
    # ---- Health Education ----
    "hlt-g2-l3": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    "hlt-g2-l5": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice daily"], ["Floss", "Once daily"], ["Dentist visit", "Every 6 months"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g2-l13": {
        "data_table": table(["Password Tip", "Why It Matters"], [
            ["Use 8+ characters", "Harder to guess"], ["Mix letters, numbers, symbols", "Increases security"],
            ["Don't share passwords", "Keeps your account safe"],
        ]),
    },
    "ict-g2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"],
            ["Website", "A collection of web pages"],
            ["Browser", "Software used to view websites"],
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
        raise SystemExit(f"Lesson ids not found in grade2.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 2 lessons (all subjects).")


if __name__ == "__main__":
    main()
