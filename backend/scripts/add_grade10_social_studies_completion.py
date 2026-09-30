#!/usr/bin/env python3
"""Depth pass, Grade 10 Social Studies: fill in real, hand-checked
data_table content for the Grade 10 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 10 Social
Studies to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g10-l1": {
        "data_table": table(["Ideology", "Core Idea"], [
            ["Conservatism", "Favors tradition and gradual change"], ["Liberalism", "Favors individual rights and reform"],
        ]),
    },
    "social-studies-g10-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"],
        ]),
    },
    "social-studies-g10-l3": {
        "data_table": table(["Government Type", "Description"], [
            ["Monarchy", "Power held by a king or queen"], ["Republic", "Power held by elected representatives"], ["Federation", "Power shared between national and regional levels"],
        ]),
    },
    "social-studies-g10-l4": {
        "data_table": table(["Body", "Role"], [
            ["General Assembly", "All member states, one vote each"], ["Security Council", "Handles peace and security, 5 permanent members"],
        ]),
    },
    "social-studies-g10-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "social-studies-g10-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Industrial Revolution began", "Late 18th century, in Britain"],
        ]),
    },
    "social-studies-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Colonialism", "One country's political control over another territory"], ["Decolonization", "Colonies gaining independence"],
        ]),
    },
    "social-studies-g10-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Cold War period", "1947-1991"], ["Main rivals", "United States and Soviet Union"],
        ]),
    },
    "social-studies-g10-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Nationalism", "Strong identification with and loyalty to one's nation"],
        ]),
    },
    "social-studies-g10-l12": {
        "data_table": table(["Movement", "Notable Figure"], [
            ["American civil rights movement", "Martin Luther King Jr."],
        ]),
    },
    "social-studies-g10-l13": {
        "data_table": table(["Branch", "Role"], [
            ["Judiciary", "Interprets and applies the law"],
        ]),
    },
    "social-studies-g10-l14": {
        "data_table": table(["System", "Description"], [
            ["Federal", "Power divided between national and regional governments"], ["Unitary", "Power concentrated at the national level"],
        ]),
    },
    "social-studies-g10-l15": {
        "data_table": table(["Voting System", "Description"], [
            ["First-past-the-post", "Candidate with the most votes wins"], ["Proportional representation", "Seats allocated by vote share"],
        ]),
    },
    "social-studies-g10-l16": {
        "data_table": table(["Ideology", "Example"], [
            ["Conservative party", "Favors tradition and limited change"],
        ]),
    },
    "social-studies-g10-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Constitution", "A country's foundational body of law"], ["Rule of law", "Everyone is subject to the law"],
        ]),
    },
    "social-studies-g10-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Citizenship", "Membership in a political community with rights and duties"],
        ]),
    },
    "social-studies-g10-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Social stratification", "The ranking of people into social classes"],
        ]),
    },
    "social-studies-g10-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanization", "The growth of cities as populations shift from rural areas"],
        ]),
    },
    "social-studies-g10-l21": {
        "data_table": table(["Cause of Migration", "Example"], [
            ["Push factor", "War or lack of jobs"], ["Pull factor", "Better opportunities"],
        ]),
    },
    "social-studies-g10-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing economic and cultural integration between countries"],
        ]),
    },
    "social-studies-g10-l23": {
        "data_table": table(["Role", "Example"], [
            ["Watchdog function", "Media investigates and reports on government actions"],
        ]),
    },
    "social-studies-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Public policy", "A course of action adopted by government to address an issue"],
        ]),
    },
    "social-studies-g10-l25": {
        "data_table": table(["Level", "Example Responsibility"], [
            ["Local government", "Manages schools, roads, and local services"],
        ]),
    },
    "social-studies-g10-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Diplomacy", "Managing relationships between countries"],
        ]),
    },
    "social-studies-g10-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["League of Nations", "1920-1946, predecessor to the UN, failed to prevent WWII"],
        ]),
    },
    "social-studies-g10-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Population distribution", "Uneven, concentrated in fertile and coastal regions"],
        ]),
    },
    "social-studies-g10-l29": {
        "data_table": table(["System", "Key Feature"], [
            ["Capitalism", "Private ownership and free markets"], ["Socialism", "Collective or state ownership"],
        ]),
    },
    "social-studies-g10-l30": {
        "data_table": table(["Movement", "Goal"], [
            ["Labor movement", "Improved workers' rights and conditions"],
        ]),
    },
    "social-studies-g10-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Slavery abolition", "Britain abolished it across most of its empire in 1833"],
        ]),
    },
    "social-studies-g10-l32": {
        "data_table": table(["Civilization", "Region"], [
            ["Mesopotamia", "Modern-day Iraq"], ["Ancient Egypt", "Along the Nile"],
        ]),
    },
    "social-studies-g10-l33": {
        "data_table": table(["Civilization", "Notable Achievement"], [
            ["Ancient Greece", "Birthplace of democracy"], ["Ancient Rome", "Extensive legal and engineering legacy"],
        ]),
    },
    "social-studies-g10-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Renaissance began", "14th century, Italy"],
        ]),
    },
    "social-studies-g10-l35": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
        ]),
    },
    "social-studies-g10-l36": {
        "data_table": table(["Revolution", "Year Began"], [
            ["American Revolution", "1775"], ["French Revolution", "1789"],
        ]),
    },
    "social-studies-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Peacekeeping", "UN forces deployed to maintain peace in conflict zones"],
        ]),
    },
    "social-studies-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Refugee", "A person forced to flee their country due to conflict or persecution"],
        ]),
    },
    "social-studies-g10-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Women's suffrage", "Movement for women's right to vote"],
        ]),
    },
    "social-studies-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Indigenous peoples", "The original inhabitants of a region, with distinct cultural traditions"],
        ]),
    },
    "social-studies-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural comparison", "Examining similarities and differences across societies"],
        ]),
    },
    "social-studies-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Nation-state", "A political entity defined by a shared national identity and sovereign territory"],
        ]),
    },
    "social-studies-g10-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Trade union", "An organization of workers formed to protect their rights"],
        ]),
    },
    "social-studies-g10-l44": {
        "data_table": table(["Position", "General View"], [
            ["Left", "Favors greater equality and government intervention"], ["Right", "Favors tradition and limited government intervention"],
        ]),
    },
    "social-studies-g10-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Census", "An official count of a population and its characteristics"],
        ]),
    },
    "social-studies-g10-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["NGO", "Non-governmental organization, works independently of government"],
        ]),
    },
    "social-studies-g10-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Conflict resolution", "Methods for peacefully ending disputes between parties"],
        ]),
    },
    "social-studies-g10-l48": {
        "data_table": table(["Empire", "Notable Fact"], [
            ["Roman Empire", "Rose from a republic, fell in 476 CE (west)"],
        ]),
    },
    "social-studies-g10-l49": {
        "data_table": table(["Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices, and ideas between China and Europe"],
        ]),
    },
    "social-studies-g10-l50": {
        "data_table": table(["Source Type", "Example"], [
            ["Primary source", "A diary written at the time of an event"], ["Secondary source", "A history book analyzing that event"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Social Studies lessons (completing 50/50).")


if __name__ == "__main__":
    main()
