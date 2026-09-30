#!/usr/bin/env python3
"""Depth pass, C1 Python: fill in real, hand-checked data_table content
for the 69 C1 Python lessons not covered by the earlier breadth-first
batch. Brings C1 Python to full 70/70 coverage.

Examples use real, runnable Python syntax.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_python_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "python-c1-l1": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "x = 5"], ["Comment", "# this is a comment"],
        ]),
        "formulae": ["x = 5", "print(x)"],
    },
    "python-c1-l2": {
        "data_table": table(["Structure", "Purpose"], [
            ["if statement", "Runs code conditionally"], ["Function", "Reusable block of code"],
        ]),
        "formulae": ["def greet(name):", "    return f\"Hello, {name}!\""],
    },
    "python-c1-l4": {
        "data_table": table(["Type", "Example"], [
            ["int", "5"], ["float", "3.14"],
        ]),
        "formulae": ["result = 7 // 2  # floor division = 3", "remainder = 7 % 2  # modulo = 1"],
    },
    "python-c1-l5": {
        "data_table": table(["Method", "Effect"], [
            [".upper()", "Converts to uppercase"], [".strip()", "Removes leading/trailing whitespace"],
        ]),
        "formulae": ["\"hello\".upper()  # 'HELLO'"],
    },
    "python-c1-l6": {
        "data_table": table(["Syntax", "Result"], [
            ["f\"{name} is {age}\"", "Embeds variables directly in a string"],
        ]),
        "formulae": ["name = \"Ana\"; age = 30", "print(f\"{name} is {age} years old\")"],
    },
    "python-c1-l7": {
        "data_table": table(["Operator", "Meaning"], [
            ["==", "Equal to"], ["!=", "Not equal to"],
        ]),
        "formulae": ["is_adult = age >= 18"],
    },
    "python-c1-l8": {
        "data_table": table(["Keyword", "Purpose"], [
            ["if", "Runs code when a condition is true"], ["elif", "Checks another condition"], ["else", "Runs when no condition matched"],
        ]),
        "formulae": ["if x > 0:", "    print(\"positive\")", "elif x == 0:", "    print(\"zero\")", "else:", "    print(\"negative\")"],
    },
    "python-c1-l9": {
        "data_table": table(["Function", "Example"], [
            ["range(5)", "Produces 0, 1, 2, 3, 4"],
        ]),
        "formulae": ["for i in range(5):", "    print(i)"],
    },
    "python-c1-l10": {
        "data_table": table(["Keyword", "Effect"], [
            ["break", "Exits the loop immediately"], ["continue", "Skips to the next iteration"],
        ]),
        "formulae": ["while count < 5:", "    count += 1"],
    },
    "python-c1-l11": {
        "data_table": table(["Keyword", "Purpose"], [
            ["def", "Defines a function"], ["return", "Sends a value back to the caller"],
        ]),
        "formulae": ["def add(a, b):", "    return a + b"],
    },
    "python-c1-l12": {
        "data_table": table(["Argument Type", "Example"], [
            ["Positional", "add(2, 3)"], ["Keyword", "add(a=2, b=3)"], ["Default", "def add(a, b=10):"],
        ]),
    },
    "python-c1-l13": {
        "data_table": table(["Scope", "Meaning"], [
            ["Local", "Variable defined inside a function"], ["Global", "Variable defined outside all functions"],
        ]),
    },
    "python-c1-l14": {
        "data_table": table(["Operation", "Example"], [
            ["Indexing", "fruits[0]"], ["Slicing", "fruits[1:3]"],
        ]),
        "formulae": ["fruits = [\"apple\", \"banana\", \"cherry\"]", "print(fruits[0])"],
    },
    "python-c1-l15": {
        "data_table": table(["Structure", "Feature"], [
            ["Tuple", "Ordered and immutable, e.g. (1, 2)"],
        ]),
        "formulae": ["point = (3, 4)"],
    },
    "python-c1-l16": {
        "data_table": table(["Structure", "Example"], [
            ["Dictionary", "student = {'name': 'Sam', 'age': 20}"],
        ]),
        "formulae": ["student = {\"name\": \"Sam\", \"age\": 20}", "print(student[\"name\"])"],
    },
    "python-c1-l17": {
        "data_table": table(["Operation", "Result"], [
            ["Union (|)", "Combines two sets"], ["Intersection (&)", "Common elements"],
        ]),
        "formulae": ["a = {1, 2, 3}", "b = {2, 3, 4}", "print(a & b)  # {2, 3}"],
    },
    "python-c1-l18": {
        "data_table": table(["Structure", "Example"], [
            ["List of dicts", "[{'id': 1}, {'id': 2}]"],
        ]),
    },
    "python-c1-l19": {
        "data_table": table(["Function", "Purpose"], [
            ["print()", "Displays output"], ["input()", "Reads user input as a string"],
        ]),
        "formulae": ["name = input(\"What's your name? \")", "print(f\"Hi {name}\")"],
    },
    "python-c1-l20": {
        "data_table": table(["Technique", "Purpose"], [
            ["Print debugging", "Inserts print statements to trace values"],
        ]),
    },
    "python-c1-l21": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Code that might raise an error"], ["except", "Handles the error if raised"],
        ]),
        "formulae": ["try:", "    x = 1 / 0", "except ZeroDivisionError:", "    print(\"Can't divide by zero\")"],
    },
    "python-c1-l22": {
        "data_table": table(["Concept", "Example"], [
            ["Custom exception", "class MyError(Exception): pass"],
        ]),
        "formulae": ["class InvalidAgeError(Exception):", "    pass"],
    },
    "python-c1-l23": {
        "data_table": table(["Concept", "Example"], [
            ["Lambda function", "square = lambda x: x * x"],
        ]),
        "formulae": ["square = lambda x: x * x", "print(square(5))  # 25"],
    },
    "python-c1-l24": {
        "data_table": table(["Concept", "Example"], [
            ["Base case", "Stops the recursion"],
        ]),
        "formulae": ["def factorial(n):", "    if n <= 1:", "        return 1", "    return n * factorial(n - 1)"],
    },
    "python-c1-l25": {
        "data_table": table(["Concept", "Example"], [
            ["Unpacking", "a, b = 1, 2"],
        ]),
        "formulae": ["a, b = 1, 2", "first, *rest = [1, 2, 3, 4]"],
    },
    "python-c1-l26": {
        "data_table": table(["Syntax", "Meaning"], [
            ["*args", "Collects extra positional arguments"], ["**kwargs", "Collects extra keyword arguments"],
        ]),
        "formulae": ["def total(*args):", "    return sum(args)"],
    },
    "python-c1-l27": {
        "data_table": table(["Function", "Purpose"], [
            ["enumerate()", "Pairs each item with its index"], ["zip()", "Combines multiple iterables"],
        ]),
        "formulae": ["for i, val in enumerate([\"a\", \"b\"]):", "    print(i, val)"],
    },
    "python-c1-l28": {
        "data_table": table(["Function", "Use"], [
            ["sorted()", "Returns a new sorted list"],
        ]),
        "formulae": ["names = sorted([\"Bob\", \"amy\"], key=str.lower)"],
    },
    "python-c1-l29": {
        "data_table": table(["Method", "Effect"], [
            [".append()", "Adds an item to the end"], [".pop()", "Removes and returns the last item"],
        ]),
    },
    "python-c1-l30": {
        "data_table": table(["Method", "Effect"], [
            [".get()", "Retrieves a value with a default"], [".keys()", "Returns all keys"],
        ]),
        "formulae": ["student.get(\"grade\", \"N/A\")"],
    },
    "python-c1-l31": {
        "data_table": table(["Slice", "Result"], [
            ["s[::-1]", "Reverses the string"],
        ]),
        "formulae": ["\"hello\"[::-1]  # 'olleh'"],
    },
    "python-c1-l32": {
        "data_table": table(["Statement", "Purpose"], [
            ["import math", "Loads the math module"],
        ]),
        "formulae": ["import math", "print(math.sqrt(16))"],
    },
    "python-c1-l33": {
        "data_table": table(["File", "Purpose"], [
            ["mymodule.py", "A file containing reusable functions to import elsewhere"],
        ]),
    },
    "python-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Virtual environment", "An isolated Python installation for a specific project"],
        ]),
        "formulae": ["python -m venv env", "source env/bin/activate"],
    },
    "python-c1-l35": {
        "data_table": table(["Command", "Purpose"], [
            ["pip install requests", "Installs the requests package"],
        ]),
        "formulae": ["pip install requests"],
    },
    "python-c1-l36": {
        "data_table": table(["Concept", "Example"], [
            ["Docstring", "\"\"\"Explains what a function does.\"\"\""],
        ]),
        "formulae": ["def add(a, b):", "    \"\"\"Return the sum of a and b.\"\"\"", "    return a + b"],
    },
    "python-c1-l37": {
        "data_table": table(["Concept", "Example"], [
            ["Type hint", "def add(a: int, b: int) -> int:"],
        ]),
        "formulae": ["def add(a: int, b: int) -> int:", "    return a + b"],
    },
    "python-c1-l38": {
        "data_table": table(["Concept", "Example"], [
            ["Test case", "self.assertEqual(add(2,3), 5)"],
        ]),
        "formulae": ["import unittest", "class TestAdd(unittest.TestCase):", "    def test_add(self):", "        self.assertEqual(add(2, 3), 5)"],
    },
    "python-c1-l39": {
        "data_table": table(["Pattern", "Matches"], [
            ["\\d+", "One or more digits"],
        ]),
        "formulae": ["import re", "re.findall(r\"\\d+\", \"a1 b22\")  # ['1', '22']"],
    },
    "python-c1-l40": {
        "data_table": table(["Function", "Use"], [
            ["datetime.now()", "Gets the current date and time"],
        ]),
        "formulae": ["from datetime import datetime", "print(datetime.now())"],
    },
    "python-c1-l41": {
        "data_table": table(["Function", "Use"], [
            ["math.sqrt()", "Square root"], ["math.pi", "The value of pi"],
        ]),
        "formulae": ["import math", "math.sqrt(25)  # 5.0"],
    },
    "python-c1-l42": {
        "data_table": table(["Function", "Use"], [
            ["random.randint(1,6)", "Random integer between 1 and 6"],
        ]),
        "formulae": ["import random", "random.randint(1, 6)"],
    },
    "python-c1-l43": {
        "data_table": table(["Function", "Use"], [
            ["os.path.join()", "Builds a file path safely"],
        ]),
        "formulae": ["import os", "os.path.join(\"folder\", \"file.txt\")"],
    },
    "python-c1-l44": {
        "data_table": table(["Attribute", "Meaning"], [
            ["sys.argv", "List of command-line arguments passed to the script"],
        ]),
        "formulae": ["import sys", "print(sys.argv[1])"],
    },
    "python-c1-l45": {
        "data_table": table(["Idiom", "Purpose"], [
            ["if __name__ == \"__main__\":", "Runs code only when the file is executed directly"],
        ]),
        "formulae": ["if __name__ == \"__main__\":", "    main()"],
    },
    "python-c1-l46": {
        "data_table": table(["Statement", "Purpose"], [
            ["with open(...) as f:", "Automatically closes a file when done"],
        ]),
        "formulae": ["with open(\"data.txt\") as f:", "    content = f.read()"],
    },
    "python-c1-l47": {
        "data_table": table(["Class", "Purpose"], [
            ["Counter", "Counts occurrences of items"], ["defaultdict", "Dictionary with a default value type"],
        ]),
        "formulae": ["from collections import Counter", "Counter([\"a\", \"b\", \"a\"])"],
    },
    "python-c1-l48": {
        "data_table": table(["Class", "Behavior"], [
            ["defaultdict(int)", "Missing keys default to 0"],
        ]),
        "formulae": ["from collections import defaultdict", "counts = defaultdict(int)"],
    },
    "python-c1-l49": {
        "data_table": table(["Syntax", "Example"], [
            ["Multiple returns", "return a, b"],
        ]),
        "formulae": ["def minmax(nums):", "    return min(nums), max(nums)"],
    },
    "python-c1-l50": {
        "data_table": table(["Type", "Mutable?"], [
            ["list", "Yes"], ["tuple", "No"], ["dict", "Yes"], ["str", "No"],
        ]),
    },
    "python-c1-l51": {
        "data_table": table(["Copy Type", "Behavior"], [
            ["Shallow copy", "Copies outer structure, nested objects still shared"], ["Deep copy", "Fully independent copy of everything"],
        ]),
        "formulae": ["import copy", "deep = copy.deepcopy(original)"],
    },
    "python-c1-l52": {
        "data_table": table(["Format Spec", "Result"], [
            ["f\"{3.14159:.2f}\"", "'3.14'"],
        ]),
        "formulae": ["f\"{3.14159:.2f}\"  # '3.14'"],
    },
    "python-c1-l53": {
        "data_table": table(["Syntax", "Purpose"], [
            ["'''text'''", "Multi-line string"], ["r\"path\\n\"", "Raw string, ignores escape sequences"],
        ]),
    },
    "python-c1-l54": {
        "data_table": table(["Expression", "Meaning"], [
            ["0 < x < 10", "Chained comparison, equivalent to 0<x and x<10"],
        ]),
        "formulae": ["0 < x < 10"],
    },
    "python-c1-l55": {
        "data_table": table(["Syntax", "Example"], [
            ["Ternary expression", "'even' if x % 2 == 0 else 'odd'"],
        ]),
        "formulae": ["result = \"even\" if x % 2 == 0 else \"odd\""],
    },
    "python-c1-l56": {
        "data_table": table(["Module", "Provides"], [
            ["math", "Mathematical functions"], ["random", "Random number generation"],
        ]),
    },
    "python-c1-l57": {
        "data_table": table(["Format", "Use"], [
            ["JSON", "Common config format, readable with json.load()"],
        ]),
        "formulae": ["import json", "config = json.load(open(\"config.json\"))"],
    },
    "python-c1-l58": {
        "data_table": table(["Line", "Purpose"], [
            ["#!/usr/bin/env python3", "Tells the shell how to run the script"],
        ]),
    },
    "python-c1-l59": {
        "data_table": table(["Notation", "Meaning"], [
            ["O(n)", "Time grows linearly with input size"], ["O(1)", "Constant time, doesn't depend on input size"],
        ]),
    },
    "python-c1-l60": {
        "data_table": table(["Rule", "Example"], [
            ["4-space indentation", "PEP 8's standard for indenting code blocks"],
        ]),
    },
    "python-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Writing a first script", "A program that prints a greeting and today's date"],
        ]),
    },
    "python-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Combining control flow", "A function that classifies a number as positive, negative, or zero"],
        ]),
    },
    "python-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Debugging a type error", "Fixing code that mixes an int and a str incorrectly"],
        ]),
    },
    "python-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Calculating a tip", "Using arithmetic operators to compute a restaurant bill total"],
        ]),
    },
    "python-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Cleaning user input", "Using string methods to normalize capitalization and whitespace"],
        ]),
    },
    "python-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Building a report string", "Formatting a summary line with f-strings"],
        ]),
    },
    "python-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Validating input", "Using comparison operators to check a value is within range"],
        ]),
    },
    "python-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Grading logic", "Using if/elif/else to assign a letter grade from a score"],
        ]),
    },
    "python-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Summing a range", "Using a for loop with range() to total numbers 1 to 100"],
        ]),
    },
    "python-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Building a countdown", "Using a while loop with break to count down from 10"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Python"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Python: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Python lessons (completing 70/70).")


if __name__ == "__main__":
    main()
