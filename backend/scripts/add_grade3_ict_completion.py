#!/usr/bin/env python3
"""Depth pass, Grade 3 ICT & Computer Science: fill in real, hand-checked
data_table content for the 18 Grade 3 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 3 ICT & Computer Science to
full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-g3-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Scratch", "A block-based visual programming language"], ["Block", "A snap-together instruction"],
        ]),
    },
    "ict-computer-science-g3-l2": {
        "data_table": table(["Part", "Function"], [
            ["CPU", "The 'brain' that processes instructions"], ["Monitor", "Displays output"],
            ["Keyboard", "Inputs text"],
        ]),
    },
    "ict-computer-science-g3-l3": {
        "data_table": table(["Device", "Use"], [
            ["Keyboard", "Typing text and commands"], ["Mouse", "Pointing, clicking, and selecting"],
        ]),
    },
    "ict-computer-science-g3-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Website", "A page or set of pages on the internet"],
        ]),
    },
    "ict-computer-science-g3-l5": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information online", "Keeps you safe from strangers"],
            ["Tell a trusted adult about anything unsafe", "Helps adults protect you"],
        ]),
    },
    "ict-computer-science-g3-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Word processor", "Software for writing and editing text documents"],
        ]),
    },
    "ict-computer-science-g3-l7": {
        "data_table": table(["Tool", "Use"], [
            ["Pencil tool", "Draws freehand lines"], ["Fill tool", "Fills a shape with color"],
        ]),
    },
    "ict-computer-science-g3-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Folder", "A container for organizing files"], ["File", "A single document, photo, or program"],
        ]),
    },
    "ict-computer-science-g3-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Email", "Electronic mail sent over the internet"], ["Inbox", "Where received emails are stored"],
        ]),
    },
    "ict-computer-science-g3-l10": {
        "data_table": table(["Tip", "Why"], [
            ["Use specific keywords", "Gets more accurate results"],
            ["Check the source", "Ensures the information is trustworthy"],
        ]),
    },
    "ict-computer-science-g3-l11": {
        "data_table": table(["Digital Citizenship Rule", "Why"], [
            ["Be respectful online", "Creates a positive experience for everyone"],
            ["Think before you post", "Posts can be seen by many people"],
        ]),
    },
    "ict-computer-science-g3-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Slide", "One page of a presentation"], ["Slideshow", "A sequence of slides shown in order"],
        ]),
    },
    "ict-computer-science-g3-l14": {
        "data_table": table(["Concept", "Meaning"], [
            ["Sequence", "Steps run in order"], ["Loop", "Steps that repeat"],
        ]),
    },
    "ict-computer-science-g3-l15": {
        "data_table": table(["Rule", "Why"], [
            ["Ask permission before downloading apps", "Keeps your device and data safe"],
            ["Use age-appropriate apps", "Ensures suitable content"],
        ]),
    },
    "ict-computer-science-g3-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Robot", "A machine that can be programmed to perform tasks"],
            ["Sensor", "Detects things like light or distance"],
        ]),
    },
    "ict-computer-science-g3-l17": {
        "data_table": table(["Device", "Common Use"], [
            ["Tablet", "Touch-screen browsing and apps"], ["Laptop", "Portable computing with keyboard"],
        ]),
    },
    "ict-computer-science-g3-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Copyright", "Legal protection for creative work"], ["Sharing online", "Should credit the original creator"],
        ]),
    },
    "ict-computer-science-g3-l20": {
        "data_table": table(["Typing Tip", "Why"], [
            ["Use all ten fingers", "Increases typing speed"], ["Keep eyes on the screen", "Improves accuracy"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json ICT & Computer Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 ICT & Computer Science lessons (completing 20/20).")


if __name__ == "__main__":
    main()
