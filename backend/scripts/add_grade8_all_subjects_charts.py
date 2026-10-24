#!/usr/bin/env python3
"""Breadth-first pass, Grade 8: add genuine, hand-checked data_table content
to a representative batch of lessons across every non-Math subject in
grade8.json (Math already covered by add_math_charts_all_levels.py). Grade
8 introduces Economics, Finance, First Aid, Physics, Chemistry, Biology and
Philosophy on top of the Grade 1-7 subject set.

Every fact here is real and independently verifiable (the Rightly Guided
Caliphs in order, real FICO score bands, the 50/30/20 budgeting rule, real
physics/chemistry/biology facts, real philosophy attributions, etc.) --
nothing fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    # ---- English ----
    "english-g8-l9": {
        "data_table": table(["Type", "Example"], [
            ["Simile", "Brave as a lion"], ["Metaphor", "Time is money"],
        ]),
    },
    "english-g8-l3": {
        "data_table": table(["Direct Speech", "Indirect Speech"], [
            ["She said, \"I am happy.\"", "She said that she was happy."],
            ["He said, \"I will go.\"", "He said that he would go."],
        ]),
    },
    # ---- Science ----
    "sci-g8-l2": {
        "data_table": table(["Newton's Law", "Statement"], [
            ["1st Law (Inertia)", "An object stays at rest or in motion unless acted on by a force"],
            ["2nd Law", "F = m x a (Force = mass x acceleration)"],
            ["3rd Law", "For every action there is an equal and opposite reaction"],
        ]),
        "formulae": ["F = m x a"],
    },
    "science-g8-l15": {
        "data_table": table(["Element", "Symbol", "Atomic Number"], [
            ["Hydrogen", "H", "1"], ["Carbon", "C", "6"], ["Oxygen", "O", "8"], ["Iron", "Fe", "26"],
        ]),
    },
    # ---- Geography ----
    "geography-g8-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Magma", "Molten rock beneath Earth's surface"],
            ["Lava", "Molten rock that reaches the surface"],
            ["Magnitude scale", "Measures earthquake strength"],
        ]),
    },
    "geography-g8-l13": {
        "data_table": table(["Ocean", "Rank by Size"], [
            ["Pacific Ocean", "1 (largest)"], ["Atlantic Ocean", "2"], ["Indian Ocean", "3"],
            ["Southern Ocean", "4"], ["Arctic Ocean", "5 (smallest)"],
        ]),
    },
    # ---- World History ----
    "hist-g8-l1": {
        "data_table": table(["Country", "Independence Year"], [
            ["India", "1947"], ["Ghana", "1957"], ["Nigeria", "1960"],
        ]),
    },
    "world-history-g8-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded", "c. 1299 CE"], ["Capital (from 1453)", "Constantinople (Istanbul)"], ["Ended", "1922"],
        ]),
    },
    # ---- Islamic Studies ----
    "islamic-studies-g8-l7": {
        "data_table": table(["Rightly Guided Caliph", "Order"], [
            ["Abu Bakr", "1st"], ["Umar ibn al-Khattab", "2nd"],
            ["Uthman ibn Affan", "3rd"], ["Ali ibn Abi Talib", "4th"],
        ]),
    },
    "is-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Fiqh", "Islamic jurisprudence; understanding and application of Sharia"],
            ["Halal", "Permissible"], ["Haram", "Forbidden"],
        ]),
    },
    # ---- Coding ----
    "coding-g8-l19": {
        "data_table": table(["Function", "Purpose"], [
            ["math.sqrt(x)", "Square root of x"], ["math.pi", "The constant pi (3.14159...)"],
            ["random.choice(list)", "Pick a random item from a list"],
        ]),
    },
    "coding-g8-l17": {
        "data_table": table(["OOP Concept", "Meaning"], [
            ["Inheritance", "A class reuses / extends another class's behavior"],
            ["Polymorphism", "Different classes respond differently to the same method call"],
        ]),
    },
    # ---- World Literature ----
    "world-literature-g8-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Mary Shelley"], ["Published", "1818"], ["Genre", "Gothic science fiction"],
        ]),
    },
    "world-literature-g8-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Full name", "Jalal ad-Din Muhammad Rumi"],
            ["Born", "1207, Balkh (in present-day Afghanistan)"],
            ["Famous work", "The Masnavi"],
        ]),
    },
    # ---- Art ----
    "art-g8-l20": {
        "data_table": table(["Style", "Approx. Period", "Famous Artist"], [
            ["Baroque", "1600-1750", "Caravaggio"], ["Rococo", "1700-1770", "Fragonard"],
        ]),
    },
    "art-g8-l4": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    # ---- Music ----
    "music-g8-l16": {
        "data_table": table(["Genre", "Approx. Origin"], [
            ["Jazz", "Early 1900s, USA"], ["Rock and Roll", "1950s, USA"], ["Hip-Hop", "1970s, USA"],
        ]),
    },
    "mus-g8-l1": {
        "data_table": table(["Scale", "Pattern (W = whole step, H = half step)"], [
            ["Major", "W-W-H-W-W-W-H"], ["Natural Minor", "W-H-W-W-H-W-W"],
        ]),
    },
    # ---- Survival Skills ----
    "survival-skills-g8-l14": {
        "data_table": table(["Condition", "Warning Signs"], [
            ["Hypothermia", "Shivering, confusion, slurred speech"],
            ["Heat Exhaustion", "Heavy sweating, weakness, nausea"],
        ]),
    },
    "survival-skills-g8-l4": {
        "data_table": table(["Method", "How It Works"], [
            ["Boiling", "Boil for at least 1 minute (3 minutes above 2,000m) to kill pathogens"],
            ["Water filter", "Physically removes bacteria and parasites"],
            ["Purification tablets", "Chemically disinfect water"],
        ]),
    },
    # ---- General Knowledge ----
    "general-knowledge-g8-l14": {
        "data_table": table(["Nobel Prize Category", "Field"], [
            ["Physics", "Science"], ["Chemistry", "Science"], ["Physiology or Medicine", "Science"],
            ["Literature", "Writing"], ["Peace", "International peace efforts"],
            ["Economic Sciences", "Added 1968, in memory of Alfred Nobel"],
        ]),
    },
    "general-knowledge-g8-l16": {
        "data_table": table(["Category", "Example"], [
            ["Ancient Wonder (only survivor)", "Great Pyramid of Giza"],
            ["New Seven Wonder (2007 poll)", "Taj Mahal, India"],
        ]),
    },
    # ---- Cooking ----
    "cooking-g8-l11": {
        "data_table": table(["Herb/Spice", "Common Use"], [
            ["Basil", "Italian dishes, pesto"], ["Cumin", "Indian and Mexican dishes"],
            ["Cinnamon", "Baking, sweet dishes"],
        ]),
    },
    "cooking-g8-l7": {
        "data_table": table(["Method", "Temperature"], [
            ["Boiling", "100C / 212F"], ["Simmering", "85-95C / 185-205F"],
        ]),
    },
    # ---- Foreign Languages ----
    "foreign-languages-g8-l3": {
        "data_table": table(["Verb", "Use"], [
            ["Ser", "Permanent characteristics (e.g. Soy alto = I am tall)"],
            ["Estar", "Temporary states/location (e.g. Estoy cansado = I am tired)"],
        ]),
    },
    "foreign-languages-g8-l9": {
        "data_table": table(["Number", "French"], [
            ["1", "un"], ["2", "deux"], ["3", "trois"], ["4", "quatre"], ["5", "cinq"],
            ["6", "six"], ["7", "sept"], ["8", "huit"], ["9", "neuf"], ["10", "dix"],
        ]),
    },
    # ---- Social Studies ----
    "social-studies-g8-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"],
            ["Started after", "Assassination of Archduke Franz Ferdinand, June 1914"],
            ["Ended by", "Armistice of 11 November 1918"],
        ]),
    },
    "social-studies-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1939-1945"],
            ["Started when", "Germany invaded Poland, September 1939"],
            ["Ended in Europe", "V-E Day, May 8, 1945"],
        ]),
    },
    # ---- Physical Education & Self-Defense ----
    "physical-education-self-defense-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Average resting heart rate (adult)", "60-100 beats per minute"],
            ["Max heart rate estimate", "220 minus your age (a common formula)"],
        ]),
    },
    "physical-education-self-defense-g8-l10": {
        "data_table": table(["Badminton Term", "Meaning"], [
            ["Shuttlecock", "The object hit over the net"],
            ["Rally", "Continuous play until a point is scored"],
            ["Match play", "Best of 3 games to 21 points"],
        ]),
    },
    # ---- Economics ----
    "economics-g8-l6": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price tends to rise"],
            ["Low demand, high supply", "Price tends to fall"],
        ]),
    },
    "economics-g8-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Inflation", "General rise in prices over time"], ["Deflation", "General fall in prices over time"],
        ]),
    },
    # ---- Finance ----
    "fin-g8-l1": {
        "data_table": table(["Category", "Recommended % of Income (50/30/20 rule)"], [
            ["Needs", "50%"], ["Wants", "30%"], ["Savings / Debt Repayment", "20%"],
        ]),
    },
    "finance-g8-l9": {
        "data_table": table(["FICO Credit Score Range", "Rating"], [
            ["800-850", "Exceptional"], ["740-799", "Very Good"], ["670-739", "Good"],
            ["580-669", "Fair"], ["300-579", "Poor"],
        ]),
    },
    # ---- First Aid ----
    "first-aid-g8-l7": {
        "data_table": table(["CPR Step", "Action"], [
            ["1", "Check responsiveness and call for emergency help"],
            ["2", "Give 30 chest compressions (about 2 inches deep)"],
            ["3", "Give 2 rescue breaths (if trained)"],
            ["4", "Repeat the 30:2 ratio until help arrives"],
        ]),
    },
    "first-aid-g8-l19": {
        "data_table": table(["Condition", "Warning Signs"], [
            ["Heat Exhaustion", "Heavy sweating, weakness, nausea"],
            ["Heat Stroke", "High body temperature, hot/dry skin, confusion (a medical emergency)"],
        ]),
    },
    # ---- Physics ----
    "physics-g8-l4": {
        "formulae": ["Speed = Distance / Time"],
        "data_table": table(["Distance", "Time", "Speed"], [
            ["100m", "10s", "10 m/s"], ["200m", "20s", "10 m/s"],
        ]),
    },
    "physics-g8-l16": {
        "formulae": ["KE = 1/2 x m x v^2", "PE = m x g x h"],
        "data_table": table(["Energy Type", "Formula"], [
            ["Kinetic", "1/2 x m x v^2"], ["Gravitational Potential", "m x g x h"],
        ]),
    },
    # ---- Chemistry ----
    "chemistry-g8-l11": {
        "data_table": table(["pH Range", "Type", "Example"], [
            ["0-6", "Acidic", "Lemon juice (~2)"], ["7", "Neutral", "Pure water"],
            ["8-14", "Basic (alkaline)", "Baking soda (~9)"],
        ]),
    },
    "chemistry-g8-l18": {
        "data_table": table(["Particle", "Charge", "Location"], [
            ["Proton", "Positive", "Nucleus"], ["Neutron", "Neutral", "Nucleus"],
            ["Electron", "Negative", "Orbiting the nucleus"],
        ]),
    },
    # ---- Biology ----
    "biology-g8-l6": {
        "data_table": table(["Mitosis Phase", "What Happens"], [
            ["Prophase", "Chromosomes condense and become visible"],
            ["Metaphase", "Chromosomes line up at the cell's center"],
            ["Anaphase", "Chromosomes are pulled to opposite ends"],
            ["Telophase", "Two new nuclei form"],
        ]),
    },
    "biology-g8-l7": {
        "formulae": ["6CO2 + 6H2O + light energy -> C6H12O6 + 6O2"],
        "data_table": table(["Input", "Output"], [
            ["Carbon dioxide + Water + Light", "Glucose + Oxygen"],
        ]),
    },
    # ---- Philosophy ----
    "philosophy-g8-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Plato"], ["Found in", "The Republic, Book VII"],
            ["Main idea", "Prisoners mistake shadows for reality until freed to see the truth"],
        ]),
    },
    "philosophy-g8-l14": {
        "data_table": table(["Philosopher", "Key Idea"], [
            ["Jeremy Bentham", "Founder of utilitarianism; the 'greatest happiness principle'"],
            ["John Stuart Mill", "Refined utilitarianism; distinguished higher and lower pleasures"],
        ]),
    },
    # ---- Critical Thinking ----
    "critical-thinking-g8-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Confirmation bias", "The tendency to favor information that confirms existing beliefs"],
        ]),
    },
    "ct-g8-l1": {
        "data_table": table(["Logical Fallacy", "Description"], [
            ["Ad Hominem", "Attacking the person instead of the argument"],
            ["Straw Man", "Misrepresenting someone's argument to attack it easily"],
            ["Slippery Slope", "Claiming one step will lead to extreme consequences without evidence"],
        ]),
    },
    # ---- Health Education ----
    "hlt-g8-l3": {
        "data_table": table(["Food Group", "Examples"], [
            ["Fruits", "Apples, bananas, berries"], ["Vegetables", "Carrots, broccoli, spinach"],
            ["Grains", "Bread, rice, pasta"], ["Protein", "Chicken, beans, eggs"], ["Dairy", "Milk, cheese, yogurt"],
        ]),
    },
    "health-education-g8-l14": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    # ---- ICT & Computer Science ----
    "ict-computer-science-g8-l20": {
        "data_table": table(["Malware Type", "Description"], [
            ["Virus", "Attaches to files and spreads when the file is run"],
            ["Worm", "Spreads automatically across networks"],
            ["Trojan", "Disguised as legitimate software"],
        ]),
    },
    "ict-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial Intelligence", "Machines performing tasks that normally require human intelligence"],
            ["Machine Learning", "A subset of AI where systems learn patterns from data"],
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
        raise SystemExit(f"Lesson ids not found in grade8.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Grade 8 lessons (all subjects).")


if __name__ == "__main__":
    main()
