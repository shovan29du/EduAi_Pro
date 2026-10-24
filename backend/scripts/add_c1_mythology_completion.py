#!/usr/bin/env python3
"""Depth pass, C1 Mythology: fill in real, hand-checked data_table
content for the 15 C1 Mythology lessons not covered by the earlier
breadth-first batch. Brings C1 Mythology to full 16/16 coverage.

Note: unlike most C1 subjects (70 lessons), Mythology is a compact
16-lesson subject: one overview lesson per major mythological tradition.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_mythology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mythology-c1-l2": {
        "data_table": table(["Figure", "Domain"], [
            ["Zeus", "King of the gods, ruler of the sky"], ["Athena", "Goddess of wisdom and strategic warfare"],
        ]),
    },
    "mythology-c1-l3": {
        "data_table": table(["Figure", "Domain"], [
            ["Ra", "Sun god, often depicted with a falcon head"], ["Osiris", "God of the afterlife and resurrection"],
        ]),
    },
    "mythology-c1-l4": {
        "data_table": table(["Figure", "Domain"], [
            ["Odin", "All-father god of wisdom, war, and death"], ["Thor", "God of thunder and protector of Midgard"],
        ]),
    },
    "mythology-c1-l5": {
        "data_table": table(["Figure", "Domain"], [
            ["The Dagda", "A powerful father-god associated with abundance"], ["Brigid", "Goddess of poetry, healing, and smithcraft"],
        ]),
    },
    "mythology-c1-l6": {
        "data_table": table(["Figure", "Domain"], [
            ["Kukulkan", "Feathered serpent deity linked to wind and learning"],
        ]),
    },
    "mythology-c1-l7": {
        "data_table": table(["Figure", "Domain"], [
            ["Quetzalcoatl", "Feathered serpent god of wind and knowledge"], ["Huitzilopochtli", "God of war and the sun"],
        ]),
    },
    "mythology-c1-l8": {
        "data_table": table(["Figure", "Domain"], [
            ["Inti", "Sun god, considered ancestor of the Inca rulers"], ["Pachamama", "Earth mother goddess"],
        ]),
    },
    "mythology-c1-l9": {
        "data_table": table(["Figure", "Domain"], [
            ["Jupiter", "King of the gods, equivalent to Greek Zeus"], ["Mars", "God of war"],
        ]),
    },
    "mythology-c1-l10": {
        "data_table": table(["Figure", "Domain"], [
            ["Marduk", "Chief Babylonian god, associated with creation"], ["Ishtar", "Goddess of love, beauty, and war"],
        ]),
    },
    "mythology-c1-l11": {
        "data_table": table(["Figure", "Domain"], [
            ["Jade Emperor", "Ruler of heaven in Chinese mythology"], ["Nuwa", "Creator goddess who shaped humanity from clay"],
        ]),
    },
    "mythology-c1-l12": {
        "data_table": table(["Figure", "Domain"], [
            ["Amaterasu", "Sun goddess, central figure in Shinto mythology"], ["Susanoo", "God of storms and the sea"],
        ]),
    },
    "mythology-c1-l13": {
        "data_table": table(["Figure", "Domain"], [
            ["Dangun", "Legendary founder of the first Korean kingdom"],
        ]),
    },
    "mythology-c1-l14": {
        "data_table": table(["Figure", "Domain"], [
            ["Maui", "Trickster demigod credited with fishing up islands"],
        ]),
    },
    "mythology-c1-l15": {
        "data_table": table(["Figure", "Domain"], [
            ["Anansi", "Trickster spider god of stories and wisdom, West Africa"],
        ]),
    },
    "mythology-c1-l16": {
        "data_table": table(["Tradition", "Figure"], [
            ["Slavic", "Perun, god of thunder and war"], ["Native American", "Coyote, a common trickster figure across many nations"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Mythology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Mythology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Mythology lessons (completing 16/16).")


if __name__ == "__main__":
    main()
