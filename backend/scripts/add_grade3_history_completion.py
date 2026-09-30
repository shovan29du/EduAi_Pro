#!/usr/bin/env python3
"""Depth pass, Grade 3 World History: fill in real, hand-checked data_table
content for the 18 Grade 3 World History lessons not covered by the
earlier breadth-first batch. Brings Grade 3 World History to full 20/20
coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g3-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous rulers", "Pharaohs, e.g. Tutankhamun"],
            ["Writing system", "Hieroglyphics"],
        ]),
    },
    "hist-g3-l2": {
        "data_table": table(["Civilization", "Known For"], [
            ["Ancient Greece", "Democracy, philosophy, the Olympics"],
            ["Ancient Rome", "Roads, law, the Colosseum"],
        ]),
    },
    "world-history-g3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["History", "The study of past events"], ["Historian", "A person who studies history"],
        ]),
    },
    "world-history-g3-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Timeline", "A visual list of events in order"], ["Chronology", "The order in which events happened"],
        ]),
    },
    "world-history-g3-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Early humans lived in", "Small groups called clans"], ["Main activities", "Hunting and gathering"],
        ]),
    },
    "world-history-g3-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"],
            ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g3-l7": {
        "data_table": table(["Invention", "Origin"], [
            ["Paper", "Ancient China"], ["The compass", "Ancient China"],
        ]),
    },
    "world-history-g3-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Major cities", "Mohenjo-daro and Harappa"], ["River", "Indus River"],
        ]),
    },
    "world-history-g3-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Route", "Linked China and Europe"], ["Goods traded", "Silk, spices, precious stones"],
        ]),
    },
    "world-history-g3-l10": {
        "data_table": table(["Aspect of Daily Life", "Detail"], [
            ["Food", "Bread, olives, wine"], ["Entertainment", "Gladiator games at the Colosseum"],
        ]),
    },
    "world-history-g3-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Built for", "Pharaoh Khufu"], ["Approximate build date", "c. 2560 BCE"],
        ]),
    },
    "world-history-g3-l12": {
        "data_table": table(["Trade Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices"], ["Trans-Saharan trade", "Gold, salt"],
        ]),
    },
    "world-history-g3-l14": {
        "data_table": table(["Castle Feature", "Purpose"], [
            ["Moat", "A water-filled ditch for defense"], ["Drawbridge", "A raisable bridge to block entry"],
        ]),
    },
    "world-history-g3-l15": {
        "data_table": table(["Kingdom", "Known For"], [
            ["Mali Empire", "Ruler Mansa Musa, wealth from gold"], ["Kingdom of Aksum", "Trade in the Horn of Africa"],
        ]),
    },
    "world-history-g3-l16": {
        "data_table": table(["Group", "Region"], [
            ["Iroquois", "Northeastern North America"], ["Sioux", "Great Plains of North America"],
        ]),
    },
    "world-history-g3-l17": {
        "data_table": table(["Invention", "Impact"], [
            ["The wheel", "Enabled transportation and machines"], ["The printing press", "Spread knowledge faster"],
        ]),
    },
    "world-history-g3-l18": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"], ["Vasco da Gama", "Sea route to India"],
        ]),
    },
    "world-history-g3-l20": {
        "data_table": table(["Landmark", "Location"], [
            ["The Great Wall", "China"], ["The Colosseum", "Italy"], ["Machu Picchu", "Peru"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 World History lessons (completing 20/20).")


if __name__ == "__main__":
    main()
