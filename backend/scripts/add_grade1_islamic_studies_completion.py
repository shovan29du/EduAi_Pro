#!/usr/bin/env python3
"""Depth pass, Grade 1 Islamic Studies: fill in real, hand-checked
data_table content for the 17 Grade 1 Islamic Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 1 Islamic Studies to
full 20/20 coverage.

These are early-childhood character/values lessons and Prophet story
overviews; content sticks to well-established, uncontroversial facts
(who each Prophet is known for and the widely-taught lesson from their
story) and general values examples -- nothing fabricated, no specific
scriptural citations that would need verification beyond common
knowledge.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_islamic_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "islamic-studies-g1-l2": {
        "data_table": table(["Act of Kindness", "Example"], [
            ["Sharing", "Sharing your toys with a friend"],
            ["Helping", "Helping someone who dropped their books"],
            ["Comforting", "Comforting a friend who is sad"],
        ]),
    },
    "islamic-studies-g1-l3": {
        "data_table": table(["Situation", "Way to Show Gratitude"], [
            ["Receiving a gift", "Saying 'thank you' and smiling"],
            ["Being helped", "Thanking the person who helped you"],
        ]),
    },
    "islamic-studies-g1-l5": {
        "data_table": table(["Time", "Purpose of the Dua"], [
            ["Before eating", "Thanking Allah for the food"],
            ["After eating", "Expressing gratitude for being fed"],
        ]),
    },
    "islamic-studies-g1-l6": {
        "data_table": table(["Value", "Example"], [
            ["Honesty", "Telling the truth even when it's hard"],
            ["Trustworthiness", "Keeping a promise you made"],
        ]),
    },
    "islamic-studies-g1-l7": {
        "data_table": table(["Sharing Example", "Who Benefits"], [
            ["Sharing food", "Family and friends at the table"],
            ["Sharing toys", "Playmates"],
        ]),
    },
    "islamic-studies-g1-l8": {
        "data_table": table(["Way to Show Respect", "Example"], [
            ["Listening", "Paying attention when they speak"],
            ["Helping", "Assisting with chores"],
        ]),
    },
    "islamic-studies-g1-l9": {
        "data_table": table(["Kind Action", "Example"], [
            ["Feeding", "Giving a pet food and water"],
            ["Gentle handling", "Petting an animal softly"],
        ]),
    },
    "islamic-studies-g1-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Prophet Adam is described as", "The first human being and prophet"],
            ["Lesson from his story", "Family, forgiveness, and starting anew"],
        ]),
    },
    "islamic-studies-g1-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Prophet Nuh (Noah) is known for", "Building an ark and patience over many years"],
            ["Lesson from his story", "Patience and trust in God"],
        ]),
    },
    "islamic-studies-g1-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Prophet Ibrahim (Abraham) is known for", "His strong faith and courage"],
            ["Lesson from his story", "Standing firm in belief"],
        ]),
    },
    "islamic-studies-g1-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Prophet Yusuf (Joseph) is known for", "Forgiving his brothers"],
            ["Lesson from his story", "Forgiveness"],
        ]),
    },
    "islamic-studies-g1-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Prophet Musa (Moses) is known for", "Leading his people and standing up for justice"],
            ["Lesson from his story", "Courage to stand for what is right"],
        ]),
    },
    "islamic-studies-g1-l16": {
        "data_table": table(["Value Shown", "Example"], [
            ["Kindness", "Caring for others even as a child"],
            ["Honesty", "Known as trustworthy from a young age"],
        ]),
    },
    "islamic-studies-g1-l17": {
        "data_table": table(["Way to Help", "Example"], [
            ["Charity", "Giving food or money to those who need it"],
            ["Volunteering", "Helping at a community event"],
        ]),
    },
    "islamic-studies-g1-l18": {
        "data_table": table(["Skill", "Example"], [
            ["Apologizing", "Saying 'I'm sorry' when you make a mistake"],
            ["Forgiving", "Letting go of anger when someone apologizes"],
        ]),
    },
    "islamic-studies-g1-l19": {
        "data_table": table(["Way to Care", "Example"], [
            ["Checking in", "Asking a neighbor how they are doing"],
            ["Helping", "Assisting a neighbor with a task"],
        ]),
    },
    "islamic-studies-g1-l20": {
        "data_table": table(["Situation", "Patient Response"], [
            ["Waiting your turn", "Waiting calmly without pushing"],
            ["Facing a challenge", "Trying again instead of giving up"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Islamic Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Islamic Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Islamic Studies lessons (completing 20/20).")


if __name__ == "__main__":
    main()
