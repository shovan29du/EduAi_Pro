#!/usr/bin/env python3
"""Depth pass, Grade 6 Social Studies: fill in real, hand-checked
data_table content for the 28 Grade 6 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 6 Social
Studies to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g6-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "social-studies-g6-l2": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Citizens vote for leaders"], ["Monarchy", "Rule by a king or queen"],
        ]),
    },
    "social-studies-g6-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Democracy", "A system where citizens vote for leaders"], ["Citizenship", "Legal membership in a country"],
        ]),
    },
    "social-studies-g6-l5": {
        "data_table": table(["Concept", "Example"], [
            ["Right", "The right to vote"], ["Responsibility", "Following the law"],
        ]),
    },
    "social-studies-g6-l6": {
        "data_table": table(["Level", "Example Responsibility"], [
            ["Local", "City services like trash collection"], ["National", "Defense and foreign policy"],
        ]),
    },
    "social-studies-g6-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing a leader or decision by ballot"], ["Election", "The process of voting"],
        ]),
    },
    "social-studies-g6-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Law", "A rule enforced by government"], ["Justice system", "Courts that interpret and apply laws"],
        ]),
    },
    "social-studies-g6-l10": {
        "data_table": table(["Term", "Example"], [
            ["Need", "Food, water, shelter"], ["Want", "A toy, video game"],
        ]),
    },
    "social-studies-g6-l11": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price rises"], ["Low demand, high supply", "Price falls"],
        ]),
    },
    "social-studies-g6-l12": {
        "data_table": table(["Term", "Example"], [
            ["Goods", "Physical items like food or clothing"], ["Services", "Actions like haircuts or teaching"],
        ]),
    },
    "social-studies-g6-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Bank", "An institution that holds and manages money"], ["Interest", "Money earned or paid for using a loan or savings"],
        ]),
    },
    "social-studies-g6-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Tax", "Money collected by government to fund public services"],
        ]),
    },
    "social-studies-g6-l15": {
        "data_table": table(["Role", "Example"], [
            ["Producer", "A farmer growing crops"], ["Consumer", "A shopper buying groceries"],
        ]),
    },
    "social-studies-g6-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Interdependence", "Countries relying on each other for goods and resources"],
        ]),
    },
    "social-studies-g6-l17": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Traditional dishes"],
        ]),
    },
    "social-studies-g6-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Immigration", "Moving to a new country to live"],
        ]),
    },
    "social-studies-g6-l19": {
        "data_table": table(["Institution", "Role"], [
            ["Public library", "Provides free access to books and resources"], ["Public school", "Provides education"],
        ]),
    },
    "social-studies-g6-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Media literacy", "The ability to evaluate and understand media messages"],
        ]),
    },
    "social-studies-g6-l21": {
        "data_table": table(["Example of Volunteering", "Benefit"], [
            ["Community clean-up", "A cleaner neighborhood"], ["Food bank help", "Supports families in need"],
        ]),
    },
    "social-studies-g6-l22": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Listening to both sides", "Understanding different views"], ["Compromise", "Finding a shared solution"],
        ]),
    },
    "social-studies-g6-l23": {
        "data_table": table(["Movement", "Known For"], [
            ["Civil rights movement", "Fighting for racial equality in the US"],
            ["Suffrage movement", "Fighting for women's right to vote"],
        ]),
    },
    "social-studies-g6-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Poverty", "Lacking sufficient resources for basic needs"], ["Inequality", "Uneven distribution of resources or opportunity"],
        ]),
    },
    "social-studies-g6-l25": {
        "data_table": table(["Community Type", "Feature"], [
            ["Urban", "Densely populated, tall buildings"], ["Rural", "Farms, open land"],
        ]),
    },
    "social-studies-g6-l26": {
        "data_table": table(["Family Structure", "Description"], [
            ["Nuclear family", "Parents and children living together"], ["Extended family", "Includes grandparents, aunts, uncles"],
        ]),
    },
    "social-studies-g6-l27": {
        "data_table": table(["Career", "Example Role"], [
            ["Teacher", "Educates students"], ["Engineer", "Designs and builds systems"],
        ]),
    },
    "social-studies-g6-l28": {
        "data_table": table(["Social Institution", "Purpose"], [
            ["Family", "Provides care and socialization"], ["Education", "Provides knowledge and skills"],
        ]),
    },
    "social-studies-g6-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "social-studies-g6-l30": {
        "data_table": table(["Goal", "Focus"], [
            ["No Poverty", "Ending poverty worldwide"], ["Quality Education", "Ensuring inclusive education for all"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Social Studies lessons (completing 30/30).")


if __name__ == "__main__":
    main()
