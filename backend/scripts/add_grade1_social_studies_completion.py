#!/usr/bin/env python3
"""Depth pass, Grade 1 Social Studies: fill in real, hand-checked
data_table content for the 17 Grade 1 Social Studies lessons not covered
by the earlier breadth-first batch. Brings Grade 1 Social Studies to full
20/20 coverage.

Content covers general, age-appropriate social/civic concepts with
concrete, uncontroversial examples -- nothing fabricated or presented as
fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g1-l1": {
        "data_table": table(["Group", "Example Members"], [
            ["Family", "Parents, siblings, grandparents"],
            ["Community", "Neighbors, local shopkeepers, teachers"],
        ]),
    },
    "social-studies-g1-l3": {
        "data_table": table(["Friendship Skill", "Example"], [
            ["Sharing", "Letting a friend use your crayons"],
            ["Listening", "Paying attention when a friend talks"],
        ]),
    },
    "social-studies-g1-l4": {
        "data_table": table(["Feeling", "Example Situation"], [
            ["Happy", "Playing with friends"], ["Sad", "Losing a favorite toy"],
            ["Angry", "Someone breaks your toy"],
        ]),
    },
    "social-studies-g1-l5": {
        "data_table": table(["Cooperation Example", "Benefit"], [
            ["Cleaning up together", "Finishes faster"], ["Building a puzzle together", "Combines everyone's ideas"],
        ]),
    },
    "social-studies-g1-l6": {
        "data_table": table(["Job", "What They Do"], [
            ["Baker", "Bakes bread and cakes"], ["Mail carrier", "Delivers letters and packages"],
        ]),
    },
    "social-studies-g1-l7": {
        "data_table": table(["School Role", "Job"], [
            ["Principal", "Leads the school"], ["Teacher", "Teaches lessons"], ["Janitor", "Keeps the school clean"],
        ]),
    },
    "social-studies-g1-l8": {
        "data_table": table(["Helper", "Role"], [
            ["Police officer", "Keeps the neighborhood safe"],
            ["Firefighter", "Responds to fires and emergencies"],
        ]),
    },
    "social-studies-g1-l9": {
        "data_table": table(["Way We Differ", "Example"], [
            ["Appearance", "Hair color, height, skin tone"], ["Culture", "Languages, foods, traditions"],
        ]),
    },
    "social-studies-g1-l10": {
        "data_table": table(["Situation", "Fair Response"], [
            ["Splitting a snack", "Give equal portions"], ["Taking turns", "Everyone gets a turn on the swing"],
        ]),
    },
    "social-studies-g1-l11": {
        "data_table": table(["Choice", "Responsibility"], [
            ["Choosing to play outside", "Coming back in on time"],
            ["Borrowing a toy", "Returning it in good condition"],
        ]),
    },
    "social-studies-g1-l13": {
        "data_table": table(["Tradition Type", "Example"], [
            ["Holiday tradition", "Special foods at celebrations"],
            ["Family tradition", "A weekly family game night"],
        ]),
    },
    "social-studies-g1-l15": {
        "data_table": table(["Community Type", "Example"], [
            ["School community", "Classmates and teachers"],
            ["Neighborhood community", "People who live near you"],
        ]),
    },
    "social-studies-g1-l16": {
        "data_table": table(["Rule", "Example"], [
            ["Ask before borrowing", "Asking a friend before using their toy"],
            ["Return what you borrow", "Giving back a borrowed book"],
        ]),
    },
    "social-studies-g1-l17": {
        "data_table": table(["Step", "Action"], [
            ["1", "Stay calm"], ["2", "Talk about the problem"], ["3", "Find a fair solution together"],
        ]),
    },
    "social-studies-g1-l18": {
        "data_table": table(["Good Citizen Habit", "Example"], [
            ["Following rules", "Waiting your turn in line"], ["Helping others", "Picking up litter"],
        ]),
    },
    "social-studies-g1-l19": {
        "data_table": table(["Custom", "Example"], [
            ["Greeting", "A handshake or a bow"], ["Food", "Special dishes eaten during celebrations"],
        ]),
    },
    "social-studies-g1-l20": {
        "data_table": table(["Then", "Now"], [
            ["Sending letters by mail", "Sending text messages"],
            ["Washing clothes by hand", "Using a washing machine"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Social Studies lessons (completing 20/20).")


if __name__ == "__main__":
    main()
