#!/usr/bin/env python3
"""Depth pass, Grade 10 Health Education: fill in real, hand-checked
data_table content for the Grade 10 Health Education lessons not
covered by the earlier breadth-first batch. Brings Grade 10 Health
Education to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_health_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hlt-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Reproductive health", "Physical and emotional wellbeing related to reproduction"],
        ]),
    },
    "hlt-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Public health", "Efforts to protect and improve the health of populations"],
        ]),
    },
    "hlt-g10-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Family planning", "Deciding the timing and spacing of children using informed choices"],
        ]),
    },
    "hlt-g10-l4": {
        "data_table": table(["Skill", "Purpose"], [
            ["Mental health first aid", "Initial support offered to someone experiencing a mental health crisis"],
        ]),
    },
    "hlt-g10-l5": {
        "data_table": table(["Career", "Focus"], [
            ["Nurse", "Direct patient care"], ["Epidemiologist", "Studies disease patterns in populations"],
        ]),
    },
    "hlt-g10-l6": {
        "data_table": table(["Issue", "Example"], [
            ["Access to clean water", "A major global health challenge"],
        ]),
    },
    "health-education-g10-l8": {
        "data_table": table(["Nutrient Group", "Example"], [
            ["Macronutrients", "Carbohydrates, proteins, fats"], ["Micronutrients", "Vitamins and minerals"],
        ]),
    },
    "health-education-g10-l9": {
        "data_table": table(["Label Element", "Meaning"], [
            ["% Daily Value", "How much a nutrient contributes to a daily diet"],
        ]),
    },
    "health-education-g10-l10": {
        "data_table": table(["Effect", "Detail"], [
            ["Regular physical activity", "Improves cardiovascular health and mood"],
        ]),
    },
    "health-education-g10-l12": {
        "data_table": table(["Technique", "Purpose"], [
            ["Deep breathing", "Reduces physical stress response"],
        ]),
    },
    "health-education-g10-l13": {
        "data_table": table(["Effect", "Detail"], [
            ["Impaired judgment", "A short-term effect of alcohol use"],
        ]),
    },
    "health-education-g10-l14": {
        "data_table": table(["Effect", "Detail"], [
            ["Nicotine addiction", "A risk of both tobacco and vaping"],
        ]),
    },
    "health-education-g10-l15": {
        "data_table": table(["Effect", "Detail"], [
            ["Illicit drug use", "Can impair brain development, especially in teens"],
        ]),
    },
    "health-education-g10-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Addiction", "A compulsive need to use a substance despite harm"],
        ]),
    },
    "health-education-g10-l17": {
        "data_table": table(["Factor", "Effect"], [
            ["Social media comparison", "Can negatively affect body image"],
        ]),
    },
    "health-education-g10-l18": {
        "data_table": table(["Disorder", "Description"], [
            ["Anorexia nervosa", "Severe restriction of food intake"], ["Bulimia nervosa", "Cycles of binge eating and purging"],
        ]),
    },
    "health-education-g10-l19": {
        "data_table": table(["Practice", "Reason"], [
            ["Regular bathing and handwashing", "Prevents illness and infection"],
        ]),
    },
    "health-education-g10-l20": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Immunization", "Builds immunity to prevent disease"],
        ]),
    },
    "health-education-g10-l21": {
        "data_table": table(["Transmission Route", "Example"], [
            ["Airborne", "Influenza"], ["Waterborne", "Cholera"],
        ]),
    },
    "health-education-g10-l22": {
        "data_table": table(["Type", "Example"], [
            ["Non-communicable disease", "Not spread person-to-person, e.g. diabetes"],
        ]),
    },
    "health-education-g10-l23": {
        "data_table": table(["Type", "Description"], [
            ["Type 1 diabetes", "Body doesn't produce insulin"], ["Type 2 diabetes", "Body doesn't use insulin effectively"],
        ]),
    },
    "health-education-g10-l24": {
        "data_table": table(["Habit", "Benefit"], [
            ["Regular exercise", "Strengthens the heart and improves circulation"],
        ]),
    },
    "health-education-g10-l25": {
        "data_table": table(["Practice", "Benefit"], [
            ["Regular screenings", "Enables early cancer detection"],
        ]),
    },
    "health-education-g10-l26": {
        "data_table": table(["Quality", "Reason"], [
            ["Mutual respect", "A cornerstone of healthy relationships"],
        ]),
    },
    "health-education-g10-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Consent", "Clear, voluntary agreement, given without pressure"],
        ]),
    },
    "health-education-g10-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Puberty", "Triggered by hormonal changes leading to physical maturity"],
        ]),
    },
    "health-education-g10-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["STIs", "Infections spread mainly through sexual contact, many preventable"],
        ]),
    },
    "health-education-g10-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Contraception", "Methods used to prevent pregnancy, vary in effectiveness"],
        ]),
    },
    "health-education-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Consent", "Clear, voluntary agreement in a relationship"],
        ]),
    },
    "health-education-g10-l32": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Reporting to a trusted adult", "Recommended response to bullying"],
        ]),
    },
    "health-education-g10-l33": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Assertiveness", "Helps resist unwanted peer pressure"],
        ]),
    },
    "health-education-g10-l34": {
        "data_table": table(["Condition", "Note"], [
            ["Anxiety", "Excessive, persistent worry"], ["Depression", "Persistent low mood and loss of interest"],
        ]),
    },
    "health-education-g10-l35": {
        "data_table": table(["Trait", "Benefit"], [
            ["Resilience", "Helps a person recover from setbacks"],
        ]),
    },
    "health-education-g10-l36": {
        "data_table": table(["Stage", "Common Reaction"], [
            ["Grief", "A natural response to loss, unique to each person"],
        ]),
    },
    "health-education-g10-l37": {
        "data_table": table(["Practice", "Reason"], [
            ["Setting screen time limits", "Supports digital wellbeing"],
        ]),
    },
    "health-education-g10-l38": {
        "data_table": table(["Practice", "Reason"], [
            ["Report and block", "Recommended response to cyberbullying"],
        ]),
    },
    "health-education-g10-l39": {
        "data_table": table(["Step", "Purpose"], [
            ["Raising awareness", "First step in health advocacy"],
        ]),
    },
    "health-education-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Health insurance", "A financial plan that helps cover medical costs"],
        ]),
    },
    "health-education-g10-l41": {
        "data_table": table(["Factor", "Effect"], [
            ["Air pollution", "Linked to respiratory illness"],
        ]),
    },
    "health-education-g10-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Food allergy", "An immune response to a specific food, can be severe"],
        ]),
    },
    "health-education-g10-l43": {
        "data_table": table(["Habit", "Benefit"], [
            ["Balanced diet and exercise", "Supports lifelong wellness"],
        ]),
    },
    "health-education-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Healthcare system", "The organizations, people, and resources that deliver health services"],
        ]),
    },
    "health-education-g10-l45": {
        "data_table": table(["Resource", "Purpose"], [
            ["Community health clinic", "Provides accessible care"],
        ]),
    },
    "health-education-g10-l46": {
        "data_table": table(["Skill", "Purpose"], [
            ["Preparing questions in advance", "Improves communication during a doctor visit"],
        ]),
    },
    "health-education-g10-l47": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Pacing activities", "Helps manage chronic pain"],
        ]),
    },
    "health-education-g10-l48": {
        "data_table": table(["Life Stage", "Health Focus"], [
            ["Adolescence", "Puberty and reproductive development"], ["Adulthood", "Ongoing reproductive health maintenance"],
        ]),
    },
    "health-education-g10-l49": {
        "data_table": table(["Practice", "Benefit"], [
            ["Regular checkups", "Supports early disease prevention and detection"],
        ]),
    },
    "health-education-g10-l50": {
        "data_table": table(["Element", "Purpose"], [
            ["Specific, measurable goal", "Makes health goals achievable"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Health Education: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Health Education lessons (completing 50/50).")


if __name__ == "__main__":
    main()
