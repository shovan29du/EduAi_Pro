#!/usr/bin/env python3
"""Depth pass, Grade 1 ICT & Computer Science: fill in real, hand-checked
data_table content for the 17 Grade 1 ICT lessons not covered by the
earlier breadth-first batch. Brings Grade 1 ICT to full 20/20 coverage,
completing all 14 subjects for Grade 1.

Content covers real, basic computing terminology and safety guidance
(QWERTY keyboard layout, real online-safety rules, what an algorithm is)
-- nothing fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_ict_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ict-computer-science-g1-l3": {
        "data_table": table(["Step", "Action"], [
            ["Turning on", "Press the power button"],
            ["Turning off", "Use the shutdown/sleep option, don't just unplug"],
        ]),
    },
    "ict-computer-science-g1-l4": {
        "data_table": table(["Device", "Use"], [
            ["Mouse", "Pointing and clicking"], ["Keyboard", "Typing letters and numbers"],
        ]),
    },
    "ict-computer-science-g1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A network connecting computers around the world"],
            ["Website", "A collection of linked pages you can visit"],
        ]),
    },
    "ict-computer-science-g1-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Never share personal information", "Keeps you safe from strangers"],
            ["Ask an adult before clicking unknown links", "Avoids unsafe content"],
        ]),
    },
    "ict-computer-science-g1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Tablet", "A portable touchscreen computer"], ["App", "A program you use on a tablet or phone"],
        ]),
    },
    "ict-computer-science-g1-l8": {
        "data_table": table(["Keyboard Row", "Example Letters"], [
            ["Top row", "Q W E R T Y"], ["Home row", "A S D F"],
        ]),
    },
    "ict-computer-science-g1-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Pencil tool", "Draws thin lines"], ["Fill tool", "Colors in a shape"],
        ]),
    },
    "ict-computer-science-g1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Robot", "A machine that can be programmed to do tasks"],
            ["Sensor", "A part that lets a robot detect its surroundings"],
        ]),
    },
    "ict-computer-science-g1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A set of step-by-step instructions"], ["Sequence", "The order steps happen in"],
        ]),
    },
    "ict-computer-science-g1-l13": {
        "data_table": table(["Device", "Common Use"], [
            ["Smartphone", "Calling, texting, apps"], ["Television", "Watching shows and movies"],
        ]),
    },
    "ict-computer-science-g1-l14": {
        "data_table": table(["Care Tip", "Why"], [
            ["Keep away from liquids", "Prevents damage"], ["Handle gently", "Prevents drops and cracks"],
        ]),
    },
    "ict-computer-science-g1-l15": {
        "data_table": table(["Command", "Effect"], [
            ["Move forward", "Character moves one step"], ["Turn", "Character changes direction"],
        ]),
    },
    "ict-computer-science-g1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Message", "A short piece of written communication"],
            ["Send", "Delivering the message to someone else"],
        ]),
    },
    "ict-computer-science-g1-l17": {
        "data_table": table(["Step", "Action"], [
            ["1", "Computer sends the document to the printer"],
            ["2", "Printer puts ink or toner on paper"], ["3", "Paper comes out printed"],
        ]),
    },
    "ict-computer-science-g1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital camera", "Captures pictures and stores them electronically"],
            ["Photo", "A saved image you can view or print"],
        ]),
    },
    "ict-computer-science-g1-l19": {
        "data_table": table(["Concept", "Example"], [
            ["Sorting", "Putting numbers in order from smallest to largest"],
            ["Pattern", "A repeating sequence like Red, Blue, Red, Blue"],
        ]),
    },
    "ict-computer-science-g1-l20": {
        "data_table": table(["Activity Type", "Example"], [
            ["Screen time", "Watching videos, playing games"],
            ["Offline time", "Playing outside, reading a book"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["ICT & Computer Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json ICT: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 ICT lessons (completing 20/20).")


if __name__ == "__main__":
    main()
