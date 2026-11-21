#!/usr/bin/env python3
"""Depth pass, Grade 7 Critical Thinking: fill in real, hand-checked
data_table content for the 38 Grade 7 Critical Thinking lessons not
covered by the earlier breadth-first batch. Brings Grade 7 Critical
Thinking to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ct-g7-l1": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Premise", "A statement offered as support"], ["Conclusion", "The claim the premises support"],
        ]),
    },
    "critical-thinking-g7-l2": {
        "data_table": table(["Reasoning Type", "Direction"], [
            ["Deductive", "General rule to specific conclusion"], ["Inductive", "Specific observations to general conclusion"],
        ]),
    },
    "critical-thinking-g7-l3": {
        "data_table": table(["Example", "Type"], [
            ["Every crow I've seen is black, so all crows are black", "Inductive reasoning"],
        ]),
    },
    "critical-thinking-g7-l5": {
        "data_table": table(["Evidence Type", "Strength"], [
            ["Peer-reviewed study", "Strong"], ["Anonymous online claim", "Weak"],
        ]),
    },
    "critical-thinking-g7-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Correlation", "Two things happen together"], ["Causation", "One thing directly causes the other"],
        ]),
    },
    "critical-thinking-g7-l7": {
        "data_table": table(["Cause", "Effect"], [
            ["It rained heavily", "The picnic was cancelled"],
        ]),
    },
    "critical-thinking-g7-l9": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Claim", "States the position"], ["Evidence", "Supports the claim"], ["Reasoning", "Connects evidence to claim"],
        ]),
    },
    "critical-thinking-g7-l10": {
        "data_table": table(["Question Type", "Purpose"], [
            ["Socratic question", "Probes assumptions and reasoning through dialogue"],
        ]),
    },
    "critical-thinking-g7-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Assumption", "Something taken for granted without proof"],
        ]),
    },
    "critical-thinking-g7-l12": {
        "data_table": table(["Sign of a Reliable Source", "Example"], [
            ["Named, credible author", "An expert with verifiable credentials"],
        ]),
    },
    "critical-thinking-g7-l13": {
        "data_table": table(["Bias", "Example"], [
            ["Confirmation bias", "Favoring information that confirms existing beliefs"],
        ]),
    },
    "critical-thinking-g7-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"],
        ]),
    },
    "critical-thinking-g7-l15": {
        "data_table": table(["Misleading Technique", "Example"], [
            ["Cherry-picking data", "Showing only favorable statistics"],
        ]),
    },
    "critical-thinking-g7-l16": {
        "data_table": table(["Skill", "Purpose"], [
            ["Verifying sources", "Confirms information is accurate"],
        ]),
    },
    "critical-thinking-g7-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Counterargument", "Addresses the opposing viewpoint"],
        ]),
    },
    "critical-thinking-g7-l18": {
        "data_table": table(["Element", "Purpose"], [
            ["Rebuttal", "Responds to and refutes a counterargument"],
        ]),
    },
    "critical-thinking-g7-l19": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "critical-thinking-g7-l20": {
        "data_table": table(["Rhetorical Appeal", "Meaning"], [
            ["Ethos", "Appeals to credibility"], ["Pathos", "Appeals to emotion"], ["Logos", "Appeals to logic"],
        ]),
    },
    "critical-thinking-g7-l21": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the problem", "Clarifies what needs solving"], ["Generate solutions", "Lists possible approaches"],
        ]),
    },
    "critical-thinking-g7-l22": {
        "data_table": table(["Step", "Purpose"], [
            ["List options", "Identifies choices"], ["Weigh pros and cons", "Evaluates each option"],
        ]),
    },
    "critical-thinking-g7-l23": {
        "data_table": table(["Technique", "Purpose"], [
            ["Brainstorming", "Generating many ideas quickly"],
        ]),
    },
    "critical-thinking-g7-l24": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Mind mapping", "Visually organizing related ideas"],
        ]),
    },
    "critical-thinking-g7-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Lateral thinking", "Solving problems through indirect, creative approaches"],
        ]),
    },
    "critical-thinking-g7-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Analogy", "Comparing two different things to explain an idea"],
        ]),
    },
    "critical-thinking-g7-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethical dilemma", "A situation with no clearly right answer between competing values"],
        ]),
    },
    "critical-thinking-g7-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Systems thinking", "Understanding how parts of a system interact and affect the whole"],
        ]),
    },
    "critical-thinking-g7-l29": {
        "data_table": table(["Tool", "Purpose"], [
            ["Mind map", "Visually organizes related ideas around a central topic"],
        ]),
    },
    "critical-thinking-g7-l30": {
        "data_table": table(["SWOT Element", "Meaning"], [
            ["Strengths", "Internal advantages"], ["Weaknesses", "Internal disadvantages"],
            ["Opportunities", "External positive factors"], ["Threats", "External negative factors"],
        ]),
    },
    "critical-thinking-g7-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Risk", "The chance of a negative outcome"], ["Risk assessment", "Evaluating how likely and serious a risk is"],
        ]),
    },
    "critical-thinking-g7-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Metacognition", "Thinking about one's own thinking process"],
        ]),
    },
    "critical-thinking-g7-l33": {
        "data_table": table(["Question Type", "Example"], [
            ["Open-ended", "Why do you think that happened?"], ["Closed-ended", "Did that happen?"],
        ]),
    },
    "critical-thinking-g7-l34": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Experiment", "Tests the hypothesis"],
        ]),
    },
    "critical-thinking-g7-l35": {
        "data_table": table(["Skill", "Example"], [
            ["Quantitative reasoning", "Interpreting numerical data to draw conclusions"],
        ]),
    },
    "critical-thinking-g7-l36": {
        "data_table": table(["Puzzle Type", "Skill Practiced"], [
            ["Logic grid puzzle", "Deductive reasoning"],
        ]),
    },
    "critical-thinking-g7-l37": {
        "data_table": table(["Concept", "Example"], [
            ["Probability", "The likelihood an event will occur"], ["Uncertainty", "Not knowing an outcome for sure"],
        ]),
    },
    "critical-thinking-g7-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Game theory", "The study of strategic decision-making between parties"],
        ]),
    },
    "critical-thinking-g7-l39": {
        "data_table": table(["Thought Experiment", "Purpose"], [
            ["Trolley problem", "Explores ethical decision-making under conflicting values"],
        ]),
    },
    "critical-thinking-g7-l40": {
        "data_table": table(["Everyday Decision", "Critical Thinking Applied"], [
            ["Choosing a purchase", "Comparing options and evidence before buying"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Critical Thinking lessons (completing 40/40).")


if __name__ == "__main__":
    main()
