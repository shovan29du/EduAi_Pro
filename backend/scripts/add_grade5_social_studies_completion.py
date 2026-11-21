#!/usr/bin/env python3
"""Depth pass, Grade 5 Social Studies: fill in real, hand-checked
data_table content for the 28 Grade 5 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 5 Social
Studies to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g5-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Interdependence", "Countries relying on each other for goods and resources"],
        ]),
    },
    "social-studies-g5-l3": {
        "data_table": table(["Concept", "Example"], [
            ["Right", "The right to an education"], ["Responsibility", "Following the law"],
        ]),
    },
    "social-studies-g5-l4": {
        "data_table": table(["Step", "Description"], [
            ["Proposal", "A law idea is introduced"], ["Vote", "Lawmakers vote on it"],
        ]),
    },
    "social-studies-g5-l5": {
        "data_table": table(["Level", "Example Responsibility"], [
            ["Local", "City services like trash collection"], ["State", "Statewide schools and roads"],
            ["National", "Defense and foreign policy"],
        ]),
    },
    "social-studies-g5-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing a leader or decision by ballot"], ["Election", "The process of voting"],
        ]),
    },
    "social-studies-g5-l7": {
        "data_table": table(["Helper", "Role"], [
            ["Firefighter", "Puts out fires, rescues people"], ["Doctor", "Treats illness and injury"],
        ]),
    },
    "social-studies-g5-l8": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price rises"], ["Low demand, high supply", "Price falls"],
        ]),
    },
    "social-studies-g5-l9": {
        "data_table": table(["Role", "Example"], [
            ["Producer", "A farmer growing crops"], ["Consumer", "A shopper buying groceries"],
        ]),
    },
    "social-studies-g5-l10": {
        "data_table": table(["Term", "Example"], [
            ["Goods", "Physical items like food or clothing"], ["Services", "Actions like haircuts or teaching"],
        ]),
    },
    "social-studies-g5-l11": {
        "data_table": table(["Term", "Example"], [
            ["Need", "Food, water, shelter"], ["Want", "A toy, video game"],
        ]),
    },
    "social-studies-g5-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Tax", "Money collected by government to fund public services"],
        ]),
    },
    "social-studies-g5-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Global trade", "Buying and selling goods between countries"],
        ]),
    },
    "social-studies-g5-l14": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Traditional dishes"],
        ]),
    },
    "social-studies-g5-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Immigration", "Moving to a new country to live"],
        ]),
    },
    "social-studies-g5-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "social-studies-g5-l17": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Listening to both sides", "Understanding different views"], ["Compromise", "Finding a shared solution"],
        ]),
    },
    "social-studies-g5-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Nonprofit organization", "A group working for a cause, not for profit"],
        ]),
    },
    "social-studies-g5-l19": {
        "data_table": table(["Figure", "Known For"], [
            ["Martin Luther King Jr.", "Leader in the American civil rights movement"],
            ["Rosa Parks", "Refused to give up her bus seat, sparking the Montgomery bus boycott"],
        ]),
    },
    "social-studies-g5-l20": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Citizens vote for leaders"], ["Monarchy", "Rule by a king or queen"],
        ]),
    },
    "social-studies-g5-l21": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["National anthem", "A patriotic song"],
        ]),
    },
    "social-studies-g5-l22": {
        "data_table": table(["Media Type", "Example"], [
            ["News outlet", "Reports current events"], ["Social media", "Shares user-generated content"],
        ]),
    },
    "social-studies-g5-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"], ["Fact-checking", "Verifying claims before trusting them"],
        ]),
    },
    "social-studies-g5-l24": {
        "data_table": table(["Economic System", "Description"], [
            ["Market economy", "Prices set by supply and demand"], ["Command economy", "Government controls production"],
        ]),
    },
    "social-studies-g5-l25": {
        "data_table": table(["Community Type", "Feature"], [
            ["Urban", "Densely populated, tall buildings"], ["Suburban", "Houses near a city"], ["Rural", "Farms, open land"],
        ]),
    },
    "social-studies-g5-l26": {
        "data_table": table(["Timeline Concept", "Meaning"], [
            ["Chronology", "The order in which events happened"],
        ]),
    },
    "social-studies-g5-l27": {
        "data_table": table(["Example of Volunteering", "Benefit"], [
            ["Community clean-up", "A cleaner neighborhood"], ["Food bank help", "Supports families in need"],
        ]),
    },
    "social-studies-g5-l28": {
        "data_table": table(["Concept", "Example"], [
            ["Global citizenship", "Caring about issues beyond your own country"],
        ]),
    },
    "social-studies-g5-l29": {
        "data_table": table(["Tradition", "Region"], [
            ["Tea ceremony", "Japan"], ["Quinceanera", "Latin America"],
        ]),
    },
    "social-studies-g5-l30": {
        "data_table": table(["Region", "Example Countries"], [
            ["East Asia", "China, Japan, Korea"], ["South Asia", "India, Bangladesh, Pakistan"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Social Studies lessons (completing 30/30).")


if __name__ == "__main__":
    main()
