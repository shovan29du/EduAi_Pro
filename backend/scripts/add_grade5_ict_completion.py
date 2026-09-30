#!/usr/bin/env python3
"""Depth pass, Grade 5 ICT & Computer Science: fill in real, hand-checked
data_table content for the 28 Grade 5 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 5 ICT & Computer Science to
full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g5-l2": {
        "data_table": table(["Hardware", "Function"], [
            ["CPU", "Processes instructions"], ["RAM", "Temporary working memory"],
        ]),
    },
    "ict-computer-science-g5-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["ISP", "A company providing internet access"],
        ]),
    },
    "ict-computer-science-g5-l4": {
        "data_table": table(["Rule", "Why"], [
            ["Be kind online", "Creates a positive experience for everyone"],
            ["Think before you post", "Posts can be seen by many people"],
        ]),
    },
    "ict-computer-science-g5-l5": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
        ]),
    },
    "ict-computer-science-g5-l6": {
        "data_table": table(["Sign of a Reliable Website", "Example"], [
            ["Trusted domain", "Government (.gov) or educational (.edu) sites"],
            ["Author cited", "Named, credible experts"],
        ]),
    },
    "ict-computer-science-g5-l7": {
        "data_table": table(["Tool", "Use"], [
            ["Bold/Italic", "Formats text for emphasis"], ["Spell check", "Finds spelling errors"],
        ]),
    },
    "ict-computer-science-g5-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Cell", "A single box in a spreadsheet"], ["Formula", "A calculation using cell values"],
        ]),
    },
    "ict-computer-science-g5-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Slide", "One page of a presentation"], ["Transition", "The effect between slides"],
        ]),
    },
    "ict-computer-science-g5-l10": {
        "data_table": table(["Tip", "Why"], [
            ["Use all ten fingers", "Increases typing speed"], ["Keep eyes on the screen", "Improves accuracy"],
        ]),
    },
    "ict-computer-science-g5-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Folder", "A container for organizing files"], ["File path", "The location of a file on a computer"],
        ]),
    },
    "ict-computer-science-g5-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"], ["Record", "One entry in a database"],
        ]),
    },
    "ict-computer-science-g5-l13": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "name = 'Sam'"], ["Input", "age = input('How old are you? ')"],
        ]),
        "formulae": ["name = \"Sam\"", "age = input(\"How old are you? \")"],
    },
    "ict-computer-science-g5-l14": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs code if a condition is true"], ["else", "Runs code if the condition is false"],
        ]),
        "formulae": ["if age >= 13:", "    print(\"Teen\")", "else:", "    print(\"Not a teen\")"],
    },
    "ict-computer-science-g5-l15": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"],
        ]),
        "formulae": ["for i in range(5):", "    print(i)"],
    },
    "ict-computer-science-g5-l16": {
        "data_table": table(["Operation", "Example"], [
            ["Create a list", "colors = ['red', 'blue']"],
        ]),
        "formulae": ["colors = [\"red\", \"blue\"]"],
    },
    "ict-computer-science-g5-l17": {
        "data_table": table(["Concept", "Example"], [
            ["Function definition", "def greet(): print('Hi')"],
        ]),
        "formulae": ["def greet():", "    print(\"Hi\")"],
    },
    "ict-computer-science-g5-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Crawling", "Search engines scan web pages"], ["Indexing", "Organizes pages for fast retrieval"],
        ]),
    },
    "ict-computer-science-g5-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Robot", "A machine that can be programmed to perform tasks"],
            ["Sensor", "Detects things like light or distance"],
        ]),
    },
    "ict-computer-science-g5-l21": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"],
        ]),
    },
    "ict-computer-science-g5-l22": {
        "data_table": table(["Step", "Action"], [
            ["Don't respond", "Avoids escalating the situation"], ["Tell a trusted adult", "Gets help to resolve it"],
        ]),
    },
    "ict-computer-science-g5-l23": {
        "data_table": table(["Rule", "Why"], [
            ["Use a strong, unique password", "Harder for others to guess"],
            ["Never share your password", "Keeps your account secure"],
        ]),
    },
    "ict-computer-science-g5-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Network", "Connected computers that share data"], ["Router", "Directs data between devices"],
        ]),
    },
    "ict-computer-science-g5-l25": {
        "data_table": table(["Logic Concept", "Example"], [
            ["Sequence", "Steps run in order"], ["Condition", "A decision point in the logic"],
        ]),
    },
    "ict-computer-science-g5-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that perform tasks that normally require human intelligence"],
        ]),
    },
    "ict-computer-science-g5-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital footprint", "The trail of data left by online activity"],
        ]),
    },
    "ict-computer-science-g5-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Web page", "A single document viewable in a browser"], ["HTML", "The language used to build web pages"],
        ]),
    },
    "ict-computer-science-g5-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Copyright", "Legal protection for creative work"], ["Fair use", "Limited use of copyrighted material without permission"],
        ]),
    },
    "ict-computer-science-g5-l30": {
        "data_table": table(["Problem", "First Troubleshooting Step"], [
            ["Device won't turn on", "Check the power connection"], ["App is frozen", "Restart the app or device"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 ICT & Computer Science lessons (completing 30/30).")


if __name__ == "__main__":
    main()
