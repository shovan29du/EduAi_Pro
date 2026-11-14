#!/usr/bin/env python3
"""Breadth-first pass, Grade 6: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade6.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real atomic particle
charges, Newton's Laws, real historical dates, real Quran structure facts,
real Nobel Prize categories, etc.) -- nothing fabricated or presented as
fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g6-l10": {
        "data_table": table(["Type", "Example"], [
            ["Simile", "Brave as a lion"], ["Metaphor", "Time is money"],
        ]),
    },
    "english-g6-l16": {
        "data_table": table(["Poetic Device", "Definition"], [
            ["Alliteration", "Repetition of initial consonant sounds"],
            ["Onomatopoeia", "A word that imitates a sound (e.g. buzz)"],
            ["Personification", "Giving human traits to non-human things"],
        ]),
    },
    # ---- Science ----
    "sci-g6-l1": {
        "data_table": table(["Particle", "Charge", "Location"], [
            ["Proton", "Positive", "Nucleus"], ["Neutron", "Neutral", "Nucleus"],
            ["Electron", "Negative", "Orbiting the nucleus"],
        ]),
    },
    "science-g6-l13": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    # ---- Geography ----
    "geography-g6-l17": {
        "data_table": table(["Country", "Capital"], [
            ["Germany", "Berlin"], ["Italy", "Rome"], ["Spain", "Madrid"], ["Poland", "Warsaw"],
        ]),
    },
    "geography-g6-l9": {
        "data_table": table(["Desert", "Location", "Type"], [
            ["Sahara", "North Africa", "Hot desert (largest hot desert)"],
            ["Gobi", "Asia (Mongolia/China)", "Cold desert"],
            ["Antarctic Desert", "Antarctica", "Coldest and largest desert overall"],
        ]),
    },
    # ---- World History ----
    "hist-g6-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Began in", "Britain, mid-1700s"],
            ["Key invention", "The steam engine (improved by James Watt)"],
            ["Major shift", "From hand production to machine manufacturing"],
        ]),
    },
    "hist-g6-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"],
            ["Started after", "Assassination of Archduke Franz Ferdinand, June 1914"],
            ["Ended by", "Armistice of 11 November 1918"],
        ]),
    },
    # ---- Islamic Studies ----
    "is-g6-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Number of Surahs (chapters)", "114"],
            ["Longest Surah", "Al-Baqarah"], ["Shortest Surah", "Al-Kawthar"],
        ]),
    },
    "islamic-studies-g6-l10": {
        "data_table": table(["Article of Faith", "Belief In"], [
            ["1", "Allah (God)"], ["2", "Angels"], ["3", "Revealed Books"],
            ["4", "Prophets"], ["5", "The Day of Judgment"], ["6", "Divine Decree (Qadar)"],
        ]),
    },
    # ---- Coding ----
    "coding-g6-l14": {
        "data_table": table(["Bubble Sort Step", "Array State"], [
            ["Start", "[5, 3, 8, 1]"], ["After pass 1", "[3, 5, 1, 8]"],
            ["After pass 2", "[3, 1, 5, 8]"], ["After pass 3 (sorted)", "[1, 3, 5, 8]"],
        ]),
    },
    "coding-g6-l19": {
        "data_table": table(["HTML Tag", "Purpose"], [
            ["<h1>", "Main heading"], ["<p>", "Paragraph"], ["<a>", "Link"], ["<img>", "Image"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g6-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["The Iliad is about", "The Trojan War"],
            ["The Odyssey is about", "Odysseus's journey home"],
            ["Attributed author", "Homer (ancient Greek poet)"],
        ]),
    },
    "world-literature-g6-l15": {
        "data_table": table(["Indian Epic", "Main Character(s)"], [
            ["Ramayana", "Rama"], ["Mahabharata", "The Pandavas and Kauravas"],
        ]),
    },
    # ---- Art ----
    "art-g6-l4": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    "art-g6-l20": {
        "data_table": table(["Element", "Common Use"], [
            ["Geometric patterns", "Mosque decoration, avoiding figurative images"],
            ["Arabesque", "Flowing plant-based patterns"],
            ["Muqarnas", "3D honeycomb-like architectural ornamentation"],
        ]),
    },
    # ---- Music ----
    "music-g6-l11": {
        "data_table": table(["Period", "Approx. Dates", "Famous Composer"], [
            ["Baroque", "1600-1750", "J.S. Bach"], ["Classical", "1750-1820", "Mozart"],
            ["Romantic", "1820-1900", "Beethoven (late) / Chopin"],
        ]),
    },
    "music-g6-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "New Orleans, USA, late 19th / early 20th century"],
            ["Key feature", "Improvisation"], ["Famous musician", "Louis Armstrong"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g6-l11": {
        "data_table": table(["Condition", "Warning Signs"], [
            ["Hypothermia", "Shivering, confusion, slurred speech"],
            ["Heatstroke", "High body temperature, hot/dry skin, confusion"],
        ]),
    },
    "survival-skills-g6-l4": {
        "data_table": table(["Method", "How It Works"], [
            ["Boiling", "Boil for at least 1 minute (3 minutes above 2,000m) to kill pathogens"],
            ["Water filter", "Physically removes bacteria and parasites"],
            ["Purification tablets", "Chemically disinfect water"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g6-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Longest river", "Nile, ~6,650 km"], ["Tallest mountain", "Mount Everest, 8,849 m"],
        ]),
    },
    "general-knowledge-g6-l19": {
        "data_table": table(["Nobel Prize Category", "Field"], [
            ["Physics", "Science"], ["Chemistry", "Science"], ["Physiology or Medicine", "Science"],
            ["Literature", "Writing"], ["Peace", "International peace efforts"],
            ["Economic Sciences", "Added 1968, in memory of Alfred Nobel"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g6-l4": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"], ["2 cups", "1 pint"],
        ]),
    },
    "cooking-g6-l15": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g6-l3": {
        "data_table": table(["Pronoun", "Hablar (\"to speak\")"], [
            ["yo", "hablo"], ["tu", "hablas"], ["el/ella", "habla"], ["nosotros", "hablamos"],
        ]),
    },
    "foreign-languages-g6-l16": {
        "data_table": table(["Arabic Letter", "Name"], [
            ["a", "Alif"], ["b", "Ba"], ["t", "Ta"], ["th", "Tha"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g6-l3": {
        "data_table": table(["Branch of Government", "Main Role"], [
            ["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "social-studies-g6-l9": {
        "data_table": table(["Fact (US Constitution example)", "Detail"], [
            ["Constitution signed", "1787"], ["Ratified", "1788"],
            ["Original amendments (Bill of Rights)", "10"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g6-l11": {
        "data_table": table(["Jumping Event", "Description"], [
            ["Long Jump", "Jumping horizontally for distance"],
            ["High Jump", "Jumping vertically over a bar"],
            ["Triple Jump", "Hop, step, and jump for distance"],
        ]),
    },
    "physical-education-self-defense-g6-l6": {
        "data_table": table(["Basketball Skill", "Description"], [
            ["Dribbling", "Bouncing the ball while moving"],
            ["Passing", "Moving the ball to a teammate"],
            ["Shooting", "Aiming the ball at the basket"],
        ]),
    },
    # ---- Critical Thinking ----
    "critical-thinking-g6-l5": {
        "data_table": table(["Logical Fallacy", "Description"], [
            ["Ad Hominem", "Attacking the person instead of the argument"],
            ["Straw Man", "Misrepresenting someone's argument to attack it easily"],
            ["Slippery Slope", "Claiming one step will lead to extreme consequences without evidence"],
        ]),
    },
    "critical-thinking-g6-l4": {
        "data_table": table(["Reasoning Type", "Description"], [
            ["Deductive", "General rule leads to a specific, guaranteed conclusion"],
            ["Inductive", "Specific observations lead to a probable general conclusion"],
        ]),
    },
    # ---- Health Education ----
    "health-education-g6-l8": {
        "data_table": table(["Immune System Component", "Role"], [
            ["White blood cells", "Fight infections"],
            ["Antibodies", "Recognize and neutralize pathogens"],
            ["Skin", "First barrier against germs"],
        ]),
    },
    "hlt-g6-l3": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g6-l18": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"], ["5", "101"],
        ]),
    },
    "ict-g6-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Firewall", "Blocks unauthorized network access"],
            ["VPN", "Encrypts an internet connection for privacy"],
            ["Phishing", "Fraudulent attempt to steal information via fake messages"],
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
        raise SystemExit(f"Lesson ids not found in grade6.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 6 lessons (all subjects).")


if __name__ == "__main__":
    main()
