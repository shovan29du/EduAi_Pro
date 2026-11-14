#!/usr/bin/env python3
"""Depth pass, C2 Web Development: fill in real, hand-checked
data_table/formulae (real runnable code) content for the 69 C2 Web
Development lessons not covered by the earlier breadth-first batch.
Brings C2 Web Development to full 70/70 coverage.

l61-l62 are "Foundations 2" lessons revisiting l49 and l6; l63-l70 are
"Worked Analysis" companions to l1-l8. l3 was already completed by an
earlier breadth-first batch, so its data_table is hard-coded here for
reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_web_development_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "web-development-c2-l1": {
        "data_table": table(["Technique", "Purpose"], [
            ["Media query", "Applies different CSS rules based on viewport width"],
        ]),
        "formulae": ["@media (max-width: 768px) {\n  .container { flex-direction: column; }\n}"],
    },
    "web-development-c2-l2": {
        "data_table": table(["Method", "Purpose"], [
            ["addEventListener", "Attaches a handler function to a DOM event"],
        ]),
        "formulae": ["document.querySelector('button').addEventListener('click', () => {\n  console.log('clicked');\n});"],
    },
    "web-development-c2-l4": {
        "data_table": table(["Method", "Purpose"], [
            ["Array.map", "Transforms each element, returning a new array"],
            ["Array.filter", "Returns a new array of elements passing a test"],
        ]),
        "formulae": ["const doubled = [1, 2, 3].map(n => n * 2);"],
    },
    "web-development-c2-l5": {
        "data_table": table(["Keyword", "Purpose"], [
            ["async", "Marks a function as returning a Promise"],
            ["await", "Pauses execution until a Promise resolves"],
        ]),
        "formulae": ["async function getData() {\n  const res = await fetch('/api/data');\n  return res.json();\n}"],
    },
    "web-development-c2-l6": {
        "data_table": table(["Property", "Purpose"], [
            ["transition", "Smoothly animates a CSS property change over time"],
        ]),
        "formulae": [".box { transition: transform 0.3s ease; }\n.box:hover { transform: scale(1.1); }"],
    },
    "web-development-c2-l7": {
        "data_table": table(["Feature", "Purpose"], [
            ["Nesting", "Allows CSS rules to be written inside one another"],
            ["Variables", "Store reusable values like colors and sizes"],
        ]),
        "formulae": ["$primary: #3498db;\n.button { background: $primary; &:hover { background: darken($primary, 10%); } }"],
    },
    "web-development-c2-l8": {
        "data_table": table(["Feature", "Benefit"], [
            ["Static typing", "Catches type errors at compile time rather than runtime"],
        ]),
        "formulae": ["function add(a: number, b: number): number {\n  return a + b;\n}"],
    },
    "web-development-c2-l9": {
        "data_table": table(["Command", "Purpose"], [
            ["git branch", "Lists or creates branches"],
            ["git merge", "Combines changes from one branch into another"],
        ]),
        "formulae": ["git checkout -b feature/login\ngit checkout main\ngit merge feature/login"],
    },
    "web-development-c2-l10": {
        "data_table": table(["File", "Purpose"], [
            ["package.json", "Declares project dependencies and scripts"],
            ["package-lock.json", "Pins exact installed dependency versions"],
        ]),
        "formulae": ["npm install lodash\nnpm run build"],
    },
    "web-development-c2-l11": {
        "data_table": table(["Tool", "Purpose"], [
            ["Webpack/Vite", "Bundles modular source files into optimized production assets"],
        ]),
    },
    "web-development-c2-l12": {
        "data_table": table(["API", "Persistence"], [
            ["localStorage", "Persists data across browser sessions"],
            ["sessionStorage", "Clears data when the tab is closed"],
        ]),
        "formulae": ["localStorage.setItem('theme', 'dark');\nconst theme = localStorage.getItem('theme');"],
    },
    "web-development-c2-l13": {
        "data_table": table(["Method", "Purpose"], [
            ["fetch()", "Makes an HTTP request and returns a Promise for the response"],
        ]),
        "formulae": ["fetch('/api/users').then(res => res.json()).then(data => console.log(data));"],
    },
    "web-development-c2-l14": {
        "data_table": table(["Attribute", "Purpose"], [
            ["required", "Prevents form submission until the field is filled"],
            ["pattern", "Validates input against a regular expression"],
        ]),
    },
    "web-development-c2-l15": {
        "data_table": table(["Framework", "Approach"], [
            ["Bootstrap", "Provides pre-styled components and a grid system"],
            ["Tailwind", "Provides low-level utility classes composed directly in markup"],
        ]),
    },
    "web-development-c2-l16": {
        "data_table": table(["Principle", "Detail"], [
            ["Mobile-first design", "Styles are written for small screens first, then progressively enhanced"],
        ]),
    },
    "web-development-c2-l17": {
        "data_table": table(["Practice", "Purpose"], [
            ["Cross-browser testing", "Verifies consistent rendering and behavior across different browsers"],
        ]),
    },
    "web-development-c2-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Web component", "Encapsulated, reusable custom HTML element with its own logic and style"],
        ]),
    },
    "web-development-c2-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Single Page Application", "Loads a single HTML page and updates content dynamically without full reloads"],
        ]),
    },
    "web-development-c2-l20": {
        "data_table": table(["Tool", "Purpose"], [
            ["Breakpoint", "Pauses JavaScript execution at a specific line for inspection"],
        ]),
    },
    "web-development-c2-l21": {
        "data_table": table(["Property", "Purpose"], [
            ["grid-template-areas", "Names grid regions for readable layout definitions"],
        ]),
        "formulae": [".layout { display: grid; grid-template-columns: 200px 1fr; }"],
    },
    "web-development-c2-l22": {
        "data_table": table(["Property", "Purpose"], [
            ["flex-grow", "Controls how much a flex item expands to fill space"],
        ]),
        "formulae": [".item { flex: 1 1 auto; }"],
    },
    "web-development-c2-l23": {
        "data_table": table(["Part", "Meaning"], [
            ["Block", "Standalone component, e.g. .card"],
            ["Element", "A part of a block, e.g. .card__title"],
            ["Modifier", "A variant, e.g. .card--featured"],
        ]),
    },
    "web-development-c2-l24": {
        "data_table": table(["Feature", "Purpose"], [
            ["CSS custom property", "Defines a reusable value that can be referenced with var()"],
        ]),
        "formulae": [":root { --primary: #3498db; }\n.button { color: var(--primary); }"],
    },
    "web-development-c2-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Closure", "A function retains access to variables from its enclosing scope after that scope exits"],
        ]),
        "formulae": ["function counter() {\n  let n = 0;\n  return () => ++n;\n}\nconst inc = counter();"],
    },
    "web-development-c2-l26": {
        "data_table": table(["Component", "Role"], [
            ["Call stack", "Tracks currently executing function calls"],
            ["Event loop", "Moves queued callbacks onto the call stack when it's empty"],
        ]),
    },
    "web-development-c2-l27": {
        "data_table": table(["Method", "Purpose"], [
            ["Promise.catch", "Handles a rejected Promise"],
            ["try/catch with await", "Handles errors from an awaited async call"],
        ]),
        "formulae": ["try {\n  await fetch('/api');\n} catch (err) {\n  console.error(err);\n}"],
    },
    "web-development-c2-l28": {
        "data_table": table(["Keyword", "Purpose"], [
            ["import", "Brings exported bindings from another module into scope"],
            ["export", "Makes a binding available to other modules"],
        ]),
        "formulae": ["export function add(a, b) { return a + b; }\nimport { add } from './math.js';"],
    },
    "web-development-c2-l29": {
        "data_table": table(["Property", "Purpose"], [
            ["closest()", "Finds the nearest matching ancestor element"],
        ]),
        "formulae": ["element.closest('.card')"],
    },
    "web-development-c2-l30": {
        "data_table": table(["API", "Purpose"], [
            ["customElements.define", "Registers a new custom HTML element"],
        ]),
        "formulae": ["class MyButton extends HTMLElement {}\ncustomElements.define('my-button', MyButton);"],
    },
    "web-development-c2-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Shadow DOM", "Encapsulates a component's internal markup and styles from the rest of the page"],
        ]),
    },
    "web-development-c2-l32": {
        "data_table": table(["Approach", "Detail"], [
            ["Centralized state management", "A single store holds shared application state accessible across components"],
        ]),
    },
    "web-development-c2-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["React component", "A reusable function or class that returns UI described in JSX"],
        ]),
        "formulae": ["function Greeting({ name }) {\n  return <h1>Hello, {name}</h1>;\n}"],
    },
    "web-development-c2-l34": {
        "data_table": table(["Principle", "Detail"], [
            ["Component-based architecture", "Builds UI from small, reusable, composable pieces"],
        ]),
    },
    "web-development-c2-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Vue reactivity", "Automatically updates the DOM when reactive data changes"],
        ]),
    },
    "web-development-c2-l36": {
        "data_table": table(["Concept", "Benefit"], [
            ["Server-side rendering", "Renders initial HTML on the server for faster first paint and SEO"],
        ]),
    },
    "web-development-c2-l37": {
        "data_table": table(["Concept", "Benefit"], [
            ["Static site generation", "Pre-builds HTML pages at build time for fast, cacheable delivery"],
        ]),
    },
    "web-development-c2-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Node.js", "Runs JavaScript outside the browser using an event-driven, non-blocking model"],
        ]),
        "formulae": ["const http = require('http');\nhttp.createServer((req, res) => res.end('Hello')).listen(3000);"],
    },
    "web-development-c2-l39": {
        "data_table": table(["Method", "Purpose"], [
            ["app.get()", "Defines a route handler for GET requests in Express"],
        ]),
        "formulae": ["const express = require('express');\nconst app = express();\napp.get('/', (req, res) => res.send('Hi'));"],
    },
    "web-development-c2-l40": {
        "data_table": table(["Principle", "Detail"], [
            ["RESTful design", "Resources are addressed by URLs and manipulated via standard HTTP verbs"],
        ]),
    },
    "web-development-c2-l41": {
        "data_table": table(["Feature", "Detail"], [
            ["GraphQL query", "Clients request exactly the fields they need in a single request"],
        ]),
        "formulae": ["query { user(id: 1) { name email } }"],
    },
    "web-development-c2-l42": {
        "data_table": table(["Concept", "Meaning"], [
            ["Authentication", "Verifies who a user is"],
            ["Authorization", "Determines what an authenticated user may do"],
        ]),
    },
    "web-development-c2-l43": {
        "data_table": table(["Part", "Content"], [
            ["JWT header", "Specifies the token type and signing algorithm"],
            ["JWT payload", "Contains claims about the authenticated user"],
        ]),
    },
    "web-development-c2-l44": {
        "data_table": table(["Threat", "Mitigation"], [
            ["SQL injection", "Use parameterized queries instead of string concatenation"],
        ]),
    },
    "web-development-c2-l45": {
        "data_table": table(["Threat", "Mitigation"], [
            ["Cross-site scripting (XSS)", "Escape or sanitize any user-supplied content before rendering"],
            ["CSRF", "Use anti-CSRF tokens tied to the user's session"],
        ]),
    },
    "web-development-c2-l46": {
        "data_table": table(["Tool", "Purpose"], [
            ["Axe/Lighthouse accessibility audit", "Automatically flags common accessibility violations"],
        ]),
    },
    "web-development-c2-l47": {
        "data_table": table(["Attribute", "Purpose"], [
            ["srcset", "Offers multiple image resolutions so the browser picks the best fit"],
        ]),
        "formulae": ["<img src=\"small.jpg\" srcset=\"large.jpg 1024w, small.jpg 480w\">"],
    },
    "web-development-c2-l48": {
        "data_table": table(["Feature", "Benefit"], [
            ["Progressive Web App", "Combines web reach with app-like installability and offline support"],
        ]),
    },
    "web-development-c2-l49": {
        "data_table": table(["Component", "Purpose"], [
            ["Service worker", "Intercepts network requests to enable offline caching"],
        ]),
        "formulae": ["self.addEventListener('fetch', event => {\n  event.respondWith(caches.match(event.request));\n});"],
    },
    "web-development-c2-l50": {
        "data_table": table(["Technology", "Feature"], [
            ["WebSocket", "Maintains a persistent, bidirectional connection for real-time communication"],
        ]),
        "formulae": ["const socket = new WebSocket('wss://example.com');\nsocket.onmessage = e => console.log(e.data);"],
    },
    "web-development-c2-l51": {
        "data_table": table(["Concept", "Purpose"], [
            ["Continuous integration", "Automatically builds and tests code on every commit"],
        ]),
    },
    "web-development-c2-l52": {
        "data_table": table(["Test Type", "Scope"], [
            ["Unit test", "Verifies a single function in isolation"],
            ["Integration test", "Verifies multiple components work together"],
        ]),
    },
    "web-development-c2-l53": {
        "data_table": table(["Function", "Purpose"], [
            ["test()", "Defines a test case in Jest"],
            ["expect()", "Asserts an expected outcome"],
        ]),
        "formulae": ["test('adds numbers', () => {\n  expect(add(2, 3)).toBe(5);\n});"],
    },
    "web-development-c2-l54": {
        "data_table": table(["Concept", "Scope"], [
            ["End-to-end test", "Simulates a real user workflow through the full application"],
        ]),
    },
    "web-development-c2-l55": {
        "data_table": table(["Command", "Effect"], [
            ["git rebase", "Replays commits onto a new base for a linear history"],
            ["git cherry-pick", "Applies a specific commit onto another branch"],
        ]),
        "formulae": ["git rebase main\ngit cherry-pick abc1234"],
    },
    "web-development-c2-l56": {
        "data_table": table(["Concept", "Benefit"], [
            ["Containerization", "Packages an app with its dependencies for consistent deployment"],
        ]),
        "formulae": ["FROM node:20-slim\nCOPY . /app\nWORKDIR /app\nRUN npm install\nCMD [\"node\", \"server.js\"]"],
    },
    "web-development-c2-l57": {
        "data_table": table(["Technique", "Purpose"], [
            ["Code splitting", "Loads only the JavaScript needed for the current view"],
            ["Lazy loading", "Defers loading of off-screen images and resources"],
        ]),
    },
    "web-development-c2-l58": {
        "data_table": table(["Metric", "Meaning"], [
            ["Largest Contentful Paint", "Measures when the main content becomes visible"],
            ["Cumulative Layout Shift", "Measures unexpected visual layout movement"],
        ]),
    },
    "web-development-c2-l59": {
        "data_table": table(["Approach", "Detail"], [
            ["CSS-in-JS", "Writes component-scoped styles directly within JavaScript code"],
        ]),
    },
    "web-development-c2-l60": {
        "data_table": table(["Tool", "Purpose"], [
            ["Browser DevTools debugger", "Inspects live DOM state, network activity, and JavaScript execution"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Declaration", "Reassignable?"], [
    ["var", "Yes (function-scoped)"], ["let", "Yes (block-scoped)"], ["const", "No (block-scoped)"],
])

# l61-l62 "Foundations 2" lessons revisit l49 and l6.
FOUNDATIONS_2_MAP = {61: 49, 62: 6}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"web-development-c2-l{base_n}"
    fields = {"data_table": CHARTS[base_key]["data_table"]}
    if "formulae" in CHARTS[base_key]:
        fields["formulae"] = CHARTS[base_key]["formulae"]
    CHARTS[f"web-development-c2-l{worked_n}"] = fields

# l63-l70 "Worked Analysis" lessons reuse the data_table/formulae of l1-l8.
WORKED_ANALYSIS_MAP = {63: 1, 64: 2, 65: 3, 66: 4, 67: 5, 68: 6, 69: 7, 70: 8}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"web-development-c2-l{base_n}"
    if base_key in CHARTS:
        fields = {"data_table": CHARTS[base_key]["data_table"]}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = CHARTS[base_key]["formulae"]
        CHARTS[f"web-development-c2-l{worked_n}"] = fields
    elif base_n == 3:
        CHARTS[f"web-development-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Web Development"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Web Development: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Web Development lessons (completing 70/70).")


if __name__ == "__main__":
    main()
