#!/usr/bin/env python3
"""Depth pass, Grade 3 Health Education: fill in real, hand-checked
data_table content for the 18 Grade 3 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 3 Health
Education to full 20/20 coverage.

Content covers standard, uncontroversial health/safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "he-g3-l1": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"], ["Dairy", "Milk, cheese"],
        ]),
    },
    "hlt-g3-l3": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"], ["Sugar content", "How much sugar is in the food"],
        ]),
    },
    "hlt-g3-l4": {
        "data_table": table(["Feeling", "Example Trigger"], [
            ["Happy", "Playing with friends"], ["Frustrated", "Losing a game"],
        ]),
    },
    "hlt-g3-l5": {
        "data_table": table(["Injury", "Prevention"], [
            ["Fall", "Wear proper shoes, watch your footing"], ["Cut", "Handle sharp objects carefully"],
        ]),
    },
    "hlt-g3-l6": {
        "data_table": table(["Hygiene Habit", "Frequency"], [
            ["Brushing teeth", "Twice daily"], ["Bathing", "Daily"],
        ]),
    },
    "health-education-g3-l7": {
        "data_table": table(["Way Germs Spread", "Example"], [
            ["Touching", "Shaking hands with a sick person"], ["Coughing/sneezing", "Droplets in the air"],
        ]),
    },
    "health-education-g3-l8": {
        "data_table": table(["When to Wash Hands", "Why"], [
            ["Before eating", "Removes germs before they enter your body"],
            ["After sneezing/coughing", "Removes germs from hands"],
        ]),
    },
    "health-education-g3-l9": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["School age (6-12 years)", "9-12 hours"], ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g3-l10": {
        "data_table": table(["Exercise Benefit", "Example"], [
            ["Stronger heart", "Running, swimming"], ["Stronger muscles", "Climbing, jumping"],
        ]),
    },
    "health-education-g3-l12": {
        "data_table": table(["Snack Type", "Example"], [
            ["Healthy snack", "Apple slices, carrots, yogurt"], ["Occasional treat", "Candy, soda"],
        ]),
    },
    "health-education-g3-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
            ["General guidance", "Drink water throughout the day, more when active"],
        ]),
    },
    "health-education-g3-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Allergy", "When the body reacts strongly to something harmless"],
            ["Allergic reaction", "Symptoms like sneezing, rash, or swelling"],
        ]),
    },
    "health-education-g3-l15": {
        "data_table": table(["Visit", "How Often (General Guideline)"], [
            ["Doctor check-up", "Once a year"], ["Dentist check-up", "Every 6 months"],
        ]),
    },
    "health-education-g3-l16": {
        "data_table": table(["Activity Type", "Example"], [
            ["Screen time", "Watching videos, playing games"], ["Offline time", "Playing outside, reading a book"],
        ]),
    },
    "health-education-g3-l17": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Talking to a trusted adult", "Helps process feelings"],
        ]),
    },
    "health-education-g3-l18": {
        "data_table": table(["Friendship Quality", "Example"], [
            ["Kindness", "Sharing and helping"], ["Trust", "Keeping promises"],
        ]),
    },
    "health-education-g3-l19": {
        "data_table": table(["Rule", "Why"], [
            ["Only take medicine given by a trusted adult", "Prevents accidental overdose"],
            ["Never share medicine", "Different medicines suit different people"],
        ]),
    },
    "health-education-g3-l20": {
        "data_table": table(["Growth Fact", "Detail"], [
            ["Growth spurts", "Periods of faster physical growth"],
            ["Everyone grows differently", "Growth timing varies from person to person"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Health Education lessons (completing 20/20).")


if __name__ == "__main__":
    main()
