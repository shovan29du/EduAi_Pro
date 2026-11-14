#!/usr/bin/env python3
"""Depth pass, Grade 2 Social Studies: fill in real, hand-checked
data_table content for the 18 Grade 2 Social Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 2 Social Studies to full
20/20 coverage.

Content covers general, age-appropriate social/civic/economic concepts
with concrete examples -- nothing fabricated or presented as fact when
it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "social-studies-g2-l2": {
        "data_table": table(["Tradition Type", "Example"], [
            ["Holiday tradition", "Special foods at celebrations"],
            ["Family tradition", "A weekly family game night"],
        ]),
    },
    "social-studies-g2-l3": {
        "data_table": table(["Rule", "Why It Matters"], [
            ["Raise your hand before speaking", "Keeps the classroom orderly"],
            ["Wait your turn in line", "Fair to everyone"],
        ]),
    },
    "social-studies-g2-l4": {
        "data_table": table(["Good Citizen Habit", "Example"], [
            ["Following rules", "Waiting your turn in line"], ["Helping others", "Picking up litter"],
        ]),
    },
    "social-studies-g2-l5": {
        "data_table": table(["Helper", "Role"], [
            ["Police officer", "Keeps the neighborhood safe"],
            ["Firefighter", "Responds to fires and emergencies"],
        ]),
    },
    "social-studies-g2-l7": {
        "data_table": table(["Role", "Example"], [
            ["Producer", "A farmer who grows wheat"],
            ["Consumer", "A person who buys bread at the store"],
        ]),
    },
    "social-studies-g2-l8": {
        "data_table": table(["Then", "Now"], [
            ["Sending letters by mail", "Sending text messages"],
            ["Washing clothes by hand", "Using a washing machine"],
        ]),
    },
    "social-studies-g2-l9": {
        "data_table": table(["Festival", "Country/Region"], [
            ["Diwali", "India"], ["Chinese New Year", "China"], ["Christmas", "Celebrated worldwide"],
        ]),
    },
    "social-studies-g2-l10": {
        "data_table": table(["Cooperation Example", "Benefit"], [
            ["Cleaning up together", "Finishes faster"],
            ["Building a puzzle together", "Combines everyone's ideas"],
        ]),
    },
    "social-studies-g2-l11": {
        "data_table": table(["Situation", "Fair Response"], [
            ["Splitting a snack", "Give equal portions"], ["Taking turns", "Everyone gets a turn on the swing"],
        ]),
    },
    "social-studies-g2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing an option to show your opinion"],
            ["Majority", "The option with the most votes wins"],
        ]),
    },
    "social-studies-g2-l13": {
        "data_table": table(["Job", "What They Do"], [
            ["Baker", "Bakes bread and cakes"], ["Mail carrier", "Delivers letters and packages"],
        ]),
    },
    "social-studies-g2-l14": {
        "data_table": table(["Common Map Symbol", "Typical Meaning"], [
            ["Blue line", "River or stream"], ["Green area", "Park or forest"],
            ["Red square", "School or important building"], ["Black line", "Road"],
        ]),
    },
    "social-studies-g2-l15": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["Anthem", "A country's official patriotic song"],
        ]),
    },
    "social-studies-g2-l16": {
        "data_table": table(["Way We Differ", "Example"], [
            ["Appearance", "Hair color, height, skin tone"], ["Culture", "Languages, foods, traditions"],
        ]),
    },
    "social-studies-g2-l17": {
        "data_table": table(["Choice", "Example"], [
            ["Saving", "Putting money in a piggy bank for later"],
            ["Spending", "Buying something you need now"],
        ]),
    },
    "social-studies-g2-l18": {
        "data_table": table(["Step", "Description"], [
            ["1. Produce", "A farmer grows crops"], ["2. Transport", "Goods are shipped to stores"],
            ["3. Sell", "Stores sell goods to customers"],
        ]),
    },
    "social-studies-g2-l19": {
        "data_table": table(["Responsibility", "Example"], [
            ["At home", "Cleaning up your toys"], ["At school", "Turning in homework on time"],
        ]),
    },
    "social-studies-g2-l20": {
        "data_table": table(["Step", "Action"], [
            ["1", "Stay calm"], ["2", "Talk about the problem"], ["3", "Find a fair solution together"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Social Studies lessons (completing 20/20).")


if __name__ == "__main__":
    main()
