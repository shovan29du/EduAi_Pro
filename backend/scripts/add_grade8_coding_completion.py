#!/usr/bin/env python3
"""Depth pass, Grade 8 Coding: fill in real, hand-checked data_table
content for the 38 Grade 8 Coding lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Coding to full 40/40 coverage.

Examples use real, runnable Python/HTML/CSS/SQL syntax where applicable.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "code-g8-l1": {
        "data_table": table(["Concept", "Example"], [
            ["Dictionary", "student = {'name': 'Sam'}"], ["File handling", "open('notes.txt', 'w')"],
        ]),
        "formulae": ["with open(\"notes.txt\", \"w\") as f:", "    f.write(\"Hello\")"],
    },
    "coding-g8-l2": {
        "data_table": table(["Concept", "Example"], [
            ["print()", "print('Hello, world!')"],
        ]),
        "formulae": ["print(\"Hello, world!\")"],
    },
    "coding-g8-l3": {
        "data_table": table(["Data Type", "Example"], [
            ["int", "5"], ["float", "3.14"], ["str", "'hello'"], ["bool", "True"],
        ]),
    },
    "coding-g8-l4": {
        "data_table": table(["Operator", "Meaning"], [
            ["+", "Addition"], ["==", "Equal to"], ["%", "Modulus (remainder)"],
        ]),
    },
    "coding-g8-l5": {
        "data_table": table(["Function", "Purpose"], [
            ["print()", "Displays output"], ["input()", "Gets typed text from the user"],
        ]),
    },
    "coding-g8-l6": {
        "data_table": table(["Statement", "Meaning"], [
            ["if", "Runs if a condition is true"], ["elif", "Checks another condition"], ["else", "Runs if none are true"],
        ]),
        "formulae": ["if score >= 90:", "    print(\"A\")", "else:", "    print(\"B\")"],
    },
    "coding-g8-l7": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for i in range(5): print(i)"], ["while", "while count < 5: count += 1"],
        ]),
    },
    "coding-g8-l8": {
        "data_table": table(["Method", "Effect"], [
            [".append()", "Adds an item to the end"], [".sort()", "Sorts the list"],
        ]),
    },
    "coding-g8-l9": {
        "data_table": table(["Structure", "Example"], [
            ["Tuple", "point = (3, 5)"], ["Set", "colors = {'red', 'blue'}"],
        ]),
    },
    "coding-g8-l10": {
        "data_table": table(["Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".split()", "Breaks a string into a list"],
        ]),
    },
    "coding-g8-l11": {
        "data_table": table(["Concept", "Example"], [
            ["Function", "def add(a, b): return a + b"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "coding-g8-l12": {
        "data_table": table(["Scope", "Meaning"], [
            ["Local", "A variable defined inside a function"], ["Global", "A variable defined outside any function"],
        ]),
    },
    "coding-g8-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Recursion", "A function that calls itself to solve a smaller version of the problem"],
        ]),
        "formulae": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"],
    },
    "coding-g8-l14": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Code that might raise an error"], ["except", "Handles the error if raised"],
        ]),
        "formulae": ["try:", "    x = 1 / 0", "except ZeroDivisionError:", "    print(\"Can't divide by zero\")"],
    },
    "coding-g8-l15": {
        "data_table": table(["Concept", "Meaning"], [
            ["OOP", "Programming organized around objects that hold data and behavior"],
        ]),
    },
    "coding-g8-l16": {
        "data_table": table(["Concept", "Example"], [
            ["Class", "class Dog:"], ["Object", "my_dog = Dog()"],
        ]),
        "formulae": ["class Dog:", "    def bark(self):", "        print(\"Woof\")", "my_dog = Dog()", "my_dog.bark()"],
    },
    "coding-g8-l18": {
        "data_table": table(["Concept", "Example"], [
            ["Module", "import math"], ["Library", "A collection of pre-written code"],
        ]),
        "formulae": ["import math", "print(math.sqrt(16))"],
    },
    "coding-g8-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithm", "A step-by-step set of instructions to solve a problem"],
        ]),
    },
    "coding-g8-l21": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Linear search", "Checks each item one at a time"], ["Binary search", "Repeatedly halves a sorted list"],
        ]),
    },
    "coding-g8-l22": {
        "data_table": table(["Algorithm", "How It Works"], [
            ["Bubble sort", "Repeatedly swaps adjacent out-of-order items"],
        ]),
    },
    "coding-g8-l23": {
        "data_table": table(["Complexity", "Meaning"], [
            ["O(n)", "Time grows linearly with input size"], ["O(n^2)", "Time grows with the square of input size"],
        ]),
    },
    "coding-g8-l24": {
        "data_table": table(["Data Structure", "Example Use"], [
            ["List", "An ordered collection of items"], ["Dictionary", "Key-value pairs for fast lookup"],
        ]),
    },
    "coding-g8-l25": {
        "data_table": table(["Structure", "Behavior"], [
            ["Stack", "Last in, first out (LIFO)"], ["Queue", "First in, first out (FIFO)"],
        ]),
    },
    "coding-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Bug", "An error in a program"], ["Debugging", "Finding and fixing bugs"],
        ]),
    },
    "coding-g8-l27": {
        "data_table": table(["Flowchart Symbol", "Meaning"], [
            ["Oval", "Start or end"], ["Diamond", "A decision point"],
        ]),
    },
    "coding-g8-l28": {
        "data_table": table(["HTML Tag", "Purpose"], [
            ["<h1>", "Heading"], ["<p>", "Paragraph"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "coding-g8-l29": {
        "data_table": table(["CSS Property", "Effect"], [
            ["color", "Sets text color"], ["font-size", "Sets text size"],
        ]),
        "formulae": ["p { color: blue; font-size: 16px; }"],
    },
    "coding-g8-l30": {
        "data_table": table(["JavaScript Concept", "Example"], [
            ["Variable", "let x = 5;"], ["Function", "function greet() { return 'Hi'; }"],
        ]),
    },
    "coding-g8-l31": {
        "data_table": table(["Tag", "Role"], [
            ["<html>", "Root element of the page"], ["<body>", "Holds visible content"],
        ]),
    },
    "coding-g8-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Database", "An organized collection of data"], ["Table", "Stores rows and columns of data"],
        ]),
    },
    "coding-g8-l33": {
        "data_table": table(["SQL Command", "Purpose"], [
            ["SELECT", "Retrieves data"], ["INSERT", "Adds new data"],
        ]),
        "formulae": ["SELECT name FROM students WHERE grade = 8;"],
    },
    "coding-g8-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Version control", "Tracks changes to code over time"], ["Commit", "Saves a snapshot of changes"],
        ]),
    },
    "coding-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A way for programs to communicate with each other"],
        ]),
    },
    "coding-g8-l36": {
        "data_table": table(["Game Element", "Purpose"], [
            ["input()", "Gets the player's typed response"], ["if/else", "Decides what happens based on the answer"],
        ]),
    },
    "coding-g8-l37": {
        "data_table": table(["Command", "Effect"], [
            ["forward(100)", "Moves the turtle forward 100 units"], ["right(90)", "Turns the turtle right 90 degrees"],
        ]),
    },
    "coding-g8-l38": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cybersecurity", "Protecting computer systems from unauthorized access"],
        ]),
    },
    "coding-g8-l39": {
        "data_table": table(["Principle", "Meaning"], [
            ["Give credit", "Don't claim others' code as your own"],
            ["Respect privacy", "Don't collect personal data without permission"],
        ]),
    },
    "coding-g8-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems that perform tasks that normally require human intelligence"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Coding lessons (completing 40/40).")


if __name__ == "__main__":
    main()
