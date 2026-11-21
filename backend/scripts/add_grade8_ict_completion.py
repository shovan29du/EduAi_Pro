#!/usr/bin/env python3
"""Depth pass, Grade 8 ICT & Computer Science: fill in real, hand-checked
data_table content for the 38 Grade 8 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 8 ICT & Computer Science to
full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g8-l2": {
        "data_table": table(["Hardware", "Function"], [
            ["CPU", "Processes instructions"], ["RAM", "Temporary working memory"],
        ]),
    },
    "ict-computer-science-g8-l3": {
        "data_table": table(["Software Type", "Example"], [
            ["Operating system", "Windows, macOS"], ["Application", "Word processor, web browser"],
        ]),
    },
    "ict-computer-science-g8-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Router", "Directs data between devices"],
        ]),
    },
    "ict-computer-science-g8-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Program", "A set of instructions for a computer"],
        ]),
    },
    "ict-computer-science-g8-l6": {
        "data_table": table(["Concept", "Example"], [
            ["print()", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "ict-computer-science-g8-l7": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["str", "'hello'"],
        ]),
    },
    "ict-computer-science-g8-l8": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs if a condition is true"], ["else", "Runs if the condition is false"],
        ]),
    },
    "ict-computer-science-g8-l9": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"],
        ]),
    },
    "ict-computer-science-g8-l10": {
        "data_table": table(["Concept", "Example"], [
            ["Function", "def add(a, b): return a + b"],
        ]),
    },
    "ict-computer-science-g8-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "ict-computer-science-g8-l12": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"],
        ]),
    },
    "ict-computer-science-g8-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "An error in a program"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "ict-computer-science-g8-l14": {
        "data_table": table(["HTML Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
    },
    "ict-computer-science-g8-l15": {
        "data_table": table(["CSS Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
    },
    "ict-computer-science-g8-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"],
        ]),
    },
    "ict-computer-science-g8-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell", "A single box in a spreadsheet"], ["Formula", "A calculation using cell values"],
        ]),
    },
    "ict-computer-science-g8-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "ict-computer-science-g8-l19": {
        "data_table": table(["Rule", "Why"], [
            ["Use a strong, unique password", "Harder for others to guess"],
        ]),
    },
    "ict-computer-science-g8-l21": {
        "data_table": table(["Rule", "Why"], [
            ["Avoid clicking unfamiliar links", "Reduces the risk of malware"],
        ]),
    },
    "ict-computer-science-g8-l22": {
        "data_table": table(["Rule", "Why"], [
            ["Be kind online", "Creates a positive experience for everyone"],
        ]),
    },
    "ict-computer-science-g8-l23": {
        "data_table": table(["Step", "Action"], [
            ["Don't respond", "Avoids escalating the situation"], ["Tell a trusted adult", "Gets help to resolve it"],
        ]),
    },
    "ict-computer-science-g8-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud computing", "Using remote servers over the internet to store and process data"],
        ]),
    },
    "ict-computer-science-g8-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Folder", "A container for organizing files"],
        ]),
    },
    "ict-computer-science-g8-l26": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"],
        ]),
    },
    "ict-computer-science-g8-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Binary", "The base-2 number system computers use internally"],
        ]),
    },
    "ict-computer-science-g8-l28": {
        "data_table": table(["Network Type", "Description"], [
            ["LAN", "Local Area Network"], ["WAN", "Wide Area Network"],
        ]),
    },
    "ict-computer-science-g8-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "The global network of connected computers"],
            ["World Wide Web", "The collection of websites accessible via the internet"],
        ]),
    },
    "ict-computer-science-g8-l30": {
        "data_table": table(["Component", "Purpose"], [
            ["Sensor", "Detects things like light or distance"], ["Motor", "Makes the robot move"],
        ]),
    },
    "ict-computer-science-g8-l31": {
        "data_table": table(["Concept", "Meaning"], [
            ["Decomposition", "Breaking a big problem into smaller parts"],
        ]),
    },
    "ict-computer-science-g8-l32": {
        "data_table": table(["Game Element", "Purpose"], [
            ["Win condition", "The requirement for the player to win"],
        ]),
    },
    "ict-computer-science-g8-l33": {
        "data_table": table(["Tool", "Use"], [
            ["Photo editor", "Adjusts and enhances images"],
        ]),
    },
    "ict-computer-science-g8-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Data privacy", "Controlling who can access your personal information"],
        ]),
    },
    "ict-computer-science-g8-l35": {
        "data_table": table(["Ethical Issue", "Example"], [
            ["Privacy", "How companies use personal data"],
        ]),
    },
    "ict-computer-science-g8-l36": {
        "data_table": table(["Milestone", "Year"], [
            ["ENIAC (early computer)", "1945"], ["Personal computer era begins", "Late 1970s"],
        ]),
    },
    "ict-computer-science-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks changes to code over time"],
        ]),
    },
    "ict-computer-science-g8-l38": {
        "data_table": table(["Step", "Purpose"], [
            ["Crawling", "Search engines scan web pages"], ["Indexing", "Organizes pages for fast retrieval"],
        ]),
    },
    "ict-computer-science-g8-l39": {
        "data_table": table(["Device", "Example Use"], [
            ["Smartwatch", "Tracks fitness and notifications"],
        ]),
    },
    "ict-computer-science-g8-l40": {
        "data_table": table(["Career", "Focus"], [
            ["Software developer", "Writes and maintains programs"], ["Network administrator", "Manages computer networks"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 ICT & Computer Science lessons (completing 40/40).")


if __name__ == "__main__":
    main()
