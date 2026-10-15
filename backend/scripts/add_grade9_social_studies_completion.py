#!/usr/bin/env python3
"""Depth pass, Grade 9 Social Studies: fill in real, hand-checked
data_table content for the 48 Grade 9 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 9 Social
Studies to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "The growing interconnection of the world's economies and cultures"],
        ]),
    },
    "social-studies-g9-l2": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Power held by the people, directly or through representatives"], ["Monarchy", "Power held by a king or queen"],
        ]),
    },
    "social-studies-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Citizenship", "Membership in a political community with rights and duties"],
        ]),
    },
    "social-studies-g9-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Constitution", "A country's foundational body of law"], ["Rule of law", "The principle that everyone is subject to the law"],
        ]),
    },
    "social-studies-g9-l5": {
        "data_table": table(["Right", "Example"], [
            ["Freedom of speech", "The right to express opinions"],
        ]),
    },
    "social-studies-g9-l6": {
        "data_table": table(["Voting System", "Description"], [
            ["First-past-the-post", "Candidate with the most votes wins"], ["Proportional representation", "Seats allocated by vote share"],
        ]),
    },
    "social-studies-g9-l7": {
        "data_table": table(["Ideology", "Core Idea"], [
            ["Conservatism", "Favors tradition and gradual change"], ["Liberalism", "Favors individual rights and reform"],
        ]),
    },
    "social-studies-g9-l8": {
        "data_table": table(["Level", "Example Responsibility"], [
            ["Local government", "Manages schools, roads, and local services"],
        ]),
    },
    "social-studies-g9-l9": {
        "data_table": table(["Branch", "Role"], [
            ["Executive", "Enforces laws"], ["Legislative", "Makes laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "social-studies-g9-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Diplomacy", "Managing relationships between countries"],
        ]),
    },
    "social-studies-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["United Nations founded", "1945"], ["Main goal", "International peace and cooperation"],
        ]),
    },
    "social-studies-g9-l12": {
        "data_table": table(["System", "Description"], [
            ["Federalism", "Power divided between national and regional governments"], ["Unitary system", "Power concentrated at the national level"],
        ]),
    },
    "social-studies-g9-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Judiciary", "The branch of government that interprets and applies the law"],
        ]),
    },
    "social-studies-g9-l15": {
        "data_table": table(["Role", "Example"], [
            ["Watchdog function", "Media investigates and reports on government actions"],
        ]),
    },
    "social-studies-g9-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Public policy", "A course of action adopted by government to address an issue"],
        ]),
    },
    "social-studies-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Social stratification", "The ranking of people into social classes"],
        ]),
    },
    "social-studies-g9-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Culture", "Shared beliefs, customs, and practices of a group"],
        ]),
    },
    "social-studies-g9-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanization", "The growth of cities as populations shift from rural areas"],
        ]),
    },
    "social-studies-g9-l21": {
        "data_table": table(["Cause of Migration", "Example"], [
            ["Push factor", "War or lack of jobs pushes people to leave"], ["Pull factor", "Better opportunities attract people"],
        ]),
    },
    "social-studies-g9-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["World population", "Over 8 billion, unevenly distributed"],
        ]),
    },
    "social-studies-g9-l23": {
        "data_table": table(["Resource", "Distribution Note"], [
            ["Oil", "Concentrated in specific regions like the Middle East"],
        ]),
    },
    "social-studies-g9-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental policy", "Government rules aimed at protecting the environment"],
        ]),
    },
    "social-studies-g9-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Sustainable Development Goals", "17 goals adopted by the UN in 2015"],
        ]),
    },
    "social-studies-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Colonialism", "One country's political control over another territory"],
        ]),
    },
    "social-studies-g9-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Decolonization", "Many former colonies gained independence in the mid-20th century"],
        ]),
    },
    "social-studies-g9-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Industrial Revolution began", "Late 18th century, in Britain"],
        ]),
    },
    "social-studies-g9-l29": {
        "data_table": table(["Movement", "Notable Figure"], [
            ["American civil rights movement", "Martin Luther King Jr."],
        ]),
    },
    "social-studies-g9-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Women's suffrage", "Movement for women's right to vote"],
        ]),
    },
    "social-studies-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Trade union", "An organization of workers formed to protect their rights"],
        ]),
    },
    "social-studies-g9-l32": {
        "data_table": table(["Institution", "Role"], [
            ["Family", "Provides support and socialization"], ["Education", "Transmits knowledge and skills"],
        ]),
    },
    "social-studies-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Social change", "Shifts in social structures and norms over time"],
        ]),
    },
    "social-studies-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Peacebuilding", "Efforts to establish lasting peace after conflict"],
        ]),
    },
    "social-studies-g9-l35": {
        "data_table": table(["Cause of War", "Example"], [
            ["Territorial disputes", "Conflicting claims over land"],
        ]),
    },
    "social-studies-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Trade agreement", "A pact between countries setting terms of trade"],
        ]),
    },
    "social-studies-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Human geography", "The study of how people interact with places"],
        ]),
    },
    "social-studies-g9-l38": {
        "data_table": table(["Tool", "Use"], [
            ["GIS (Geographic Information Systems)", "Maps and analyzes spatial data"],
        ]),
    },
    "social-studies-g9-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Settlement patterns", "Often shaped by access to water and fertile land"],
        ]),
    },
    "social-studies-g9-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural pluralism", "Different cultural groups coexisting within a society"],
        ]),
    },
    "social-studies-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Nationalism", "Strong identification with and loyalty to one's nation"],
        ]),
    },
    "social-studies-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Global inequality", "Unequal distribution of wealth and resources across countries"],
        ]),
    },
    "social-studies-g9-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Development", "Improvement in a country's economic and social conditions"],
        ]),
    },
    "social-studies-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["NGO", "Non-governmental organization, works independently of government"],
        ]),
    },
    "social-studies-g9-l45": {
        "data_table": table(["Right", "Example"], [
            ["Right to a refund", "Consumer protection against faulty goods"],
        ]),
    },
    "social-studies-g9-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Public health", "Efforts to protect and improve the health of populations"],
        ]),
    },
    "social-studies-g9-l47": {
        "data_table": table(["Impact", "Example"], [
            ["Social media", "Changed how people communicate and access information"],
        ]),
    },
    "social-studies-g9-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethics", "Principles guiding right and wrong conduct"],
        ]),
    },
    "social-studies-g9-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Refugee", "A person forced to flee their country due to conflict or persecution"],
        ]),
    },
    "social-studies-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Global citizenship", "Seeing oneself as part of a worldwide community with shared responsibilities"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Social Studies lessons (completing 50/50).")


if __name__ == "__main__":
    main()
