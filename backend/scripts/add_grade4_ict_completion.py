#!/usr/bin/env python3
"""Depth pass, Grade 4 ICT & Computer Science: fill in real, hand-checked
data_table content for the 28 Grade 4 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 4 ICT & Computer Science to
full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g4-l2": {
        "data_table": table(["Hardware", "Function"], [
            ["CPU", "Processes instructions"], ["RAM", "Temporary working memory"], ["Hard drive", "Stores data long-term"],
        ]),
    },
    "ict-computer-science-g4-l3": {
        "data_table": table(["Software Type", "Example"], [
            ["Operating system", "Windows, macOS"], ["Application", "Word processor, web browser"],
        ]),
    },
    "ict-computer-science-g4-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Router", "Directs data between devices"],
        ]),
    },
    "ict-computer-science-g4-l5": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
            ["Be kind online", "Creates a positive experience for everyone"],
        ]),
    },
    "ict-computer-science-g4-l6": {
        "data_table": table(["Tool", "Use"], [
            ["Bold/Italic", "Formats text for emphasis"], ["Spell check", "Finds spelling errors"],
        ]),
    },
    "ict-computer-science-g4-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell", "A single box in a spreadsheet"], ["Formula", "A calculation using cell values"],
        ]),
    },
    "ict-computer-science-g4-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Slide", "One page of a presentation"], ["Transition", "The effect between slides"],
        ]),
    },
    "ict-computer-science-g4-l9": {
        "data_table": table(["Tip", "Why"], [
            ["Use all ten fingers", "Increases typing speed"], ["Keep eyes on the screen", "Improves accuracy"],
        ]),
    },
    "ict-computer-science-g4-l10": {
        "data_table": table(["File Type", "Common Use"], [
            [".docx", "Word processing documents"], [".jpg", "Photos and images"], [".mp3", "Audio files"],
        ]),
    },
    "ict-computer-science-g4-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["World Wide Web", "The collection of websites accessible via the internet"],
            ["Browser", "Software used to view websites"],
        ]),
    },
    "ict-computer-science-g4-l12": {
        "data_table": table(["Email Etiquette Rule", "Why"], [
            ["Use a clear subject line", "Helps the reader understand the topic"],
            ["Be polite", "Maintains good communication"],
        ]),
    },
    "ict-computer-science-g4-l13": {
        "data_table": table(["Tip", "Why"], [
            ["Use specific keywords", "Gets more accurate results"],
            ["Check the source", "Ensures the information is trustworthy"],
        ]),
    },
    "ict-computer-science-g4-l14": {
        "data_table": table(["Rule", "Why"], [
            ["Use a strong, unique password", "Harder for others to guess"],
            ["Never share your password", "Keeps your account secure"],
        ]),
    },
    "ict-computer-science-g4-l15": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sequence", "Steps run in order"], ["Loop", "Steps that repeat"],
        ]),
    },
    "ict-computer-science-g4-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Robot", "A machine that can be programmed to perform tasks"],
            ["Automation", "Using technology to perform tasks without human effort"],
        ]),
    },
    "ict-computer-science-g4-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital footprint", "The trail of data left by online activity"],
            ["Privacy", "Controlling what personal information is shared"],
        ]),
    },
    "ict-computer-science-g4-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that can perform tasks that normally require human intelligence"],
        ]),
    },
    "ict-computer-science-g4-l20": {
        "data_table": table(["Tip", "Why"], [
            ["Check the source", "Ensures information is trustworthy"],
            ["Look for multiple sources", "Confirms the facts are accurate"],
        ]),
    },
    "ict-computer-science-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Class attendance list", "A simple database of names and dates"],
        ]),
    },
    "ict-computer-science-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Buying a computer", "Comparing CPU and RAM specifications"],
        ]),
    },
    "ict-computer-science-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Choosing an app", "Picking the right software for a task"],
        ]),
    },
    "ict-computer-science-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Video calling", "Data travels over the internet in real time"],
        ]),
    },
    "ict-computer-science-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Social media use", "Applying online safety rules"],
        ]),
    },
    "ict-computer-science-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Writing a school report", "Using a word processor"],
        ]),
    },
    "ict-computer-science-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Tracking allowance", "Using a spreadsheet to log savings"],
        ]),
    },
    "ict-computer-science-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Class project", "Presenting research with slides"],
        ]),
    },
    "ict-computer-science-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Writing assignments", "Typing faster and more accurately"],
        ]),
    },
    "ict-computer-science-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Saving homework", "Choosing the right file type and location"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 ICT & Computer Science lessons (completing 30/30).")


if __name__ == "__main__":
    main()
