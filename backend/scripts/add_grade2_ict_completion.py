#!/usr/bin/env python3
"""Depth pass, Grade 2 ICT & Computer Science: fill in real, hand-checked
data_table content for the 18 Grade 2 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 2 ICT to full 20/20 coverage,
completing all 16 subjects for Grade 2.

Content covers real, basic computing terminology (email parts, hardware
vs. software, printer vs. scanner functions) -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g2-l2": {
        "data_table": table(["Computer Part", "Function"], [
            ["Keyboard", "Used for typing text and commands"],
            ["Mouse", "Used for pointing and clicking"],
            ["Screen (Monitor)", "Displays what the computer is doing"],
        ]),
    },
    "ict-computer-science-g2-l3": {
        "data_table": table(["Device", "Use"], [
            ["Mouse", "Pointing and clicking"], ["Keyboard", "Typing letters and numbers"],
        ]),
    },
    "ict-computer-science-g2-l4": {
        "data_table": table(["Keyboard Row", "Example Letters"], [
            ["Top row", "Q W E R T Y"], ["Home row", "A S D F"],
        ]),
    },
    "ict-computer-science-g2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Tablet", "A portable touchscreen computer"], ["App", "A program you use on a tablet or phone"],
        ]),
    },
    "ict-computer-science-g2-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information", "Keeps you safe from strangers"],
            ["Ask an adult before clicking unknown links", "Avoids unsafe content"],
        ]),
    },
    "ict-computer-science-g2-l7": {
        "data_table": table(["Email Part", "Purpose"], [
            ["To", "Who receives the email"], ["Subject", "A short summary of the email"],
            ["Body", "The main message"],
        ]),
    },
    "ict-computer-science-g2-l8": {
        "data_table": table(["Tool", "Use"], [
            ["Word processor", "Writing and formatting text documents"],
            ["Bold/Italic", "Emphasizing text"],
        ]),
    },
    "ict-computer-science-g2-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Pencil tool", "Draws thin lines"], ["Fill tool", "Colors in a shape"],
        ]),
    },
    "ict-computer-science-g2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Website", "A collection of linked pages you can visit"],
            ["Web browser", "Software used to view websites"],
        ]),
    },
    "ict-computer-science-g2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Search engine", "A tool that helps you find information online"],
            ["Keyword", "Words you type to search for something"],
        ]),
    },
    "ict-computer-science-g2-l12": {
        "data_table": table(["Digital Citizenship Habit", "Example"], [
            ["Being kind online", "Not writing mean comments"],
            ["Protecting privacy", "Not sharing personal information"],
        ]),
    },
    "ict-computer-science-g2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["File", "A single document, picture, or program"],
            ["Folder", "A place to organize and store files"],
        ]),
    },
    "ict-computer-science-g2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Software", "Programs that run on a computer"],
            ["Hardware", "The physical parts of a computer"],
        ]),
    },
    "ict-computer-science-g2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Cloud storage", "Saving files on the internet instead of just your device"],
            ["Benefit", "Access your files from any device"],
        ]),
    },
    "ict-computer-science-g2-l17": {
        "data_table": table(["Device", "Common Use"], [
            ["Smartphone", "Calling, texting, apps"], ["Television", "Watching shows and movies"],
        ]),
    },
    "ict-computer-science-g2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Video call", "A call where you can see and hear the other person"],
            ["Webcam", "A camera used for video calls"],
        ]),
    },
    "ict-computer-science-g2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital camera", "Captures pictures and stores them electronically"],
            ["Photo", "A saved image you can view or print"],
        ]),
    },
    "ict-computer-science-g2-l20": {
        "data_table": table(["Device", "Function"], [
            ["Printer", "Turns a digital document into a paper copy"],
            ["Scanner", "Turns a paper document into a digital file"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json ICT: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 ICT lessons (completing 20/20).")


if __name__ == "__main__":
    main()
