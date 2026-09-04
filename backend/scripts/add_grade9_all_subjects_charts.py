#!/usr/bin/env python3
"""Breadth-first pass, Grade 9: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade9.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real historical
dates for the Persian Empire and Hijrah, the real FAST/RICE first-aid
mnemonics, real simple/compound interest arithmetic, real ionic/covalent
bonding facts, etc.) -- nothing fabricated or presented as fact when it's
actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g9-l4": {
        "data_table": table(["Poetic Device", "Definition"], [
            ["Alliteration", "Repetition of initial consonant sounds"],
            ["Onomatopoeia", "A word that imitates a sound (e.g. buzz)"],
            ["Personification", "Giving human traits to non-human things"],
        ]),
    },
    "eng-g9-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Born", "1564, Stratford-upon-Avon"], ["Died", "1616"],
            ["Number of plays attributed to him", "~37-39"],
        ]),
    },
    # ---- Science ----
    "sci-g9-l1": {
        "data_table": table(["Concept", "Meaning"], [
            ["Natural selection", "Organisms better suited to their environment survive and reproduce more"],
            ["Proposed by", "Charles Darwin (On the Origin of Species, 1859)"],
        ]),
    },
    "science-g9-l7": {
        "data_table": table(["Cross", "Genotype Ratio (Aa x Aa)"], [
            ["Offspring", "1 AA : 2 Aa : 1 aa"],
        ]),
    },
    # ---- Geography ----
    "geography-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Tectonic plate", "A large slab of Earth's crust that moves slowly"],
            ["Fault", "A crack where plates meet and can slip"],
            ["Magnitude scale", "Measures the energy/strength of an earthquake"],
        ]),
    },
    "geography-g9-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Glacier", "A large, slow-moving mass of ice"],
            ["Moraine", "Debris deposited by a glacier"],
        ]),
    },
    # ---- World History ----
    "world-history-g9-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Cyrus the Great, c. 550 BCE"],
            ["Peak extent", "Stretched from Egypt to the Indus Valley"],
        ]),
    },
    "world-history-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Born", "356 BCE, Pella, Macedon"], ["Died", "323 BCE, Babylon"],
            ["Empire extent", "Greece to northwestern India"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g9-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Year", "622 CE"], ["Significance", "Marks the start of the Islamic calendar"],
        ]),
    },
    "islamic-studies-g9-l16": {
        "data_table": table(["Article of Faith", "Belief In"], [
            ["1", "Allah (God)"], ["2", "Angels"], ["3", "Revealed Books"],
            ["4", "Prophets"], ["5", "The Day of Judgment"], ["6", "Divine Decree (Qadar)"],
        ]),
    },
    # ---- Coding ----
    "coding-g9-l12": {
        "data_table": table(["Big O Notation", "Meaning"], [
            ["O(1)", "Constant time"], ["O(n)", "Linear time"],
            ["O(log n)", "Logarithmic time"], ["O(n^2)", "Quadratic time"],
        ]),
    },
    "coding-g9-l17": {
        "data_table": table(["Git Command", "Purpose"], [
            ["git commit", "Save a snapshot of changes"],
            ["git push", "Upload commits to a remote repository"],
            ["git pull", "Download changes from a remote repository"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g9-l4": {
        "data_table": table(["Epic", "Origin", "Approx. Date"], [
            ["Epic of Gilgamesh", "Mesopotamia", "c. 2100 BCE (oldest known epic)"],
        ]),
    },
    "world-literature-g9-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Dante Alighieri"], ["Written", "Early 1300s"],
            ["Three parts", "Inferno, Purgatorio, Paradiso"],
        ]),
    },
    # ---- Art ----
    "art-g9-l8": {
        "data_table": table(["Perspective Type", "Vanishing Points"], [
            ["One-point", "1"], ["Two-point", "2"],
        ]),
    },
    "art-g9-l4": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    # ---- Music ----
    "music-g9-l7": {
        "data_table": table(["Scale", "Pattern (W = whole step, H = half step)"], [
            ["Major", "W-W-H-W-W-W-H"], ["Natural Minor", "W-H-W-W-H-W-W"],
        ]),
    },
    "music-g9-l16": {
        "data_table": table(["Period", "Approx. Dates", "Famous Composer"], [
            ["Baroque", "1600-1750", "J.S. Bach"], ["Classical", "1750-1820", "Mozart"],
            ["Romantic", "1820-1900", "Beethoven (late) / Chopin"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g9-l3": {
        "data_table": table(["CPR Step", "Action"], [
            ["1", "Check responsiveness and call for emergency help"],
            ["2", "Give 30 chest compressions (about 2 inches deep)"],
            ["3", "Give 2 rescue breaths (if trained)"],
            ["4", "Repeat the 30:2 ratio until help arrives"],
        ]),
    },
    "survival-skills-g9-l13": {
        "data_table": table(["Condition", "Warning Signs"], [
            ["Hypothermia", "Shivering, confusion, slurred speech"],
            ["Heatstroke", "High body temperature, hot/dry skin, confusion"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g9-l6": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"], ["2 cups", "1 pint"],
        ]),
    },
    "cooking-g9-l15": {
        "data_table": table(["Leavening Agent", "How It Works"], [
            ["Baking soda", "Reacts with acid to release carbon dioxide"],
            ["Baking powder", "Contains its own acid and base; reacts with liquid and heat"],
            ["Yeast", "Ferments sugars to produce carbon dioxide"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g9-l3": {
        "data_table": table(["Verb", "Use"], [
            ["Ser", "Permanent characteristics (e.g. Soy alto = I am tall)"],
            ["Estar", "Temporary states/location (e.g. Estoy cansado = I am tired)"],
        ]),
    },
    "foreign-languages-g9-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Creator", "King Sejong the Great"], ["Introduced", "1443/1446"],
            ["Structure", "Featural alphabet; letters grouped into syllable blocks"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g9-l4": {
        "data_table": table(["River", "Approx. Length", "Location"], [
            ["Nile", "~6,650 km", "Africa"], ["Amazon", "~6,400 km", "South America"],
            ["Yangtze", "~6,300 km", "China"],
        ]),
    },
    "general-knowledge-g9-l15": {
        "data_table": table(["Nobel Prize Category", "Field"], [
            ["Physics", "Science"], ["Chemistry", "Science"], ["Physiology or Medicine", "Science"],
            ["Literature", "Writing"], ["Peace", "International peace efforts"],
            ["Economic Sciences", "Added 1968, in memory of Alfred Nobel"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g9-l14": {
        "data_table": table(["Branch of Government", "Main Role"], [
            ["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "social-studies-g9-l17": {
        "data_table": table(["Tax Type", "Example"], [
            ["Income tax", "Tax on money earned from work"],
            ["Sales tax", "Tax added to purchases"],
            ["Property tax", "Tax on land/buildings owned"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g9-l7": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    "physical-education-self-defense-g9-l14": {
        "data_table": table(["Badminton Term", "Meaning"], [
            ["Shuttlecock", "The object hit over the net"],
            ["Rally", "Continuous play until a point is scored"],
            ["Match play", "Best of 3 games to 21 points"],
        ]),
    },
    # ---- Economics ----
    "economics-g9-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["GDP", "Total value of goods and services produced in a country in a given period"],
            ["GDP per capita", "GDP divided by population"],
        ]),
    },
    "economics-g9-l6": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price tends to rise"],
            ["Low demand, high supply", "Price tends to fall"],
        ]),
    },
    # ---- Finance ----
    "finance-g9-l8": {
        "formulae": ["Simple Interest = P x r x t", "Compound Interest = P(1+r)^t - P"],
        "data_table": table(["Interest Type", "$1000 at 5% after 3 years"], [
            ["Simple", "$1,150"], ["Compound (annual)", "$1,157.63"],
        ]),
    },
    "finance-g9-l10": {
        "data_table": table(["FICO Credit Score Range", "Rating"], [
            ["800-850", "Exceptional"], ["740-799", "Very Good"], ["670-739", "Good"],
            ["580-669", "Fair"], ["300-579", "Poor"],
        ]),
    },
    # ---- First Aid ----
    "first-aid-g9-l15": {
        "data_table": table(["FAST Letter", "Check For"], [
            ["F - Face", "Facial drooping"], ["A - Arms", "Arm weakness or drift"],
            ["S - Speech", "Slurred speech"], ["T - Time", "Time to call emergency services"],
        ]),
    },
    "first-aid-g9-l13": {
        "data_table": table(["RICE Letter", "Meaning"], [
            ["R", "Rest"], ["I", "Ice"], ["C", "Compression"], ["E", "Elevation"],
        ]),
    },
    # ---- Physics ----
    "physics-g9-l10": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    "physics-g9-l18": {
        "formulae": ["KE = 1/2 x m x v^2"],
        "data_table": table(["Energy Type", "Formula"], [
            ["Kinetic", "1/2 x m x v^2"],
        ]),
    },
    # ---- Chemistry ----
    "chemistry-g9-l5": {
        "data_table": table(["Element", "Symbol", "Atomic Number"], [
            ["Hydrogen", "H", "1"], ["Carbon", "C", "6"], ["Oxygen", "O", "8"], ["Iron", "Fe", "26"],
        ]),
    },
    "chemistry-g9-l8": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic", "Transfer of electrons between atoms (metal + nonmetal)"],
            ["Covalent", "Sharing of electrons between atoms (nonmetal + nonmetal)"],
        ]),
    },
    # ---- Biology ----
    "biology-g9-l20": {
        "data_table": table(["Mitosis Phase", "What Happens"], [
            ["Prophase", "Chromosomes condense and become visible"],
            ["Metaphase", "Chromosomes line up at the cell's center"],
            ["Anaphase", "Chromosomes are pulled to opposite ends"],
            ["Telophase", "Two new nuclei form"],
        ]),
    },
    "biology-g9-l9": {
        "data_table": table(["Organ", "Role"], [
            ["Stomach", "Breaks down food with acid and enzymes"],
            ["Small intestine", "Absorbs nutrients"],
            ["Large intestine", "Absorbs water, forms waste"],
        ]),
    },
    # ---- Philosophy ----
    "philosophy-g9-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Plato"],
            ["Key idea", "Forms are perfect, unchanging ideas that physical objects imperfectly reflect"],
            ["Student of", "Socrates"],
        ]),
    },
    "philosophy-g9-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Aristotle"],
            ["Key idea", "Virtue lies at the 'golden mean' between two extremes"],
            ["Teacher", "Plato"],
        ]),
    },
    # ---- Critical Thinking ----
    "critical-thinking-g9-l10": {
        "data_table": table(["Logical Fallacy", "Description"], [
            ["False Dilemma", "Presenting only two options when more exist"],
            ["Ad Hominem", "Attacking the person instead of the argument"],
            ["Strawman", "Misrepresenting an argument to attack it easily"],
        ]),
    },
    "critical-thinking-g9-l17": {
        "data_table": table(["Cognitive Bias", "Description"], [
            ["Availability heuristic", "Judging likelihood by how easily examples come to mind"],
            ["Anchoring bias", "Relying too heavily on the first piece of information given"],
        ]),
    },
    # ---- Health Education ----
    "health-education-g9-l12": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g9-l8": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g9-l6": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["3", "11"], ["4", "100"], ["5", "101"],
        ]),
    },
    "ict-g9-l1": {
        "data_table": table(["Web Technology", "Role"], [
            ["HTML", "Structure of a webpage"], ["CSS", "Styling of a webpage"],
            ["JavaScript", "Interactivity of a webpage"],
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
        raise SystemExit(f"Lesson ids not found in grade9.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 9 lessons (all subjects).")


if __name__ == "__main__":
    main()
