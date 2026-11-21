#!/usr/bin/env python3
"""Depth pass, C1 Philosophy: fill in real, hand-checked data_table
content for the 69 C1 Philosophy lessons not covered by the earlier
breadth-first batch. Brings C1 Philosophy to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "philosophy-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy", "The study of fundamental questions about existence, knowledge, and values"],
        ]),
    },
    "philosophy-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Argument", "A set of premises offered in support of a conclusion"],
        ]),
    },
    "philosophy-c1-l4": {
        "data_table": table(["Term", "Example"], [
            ["Categorical syllogism", "All men are mortal; Socrates is a man; therefore Socrates is mortal"],
        ]),
    },
    "philosophy-c1-l5": {
        "data_table": table(["Type", "Meaning"], [
            ["Formal fallacy", "An error in the logical structure of an argument"], ["Informal fallacy", "An error in the content or context of an argument"],
        ]),
    },
    "philosophy-c1-l6": {
        "data_table": table(["Condition", "Meaning"], [
            ["Necessary condition", "Must be true for something to occur"], ["Sufficient condition", "Guarantees something will occur"],
        ]),
    },
    "philosophy-c1-l7": {
        "data_table": table(["Philosopher", "Idea"], [
            ["Thales", "Water is the fundamental substance"], ["Heraclitus", "Everything is in flux"],
        ]),
    },
    "philosophy-c1-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Socrates", "Believed 'the unexamined life is not worth living'"],
        ]),
    },
    "philosophy-c1-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Allegory of the Cave", "Plato's story about perception, illusion, and reality"],
        ]),
    },
    "philosophy-c1-l10": {
        "data_table": table(["Thinker", "Idea"], [
            ["Aristotle", "Virtue lies at the golden mean between excess and deficiency"],
        ]),
    },
    "philosophy-c1-l11": {
        "data_table": table(["Theory", "Definition of Truth"], [
            ["Correspondence theory", "A statement is true if it matches reality"], ["Coherence theory", "A statement is true if it fits within a consistent system of beliefs"],
        ]),
    },
    "philosophy-c1-l12": {
        "data_table": table(["Question", "Focus"], [
            ["Problem of illusion", "How can we trust our senses if they can deceive us?"],
        ]),
    },
    "philosophy-c1-l13": {
        "data_table": table(["Question", "Focus"], [
            ["Mind-body problem", "How the mind relates to the physical body"],
        ]),
    },
    "philosophy-c1-l14": {
        "data_table": table(["Question", "Focus"], [
            ["Animal minds", "Whether non-human animals have conscious experience"],
        ]),
    },
    "philosophy-c1-l15": {
        "data_table": table(["Question", "Focus"], [
            ["Problem of evil", "How evil can exist if God is all-good and all-powerful"],
        ]),
    },
    "philosophy-c1-l16": {
        "data_table": table(["Argument", "Summary"], [
            ["Cosmological argument", "The universe requires a first cause"], ["Teleological argument", "Order in nature implies a designer"],
        ]),
    },
    "philosophy-c1-l17": {
        "data_table": table(["Theory", "Principle"], [
            ["Consequentialism", "Judges actions by their outcomes"], ["Deontology", "Judges actions by rules or duties"],
        ]),
    },
    "philosophy-c1-l18": {
        "data_table": table(["Position", "View"], [
            ["Cultural relativism", "Moral truths vary by culture"], ["Moral objectivism", "Some moral truths hold universally"],
        ]),
    },
    "philosophy-c1-l19": {
        "data_table": table(["Question", "Focus"], [
            ["Aesthetic experience", "Whether beauty is objective or in the eye of the beholder"],
        ]),
    },
    "philosophy-c1-l20": {
        "data_table": table(["Skill", "Purpose"], [
            ["Charitable reading", "Interpreting a philosophical text in its strongest form before critiquing it"],
        ]),
    },
    "philosophy-c1-l21": {
        "data_table": table(["Branch", "Focus"], [
            ["Metaphysics", "Nature of reality"], ["Epistemology", "Nature of knowledge"], ["Ethics", "Right and wrong"],
        ]),
    },
    "philosophy-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Epistemology", "The study of knowledge, belief, and justification"],
        ]),
    },
    "philosophy-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Metaphysics", "The study of the fundamental nature of reality and existence"],
        ]),
    },
    "philosophy-c1-l24": {
        "data_table": table(["Theory", "Focus"], [
            ["Utilitarianism", "The greatest good for the greatest number"], ["Virtue ethics", "Focuses on character rather than rules or consequences"],
        ]),
    },
    "philosophy-c1-l25": {
        "data_table": table(["Question", "Focus"], [
            ["Political philosophy", "Explores justice, authority, and governance"],
        ]),
    },
    "philosophy-c1-l26": {
        "data_table": table(["Question", "Focus"], [
            ["Philosophy of mind", "Explores the nature of consciousness and mental states"],
        ]),
    },
    "philosophy-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of language", "Explores how language relates to meaning and thought"],
        ]),
    },
    "philosophy-c1-l28": {
        "data_table": table(["Principle", "Meaning"], [
            ["Falsifiability", "A good scientific claim can be tested and potentially disproven"],
        ]),
    },
    "philosophy-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Aesthetics", "The philosophical study of beauty and art"],
        ]),
    },
    "philosophy-c1-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Existentialism", "Philosophy emphasizing individual freedom and meaning-making"],
        ]),
    },
    "philosophy-c1-l31": {
        "data_table": table(["Theory", "Principle"], [
            ["Utilitarianism", "The greatest good for the greatest number"],
        ]),
    },
    "philosophy-c1-l32": {
        "data_table": table(["Thinker", "Idea"], [
            ["Immanuel Kant", "The categorical imperative, act only on principles you'd will universal"],
        ]),
    },
    "philosophy-c1-l33": {
        "data_table": table(["Theory", "Principle"], [
            ["Virtue ethics", "Focuses on character and virtue rather than rules or consequences"],
        ]),
    },
    "philosophy-c1-l34": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Government exists by consent of the governed"],
        ]),
    },
    "philosophy-c1-l35": {
        "data_table": table(["Thinker", "Idea"], [
            ["Thomas Hobbes", "Life in the state of nature is 'nasty, brutish, and short'"],
        ]),
    },
    "philosophy-c1-l36": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
        ]),
    },
    "philosophy-c1-l37": {
        "data_table": table(["Thinker", "Idea"], [
            ["Jean-Jacques Rousseau", "The general will represents the collective good of the community"],
        ]),
    },
    "philosophy-c1-l38": {
        "data_table": table(["Thinker", "Idea"], [
            ["Rene Descartes", "'Cogito ergo sum' - I think, therefore I am"],
        ]),
    },
    "philosophy-c1-l39": {
        "data_table": table(["Thinker", "Idea"], [
            ["David Hume", "Causation is inferred from habit, not directly observed"],
        ]),
    },
    "philosophy-c1-l40": {
        "data_table": table(["Thinker", "Idea"], [
            ["Immanuel Kant", "The mind actively structures our experience of reality"],
        ]),
    },
    "philosophy-c1-l41": {
        "data_table": table(["Thinker", "Idea"], [
            ["Friedrich Nietzsche", "Critiqued traditional morality and proposed the will to power"],
        ]),
    },
    "philosophy-c1-l42": {
        "data_table": table(["Thinker", "Idea"], [
            ["Jean-Paul Sartre", "Humans are 'condemned to be free'"],
        ]),
    },
    "philosophy-c1-l43": {
        "data_table": table(["Thinker", "Idea"], [
            ["Simone de Beauvoir", "'One is not born, but rather becomes, a woman'"],
        ]),
    },
    "philosophy-c1-l44": {
        "data_table": table(["Fact", "Detail"], [
            ["Confucianism", "Chinese philosophy emphasizing ethics and social harmony"],
        ]),
    },
    "philosophy-c1-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Daoism", "Chinese philosophy emphasizing living in harmony with the Dao (the Way)"],
        ]),
    },
    "philosophy-c1-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["Buddhism", "Founded by Siddhartha Gautama, emphasizes the end of suffering"],
        ]),
    },
    "philosophy-c1-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["African philosophy", "Encompasses diverse traditions, including Ubuntu ethics of communal personhood"],
        ]),
    },
    "philosophy-c1-l48": {
        "data_table": table(["Fact", "Detail"], [
            ["Latin American philosophy", "Includes liberation philosophy addressing social justice"],
        ]),
    },
    "philosophy-c1-l49": {
        "data_table": table(["Dilemma", "Focus"], [
            ["Trolley problem", "Tests intuitions about consequentialist versus deontological ethics"],
        ]),
    },
    "philosophy-c1-l50": {
        "data_table": table(["Position", "View"], [
            ["Determinism", "All events are caused by prior events"], ["Free will", "Humans can make genuinely free choices"],
        ]),
    },
    "philosophy-c1-l51": {
        "data_table": table(["Question", "Focus"], [
            ["Personal identity", "What makes a person the same person over time"],
        ]),
    },
    "philosophy-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Applied ethics", "Applying ethical theory to specific real-world issues"],
        ]),
    },
    "philosophy-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental ethics", "Examines humans' ethical relationship with nature"],
        ]),
    },
    "philosophy-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Bioethics", "Examines ethical issues in medicine and biological research"],
        ]),
    },
    "philosophy-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of law", "Examines the nature, purpose, and legitimacy of law"],
        ]),
    },
    "philosophy-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Feminist philosophy", "Examines gender, power, and equality through a philosophical lens"],
        ]),
    },
    "philosophy-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of religion", "Examines religious belief and practice beyond questions of theism"],
        ]),
    },
    "philosophy-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Deductive reasoning", "Reasoning from general premises to a certain conclusion"], ["Inductive reasoning", "Reasoning from specific cases to a probable conclusion"],
        ]),
    },
    "philosophy-c1-l59": {
        "data_table": table(["Fallacy", "Description"], [
            ["Ad hominem", "Attacking the person instead of the argument"],
        ]),
    },
    "philosophy-c1-l60": {
        "data_table": table(["Part", "Purpose"], [
            ["Thesis", "States the paper's central claim"], ["Supporting argument", "Provides reasons for the claim"],
        ]),
    },
    "philosophy-c1-l61": {
        "data_table": table(["Thinker", "Idea"], [
            ["Jean-Jacques Rousseau", "Society should be governed by the collective general will"],
        ]),
    },
    "philosophy-c1-l62": {
        "data_table": table(["Thinker", "Idea"], [
            ["Simone de Beauvoir", "Explored how gender is socially constructed"],
        ]),
    },
    "philosophy-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a real-world debate", "Identifying which branch of philosophy it falls under"],
        ]),
    },
    "philosophy-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Diagramming an argument", "Breaking a newspaper editorial into premises and conclusion"],
        ]),
    },
    "philosophy-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating truth value", "Determining whether a proposition is true, false, or ambiguous"],
        ]),
    },
    "philosophy-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Testing a syllogism", "Checking whether a sample syllogism's conclusion follows validly"],
        ]),
    },
    "philosophy-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Spotting a fallacy", "Identifying a strawman argument in a political ad"],
        ]),
    },
    "philosophy-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Applying necessary/sufficient conditions", "Analyzing what qualifies something as a 'bachelor'"],
        ]),
    },
    "philosophy-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Comparing pre-Socratic views", "Contrasting Thales's and Heraclitus's accounts of reality"],
        ]),
    },
    "philosophy-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying the Socratic method", "Using probing questions to examine a common assumption"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Philosophy: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Philosophy lessons (completing 70/70).")


if __name__ == "__main__":
    main()
