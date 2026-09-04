#!/usr/bin/env python3
"""Depth pass, Grade 7 ICT & Computer Science: fill in real, hand-checked
data_table content for the 38 Grade 7 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 7 ICT & Computer Science to
full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g7-l2": {
        "data_table": table(["Hardware", "Function"], [
            ["CPU", "Processes instructions"], ["RAM", "Temporary working memory"], ["Hard drive", "Stores data long-term"],
        ]),
    },
    "ict-computer-science-g7-l3": {
        "data_table": table(["Software Type", "Example"], [
            ["Operating system", "Windows, macOS"], ["Application", "Word processor, web browser"],
        ]),
    },
    "ict-computer-science-g7-l4": {
        "data_table": table(["OS", "Type"], [
            ["Windows", "Desktop operating system"], ["Android", "Mobile operating system"],
        ]),
    },
    "ict-computer-science-g7-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Folder", "A container for organizing files"], ["File path", "The location of a file on a computer"],
        ]),
    },
    "ict-computer-science-g7-l6": {
        "data_table": table(["Device Type", "Example"], [
            ["Input device", "Keyboard, mouse"], ["Output device", "Monitor, speakers"],
        ]),
    },
    "ict-computer-science-g7-l7": {
        "data_table": table(["Storage Device", "Type"], [
            ["Hard disk drive", "Magnetic storage"], ["Solid-state drive", "Flash memory storage"],
        ]),
    },
    "ict-computer-science-g7-l8": {
        "data_table": table(["Network Type", "Description"], [
            ["LAN", "Local Area Network, covers a small area"], ["WAN", "Wide Area Network, covers a large area"],
        ]),
    },
    "ict-computer-science-g7-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Router", "Directs data between devices"],
        ]),
    },
    "ict-computer-science-g7-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["World Wide Web", "The collection of websites accessible via the internet"], ["Browser", "Software used to view websites"],
        ]),
    },
    "ict-computer-science-g7-l11": {
        "data_table": table(["Tip", "Why"], [
            ["Use specific keywords", "Gets more accurate results"],
            ["Check the source", "Ensures the information is trustworthy"],
        ]),
    },
    "ict-computer-science-g7-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "ict-computer-science-g7-l13": {
        "data_table": table(["Rule", "Why"], [
            ["Use a strong, unique password", "Harder for others to guess"],
            ["Never share your password", "Keeps your account secure"],
        ]),
    },
    "ict-computer-science-g7-l15": {
        "data_table": table(["Rule", "Why"], [
            ["Be kind online", "Creates a positive experience for everyone"],
            ["Think before you post", "Posts can be seen by many people"],
        ]),
    },
    "ict-computer-science-g7-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital footprint", "The trail of data left by online activity"],
        ]),
    },
    "ict-computer-science-g7-l17": {
        "data_table": table(["Skill", "Purpose"], [
            ["Verifying sources", "Confirms information is accurate"],
        ]),
    },
    "ict-computer-science-g7-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell", "A single box in a spreadsheet"], ["Formula", "A calculation using cell values"],
        ]),
    },
    "ict-computer-science-g7-l19": {
        "data_table": table(["Tool", "Use"], [
            ["Bold/Italic", "Formats text for emphasis"], ["Spell check", "Finds spelling errors"],
        ]),
    },
    "ict-computer-science-g7-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Slide", "One page of a presentation"], ["Transition", "The effect between slides"],
        ]),
    },
    "ict-computer-science-g7-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"], ["Record", "One entry in a database"],
        ]),
    },
    "ict-computer-science-g7-l22": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"],
        ]),
    },
    "ict-computer-science-g7-l23": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["4", "100"],
        ]),
    },
    "ict-computer-science-g7-l24": {
        "data_table": table(["Logic Gate", "Function"], [
            ["AND", "Outputs true only if both inputs are true"], ["OR", "Outputs true if either input is true"],
        ]),
    },
    "ict-computer-science-g7-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that perform tasks that normally require human intelligence"],
        ]),
    },
    "ict-computer-science-g7-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine learning", "A type of AI where systems learn from data"],
        ]),
    },
    "ict-computer-science-g7-l27": {
        "data_table": table(["Component", "Purpose"], [
            ["Sensor", "Detects things like light or distance"], ["Motor", "Makes the robot move"],
        ]),
    },
    "ict-computer-science-g7-l28": {
        "data_table": table(["Milestone", "Year"], [
            ["ENIAC (early computer)", "1945"], ["Personal computer era begins", "Late 1970s"],
        ]),
    },
    "ict-computer-science-g7-l29": {
        "data_table": table(["Ethical Issue", "Example"], [
            ["Privacy", "How companies use personal data"], ["Digital divide", "Unequal access to technology"],
        ]),
    },
    "ict-computer-science-g7-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Copyright", "Legal protection for creative work"], ["Fair use", "Limited use of copyrighted material without permission"],
        ]),
    },
    "ict-computer-science-g7-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud computing", "Using remote servers over the internet to store and process data"],
        ]),
    },
    "ict-computer-science-g7-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Pixel", "The smallest unit of a digital image"],
        ]),
    },
    "ict-computer-science-g7-l33": {
        "data_table": table(["Tool", "Use"], [
            ["Photo editor", "Adjusts and enhances images"], ["Video editor", "Cuts and arranges video clips"],
        ]),
    },
    "ict-computer-science-g7-l34": {
        "data_table": table(["Tip", "Why"], [
            ["Use all ten fingers", "Increases typing speed"], ["Keep eyes on the screen", "Improves accuracy"],
        ]),
    },
    "ict-computer-science-g7-l35": {
        "data_table": table(["Problem", "First Troubleshooting Step"], [
            ["Device won't turn on", "Check the power connection"], ["App is frozen", "Restart the app or device"],
        ]),
    },
    "ict-computer-science-g7-l36": {
        "data_table": table(["Network Type", "Description"], [
            ["LAN", "Local Area Network, covers a small area"], ["WAN", "Wide Area Network, covers a large area"],
        ]),
    },
    "ict-computer-science-g7-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["E-commerce", "Buying and selling goods or services over the internet"],
        ]),
    },
    "ict-computer-science-g7-l38": {
        "data_table": table(["HTML Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "ict-computer-science-g7-l39": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
        ]),
    },
    "ict-computer-science-g7-l40": {
        "data_table": table(["Emerging Technology", "Example Use"], [
            ["Artificial intelligence", "Voice assistants, recommendation systems"],
            ["Virtual reality", "Immersive simulations and games"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 ICT & Computer Science lessons (completing 40/40).")


if __name__ == "__main__":
    main()
