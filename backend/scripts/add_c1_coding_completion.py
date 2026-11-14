#!/usr/bin/env python3
"""Depth pass, C1 Coding: fill in real, hand-checked data_table and
formulae (real code) content for the 69 C1 Coding lessons not covered
by the earlier breadth-first batch. Brings C1 Coding to full 70/70
coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_coding_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "coding-c1-l1": {
        "data_table": table(["Concept", "Meaning"], [
            ["Variable", "A named storage location for a value that can change"],
        ]),
    },
    "coding-c1-l2": {
        "data_table": table(["Structure", "Use"], [
            ["Array", "Stores an ordered collection of items"], ["Linked list", "Stores items as nodes connected by pointers"],
        ]),
    },
    "coding-c1-l4": {
        "data_table": table(["Concept", "Example"], [
            ["Base case", "The condition that stops recursion"], ["Recursive case", "The step that calls the function on a smaller subproblem"],
        ]),
        "formulae": ["def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)"],
    },
    "coding-c1-l5": {
        "data_table": table(["Algorithm", "Time Complexity"], [
            ["Bubble sort", "O(n^2)"], ["Binary search", "O(log n)"],
        ]),
    },
    "coding-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Dynamic programming", "Solving problems by breaking them into overlapping subproblems and caching results"],
        ]),
    },
    "coding-c1-l7": {
        "data_table": table(["Traversal", "Order"], [
            ["BFS", "Explores neighbors level by level using a queue"], ["DFS", "Explores as deep as possible before backtracking, using a stack"],
        ]),
    },
    "coding-c1-l8": {
        "data_table": table(["Property", "Rule"], [
            ["Binary search tree", "Left child less than parent, right child greater than parent"],
        ]),
    },
    "coding-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Hash table", "Stores key-value pairs using a hash function for fast lookup"],
        ]),
        "formulae": ["d = {}\nd['apple'] = 1\nprint(d['apple'])"],
    },
    "coding-c1-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Class", "A blueprint for creating objects"], ["Object", "An instance of a class"],
        ]),
    },
    "coding-c1-l11": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Singleton", "Ensures only one instance of a class exists"], ["Observer", "Notifies dependents when an object changes state"],
        ]),
    },
    "coding-c1-l12": {
        "data_table": table(["Style", "Feature"], [
            ["Monolithic architecture", "Single deployable unit for the whole application"], ["Microservices", "Independent, loosely coupled services"],
        ]),
    },
    "coding-c1-l13": {
        "data_table": table(["Command", "Purpose"], [
            ["git init", "Creates a new repository"], ["git commit", "Saves a snapshot of staged changes"],
        ]),
        "formulae": ["git init\ngit add .\ngit commit -m \"Initial commit\""],
    },
    "coding-c1-l14": {
        "data_table": table(["Practice", "Benefit"], [
            ["Peer code review", "Catches bugs and shares knowledge before merging"],
        ]),
    },
    "coding-c1-l15": {
        "data_table": table(["Technique", "Use"], [
            ["Print debugging", "Inserts print statements to trace values"], ["Breakpoints", "Pauses execution at a specific line"],
        ]),
    },
    "coding-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Unit test", "A test verifying a small, isolated piece of code behaves correctly"],
        ]),
        "formulae": ["def test_add():\n    assert add(2, 3) == 5"],
    },
    "coding-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Continuous integration", "Automatically building and testing code on every change"],
        ]),
    },
    "coding-c1-l18": {
        "data_table": table(["Region", "Purpose"], [
            ["Stack", "Stores function calls and local variables"], ["Heap", "Stores dynamically allocated objects"],
        ]),
    },
    "coding-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Concurrency", "Running multiple tasks in overlapping time periods"],
        ]),
    },
    "coding-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Parsing arguments", "Reads user input from the command line"],
        ]),
        "formulae": ["import sys\nprint(f\"Hello, {sys.argv[1]}!\")"],
    },
    "coding-c1-l21": {
        "data_table": table(["Type", "Example"], [
            ["Integer", "42"], ["String", "'hello'"], ["Boolean", "True"],
        ]),
        "formulae": ["x = 42\nname = \"hello\"\nis_valid = True"],
    },
    "coding-c1-l22": {
        "data_table": table(["Keyword", "Purpose"], [
            ["if", "Runs a block when a condition is true"], ["else", "Runs a block when the condition is false"],
        ]),
        "formulae": ["if x > 0:\n    print(\"positive\")\nelse:\n    print(\"non-positive\")"],
    },
    "coding-c1-l23": {
        "data_table": table(["Loop", "Use"], [
            ["for", "Iterates over a known sequence"], ["while", "Repeats while a condition holds"],
        ]),
        "formulae": ["for i in range(5):\n    print(i)"],
    },
    "coding-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Parameter", "A named input a function accepts"], ["Return value", "The output a function produces"],
        ]),
        "formulae": ["def add(a, b):\n    return a + b"],
    },
    "coding-c1-l25": {
        "data_table": table(["Operation", "Example"], [
            ["Append", "arr.append(4)"], ["Index access", "arr[0]"],
        ]),
        "formulae": ["arr = [1, 2, 3]\narr.append(4)\nprint(arr[0])"],
    },
    "coding-c1-l26": {
        "data_table": table(["Method", "Purpose"], [
            ["split()", "Divides a string into a list"], ["join()", "Combines a list into a string"],
        ]),
        "formulae": ["s = \"a,b,c\"\nparts = s.split(\",\")"],
    },
    "coding-c1-l27": {
        "data_table": table(["Operation", "Example"], [
            ["Set a key", "d['key'] = 'value'"], ["Get a key", "d['key']"],
        ]),
        "formulae": ["d = {\"a\": 1, \"b\": 2}\nprint(d[\"a\"])"],
    },
    "coding-c1-l28": {
        "data_table": table(["Operation", "Purpose"], [
            ["Open a file", "Grants read or write access to a file on disk"],
        ]),
        "formulae": ["with open(\"data.txt\", \"r\") as f:\n    content = f.read()"],
    },
    "coding-c1-l29": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Wraps code that might raise an error"], ["except", "Handles a raised error"],
        ]),
        "formulae": ["try:\n    risky()\nexcept ValueError as e:\n    print(e)"],
    },
    "coding-c1-l30": {
        "data_table": table(["Concept", "Meaning"], [
            ["Command-line argument", "A value passed to a program when it is launched"],
        ]),
    },
    "coding-c1-l31": {
        "data_table": table(["Pattern", "Matches"], [
            ["\\d+", "One or more digits"], ["^[A-Z]", "A string starting with a capital letter"],
        ]),
        "formulae": ["import re\nre.match(r\"\\d+\", \"123abc\")"],
    },
    "coding-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["JSON", "A lightweight, human-readable data interchange format"],
        ]),
        "formulae": ["{\"name\": \"Sam\", \"age\": 20}"],
    },
    "coding-c1-l33": {
        "data_table": table(["Method", "Purpose"], [
            ["GET", "Retrieves data from a server"], ["POST", "Sends data to a server"],
        ]),
    },
    "coding-c1-l34": {
        "data_table": table(["Type", "Example"], [
            ["Relational database", "MySQL, PostgreSQL"], ["NoSQL database", "MongoDB"],
        ]),
    },
    "coding-c1-l35": {
        "data_table": table(["Clause", "Purpose"], [
            ["SELECT", "Chooses which columns to return"], ["WHERE", "Filters rows by condition"],
        ]),
        "formulae": ["SELECT name FROM users WHERE age > 18;"],
    },
    "coding-c1-l36": {
        "data_table": table(["Concept", "Meaning"], [
            ["Constructor", "A special method that initializes a new object"],
        ]),
        "formulae": ["class Dog:\n    def __init__(self, name):\n        self.name = name"],
    },
    "coding-c1-l37": {
        "data_table": table(["Concept", "Meaning"], [
            ["Inheritance", "A class acquiring properties and methods from a parent class"], ["Polymorphism", "Different classes responding to the same method call in their own way"],
        ]),
    },
    "coding-c1-l38": {
        "data_table": table(["Concept", "Meaning"], [
            ["Interface", "Defines a contract of methods a class must implement"],
        ]),
    },
    "coding-c1-l39": {
        "data_table": table(["Concept", "Meaning"], [
            ["Pure function", "A function whose output depends only on its inputs, with no side effects"],
        ]),
        "formulae": ["squares = list(map(lambda x: x * x, [1, 2, 3]))"],
    },
    "coding-c1-l40": {
        "data_table": table(["Application", "Example"], [
            ["Tree traversal", "Recursively visiting each node of a tree"],
        ]),
    },
    "coding-c1-l41": {
        "data_table": table(["Strategy", "Example"], [
            ["Greedy", "Makes the locally optimal choice at each step"], ["Divide and conquer", "Breaks a problem into independent subproblems"],
        ]),
    },
    "coding-c1-l42": {
        "data_table": table(["Notation", "Meaning"], [
            ["O(1)", "Constant time, independent of input size"], ["O(n)", "Time grows linearly with input size"],
        ]),
    },
    "coding-c1-l43": {
        "data_table": table(["Framework", "Language"], [
            ["pytest", "Python"], ["Jest", "JavaScript"],
        ]),
        "formulae": ["def test_multiply():\n    assert multiply(3, 4) == 12"],
    },
    "coding-c1-l44": {
        "data_table": table(["Action", "Purpose"], [
            ["Set a breakpoint", "Pauses execution to inspect variable state"],
        ]),
    },
    "coding-c1-l45": {
        "data_table": table(["Practice", "Benefit"], [
            ["Descriptive naming", "Makes code self-explanatory without extra comments"],
        ]),
    },
    "coding-c1-l46": {
        "data_table": table(["Tool", "Language"], [
            ["pip", "Python"], ["npm", "JavaScript"],
        ]),
        "formulae": ["pip install requests"],
    },
    "coding-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Environment variable", "A named value in the operating system used to configure programs"],
        ]),
    },
    "coding-c1-l48": {
        "data_table": table(["Tag", "Purpose"], [
            ["<div>", "A generic container element"], ["<p>", "A paragraph of text"],
        ]),
        "formulae": ["<!DOCTYPE html>\n<html><body><h1>Hello</h1></body></html>"],
    },
    "coding-c1-l49": {
        "data_table": table(["Feature", "Purpose"], [
            ["DOM manipulation", "Changing page content dynamically after it loads"],
        ]),
        "formulae": ["document.getElementById(\"title\").textContent = \"Hello\";"],
    },
    "coding-c1-l50": {
        "data_table": table(["Verb", "Purpose"], [
            ["GET /items", "Retrieves a list of items"], ["POST /items", "Creates a new item"],
        ]),
    },
    "coding-c1-l51": {
        "data_table": table(["Type", "Purpose"], [
            ["README", "Explains what a project does and how to use it"], ["Docstring", "Documents a function or class inline"],
        ]),
    },
    "coding-c1-l52": {
        "data_table": table(["Tool", "Purpose"], [
            ["Prettier", "Automatically formats code style"], ["ESLint", "Flags code quality issues"],
        ]),
    },
    "coding-c1-l53": {
        "data_table": table(["Practice", "Benefit"], [
            ["Splitting code into modules", "Improves readability and reuse across a project"],
        ]),
    },
    "coding-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Dependency", "External code a project relies on to function"],
        ]),
    },
    "coding-c1-l55": {
        "data_table": table(["Check", "Purpose"], [
            ["Type validation", "Ensures input matches the expected data type"],
        ]),
    },
    "coding-c1-l56": {
        "data_table": table(["Tool", "Purpose"], [
            ["curl", "Sends HTTP requests from the terminal"], ["grep", "Searches text using patterns"],
        ]),
    },
    "coding-c1-l57": {
        "data_table": table(["Role", "Responsibility"], [
            ["Driver", "Writes the code"], ["Navigator", "Reviews and guides in real time"],
        ]),
    },
    "coding-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Sprint", "A fixed, short time period for completing a set of tasks"],
        ]),
    },
    "coding-c1-l59": {
        "data_table": table(["Step", "Purpose"], [
            ["Fork a repository", "Creates your own copy of an open-source project to modify"],
        ]),
    },
    "coding-c1-l60": {
        "data_table": table(["Layer", "Responsibility"], [
            ["Frontend", "Handles the user interface"], ["Backend", "Handles data and business logic"],
        ]),
    },
    "coding-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Writing a basic script", "Using variables and control flow to solve a small task"],
        ]),
    },
    "coding-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a data structure", "Picking a hash table over an array for fast lookups"],
        ]),
    },
    "coding-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Comparing algorithm efficiency", "Choosing binary search over linear search on sorted data"],
        ]),
        "formulae": ["Binary search: O(log n) vs. Linear search: O(n)"],
    },
    "coding-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a recursive call", "Following the call stack of a factorial function"],
        ]),
    },
    "coding-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a sort algorithm", "Selecting merge sort for large, stable datasets"],
        ]),
    },
    "coding-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Solving a DP problem", "Computing Fibonacci numbers with memoization"],
        ]),
        "formulae": ["def fib(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)\n    return memo[n]"],
    },
    "coding-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Traversing a graph", "Finding the shortest path between two nodes using BFS"],
        ]),
    },
    "coding-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Searching a BST", "Finding a value by comparing against each node"],
        ]),
    },
    "coding-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Using a hash table", "Counting word frequency in a block of text"],
        ]),
    },
    "coding-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Modeling with a class", "Designing a simple object with attributes and methods"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Coding"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Coding: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Coding lessons (completing 70/70).")


if __name__ == "__main__":
    main()
