#!/usr/bin/env python3
"""Depth pass, Grade 5 World Literature: fill in real, hand-checked
data_table content for the 28 Grade 5 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 5 World
Literature to full 30/30 coverage.

Content covers real literary/folk origins -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g5-l1": {
        "data_table": table(["Poet", "Country"], [
            ["Rumi", "Persia"], ["Matsuo Basho", "Japan"],
        ]),
    },
    "world-literature-g5-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Credited to", "Aesop, ancient Greece"], ["Style", "Short animal stories with morals"],
        ]),
    },
    "world-literature-g5-l3": {
        "data_table": table(["Folktale", "Origin"], [
            ["Cinderella variants", "Found across many cultures"], ["Anansi tales", "West Africa"],
        ]),
    },
    "world-literature-g5-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient India"], ["Purpose", "Teaching wisdom through animal stories"],
        ]),
    },
    "world-literature-g5-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Also known as", "One Thousand and One Nights"], ["Origin", "Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g5-l6": {
        "data_table": table(["God/Hero", "Known For"], [
            ["Zeus", "King of the gods"], ["Hercules", "Twelve legendary labors"],
        ]),
    },
    "world-literature-g5-l7": {
        "data_table": table(["Figure", "Known For"], [
            ["Odin", "Chief god, associated with wisdom"], ["Thor", "God of thunder"],
        ]),
    },
    "world-literature-g5-l8": {
        "data_table": table(["Tradition", "Region"], [
            ["Griot storytelling", "West Africa"],
        ]),
    },
    "world-literature-g5-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Indigenous peoples of North America"], ["Purpose", "Passing down cultural values orally"],
        ]),
    },
    "world-literature-g5-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "China"], ["Example", "Journey to the West"],
        ]),
    },
    "world-literature-g5-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "Japan"], ["Example", "Momotaro, the Peach Boy"],
        ]),
    },
    "world-literature-g5-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Collectors", "Jacob and Wilhelm Grimm"], ["Country", "Germany"],
        ]),
    },
    "world-literature-g5-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Country", "Denmark"],
        ]),
    },
    "world-literature-g5-l14": {
        "data_table": table(["Novel", "Author"], [
            ["Treasure Island", "Robert Louis Stevenson"], ["Around the World in Eighty Days", "Jules Verne"],
        ]),
    },
    "world-literature-g5-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Mark Twain"], ["Famous work", "The Adventures of Tom Sawyer"],
        ]),
    },
    "world-literature-g5-l17": {
        "data_table": table(["Region", "Example"], [
            ["Latin America", "La Llorona legend"],
        ]),
    },
    "world-literature-g5-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Region", "Middle East"], ["Example", "One Thousand and One Nights"],
        ]),
    },
    "world-literature-g5-l19": {
        "data_table": table(["Culture", "Poetic Form"], [
            ["Japan", "Haiku"], ["Persia", "Ghazal"],
        ]),
    },
    "world-literature-g5-l21": {
        "data_table": table(["Fable", "Moral"], [
            ["The Tortoise and the Hare", "Slow and steady wins the race"],
            ["The Ant and the Grasshopper", "Prepare for hard times"],
        ]),
    },
    "world-literature-g5-l22": {
        "data_table": table(["Epic", "Hero"], [
            ["The Odyssey", "Odysseus"], ["Gilgamesh", "Gilgamesh"],
        ]),
    },
    "world-literature-g5-l23": {
        "data_table": table(["Version", "Origin"], [
            ["Cendrillon", "France"], ["Ye Xian", "China"],
        ]),
    },
    "world-literature-g5-l24": {
        "data_table": table(["Trickster Character", "Origin"], [
            ["Anansi", "West Africa"], ["Br'er Rabbit", "African American folklore"],
        ]),
    },
    "world-literature-g5-l25": {
        "data_table": table(["Creation Myth", "Culture"], [
            ["Genesis", "Judeo-Christian tradition"], ["Izanagi and Izanami", "Japan"],
        ]),
    },
    "world-literature-g5-l26": {
        "data_table": table(["Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows dialogue"],
        ]),
    },
    "world-literature-g5-l27": {
        "data_table": table(["Genre", "Definition"], [
            ["Historical fiction", "Invented story set in a real historical period"],
        ]),
    },
    "world-literature-g5-l28": {
        "data_table": table(["Genre", "Definition"], [
            ["Biography", "A true account of someone else's life"],
            ["Autobiography", "A true account written by the subject themselves"],
        ]),
    },
    "world-literature-g5-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Translation", "Rendering a text into another language"],
        ]),
    },
    "world-literature-g5-l30": {
        "data_table": table(["Format", "Strength"], [
            ["Book", "Rich internal detail and description"], ["Film", "Visual and audio storytelling"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 World Literature lessons (completing 30/30).")


if __name__ == "__main__":
    main()
