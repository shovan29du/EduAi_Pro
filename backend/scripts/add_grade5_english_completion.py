#!/usr/bin/env python3
"""Depth pass, Grade 5 English: fill in real, hand-checked data_table
content for the 28 Grade 5 English lessons not covered by the earlier
breadth-first batch. Brings Grade 5 English to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g5-l1": {
        "data_table": table(["Technique", "Effect"], [
            ["Flashback", "Shows an earlier event"], ["Foreshadowing", "Hints at what's to come"],
        ]),
    },
    "english-g5-l2": {
        "data_table": table(["Clause Type", "Example"], [
            ["Independent", "She ran fast (complete thought)"], ["Dependent", "Because she ran fast (incomplete)"],
        ]),
    },
    "english-g5-l3": {
        "data_table": table(["Sentence Type", "Example"], [
            ["Compound", "I like tea, and I like coffee."], ["Complex", "Although it rained, we went outside."],
        ]),
    },
    "english-g5-l4": {
        "data_table": table(["Voice", "Example"], [
            ["Active", "The dog chased the ball."], ["Passive", "The ball was chased by the dog."],
        ]),
    },
    "english-g5-l5": {
        "data_table": table(["Confused Pair", "Correct Use"], [
            ["Their/There/They're", "Their book, over there, they're happy"],
            ["Your/You're", "Your book, you're happy"],
        ]),
    },
    "english-g5-l8": {
        "data_table": table(["Concept", "Definition"], [
            ["Theme", "The underlying message or lesson of a story"],
        ]),
    },
    "english-g5-l9": {
        "data_table": table(["Comparison Type", "Example"], [
            ["Character trait comparison", "Comparing bravery across two characters"],
        ]),
    },
    "english-g5-l10": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["First person", "I, we"], ["Second person", "you"], ["Third person", "he, she, they"],
        ]),
    },
    "english-g5-l11": {
        "data_table": table(["Purpose", "Example"], [
            ["To persuade", "An opinion editorial"], ["To inform", "A textbook"], ["To entertain", "A novel"],
        ]),
    },
    "english-g5-l12": {
        "data_table": table(["Text Type", "Summary Focus"], [
            ["Fiction", "Main plot events"], ["Nonfiction", "Key facts and ideas"],
        ]),
    },
    "english-g5-l13": {
        "data_table": table(["Structure", "Signal Words"], [
            ["Compare and contrast", "similarly, however, both"],
        ]),
    },
    "english-g5-l14": {
        "data_table": table(["Structure", "Signal Words"], [
            ["Problem and solution", "problem, solution, therefore"],
        ]),
    },
    "english-g5-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Evidence", "Facts that support a claim"], ["Argument", "A claim backed by reasoning"],
        ]),
    },
    "english-g5-l16": {
        "data_table": table(["Poetic Element", "Meaning"], [
            ["Rhyme", "Words that end with the same sound"], ["Rhythm", "The pattern of stressed and unstressed syllables"],
        ]),
    },
    "english-g5-l17": {
        "data_table": table(["Essay Part", "Purpose"], [
            ["Claim", "States the writer's opinion"], ["Evidence", "Supports the claim"],
        ]),
    },
    "english-g5-l18": {
        "data_table": table(["Report Section", "Purpose"], [
            ["Introduction", "States the topic"], ["Body", "Presents researched facts"], ["Conclusion", "Summarizes"],
        ]),
    },
    "english-g5-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Citation", "Credit given to the original source"], ["Plagiarism", "Using someone's work without credit"],
        ]),
    },
    "english-g5-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Revising", "Improving content and organization"], ["Editing", "Fixing grammar and spelling"],
        ]),
    },
    "english-g5-l21": {
        "data_table": table(["Transition Word", "Use"], [
            ["However", "Shows contrast"], ["Therefore", "Shows a result"], ["Furthermore", "Adds information"],
        ]),
    },
    "english-g5-l22": {
        "data_table": table(["Rule", "Example"], [
            ["Use quotation marks", "\"Let's go,\" she said."], ["New line for new speaker", "Each character's dialogue starts a new paragraph"],
        ]),
    },
    "english-g5-l23": {
        "data_table": table(["Poetic Device", "Example"], [
            ["Metaphor", "Time is a thief"], ["Simile", "As brave as a lion"], ["Alliteration", "Peter Piper picked"],
        ]),
    },
    "english-g5-l24": {
        "data_table": table(["Organizer Type", "Use"], [
            ["Venn diagram", "Comparing and contrasting two things"], ["Timeline", "Showing events in order"],
        ]),
    },
    "english-g5-l25": {
        "data_table": table(["Debate Element", "Purpose"], [
            ["Claim", "States a position"], ["Rebuttal", "Responds to the opposing argument"],
        ]),
    },
    "english-g5-l26": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Bullet points", "Captures key ideas quickly"], ["Abbreviations", "Speeds up writing"],
        ]),
    },
    "english-g5-l27": {
        "data_table": table(["Tone", "Example Word Choice"], [
            ["Formal tone", "'I would like to request'"], ["Playful tone", "'Wanna grab a snack?'"],
        ]),
    },
    "english-g5-l28": {
        "data_table": table(["Fluency Skill", "Why It Matters"], [
            ["Reading at a steady pace", "Helps understanding"], ["Using expression", "Makes reading engaging"],
        ]),
    },
    "english-g5-l29": {
        "data_table": table(["Genre", "Purpose"], [
            ["Folktale", "Passed down orally, reflects cultural values"], ["Fable", "Teaches a moral lesson"],
        ]),
    },
    "english-g5-l30": {
        "data_table": table(["Letter Part", "Purpose"], [
            ["Formal greeting", "Dear Sir/Madam,"], ["Formal closing", "Sincerely,"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 English lessons (completing 30/30).")


if __name__ == "__main__":
    main()
