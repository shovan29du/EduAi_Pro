#!/usr/bin/env python3
"""Depth pass, Grade 10 Philosophy: fill in real, hand-checked
data_table content for the Grade 10 Philosophy lessons not covered by
the earlier breadth-first batch. Brings Grade 10 Philosophy to full
50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "phil-g10-l1": {
        "data_table": table(["Question", "Focus"], [
            ["Free will", "Whether humans can genuinely choose their actions"],
        ]),
    },
    "philosophy-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy", "The study of fundamental questions about existence, knowledge, and values"],
        ]),
    },
    "philosophy-g10-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Argument", "A set of premises offered in support of a conclusion"],
        ]),
    },
    "philosophy-g10-l4": {
        "data_table": table(["Question", "Focus"], [
            ["Ethics", "What makes an action morally right or wrong"],
        ]),
    },
    "philosophy-g10-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Metaphysics", "The study of the fundamental nature of reality and existence"],
        ]),
    },
    "philosophy-g10-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Epistemology", "The study of knowledge, belief, and justification"],
        ]),
    },
    "philosophy-g10-l7": {
        "data_table": table(["Thinker", "Idea"], [
            ["Plato", "Theory of Forms, perfect abstract realities behind physical objects"],
        ]),
    },
    "philosophy-g10-l8": {
        "data_table": table(["Thinker", "Idea"], [
            ["Aristotle", "The golden mean, virtue lies between extremes"],
        ]),
    },
    "philosophy-g10-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Socratic method", "Teaching through asking probing questions"],
        ]),
    },
    "philosophy-g10-l11": {
        "data_table": table(["Theory", "Principle"], [
            ["Deontology", "Judges actions by whether they follow moral rules or duties"],
        ]),
    },
    "philosophy-g10-l12": {
        "data_table": table(["Theory", "Principle"], [
            ["Virtue ethics", "Focuses on character and virtue rather than rules or consequences"],
        ]),
    },
    "philosophy-g10-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Existentialism", "Philosophy emphasizing individual freedom and meaning-making"],
        ]),
    },
    "philosophy-g10-l14": {
        "data_table": table(["Question", "Focus"], [
            ["Political philosophy", "Explores justice, authority, and governance"],
        ]),
    },
    "philosophy-g10-l16": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Rawls", "Justice as fairness, the 'veil of ignorance'"],
        ]),
    },
    "philosophy-g10-l17": {
        "data_table": table(["Dilemma", "Focus"], [
            ["Trolley problem", "Tests intuitions about consequentialist versus deontological ethics"],
        ]),
    },
    "philosophy-g10-l18": {
        "data_table": table(["Thinker", "Idea"], [
            ["Aristotle", "Happiness (eudaimonia) as the highest human good"],
        ]),
    },
    "philosophy-g10-l19": {
        "data_table": table(["Argument", "Summary"], [
            ["Cosmological argument", "The universe requires a first cause"],
        ]),
    },
    "philosophy-g10-l20": {
        "data_table": table(["Question", "Focus"], [
            ["Problem of evil", "How evil can exist if God is all-good and all-powerful"],
        ]),
    },
    "philosophy-g10-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Confucianism", "Chinese philosophy emphasizing ethics and social harmony"],
        ]),
    },
    "philosophy-g10-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Buddhism", "Founded by Siddhartha Gautama, emphasizes the end of suffering"],
        ]),
    },
    "philosophy-g10-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Stoicism", "Ancient Greek philosophy emphasizing virtue and control over one's reactions"],
        ]),
    },
    "philosophy-g10-l24": {
        "data_table": table(["Theory", "Definition of Truth"], [
            ["Correspondence theory", "A statement is true if it matches reality"],
        ]),
    },
    "philosophy-g10-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Skepticism", "The philosophical position that questions whether certain knowledge is possible"],
        ]),
    },
    "philosophy-g10-l26": {
        "data_table": table(["Principle", "Meaning"], [
            ["Falsifiability", "A good scientific claim can be tested and potentially disproven"],
        ]),
    },
    "philosophy-g10-l27": {
        "data_table": table(["Position", "View"], [
            ["Determinism", "All events are caused by prior events"], ["Free will", "Humans can make genuinely free choices"],
        ]),
    },
    "philosophy-g10-l28": {
        "data_table": table(["Question", "Focus"], [
            ["Personal identity", "What makes a person the same person over time"],
        ]),
    },
    "philosophy-g10-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Ship of Theseus", "A thought experiment about identity when all parts are replaced"],
        ]),
    },
    "philosophy-g10-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Aesthetics", "The philosophical study of beauty and art"],
        ]),
    },
    "philosophy-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental ethics", "Examines humans' ethical relationship with nature"],
        ]),
    },
    "philosophy-g10-l32": {
        "data_table": table(["Question", "Focus"], [
            ["Animal rights", "Considers the moral status of animals"],
        ]),
    },
    "philosophy-g10-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of law", "Examines the nature, purpose, and legitimacy of law"],
        ]),
    },
    "philosophy-g10-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Rights", "Entitlements owed to a person"], ["Responsibilities", "Duties expected of a person"],
        ]),
    },
    "philosophy-g10-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Formal logic", "The systematic study of valid inference using symbols"],
        ]),
    },
    "philosophy-g10-l36": {
        "data_table": table(["Fallacy", "Description"], [
            ["Ad hominem", "Attacking the person instead of the argument"],
        ]),
    },
    "philosophy-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of language", "Explores how language relates to meaning and thought"],
        ]),
    },
    "philosophy-g10-l38": {
        "data_table": table(["Thinker", "Idea"], [
            ["Rene Descartes", "'Cogito ergo sum' - I think, therefore I am"],
        ]),
    },
    "philosophy-g10-l39": {
        "data_table": table(["Position", "View"], [
            ["Rationalism", "Knowledge comes primarily from reason"], ["Empiricism", "Knowledge comes primarily from experience"],
        ]),
    },
    "philosophy-g10-l40": {
        "data_table": table(["Thinker", "Idea"], [
            ["Immanuel Kant", "The categorical imperative, act only on principles you'd will universal"],
        ]),
    },
    "philosophy-g10-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Confucian ethics", "Emphasizes social harmony and proper relationships"],
        ]),
    },
    "philosophy-g10-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Allegory of the Cave", "Plato's story about perception and reality"],
        ]),
    },
    "philosophy-g10-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of technology", "Examines the impact and ethics of technology"],
        ]),
    },
    "philosophy-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Feminist philosophy", "Examines gender, power, and equality through a philosophical lens"],
        ]),
    },
    "philosophy-g10-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Human rights", "Rights considered inherent to all people"],
        ]),
    },
    "philosophy-g10-l46": {
        "data_table": table(["Question", "Focus"], [
            ["Ethics of AI", "Considers fairness, bias, and responsibility in artificial intelligence"],
        ]),
    },
    "philosophy-g10-l47": {
        "data_table": table(["Philosopher", "Contribution"], [
            ["Socrates", "The Socratic method"], ["Plato", "Theory of Forms"], ["Aristotle", "Logic and virtue ethics"],
        ]),
    },
    "philosophy-g10-l48": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
        ]),
    },
    "philosophy-g10-l49": {
        "data_table": table(["Skill", "Purpose"], [
            ["Reflective questioning", "Helps apply philosophical thinking to daily decisions"],
        ]),
    },
    "philosophy-g10-l50": {
        "data_table": table(["Part", "Purpose"], [
            ["Premise", "A statement offered as evidence"], ["Conclusion", "What the argument claims follows"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Philosophy: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Philosophy lessons (completing 50/50).")


if __name__ == "__main__":
    main()
