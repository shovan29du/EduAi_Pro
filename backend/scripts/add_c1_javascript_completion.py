#!/usr/bin/env python3
"""Depth pass, C1 JavaScript: fill in real, hand-checked data_table
content for the 69 C1 JavaScript lessons not covered by the earlier
breadth-first batch. Brings C1 JavaScript to full 70/70 coverage.

Examples use real, runnable JavaScript syntax.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_javascript_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "javascript-c1-l1": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "let x = 5;"], ["Function", "function greet() {}"],
        ]),
        "formulae": ["let x = 5;", "console.log(x);"],
    },
    "javascript-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Scope", "Where a variable can be accessed in code"],
        ]),
        "formulae": ["function add(a, b) {", "  return a + b;", "}"],
    },
    "javascript-c1-l4": {
        "data_table": table(["Operator", "Meaning"], [
            ["+", "Addition or string concatenation"], ["===", "Strict equality"],
        ]),
        "formulae": ["let sum = 3 + 4;"],
    },
    "javascript-c1-l5": {
        "data_table": table(["Keyword", "Purpose"], [
            ["if", "Runs code when a condition is true"], ["else", "Runs when the condition is false"],
        ]),
        "formulae": ["if (age >= 18) {", "  console.log(\"Adult\");", "} else {", "  console.log(\"Minor\");", "}"],
    },
    "javascript-c1-l6": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for (let i=0; i<5; i++) {}"], ["while", "while (x < 10) {}"],
        ]),
        "formulae": ["for (let i = 0; i < 5; i++) {", "  console.log(i);", "}"],
    },
    "javascript-c1-l7": {
        "data_table": table(["Context", "Value of `this`"], [
            ["Global scope", "The global object (or undefined in strict mode)"], ["Object method", "The object the method was called on"],
        ]),
    },
    "javascript-c1-l8": {
        "data_table": table(["Syntax", "Result"], [
            ["`${name} is ${age}`", "Embeds variables directly in a string"],
        ]),
        "formulae": ["let name = \"Ana\";", "console.log(`Hello, ${name}!`);"],
    },
    "javascript-c1-l9": {
        "data_table": table(["Method", "Effect"], [
            [".push()", "Adds an item to the end"], [".pop()", "Removes the last item"],
        ]),
        "formulae": ["let fruits = [\"apple\", \"banana\"];", "fruits.push(\"cherry\");"],
    },
    "javascript-c1-l10": {
        "data_table": table(["Syntax", "Example"], [
            ["Object literal", "{ name: 'Sam', age: 20 }"],
        ]),
        "formulae": ["const student = { name: \"Sam\", age: 20 };", "console.log(student.name);"],
    },
    "javascript-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Hoisting", "Variable and function declarations are moved to the top of their scope"],
        ]),
    },
    "javascript-c1-l12": {
        "data_table": table(["Keyword", "Reassignable?", "Scope"], [
            ["var", "Yes", "Function-scoped"], ["let", "Yes", "Block-scoped"], ["const", "No", "Block-scoped"],
        ]),
    },
    "javascript-c1-l13": {
        "data_table": table(["Syntax", "Example"], [
            ["Function declaration", "function greet() { return 'Hi'; }"],
        ]),
        "formulae": ["function greet() {", "  return \"Hi\";", "}"],
    },
    "javascript-c1-l14": {
        "data_table": table(["Type", "Example"], [
            ["Function declaration", "function add(a,b) { return a+b; }"], ["Arrow function", "const add = (a,b) => a+b;"],
        ]),
        "formulae": ["const add = (a, b) => a + b;"],
    },
    "javascript-c1-l15": {
        "data_table": table(["Method", "Purpose"], [
            ["console.log()", "Prints output to the browser console"],
        ]),
        "formulae": ["console.log(\"Hello, console!\");"],
    },
    "javascript-c1-l16": {
        "data_table": table(["Method", "Purpose"], [
            ["console.error()", "Logs an error message"], ["console.table()", "Displays data as a table"],
        ]),
    },
    "javascript-c1-l17": {
        "data_table": table(["Falsy Value", "Example"], [
            ["0, '', null, undefined, NaN, false", "All evaluate as false in a boolean context"],
        ]),
    },
    "javascript-c1-l18": {
        "data_table": table(["Syntax", "Purpose"], [
            ["// comment", "Single-line comment"], ["/* comment */", "Multi-line comment"],
        ]),
    },
    "javascript-c1-l19": {
        "data_table": table(["Method", "Purpose"], [
            ["Math.round()", "Rounds to the nearest integer"], ["toFixed(2)", "Formats to 2 decimal places"],
        ]),
        "formulae": ["(3.14159).toFixed(2)  // '3.14'"],
    },
    "javascript-c1-l20": {
        "data_table": table(["Method", "Purpose"], [
            ["new Date()", "Creates a date object for the current time"],
        ]),
        "formulae": ["const now = new Date();"],
    },
    "javascript-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Runtime environment", "Where JavaScript code executes, e.g. a browser or Node.js"],
        ]),
    },
    "javascript-c1-l22": {
        "data_table": table(["Tool", "Purpose"], [
            ["Node.js", "Runs JavaScript outside the browser"], ["Code editor", "Writes and edits source files"],
        ]),
    },
    "javascript-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Call stack", "Tracks function calls in the order they need to execute"],
        ]),
    },
    "javascript-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Event loop", "Manages execution of code, handling asynchronous callbacks"],
        ]),
    },
    "javascript-c1-l25": {
        "data_table": table(["Method", "Effect"], [
            [".toUpperCase()", "Converts to uppercase"], [".slice()", "Extracts part of a string"],
        ]),
    },
    "javascript-c1-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Floating point precision", "0.1 + 0.2 does not exactly equal 0.3 in JavaScript"],
        ]),
    },
    "javascript-c1-l27": {
        "data_table": table(["Operator", "Meaning"], [
            ["&&", "Logical AND"], ["||", "Logical OR"],
        ]),
    },
    "javascript-c1-l28": {
        "data_table": table(["Method", "Effect"], [
            ["Array.isArray()", "Checks if a value is an array"],
        ]),
        "formulae": ["let nums = [1, 2, 3];"],
    },
    "javascript-c1-l29": {
        "data_table": table(["Access Method", "Example"], [
            ["Dot notation", "obj.property"], ["Bracket notation", "obj['property']"],
        ]),
    },
    "javascript-c1-l30": {
        "data_table": table(["Concept", "Example"], [
            ["Calling a function", "greet(\"Sam\")"],
        ]),
    },
    "javascript-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Parameter", "A variable listed in a function's definition"], ["Return value", "What the function sends back"],
        ]),
    },
    "javascript-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Callback function", "A function passed as an argument to another function"],
        ]),
        "formulae": ["setTimeout(() => console.log(\"done\"), 1000);"],
    },
    "javascript-c1-l33": {
        "data_table": table(["Term", "Example"], [
            ["IIFE", "(function() { console.log('run immediately'); })();"],
        ]),
    },
    "javascript-c1-l34": {
        "data_table": table(["Keyword", "Purpose"], [
            ["try", "Code that might throw an error"], ["catch", "Handles the error"],
        ]),
        "formulae": ["try {", "  JSON.parse(\"invalid\");", "} catch (e) {", "  console.log(\"Error caught\");", "}"],
    },
    "javascript-c1-l35": {
        "data_table": table(["Property/Method", "Purpose"], [
            ["Math.PI", "The value of pi"], ["Math.max()", "Largest of given numbers"],
        ]),
    },
    "javascript-c1-l36": {
        "data_table": table(["Method", "Purpose"], [
            ["JSON.stringify()", "Converts an object to a JSON string"], ["JSON.parse()", "Converts a JSON string to an object"],
        ]),
        "formulae": ["JSON.stringify({a: 1})  // '{\"a\":1}'"],
    },
    "javascript-c1-l37": {
        "data_table": table(["Object", "Purpose"], [
            ["window", "Represents the browser window"], ["navigator", "Provides browser information"],
        ]),
    },
    "javascript-c1-l38": {
        "data_table": table(["Attribute", "Purpose"], [
            ["required", "Marks a form field as mandatory"], ["pattern", "Validates input against a regex"],
        ]),
    },
    "javascript-c1-l39": {
        "data_table": table(["Function", "Purpose"], [
            ["setTimeout()", "Runs code once after a delay"], ["setInterval()", "Runs code repeatedly at an interval"],
        ]),
        "formulae": ["setTimeout(() => console.log(\"Hi\"), 1000);"],
    },
    "javascript-c1-l40": {
        "data_table": table(["Conversion", "Example"], [
            ["String to number", "Number(\"5\") // 5"],
        ]),
    },
    "javascript-c1-l41": {
        "data_table": table(["Directive", "Effect"], [
            ["'use strict';", "Enables stricter parsing and error handling"],
        ]),
    },
    "javascript-c1-l42": {
        "data_table": table(["Structure", "Example"], [
            ["2D array", "[[1,2],[3,4]]"],
        ]),
    },
    "javascript-c1-l43": {
        "data_table": table(["Method", "Returns"], [
            ["Object.keys()", "An array of property names"], ["Object.values()", "An array of property values"],
        ]),
    },
    "javascript-c1-l44": {
        "data_table": table(["Operator", "Behavior"], [
            ["==", "Compares with type coercion"], ["===", "Compares value and type strictly"],
        ]),
    },
    "javascript-c1-l45": {
        "data_table": table(["Syntax", "Example"], [
            ["Ternary operator", "age >= 18 ? 'adult' : 'minor'"],
        ]),
        "formulae": ["let status = age >= 18 ? \"adult\" : \"minor\";"],
    },
    "javascript-c1-l46": {
        "data_table": table(["Practice", "Benefit"], [
            ["Meaningful variable names", "Makes code easier to understand"],
        ]),
    },
    "javascript-c1-l47": {
        "data_table": table(["Concept", "Example"], [
            ["Base case", "Stops the recursion"],
        ]),
        "formulae": ["function factorial(n) {", "  if (n <= 1) return 1;", "  return n * factorial(n - 1);", "}"],
    },
    "javascript-c1-l48": {
        "data_table": table(["Structure", "Feature"], [
            ["Set", "Stores unique values"], ["Map", "Stores key-value pairs, any type as key"],
        ]),
    },
    "javascript-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Template engine", "Generates HTML dynamically from data and templates"],
        ]),
    },
    "javascript-c1-l50": {
        "data_table": table(["Tool", "Purpose"], [
            ["Browser DevTools", "Inspects, debugs, and profiles web pages"],
        ]),
    },
    "javascript-c1-l51": {
        "data_table": table(["Command", "Purpose"], [
            ["npm install", "Installs packages listed in package.json"],
        ]),
        "formulae": ["npm install lodash"],
    },
    "javascript-c1-l52": {
        "data_table": table(["Command", "Purpose"], [
            ["node script.js", "Runs a JavaScript file with Node.js"],
        ]),
        "formulae": ["console.log(\"Hello from Node!\");"],
    },
    "javascript-c1-l53": {
        "data_table": table(["Keyword", "Purpose"], [
            ["export", "Makes code available to other files"], ["import", "Brings in code from another file"],
        ]),
        "formulae": ["export function add(a, b) { return a + b; }"],
    },
    "javascript-c1-l54": {
        "data_table": table(["API", "Persistence"], [
            ["localStorage", "Persists after the browser closes"], ["sessionStorage", "Cleared when the tab closes"],
        ]),
    },
    "javascript-c1-l55": {
        "data_table": table(["Method", "Example"], [
            ["Template literal", "`Total: ${price}`"],
        ]),
    },
    "javascript-c1-l56": {
        "data_table": table(["Method", "Returns"], [
            ["find()", "The first matching element"], ["includes()", "True/false if the value exists"],
        ]),
    },
    "javascript-c1-l57": {
        "data_table": table(["Scope Type", "Accessible From"], [
            ["Global scope", "Anywhere in the code"], ["Local scope", "Only within its function or block"],
        ]),
    },
    "javascript-c1-l58": {
        "data_table": table(["Practice", "Benefit"], [
            ["JSDoc comments", "Documents function parameters and return types"],
        ]),
    },
    "javascript-c1-l59": {
        "data_table": table(["Technique", "Purpose"], [
            ["requestAnimationFrame()", "Smoothly schedules animation frames"],
        ]),
    },
    "javascript-c1-l60": {
        "data_table": table(["Feature", "Implementation"], [
            ["Add a task", "Push a new item to an array and re-render the list"],
        ]),
    },
    "javascript-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Writing a first script", "A program that logs a greeting to the console"],
        ]),
    },
    "javascript-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Debugging scope errors", "Fixing a variable accessed outside its block"],
        ]),
    },
    "javascript-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Predicting coercion", "Determining the result of '5' + 3 vs '5' - 3"],
        ]),
    },
    "javascript-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building an expression", "Calculating a total price with tax using operators"],
        ]),
    },
    "javascript-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Grading logic", "Using if/else if/else to assign a letter grade"],
        ]),
    },
    "javascript-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Summing an array", "Using a for loop to total an array of numbers"],
        ]),
    },
    "javascript-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Tracing `this`", "Predicting the value of `this` inside a method versus a callback"],
        ]),
    },
    "javascript-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a message", "Using a template literal to format a receipt line"],
        ]),
    },
    "javascript-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Filtering an array", "Using array methods to remove items below a threshold"],
        ]),
    },
    "javascript-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Building an object", "Modeling a product with name, price, and quantity properties"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["JavaScript"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json JavaScript: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 JavaScript lessons (completing 70/70).")


if __name__ == "__main__":
    main()
