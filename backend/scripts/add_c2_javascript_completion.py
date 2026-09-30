#!/usr/bin/env python3
"""Depth pass, C2 JavaScript: fill in real, hand-checked
data_table/formulae (real runnable JS code) content for the 69 C2
JavaScript lessons not covered by the earlier breadth-first batch.
Brings C2 JavaScript to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_javascript_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "javascript-c2-l1": {
        "data_table": table(["Structure", "Example"], [
            ["Array", "[1, 2, 3]"], ["Object", "{ name: 'Sam', age: 20 }"],
        ]),
        "formulae": ["const arr = [1, 2, 3];\nconst obj = { name: \"Sam\", age: 20 };"],
    },
    "javascript-c2-l2": {
        "data_table": table(["Method", "Purpose"], [
            ["document.querySelector", "Selects the first matching element"], ["element.textContent", "Gets or sets an element's text content"],
        ]),
        "formulae": ["document.querySelector(\"#title\").textContent = \"Hello\";"],
    },
    "javascript-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Scope chain", "The nested chain of scopes JavaScript searches when resolving a variable"],
        ]),
        "formulae": ["function outer() {\n  let x = 1;\n  function inner() {\n    console.log(x);\n  }\n  inner();\n}"],
    },
    "javascript-c2-l5": {
        "data_table": table(["Method", "Purpose"], [
            ["map", "Transforms each element, returning a new array"], ["filter", "Keeps elements matching a condition"], ["reduce", "Accumulates values into a single result"],
        ]),
        "formulae": ["const doubled = [1, 2, 3].map(x => x * 2);"],
    },
    "javascript-c2-l6": {
        "data_table": table(["Descriptor", "Meaning"], [
            ["writable", "Whether a property's value can be changed"], ["enumerable", "Whether a property shows up in for...in loops"],
        ]),
        "formulae": ["Object.defineProperty(obj, \"x\", { value: 1, writable: false });"],
    },
    "javascript-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Prototype chain", "The lookup path JavaScript follows to find inherited properties"],
        ]),
        "formulae": ["console.log(Object.getPrototypeOf([]));"],
    },
    "javascript-c2-l8": {
        "data_table": table(["Keyword", "Purpose"], [
            ["new", "Creates a new object and binds it to the constructor's this"],
        ]),
        "formulae": ["function Dog(name) {\n  this.name = name;\n}\nconst d = new Dog(\"Rex\");"],
    },
    "javascript-c2-l9": {
        "data_table": table(["Function", "Purpose"], [
            ["JSON.stringify", "Converts a JS object to a JSON string"], ["JSON.parse", "Converts a JSON string to a JS object"],
        ]),
        "formulae": ["const str = JSON.stringify({ a: 1 });\nconst obj = JSON.parse(str);"],
    },
    "javascript-c2-l10": {
        "data_table": table(["Method", "Purpose"], [
            ["addEventListener", "Registers a function to run when an event occurs"],
        ]),
        "formulae": ["button.addEventListener(\"click\", (event) => console.log(event.target));"],
    },
    "javascript-c2-l11": {
        "data_table": table(["Phase", "Direction"], [
            ["Bubbling", "Event propagates from target up to ancestors"], ["Capturing", "Event propagates from ancestors down to target"],
        ]),
    },
    "javascript-c2-l12": {
        "data_table": table(["Method", "Purpose"], [
            ["checkValidity", "Checks whether a form field satisfies its validation constraints"],
        ]),
        "formulae": ["if (!input.checkValidity()) { input.reportValidity(); }"],
    },
    "javascript-c2-l13": {
        "data_table": table(["Property", "Purpose"], [
            ["window.location", "Provides information about and control over the current URL"],
        ]),
    },
    "javascript-c2-l14": {
        "data_table": table(["Pattern", "Matches"], [
            ["/\\d+/", "One or more digits"],
        ]),
        "formulae": ["const match = \"abc123\".match(/\\d+/);"],
    },
    "javascript-c2-l15": {
        "data_table": table(["Syntax", "Purpose"], [
            ["const { a, b } = obj", "Extracts object properties into variables"], ["const [x, y] = arr", "Extracts array elements into variables"],
        ]),
        "formulae": ["const { name, age } = { name: \"Sam\", age: 20 };"],
    },
    "javascript-c2-l16": {
        "data_table": table(["Operator", "Purpose"], [
            ["...spread", "Expands an iterable into individual elements"], ["...rest", "Collects remaining arguments into an array"],
        ]),
        "formulae": ["function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }"],
    },
    "javascript-c2-l17": {
        "data_table": table(["Feature", "Example"], [
            ["Default parameter", "function greet(name = \"World\") {}"],
        ]),
        "formulae": ["function greet(name = \"World\") { return `Hello, ${name}`; }"],
    },
    "javascript-c2-l18": {
        "data_table": table(["Method", "Purpose"], [
            ["template literal", "Embeds expressions directly in strings using backticks"],
        ]),
        "formulae": ["const msg = `Hello, ${name}!`;"],
    },
    "javascript-c2-l19": {
        "data_table": table(["Method", "Purpose"], [
            ["Array.sort", "Sorts array elements in place"], ["Array.includes", "Checks whether an array contains a value"],
        ]),
        "formulae": ["[3, 1, 2].sort((a, b) => a - b);"],
    },
    "javascript-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["DOM tree", "A hierarchical, tree-structured representation of an HTML document"],
        ]),
    },
    "javascript-c2-l21": {
        "data_table": table(["Pattern", "Feature"], [
            ["Callback", "A function passed to run after an async operation completes"], ["Promise", "An object representing an eventual async result"], ["Async/await", "Syntactic sugar for writing promise code sequentially"],
        ]),
        "formulae": ["async function load() {\n  const data = await fetch(url);\n}"],
    },
    "javascript-c2-l22": {
        "data_table": table(["Method", "Purpose"], [
            [".then()", "Handles a promise's resolved value"], [".catch()", "Handles a promise's rejection"],
        ]),
        "formulae": ["fetch(url).then(res => res.json()).catch(err => console.error(err));"],
    },
    "javascript-c2-l23": {
        "data_table": table(["Queue", "Runs"], [
            ["Microtask queue", "Promise callbacks, runs before the next macrotask"], ["Macrotask queue", "setTimeout callbacks, runs after all microtasks"],
        ]),
    },
    "javascript-c2-l24": {
        "data_table": table(["Function", "Purpose"], [
            ["fetch", "Sends an HTTP request and returns a promise resolving to the response"],
        ]),
        "formulae": ["const res = await fetch(\"https://api.example.com/data\");\nconst data = await res.json();"],
    },
    "javascript-c2-l25": {
        "data_table": table(["Approach", "Syntax"], [
            ["try/catch with async", "Wraps await calls to catch rejected promises"],
        ]),
        "formulae": ["try {\n  await riskyOperation();\n} catch (err) {\n  console.error(err);\n}"],
    },
    "javascript-c2-l26": {
        "data_table": table(["Method", "Purpose"], [
            ["flatMap", "Maps then flattens the result by one level"],
        ]),
        "formulae": ["[[1, 2], [3]].flatMap(x => x);"],
    },
    "javascript-c2-l27": {
        "data_table": table(["Function", "Purpose"], [
            ["Object.freeze", "Prevents an object's properties from being changed"],
        ]),
        "formulae": ["const frozen = Object.freeze({ a: 1 });"],
    },
    "javascript-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Currying", "Transforming a function of multiple arguments into a sequence of single-argument functions"],
        ]),
        "formulae": ["const add = a => b => a + b;\nadd(2)(3);"],
    },
    "javascript-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Higher-order function", "A function that takes or returns another function"],
        ]),
        "formulae": ["const withLogging = fn => (...args) => { console.log(args); return fn(...args); };"],
    },
    "javascript-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["IIFE", "An Immediately Invoked Function Expression that runs as soon as it's defined"],
        ]),
        "formulae": ["(function() {\n  console.log(\"runs immediately\");\n})();"],
    },
    "javascript-c2-l31": {
        "data_table": table(["Syntax", "Purpose"], [
            ["export", "Makes a value available to other modules"], ["import", "Brings a value from another module into scope"],
        ]),
        "formulae": ["export function add(a, b) { return a + b; }\nimport { add } from \"./math.js\";"],
    },
    "javascript-c2-l32": {
        "data_table": table(["Keyword", "Purpose"], [
            ["class", "Defines a blueprint for creating objects"], ["extends", "Establishes inheritance between classes"],
        ]),
        "formulae": ["class Animal {\n  speak() { return \"...\"; }\n}\nclass Dog extends Animal {\n  speak() { return \"Woof\"; }\n}"],
    },
    "javascript-c2-l33": {
        "data_table": table(["Keyword", "Purpose"], [
            ["get", "Defines a computed property accessed like a field"], ["set", "Defines logic to run when a property is assigned"],
        ]),
        "formulae": ["class Circle {\n  get area() { return Math.PI * this.r ** 2; }\n}"],
    },
    "javascript-c2-l34": {
        "data_table": table(["Symbol", "Purpose"], [
            ["Symbol.iterator", "Defines how an object is iterated with for...of"],
        ]),
    },
    "javascript-c2-l35": {
        "data_table": table(["Protocol", "Requirement"], [
            ["Iterable", "Implements Symbol.iterator"],
        ]),
        "formulae": ["const it = [1, 2, 3][Symbol.iterator]();\nit.next();"],
    },
    "javascript-c2-l36": {
        "data_table": table(["Keyword", "Purpose"], [
            ["function*", "Defines a generator function"], ["yield", "Pauses execution and returns a value"],
        ]),
        "formulae": ["function* counter() {\n  let n = 0;\n  while (true) yield n++;\n}"],
    },
    "javascript-c2-l37": {
        "data_table": table(["Structure", "Feature"], [
            ["WeakMap", "Keys are weakly held, allowing garbage collection"],
        ]),
        "formulae": ["const wm = new WeakMap();\nwm.set(obj, \"data\");"],
    },
    "javascript-c2-l38": {
        "data_table": table(["Object", "Purpose"], [
            ["Proxy", "Intercepts and customizes operations on an object"], ["Reflect", "Provides methods mirroring default object operations"],
        ]),
        "formulae": ["const p = new Proxy(target, { get(obj, key) { return obj[key]; } });"],
    },
    "javascript-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Garbage collection", "Automatically frees memory no longer reachable by the program"],
        ]),
    },
    "javascript-c2-l40": {
        "data_table": table(["Technique", "Purpose"], [
            ["Debouncing", "Delays execution until input stops for a period"], ["Throttling", "Limits execution to once per fixed interval"],
        ]),
        "formulae": ["function debounce(fn, ms) {\n  let timer;\n  return (...args) => {\n    clearTimeout(timer);\n    timer = setTimeout(() => fn(...args), ms);\n  };\n}"],
    },
    "javascript-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Web Worker", "Runs JavaScript in a background thread separate from the main UI thread"],
        ]),
        "formulae": ["const worker = new Worker(\"worker.js\");"],
    },
    "javascript-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Service Worker", "A background script enabling offline caching and push notifications"],
        ]),
    },
    "javascript-c2-l43": {
        "data_table": table(["Feature", "Benefit"], [
            ["TypeScript", "Adds static typing to JavaScript, catching errors before runtime"],
        ]),
        "formulae": ["function add(a: number, b: number): number { return a + b; }"],
    },
    "javascript-c2-l44": {
        "data_table": table(["Framework", "Purpose"], [
            ["Jest", "A popular JavaScript testing framework"],
        ]),
        "formulae": ["test(\"adds numbers\", () => {\n  expect(add(2, 3)).toBe(5);\n});"],
    },
    "javascript-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Mock", "A fake implementation replacing a real dependency in a test"], ["Stub", "A simplified function that returns preset values"],
        ]),
        "formulae": ["const mockFn = jest.fn().mockReturnValue(42);"],
    },
    "javascript-c2-l46": {
        "data_table": table(["Tool", "Purpose"], [
            ["Webpack", "Bundles JavaScript modules and assets for production"], ["Vite", "A fast modern build tool with instant dev server startup"],
        ]),
    },
    "javascript-c2-l47": {
        "data_table": table(["Technique", "Benefit"], [
            ["Tree shaking", "Removes unused code from the final bundle"], ["Code splitting", "Breaks the bundle into smaller chunks loaded on demand"],
        ]),
    },
    "javascript-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Stream", "Processes data incrementally rather than loading it all into memory at once"],
        ]),
    },
    "javascript-c2-l49": {
        "data_table": table(["Method", "Purpose"], [
            ["app.get", "Defines a route handler for HTTP GET requests"],
        ]),
        "formulae": ["const express = require(\"express\");\nconst app = express();\napp.get(\"/users\", (req, res) => res.json([]));"],
    },
    "javascript-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Middleware", "A function that processes requests before they reach the final route handler"],
        ]),
        "formulae": ["app.use((req, res, next) => {\n  console.log(req.method);\n  next();\n});"],
    },
    "javascript-c2-l51": {
        "data_table": table(["Practice", "Reason"], [
            ["Using .env files", "Keeps sensitive configuration out of source code"],
        ]),
    },
    "javascript-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["WebSocket", "Enables persistent, two-way real-time communication between client and server"],
        ]),
        "formulae": ["const ws = new WebSocket(\"wss://example.com\");"],
    },
    "javascript-c2-l53": {
        "data_table": table(["Pattern", "Purpose"], [
            ["Centralized store", "Manages shared application state predictably across components"],
        ]),
    },
    "javascript-c2-l54": {
        "data_table": table(["Concept", "Meaning"], [
            ["Component", "A reusable, self-contained piece of UI with its own logic and markup"],
        ]),
    },
    "javascript-c2-l55": {
        "data_table": table(["Tool", "Purpose"], [
            ["Performance tab", "Browser dev tool for identifying rendering and script bottlenecks"],
        ]),
    },
    "javascript-c2-l56": {
        "data_table": table(["Attack", "Meaning"], [
            ["XSS", "Injecting malicious scripts into a trusted webpage"], ["CSRF", "Tricking a user's browser into making unwanted authenticated requests"],
        ]),
    },
    "javascript-c2-l57": {
        "data_table": table(["Concept", "Meaning"], [
            ["Pure function", "Given the same input, always returns the same output with no side effects"],
        ]),
        "formulae": ["const add = (a, b) => a + b;"],
    },
    "javascript-c2-l58": {
        "data_table": table(["Method", "Purpose"], [
            ["Object.create", "Creates a new object with a specified prototype"],
        ]),
        "formulae": ["const proto = { greet() { return \"hi\"; } };\nconst obj = Object.create(proto);"],
    },
    "javascript-c2-l59": {
        "data_table": table(["Feature", "Example"], [
            ["Named capture group", "/(?<year>\\d{4})/"],
        ]),
        "formulae": ["const m = \"2024\".match(/(?<year>\\d{4})/);"],
    },
    "javascript-c2-l60": {
        "data_table": table(["File", "Purpose"], [
            ["package.json", "Declares an npm package's metadata, dependencies, and entry point"],
        ]),
        "formulae": ["npm init -y\nnpm publish"],
    },
    "javascript-c2-l61": {
        "data_table": table(["Method", "Purpose"], [
            ["replaceAll", "Replaces every match of a pattern within a string"],
        ]),
        "formulae": ["\"a-b-c\".replaceAll(\"-\", \" \");"],
    },
    "javascript-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Nesting arrays and objects", "Modeling structured data like a list of user records"],
        ]),
    },
    "javascript-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Updating the page dynamically", "Changing element content in response to user input"],
        ]),
    },
    "javascript-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a private counter", "Using a closure to hide internal state from outside access"],
        ]),
    },
    "javascript-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Tracing variable lookup", "Following the scope chain to resolve a nested variable"],
        ]),
    },
    "javascript-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Chaining array methods", "Filtering then transforming a list in one expression"],
        ]),
    },
    "javascript-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Making a property read-only", "Using defineProperty to lock a value"],
        ]),
    },
    "javascript-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Tracing an inherited method", "Following the prototype chain to find where a method is defined"],
        ]),
    },
    "javascript-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Building objects with a constructor", "Creating multiple similar objects using new"],
        ]),
    },
    "javascript-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Serializing data for storage", "Converting a JS object to JSON before saving it"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["JavaScript"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json JavaScript: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 JavaScript lessons (completing 70/70).")


if __name__ == "__main__":
    main()
