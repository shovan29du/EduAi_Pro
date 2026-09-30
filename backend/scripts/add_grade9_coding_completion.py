#!/usr/bin/env python3
"""Depth pass, Grade 9 Coding: fill in real, hand-checked data_table
content for the 48 Grade 9 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Coding to full 50/50 coverage.

Examples use real, runnable Python/HTML/CSS/SQL syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g9-l1": {
        "data_table": table(["Concept", "Example"], [
            ["Class", "class Dog:"], ["Object", "my_dog = Dog()"],
        ]),
        "formulae": ["class Dog:", "    def bark(self):", "        print(\"Woof\")"],
    },
    "coding-g9-l2": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "coding-g9-l3": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs if a condition is true"], ["else", "Runs if the condition is false"],
        ]),
    },
    "coding-g9-l4": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"], ["while", "while count < 5: count += 1"],
        ]),
    },
    "coding-g9-l5": {
        "data_table": table(["Concept", "Example"], [
            ["Function", "def add(a, b): return a + b"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "coding-g9-l6": {
        "data_table": table(["Structure", "Example"], [
            ["Array/List", "fruits = ['apple', 'banana']"],
        ]),
    },
    "coding-g9-l7": {
        "data_table": table(["Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".split()", "Breaks a string into a list"],
        ]),
    },
    "coding-g9-l8": {
        "data_table": table(["Concept", "Example"], [
            ["Dictionary", "student = {'name': 'Sam'}"],
        ]),
    },
    "coding-g9-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Recursion", "A function that calls itself to solve a smaller version of the problem"],
        ]),
        "formulae": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"],
    },
    "coding-g9-l10": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Linear search", "Checks each item one at a time"], ["Binary search", "Repeatedly halves a sorted list"],
        ]),
    },
    "coding-g9-l11": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Bubble sort", "Repeatedly swaps adjacent out-of-order items"],
        ]),
    },
    "coding-g9-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "An error in a program"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "coding-g9-l14": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Code that might raise an error"], ["except", "Handles the error if raised"],
        ]),
        "formulae": ["try:", "    x = 1 / 0", "except ZeroDivisionError:", "    print(\"Can't divide by zero\")"],
    },
    "coding-g9-l15": {
        "data_table": table(["Concept", "Example"], [
            ["print()", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "coding-g9-l16": {
        "data_table": table(["JavaScript Concept", "Example"], [
            ["Variable", "let x = 5;"], ["Function", "function greet() { return 'Hi'; }"],
        ]),
    },
    "coding-g9-l18": {
        "data_table": table(["Function", "Purpose"], [
            ["open()", "Opens a file"], ["write()", "Writes text to a file"],
        ]),
        "formulae": ["with open(\"notes.txt\", \"w\") as f:", "    f.write(\"Hello\")"],
    },
    "coding-g9-l19": {
        "data_table": table(["HTML Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "coding-g9-l20": {
        "data_table": table(["CSS Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
        "formulae": ["p { color: blue; font-size: 16px; }"],
    },
    "coding-g9-l21": {
        "data_table": table(["Tag", "Role"], [
            ["<html>", "Root element of the page"], ["<body>", "Holds visible content"],
        ]),
    },
    "coding-g9-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"], ["Table", "Stores rows and columns of data"],
        ]),
    },
    "coding-g9-l23": {
        "data_table": table(["SQL Command", "Purpose"], [
            ["SELECT", "Retrieves data"], ["WHERE", "Filters results"],
        ]),
        "formulae": ["SELECT name FROM students WHERE grade = 9;"],
    },
    "coding-g9-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A way for programs to communicate with each other"],
        ]),
    },
    "coding-g9-l25": {
        "data_table": table(["Data Structure", "Example Use"], [
            ["List", "An ordered collection of items"], ["Dictionary", "Key-value pairs for fast lookup"],
        ]),
    },
    "coding-g9-l26": {
        "data_table": table(["Structure", "Behavior"], [
            ["Stack", "Last in, first out (LIFO)"], ["Queue", "First in, first out (FIFO)"],
        ]),
    },
    "coding-g9-l27": {
        "data_table": table(["Structure", "Description"], [
            ["Linked list", "A sequence of nodes, each pointing to the next"],
        ]),
    },
    "coding-g9-l28": {
        "data_table": table(["Structure", "Description"], [
            ["Binary tree", "A tree where each node has at most two children"],
        ]),
    },
    "coding-g9-l29": {
        "data_table": table(["Structure", "Description"], [
            ["Hash table", "Stores data using key-value pairs for fast lookup"],
        ]),
    },
    "coding-g9-l30": {
        "data_table": table(["Operator", "Meaning"], [
            ["AND", "True only if both are true"], ["OR", "True if either is true"], ["NOT", "Reverses the value"],
        ]),
    },
    "coding-g9-l31": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"],
        ]),
    },
    "coding-g9-l32": {
        "data_table": table(["SDLC Phase", "Purpose"], [
            ["Requirements", "Defines what the software should do"], ["Testing", "Verifies the software works correctly"],
        ]),
    },
    "coding-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Agile", "An iterative approach to software development"], ["Sprint", "A short, fixed development cycle"],
        ]),
    },
    "coding-g9-l34": {
        "data_table": table(["App Type", "Example"], [
            ["Mobile app", "Runs on smartphones"], ["Web app", "Runs in a browser"],
        ]),
    },
    "coding-g9-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Event", "Something that triggers an action"], ["Event handler", "Code that responds to an event"],
        ]),
    },
    "coding-g9-l36": {
        "data_table": table(["Game Element", "Purpose"], [
            ["Game loop", "Continuously updates the game state"], ["Win condition", "Determines when the player wins"],
        ]),
    },
    "coding-g9-l37": {
        "data_table": table(["Concept", "Purpose"], [
            ["Frame rate", "How many images are shown per second"],
        ]),
    },
    "coding-g9-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that perform tasks that normally require human intelligence"],
        ]),
    },
    "coding-g9-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine learning", "A type of AI where systems learn from data"],
        ]),
    },
    "coding-g9-l40": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "coding-g9-l41": {
        "data_table": table(["Network Type", "Description"], [
            ["LAN", "Local Area Network"], ["WAN", "Wide Area Network"],
        ]),
    },
    "coding-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Internet", "A global network connecting computers"], ["Router", "Directs data between devices"],
        ]),
    },
    "coding-g9-l43": {
        "data_table": table(["Decimal", "Binary"], [
            ["0", "0"], ["1", "1"], ["2", "10"], ["4", "100"],
        ]),
    },
    "coding-g9-l44": {
        "data_table": table(["Component", "Purpose"], [
            ["Sensor", "Detects things like light or distance"], ["Motor", "Makes the robot move"],
        ]),
    },
    "coding-g9-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Testing", "Verifying that software works as intended"], ["Bug", "An error found during testing"],
        ]),
    },
    "coding-g9-l46": {
        "data_table": table(["Practice", "Benefit"], [
            ["Comments (#)", "Explains what code does"], ["Clear variable names", "Makes code easier to read"],
        ]),
    },
    "coding-g9-l47": {
        "data_table": table(["Concept", "Example"], [
            ["Module", "import math"], ["Library", "A collection of pre-written code"],
        ]),
    },
    "coding-g9-l48": {
        "data_table": table(["Command", "Purpose"], [
            ["ls", "Lists files in a directory"], ["cd", "Changes the current directory"],
        ]),
    },
    "coding-g9-l49": {
        "data_table": table(["Principle", "Meaning"], [
            ["Give credit", "Don't claim others' code as your own"],
            ["Respect privacy", "Don't collect personal data without permission"],
        ]),
    },
    "coding-g9-l50": {
        "data_table": table(["Career", "Focus"], [
            ["Software developer", "Writes and maintains programs"], ["Data scientist", "Analyzes data for insights"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Coding lessons (completing 50/50).")


if __name__ == "__main__":
    main()
