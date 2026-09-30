#!/usr/bin/env python3
"""Depth pass, Grade 9 Critical Thinking: fill in real, hand-checked
data_table content for the 48 Grade 9 Critical Thinking lessons not
covered by the earlier breadth-first batch. Brings Grade 9 Critical
Thinking to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ct-g9-l1": {
        "data_table": table(["Question to Ask", "Purpose"], [
            ["Who wrote this and why?", "Reveals potential bias"],
        ]),
    },
    "critical-thinking-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Critical thinking", "Objectively analyzing and evaluating information to form a judgment"],
        ]),
    },
    "critical-thinking-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Logic", "The study of valid reasoning"], ["Reasoning", "The process of drawing conclusions from evidence"],
        ]),
    },
    "critical-thinking-g9-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Deductive reasoning", "Reasoning from general premises to a specific, certain conclusion"],
        ]),
    },
    "critical-thinking-g9-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Inductive reasoning", "Reasoning from specific observations to a general, probable conclusion"],
        ]),
    },
    "critical-thinking-g9-l6": {
        "data_table": table(["Part", "Role"], [
            ["Premise", "A statement offered as evidence"], ["Conclusion", "What the argument claims follows"],
        ]),
    },
    "critical-thinking-g9-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Logical fallacy", "An error in reasoning that weakens an argument"],
        ]),
    },
    "critical-thinking-g9-l8": {
        "data_table": table(["Fallacy", "Description"], [
            ["Ad hominem", "Attacking the person rather than the argument"],
        ]),
    },
    "critical-thinking-g9-l9": {
        "data_table": table(["Fallacy", "Description"], [
            ["Strawman", "Misrepresenting an argument to make it easier to attack"],
        ]),
    },
    "critical-thinking-g9-l11": {
        "data_table": table(["Fallacy", "Description"], [
            ["Slippery slope", "Claiming one step will inevitably lead to extreme consequences"],
        ]),
    },
    "critical-thinking-g9-l12": {
        "data_table": table(["Fallacy", "Description"], [
            ["Appeal to authority", "Assuming a claim is true because an authority figure said so"],
        ]),
    },
    "critical-thinking-g9-l13": {
        "data_table": table(["Fallacy", "Description"], [
            ["Circular reasoning", "The conclusion is used as its own premise"],
        ]),
    },
    "critical-thinking-g9-l14": {
        "data_table": table(["Concept", "Meaning"], [
            ["Correlation", "Two things occur together"], ["Causation", "One thing directly causes another"],
        ]),
    },
    "critical-thinking-g9-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Confirmation bias", "The tendency to favor information that confirms existing beliefs"],
        ]),
    },
    "critical-thinking-g9-l16": {
        "data_table": table(["Bias", "Description"], [
            ["Confirmation bias", "Favoring information that confirms beliefs"], ["Anchoring bias", "Over-relying on the first piece of information"],
        ]),
    },
    "critical-thinking-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Anchoring bias", "Relying too heavily on the first piece of information encountered"],
        ]),
    },
    "critical-thinking-g9-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Groupthink", "Prioritizing group harmony over critical evaluation of a decision"],
        ]),
    },
    "critical-thinking-g9-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify the conclusion", "Understand what the argument is claiming"],
        ]),
    },
    "critical-thinking-g9-l21": {
        "data_table": table(["Requirement", "Meaning"], [
            ["Valid argument", "The conclusion logically follows from the premises"], ["Sound argument", "Valid and all premises are true"],
        ]),
    },
    "critical-thinking-g9-l22": {
        "data_table": table(["Question", "Purpose"], [
            ["Is the source credible?", "Assesses the reliability of evidence"],
        ]),
    },
    "critical-thinking-g9-l23": {
        "data_table": table(["Type", "Example"], [
            ["Fact", "Verifiable statement"], ["Opinion", "A personal judgment or belief"],
        ]),
    },
    "critical-thinking-g9-l24": {
        "data_table": table(["Technique", "Description"], [
            ["Propaganda", "Information used to promote a particular viewpoint, often misleading"],
        ]),
    },
    "critical-thinking-g9-l25": {
        "data_table": table(["Technique", "Purpose"], [
            ["Emotional appeal in ads", "Persuades through feelings rather than facts"],
        ]),
    },
    "critical-thinking-g9-l26": {
        "data_table": table(["Trick", "Effect"], [
            ["Truncated graph axis", "Exaggerates differences between data points"],
        ]),
    },
    "critical-thinking-g9-l27": {
        "data_table": table(["Question to Ask", "Purpose"], [
            ["What do the axes represent?", "Prevents misreading a graph's scale"],
        ]),
    },
    "critical-thinking-g9-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Sample size", "The number of respondents in a survey, affects reliability"],
        ]),
    },
    "critical-thinking-g9-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Probability", "The likelihood of an event, from 0 to 1"],
        ]),
    },
    "critical-thinking-g9-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the problem", "Clarifies exactly what needs to be solved"],
        ]),
    },
    "critical-thinking-g9-l31": {
        "data_table": table(["Framework", "Use"], [
            ["Pros and cons list", "Weighs the tradeoffs of a decision"],
        ]),
    },
    "critical-thinking-g9-l32": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic questioning", "Uses probing questions to examine assumptions"],
        ]),
    },
    "critical-thinking-g9-l33": {
        "data_table": table(["Skill", "Purpose"], [
            ["Rebuttal", "Responding to an opposing argument with evidence"],
        ]),
    },
    "critical-thinking-g9-l34": {
        "data_table": table(["Step", "Purpose"], [
            ["Anticipate objections", "Strengthens your own argument"],
        ]),
    },
    "critical-thinking-g9-l35": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cause and effect", "One event bringing about another"],
        ]),
    },
    "critical-thinking-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Systems thinking", "Viewing a problem as part of an interconnected whole"],
        ]),
    },
    "critical-thinking-g9-l37": {
        "data_table": table(["Type", "Focus"], [
            ["Creative thinking", "Generating new ideas"], ["Critical thinking", "Evaluating ideas rigorously"],
        ]),
    },
    "critical-thinking-g9-l38": {
        "data_table": table(["Step", "Purpose"], [
            ["Brainstorm freely first", "Generates many ideas before judging them"],
        ]),
    },
    "critical-thinking-g9-l39": {
        "data_table": table(["Skill", "Purpose"], [
            ["Media literacy", "Evaluating the credibility and intent of media messages"],
        ]),
    },
    "critical-thinking-g9-l40": {
        "data_table": table(["Question to Ask", "Purpose"], [
            ["Is this source verified?", "Checks credibility of online information"],
        ]),
    },
    "critical-thinking-g9-l41": {
        "data_table": table(["Warning Sign", "Detail"], [
            ["Sensational headlines", "A common sign of fake news"],
        ]),
    },
    "critical-thinking-g9-l42": {
        "data_table": table(["Practice", "Purpose"], [
            ["Read beyond the headline", "Avoids being misled by clickbait"],
        ]),
    },
    "critical-thinking-g9-l43": {
        "data_table": table(["Principle", "Meaning"], [
            ["Falsifiability", "A good scientific claim can be tested and potentially disproven"],
        ]),
    },
    "critical-thinking-g9-l44": {
        "data_table": table(["Step", "Purpose"], [
            ["Form a hypothesis", "Makes a testable prediction"],
        ]),
    },
    "critical-thinking-g9-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Analogical reasoning", "Drawing conclusions based on similarities between situations"],
        ]),
    },
    "critical-thinking-g9-l46": {
        "data_table": table(["Tactic", "Detail"], [
            ["Guilt-tripping", "Uses emotion rather than facts to persuade"],
        ]),
    },
    "critical-thinking-g9-l47": {
        "data_table": table(["Skill", "Purpose"], [
            ["Active listening", "Fully understanding a speaker's message before responding"],
        ]),
    },
    "critical-thinking-g9-l48": {
        "data_table": table(["Process", "Purpose"], [
            ["Peer review", "Experts evaluate research before publication"],
        ]),
    },
    "critical-thinking-g9-l49": {
        "data_table": table(["Step", "Purpose"], [
            ["Weigh evidence from multiple sources", "Builds a well-supported opinion"],
        ]),
    },
    "critical-thinking-g9-l50": {
        "data_table": table(["Practice", "Benefit"], [
            ["Reflective thinking", "Improves self-awareness and decision quality over time"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Critical Thinking lessons (completing 50/50).")


if __name__ == "__main__":
    main()
