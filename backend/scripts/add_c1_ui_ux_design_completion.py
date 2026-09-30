#!/usr/bin/env python3
"""Depth pass, C1 UI/UX Design: fill in real, hand-checked data_table
content for the 69 C1 UI/UX Design lessons not covered by the earlier
breadth-first batch. Brings C1 UI/UX Design to full 70/70 coverage.

Note: lesson ids 1-60 use the "ui/ux-design-c1-lN" prefix (with a
slash) while ids 61-70 use "ui-ux-design-c1-lN" (hyphenated) -- both
are preserved exactly as they appear in the syllabus JSON.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_ui_ux_design_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ui/ux-design-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["UI design", "Focuses on the visual interface"], ["UX design", "Focuses on the overall user experience"],
        ]),
    },
    "ui/ux-design-c1-l2": {
        "data_table": table(["Method", "Type"], [
            ["Interviews", "Qualitative research"], ["Surveys", "Quantitative research"],
        ]),
    },
    "ui/ux-design-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Pain point", "A specific problem users encounter"],
        ]),
    },
    "ui/ux-design-c1-l5": {
        "data_table": table(["Heuristic", "Meaning"], [
            ["Visibility of system status", "Keeps users informed about what's happening"],
        ]),
    },
    "ui/ux-design-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Persona", "A fictional user profile based on research, representing a user group"],
        ]),
    },
    "ui/ux-design-c1-l7": {
        "data_table": table(["Element", "Purpose"], [
            ["Touchpoint", "A specific interaction point in the user's journey"],
        ]),
    },
    "ui/ux-design-c1-l8": {
        "data_table": table(["Technique", "Purpose"], [
            ["Sketching", "Quickly explores many ideas before committing to one"],
        ]),
    },
    "ui/ux-design-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Grid system", "A structure of columns and rows that organizes layout"],
        ]),
    },
    "ui/ux-design-c1-l10": {
        "data_table": table(["Practice", "Benefit"], [
            ["Design critique", "Structured feedback that improves a design before launch"],
        ]),
    },
    "ui/ux-design-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Low-fidelity prototype", "A simple, quick mockup used to test concepts early"],
        ]),
    },
    "ui/ux-design-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["User flow", "The path a user takes to complete a task in an interface"],
        ]),
    },
    "ui/ux-design-c1-l13": {
        "data_table": table(["Principle", "Meaning"], [
            ["Icon clarity", "Icons should be instantly recognizable and unambiguous"],
        ]),
    },
    "ui/ux-design-c1-l14": {
        "data_table": table(["Role", "Focus"], [
            ["UX researcher", "Studies user behavior and needs"], ["UI designer", "Crafts the visual interface"],
        ]),
    },
    "ui/ux-design-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Affordance", "A visual cue suggesting how an object can be used"], ["Signifier", "An explicit indicator of how to interact"],
        ]),
    },
    "ui/ux-design-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Content hierarchy", "Organizing content by importance to guide the user's eye"],
        ]),
    },
    "ui/ux-design-c1-l17": {
        "data_table": table(["Principle", "Reason"], [
            ["Minimal required fields", "Reduces friction and abandonment in forms"],
        ]),
    },
    "ui/ux-design-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Empathy map", "A tool capturing what a user says, thinks, feels, and does"],
        ]),
    },
    "ui/ux-design-c1-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Competitive UX audit", "Identifies strengths and weaknesses in competitor products"],
        ]),
    },
    "ui/ux-design-c1-l20": {
        "data_table": table(["Principle", "Meaning"], [
            ["Avoiding dark patterns", "Designing interfaces that respect user intent, not manipulate it"],
        ]),
    },
    "ui/ux-design-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Color contrast", "The difference in luminance affecting text readability"],
        ]),
    },
    "ui/ux-design-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Typography", "The art and technique of arranging text for readability and style"],
        ]),
    },
    "ui/ux-design-c1-l23": {
        "data_table": table(["Principle", "Meaning"], [
            ["Visual hierarchy", "Arranging elements to show their order of importance"],
        ]),
    },
    "ui/ux-design-c1-l24": {
        "data_table": table(["Principle", "Meaning"], [
            ["Proximity", "Elements close together are perceived as related"], ["Similarity", "Similar elements are perceived as grouped"],
        ]),
    },
    "ui/ux-design-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Design system", "A collection of reusable components and standards for consistent design"],
        ]),
    },
    "ui/ux-design-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Component library", "A repository of reusable UI elements like buttons and inputs"],
        ]),
    },
    "ui/ux-design-c1-l27": {
        "data_table": table(["Principle", "Meaning"], [
            ["Accessibility", "Designing so people with disabilities can use a product"],
        ]),
    },
    "ui/ux-design-c1-l28": {
        "data_table": table(["Standard", "Requirement"], [
            ["WCAG AA", "Minimum 4.5:1 contrast ratio for normal text"],
        ]),
    },
    "ui/ux-design-c1-l29": {
        "data_table": table(["Method", "Purpose"], [
            ["Usability testing", "Observes real users completing tasks to find problems"],
        ]),
    },
    "ui/ux-design-c1-l30": {
        "data_table": table(["Element", "Purpose"], [
            ["Task scenario", "Gives the participant a realistic goal to complete"],
        ]),
    },
    "ui/ux-design-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Interaction design", "Designing how users interact with a product's behavior"],
        ]),
    },
    "ui/ux-design-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Microinteraction", "A small, focused interaction, like a button animation on click"],
        ]),
    },
    "ui/ux-design-c1-l33": {
        "data_table": table(["Principle", "Reason"], [
            ["Thumb-friendly design", "Places key actions within easy reach on mobile"],
        ]),
    },
    "ui/ux-design-c1-l34": {
        "data_table": table(["Guideline", "Detail"], [
            ["Minimum touch target size", "Commonly recommended at 44x44 pixels"],
        ]),
    },
    "ui/ux-design-c1-l35": {
        "data_table": table(["Tool", "Purpose"], [
            ["Figma", "A collaborative interface design tool"],
        ]),
    },
    "ui/ux-design-c1-l36": {
        "data_table": table(["Feature", "Benefit"], [
            ["Real-time collaboration", "Multiple designers can edit a file simultaneously"],
        ]),
    },
    "ui/ux-design-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Visual identity", "The consistent visual elements representing a brand"],
        ]),
    },
    "ui/ux-design-c1-l38": {
        "data_table": table(["Element", "Purpose"], [
            ["Logo", "A distinctive symbol identifying a brand"],
        ]),
    },
    "ui/ux-design-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Microcopy", "Small pieces of text that guide users, like button labels"],
        ]),
    },
    "ui/ux-design-c1-l40": {
        "data_table": table(["Principle", "Example"], [
            ["Clear, actionable error messages", "'Password must be 8+ characters' instead of 'Invalid input'"],
        ]),
    },
    "ui/ux-design-c1-l41": {
        "data_table": table(["Goal", "Reason"], [
            ["Onboarding", "Helps new users understand a product's value quickly"],
        ]),
    },
    "ui/ux-design-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Empty state", "The screen shown when there is no content yet, e.g. an empty inbox"],
        ]),
    },
    "ui/ux-design-c1-l43": {
        "data_table": table(["Tool", "Purpose"], [
            ["Mood board", "A visual collage establishing a design's tone and style"],
        ]),
    },
    "ui/ux-design-c1-l44": {
        "data_table": table(["Document", "Purpose"], [
            ["Style guide", "Documents colors, fonts, and component usage rules"],
        ]),
    },
    "ui/ux-design-c1-l45": {
        "data_table": table(["Stage", "Purpose"], [
            ["Empathize", "Understand the user's needs"], ["Define", "Frame the problem clearly"], ["Ideate", "Generate solutions"],
        ]),
    },
    "ui/ux-design-c1-l46": {
        "data_table": table(["Thinking Type", "Purpose"], [
            ["Divergent", "Generates many possible ideas"], ["Convergent", "Narrows down to the best idea"],
        ]),
    },
    "ui/ux-design-c1-l47": {
        "data_table": table(["Method", "Purpose"], [
            ["Heuristic evaluation", "Experts review an interface against established usability principles"],
        ]),
    },
    "ui/ux-design-c1-l48": {
        "data_table": table(["Heuristic", "Meaning"], [
            ["Visibility of system status", "Keeps users informed"], ["User control and freedom", "Provides an 'undo' option"],
        ]),
    },
    "ui/ux-design-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["A/B testing", "Comparing two design versions to see which performs better"],
        ]),
    },
    "ui/ux-design-c1-l50": {
        "data_table": table(["Dark Pattern", "Example"], [
            ["Confirmshaming", "Guilt-tripping users for declining an offer"],
        ]),
    },
    "ui/ux-design-c1-l51": {
        "data_table": table(["Principle", "Purpose"], [
            ["Motion for feedback", "Confirms an action was received"],
        ]),
    },
    "ui/ux-design-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Easing", "How an animation's speed changes over its duration"],
        ]),
    },
    "ui/ux-design-c1-l53": {
        "data_table": table(["Principle", "Meaning"], [
            ["Responsive design", "A layout that adapts to different screen sizes"],
        ]),
    },
    "ui/ux-design-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Breakpoint", "A screen width where the layout changes to fit better"],
        ]),
    },
    "ui/ux-design-c1-l55": {
        "data_table": table(["Platform", "Consideration"], [
            ["iOS", "Follows Apple's Human Interface Guidelines"], ["Android", "Follows Google's Material Design"],
        ]),
    },
    "ui/ux-design-c1-l56": {
        "data_table": table(["Guideline Set", "Platform"], [
            ["Human Interface Guidelines", "Apple/iOS"], ["Material Design", "Google/Android"],
        ]),
    },
    "ui/ux-design-c1-l57": {
        "data_table": table(["Practice", "Reason"], [
            ["Asking open-ended questions", "Reveals deeper user motivations"],
        ]),
    },
    "ui/ux-design-c1-l58": {
        "data_table": table(["Practice", "Reason"], [
            ["Avoiding leading questions", "Prevents biasing the participant's answer"],
        ]),
    },
    "ui/ux-design-c1-l59": {
        "data_table": table(["Question Type", "Use"], [
            ["Likert scale", "Measures agreement on a numeric scale"],
        ]),
    },
    "ui/ux-design-c1-l60": {
        "data_table": table(["Element", "Purpose"], [
            ["Case study", "Shows the process and outcome behind a design project"],
        ]),
    },
}

# Lessons 61-70 use the hyphenated "ui-ux-design-c1-lN" prefix.
CHARTS.update({
    "ui-ux-design-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying the double diamond", "Mapping a redesign project onto its four stages"],
        ]),
    },
    "ui-ux-design-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Planning a research study", "Choosing between interviews and surveys for a given question"],
        ]),
    },
    "ui-ux-design-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Diverging then converging", "Brainstorming ten ideas before narrowing to one"],
        ]),
    },
    "ui-ux-design-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a pain point", "Finding where users get stuck in a sample checkout flow"],
        ]),
    },
    "ui-ux-design-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Applying a heuristic", "Checking a sample screen against 'visibility of system status'"],
        ]),
    },
    "ui-ux-design-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Building a persona", "Turning research notes into a one-page user persona"],
        ]),
    },
    "ui-ux-design-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Mapping a user journey", "Charting the steps and emotions in a sample task"],
        ]),
    },
    "ui-ux-design-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Sketching alternatives", "Producing three quick layout sketches for one screen"],
        ]),
    },
    "ui-ux-design-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Applying a grid", "Aligning a sample page's elements to a 12-column grid"],
        ]),
    },
    "ui-ux-design-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Giving a design critique", "Providing structured feedback on a sample screen"],
        ]),
    },
})


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["UI/UX Design"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json UI/UX Design: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 UI/UX Design lessons (completing 70/70).")


if __name__ == "__main__":
    main()
