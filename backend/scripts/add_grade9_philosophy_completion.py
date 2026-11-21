#!/usr/bin/env python3
"""Depth pass, Grade 9 Philosophy: fill in real, hand-checked data_table
content for the 48 Grade 9 Philosophy lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Philosophy to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "phil-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethics", "The branch of philosophy concerned with right and wrong"],
        ]),
    },
    "philosophy-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy", "The study of fundamental questions about existence, knowledge, and values"],
        ]),
    },
    "philosophy-g9-l3": {
        "data_table": table(["Branch", "Focus"], [
            ["Metaphysics", "Nature of reality"], ["Epistemology", "Nature of knowledge"], ["Ethics", "Right and wrong"],
        ]),
    },
    "philosophy-g9-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Logic", "The study of valid reasoning"],
        ]),
    },
    "philosophy-g9-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Metaphysics", "The study of the fundamental nature of reality and existence"],
        ]),
    },
    "philosophy-g9-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Epistemology", "The study of knowledge, belief, and justification"],
        ]),
    },
    "philosophy-g9-l7": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of mind", "Explores the nature of consciousness and mental states"],
        ]),
    },
    "philosophy-g9-l8": {
        "data_table": table(["Theory", "Definition of Truth"], [
            ["Correspondence theory", "A statement is true if it matches reality"],
        ]),
    },
    "philosophy-g9-l9": {
        "data_table": table(["Question", "Focus"], [
            ["Free will", "Whether humans can genuinely choose their actions"],
        ]),
    },
    "philosophy-g9-l10": {
        "data_table": table(["Position", "View"], [
            ["Determinism", "All events are caused by prior events"], ["Free will", "Humans can make genuinely free choices"],
        ]),
    },
    "philosophy-g9-l11": {
        "data_table": table(["Question", "Focus"], [
            ["Personal identity", "What makes a person the same person over time"],
        ]),
    },
    "philosophy-g9-l12": {
        "data_table": table(["Question", "Focus"], [
            ["Mind-body problem", "How the mind relates to the physical body"],
        ]),
    },
    "philosophy-g9-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Socratic method", "Teaching through asking probing questions"],
        ]),
    },
    "philosophy-g9-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Confucius", "Chinese philosopher who emphasized ethics and social harmony"],
        ]),
    },
    "philosophy-g9-l17": {
        "data_table": table(["Tradition", "Region"], [
            ["Confucianism", "China"], ["Buddhism", "South Asia"],
        ]),
    },
    "philosophy-g9-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Stoicism", "Ancient Greek philosophy emphasizing virtue and control over one's reactions"],
        ]),
    },
    "philosophy-g9-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Existentialism", "Philosophy emphasizing individual freedom and meaning-making"],
        ]),
    },
    "philosophy-g9-l20": {
        "data_table": table(["Theory", "Principle"], [
            ["Utilitarianism", "The greatest good for the greatest number"],
        ]),
    },
    "philosophy-g9-l21": {
        "data_table": table(["Theory", "Principle"], [
            ["Deontology", "Judges actions by whether they follow moral rules or duties"],
        ]),
    },
    "philosophy-g9-l22": {
        "data_table": table(["Theory", "Focus"], [
            ["Consequentialism", "Judges actions by their outcomes"],
        ]),
    },
    "philosophy-g9-l23": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Government exists by consent of the governed"],
        ]),
    },
    "philosophy-g9-l24": {
        "data_table": table(["Question", "Focus"], [
            ["Political philosophy", "Explores justice, authority, and governance"],
        ]),
    },
    "philosophy-g9-l25": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Rawls", "Justice as fairness, the 'veil of ignorance'"],
        ]),
    },
    "philosophy-g9-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Human rights", "Rights considered inherent to all people"],
        ]),
    },
    "philosophy-g9-l27": {
        "data_table": table(["Thinker", "Idea"], [
            ["Aristotle", "Happiness (eudaimonia) as the highest human good"],
        ]),
    },
    "philosophy-g9-l28": {
        "data_table": table(["Dilemma", "Focus"], [
            ["Trolley problem", "Tests intuitions about consequentialist versus deontological ethics"],
        ]),
    },
    "philosophy-g9-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Aesthetics", "The philosophical study of beauty and art"],
        ]),
    },
    "philosophy-g9-l30": {
        "data_table": table(["Question", "Focus"], [
            ["What is beauty?", "Debated across aesthetics as objective or subjective"],
        ]),
    },
    "philosophy-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of science", "Examines the foundations and methods of scientific inquiry"],
        ]),
    },
    "philosophy-g9-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of religion", "Examines questions about the existence and nature of God"],
        ]),
    },
    "philosophy-g9-l33": {
        "data_table": table(["Argument", "Summary"], [
            ["Cosmological argument", "The universe requires a first cause"],
        ]),
    },
    "philosophy-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of language", "Explores how language relates to meaning and thought"],
        ]),
    },
    "philosophy-g9-l35": {
        "data_table": table(["Skill", "Purpose"], [
            ["Critical reasoning", "Evaluating arguments for validity and soundness"],
        ]),
    },
    "philosophy-g9-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Allegory of the Cave", "Plato's story about perception and reality"],
        ]),
    },
    "philosophy-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of education", "Examines the purposes and methods of teaching and learning"],
        ]),
    },
    "philosophy-g9-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental philosophy", "Examines humans' ethical relationship with nature"],
        ]),
    },
    "philosophy-g9-l39": {
        "data_table": table(["Question", "Focus"], [
            ["Animal ethics", "Considers the moral status of animals"],
        ]),
    },
    "philosophy-g9-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of technology", "Examines the impact and ethics of technology"],
        ]),
    },
    "philosophy-g9-l41": {
        "data_table": table(["Question", "Focus"], [
            ["Ethics of AI", "Considers fairness, bias, and responsibility in artificial intelligence"],
        ]),
    },
    "philosophy-g9-l42": {
        "data_table": table(["Question", "Focus"], [
            ["Personal identity over time", "Asks what makes someone the same person across their life"],
        ]),
    },
    "philosophy-g9-l43": {
        "data_table": table(["Question", "Focus"], [
            ["Consciousness", "Considers what it means to be subjectively aware"],
        ]),
    },
    "philosophy-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Skepticism", "The philosophical position that questions whether certain knowledge is possible"],
        ]),
    },
    "philosophy-g9-l45": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of time", "Explores whether time is real, and how past/present/future relate"],
        ]),
    },
    "philosophy-g9-l46": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of death", "Considers the meaning and significance of mortality"],
        ]),
    },
    "philosophy-g9-l47": {
        "data_table": table(["Fallacy", "Description"], [
            ["Ad hominem", "Attacking the person instead of the argument"],
        ]),
    },
    "philosophy-g9-l48": {
        "data_table": table(["Position", "View"], [
            ["Rationalism", "Knowledge comes primarily from reason"], ["Empiricism", "Knowledge comes primarily from experience"],
        ]),
    },
    "philosophy-g9-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Wisdom", "The capacity to apply knowledge and experience well in judgment"],
        ]),
    },
    "philosophy-g9-l50": {
        "data_table": table(["Practice", "Benefit"], [
            ["Reflective questioning", "Helps apply philosophical thinking to daily decisions"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Philosophy: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Philosophy lessons (completing 50/50).")


if __name__ == "__main__":
    main()
