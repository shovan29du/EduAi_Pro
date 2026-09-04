#!/usr/bin/env python3
"""Depth pass, C1 Web Development: fill in real, hand-checked
data_table content for the 69 C1 Web Development lessons not covered
by the earlier breadth-first batch. Brings C1 Web Development to full
70/70 coverage.

Examples use real, runnable HTML/CSS/JS syntax.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_web_development_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "web-development-c1-l1": {
        "data_table": table(["Language", "Purpose"], [
            ["HTML", "Structures web content"], ["CSS", "Styles web content"],
        ]),
        "formulae": ["<h1>Title</h1>", "<p>Some text.</p>"],
    },
    "web-development-c1-l2": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "let x = 5;"],
        ]),
        "formulae": ["let x = 5;", "console.log(x);"],
    },
    "web-development-c1-l4": {
        "data_table": table(["Layer", "From Inside Out"], [
            ["Content, padding, border, margin", "The four layers of the CSS box model"],
        ]),
        "formulae": ["div { padding: 10px; border: 1px solid; margin: 5px; }"],
    },
    "web-development-c1-l5": {
        "data_table": table(["Property", "Effect"], [
            ["display: flex", "Enables flexbox layout"], ["justify-content", "Aligns items horizontally"],
        ]),
        "formulae": [".container { display: flex; justify-content: center; }"],
    },
    "web-development-c1-l6": {
        "data_table": table(["Property", "Effect"], [
            ["display: grid", "Enables grid layout"], ["grid-template-columns", "Defines column sizes"],
        ]),
        "formulae": [".container { display: grid; grid-template-columns: 1fr 1fr; }"],
    },
    "web-development-c1-l7": {
        "data_table": table(["Principle", "Example"], [
            ["Alt text", "Describes images for screen readers"],
        ]),
        "formulae": ["<img src=\"cat.jpg\" alt=\"A sleeping cat\">"],
    },
    "web-development-c1-l8": {
        "data_table": table(["Tool", "Purpose"], [
            ["Elements panel", "Inspects and edits the DOM live"], ["Console", "Runs JavaScript and shows logs"],
        ]),
    },
    "web-development-c1-l9": {
        "data_table": table(["Command", "Purpose"], [
            ["git commit", "Saves a snapshot of changes"], ["git push", "Uploads commits to a remote repository"],
        ]),
        "formulae": ["git add .", "git commit -m \"message\""],
    },
    "web-development-c1-l10": {
        "data_table": table(["Type", "Example"], [
            ["Number", "5"], ["String", "'hello'"], ["Boolean", "true"],
        ]),
    },
    "web-development-c1-l11": {
        "data_table": table(["Attribute", "Purpose"], [
            ["required", "Marks a field as mandatory"], ["type=\"email\"", "Validates email format"],
        ]),
        "formulae": ["<input type=\"email\" required>"],
    },
    "web-development-c1-l12": {
        "data_table": table(["Selector", "Specificity"], [
            ["Inline style", "Highest"], ["ID selector", "High"], ["Class selector", "Medium"], ["Element selector", "Low"],
        ]),
    },
    "web-development-c1-l13": {
        "data_table": table(["Property", "Purpose"], [
            ["font-family", "Sets the typeface"], ["line-height", "Sets spacing between lines"],
        ]),
    },
    "web-development-c1-l14": {
        "data_table": table(["Attribute", "Purpose"], [
            ["srcset", "Serves different image sizes for different screens"],
        ]),
    },
    "web-development-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Web hosting", "A service that stores website files and serves them to visitors"],
        ]),
    },
    "web-development-c1-l16": {
        "data_table": table(["Method", "Purpose"], [
            ["GET", "Requests data"], ["POST", "Sends data to be processed"],
        ]),
    },
    "web-development-c1-l17": {
        "data_table": table(["Format", "Feature"], [
            ["JSON", "Lightweight, human-readable data exchange format"],
        ]),
        "formulae": ["{\"name\": \"Sam\", \"age\": 20}"],
    },
    "web-development-c1-l18": {
        "data_table": table(["Command", "Purpose"], [
            ["cd", "Changes directory"], ["ls", "Lists files"],
        ]),
    },
    "web-development-c1-l19": {
        "data_table": table(["Feature", "Benefit"], [
            ["Syntax highlighting", "Makes code easier to read"], ["Extensions", "Add linting, formatting, and more"],
        ]),
    },
    "web-development-c1-l20": {
        "data_table": table(["Tag", "Purpose"], [
            ["<title>", "Sets the browser tab title, important for SEO"],
        ]),
    },
    "web-development-c1-l21": {
        "data_table": table(["Value", "Behavior"], [
            ["static", "Default, normal document flow"], ["absolute", "Positioned relative to nearest positioned ancestor"],
        ]),
    },
    "web-development-c1-l22": {
        "data_table": table(["Unit", "Meaning"], [
            ["px", "Fixed pixel size"], ["em", "Relative to parent font size"], ["rem", "Relative to root font size"],
        ]),
    },
    "web-development-c1-l23": {
        "data_table": table(["Syntax", "Example"], [
            ["CSS variable", "--main-color: blue;"],
        ]),
        "formulae": [":root { --main-color: blue; }", "p { color: var(--main-color); }"],
    },
    "web-development-c1-l24": {
        "data_table": table(["Type", "Example"], [
            ["Pseudo-class", ":hover"], ["Pseudo-element", "::before"],
        ]),
        "formulae": ["a:hover { color: red; }"],
    },
    "web-development-c1-l25": {
        "data_table": table(["Tag", "Purpose"], [
            ["<table>", "Defines a table"], ["<tr>", "A table row"], ["<td>", "A table cell"],
        ]),
    },
    "web-development-c1-l26": {
        "data_table": table(["Tag", "Purpose"], [
            ["<ul>", "Unordered list"], ["<nav>", "Navigation menu container"],
        ]),
    },
    "web-development-c1-l27": {
        "data_table": table(["Syntax", "Example"], [
            ["Function", "function greet() { return 'Hi'; }"],
        ]),
        "formulae": ["function greet() {", "  return \"Hi\";", "}"],
    },
    "web-development-c1-l28": {
        "data_table": table(["Method", "Effect"], [
            [".map()", "Transforms each item into a new array"], [".filter()", "Keeps items matching a condition"],
        ]),
    },
    "web-development-c1-l29": {
        "data_table": table(["Syntax", "Example"], [
            ["Object literal", "{ name: 'Sam' }"],
        ]),
    },
    "web-development-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["DOM", "The browser's tree representation of an HTML page"],
        ]),
        "formulae": ["document.getElementById(\"title\")"],
    },
    "web-development-c1-l31": {
        "data_table": table(["Method", "Purpose"], [
            ["addEventListener()", "Runs code in response to an event like a click"],
        ]),
        "formulae": ["btn.addEventListener(\"click\", () => alert(\"Clicked!\"));"],
    },
    "web-development-c1-l32": {
        "data_table": table(["Attribute", "Purpose"], [
            ["required", "Prevents submission if empty"], ["pattern", "Validates against a regex"],
        ]),
    },
    "web-development-c1-l33": {
        "data_table": table(["Format", "Example"], [
            ["Hex", "#ff0000"], ["RGB", "rgb(255, 0, 0)"],
        ]),
    },
    "web-development-c1-l34": {
        "data_table": table(["Property", "Effect"], [
            ["transition", "Animates a property change smoothly"],
        ]),
        "formulae": ["button { transition: background-color 0.3s; }"],
    },
    "web-development-c1-l35": {
        "data_table": table(["Rule", "Purpose"], [
            ["@media (max-width: 600px)", "Applies styles only on small screens"],
        ]),
        "formulae": ["@media (max-width: 600px) { body { font-size: 14px; } }"],
    },
    "web-development-c1-l36": {
        "data_table": table(["Principle", "Meaning"], [
            ["Mobile-first design", "Designing for small screens first, then scaling up"],
        ]),
    },
    "web-development-c1-l37": {
        "data_table": table(["Factor", "Impact"], [
            ["Image size", "Large images slow page load"],
        ]),
    },
    "web-development-c1-l38": {
        "data_table": table(["Technique", "Benefit"], [
            ["Compression", "Reduces file size without major quality loss"],
        ]),
    },
    "web-development-c1-l39": {
        "data_table": table(["Tag", "Purpose"], [
            ["<link rel=\"icon\">", "Sets the favicon"], ["<meta name=\"description\">", "Sets the page's search snippet"],
        ]),
    },
    "web-development-c1-l40": {
        "data_table": table(["Step", "Description"], [
            ["Request", "Browser asks the server for a resource"], ["Response", "Server sends back the requested data"],
        ]),
    },
    "web-development-c1-l41": {
        "data_table": table(["Code", "Meaning"], [
            ["200", "OK"], ["404", "Not Found"], ["500", "Server Error"],
        ]),
    },
    "web-development-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Cookie", "Small data stored in the browser, sent with each request"], ["Session", "Server-side data tied to a user's visit"],
        ]),
    },
    "web-development-c1-l43": {
        "data_table": table(["Threat", "Prevention"], [
            ["SQL injection", "Use parameterized queries"], ["XSS", "Escape user input before rendering"],
        ]),
    },
    "web-development-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["XSS", "Cross-Site Scripting, injecting malicious scripts into a trusted webpage"],
        ]),
    },
    "web-development-c1-l45": {
        "data_table": table(["Command", "Purpose"], [
            ["SELECT", "Retrieves data"], ["WHERE", "Filters results"],
        ]),
        "formulae": ["SELECT name FROM users WHERE active = 1;"],
    },
    "web-development-c1-l46": {
        "data_table": table(["Role", "Responsibility"], [
            ["Client", "Requests and displays data"], ["Server", "Processes requests and returns data"],
        ]),
    },
    "web-development-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["API", "A defined way for programs to communicate"], ["Endpoint", "A specific URL an API exposes"],
        ]),
    },
    "web-development-c1-l48": {
        "data_table": table(["Principle", "Meaning"], [
            ["Statelessness", "Each request contains all information needed to process it"],
        ]),
    },
    "web-development-c1-l49": {
        "data_table": table(["Engine", "Browser"], [
            ["Blink", "Chrome, Edge"], ["Gecko", "Firefox"], ["WebKit", "Safari"],
        ]),
    },
    "web-development-c1-l50": {
        "data_table": table(["Tool", "Purpose"], [
            ["Breakpoints", "Pauses code execution to inspect state"],
        ]),
    },
    "web-development-c1-l51": {
        "data_table": table(["Platform", "Feature"], [
            ["GitHub Pages", "Free static site hosting from a repository"],
        ]),
    },
    "web-development-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["DNS", "Translates domain names into IP addresses"],
        ]),
    },
    "web-development-c1-l53": {
        "data_table": table(["Service", "Purpose"], [
            ["Google Fonts", "Free web font library"],
        ]),
        "formulae": ["<link href=\"https://fonts.googleapis.com/css2?family=Roboto\" rel=\"stylesheet\">"],
    },
    "web-development-c1-l54": {
        "data_table": table(["Framework", "Feature"], [
            ["Bootstrap", "Prebuilt CSS components and grid system"], ["Tailwind CSS", "Utility-first CSS classes"],
        ]),
    },
    "web-development-c1-l55": {
        "data_table": table(["Tool", "Purpose"], [
            ["Wireframe", "A low-fidelity layout sketch before building a page"],
        ]),
    },
    "web-development-c1-l56": {
        "data_table": table(["Organization", "Role"], [
            ["W3C", "Develops and maintains web standards"],
        ]),
    },
    "web-development-c1-l57": {
        "data_table": table(["Principle", "Meaning"], [
            ["Progressive enhancement", "Building a basic working experience first, then adding advanced features"],
        ]),
    },
    "web-development-c1-l58": {
        "data_table": table(["Practice", "Reason"], [
            ["Cross-browser testing", "Ensures a page works consistently across browsers"],
        ]),
    },
    "web-development-c1-l59": {
        "data_table": table(["Tool", "Purpose"], [
            ["Local dev server", "Serves files locally for testing before deployment"],
        ]),
    },
    "web-development-c1-l60": {
        "data_table": table(["Syntax", "Renders As"], [
            ["# Heading", "<h1>Heading</h1>"], ["**bold**", "<strong>bold</strong>"],
        ]),
    },
    "web-development-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Building a simple page", "Combining HTML structure with CSS styling"],
        ]),
    },
    "web-development-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Adding interactivity", "Using JavaScript to change text when a button is clicked"],
        ]),
    },
    "web-development-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Improving accessibility", "Converting a div-based layout to semantic HTML5 tags"],
        ]),
    },
    "web-development-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Debugging spacing issues", "Using the box model to fix unexpected element overlap"],
        ]),
    },
    "web-development-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Building a navbar", "Using flexbox to align navigation links horizontally"],
        ]),
    },
    "web-development-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Building a photo gallery", "Using CSS grid to arrange images in a responsive layout"],
        ]),
    },
    "web-development-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Auditing a page", "Checking color contrast and alt text for accessibility"],
        ]),
    },
    "web-development-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Inspecting a live site", "Using DevTools to find and fix a CSS bug"],
        ]),
    },
    "web-development-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Making a first commit", "Initializing a Git repo and committing a starter project"],
        ]),
    },
    "web-development-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Validating form input", "Writing JavaScript that checks a field is not empty before submit"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Web Development"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Web Development: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Web Development lessons (completing 70/70).")


if __name__ == "__main__":
    main()
