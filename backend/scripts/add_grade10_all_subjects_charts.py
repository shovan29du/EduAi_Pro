#!/usr/bin/env python3
"""Breadth-first pass, Grade 10: add genuine, hand-checked data_table
content to a representative batch of lessons across every non-Math subject
in grade10.json (Math already covered by add_math_charts_all_levels.py).

Every fact here is real and independently verifiable (real sonnet rhyme
schemes, the real DRSABCD first-aid mnemonic, Avogadro's number, real
DNA base pairing, real social contract philosophers, etc.) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g10-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "William Shakespeare"], ["Written", "c. 1606"], ["Setting", "Scotland"],
        ]),
    },
    "english-g10-l11": {
        "data_table": table(["Sonnet Form", "Rhyme Scheme"], [
            ["Shakespearean (English)", "ABAB CDCD EFEF GG"], ["Petrarchan (Italian)", "ABBAABBA CDECDE"],
        ]),
    },
    # ---- Science ----
    "science-g10-l14": {
        "formulae": ["PV = nRT (Ideal Gas Law)", "Boyle's Law: P1V1 = P2V2"],
        "data_table": table(["Gas Law", "Relationship"], [
            ["Boyle's Law", "Pressure and volume are inversely related (constant temperature)"],
            ["Charles's Law", "Volume and temperature are directly related (constant pressure)"],
        ]),
    },
    "science-g10-l16": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    # ---- Geography ----
    "geography-g10-l10": {
        "data_table": table(["Greenhouse Gas", "Main Human Source"], [
            ["Carbon dioxide (CO2)", "Burning fossil fuels"],
            ["Methane (CH4)", "Agriculture, livestock, landfills"],
            ["Nitrous oxide (N2O)", "Fertilizers, industrial processes"],
        ]),
    },
    "geography-g10-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Magma", "Molten rock beneath Earth's surface"],
            ["Lava", "Molten rock that reaches the surface"],
            ["Magnitude scale", "Measures earthquake strength"],
        ]),
    },
    # ---- World History ----
    "world-history-g10-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Approximate period", "16th-19th century"],
            ["Estimated number transported", "~12.5 million Africans"],
            ["Abolished in the British Empire", "1833 (Slavery Abolition Act)"],
        ]),
    },
    "hist-g10-l1": {
        "data_table": table(["Conflict", "Dates"], [
            ["World War I", "1914-1918"], ["World War II", "1939-1945"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g10-l13": {
        "data_table": table(["Rightly Guided Caliph", "Order"], [
            ["Abu Bakr", "1st"], ["Umar ibn al-Khattab", "2nd"],
            ["Uthman ibn Affan", "3rd"], ["Ali ibn Abi Talib", "4th"],
        ]),
    },
    "islamic-studies-g10-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Split originated over", "Disagreement on succession after the Prophet's death, 632 CE"],
            ["Majority tradition worldwide", "Sunni (~85-90% of Muslims)"],
        ]),
    },
    # ---- Coding ----
    "coding-g10-l15": {
        "data_table": table(["Big O Notation", "Meaning"], [
            ["O(1)", "Constant time"], ["O(n)", "Linear time"],
            ["O(log n)", "Logarithmic time"], ["O(n^2)", "Quadratic time"],
        ]),
    },
    "coding-g10-l16": {
        "data_table": table(["Structure", "Order"], [
            ["Stack", "LIFO (Last In, First Out)"], ["Queue", "FIFO (First In, First Out)"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g10-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Playwright", "Sophocles"], ["Written", "c. 429 BCE"], ["Genre", "Greek tragedy"],
        ]),
    },
    "world-literature-g10-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Victor Hugo"], ["Published", "1862"], ["Setting", "19th-century France"],
        ]),
    },
    # ---- Art ----
    "art-g10-l20": {
        "data_table": table(["Style", "Approx. Period", "Famous Artist"], [
            ["Baroque", "1600-1750", "Caravaggio"], ["Rococo", "1700-1770", "Fragonard"],
        ]),
    },
    "art-g10-l3": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    # ---- Music ----
    "music-g10-l17": {
        "data_table": table(["Period", "Approx. Dates", "Famous Composer"], [
            ["Baroque", "1600-1750", "J.S. Bach"], ["Classical", "1750-1820", "Mozart"],
            ["Romantic", "1820-1900", "Beethoven (late) / Chopin"],
        ]),
    },
    "music-g10-l8": {
        "data_table": table(["Interval", "Semitones"], [
            ["Minor 2nd", "1"], ["Major 2nd", "2"], ["Perfect 4th", "5"],
            ["Perfect 5th", "7"], ["Octave", "12"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g10-l3": {
        "data_table": table(["CPR Step", "Action"], [
            ["1", "Check responsiveness and call for emergency help"],
            ["2", "Give 30 chest compressions (about 2 inches deep)"],
            ["3", "Give 2 rescue breaths (if trained)"],
            ["4", "Repeat the 30:2 ratio until help arrives"],
        ]),
    },
    "survival-skills-g10-l10": {
        "data_table": table(["Method", "How It Works"], [
            ["Boiling", "Boil for at least 1 minute (3 minutes above 2,000m) to kill pathogens"],
            ["Water filter", "Physically removes bacteria and parasites"],
            ["Purification tablets", "Chemically disinfect water"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g10-l11": {
        "data_table": table(["Taste", "Example Food"], [
            ["Sweet", "Sugar, honey"], ["Sour", "Lemon, vinegar"], ["Salty", "Salt, soy sauce"],
            ["Bitter", "Coffee, dark chocolate"], ["Umami", "Mushrooms, parmesan, soy sauce"],
        ]),
    },
    "cooking-g10-l5": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"], ["2 cups", "1 pint"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g10-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Creator", "King Sejong the Great"], ["Introduced", "1443/1446"],
            ["Structure", "Featural alphabet; letters grouped into syllable blocks"],
        ]),
    },
    "foreign-languages-g10-l2": {
        "data_table": table(["Spanish Past Tense", "Use"], [
            ["Preterite", "Completed actions at a specific time"],
            ["Imperfect", "Ongoing or repeated past actions"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g10-l10": {
        "data_table": table(["Nobel Prize Category", "Field"], [
            ["Physics", "Science"], ["Chemistry", "Science"], ["Physiology or Medicine", "Science"],
            ["Literature", "Writing"], ["Peace", "International peace efforts"],
            ["Economic Sciences", "Added 1968, in memory of Alfred Nobel"],
        ]),
    },
    "general-knowledge-g10-l20": {
        "data_table": table(["Desert", "Location", "Type"], [
            ["Sahara", "North Africa", "Hot desert (largest hot desert)"],
            ["Gobi", "Asia (Mongolia/China)", "Cold desert"],
            ["Antarctic Desert", "Antarctica", "Coldest and largest desert overall"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g10-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"],
            ["Started after", "Assassination of Archduke Franz Ferdinand, June 1914"],
            ["Ended by", "Armistice of 11 November 1918"],
        ]),
    },
    "social-studies-g10-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1939-1945"],
            ["Started when", "Germany invaded Poland, September 1939"],
            ["Ended in Europe", "V-E Day, May 8, 1945"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g10-l19": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    "physical-education-self-defense-g10-l11": {
        "data_table": table(["Badminton Term", "Meaning"], [
            ["Shuttlecock", "The object hit over the net"],
            ["Rally", "Continuous play until a point is scored"],
            ["Match play", "Best of 3 games to 21 points"],
        ]),
    },
    # ---- Economics ----
    "economics-g10-l14": {
        "data_table": table(["Market Structure", "Number of Sellers"], [
            ["Perfect Competition", "Many"], ["Monopolistic Competition", "Many, differentiated products"],
            ["Oligopoly", "Few"], ["Monopoly", "One"],
        ]),
    },
    "economics-g10-l20": {
        "data_table": table(["Concept", "Meaning"], [
            ["Absolute advantage", "Producing more of a good with the same resources"],
            ["Comparative advantage", "Producing a good at a lower opportunity cost than another"],
        ]),
    },
    # ---- Finance ----
    "finance-g10-l8": {
        "formulae": ["Simple Interest = P x r x t", "Compound Interest = P(1+r)^t - P"],
        "data_table": table(["Interest Type", "$1000 at 5% after 3 years"], [
            ["Simple", "$1,150"], ["Compound (annual)", "$1,157.63"],
        ]),
    },
    "finance-g10-l9": {
        "data_table": table(["FICO Credit Score Range", "Rating"], [
            ["800-850", "Exceptional"], ["740-799", "Very Good"], ["670-739", "Good"],
            ["580-669", "Fair"], ["300-579", "Poor"],
        ]),
    },
    # ---- First Aid ----
    "first-aid-g10-l2": {
        "data_table": table(["DRSABCD Letter", "Meaning"], [
            ["D", "Danger - check for danger"], ["R", "Response - check responsiveness"],
            ["S", "Send for help"], ["A", "Airway - open the airway"],
            ["B", "Breathing - check for breathing"], ["C", "CPR - start chest compressions"],
            ["D", "Defibrillation - use an AED if available"],
        ]),
    },
    "first-aid-g10-l17": {
        "data_table": table(["RICE Letter", "Meaning"], [
            ["R", "Rest"], ["I", "Ice"], ["C", "Compression"], ["E", "Elevation"],
        ]),
    },
    # ---- Physics ----
    "physics-g10-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Principle", "A submerged object feels an upward force equal to the weight of fluid it displaces"],
            ["Discovered by", "Archimedes of Syracuse, c. 250 BCE"],
        ]),
    },
    "physics-g10-l9": {
        "formulae": ["Work = Force x Distance", "Power = Work / Time"],
        "data_table": table(["Quantity", "Formula", "SI Unit"], [
            ["Work", "F x d", "Joule (J)"], ["Power", "W / t", "Watt (W)"],
        ]),
    },
    # ---- Chemistry ----
    "chemistry-g10-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Avogadro's number", "6.022 x 10^23 particles per mole"],
            ["1 mole of any gas at STP", "Occupies 22.4 liters"],
        ]),
    },
    "chemistry-g10-l11": {
        "data_table": table(["pH Range", "Type", "Example"], [
            ["0-6", "Acidic", "Lemon juice (~2)"], ["7", "Neutral", "Pure water"],
            ["8-14", "Basic (alkaline)", "Baking soda (~9)"],
        ]),
    },
    # ---- Biology ----
    "biology-g10-l10": {
        "data_table": table(["Cross", "Genotype Ratio (Aa x Aa)"], [
            ["Offspring", "1 AA : 2 Aa : 1 aa"],
        ]),
    },
    "biology-g10-l8": {
        "data_table": table(["DNA Base", "Pairs With"], [
            ["Adenine (A)", "Thymine (T)"], ["Cytosine (C)", "Guanine (G)"],
        ]),
    },
    # ---- Philosophy ----
    "philosophy-g10-l15": {
        "data_table": table(["Philosopher", "Key Idea"], [
            ["Thomas Hobbes", "People consent to government to escape a brutal 'state of nature'"],
            ["John Locke", "Government exists to protect natural rights (life, liberty, property)"],
            ["Jean-Jacques Rousseau", "Legitimate government reflects the 'general will' of the people"],
        ]),
    },
    "philosophy-g10-l10": {
        "data_table": table(["Philosopher", "Key Idea"], [
            ["Jeremy Bentham", "Founder of utilitarianism; the 'greatest happiness principle'"],
            ["John Stuart Mill", "Refined utilitarianism; distinguished higher and lower pleasures"],
        ]),
    },
    # ---- Critical Thinking ----
    "critical-thinking-g10-l5": {
        "data_table": table(["Logical Fallacy", "Description"], [
            ["Ad Hominem", "Attacking the person instead of the argument"],
            ["Straw Man", "Misrepresenting someone's argument to attack it easily"],
            ["Slippery Slope", "Claiming one step will lead to extreme consequences without evidence"],
        ]),
    },
    "critical-thinking-g10-l9": {
        "data_table": table(["Cognitive Bias", "Description"], [
            ["Availability heuristic", "Judging likelihood by how easily examples come to mind"],
            ["Anchoring bias", "Relying too heavily on the first piece of information given"],
        ]),
    },
    # ---- Health Education ----
    "health-education-g10-l11": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g10-l7": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g10-l19": {
        "data_table": table(["SQL Keyword", "Purpose"], [
            ["SELECT", "Retrieve data from a table"], ["WHERE", "Filter rows by a condition"],
            ["INSERT", "Add new data to a table"],
        ]),
    },
    "ict-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step procedure for solving a problem"],
            ["Data structure", "A way of organizing data for efficient use"],
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
        raise SystemExit(f"Lesson ids not found in grade10.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 10 lessons (all subjects).")


if __name__ == "__main__":
    main()
