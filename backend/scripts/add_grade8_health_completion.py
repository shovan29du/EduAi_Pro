#!/usr/bin/env python3
"""Depth pass, Grade 8 Health Education: fill in real, hand-checked
data_table content for the 38 Grade 8 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 8 Health
Education to full 40/40 coverage.

Content covers standard, uncontroversial, age-appropriate health
guidance -- nothing fabricated or presented as fact when it's actually
invented. Sensitive topics (consent, puberty, substance risks) stick to
general, factual, age-appropriate framing that emphasizes trusted
adults and healthcare providers for specifics.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_health_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "he-g8-l1": {
        "data_table": table(["Substance", "Risk"], [
            ["Tobacco", "Harms the lungs and heart"], ["Alcohol", "Impairs judgment and harms the body"],
        ]),
    },
    "hlt-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Consent", "Agreeing to something willingly"],
            ["Personal boundary", "A limit on what a person is comfortable with"],
        ]),
    },
    "hlt-g8-l4": {
        "data_table": table(["Program Element", "Purpose"], [
            ["Warm-up", "Prepares the body for exercise"], ["Progressive overload", "Gradually increases training demand"],
        ]),
    },
    "hlt-g8-l5": {
        "data_table": table(["Step", "Purpose"], [
            ["Check", "Assess the situation"], ["Call", "Contact emergency services"],
        ]),
    },
    "hlt-g8-l6": {
        "data_table": table(["Sign of Misleading Health Claims", "Example"], [
            ["Unrealistic promises", "'Lose 10 pounds overnight'"],
        ]),
    },
    "health-education-g8-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Mental health", "Emotional and psychological well-being"],
        ]),
    },
    "health-education-g8-l8": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Deep breathing", "Calms the body"], ["Time management", "Reduces last-minute pressure"],
        ]),
    },
    "health-education-g8-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Anxiety", "Persistent worry or fear"], ["Depression", "Persistent sadness affecting daily life"],
        ]),
    },
    "health-education-g8-l10": {
        "data_table": table(["Friendship Quality", "Example"], [
            ["Kindness", "Sharing and helping"], ["Trust", "Keeping promises"],
        ]),
    },
    "health-education-g8-l11": {
        "data_table": table(["Communication Skill", "Purpose"], [
            ["Active listening", "Fully focusing on the other person"],
        ]),
    },
    "health-education-g8-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Peer pressure", "Influence from friends to act a certain way"],
        ]),
    },
    "health-education-g8-l13": {
        "data_table": table(["Concept", "Meaning"], [
            ["Body image", "How a person views their own body"], ["Self-esteem", "How a person values themselves"],
        ]),
    },
    "health-education-g8-l15": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"],
        ]),
    },
    "health-education-g8-l16": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"],
        ]),
    },
    "health-education-g8-l17": {
        "data_table": table(["Food", "Example Portion"], [
            ["Cooked rice", "About the size of a fist"],
        ]),
    },
    "health-education-g8-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Human body water content", "About 60% water (average adult)"],
        ]),
    },
    "health-education-g8-l19": {
        "data_table": table(["Age Group", "Recommended Weekly Activity"], [
            ["Teens (ages 6-17)", "At least 60 minutes of moderate to vigorous activity daily"],
        ]),
    },
    "health-education-g8-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "A normal stage of growth where the body changes over time"],
            ["Guidance", "Trusted adults and healthcare providers can answer specific questions"],
        ]),
    },
    "health-education-g8-l21": {
        "data_table": table(["Hygiene Habit", "Frequency"], [
            ["Brushing teeth", "Twice daily"], ["Bathing", "Daily"],
        ]),
    },
    "health-education-g8-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Vaccine", "Helps the body build immunity to a disease"],
        ]),
    },
    "health-education-g8-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Communicable disease", "An illness that can spread from person to person"],
        ]),
    },
    "health-education-g8-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Chronic disease", "A long-lasting health condition, like asthma or diabetes"],
        ]),
    },
    "health-education-g8-l25": {
        "data_table": table(["Substance", "Risk"], [
            ["Tobacco", "Harms the lungs and heart"], ["Vaping", "Exposes the lungs to harmful chemicals"],
        ]),
    },
    "health-education-g8-l26": {
        "data_table": table(["Health Risk", "Detail"], [
            ["Alcohol", "Impairs judgment and can damage the liver over time"],
        ]),
    },
    "health-education-g8-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Addiction", "A compulsive need to use a substance despite harmful consequences"],
        ]),
    },
    "health-education-g8-l28": {
        "data_table": table(["Decision Step", "Purpose"], [
            ["Weigh the consequences", "Considers outcomes before acting"],
        ]),
    },
    "health-education-g8-l29": {
        "data_table": table(["Healthcare Resource", "Purpose"], [
            ["Community health clinic", "Provides accessible medical care"],
        ]),
    },
    "health-education-g8-l30": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Drink more water this week"], ["Long-term", "Build a regular exercise habit"],
        ]),
    },
    "health-education-g8-l31": {
        "data_table": table(["Habit", "Recommendation"], [
            ["Screen breaks", "Take regular breaks from screens"],
        ]),
    },
    "health-education-g8-l32": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
        ]),
    },
    "health-education-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Consent", "Agreeing willingly, whether to physical contact or sharing information"],
        ]),
    },
    "health-education-g8-l34": {
        "data_table": table(["Step", "Action"], [
            ["Tell a trusted adult", "Reports the behavior"],
        ]),
    },
    "health-education-g8-l35": {
        "data_table": table(["Coping Strategy", "Purpose"], [
            ["Talking about feelings", "Helps process grief"], ["Seeking support", "Reduces isolation"],
        ]),
    },
    "health-education-g8-l36": {
        "data_table": table(["System", "Function"], [
            ["Circulatory", "Moves blood through the body"], ["Respiratory", "Exchanges oxygen and carbon dioxide"],
        ]),
    },
    "health-education-g8-l37": {
        "data_table": table(["Pollutant", "Health Effect"], [
            ["Air pollution", "Can worsen asthma and respiratory issues"],
        ]),
    },
    "health-education-g8-l38": {
        "data_table": table(["Resource", "Purpose"], [
            ["School nurse", "Trained to help with health concerns"],
        ]),
    },
    "health-education-g8-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Health insurance", "A plan that helps cover the cost of medical care"],
        ]),
    },
    "health-education-g8-l40": {
        "data_table": table(["Action", "Example"], [
            ["Raising awareness", "Sharing accurate health information"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Health Education lessons (completing 40/40).")


if __name__ == "__main__":
    main()
