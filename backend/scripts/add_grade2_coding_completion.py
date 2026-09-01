#!/usr/bin/env python3
"""Depth pass, Grade 2 Coding: fill in real, hand-checked data_table
content for the 18 Grade 2 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 2 Coding to full 20/20 coverage.

Content covers real, basic computer-science terminology (algorithm,
decomposition, debugging, sprite/costume in Scratch-style block coding)
-- nothing fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A set of step-by-step instructions"],
            ["Example", "A recipe is an algorithm for cooking"],
        ]),
    },
    "coding-g2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer program", "A set of instructions a computer follows"],
            ["Code", "The instructions written in a programming language"],
        ]),
    },
    "coding-g2-l3": {
        "data_table": table(["Step", "Action"], [
            ["1", "Wake up"], ["2", "Brush teeth"], ["3", "Get dressed"],
        ]),
    },
    "coding-g2-l4": {
        "data_table": table(["Direction", "Movement"], [
            ["Up", "Moves upward"], ["Down", "Moves downward"], ["Left", "Moves left"], ["Right", "Moves right"],
        ]),
    },
    "coding-g2-l6": {
        "data_table": table(["Condition", "Then"], [
            ["If it's raining", "Then bring an umbrella"], ["If the light is red", "Then stop"],
        ]),
    },
    "coding-g2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "A mistake in code"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "coding-g2-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Block", "A puzzle-piece instruction you snap together"],
            ["Block-based coding", "Building programs by connecting blocks (e.g. Scratch)"],
        ]),
    },
    "coding-g2-l9": {
        "data_table": table(["Block Command", "Effect"], [
            ["Move 10 steps", "Sprite moves forward"], ["Turn 15 degrees", "Sprite rotates"],
        ]),
    },
    "coding-g2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Animation", "A series of images shown quickly to create movement"],
            ["Costume", "A different image/pose for a sprite"],
        ]),
    },
    "coding-g2-l11": {
        "data_table": table(["Pattern", "Example"], [
            ["Repeating pattern", "repeat 3: move, turn"],
            ["Sequence pattern", "Step 1, then Step 2, then Step 3"],
        ]),
    },
    "coding-g2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Decomposition", "Breaking a big problem into smaller parts"],
            ["Example", "Making a sandwich = get bread + add filling + close it"],
        ]),
    },
    "coding-g2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Robot", "A machine that can be programmed to do tasks"],
            ["Sensor", "A part that lets a robot detect its surroundings"],
        ]),
    },
    "coding-g2-l15": {
        "data_table": table(["Instruction", "Robot Action"], [
            ["Move forward", "Robot moves ahead"], ["Turn left", "Robot rotates left"],
        ]),
    },
    "coding-g2-l16": {
        "data_table": table(["Sort Type", "Example"], [
            ["Alphabetical", "Apple, Banana, Cherry"], ["Numerical", "1, 2, 3, 4"],
        ]),
    },
    "coding-g2-l17": {
        "data_table": table(["Event", "Triggered Action"], [
            ["Click the green flag", "Program starts"], ["Press spacebar", "Character jumps"],
        ]),
    },
    "coding-g2-l18": {
        "data_table": table(["Story Element", "Coding Equivalent"], [
            ["Character", "Sprite"], ["Setting", "Background"], ["Plot", "Sequence of blocks"],
        ]),
    },
    "coding-g2-l19": {
        "data_table": table(["Variable", "Value Stored"], [
            ["score", "0"], ["lives", "3"],
        ]),
    },
    "coding-g2-l20": {
        "data_table": table(["Step", "Action"], [
            ["1", "Get two slices of bread"], ["2", "Add filling"], ["3", "Put the slices together"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Coding lessons (completing 20/20).")


if __name__ == "__main__":
    main()
