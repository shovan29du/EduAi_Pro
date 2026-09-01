#!/usr/bin/env python3
"""Depth pass, Grade 5 Coding: fill in real, hand-checked data_table
content for the 28 Grade 5 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 5 Coding to full 30/30 coverage.

This grade introduces Python; examples use real, runnable Python syntax.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g5-l1": {
        "data_table": table(["Concept", "Example"], [
            ["print()", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "coding-g5-l2": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["float", "3.14"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "coding-g5-l3": {
        "data_table": table(["String Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".lower()", "Converts to lowercase"],
        ]),
        "formulae": ["name = \"Sam\"", "print(name.upper())"],
    },
    "coding-g5-l4": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs code if a condition is true"], ["else", "Runs code if the condition is false"],
        ]),
        "formulae": ["if score >= 60:", "    print(\"Pass\")", "else:", "    print(\"Try again\")"],
    },
    "coding-g5-l5": {
        "data_table": table(["Operator", "Meaning"], [
            ["==", "Equal to"], ["and", "Both conditions true"], ["or", "Either condition true"],
        ]),
    },
    "coding-g5-l6": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"],
        ]),
        "formulae": ["for i in range(5):", "    print(i)"],
    },
    "coding-g5-l7": {
        "data_table": table(["Loop", "Example"], [
            ["while", "while count < 5: count += 1"],
        ]),
        "formulae": ["count = 0", "while count < 5:", "    count += 1"],
    },
    "coding-g5-l8": {
        "data_table": table(["Operation", "Example"], [
            ["Create a list", "fruits = ['apple', 'banana']"],
        ]),
        "formulae": ["fruits = [\"apple\", \"banana\"]"],
    },
    "coding-g5-l9": {
        "data_table": table(["Method", "Effect"], [
            [".append()", "Adds an item to the end"], [".remove()", "Removes a matching item"], [".sort()", "Sorts the list"],
        ]),
    },
    "coding-g5-l11": {
        "data_table": table(["Concept", "Example"], [
            ["Function definition", "def greet(): print('Hi')"],
        ]),
        "formulae": ["def greet():", "    print(\"Hi\")"],
    },
    "coding-g5-l12": {
        "data_table": table(["Concept", "Example"], [
            ["Parameter", "def add(a, b):"], ["Return value", "return a + b"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "coding-g5-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "An error in a program"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "coding-g5-l14": {
        "data_table": table(["Error Type", "Meaning"], [
            ["SyntaxError", "Code doesn't follow the language's rules"],
            ["NameError", "A variable isn't defined"],
        ]),
    },
    "coding-g5-l15": {
        "data_table": table(["Practice", "Benefit"], [
            ["Comments (#)", "Explains what code does"], ["Clear variable names", "Makes code easier to read"],
        ]),
    },
    "coding-g5-l16": {
        "data_table": table(["Concept", "Example"], [
            ["Nested loop", "A loop inside another loop"],
        ]),
        "formulae": ["for i in range(3):", "    for j in range(2):", "        print(i, j)"],
    },
    "coding-g5-l17": {
        "data_table": table(["Value", "Meaning"], [
            ["True", "A condition that is met"], ["False", "A condition that is not met"],
        ]),
    },
    "coding-g5-l19": {
        "data_table": table(["Command", "Effect"], [
            ["forward(100)", "Moves the turtle forward 100 units"], ["right(90)", "Turns the turtle right 90 degrees"],
        ]),
    },
    "coding-g5-l20": {
        "data_table": table(["Game Element", "Purpose"], [
            ["input()", "Gets the player's typed response"], ["if/else", "Decides what happens based on the answer"],
        ]),
    },
    "coding-g5-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "coding-g5-l22": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"], ["Rectangle", "A process step"],
        ]),
    },
    "coding-g5-l23": {
        "data_table": table(["Block Concept", "Text Equivalent"], [
            ["Repeat 10 times", "for i in range(10):"], ["If-then block", "if condition:"],
        ]),
    },
    "coding-g5-l24": {
        "data_table": table(["Function", "Purpose"], [
            ["input()", "Gets typed text from the user"],
        ]),
        "formulae": ["name = input(\"What is your name? \")", "print(\"Hello, \" + name)"],
    },
    "coding-g5-l25": {
        "data_table": table(["Concept", "Example"], [
            ["Data validation", "Checking that input is a valid number before using it"],
        ]),
    },
    "coding-g5-l26": {
        "data_table": table(["Concept", "Benefit"], [
            ["Modular program", "Splits code into reusable functions"],
        ]),
    },
    "coding-g5-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks changes to code over time"], ["Commit", "Saves a snapshot of changes"],
        ]),
    },
    "coding-g5-l28": {
        "data_table": table(["Principle", "Meaning"], [
            ["Give credit", "Don't claim others' code as your own"],
            ["Respect privacy", "Don't collect personal data without permission"],
        ]),
    },
    "coding-g5-l29": {
        "data_table": table(["Structure", "Example"], [
            ["Tuple", "coordinates = (3, 5)"],
        ]),
        "formulae": ["coordinates = (3, 5)"],
    },
    "coding-g5-l30": {
        "data_table": table(["Planning Step", "Purpose"], [
            ["Define the goal", "Know what the program should do"],
            ["Sketch the steps", "Plan the logic before writing code"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Coding lessons (completing 30/30).")


if __name__ == "__main__":
    main()
