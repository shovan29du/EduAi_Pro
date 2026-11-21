#!/usr/bin/env python3
"""Depth pass, Grade 8 Critical Thinking: fill in real, hand-checked
data_table content for the 38 Grade 8 Critical Thinking lessons not
covered by the earlier breadth-first batch. Brings Grade 8 Critical
Thinking to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "critical-thinking-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Critical thinking", "Analyzing information objectively before forming a judgment"],
        ]),
    },
    "critical-thinking-g8-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Assumption", "Something taken for granted without proof"],
        ]),
    },
    "critical-thinking-g8-l4": {
        "data_table": table(["Type", "Example"], [
            ["Fact", "Water boils at 100C at sea level"], ["Opinion", "Chocolate ice cream is the best flavor"],
        ]),
    },
    "critical-thinking-g8-l5": {
        "data_table": table(["Sign of a Reliable Source", "Example"], [
            ["Named, credible author", "An expert with verifiable credentials"],
        ]),
    },
    "critical-thinking-g8-l6": {
        "data_table": table(["Reasoning Type", "Direction"], [
            ["Deductive", "General rule to specific conclusion"],
        ]),
    },
    "critical-thinking-g8-l7": {
        "data_table": table(["Reasoning Type", "Direction"], [
            ["Inductive", "Specific observations to general conclusion"],
        ]),
    },
    "critical-thinking-g8-l8": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Premise", "A statement offered as support"], ["Conclusion", "The claim the premises support"],
        ]),
    },
    "critical-thinking-g8-l9": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Premise", "Supports the conclusion"], ["Conclusion", "The claim being argued for"],
        ]),
    },
    "critical-thinking-g8-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Correlation", "Two things happen together"], ["Causation", "One thing directly causes the other"],
        ]),
    },
    "critical-thinking-g8-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "A leaning toward a particular viewpoint"],
        ]),
    },
    "critical-thinking-g8-l13": {
        "data_table": table(["Misleading Technique", "Example"], [
            ["Cherry-picking data", "Showing only favorable statistics"],
        ]),
    },
    "critical-thinking-g8-l14": {
        "data_table": table(["Misleading Technique", "Example"], [
            ["Truncated axis", "Making differences look bigger than they are"],
        ]),
    },
    "critical-thinking-g8-l15": {
        "data_table": table(["Technique", "Example"], [
            ["Emotional appeal", "Using feelings instead of facts to sell"],
        ]),
    },
    "critical-thinking-g8-l16": {
        "data_table": table(["Technique", "Example"], [
            ["Bandwagon", "'Everyone is doing it, so you should too'"],
        ]),
    },
    "critical-thinking-g8-l17": {
        "data_table": table(["Fallacy", "Example"], [
            ["Appeal to authority", "'It's true because a famous person said so'"],
        ]),
    },
    "critical-thinking-g8-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Evidence", "Facts that support a claim"], ["Anecdote", "A single personal story, not proof"],
        ]),
    },
    "critical-thinking-g8-l19": {
        "data_table": table(["Technique", "Example"], [
            ["Fear appeal", "Uses fear instead of facts"],
        ]),
    },
    "critical-thinking-g8-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Steelmanning", "Presenting the strongest version of an opposing argument"],
            ["Strawmanning", "Misrepresenting an argument to make it easier to attack"],
        ]),
    },
    "critical-thinking-g8-l21": {
        "data_table": table(["Question Type", "Example"], [
            ["Open-ended", "Why do you think that happened?"],
        ]),
    },
    "critical-thinking-g8-l22": {
        "data_table": table(["Step", "Purpose"], [
            ["Define the problem", "Clarifies what needs solving"],
        ]),
    },
    "critical-thinking-g8-l23": {
        "data_table": table(["Concept", "Example"], [
            ["Uncertainty", "Not knowing an outcome for sure"],
        ]),
    },
    "critical-thinking-g8-l24": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cost-benefit analysis", "Weighing the pros and cons of a decision"],
        ]),
    },
    "critical-thinking-g8-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Groupthink", "When a group prioritizes agreement over critical evaluation"],
        ]),
    },
    "critical-thinking-g8-l26": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic method", "Uses probing questions to examine beliefs"],
        ]),
    },
    "critical-thinking-g8-l27": {
        "data_table": table(["Skill", "Purpose"], [
            ["Verifying sources", "Confirms information is accurate"],
        ]),
    },
    "critical-thinking-g8-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Sample size", "The number of observations in a study"],
        ]),
    },
    "critical-thinking-g8-l29": {
        "data_table": table(["Fallacy", "Example"], [
            ["False dilemma", "Presenting only two options when more exist"],
        ]),
    },
    "critical-thinking-g8-l30": {
        "data_table": table(["Fallacy", "Example"], [
            ["Slippery slope", "Claiming one small step leads to extreme consequences"],
        ]),
    },
    "critical-thinking-g8-l31": {
        "data_table": table(["Fallacy", "Example"], [
            ["Circular reasoning", "The conclusion restates the premise"],
        ]),
    },
    "critical-thinking-g8-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Causal claim", "A statement that one thing causes another"],
        ]),
    },
    "critical-thinking-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Analogy", "Comparing two different things to explain an idea"],
        ]),
    },
    "critical-thinking-g8-l34": {
        "data_table": table(["Term", "Example"], [
            ["Loaded language", "Words chosen to provoke an emotional reaction"],
        ]),
    },
    "critical-thinking-g8-l35": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Checking multiple sources", "Confirms information is accurate"],
        ]),
    },
    "critical-thinking-g8-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Metacognition", "Thinking about one's own thinking process"],
        ]),
    },
    "critical-thinking-g8-l37": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "critical-thinking-g8-l38": {
        "data_table": table(["Tactic", "Example"], [
            ["Guilt-tripping", "Using guilt to pressure agreement"],
        ]),
    },
    "critical-thinking-g8-l39": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Peer review", "Expert evaluation before publication"],
        ]),
    },
    "critical-thinking-g8-l40": {
        "data_table": table(["Habit", "Benefit"], [
            ["Reflective journaling", "Builds self-awareness over time"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Critical Thinking lessons (completing 40/40).")


if __name__ == "__main__":
    main()
