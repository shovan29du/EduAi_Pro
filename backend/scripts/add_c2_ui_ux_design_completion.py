#!/usr/bin/env python3
"""Depth pass, C2 UI/UX Design: fill in real, hand-checked data_table
content for the 69 C2 UI/UX Design lessons not covered by the earlier
breadth-first batch. Brings the subject to full 70/70 coverage.

Note: lesson ids l1-l64 use the prefix "ui/ux-design-c2-" with a literal
slash, while l65-l70 use "ui-ux-design-c2-" (hyphenated). Both forms are
preserved exactly as they exist in level_c2.json.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_ui_ux_design_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ui/ux-design-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Information architecture", "Organizing and structuring content so users can find it intuitively"],
        ]),
    },
    "ui/ux-design-c2-l2": {
        "data_table": table(["Fidelity", "Purpose"], [
            ["Wireframe", "Low-fidelity layout skeleton without visual styling"], ["Prototype", "An interactive simulation of the final product"],
        ]),
    },
    "ui/ux-design-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Tree testing", "Evaluates navigation findability using a text-only site hierarchy"],
        ]),
    },
    "ui/ux-design-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Sitemap", "A visual diagram of a product's page hierarchy and structure"],
        ]),
    },
    "ui/ux-design-c2-l6": {
        "data_table": table(["Pattern", "Use"], [
            ["Tab bar", "Primary navigation for mobile apps"], ["Hamburger menu", "Collapses secondary navigation to save space"],
        ]),
    },
    "ui/ux-design-c2-l7": {
        "data_table": table(["Fidelity", "Feature"], [
            ["Mid-fidelity wireframe", "Shows layout and hierarchy with more detail than sketches, less than final visuals"],
        ]),
    },
    "ui/ux-design-c2-l8": {
        "data_table": table(["Tool", "Use"], [
            ["Figma", "A widely used collaborative interface design and prototyping tool"],
        ]),
    },
    "ui/ux-design-c2-l9": {
        "data_table": table(["Step", "Purpose"], [
            ["Testing a clickable prototype", "Reveals usability issues before development begins"],
        ]),
    },
    "ui/ux-design-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Content model", "Defines the structure and relationships of content types within a product"],
        ]),
    },
    "ui/ux-design-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Taxonomy", "A structured classification system organizing content into categories"],
        ]),
    },
    "ui/ux-design-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Findability", "How easily users can locate information within a product"],
        ]),
    },
    "ui/ux-design-c2-l13": {
        "data_table": table(["Consideration", "Detail"], [
            ["Touch target size", "Mobile prototypes must account for finger-sized tap areas"],
        ]),
    },
    "ui/ux-design-c2-l14": {
        "data_table": table(["Purpose", "Detail"], [
            ["Storyboard", "Visualizes a user's journey through a sequence of key scenarios"],
        ]),
    },
    "ui/ux-design-c2-l15": {
        "data_table": table(["Benefit", "Detail"], [
            ["Paper prototyping", "Enables extremely fast, low-cost iteration before digital tools are used"],
        ]),
    },
    "ui/ux-design-c2-l16": {
        "data_table": table(["Document", "Purpose"], [
            ["Design rationale doc", "Explains the reasoning behind key design decisions"],
        ]),
    },
    "ui/ux-design-c2-l17": {
        "data_table": table(["Practice", "Reason"], [
            ["Annotating wireframes", "Clarifies interaction behavior and edge cases for developers"],
        ]),
    },
    "ui/ux-design-c2-l18": {
        "data_table": table(["Breakpoint", "Purpose"], [
            ["Mobile breakpoint", "Adjusts layout for small screens"], ["Desktop breakpoint", "Adjusts layout for large screens"],
        ]),
    },
    "ui/ux-design-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Micro-flow", "A small, focused sequence of interactions, like a password reset"],
        ]),
    },
    "ui/ux-design-c2-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Design handoff", "Transfers finalized design specs and assets to developers"],
        ]),
    },
    "ui/ux-design-c2-l21": {
        "data_table": table(["Layer", "Purpose"], [
            ["Design system", "A shared library of reusable components and standards"],
        ]),
    },
    "ui/ux-design-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Design token", "A named, platform-agnostic value like a color or spacing unit used across a design system"],
        ]),
    },
    "ui/ux-design-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["ARIA", "Accessible Rich Internet Applications, attributes that improve screen reader support"],
        ]),
    },
    "ui/ux-design-c2-l24": {
        "data_table": table(["Principle", "Meaning"], [
            ["Inclusive design", "Designs for the full range of human diversity, beyond minimum compliance"],
        ]),
    },
    "ui/ux-design-c2-l25": {
        "data_table": table(["Type", "Feature"], [
            ["Moderated testing", "A facilitator guides the session in real time"], ["Unmoderated testing", "Participants complete tasks independently, remotely"],
        ]),
    },
    "ui/ux-design-c2-l26": {
        "data_table": table(["Metric", "Meaning"], [
            ["Task success rate", "The percentage of users completing a task correctly"], ["Time on task", "How long users take to complete a task"],
        ]),
    },
    "ui/ux-design-c2-l27": {
        "data_table": table(["Pattern", "Use"], [
            ["Progressive disclosure", "Reveals complexity gradually to avoid overwhelming users"],
        ]),
    },
    "ui/ux-design-c2-l28": {
        "data_table": table(["State", "Example"], [
            ["Empty state", "Shown when there's no content yet"], ["Error state", "Shown when something goes wrong"],
        ]),
    },
    "ui/ux-design-c2-l29": {
        "data_table": table(["Gesture", "Common Use"], [
            ["Swipe", "Dismisses or navigates between items"], ["Pinch", "Zooms in or out"],
        ]),
    },
    "ui/ux-design-c2-l30": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Shared design tokens", "Maintains visual consistency across platforms"],
        ]),
    },
    "ui/ux-design-c2-l31": {
        "data_table": table(["Feature", "Benefit"], [
            ["Interactive components", "Enables realistic, functional prototype testing"],
        ]),
    },
    "ui/ux-design-c2-l32": {
        "data_table": table(["Practice", "Reason"], [
            ["Versioning a design system", "Tracks changes and prevents breaking downstream products"],
        ]),
    },
    "ui/ux-design-c2-l33": {
        "data_table": table(["Element", "Purpose"], [
            ["Brand voice", "Ensures consistent tone across digital touchpoints"],
        ]),
    },
    "ui/ux-design-c2-l34": {
        "data_table": table(["Consideration", "Detail"], [
            ["Conversational design", "Requires designing for natural language rather than visual navigation"],
        ]),
    },
    "ui/ux-design-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["UX writing", "Crafting concise, clear microcopy that guides users through a product"],
        ]),
    },
    "ui/ux-design-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Internationalization", "Designing a product to be adaptable to different languages and regions"],
        ]),
    },
    "ui/ux-design-c2-l37": {
        "data_table": table(["Step", "Purpose"], [
            ["Reducing onboarding friction", "Improves activation and reduces early user drop-off"],
        ]),
    },
    "ui/ux-design-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Persuasive pattern", "A design technique that nudges user behavior, sometimes ethically questionable"],
        ]),
    },
    "ui/ux-design-c2-l39": {
        "data_table": table(["Step", "Purpose"], [
            ["Facilitating a design sprint", "Aligns a team quickly around a shared problem and solution"],
        ]),
    },
    "ui/ux-design-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Co-design", "Involves users directly as collaborators in the design process"],
        ]),
    },
    "ui/ux-design-c2-l41": {
        "data_table": table(["Method", "Feature"], [
            ["Heuristic evaluation", "Experts review an interface against established usability principles"],
        ]),
    },
    "ui/ux-design-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Cognitive walkthrough", "Evaluates whether a new user could complete a task through exploration alone"],
        ]),
    },
    "ui/ux-design-c2-l43": {
        "data_table": table(["Type", "Feature"], [
            ["Multivariate testing", "Tests multiple variables simultaneously to find the best combination"],
        ]),
    },
    "ui/ux-design-c2-l44": {
        "data_table": table(["Practice", "Purpose"], [
            ["Ethical design audit", "Identifies manipulative or exploitative design patterns"],
        ]),
    },
    "ui/ux-design-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Micro-animation", "A small, purposeful animation providing feedback or guiding attention"],
        ]),
    },
    "ui/ux-design-c2-l46": {
        "data_table": table(["Property", "Effect"], [
            ["Easing curve", "Controls the acceleration and deceleration of an animation"],
        ]),
    },
    "ui/ux-design-c2-l47": {
        "data_table": table(["Approach", "Feature"], [
            ["Fluid design", "Scales smoothly across any screen size rather than snapping between fixed breakpoints"],
        ]),
    },
    "ui/ux-design-c2-l48": {
        "data_table": table(["Consideration", "Detail"], [
            ["Foldable devices", "Require designs that adapt to changing screen dimensions and hinge states"],
        ]),
    },
    "ui/ux-design-c2-l49": {
        "data_table": table(["Platform", "Convention"], [
            ["iOS", "Follows Apple's Human Interface Guidelines"], ["Android", "Follows Google's Material Design guidelines"],
        ]),
    },
    "ui/ux-design-c2-l50": {
        "data_table": table(["Constraint", "Detail"], [
            ["Small screen size", "Requires extreme content prioritization on wearable devices"],
        ]),
    },
    "ui/ux-design-c2-l51": {
        "data_table": table(["Step", "Purpose"], [
            ["Synthesizing interview transcripts", "Identifies recurring patterns and pain points across users"],
        ]),
    },
    "ui/ux-design-c2-l52": {
        "data_table": table(["Method", "Purpose"], [
            ["Affinity mapping", "Groups qualitative research findings into meaningful themes"],
        ]),
    },
    "ui/ux-design-c2-l53": {
        "data_table": table(["Element", "Purpose"], [
            ["Likert scale", "Measures attitude intensity in a structured survey question"],
        ]),
    },
    "ui/ux-design-c2-l54": {
        "data_table": table(["Method", "Feature"], [
            ["Longitudinal study", "Tracks user behavior and attitudes over an extended period"],
        ]),
    },
    "ui/ux-design-c2-l55": {
        "data_table": table(["Element", "Purpose"], [
            ["Problem statement", "Frames the case study around a clear design challenge"],
        ]),
    },
    "ui/ux-design-c2-l56": {
        "data_table": table(["Practice", "Reason"], [
            ["Framing around business impact", "Helps stakeholders connect design decisions to outcomes they care about"],
        ]),
    },
    "ui/ux-design-c2-l57": {
        "data_table": table(["Skill", "Purpose"], [
            ["Giving constructive feedback", "Helps a design team improve without discouraging experimentation"],
        ]),
    },
    "ui/ux-design-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["DesignOps", "Optimizes people, process, and tools to help design teams scale efficiently"],
        ]),
    },
    "ui/ux-design-c2-l59": {
        "data_table": table(["Practice", "Reason"], [
            ["Structured critique format", "Keeps design feedback focused and productive"],
        ]),
    },
    "ui/ux-design-c2-l60": {
        "data_table": table(["Metric", "Link"], [
            ["Conversion rate", "Connects a redesigned flow directly to business revenue impact"],
        ]),
    },
    "ui/ux-design-c2-l61": {
        "data_table": table(["Consideration", "Detail"], [
            ["Voice UI error recovery", "Must gracefully handle misunderstood commands without visual cues"],
        ]),
    },
    "ui/ux-design-c2-l62": {
        "data_table": table(["Consideration", "Detail"], [
            ["Text expansion", "Translated text often requires more space than the source language"],
        ]),
    },
    "ui/ux-design-c2-l63": {
        "data_table": table(["Method", "Example"], [
            ["Participatory workshop", "Users help sketch solutions alongside the design team"],
        ]),
    },
    "ui/ux-design-c2-l64": {
        "data_table": table(["Pattern", "Consideration"], [
            ["Bottom navigation", "Keeps primary actions within thumb reach on mobile"],
        ]),
    },
    "ui-ux-design-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Restructuring a site's IA", "Reorganizing categories based on card sorting results"],
        ]),
    },
    "ui-ux-design-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Moving from wireframe to prototype", "Adding interactivity to a static layout for testing"],
        ]),
    },
    "ui-ux-design-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Running a card sort", "Analyzing how users naturally group a set of content items"],
        ]),
    },
    "ui-ux-design-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting tree test results", "Identifying where users got lost in a navigation hierarchy"],
        ]),
    },
    "ui-ux-design-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Building a sitemap", "Mapping out a product's full page hierarchy before design begins"],
        ]),
    },
    "ui-ux-design-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a navigation pattern", "Selecting tabs versus a hamburger menu for a given app"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["UI/UX Design"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json UI/UX Design: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 UI/UX Design lessons (completing 70/70).")


if __name__ == "__main__":
    main()
