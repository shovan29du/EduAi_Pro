#!/usr/bin/env python3
"""Depth pass, Grade 8 Philosophy: fill in real, hand-checked data_table
content for the 38 Grade 8 Philosophy lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Philosophy to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "phil-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy", "The study of fundamental questions about existence, knowledge, and ethics"],
        ]),
    },
    "philosophy-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Epistemology", "The branch of philosophy studying knowledge and belief"],
        ]),
    },
    "philosophy-g8-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Metaphysics", "The branch of philosophy studying the nature of reality"],
        ]),
    },
    "philosophy-g8-l4": {
        "data_table": table(["Ethical Framework", "Focus"], [
            ["Consequentialism", "Judges actions by their outcomes"], ["Deontology", "Judges actions by rules and duties"],
        ]),
    },
    "philosophy-g8-l5": {
        "data_table": table(["Scenario Element", "Question Raised"], [
            ["The trolley problem", "Is it right to sacrifice one to save many?"],
        ]),
    },
    "philosophy-g8-l6": {
        "data_table": table(["Theory of Justice", "Core Idea"], [
            ["Distributive justice", "Fair allocation of resources"],
        ]),
    },
    "philosophy-g8-l8": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic questioning", "Uses probing questions to examine beliefs"],
        ]),
    },
    "philosophy-g8-l9": {
        "data_table": table(["Thinker", "View on Happiness"], [
            ["Aristotle", "True happiness (eudaimonia) comes from living virtuously"],
        ]),
    },
    "philosophy-g8-l10": {
        "data_table": table(["Position", "Meaning"], [
            ["Free will", "The idea that people can choose their actions"],
            ["Determinism", "The idea that events are determined by prior causes"],
        ]),
    },
    "philosophy-g8-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Mind-body problem", "The philosophical question of how the mind relates to the physical body"],
        ]),
    },
    "philosophy-g8-l12": {
        "data_table": table(["Question", "Focus"], [
            ["Personal identity", "What makes a person the same over time"],
        ]),
    },
    "philosophy-g8-l13": {
        "data_table": table(["Thought Experiment", "Question Raised"], [
            ["Ship of Theseus", "If all parts are replaced, is it still the same object?"],
        ]),
    },
    "philosophy-g8-l15": {
        "data_table": table(["Ethical Framework", "Focus"], [
            ["Deontology", "Judges actions by rules and duties, not outcomes"],
        ]),
    },
    "philosophy-g8-l16": {
        "data_table": table(["Ethical Framework", "Focus"], [
            ["Virtue ethics", "Focuses on developing good character traits"],
        ]),
    },
    "philosophy-g8-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Argument", "A set of premises offered in support of a conclusion"],
        ]),
    },
    "philosophy-g8-l18": {
        "data_table": table(["Theory of Truth", "Core Idea"], [
            ["Correspondence theory", "A statement is true if it matches reality"],
        ]),
    },
    "philosophy-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Skepticism", "The philosophical position of doubting claims to knowledge"],
        ]),
    },
    "philosophy-g8-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Problem of evil", "The philosophical question of why evil exists if God is good and all-powerful"],
        ]),
    },
    "philosophy-g8-l21": {
        "data_table": table(["Thinker", "Idea"], [
            ["Jean-Paul Sartre", "Existence precedes essence"],
        ]),
    },
    "philosophy-g8-l22": {
        "data_table": table(["Concept", "Meaning"], [
            ["Stoicism", "Focus on controlling your responses, not external events"],
        ]),
    },
    "philosophy-g8-l23": {
        "data_table": table(["Thinker", "Core Idea"], [
            ["Confucius", "Emphasized moral virtue, social harmony, and proper relationships"],
        ]),
    },
    "philosophy-g8-l24": {
        "data_table": table(["Noble Truth", "Meaning"], [
            ["1st", "Suffering exists"], ["2nd", "Suffering has a cause"],
        ]),
    },
    "philosophy-g8-l25": {
        "data_table": table(["Thinker", "Idea"], [
            ["Thomas Hobbes", "People agree to a social contract to escape a chaotic 'state of nature'"],
        ]),
    },
    "philosophy-g8-l26": {
        "data_table": table(["Question", "Focus"], [
            ["Animal rights", "Whether and how animals deserve moral consideration"],
        ]),
    },
    "philosophy-g8-l27": {
        "data_table": table(["Question", "Focus"], [
            ["Environmental ethics", "Moral obligations toward the natural environment"],
        ]),
    },
    "philosophy-g8-l28": {
        "data_table": table(["Question", "Focus"], [
            ["Ethics of lying", "Whether lying can ever be morally justified"],
        ]),
    },
    "philosophy-g8-l29": {
        "data_table": table(["Thought Experiment", "Question Raised"], [
            ["Trolley problem", "Weighing harm against inaction"],
        ]),
    },
    "philosophy-g8-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Aesthetics", "The branch of philosophy studying beauty and art"],
        ]),
    },
    "philosophy-g8-l31": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of friendship", "What makes a relationship a true friendship"],
        ]),
    },
    "philosophy-g8-l32": {
        "data_table": table(["Concept", "Meaning"], [
            ["Wisdom", "Good judgment developed through knowledge and experience"],
        ]),
    },
    "philosophy-g8-l33": {
        "data_table": table(["Position", "Meaning"], [
            ["Cultural relativism", "Moral standards vary by culture"],
            ["Moral universalism", "Some moral standards apply to everyone"],
        ]),
    },
    "philosophy-g8-l34": {
        "data_table": table(["Concept", "Example"], [
            ["Fairness in games", "Applying consistent rules to all players"],
        ]),
    },
    "philosophy-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Political philosophy", "The study of government, justice, and rights"],
        ]),
    },
    "philosophy-g8-l36": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of science", "What makes something a valid scientific claim"],
        ]),
    },
    "philosophy-g8-l37": {
        "data_table": table(["Concept", "Origin"], [
            ["The examined life", "Attributed to Socrates: 'The unexamined life is not worth living'"],
        ]),
    },
    "philosophy-g8-l38": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of technology", "Ethical implications of new technologies"],
        ]),
    },
    "philosophy-g8-l39": {
        "data_table": table(["Tradition", "Focus"], [
            ["Western philosophy", "Often emphasizes logic and individual reasoning"],
            ["Eastern philosophy", "Often emphasizes harmony and community"],
        ]),
    },
    "philosophy-g8-l40": {
        "data_table": table(["Argument Part", "Purpose"], [
            ["Premise", "A statement offered as support"], ["Conclusion", "The claim the premises support"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Philosophy: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Philosophy lessons (completing 40/40).")


if __name__ == "__main__":
    main()
