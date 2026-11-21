#!/usr/bin/env python3
"""Depth pass, Grade 4 Social Studies: fill in real, hand-checked
data_table content for the 28 Grade 4 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 4 Social
Studies to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g4-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Government", "An organization that makes and enforces laws"],
            ["Citizenship", "Being a legally recognized member of a country"],
        ]),
    },
    "social-studies-g4-l2": {
        "data_table": table(["Helper", "Role"], [
            ["Firefighter", "Puts out fires, rescues people"], ["Doctor", "Treats illness and injury"],
        ]),
    },
    "social-studies-g4-l3": {
        "data_table": table(["Concept", "Example"], [
            ["Right", "The right to an education"], ["Responsibility", "Following school rules"],
        ]),
    },
    "social-studies-g4-l5": {
        "data_table": table(["Step", "Description"], [
            ["Proposal", "A law idea is introduced"], ["Vote", "Lawmakers vote on it"],
            ["Signing", "The leader signs it into law"],
        ]),
    },
    "social-studies-g4-l6": {
        "data_table": table(["Term", "Example"], [
            ["Need", "Food, water, shelter"], ["Want", "A toy, video game"],
        ]),
    },
    "social-studies-g4-l7": {
        "data_table": table(["Term", "Example"], [
            ["Goods", "Physical items like food or clothing"], ["Services", "Actions like haircuts or teaching"],
        ]),
    },
    "social-studies-g4-l9": {
        "data_table": table(["Concept", "Meaning"], [
            ["Saving", "Setting aside money for later"], ["Spending", "Using money to buy things now"],
        ]),
    },
    "social-studies-g4-l10": {
        "data_table": table(["Map Type", "Shows"], [
            ["Neighborhood map", "Streets and nearby buildings"], ["City map", "The layout of a whole city"],
        ]),
    },
    "social-studies-g4-l11": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Traditional dishes"],
        ]),
    },
    "social-studies-g4-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Immigration", "Moving to a new country to live"], ["Migration", "Moving from one place to another"],
        ]),
    },
    "social-studies-g4-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing a leader or decision by ballot"], ["Election", "The process of voting"],
        ]),
    },
    "social-studies-g4-l14": {
        "data_table": table(["Landmark", "Significance"], [
            ["Capitol building", "Where government meets"], ["War memorial", "Honors those who served"],
        ]),
    },
    "social-studies-g4-l15": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Listening to both sides", "Understanding different views"], ["Compromise", "Finding a shared solution"],
        ]),
    },
    "social-studies-g4-l16": {
        "data_table": table(["Example of Volunteering", "Benefit"], [
            ["Community clean-up", "A cleaner neighborhood"], ["Food bank help", "Supports families in need"],
        ]),
    },
    "social-studies-g4-l17": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["National anthem", "A patriotic song"],
        ]),
    },
    "social-studies-g4-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Family tree", "A diagram showing family relationships across generations"],
        ]),
    },
    "social-studies-g4-l19": {
        "data_table": table(["Community Type", "Feature"], [
            ["Rural", "Farms, open land"], ["Suburban", "Houses near a city"], ["Urban", "Tall buildings, dense population"],
        ]),
    },
    "social-studies-g4-l20": {
        "data_table": table(["Concept", "Example"], [
            ["Global citizenship", "Caring about issues beyond your own country"],
            ["Cooperation", "Countries working together on shared goals"],
        ]),
    },
    "social-studies-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Understanding local news", "Recognizing the mayor's role"],
        ]),
    },
    "social-studies-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Community events", "Thanking a local firefighter or nurse"],
        ]),
    },
    "social-studies-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["School rules", "Understanding both rights and responsibilities as a student"],
        ]),
    },
    "social-studies-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Following local rules", "Understanding a city ordinance"],
        ]),
    },
    "social-studies-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["School rule changes", "Understanding how a new rule gets proposed and approved"],
        ]),
    },
    "social-studies-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Family budgeting", "Choosing needs over wants when money is limited"],
        ]),
    },
    "social-studies-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Shopping", "Understanding you're paying for a good or a service"],
        ]),
    },
    "social-studies-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Popular toy shortage", "Understanding why prices rise when supply is low"],
        ]),
    },
    "social-studies-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Allowance", "Saving part of it instead of spending it all"],
        ]),
    },
    "social-studies-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["New neighborhood", "Using a map to find your way around"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Social Studies lessons (completing 30/30).")


if __name__ == "__main__":
    main()
