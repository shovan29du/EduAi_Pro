#!/usr/bin/env python3
"""Depth pass, Grade 6 ICT & Computer Science: fill in real, hand-checked
data_table content for the 28 Grade 6 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 6 ICT & Computer Science to
full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g6-l2": {
        "data_table": table(["Hardware", "Function"], [
            ["CPU", "Processes instructions"], ["RAM", "Temporary working memory"], ["Hard drive", "Stores data long-term"],
        ]),
    },
    "ict-computer-science-g6-l3": {
        "data_table": table(["Software Type", "Example"], [
            ["Operating system", "Windows, macOS"], ["Application", "Word processor, web browser"],
        ]),
    },
    "ict-computer-science-g6-l4": {
        "data_table": table(["OS", "Type"], [
            ["Windows", "Desktop operating system"], ["Android", "Mobile operating system"],
        ]),
    },
    "ict-computer-science-g6-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Folder", "A container for organizing files"], ["File path", "The location of a file on a computer"],
        ]),
    },
    "ict-computer-science-g6-l6": {
        "data_table": table(["Tool", "Use"], [
            ["Bold/Italic", "Formats text for emphasis"], ["Spell check", "Finds spelling errors"],
        ]),
    },
    "ict-computer-science-g6-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell", "A single box in a spreadsheet"], ["Formula", "A calculation using cell values"],
        ]),
    },
    "ict-computer-science-g6-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Slide", "One page of a presentation"], ["Transition", "The effect between slides"],
        ]),
    },
    "ict-computer-science-g6-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Browser", "Software used to view websites"],
        ]),
    },
    "ict-computer-science-g6-l10": {
        "data_table": table(["Tip", "Why"], [
            ["Use specific keywords", "Gets more accurate results"],
            ["Check the source", "Ensures the information is trustworthy"],
        ]),
    },
    "ict-computer-science-g6-l11": {
        "data_table": table(["Email Etiquette Rule", "Why"], [
            ["Use a clear subject line", "Helps the reader understand the topic"],
            ["Be polite", "Maintains good communication"],
        ]),
    },
    "ict-computer-science-g6-l12": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
            ["Think before you post", "Posts can be seen by many people"],
        ]),
    },
    "ict-computer-science-g6-l13": {
        "data_table": table(["Step", "Action"], [
            ["Don't respond", "Avoids escalating the situation"], ["Tell a trusted adult", "Gets help to resolve it"],
        ]),
    },
    "ict-computer-science-g6-l14": {
        "data_table": table(["Rule", "Why"], [
            ["Use a strong, unique password", "Harder for others to guess"],
            ["Never share your password", "Keeps your account secure"],
        ]),
    },
    "ict-computer-science-g6-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud storage", "Storing files on remote servers accessed via the internet"],
        ]),
    },
    "ict-computer-science-g6-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Data", "Raw facts and figures"], ["Information", "Data processed into something meaningful"],
        ]),
    },
    "ict-computer-science-g6-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"], ["Record", "One entry in a database"],
        ]),
    },
    "ict-computer-science-g6-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that perform tasks that normally require human intelligence"],
        ]),
    },
    "ict-computer-science-g6-l20": {
        "data_table": table(["Component", "Purpose"], [
            ["Sensor", "Detects things like light or distance"], ["Motor", "Makes the robot move"],
        ]),
    },
    "ict-computer-science-g6-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital footprint", "The trail of data left by online activity"],
        ]),
    },
    "ict-computer-science-g6-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Copyright", "Legal protection for creative work"], ["Fair use", "Limited use of copyrighted material without permission"],
        ]),
    },
    "ict-computer-science-g6-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Coding", "Writing instructions for a computer"], ["Computer science", "The study of computers and computation"],
        ]),
    },
    "ict-computer-science-g6-l24": {
        "data_table": table(["Tip", "Why"], [
            ["Use all ten fingers", "Increases typing speed"], ["Keep eyes on the screen", "Improves accuracy"],
        ]),
    },
    "ict-computer-science-g6-l25": {
        "data_table": table(["Tool", "Use"], [
            ["Photo editor", "Adjusts and enhances images"], ["Video editor", "Cuts and arranges video clips"],
        ]),
    },
    "ict-computer-science-g6-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Network", "Connected computers that share data"], ["Router", "Directs data between devices"],
        ]),
    },
    "ict-computer-science-g6-l27": {
        "data_table": table(["Skill", "Purpose"], [
            ["Verifying sources", "Confirms information is accurate"], ["Recognizing manipulation", "Avoids being misled"],
        ]),
    },
    "ict-computer-science-g6-l28": {
        "data_table": table(["Skill", "Purpose"], [
            ["Comparing multiple sources", "Confirms information is accurate"],
            ["Checking the author/publisher", "Assesses credibility"],
        ]),
    },
    "ict-computer-science-g6-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["3D printing", "Building physical objects layer by layer from a digital design"],
        ]),
    },
    "ict-computer-science-g6-l30": {
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
        raise SystemExit(f"Lesson ids not found in grade6.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 ICT & Computer Science lessons (completing 30/30).")


if __name__ == "__main__":
    main()
