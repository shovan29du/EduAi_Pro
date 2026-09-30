#!/usr/bin/env python3
"""Depth pass, Grade 3 World Literature: fill in real, hand-checked
data_table content for the 18 Grade 3 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 3 World
Literature to full 20/20 coverage.

Content covers real folk tale origins and morals -- nothing fabricated
or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g3-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Fable", "A short story that teaches a moral lesson"],
            ["Moral", "The lesson a story teaches"],
        ]),
    },
    "world-literature-g3-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient Greece, credited to Aesop"], ["Moral", "Slow and steady wins the race"],
        ]),
    },
    "world-literature-g3-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "West African oral tradition"], ["Character", "Anansi, a clever trickster spider"],
        ]),
    },
    "world-literature-g3-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient Greece, credited to Aesop"],
            ["Moral", "Lying makes people distrust you, even when you tell the truth"],
        ]),
    },
    "world-literature-g3-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Japan"], ["Character", "Momotaro, born from a giant peach"],
        ]),
    },
    "world-literature-g3-l7": {
        "data_table": table(["Version", "Origin"], [
            ["Cendrillon", "France"], ["Ye Xian", "China"], ["Cinderella", "Popularized by Charles Perrault, France"],
        ]),
    },
    "world-literature-g3-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Country", "Denmark"],
        ]),
    },
    "world-literature-g3-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "African American folklore, rooted in African trickster tales"],
            ["Character", "Br'er Rabbit, a clever trickster"],
        ]),
    },
    "world-literature-g3-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Moral", "Speaking honestly, even when unpopular"],
        ]),
    },
    "world-literature-g3-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "European folklore, popularized by the Brothers Grimm"],
            ["Moral", "Be cautious of strangers"],
        ]),
    },
    "world-literature-g3-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient India"], ["Purpose", "Teaching wisdom through animal stories"],
        ]),
    },
    "world-literature-g3-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Setting", "Imperial China"],
        ]),
    },
    "world-literature-g3-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "English folklore"], ["Moral", "Being resourceful, but also facing consequences of greed"],
        ]),
    },
    "world-literature-g3-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Native American (Ojibwe) tradition"], ["Purpose", "Believed to filter out bad dreams"],
        ]),
    },
    "world-literature-g3-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient Greece, credited to Aesop"],
            ["Moral", "It is best to prepare for hard times"],
        ]),
    },
    "world-literature-g3-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Germany, collected by the Brothers Grimm"],
            ["Moral", "Being content with what you have"],
        ]),
    },
    "world-literature-g3-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "China, classic novel Journey to the West"], ["Character", "Sun Wukong, the Monkey King"],
        ]),
    },
    "world-literature-g3-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient Greece, credited to Aesop"], ["Moral", "Small acts of kindness are never wasted"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 World Literature lessons (completing 20/20).")


if __name__ == "__main__":
    main()
