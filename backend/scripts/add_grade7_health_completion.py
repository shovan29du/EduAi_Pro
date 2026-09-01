#!/usr/bin/env python3
"""Depth pass, Grade 7 Health Education: fill in real, hand-checked
data_table content for the 38 Grade 7 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 7 Health
Education to full 40/40 coverage.

Content covers standard, uncontroversial, age-appropriate health
guidance -- nothing fabricated or presented as fact when it's actually
invented. Sensitive topics (reproductive health, puberty, substance
risks) stick to general, factual, age-appropriate framing that
emphasizes trusted adults and healthcare providers for specifics.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hlt-g7-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Mental health", "Emotional and psychological well-being"],
        ]),
    },
    "hlt-g7-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A stage of physical growth and change"],
            ["Guidance", "Trusted adults and healthcare providers can answer specific questions"],
        ]),
    },
    "hlt-g7-l3": {
        "data_table": table(["Substance", "Risk"], [
            ["Tobacco", "Harms the lungs and heart"], ["Alcohol", "Impairs judgment and harms the body"],
        ]),
    },
    "hlt-g7-l4": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Talking to a trusted adult", "Helps process feelings"],
        ]),
    },
    "hlt-g7-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Chronic disease", "A long-lasting health condition, like asthma or diabetes"],
        ]),
    },
    "hlt-g7-l6": {
        "data_table": table(["Communication Skill", "Purpose"], [
            ["Active listening", "Fully focusing on the other person"], ["Expressing needs clearly", "Reduces misunderstandings"],
        ]),
    },
    "health-education-g7-l7": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"], ["Dairy", "Milk, cheese"],
        ]),
    },
    "health-education-g7-l8": {
        "data_table": table(["Age Group", "Recommended Weekly Activity"], [
            ["Teens (ages 6-17)", "At least 60 minutes of moderate to vigorous activity daily"],
        ]),
    },
    "health-education-g7-l10": {
        "data_table": table(["Hygiene Habit", "Frequency"], [
            ["Brushing teeth", "Twice daily"], ["Bathing", "Daily"],
        ]),
    },
    "health-education-g7-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A normal stage of growth where the body changes over time"],
            ["Timing", "Varies from person to person"],
        ]),
    },
    "health-education-g7-l13": {
        "data_table": table(["Way Germs Spread", "Example"], [
            ["Touching", "Shaking hands with a sick person"], ["Coughing/sneezing", "Droplets in the air"],
        ]),
    },
    "health-education-g7-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Vaccine", "Helps the body build immunity to a disease"],
        ]),
    },
    "health-education-g7-l15": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Recognize and neutralize pathogens"],
        ]),
    },
    "health-education-g7-l16": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Time management", "Reduces last-minute pressure"], ["Physical activity", "Releases tension"],
        ]),
    },
    "health-education-g7-l17": {
        "data_table": table(["Habit", "Recommendation"], [
            ["Screen breaks", "Take regular breaks from screens"],
            ["Balance", "Combine screen time with physical activity"],
        ]),
    },
    "health-education-g7-l18": {
        "data_table": table(["Concept", "Meaning"], [
            ["Body image", "How a person views their own body"], ["Self-esteem", "How a person values themselves"],
        ]),
    },
    "health-education-g7-l19": {
        "data_table": table(["Step", "Action"], [
            ["Tell a trusted adult", "Reports the behavior"], ["Support the person being bullied", "Reduces isolation"],
        ]),
    },
    "health-education-g7-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Peer pressure", "Influence from friends to act a certain way"],
            ["Healthy response", "Making your own informed choices"],
        ]),
    },
    "health-education-g7-l21": {
        "data_table": table(["Decision Step", "Purpose"], [
            ["Weigh the consequences", "Considers outcomes before acting"], ["Ask a trusted adult", "Gets outside perspective"],
        ]),
    },
    "health-education-g7-l22": {
        "data_table": table(["Sign of Misleading Advertising", "Example"], [
            ["Unrealistic promises", "'Lose 10 pounds overnight'"],
            ["No credible sourcing", "Claims without scientific backing"],
        ]),
    },
    "health-education-g7-l23": {
        "data_table": table(["Pollutant", "Health Effect"], [
            ["Air pollution", "Can worsen asthma and respiratory issues"],
        ]),
    },
    "health-education-g7-l24": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Small cut", "Clean it and cover with a bandage"], ["Sprain", "Rest, ice, compression, elevation"],
        ]),
    },
    "health-education-g7-l25": {
        "data_table": table(["Rule", "Why"], [
            ["Only take medicine given by a trusted adult", "Prevents accidental overdose"],
            ["Follow the recommended dosage", "Prevents harm"],
        ]),
    },
    "health-education-g7-l26": {
        "data_table": table(["Health Risk", "Detail"], [
            ["Alcohol", "Impairs judgment and can damage the liver over time"],
        ]),
    },
    "health-education-g7-l27": {
        "data_table": table(["Substance", "Risk"], [
            ["Tobacco", "Harms the lungs and heart"], ["Vaping", "Exposes the lungs to harmful chemicals"],
        ]),
    },
    "health-education-g7-l28": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"], ["Sugar content", "How much sugar is in the food"],
        ]),
    },
    "health-education-g7-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
        ]),
    },
    "health-education-g7-l30": {
        "data_table": table(["Budget Tip", "Benefit"], [
            ["Buying seasonal produce", "Often cheaper and fresher"], ["Cooking in bulk", "Saves money and time"],
        ]),
    },
    "health-education-g7-l31": {
        "data_table": table(["Action", "Effect"], [
            ["Talking openly about mental health", "Reduces stigma"], ["Supporting a friend", "Encourages them to seek help"],
        ]),
    },
    "health-education-g7-l32": {
        "data_table": table(["Skill", "Meaning"], [
            ["Self-awareness", "Recognizing your own emotions"], ["Empathy", "Understanding others' feelings"],
        ]),
    },
    "health-education-g7-l33": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Drink more water this week"], ["Long-term", "Build a regular exercise habit"],
        ]),
    },
    "health-education-g7-l34": {
        "data_table": table(["Resource", "Purpose"], [
            ["Community health clinic", "Provides accessible medical care"], ["School counselor", "Supports emotional well-being"],
        ]),
    },
    "health-education-g7-l35": {
        "data_table": table(["Issue", "Detail"], [
            ["Access to clean water", "A major global health challenge"],
            ["Access to vaccines", "Varies significantly by region"],
        ]),
    },
    "health-education-g7-l36": {
        "data_table": table(["System", "Function"], [
            ["Circulatory", "Moves blood through the body"], ["Respiratory", "Exchanges oxygen and carbon dioxide"],
        ]),
    },
    "health-education-g7-l37": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"],
            ["Look both ways before crossing", "Checks for oncoming traffic"],
        ]),
    },
    "health-education-g7-l38": {
        "data_table": table(["Age Group", "CDC-Recommended Sleep"], [
            ["Teens (13-18 years)", "8-10 hours"],
        ]),
    },
    "health-education-g7-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Allergy", "When the body reacts strongly to something harmless"],
        ]),
    },
    "health-education-g7-l40": {
        "data_table": table(["Friendship Quality", "Example"], [
            ["Kindness", "Sharing and helping"], ["Trust", "Keeping promises"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Health Education lessons (completing 40/40).")


if __name__ == "__main__":
    main()
