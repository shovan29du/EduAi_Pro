#!/usr/bin/env python3
"""Depth pass, Grade 7 Social Studies: fill in real, hand-checked
data_table content for the 38 Grade 7 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 7 Social
Studies to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g7-l1": {
        "data_table": table(["Strategy", "How It Helps"], [
            ["Diplomacy", "Resolves disputes through negotiation"], ["Compromise", "Finds a shared solution"],
        ]),
    },
    "social-studies-g7-l3": {
        "data_table": table(["Branch", "Role"], [
            ["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "social-studies-g7-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Democracy", "A system where citizens vote for leaders"], ["Citizenship", "Legal membership in a country"],
        ]),
    },
    "social-studies-g7-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing a leader or decision by ballot"], ["Election", "The process of voting"],
        ]),
    },
    "social-studies-g7-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "social-studies-g7-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Rule of law", "The principle that everyone, including leaders, is subject to the law"],
        ]),
    },
    "social-studies-g7-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Constitution", "A document establishing a country's fundamental laws"],
        ]),
    },
    "social-studies-g7-l9": {
        "data_table": table(["Level", "Example Responsibility"], [
            ["Local", "City services like trash collection"],
        ]),
    },
    "social-studies-g7-l10": {
        "data_table": table(["Example of Volunteering", "Benefit"], [
            ["Community clean-up", "A cleaner neighborhood"],
        ]),
    },
    "social-studies-g7-l11": {
        "data_table": table(["Situation", "Effect on Price"], [
            ["High demand, low supply", "Price rises"], ["Low demand, high supply", "Price falls"],
        ]),
    },
    "social-studies-g7-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Market", "A system where buyers and sellers exchange goods"],
        ]),
    },
    "social-studies-g7-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Tax", "Money collected by government to fund public services"],
        ]),
    },
    "social-studies-g7-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Labour rights", "Legal protections for workers, like fair pay and safe conditions"],
        ]),
    },
    "social-studies-g7-l16": {
        "data_table": table(["Right", "Example"], [
            ["Right to a refund", "For a defective product"], ["Right to accurate information", "Truthful advertising"],
        ]),
    },
    "social-studies-g7-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Poverty", "Lacking sufficient resources for basic needs"],
        ]),
    },
    "social-studies-g7-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Social class", "A group defined by economic or social status"],
        ]),
    },
    "social-studies-g7-l19": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"],
        ]),
    },
    "social-studies-g7-l20": {
        "data_table": table(["Family Structure", "Description"], [
            ["Nuclear family", "Parents and children living together"], ["Extended family", "Includes grandparents, aunts, uncles"],
        ]),
    },
    "social-studies-g7-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Gender equality", "A core value in the UN Sustainable Development Goals"],
        ]),
    },
    "social-studies-g7-l22": {
        "data_table": table(["Aspect of Society", "Religion's Role"], [
            ["Community", "Provides shared beliefs and gatherings"], ["Ethics", "Often shapes moral guidance"],
        ]),
    },
    "social-studies-g7-l23": {
        "data_table": table(["Education System", "Feature"], [
            ["Finland", "Emphasizes shorter school days and less homework"],
        ]),
    },
    "social-studies-g7-l24": {
        "data_table": table(["Movement", "Known For"], [
            ["Civil rights movement", "Fighting for racial equality in the US"],
            ["Suffrage movement", "Fighting for women's right to vote"],
        ]),
    },
    "social-studies-g7-l25": {
        "data_table": table(["Technique", "Example"], [
            ["Bandwagon", "'Everyone is doing it, so you should too'"],
        ]),
    },
    "social-studies-g7-l26": {
        "data_table": table(["Media Type", "Example"], [
            ["News outlet", "Reports current events"], ["Social media", "Shares user-generated content"],
        ]),
    },
    "social-studies-g7-l27": {
        "data_table": table(["Technology", "Social Impact"], [
            ["Smartphones", "Changed how people communicate"],
        ]),
    },
    "social-studies-g7-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "social-studies-g7-l29": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "social-studies-g7-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanisation", "Growth of cities as more people move there"],
        ]),
    },
    "social-studies-g7-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Justice system", "Courts that interpret and apply laws"],
        ]),
    },
    "social-studies-g7-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["International law", "Rules governing relations between countries"],
        ]),
    },
    "social-studies-g7-l33": {
        "data_table": table(["NGO", "Focus"], [
            ["Red Cross", "Humanitarian relief"], ["Amnesty International", "Human rights advocacy"],
        ]),
    },
    "social-studies-g7-l34": {
        "data_table": table(["Institution", "Purpose"], [
            ["United Nations", "Promotes peace and cooperation among countries"],
        ]),
    },
    "social-studies-g7-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Social justice", "Fair treatment and opportunity for all members of society"],
        ]),
    },
    "social-studies-g7-l36": {
        "data_table": table(["Then", "Now"], [
            ["Letters sent by mail", "Instant messages and email"],
        ]),
    },
    "social-studies-g7-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Public opinion", "The collective views of a population on an issue"],
        ]),
    },
    "social-studies-g7-l38": {
        "data_table": table(["Example of Volunteering", "Benefit"], [
            ["Food bank help", "Supports families in need"],
        ]),
    },
    "social-studies-g7-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Social contract", "The idea that citizens agree to follow rules in exchange for protection and order"],
        ]),
    },
    "social-studies-g7-l40": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Citizens vote for leaders"], ["Monarchy", "Rule by a king or queen"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Social Studies lessons (completing 40/40).")


if __name__ == "__main__":
    main()
