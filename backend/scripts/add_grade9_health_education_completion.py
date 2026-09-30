#!/usr/bin/env python3
"""Depth pass, Grade 9 Health Education: fill in real, hand-checked
data_table content for the 48 Grade 9 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 9 Health
Education to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_health_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "he-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Consent", "Clear, voluntary agreement, given without pressure"],
        ]),
    },
    "hlt-g9-l2": {
        "data_table": table(["Dimension", "Focus"], [
            ["Physical health", "The body"], ["Mental health", "Thoughts and emotions"],
        ]),
    },
    "hlt-g9-l3": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Immunization", "Builds immunity to prevent disease"], ["Handwashing", "Reduces the spread of germs"],
        ]),
    },
    "hlt-g9-l4": {
        "data_table": table(["Condition", "Note"], [
            ["Anxiety disorder", "Excessive, persistent worry"], ["Depression", "Persistent low mood and loss of interest"],
        ]),
    },
    "hlt-g9-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Addiction", "A compulsive need to use a substance or engage in a behavior despite harm"],
        ]),
    },
    "hlt-g9-l6": {
        "data_table": table(["Skill", "Purpose"], [
            ["Reading health claims critically", "Avoids being misled by unverified products"],
        ]),
    },
    "health-education-g9-l7": {
        "data_table": table(["Dimension", "Example"], [
            ["Physical", "Exercise and nutrition"], ["Mental", "Emotional wellbeing"], ["Social", "Healthy relationships"],
        ]),
    },
    "health-education-g9-l9": {
        "data_table": table(["Label Element", "Meaning"], [
            ["% Daily Value", "How much a nutrient contributes to a daily diet"],
        ]),
    },
    "health-education-g9-l10": {
        "data_table": table(["Practice", "Benefit"], [
            ["Eating a variety of foods", "Ensures balanced nutrient intake"],
        ]),
    },
    "health-education-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Dehydration signs", "Thirst, dark urine, fatigue"],
        ]),
    },
    "health-education-g9-l13": {
        "data_table": table(["Practice", "Benefit"], [
            ["Consistent sleep schedule", "Improves sleep quality"],
        ]),
    },
    "health-education-g9-l14": {
        "data_table": table(["Guideline", "Detail"], [
            ["Teens", "Recommended at least 60 minutes of physical activity daily"],
        ]),
    },
    "health-education-g9-l15": {
        "data_table": table(["Factor", "Effect"], [
            ["Social media comparison", "Can negatively affect body image"],
        ]),
    },
    "health-education-g9-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "Triggered by hormonal changes leading to physical maturity"],
        ]),
    },
    "health-education-g9-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Menstrual cycle", "Typically around 28 days, varies by individual"],
        ]),
    },
    "health-education-g9-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Reproductive health", "Encompasses physical and emotional wellbeing related to reproduction"],
        ]),
    },
    "health-education-g9-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Contraception", "Methods used to prevent pregnancy, vary in effectiveness"],
        ]),
    },
    "health-education-g9-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["STIs", "Infections spread mainly through sexual contact, many preventable"],
        ]),
    },
    "health-education-g9-l21": {
        "data_table": table(["Quality", "Reason"], [
            ["Mutual respect", "A cornerstone of healthy relationships"],
        ]),
    },
    "health-education-g9-l22": {
        "data_table": table(["Skill", "Benefit"], [
            ["Active listening", "Builds trust and understanding"],
        ]),
    },
    "health-education-g9-l23": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Assertiveness", "Helps resist unwanted peer pressure"],
        ]),
    },
    "health-education-g9-l24": {
        "data_table": table(["Technique", "Purpose"], [
            ["Deep breathing", "Reduces physical stress response"],
        ]),
    },
    "health-education-g9-l25": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Grounding techniques", "Helps manage anxiety in the moment"],
        ]),
    },
    "health-education-g9-l26": {
        "data_table": table(["Symptom", "Detail"], [
            ["Persistent sadness", "A common symptom of depression"],
        ]),
    },
    "health-education-g9-l27": {
        "data_table": table(["Warning Sign", "Action"], [
            ["Talking about hopelessness", "Take seriously and seek help immediately"],
        ]),
    },
    "health-education-g9-l28": {
        "data_table": table(["Trait", "Benefit"], [
            ["Resilience", "Helps a person recover from setbacks"],
        ]),
    },
    "health-education-g9-l29": {
        "data_table": table(["Practice", "Benefit"], [
            ["Mindfulness", "Reduces stress and improves focus"],
        ]),
    },
    "health-education-g9-l30": {
        "data_table": table(["Effect", "Detail"], [
            ["Impaired judgment", "A short-term effect of alcohol use"],
        ]),
    },
    "health-education-g9-l31": {
        "data_table": table(["Effect", "Detail"], [
            ["Nicotine addiction", "A risk of both tobacco and vaping"],
        ]),
    },
    "health-education-g9-l32": {
        "data_table": table(["Effect", "Detail"], [
            ["Drug use", "Can impair brain development, especially in teens"],
        ]),
    },
    "health-education-g9-l33": {
        "data_table": table(["Step", "Purpose"], [
            ["Seeking professional support", "A key part of addiction recovery"],
        ]),
    },
    "health-education-g9-l34": {
        "data_table": table(["Practice", "Reason"], [
            ["Wearing protective gear", "Reduces injury risk"],
        ]),
    },
    "health-education-g9-l35": {
        "data_table": table(["Practice", "Reason"], [
            ["Using crosswalks", "Reduces pedestrian accident risk"],
        ]),
    },
    "health-education-g9-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Setting screen time limits", "Supports digital wellbeing"],
        ]),
    },
    "health-education-g9-l37": {
        "data_table": table(["Effect", "Detail"], [
            ["Excess screen time", "Linked to disrupted sleep and reduced physical activity"],
        ]),
    },
    "health-education-g9-l38": {
        "data_table": table(["Practice", "Reason"], [
            ["Regular bathing and handwashing", "Prevents illness and infection"],
        ]),
    },
    "health-education-g9-l39": {
        "data_table": table(["Practice", "Reason"], [
            ["Brushing twice daily", "Prevents cavities and gum disease"],
        ]),
    },
    "health-education-g9-l40": {
        "data_table": table(["Practice", "Reason"], [
            ["Wearing sunscreen", "Reduces skin cancer risk"],
        ]),
    },
    "health-education-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Chronic disease", "A long-lasting condition, often manageable but not curable"],
        ]),
    },
    "health-education-g9-l42": {
        "data_table": table(["Type", "Description"], [
            ["Type 1 diabetes", "Body doesn't produce insulin"], ["Type 2 diabetes", "Body doesn't use insulin effectively"],
        ]),
    },
    "health-education-g9-l43": {
        "data_table": table(["Habit", "Benefit"], [
            ["Regular exercise", "Strengthens the heart and improves circulation"],
        ]),
    },
    "health-education-g9-l44": {
        "data_table": table(["Practice", "Benefit"], [
            ["Regular screenings", "Enables early cancer detection"],
        ]),
    },
    "health-education-g9-l45": {
        "data_table": table(["Factor", "Effect"], [
            ["Air pollution", "Linked to respiratory illness"],
        ]),
    },
    "health-education-g9-l46": {
        "data_table": table(["Resource", "Purpose"], [
            ["Community health clinic", "Provides accessible care"],
        ]),
    },
    "health-education-g9-l47": {
        "data_table": table(["Step", "Purpose"], [
            ["Consider consequences", "Improves the quality of health decisions"],
        ]),
    },
    "health-education-g9-l48": {
        "data_table": table(["Element", "Purpose"], [
            ["Specific, measurable goal", "Makes health goals achievable"],
        ]),
    },
    "health-education-g9-l49": {
        "data_table": table(["Fact", "Detail"], [
            ["Food allergy", "An immune response to a specific food, can be severe"],
        ]),
    },
    "health-education-g9-l50": {
        "data_table": table(["Disorder", "Description"], [
            ["Anorexia nervosa", "Severe restriction of food intake"], ["Bulimia nervosa", "Cycles of binge eating and purging"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Health Education lessons (completing 50/50).")


if __name__ == "__main__":
    main()
