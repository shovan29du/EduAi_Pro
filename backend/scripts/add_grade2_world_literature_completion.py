#!/usr/bin/env python3
"""Depth pass, Grade 2 World Literature: fill in real, hand-checked
data_table content for the 18 Grade 2 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 2 World
Literature to full 20/20 coverage.

Every fact is real (Beatrix Potter's 1902 publication of Peter Rabbit,
real folktale origins, real Aesop's Fables morals) -- nothing fabricated
or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Myth", "A traditional story explaining natural events, often with gods"],
            ["Legend", "A story based on real people/events, often exaggerated"],
        ]),
    },
    "world-literature-g2-l2": {
        "data_table": table(["Fable", "Moral Lesson"], [
            ["The Tortoise and the Hare", "Slow and steady wins the race"],
            ["The Ant and the Grasshopper", "Prepare for the future"],
        ]),
    },
    "world-literature-g2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Aesop's Fables, Ancient Greece"], ["Moral", "Slow and steady wins the race"],
        ]),
    },
    "world-literature-g2-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "West African (Ashanti) folklore"],
            ["Character", "Anansi, a clever trickster spider"],
        ]),
    },
    "world-literature-g2-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Aesop's Fables, Ancient Greece"],
            ["Moral", "Lying makes people stop believing you"],
        ]),
    },
    "world-literature-g2-l6": {
        "data_table": table(["Version", "Origin"], [
            ["Rhodopis", "Ancient Egypt/Greece (oldest known recorded version)"],
            ["Ye Xian", "China (Tang dynasty, 9th century)"],
            ["Cendrillon", "France (Charles Perrault, 1697)"],
        ]),
    },
    "world-literature-g2-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Published", "1843"],
            ["Moral", "True beauty and worth take time to be recognized"],
        ]),
    },
    "world-literature-g2-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "European folktale, best known from Charles Perrault (1697) and the Brothers Grimm (1812)"],
            ["Moral", "Be cautious of strangers"],
        ]),
    },
    "world-literature-g2-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "English folktale"], ["Moral", "Hard work and good planning pay off"],
        ]),
    },
    "world-literature-g2-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "English folktale, popularized by Robert Southey (1837)"],
            ["Moral", "Respect other people's belongings"],
        ]),
    },
    "world-literature-g2-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Beatrix Potter"], ["Published", "1902"], ["Main character", "Peter Rabbit"],
        ]),
    },
    "world-literature-g2-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient India, compiled c. 200 BCE-300 CE"],
            ["Content", "Animal fables teaching wisdom"],
        ]),
    },
    "world-literature-g2-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Chinese novel, published 16th century"],
            ["Attributed author", "Wu Cheng'en"], ["Main character", "Sun Wukong, the Monkey King"],
        ]),
    },
    "world-literature-g2-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Also known as", "One Thousand and One Nights"], ["Frame narrator", "Scheherazade"],
            ["Famous tales included", "Aladdin, Ali Baba, Sinbad the Sailor"],
        ]),
    },
    "world-literature-g2-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Various Native American traditions"],
            ["Character", "Coyote, a common trickster figure"],
        ]),
    },
    "world-literature-g2-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Character", "Sun Wukong, the Monkey King"],
            ["Origin", "Journey to the West, 16th-century Chinese novel"],
        ]),
    },
    "world-literature-g2-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Japanese folktale"],
            ["Character", "Momotaro, 'Peach Boy', born from a giant peach"],
        ]),
    },
    "world-literature-g2-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Aesop's Fables, Ancient Greece"],
            ["Moral", "It's easy to dismiss what you can't have as undesirable"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 World Literature lessons (completing 20/20).")


if __name__ == "__main__":
    main()
