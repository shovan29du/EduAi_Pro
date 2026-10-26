#!/usr/bin/env python3
"""Depth pass, Grade 3 Social Studies: fill in real, hand-checked
data_table content for the 18 Grade 3 Social Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 3 Social Studies to
full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g3-l1": {
        "data_table": table(["Skill", "Purpose"], [
            ["Reading a map key", "Understanding what symbols mean"], ["Using a compass", "Finding direction"],
        ]),
    },
    "social-studies-g3-l2": {
        "data_table": table(["Community Feature", "Example"], [
            ["Shared spaces", "Parks, libraries"], ["Shared rules", "Laws everyone follows"],
        ]),
    },
    "social-studies-g3-l4": {
        "data_table": table(["Concept", "Example"], [
            ["Right", "The right to an education"], ["Responsibility", "Following school rules"],
        ]),
    },
    "social-studies-g3-l5": {
        "data_table": table(["Local Government Role", "Example"], [
            ["Mayor", "Leads a city or town"], ["City council", "Makes local decisions and laws"],
        ]),
    },
    "social-studies-g3-l6": {
        "data_table": table(["Term", "Example"], [
            ["Goods", "Physical items like food or clothing"], ["Services", "Actions like haircuts or teaching"],
        ]),
    },
    "social-studies-g3-l7": {
        "data_table": table(["Term", "Example"], [
            ["Need", "Food, water, shelter"], ["Want", "A toy, video game"],
        ]),
    },
    "social-studies-g3-l9": {
        "data_table": table(["Job", "What They Do"], [
            ["Teacher", "Educates students"], ["Police officer", "Keeps the community safe"],
        ]),
    },
    "social-studies-g3-l10": {
        "data_table": table(["Tradition", "Example"], [
            ["Holiday celebration", "Family gatherings, special foods"], ["Cultural dress", "Traditional clothing worn on special occasions"],
        ]),
    },
    "social-studies-g3-l11": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Different traditional dishes"],
        ]),
    },
    "social-studies-g3-l12": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flag", "Represents a country's identity"], ["National anthem", "A patriotic song representing a nation"],
        ]),
    },
    "social-studies-g3-l13": {
        "data_table": table(["Good Citizen Trait", "Example"], [
            ["Following rules", "Obeying laws"], ["Helping others", "Volunteering in the community"],
        ]),
    },
    "social-studies-g3-l14": {
        "data_table": table(["Then", "Now"], [
            ["Letters sent by mail", "Instant messages and email"], ["Horse and carriage", "Cars and buses"],
        ]),
    },
    "social-studies-g3-l15": {
        "data_table": table(["Community Type", "Feature"], [
            ["Rural", "Farms, open land"], ["Suburban", "Houses near a city"], ["Urban", "Tall buildings, dense population"],
        ]),
    },
    "social-studies-g3-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing a leader or decision by ballot"], ["Election", "The process of voting"],
        ]),
    },
    "social-studies-g3-l17": {
        "data_table": table(["Landmark", "Significance"], [
            ["Town hall", "Where local government meets"], ["War memorial", "Honors those who served"],
        ]),
    },
    "social-studies-g3-l18": {
        "data_table": table(["Example of Teamwork", "Benefit"], [
            ["Community clean-up", "A cleaner neighborhood"], ["Group project", "Shared workload and ideas"],
        ]),
    },
    "social-studies-g3-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Immigration", "Moving to a new country to live"], ["Immigrant", "A person who moves to a new country"],
        ]),
    },
    "social-studies-g3-l20": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Listening to both sides", "Understanding different views"], ["Compromise", "Finding a solution both agree on"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Social Studies lessons (completing 20/20).")


if __name__ == "__main__":
    main()
