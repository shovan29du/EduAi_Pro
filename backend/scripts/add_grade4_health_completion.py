#!/usr/bin/env python3
"""Depth pass, Grade 4 Health Education: fill in real, hand-checked
data_table content for the 28 Grade 4 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 4 Health
Education to full 30/30 coverage.

Content covers standard, uncontroversial, age-appropriate health
guidance -- nothing fabricated or presented as fact when it's actually
invented. Puberty/reproductive-health lessons stick to general,
factual, age-appropriate framing (body changes happen; consult trusted
adults and healthcare providers for specifics).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hlt-g4-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A stage of physical growth and change"],
            ["Timing", "Varies from person to person"],
        ]),
    },
    "hlt-g4-l3": {
        "data_table": table(["Habit", "Recommendation"], [
            ["Screen breaks", "Take regular breaks from screens"],
            ["Balance", "Combine screen time with physical activity"],
        ]),
    },
    "hlt-g4-l4": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Small cut", "Clean it and cover with a bandage"], ["Bruise", "Apply a cold pack"],
        ]),
    },
    "hlt-g4-l5": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Talking to a trusted adult", "Helps process feelings"],
        ]),
    },
    "hlt-g4-l6": {
        "data_table": table(["Sun Safety Tip", "Why"], [
            ["Wear sunscreen", "Protects skin from UV rays"], ["Wear a hat", "Shades your face and head"],
        ]),
    },
    "health-education-g4-l7": {
        "data_table": table(["Hygiene Habit", "Frequency"], [
            ["Brushing teeth", "Twice daily"], ["Bathing", "Daily"],
        ]),
    },
    "health-education-g4-l8": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice daily"], ["Dentist visit", "Every 6 months"],
        ]),
    },
    "health-education-g4-l10": {
        "data_table": table(["Way Germs Spread", "Example"], [
            ["Touching", "Shaking hands with a sick person"], ["Coughing/sneezing", "Droplets in the air"],
        ]),
    },
    "health-education-g4-l11": {
        "data_table": table(["When to Wash Hands", "Why"], [
            ["Before eating", "Removes germs before they enter your body"],
            ["After using the bathroom", "Removes germs from hands"],
        ]),
    },
    "health-education-g4-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Vaccine", "Helps the body build immunity to a disease"],
            ["Immunity", "The body's ability to fight off a specific illness"],
        ]),
    },
    "health-education-g4-l13": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"], ["Sugar content", "How much sugar is in the food"],
        ]),
    },
    "health-education-g4-l14": {
        "data_table": table(["Exercise Benefit", "Example"], [
            ["Stronger heart", "Running, swimming"], ["Stronger muscles", "Climbing, jumping"],
        ]),
    },
    "health-education-g4-l15": {
        "data_table": table(["Feeling", "Healthy Way to Express It"], [
            ["Frustration", "Talking about it calmly"], ["Sadness", "Sharing with a trusted person"],
        ]),
    },
    "health-education-g4-l16": {
        "data_table": table(["Body System", "Function"], [
            ["Skeletal system", "Supports and protects the body"], ["Digestive system", "Breaks down food for energy"],
        ]),
    },
    "health-education-g4-l17": {
        "data_table": table(["Rule", "Why"], [
            ["Only take medicine given by a trusted adult", "Prevents accidental overdose"],
            ["Never share medicine", "Different medicines suit different people"],
        ]),
    },
    "health-education-g4-l18": {
        "data_table": table(["Rule", "Why"], [
            ["Never accept unknown substances", "Protects against harm"],
            ["Tell a trusted adult if offered something unsafe", "Keeps you safe"],
        ]),
    },
    "health-education-g4-l19": {
        "data_table": table(["Friendship Quality", "Example"], [
            ["Kindness", "Sharing and helping"], ["Trust", "Keeping promises"],
        ]),
    },
    "health-education-g4-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Allergy", "When the body reacts strongly to something harmless"],
            ["Allergic reaction", "Symptoms like sneezing, rash, or swelling"],
        ]),
    },
    "health-education-g4-l21": {
        "data_table": table(["Skill", "Real-World Use"], [
            ["Reading a nutrition label", "Choosing a healthier snack at the store"],
        ]),
    },
    "health-education-g4-l22": {
        "data_table": table(["Skill", "Real-World Use"], [
            ["Balanced plate planning", "Building a healthy dinner plate"],
        ]),
    },
    "health-education-g4-l23": {
        "data_table": table(["Skill", "Real-World Use"], [
            ["Tracking activity", "Noticing how much daily movement you get"],
        ]),
    },
    "health-education-g4-l24": {
        "data_table": table(["Skill", "Real-World Use"], [
            ["Sleep routine", "Setting a consistent bedtime"],
        ]),
    },
    "health-education-g4-l25": {
        "data_table": table(["Skill", "Real-World Use"], [
            ["Naming feelings", "Describing an emotion accurately to a trusted adult"],
        ]),
    },
    "health-education-g4-l26": {
        "data_table": table(["Skill", "Real-World Use"], [
            ["Coping strategy", "Using deep breathing before a test"],
        ]),
    },
    "health-education-g4-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A normal stage of growth where the body changes over time"],
            ["Guidance", "Trusted adults and healthcare providers can answer specific questions"],
        ]),
    },
    "health-education-g4-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Communicable disease", "An illness that can spread from person to person, like a cold"],
        ]),
    },
    "health-education-g4-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Noncommunicable disease", "An illness that does not spread between people, like asthma"],
        ]),
    },
    "health-education-g4-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Medicine", "A substance used to treat illness, given under adult/medical guidance"],
            ["Vaccine", "Helps prevent illness by building immunity"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Health Education lessons (completing 30/30).")


if __name__ == "__main__":
    main()
