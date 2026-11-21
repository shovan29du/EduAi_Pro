#!/usr/bin/env python3
"""Depth pass, Grade 1 Health Education: fill in real, hand-checked
data_table content for the 17 Grade 1 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 1 Health
Education to full 20/20 coverage.

Content covers standard, uncontroversial health/safety guidance (the
"Stop, Drop, and Roll" fire-safety technique, the 20-second handwashing
guideline, real doctor/dentist check-up frequency) -- nothing fabricated
or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hlt-g1-l1": {
        "data_table": table(["Habit", "Benefit"], [
            ["Washing hands", "Removes germs"], ["Sleeping enough", "Helps your body and brain rest"],
        ]),
    },
    "hlt-g1-l2": {
        "data_table": table(["Step", "Action"], [
            ["1", "Wet hands with water"], ["2", "Add soap and scrub for 20 seconds"], ["3", "Rinse and dry"],
        ]),
    },
    "hlt-g1-l4": {
        "data_table": table(["Food", "Nutrient Benefit"], [
            ["Carrots", "Vitamin A, good for eyes"], ["Oranges", "Vitamin C, helps fight illness"],
        ]),
    },
    "hlt-g1-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Wear sunscreen", "Protects skin from sunburn"], ["Stay with an adult", "Keeps you safe"],
        ]),
    },
    "health-education-g1-l7": {
        "data_table": table(["Feeling", "What It Might Look Like"], [
            ["Happy", "Smiling, laughing"], ["Frustrated", "Furrowed brow, clenched fists"],
        ]),
    },
    "health-education-g1-l8": {
        "data_table": table(["Body Care", "Example"], [
            ["Hygiene", "Bathing and brushing teeth"], ["Nutrition", "Eating balanced meals"],
        ]),
    },
    "health-education-g1-l9": {
        "data_table": table(["Snack Type", "Example"], [
            ["Healthy snack", "Apple slices, carrots, yogurt"], ["Sugary treat", "Candy, soda (occasional treat)"],
        ]),
    },
    "health-education-g1-l11": {
        "data_table": table(["Weather", "What to Wear"], [
            ["Cold", "Coat, hat, gloves"], ["Hot", "Light clothing, sun hat"], ["Rainy", "Raincoat, boots"],
        ]),
    },
    "health-education-g1-l12": {
        "data_table": table(["Visit", "How Often (General Guideline)"], [
            ["Doctor check-up", "Once a year"], ["Dentist check-up", "Every 6 months"],
        ]),
    },
    "health-education-g1-l13": {
        "data_table": table(["Way Germs Spread", "Example"], [
            ["Touching", "Shaking hands with a sick person"], ["Coughing/sneezing", "Droplets in the air"],
        ]),
    },
    "health-education-g1-l14": {
        "data_table": table(["Correct Way", "Why"], [
            ["Cough/sneeze into your elbow", "Stops germs from spreading to hands"],
            ["Wash hands after", "Removes any remaining germs"],
        ]),
    },
    "health-education-g1-l15": {
        "data_table": table(["Activity", "Benefit"], [
            ["Running", "Strengthens the heart"], ["Stretching", "Improves flexibility"],
        ]),
    },
    "health-education-g1-l16": {
        "data_table": table(["Touch Type", "Example"], [
            ["Safe touch", "A hug from a parent, a high-five"],
            ["Unsafe touch", "Any touch that makes you feel uncomfortable or scared"],
        ]),
    },
    "health-education-g1-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Stop, Look, Listen", "Before crossing the street"], ["Use crosswalks", "Safer place to cross"],
        ]),
    },
    "health-education-g1-l18": {
        "data_table": table(["Step", "Action"], [
            ["Stop", "Stop what you're doing"], ["Drop", "Drop to the ground"],
            ["Roll", "Roll to put out flames if clothes catch fire"],
        ]),
    },
    "health-education-g1-l19": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Talking to a trusted adult", "Helps process feelings"],
        ]),
    },
    "health-education-g1-l20": {
        "data_table": table(["Activity", "Benefit"], [
            ["Quiet reading time", "Calms the mind"], ["Napping", "Restores energy"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Health Education lessons (completing 20/20).")


if __name__ == "__main__":
    main()
