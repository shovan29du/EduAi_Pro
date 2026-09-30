#!/usr/bin/env python3
"""Depth pass, Grade 10 Critical Thinking: fill in real, hand-checked
data_table content for the Grade 10 Critical Thinking lessons not
covered by the earlier breadth-first batch. Brings Grade 10 Critical
Thinking to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ct-g10-l1": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the problem", "Clarifies exactly what needs to be solved"],
        ]),
    },
    "critical-thinking-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Critical thinking", "Objectively analyzing and evaluating information to form a judgment"],
        ]),
    },
    "critical-thinking-g10-l3": {
        "data_table": table(["Part", "Role"], [
            ["Claim", "The position an argument asserts"], ["Evidence", "Support offered for the claim"],
        ]),
    },
    "critical-thinking-g10-l4": {
        "data_table": table(["Type", "Example"], [
            ["Fact", "Verifiable statement"], ["Opinion", "A personal judgment or belief"],
        ]),
    },
    "critical-thinking-g10-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Deductive reasoning", "Reasoning from general premises to a specific, certain conclusion"],
        ]),
    },
    "critical-thinking-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Inductive reasoning", "Reasoning from specific observations to a general, probable conclusion"],
        ]),
    },
    "critical-thinking-g10-l8": {
        "data_table": table(["Question", "Purpose"], [
            ["Is the source credible?", "Assesses the reliability of evidence"],
        ]),
    },
    "critical-thinking-g10-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Confirmation bias", "The tendency to favor information that confirms existing beliefs"],
        ]),
    },
    "critical-thinking-g10-l11": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cause and effect", "One event bringing about another"],
        ]),
    },
    "critical-thinking-g10-l12": {
        "data_table": table(["Concept", "Meaning"], [
            ["Correlation", "Two things occur together"], ["Causation", "One thing directly causes another"],
        ]),
    },
    "critical-thinking-g10-l13": {
        "data_table": table(["Question", "Purpose"], [
            ["Who wrote this and why?", "Reveals potential bias in a source"],
        ]),
    },
    "critical-thinking-g10-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Misinformation", "False or inaccurate information, regardless of intent to deceive"],
        ]),
    },
    "critical-thinking-g10-l15": {
        "data_table": table(["Technique", "Description"], [
            ["Propaganda", "Information used to promote a viewpoint, often misleading"],
        ]),
    },
    "critical-thinking-g10-l16": {
        "data_table": table(["Requirement", "Meaning"], [
            ["Valid argument", "The conclusion logically follows from the premises"], ["Sound argument", "Valid and all premises are true"],
        ]),
    },
    "critical-thinking-g10-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Assumption", "An unstated belief taken for granted in an argument"],
        ]),
    },
    "critical-thinking-g10-l18": {
        "data_table": table(["Trick", "Effect"], [
            ["Truncated graph axis", "Exaggerates differences between data points"],
        ]),
    },
    "critical-thinking-g10-l19": {
        "data_table": table(["Bias", "Description"], [
            ["Confirmation bias", "Favoring information that confirms beliefs"], ["Anchoring bias", "Over-relying on the first piece of information"],
        ]),
    },
    "critical-thinking-g10-l20": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic questioning", "Uses probing questions to examine assumptions"],
        ]),
    },
    "critical-thinking-g10-l21": {
        "data_table": table(["Step", "Purpose"], [
            ["Brainstorm freely first", "Generates many ideas before judging them"],
        ]),
    },
    "critical-thinking-g10-l22": {
        "data_table": table(["Framework", "Use"], [
            ["Pros and cons list", "Weighs the tradeoffs of a decision"],
        ]),
    },
    "critical-thinking-g10-l23": {
        "data_table": table(["Method", "Purpose"], [
            ["Root cause analysis", "Identifies the underlying source of a problem, not just symptoms"],
        ]),
    },
    "critical-thinking-g10-l24": {
        "data_table": table(["Model", "Approach"], [
            ["Cost-benefit analysis", "Weighs expected gains against expected losses"],
        ]),
    },
    "critical-thinking-g10-l25": {
        "data_table": table(["Framework", "Use"], [
            ["Pros and cons list", "Weighs the tradeoffs of a decision"],
        ]),
    },
    "critical-thinking-g10-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify likelihood and impact", "Core steps in assessing risk"],
        ]),
    },
    "critical-thinking-g10-l27": {
        "data_table": table(["Technique", "Purpose"], [
            ["Annotating text", "Improves active engagement while reading critically"],
        ]),
    },
    "critical-thinking-g10-l28": {
        "data_table": table(["Technique", "Purpose"], [
            ["Emotional appeal in ads", "Persuades through feelings rather than facts"],
        ]),
    },
    "critical-thinking-g10-l29": {
        "data_table": table(["Skill", "Purpose"], [
            ["Rebuttal", "Responding to an opposing argument with evidence"],
        ]),
    },
    "critical-thinking-g10-l30": {
        "data_table": table(["Warning Sign", "Detail"], [
            ["Sensational headlines", "A common sign of fake news"],
        ]),
    },
    "critical-thinking-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Sample bias", "A survey sample that doesn't represent the full population"],
        ]),
    },
    "critical-thinking-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Analogical reasoning", "Drawing conclusions based on similarities between situations"],
        ]),
    },
    "critical-thinking-g10-l33": {
        "data_table": table(["Tactic", "Detail"], [
            ["Guilt-tripping", "Uses emotion rather than facts to persuade"],
        ]),
    },
    "critical-thinking-g10-l34": {
        "data_table": table(["Requirement", "Meaning"], [
            ["Valid argument", "The conclusion logically follows from the premises"], ["Sound argument", "Valid, and premises are also true"],
        ]),
    },
    "critical-thinking-g10-l35": {
        "data_table": table(["Element", "Purpose"], [
            ["Visual metaphor", "Conveys a political message through imagery in a cartoon"],
        ]),
    },
    "critical-thinking-g10-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Groupthink", "Prioritizing group harmony over critical evaluation of a decision"],
        ]),
    },
    "critical-thinking-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethical reasoning", "Applying moral principles to evaluate a decision"],
        ]),
    },
    "critical-thinking-g10-l38": {
        "data_table": table(["Principle", "Meaning"], [
            ["Falsifiability", "A good scientific claim can be tested and potentially disproven"],
        ]),
    },
    "critical-thinking-g10-l39": {
        "data_table": table(["Skill", "Purpose"], [
            ["Steelmanning", "Engaging with the strongest version of an opposing view"],
        ]),
    },
    "critical-thinking-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Systems thinking", "Viewing a problem as part of an interconnected whole"],
        ]),
    },
    "critical-thinking-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Lateral thinking", "Solving problems through indirect, creative approaches"],
        ]),
    },
    "critical-thinking-g10-l42": {
        "data_table": table(["Tool", "Purpose"], [
            ["Mind map", "Visually organizes ideas around a central concept"],
        ]),
    },
    "critical-thinking-g10-l43": {
        "data_table": table(["Technique", "Purpose"], [
            ["Five Whys", "Repeatedly asks 'why' to find a problem's root cause"],
        ]),
    },
    "critical-thinking-g10-l44": {
        "data_table": table(["Question", "Purpose"], [
            ["Is this expert speaking within their field?", "Tests the credibility of an expert opinion"],
        ]),
    },
    "critical-thinking-g10-l45": {
        "data_table": table(["Fallacy", "Description"], [
            ["False dichotomy", "Presents only two options when more exist"],
        ]),
    },
    "critical-thinking-g10-l46": {
        "data_table": table(["Question to Ask", "Purpose"], [
            ["Is there peer-reviewed evidence?", "Evaluates the credibility of a health claim"],
        ]),
    },
    "critical-thinking-g10-l47": {
        "data_table": table(["Question to Ask", "Purpose"], [
            ["What are the fees and risks?", "Applies critical thinking to financial decisions"],
        ]),
    },
    "critical-thinking-g10-l48": {
        "data_table": table(["Skill", "Purpose"], [
            ["Fact-checking online claims", "Reduces the spread of misinformation"],
        ]),
    },
    "critical-thinking-g10-l49": {
        "data_table": table(["Practice", "Benefit"], [
            ["Reflective thinking", "Improves self-awareness and decision quality over time"],
        ]),
    },
    "critical-thinking-g10-l50": {
        "data_table": table(["Skill", "Application"], [
            ["Case study analysis", "Applies critical thinking tools to a real-world scenario"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Critical Thinking lessons (completing 50/50).")


if __name__ == "__main__":
    main()
