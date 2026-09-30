#!/usr/bin/env python3
"""Depth pass, Grade 6 Critical Thinking: fill in real, hand-checked
data_table content for the 28 Grade 6 Critical Thinking lessons not
covered by the earlier breadth-first batch. Brings Grade 6 Critical
Thinking to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ct-g6-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Critical thinking", "Analyzing information objectively before forming a judgment"],
        ]),
    },
    "critical-thinking-g6-l2": {
        "data_table": table(["Type", "Example"], [
            ["Fact", "Water boils at 100C at sea level"], ["Opinion", "Chocolate ice cream is the best flavor"],
        ]),
    },
    "critical-thinking-g6-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"],
        ]),
    },
    "critical-thinking-g6-l6": {
        "data_table": table(["Sign of a Reliable Source", "Example"], [
            ["Named, credible author", "An expert with verifiable credentials"],
            ["Cross-checked by other sources", "Multiple outlets report the same facts"],
        ]),
    },
    "critical-thinking-g6-l7": {
        "data_table": table(["Cause", "Effect"], [
            ["It rained heavily", "The picnic was cancelled"],
        ]),
    },
    "critical-thinking-g6-l8": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Claim", "States the position"], ["Evidence", "Supports the claim with facts"],
        ]),
    },
    "critical-thinking-g6-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Valid argument", "The conclusion logically follows from the premises"],
        ]),
    },
    "critical-thinking-g6-l10": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the problem", "Clarifies what needs solving"], ["Generate solutions", "Lists possible approaches"],
        ]),
    },
    "critical-thinking-g6-l11": {
        "data_table": table(["Step", "Purpose"], [
            ["List options", "Identifies choices"], ["Weigh pros and cons", "Evaluates each option"],
        ]),
    },
    "critical-thinking-g6-l12": {
        "data_table": table(["Question Type", "Example"], [
            ["Open-ended", "Why do you think that happened?"], ["Closed-ended", "Did that happen?"],
        ]),
    },
    "critical-thinking-g6-l13": {
        "data_table": table(["Skill", "Meaning"], [
            ["Comparing", "Finding similarities"], ["Contrasting", "Finding differences"],
        ]),
    },
    "critical-thinking-g6-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Assumption", "Something taken for granted without proof"],
        ]),
    },
    "critical-thinking-g6-l15": {
        "data_table": table(["Technique", "Example"], [
            ["Bandwagon", "'Everyone is doing it, so you should too'"],
            ["Fear appeal", "Using fear to persuade rather than facts"],
        ]),
    },
    "critical-thinking-g6-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Correlation", "Two things happen together"], ["Causation", "One thing directly causes the other"],
        ]),
    },
    "critical-thinking-g6-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Analogy", "Comparing two different things to explain an idea"],
        ]),
    },
    "critical-thinking-g6-l18": {
        "data_table": table(["Technique", "Purpose"], [
            ["Brainstorming", "Generating many ideas quickly"], ["Mind mapping", "Visually organizing related ideas"],
        ]),
    },
    "critical-thinking-g6-l19": {
        "data_table": table(["Sign of Credibility", "Example"], [
            ["Verifiable evidence", "Data that can be checked"], ["Expert consensus", "Agreement among specialists"],
        ]),
    },
    "critical-thinking-g6-l20": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Claim", "States the position"], ["Evidence", "Supports the claim"], ["Conclusion", "Summarizes the argument"],
        ]),
    },
    "critical-thinking-g6-l21": {
        "data_table": table(["Technique", "Example"], [
            ["Fear appeal", "Uses fear instead of facts"], ["Guilt appeal", "Uses guilt to pressure agreement"],
        ]),
    },
    "critical-thinking-g6-l22": {
        "data_table": table(["Decision", "Possible Consequence"], [
            ["Skipping homework", "Lower grades over time"], ["Saving money regularly", "Building financial security"],
        ]),
    },
    "critical-thinking-g6-l23": {
        "data_table": table(["Skill", "Meaning"], [
            ["Perspective-taking", "Considering another person's point of view"],
            ["Empathy", "Understanding another person's feelings"],
        ]),
    },
    "critical-thinking-g6-l24": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "critical-thinking-g6-l25": {
        "data_table": table(["Skill", "Example"], [
            ["Pattern recognition", "Noticing a repeating trend in data"],
        ]),
    },
    "critical-thinking-g6-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Risk", "The chance of a negative outcome"], ["Risk assessment", "Evaluating how likely and serious a risk is"],
        ]),
    },
    "critical-thinking-g6-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethical dilemma", "A situation with no clearly right answer between competing values"],
        ]),
    },
    "critical-thinking-g6-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Metacognition", "Thinking about one's own thinking process"],
        ]),
    },
    "critical-thinking-g6-l29": {
        "data_table": table(["Concept", "Example"], [
            ["Probability", "The likelihood an event will occur"], ["Uncertainty", "Not knowing an outcome for sure"],
        ]),
    },
    "critical-thinking-g6-l30": {
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
        raise SystemExit(f"Lesson ids not found in grade6.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Critical Thinking lessons (completing 30/30).")


if __name__ == "__main__":
    main()
