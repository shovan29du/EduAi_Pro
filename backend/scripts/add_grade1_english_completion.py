#!/usr/bin/env python3
"""Depth pass, Grade 1 English: fill in real, hand-checked data_table
content for the 17 Grade 1 English lessons not covered by the earlier
breadth-first batch (add_grade1_all_subjects_charts.py did 3 of the 20).
Brings Grade 1 English to full 20/20 real-content coverage.

Every fact is real (standard phonics blends, real vowel/consonant sounds,
real grammar categories) or explicitly structured reference content (a
letter-formation stroke guide, a directions-following checklist) --
nothing fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_english_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "eng-g1-l2": {
        "data_table": table(["Sight Word", "Example Sentence"], [
            ["the", "The dog runs."], ["is", "The sky is blue."], ["and", "I like cats and dogs."],
        ]),
    },
    "eng-g1-l3": {
        "data_table": table(["Story Part", "Question It Answers"], [
            ["Beginning", "Who and where does the story start?"],
            ["Middle", "What happens?"], ["End", "How does it finish?"],
        ]),
    },
    "eng-g1-l4": {
        "data_table": table(["Sentence Part", "Example"], [
            ["Naming part (who/what)", "The cat"], ["Telling part (what happens)", "sat on the mat."],
        ]),
    },
    "eng-g1-l5": {
        "data_table": table(["Word Type", "Example"], [
            ["Noun (a person, place, or thing)", "dog, school, ball"],
            ["Verb (an action)", "run, jump, eat"],
        ]),
    },
    "eng-g1-l6": {
        "data_table": table(["Rhyming Pair", "Example"], [
            ["cat / hat", "The cat wore a hat."], ["sun / fun", "The sun is fun."],
        ]),
    },
    "english-g1-l7": {
        "data_table": table(["Sounds Blended", "Word"], [
            ["c-a-t", "cat"], ["d-o-g", "dog"], ["s-u-n", "sun"],
        ]),
    },
    "english-g1-l8": {
        "data_table": table(["Word", "Beginning Sound", "Ending Sound"], [
            ["cat", "/k/", "/t/"], ["dog", "/d/", "/g/"], ["sun", "/s/", "/n/"],
        ]),
    },
    "english-g1-l10": {
        "data_table": table(["Letter", "Uppercase", "Lowercase"], [
            ["A", "A", "a"], ["B", "B", "b"], ["C", "C", "c"],
        ]),
    },
    "english-g1-l11": {
        "data_table": table(["Sight Word", "Example Sentence"], [
            ["can", "I can run."], ["see", "I see a bird."], ["like", "I like apples."],
        ]),
    },
    "english-g1-l12": {
        "data_table": table(["Direction Word", "Meaning"], [
            ["First", "Do this step before the others"], ["Then", "Do this step next"],
            ["Last", "Do this step at the end"],
        ]),
    },
    "english-g1-l13": {
        "data_table": table(["Speaking Skill", "Example"], [
            ["Sharing an idea", "'I think the story is about a lost dog.'"],
            ["Asking a question", "'Why did the dog get lost?'"],
        ]),
    },
    "english-g1-l14": {
        "data_table": table(["Retelling Word", "When to Use It"], [
            ["First", "The very beginning of the story"], ["Next", "What happens after that"],
            ["Finally", "How the story ends"],
        ]),
    },
    "english-g1-l15": {
        "data_table": table(["Adjective", "Describes"], [
            ["Big", "Size"], ["Red", "Color"], ["Soft", "Texture"],
        ]),
    },
    "english-g1-l16": {
        "data_table": table(["Punctuation Mark", "Use"], [
            [".", "Ends a statement"], ["?", "Ends a question"], ["!", "Shows excitement"],
        ]),
    },
    "english-g1-l17": {
        "data_table": table(["Letter Stroke Type", "Example Letters"], [
            ["Straight lines", "L, T, I"], ["Curves", "C, O, S"], ["Straight lines + curves", "B, D, P"],
        ]),
    },
    "english-g1-l18": {
        "data_table": table(["Writing Type", "Example"], [
            ["Label", "'Toys' on a box"], ["List", "Milk, Eggs, Bread"],
        ]),
    },
    "english-g1-l19": {
        "data_table": table(["Question Word", "Asks About"], [
            ["Who", "The people or characters"], ["What", "The event or object"],
            ["Where", "The place or setting"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["English"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json English: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 English lessons (completing 20/20).")


if __name__ == "__main__":
    main()
