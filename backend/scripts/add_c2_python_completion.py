#!/usr/bin/env python3
"""Depth pass, C2 Python: fill in real, hand-checked data_table/formulae
(real runnable code) content for the 69 C2 Python lessons not covered
by the earlier breadth-first batch. Brings C2 Python to full 70/70
coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_python_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "python-c2-l1": {
        "data_table": table(["Structure", "Feature"], [
            ["list", "Ordered, mutable collection"], ["tuple", "Ordered, immutable collection"], ["dict", "Key-value mapping"],
        ]),
        "formulae": ["nums = [1, 2, 3]\npoint = (1, 2)\nd = {\"a\": 1}"],
    },
    "python-c2-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Class", "A blueprint for creating objects"], ["Instance", "A specific object created from a class"],
        ]),
        "formulae": ["class Dog:\n    def __init__(self, name):\n        self.name = name"],
    },
    "python-c2-l4": {
        "data_table": table(["Type", "Example"], [
            ["Dict comprehension", "{k: v*2 for k, v in d.items()}"], ["Set comprehension", "{x*x for x in range(5)}"],
        ]),
        "formulae": ["squares = {x: x * x for x in range(5)}"],
    },
    "python-c2-l5": {
        "data_table": table(["Protocol", "Requirement"], [
            ["Iterable", "Implements __iter__"], ["Iterator", "Implements __next__"],
        ]),
        "formulae": ["it = iter([1, 2, 3])\nnext(it)"],
    },
    "python-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Generator", "A function that yields values lazily, one at a time"],
        ]),
        "formulae": ["def counter():\n    n = 0\n    while True:\n        yield n\n        n += 1"],
    },
    "python-c2-l7": {
        "data_table": table(["Method", "Purpose"], [
            ["__init__", "Initializes a new instance's attributes"],
        ]),
        "formulae": ["class Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y"],
    },
    "python-c2-l8": {
        "data_table": table(["Type", "Scope"], [
            ["Instance attribute", "Unique to each object"], ["Class attribute", "Shared across all instances"],
        ]),
        "formulae": ["class Dog:\n    species = \"Canis familiaris\"\n    def __init__(self, name):\n        self.name = name"],
    },
    "python-c2-l9": {
        "data_table": table(["Concept", "Meaning"], [
            ["Inheritance", "A class acquiring attributes and methods from a parent class"],
        ]),
        "formulae": ["class Animal:\n    def speak(self):\n        return \"...\"\n\nclass Dog(Animal):\n    def speak(self):\n        return \"Woof\""],
    },
    "python-c2-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Polymorphism", "Different classes responding to the same method call in their own way"],
        ]),
        "formulae": ["for animal in [Dog(), Cat()]:\n    print(animal.speak())"],
    },
    "python-c2-l11": {
        "data_table": table(["Concept", "Purpose"], [
            ["Property decorator", "Exposes a method as a read-only attribute"],
        ]),
        "formulae": ["class Circle:\n    def __init__(self, r):\n        self._r = r\n    @property\n    def area(self):\n        return 3.14159 * self._r ** 2"],
    },
    "python-c2-l12": {
        "data_table": table(["Magic Method", "Purpose"], [
            ["__add__", "Defines behavior for the + operator"], ["__str__", "Defines the string representation of an object"],
        ]),
        "formulae": ["class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)"],
    },
    "python-c2-l13": {
        "data_table": table(["Approach", "Principle"], [
            ["Composition", "'Has-a' relationship, building objects from other objects"], ["Inheritance", "'Is-a' relationship, extending a base class"],
        ]),
    },
    "python-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Abstract base class", "Defines a required interface that subclasses must implement"],
        ]),
        "formulae": ["from abc import ABC, abstractmethod\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): ..."],
    },
    "python-c2-l15": {
        "data_table": table(["Statement", "Purpose"], [
            ["import module", "Loads an entire module"], ["from module import name", "Loads a specific name from a module"],
        ]),
        "formulae": ["import math\nfrom math import sqrt"],
    },
    "python-c2-l16": {
        "data_table": table(["File", "Purpose"], [
            ["__init__.py", "Marks a directory as a Python package"],
        ]),
    },
    "python-c2-l17": {
        "data_table": table(["Mode", "Purpose"], [
            ["'r'", "Read a text file"], ["'w'", "Write, overwriting existing content"],
        ]),
        "formulae": ["with open(\"file.txt\", \"r\") as f:\n    content = f.read()"],
    },
    "python-c2-l18": {
        "data_table": table(["Module", "Purpose"], [
            ["csv", "Reads and writes comma-separated value files"],
        ]),
        "formulae": ["import csv\nwith open(\"data.csv\") as f:\n    reader = csv.reader(f)\n    for row in reader:\n        print(row)"],
    },
    "python-c2-l19": {
        "data_table": table(["Function", "Purpose"], [
            ["json.dumps", "Converts a Python object to a JSON string"], ["json.loads", "Parses a JSON string into a Python object"],
        ]),
        "formulae": ["import json\ndata = json.loads('{\"a\": 1}')"],
    },
    "python-c2-l20": {
        "data_table": table(["Exception", "Trigger"], [
            ["ValueError", "An operation receives an argument of the right type but wrong value"], ["KeyError", "A dictionary key isn't found"],
        ]),
        "formulae": ["try:\n    int(\"abc\")\nexcept ValueError as e:\n    print(e)"],
    },
    "python-c2-l21": {
        "data_table": table(["Example", "Result"], [
            ["[x for x in range(10) if x % 2 == 0]", "Even numbers from 0 to 9"],
        ]),
        "formulae": ["evens = [x for x in range(10) if x % 2 == 0]"],
    },
    "python-c2-l22": {
        "data_table": table(["Example", "Result"], [
            ["[[y for y in range(3)] for x in range(2)]", "A 2x3 nested list"],
        ]),
        "formulae": ["matrix = [[y for y in range(3)] for x in range(2)]"],
    },
    "python-c2-l23": {
        "data_table": table(["Syntax", "Feature"], [
            ["(x*x for x in range(5))", "Lazily evaluates values one at a time, saving memory"],
        ]),
        "formulae": ["gen = (x * x for x in range(5))"],
    },
    "python-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Decorator", "A function that wraps another function to extend its behavior"],
        ]),
        "formulae": ["def my_decorator(func):\n    def wrapper():\n        print(\"before\")\n        func()\n    return wrapper"],
    },
    "python-c2-l25": {
        "data_table": table(["Feature", "Purpose"], [
            ["Decorator with arguments", "A decorator factory that returns a configured decorator"],
        ]),
        "formulae": ["def repeat(n):\n    def decorator(func):\n        def wrapper(*args):\n            for _ in range(n):\n                func(*args)\n        return wrapper\n    return decorator"],
    },
    "python-c2-l26": {
        "data_table": table(["Function", "Purpose"], [
            ["functools.reduce", "Cumulatively applies a function to a sequence"], ["functools.lru_cache", "Caches function results to speed up repeated calls"],
        ]),
        "formulae": ["from functools import reduce\ntotal = reduce(lambda a, b: a + b, [1, 2, 3])"],
    },
    "python-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Closure", "A function that remembers variables from its enclosing scope"],
        ]),
        "formulae": ["def make_adder(n):\n    def adder(x):\n        return x + n\n    return adder"],
    },
    "python-c2-l28": {
        "data_table": table(["Function", "Purpose"], [
            ["itertools.chain", "Combines multiple iterables into one"], ["itertools.combinations", "Generates all combinations of a given length"],
        ]),
        "formulae": ["from itertools import chain\nlist(chain([1, 2], [3, 4]))"],
    },
    "python-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Method Resolution Order", "The order Python searches parent classes when resolving multiple inheritance"],
        ]),
        "formulae": ["class C(A, B):\n    pass\nprint(C.__mro__)"],
    },
    "python-c2-l30": {
        "data_table": table(["Decorator", "Purpose"], [
            ["@classmethod", "Receives the class as the first argument"], ["@staticmethod", "Receives no implicit first argument"],
        ]),
        "formulae": ["class Circle:\n    @staticmethod\n    def is_valid_radius(r):\n        return r > 0"],
    },
    "python-c2-l31": {
        "data_table": table(["Feature", "Benefit"], [
            ["@dataclass", "Auto-generates __init__, __repr__, and __eq__ for simple classes"],
        ]),
        "formulae": ["from dataclasses import dataclass\n@dataclass\nclass Point:\n    x: int\n    y: int"],
    },
    "python-c2-l32": {
        "data_table": table(["Tool", "Purpose"], [
            ["mypy", "Statically checks Python type hints for errors before runtime"],
        ]),
        "formulae": ["def add(a: int, b: int) -> int:\n    return a + b"],
    },
    "python-c2-l33": {
        "data_table": table(["Practice", "Benefit"], [
            ["Custom exception classes", "Lets code catch and handle specific error types precisely"],
        ]),
        "formulae": ["class InsufficientFundsError(Exception):\n    pass"],
    },
    "python-c2-l34": {
        "data_table": table(["Tool", "Purpose"], [
            ["contextlib.contextmanager", "Turns a generator function into a context manager"],
        ]),
        "formulae": ["from contextlib import contextmanager\n@contextmanager\ndef managed_resource():\n    print(\"open\")\n    yield\n    print(\"close\")"],
    },
    "python-c2-l35": {
        "data_table": table(["Module", "Purpose"], [
            ["threading", "Runs code concurrently using multiple threads within one process"],
        ]),
        "formulae": ["import threading\nt = threading.Thread(target=my_func)\nt.start()"],
    },
    "python-c2-l36": {
        "data_table": table(["Module", "Purpose"], [
            ["multiprocessing", "Runs code in parallel across multiple processes, bypassing the GIL"],
        ]),
        "formulae": ["from multiprocessing import Process\np = Process(target=my_func)\np.start()"],
    },
    "python-c2-l37": {
        "data_table": table(["Keyword", "Purpose"], [
            ["async def", "Defines a coroutine function"], ["await", "Pauses execution until an awaitable completes"],
        ]),
        "formulae": ["import asyncio\nasync def main():\n    await asyncio.sleep(1)"],
    },
    "python-c2-l38": {
        "data_table": table(["Function", "Purpose"], [
            ["asyncio.gather", "Runs multiple coroutines concurrently"],
        ]),
        "formulae": ["results = await asyncio.gather(task1(), task2())"],
    },
    "python-c2-l39": {
        "data_table": table(["Pattern", "Meaning"], [
            ["(?=...)", "Positive lookahead"], ["(\\w+)", "A capturing group of word characters"],
        ]),
        "formulae": ["import re\nre.search(r\"(\\d+)(?=px)\", \"10px\")"],
    },
    "python-c2-l40": {
        "data_table": table(["Type", "Meaning"], [
            ["bytes", "An immutable sequence of raw byte values"],
        ]),
        "formulae": ["b = b\"hello\"\nb.decode(\"utf-8\")"],
    },
    "python-c2-l41": {
        "data_table": table(["Function", "Purpose"], [
            ["pickle.dump", "Serializes a Python object to a file"], ["pickle.load", "Deserializes an object from a file"],
        ]),
        "formulae": ["import pickle\nwith open(\"data.pkl\", \"wb\") as f:\n    pickle.dump(obj, f)"],
    },
    "python-c2-l42": {
        "data_table": table(["Function", "Purpose"], [
            ["sqlite3.connect", "Opens a connection to a SQLite database file"],
        ]),
        "formulae": ["import sqlite3\nconn = sqlite3.connect(\"app.db\")\ncur = conn.cursor()\ncur.execute(\"SELECT * FROM users\")"],
    },
    "python-c2-l43": {
        "data_table": table(["File", "Purpose"], [
            ["pyproject.toml", "Declares a project's dependencies and metadata for Poetry"],
        ]),
        "formulae": ["poetry add requests\npoetry install"],
    },
    "python-c2-l44": {
        "data_table": table(["File", "Purpose"], [
            ["setup.py or pyproject.toml", "Defines how a package is built and distributed"],
        ]),
    },
    "python-c2-l45": {
        "data_table": table(["Function", "Purpose"], [
            ["assert", "Checks that a condition holds true in a test"],
        ]),
        "formulae": ["def test_add():\n    assert add(2, 3) == 5"],
    },
    "python-c2-l46": {
        "data_table": table(["Tool", "Purpose"], [
            ["@pytest.fixture", "Provides reusable setup code for tests"], ["unittest.mock", "Replaces real objects with fake ones during testing"],
        ]),
        "formulae": ["import pytest\n@pytest.fixture\ndef sample_data():\n    return [1, 2, 3]"],
    },
    "python-c2-l47": {
        "data_table": table(["Level", "Use"], [
            ["INFO", "General operational messages"], ["ERROR", "A serious problem occurred"],
        ]),
        "formulae": ["import logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info(\"Started\")"],
    },
    "python-c2-l48": {
        "data_table": table(["Tool", "Purpose"], [
            ["cProfile", "Measures where a program spends its execution time"],
        ]),
        "formulae": ["import cProfile\ncProfile.run(\"my_function()\")"],
    },
    "python-c2-l49": {
        "data_table": table(["Concept", "Meaning"], [
            ["Reference counting", "Python's primary memory management mechanism, freeing objects with zero references"],
        ]),
    },
    "python-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Metaclass", "A class whose instances are themselves classes, controlling class creation"],
        ]),
    },
    "python-c2-l51": {
        "data_table": table(["Method", "Purpose"], [
            ["__get__ / __set__", "Customize attribute access via the descriptor protocol"],
        ]),
    },
    "python-c2-l52": {
        "data_table": table(["Function", "Purpose"], [
            ["argparse.ArgumentParser", "Builds a command-line argument interface"],
        ]),
        "formulae": ["import argparse\nparser = argparse.ArgumentParser()\nparser.add_argument(\"--name\")"],
    },
    "python-c2-l53": {
        "data_table": table(["Function", "Purpose"], [
            ["requests.get", "Sends an HTTP GET request and returns the response"],
        ]),
        "formulae": ["import requests\nresponse = requests.get(\"https://api.example.com/data\")"],
    },
    "python-c2-l54": {
        "data_table": table(["Library", "Purpose"], [
            ["BeautifulSoup", "Parses HTML to extract data from web pages"],
        ]),
        "formulae": ["from bs4 import BeautifulSoup\nsoup = BeautifulSoup(html, \"html.parser\")"],
    },
    "python-c2-l55": {
        "data_table": table(["Feature", "Benefit"], [
            ["NumPy array", "Enables fast, vectorized numerical operations"],
        ]),
        "formulae": ["import numpy as np\narr = np.array([1, 2, 3])\narr * 2"],
    },
    "python-c2-l56": {
        "data_table": table(["Structure", "Purpose"], [
            ["pandas.DataFrame", "A labeled, 2D tabular data structure for analysis"],
        ]),
        "formulae": ["import pandas as pd\ndf = pd.DataFrame({\"a\": [1, 2], \"b\": [3, 4]})"],
    },
    "python-c2-l57": {
        "data_table": table(["Format", "Use Case"], [
            ["JSON", "Lightweight, common for web APIs"], ["YAML", "Human-readable, common for configuration files"],
        ]),
    },
    "python-c2-l58": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Singleton", "Ensures only one instance of a class exists"], ["Factory", "Creates objects without specifying the exact class"],
        ]),
    },
    "python-c2-l59": {
        "data_table": table(["Practice", "Reason"], [
            ["Following PEP 8", "Keeps code style consistent and readable across the community"],
        ]),
    },
    "python-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Uploading with twine", "Publishes a built package distribution to PyPI"],
        ]),
        "formulae": ["python -m build\ntwine upload dist/*"],
    },
    "python-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Building a counter with closures", "Maintaining private state without a class"],
        ]),
    },
    "python-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Choosing classmethod vs staticmethod", "Deciding whether a method needs access to the class"],
        ]),
    },
    "python-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Building an infinite generator", "Creating a lazy sequence that yields values on demand"],
        ]),
    },
    "python-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Overloading an operator", "Implementing __eq__ to compare custom objects"],
        ]),
    },
    "python-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a data structure", "Picking a set over a list for fast membership testing"],
        ]),
    },
    "python-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Designing a class hierarchy", "Modeling shapes with a shared base class"],
        ]),
    },
    "python-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Filtering with a comprehension", "Extracting values meeting a condition from a list"],
        ]),
    },
    "python-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Transforming a dict", "Building a new dictionary with modified values"],
        ]),
    },
    "python-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Implementing a custom iterator", "Writing __iter__ and __next__ for a class"],
        ]),
    },
    "python-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Comparing generators to lists", "Measuring memory use for a large sequence"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Python"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Python: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Python lessons (completing 70/70).")


if __name__ == "__main__":
    main()
