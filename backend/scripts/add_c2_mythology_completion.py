#!/usr/bin/env python3
"""Depth pass, C2 Mythology: fill in real, hand-checked data_table
content for the 15 C2 Mythology lessons not covered by the earlier
breadth-first batch. Brings C2 Mythology to full 16/16 coverage.

Unlike most C2 subjects, Mythology has only 16 lessons, one per
mythological tradition. l1 was already completed by an earlier
breadth-first batch.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_mythology_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mythology-c2-l2": {
        "data_table": table(["Deity", "Domain"], [
            ["Zeus", "King of the gods, sky and thunder"],
            ["Chaos", "The primordial void from which the cosmos emerged"],
        ]),
    },
    "mythology-c2-l3": {
        "data_table": table(["Deity", "Domain"], [
            ["Ra", "Sun god and creator figure"],
            ["Nun", "The primordial waters of chaos before creation"],
        ]),
    },
    "mythology-c2-l4": {
        "data_table": table(["Deity", "Domain"], [
            ["Odin", "Chief god, wisdom, war, and death"],
            ["Ymir", "The primordial giant from whose body the world was formed"],
        ]),
    },
    "mythology-c2-l5": {
        "data_table": table(["Figure", "Domain"], [
            ["The Tuatha De Danann", "A race of divine beings central to Irish mythological cosmology"],
        ]),
    },
    "mythology-c2-l6": {
        "data_table": table(["Text", "Feature"], [
            ["Popol Vuh", "K'iche' Maya creation narrative describing the shaping of humanity"],
        ]),
    },
    "mythology-c2-l7": {
        "data_table": table(["Deity", "Domain"], [
            ["Huitzilopochtli", "Sun and war deity, patron of the Aztec people"],
            ["Quetzalcoatl", "Feathered serpent deity associated with creation and wind"],
        ]),
    },
    "mythology-c2-l8": {
        "data_table": table(["Deity", "Domain"], [
            ["Inti", "Sun god, ancestral figure of the Inca ruling line"],
            ["Viracocha", "Creator god who shaped the world and humanity"],
        ]),
    },
    "mythology-c2-l9": {
        "data_table": table(["Deity", "Domain"], [
            ["Jupiter", "King of the gods, sky and thunder"],
            ["Chaos (Roman)", "The formless void preceding ordered creation"],
        ]),
    },
    "mythology-c2-l10": {
        "data_table": table(["Text", "Feature"], [
            ["Enuma Elish", "Babylonian creation epic describing the origin of the cosmos and gods"],
        ]),
    },
    "mythology-c2-l11": {
        "data_table": table(["Figure", "Domain"], [
            ["Pangu", "Primordial being whose body formed the sky and earth upon death"],
            ["Nuwa", "Creator goddess who fashioned humanity"],
        ]),
    },
    "mythology-c2-l12": {
        "data_table": table(["Deity", "Domain"], [
            ["Izanagi and Izanami", "Primordial deities who created the Japanese islands"],
            ["Amaterasu", "Sun goddess, central figure of Shinto cosmology"],
        ]),
    },
    "mythology-c2-l13": {
        "data_table": table(["Figure", "Domain"], [
            ["Dangun", "Legendary founding figure of the first Korean kingdom"],
        ]),
    },
    "mythology-c2-l14": {
        "data_table": table(["Concept", "Feature"], [
            ["Mana", "A spiritual life force present in people, objects, and the natural world"],
        ]),
    },
    "mythology-c2-l15": {
        "data_table": table(["Figure", "Domain"], [
            ["Anansi", "Trickster spider figure prominent across West African oral tradition"],
        ]),
    },
    "mythology-c2-l16": {
        "data_table": table(["Tradition", "Feature"], [
            ["Australian Aboriginal", "Dreamtime narratives describe the ancestral creation of land and law"],
            ["Slavic", "Perun and other deities personify natural forces like thunder"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Mythology"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Mythology: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Mythology lessons (completing 16/16).")


if __name__ == "__main__":
    main()
