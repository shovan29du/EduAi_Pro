#!/usr/bin/env python3
"""Depth pass, Grade 2 Health Education: fill in real, hand-checked
data_table content for the 18 Grade 2 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 2 Health
Education to full 20/20 coverage.

Content covers standard, uncontroversial health/safety guidance -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hlt-g2-l2": {
        "data_table": table(["Way Germs Spread", "Example"], [
            ["Touching", "Shaking hands with a sick person"], ["Coughing/sneezing", "Droplets in the air"],
        ]),
    },
    "he-g2-l1": {
        "data_table": table(["Habit", "Benefit"], [
            ["Washing hands", "Removes germs"], ["Sleeping enough", "Helps your body and brain rest"],
        ]),
    },
    "hlt-g2-l4": {
        "data_table": table(["Exercise Benefit", "Example"], [
            ["Stronger heart", "Running, swimming"], ["Stronger muscles", "Climbing, jumping"],
        ]),
    },
    "hlt-g2-l5": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice daily"], ["Floss", "Once daily"], ["Dentist visit", "Every 6 months"],
        ]),
    },
    "hlt-g2-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Only take medicine given by a trusted adult", "Prevents accidental overdose"],
            ["Never share medicine", "Different medicines suit different people"],
        ]),
    },
    "health-education-g2-l7": {
        "data_table": table(["When to Wash Hands", "Why"], [
            ["Before eating", "Removes germs before they enter your body"],
            ["After using the bathroom", "Removes germs from hands"],
        ]),
    },
    "health-education-g2-l8": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Preschool (3-5 years)", "10-13 hours"], ["School age (6-12 years)", "9-12 hours"],
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g2-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
            ["General guidance", "Drink water throughout the day, more when active"],
        ]),
    },
    "health-education-g2-l10": {
        "data_table": table(["Snack Type", "Example"], [
            ["Healthy snack", "Apple slices, carrots, yogurt"], ["Sugary treat", "Candy, soda (occasional treat)"],
        ]),
    },
    "health-education-g2-l11": {
        "data_table": table(["Feeling", "What It Might Look Like"], [
            ["Happy", "Smiling, laughing"], ["Frustrated", "Furrowed brow, clenched fists"],
        ]),
    },
    "health-education-g2-l12": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Talking to a trusted adult", "Helps process feelings"],
        ]),
    },
    "health-education-g2-l13": {
        "data_table": table(["Body Care", "Example"], [
            ["Hygiene", "Bathing and brushing teeth"], ["Nutrition", "Eating balanced meals"],
        ]),
    },
    "health-education-g2-l14": {
        "data_table": table(["Sun Safety Tip", "Why"], [
            ["Wear sunscreen", "Protects skin from UV rays"], ["Wear a hat", "Shades your face and head"],
        ]),
    },
    "health-education-g2-l15": {
        "data_table": table(["Touch Type", "Example"], [
            ["Safe touch", "A hug from a parent, a high-five"],
            ["Unsafe touch", "Any touch that makes you feel uncomfortable or scared"],
        ]),
    },
    "health-education-g2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Allergy", "When the body reacts strongly to something harmless, like peanuts or pollen"],
            ["Allergic reaction", "Symptoms like sneezing, rash, or swelling"],
        ]),
    },
    "health-education-g2-l17": {
        "data_table": table(["Visit", "How Often (General Guideline)"], [
            ["Doctor check-up", "Once a year"], ["Dentist check-up", "Every 6 months"],
        ]),
    },
    "health-education-g2-l18": {
        "data_table": table(["Rule", "Why"], [
            ["Don't go anywhere with a stranger", "Keeps you safe"],
            ["Tell a trusted adult if a stranger approaches", "Helps adults protect you"],
        ]),
    },
    "health-education-g2-l19": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Small cut", "Clean it and cover with a bandage"], ["Bruise", "Apply a cold pack"],
        ]),
    },
    "health-education-g2-l20": {
        "data_table": table(["Activity Type", "Example"], [
            ["Screen time", "Watching videos, playing games"], ["Offline time", "Playing outside, reading a book"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Health Education lessons (completing 20/20).")


if __name__ == "__main__":
    main()
