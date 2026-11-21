#!/usr/bin/env python3
"""Depth pass, Grade 6 Health Education: fill in real, hand-checked
data_table content for the 28 Grade 6 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 6 Health
Education to full 30/30 coverage.

Content covers standard, uncontroversial, age-appropriate health
guidance -- nothing fabricated or presented as fact when it's actually
invented. Sensitive topics (puberty, consent, substance risks) stick to
general, factual, age-appropriate framing that emphasizes trusted
adults and healthcare providers for specifics.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "he-g6-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Mental health", "Emotional and psychological well-being"],
        ]),
    },
    "hlt-g6-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A stage of physical growth and change"], ["Timing", "Varies from person to person"],
        ]),
    },
    "hlt-g6-l4": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Talking to a trusted adult", "Helps process feelings"],
        ]),
    },
    "hlt-g6-l5": {
        "data_table": table(["Concept", "Meaning"], [
            ["Risk", "The chance of a negative outcome"], ["Safe decision-making", "Weighing consequences before acting"],
        ]),
    },
    "hlt-g6-l6": {
        "data_table": table(["Skill", "Purpose"], [
            ["Basic first aid", "Provides initial care for injuries"], ["CPR awareness", "Understanding when and how it's used"],
        ]),
    },
    "health-education-g6-l7": {
        "data_table": table(["Hygiene Habit", "Frequency"], [
            ["Brushing teeth", "Twice daily"], ["Bathing", "Daily"],
        ]),
    },
    "health-education-g6-l9": {
        "data_table": table(["Way Germs Spread", "Example"], [
            ["Touching", "Shaking hands with a sick person"], ["Coughing/sneezing", "Droplets in the air"],
        ]),
    },
    "health-education-g6-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Vaccine", "Helps the body build immunity to a disease"],
        ]),
    },
    "health-education-g6-l11": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["School age (6-12 years)", "9-12 hours"], ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g6-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A normal stage of growth where the body changes over time"],
            ["Guidance", "Trusted adults and healthcare providers can answer specific questions"],
        ]),
    },
    "health-education-g6-l13": {
        "data_table": table(["Organ", "Function"], [
            ["Stomach", "Breaks down food with acid"], ["Small intestine", "Absorbs nutrients"],
        ]),
    },
    "health-education-g6-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
            ["General guidance", "Drink water throughout the day, more when active"],
        ]),
    },
    "health-education-g6-l15": {
        "data_table": table(["Habit", "Recommendation"], [
            ["Screen breaks", "Take regular breaks from screens"],
            ["Balance", "Combine screen time with physical activity"],
        ]),
    },
    "health-education-g6-l16": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Naming the emotion", "Helps process it"], ["Taking a break", "Provides space to calm down"],
        ]),
    },
    "health-education-g6-l17": {
        "data_table": table(["Friendship Quality", "Example"], [
            ["Kindness", "Sharing and helping"], ["Trust", "Keeping promises"],
        ]),
    },
    "health-education-g6-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Peer pressure", "Influence from friends to act a certain way"],
            ["Healthy response", "Making your own informed choices"],
        ]),
    },
    "health-education-g6-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Consent", "Agreeing to something willingly"],
            ["Personal boundary", "A limit on what a person is comfortable with"],
        ]),
    },
    "health-education-g6-l20": {
        "data_table": table(["Substance", "Risk"], [
            ["Tobacco", "Harms the lungs and heart"], ["Alcohol", "Impairs judgment and harms the body"],
        ]),
    },
    "health-education-g6-l21": {
        "data_table": table(["Rule", "Why"], [
            ["Only take medicine given by a trusted adult", "Prevents accidental overdose"],
            ["Never share medicine", "Different medicines suit different people"],
        ]),
    },
    "health-education-g6-l22": {
        "data_table": table(["Guideline", "Recommendation"], [
            ["Brush teeth", "Twice daily"], ["Dentist visit", "Every 6 months"],
        ]),
    },
    "health-education-g6-l23": {
        "data_table": table(["Check-up", "Purpose"], [
            ["Vision test", "Detects eyesight problems early"], ["Hearing test", "Detects hearing loss early"],
        ]),
    },
    "health-education-g6-l24": {
        "data_table": table(["Concept", "Meaning"], [
            ["Body image", "How a person views their own body"], ["Self-esteem", "How a person values themselves"],
        ]),
    },
    "health-education-g6-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Allergy", "When the body reacts strongly to something harmless"],
            ["Allergic reaction", "Symptoms like sneezing, rash, or swelling"],
        ]),
    },
    "health-education-g6-l26": {
        "data_table": table(["Pollutant", "Health Effect"], [
            ["Air pollution", "Can worsen asthma and respiratory issues"], ["Water pollution", "Can spread illness"],
        ]),
    },
    "health-education-g6-l27": {
        "data_table": table(["Hazard", "Prevention"], [
            ["Loose rugs", "Secure them to prevent trips"], ["Exposed wires", "Keep them covered and tidy"],
        ]),
    },
    "health-education-g6-l28": {
        "data_table": table(["Concept", "Meaning"], [
            ["Disability", "A condition that affects one or more major life activities"],
            ["Inclusion", "Ensuring everyone can fully participate"],
        ]),
    },
    "health-education-g6-l29": {
        "data_table": table(["Communication Skill", "Purpose"], [
            ["Active listening", "Fully focusing on the other person"], ["Expressing needs clearly", "Reduces misunderstandings"],
        ]),
    },
    "health-education-g6-l30": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Drink more water this week"], ["Long-term", "Build a regular exercise habit"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Health Education lessons (completing 30/30).")


if __name__ == "__main__":
    main()
