#!/usr/bin/env python3
"""Depth pass, Grade 4 World History: fill in real, hand-checked
data_table content for the 28 Grade 4 World History lessons not covered
by the earlier breadth-first batch. Brings Grade 4 World History to full
30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g4-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Genghis Khan"], ["Extent", "Largest contiguous land empire in history"],
        ]),
    },
    "world-history-g4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous structure", "The Great Pyramid of Giza"],
        ]),
    },
    "world-history-g4-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g4-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"], ["Meaning of 'democracy'", "Rule by the people"],
        ]),
    },
    "world-history-g4-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Great Wall length", "Over 13,000 miles (with all branches)"], ["Purpose", "Defense against invasions"],
        ]),
    },
    "world-history-g4-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Major cities", "Mohenjo-daro and Harappa"], ["River", "Indus River"],
        ]),
    },
    "world-history-g4-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Route", "Linked China and Europe"], ["Goods traded", "Silk, spices, precious stones"],
        ]),
    },
    "world-history-g4-l10": {
        "data_table": table(["Castle Feature", "Purpose"], [
            ["Moat", "Water-filled ditch for defense"], ["Drawbridge", "Raisable bridge to block entry"],
        ]),
    },
    "world-history-g4-l11": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"], ["Vasco da Gama", "Sea route to India"],
        ]),
    },
    "world-history-g4-l12": {
        "data_table": table(["Civilization", "Location"], [
            ["Maya", "Central America"], ["Inca", "Andes Mountains, South America"], ["Aztec", "Central Mexico"],
        ]),
    },
    "world-history-g4-l13": {
        "data_table": table(["Kingdom", "Known For"], [
            ["Mali Empire", "Ruler Mansa Musa, wealth from gold"], ["Kingdom of Ghana", "Early West African trade empire"],
        ]),
    },
    "world-history-g4-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "14th-17th century, began in Italy"], ["Meaning", "'Rebirth' of art, science, and learning"],
        ]),
    },
    "world-history-g4-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Scandinavia (Norway, Sweden, Denmark)"], ["Known for", "Longships and seafaring voyages"],
        ]),
    },
    "world-history-g4-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Samurai", "Japanese warrior class"], ["Code of honor", "Bushido"],
        ]),
    },
    "world-history-g4-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Capital", "Constantinople (modern Istanbul)"], ["Duration", "1299-1922"],
        ]),
    },
    "world-history-g4-l18": {
        "data_table": table(["Trade Route", "Goods Traded"], [
            ["Spice Routes", "Cinnamon, pepper, cloves"],
        ]),
    },
    "world-history-g4-l19": {
        "data_table": table(["Invention", "Origin"], [
            ["The wheel", "Ancient Mesopotamia"], ["Paper", "Ancient China"],
        ]),
    },
    "world-history-g4-l20": {
        "data_table": table(["Era", "Approximate Period"], [
            ["Ancient history", "3000 BCE - 500 CE"], ["Medieval history", "500 CE - 1500 CE"],
        ]),
    },
    "world-history-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Modern medicine", "Some early medical texts trace to the Islamic Golden Age"],
        ]),
    },
    "world-history-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Trade networks today", "Modern global trade echoes historic empire trade routes"],
        ]),
    },
    "world-history-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Modern engineering", "Pyramid construction techniques still studied today"],
        ]),
    },
    "world-history-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Record-keeping", "Modern writing systems evolved from early scripts"],
        ]),
    },
    "world-history-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Modern government", "Many democracies trace ideas back to ancient Athens"],
        ]),
    },
    "world-history-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Modern law", "Roman legal principles influence many legal systems today"],
        ]),
    },
    "world-history-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Tourism", "The Great Wall is a major visited landmark today"],
        ]),
    },
    "world-history-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Urban planning", "Indus Valley cities had early drainage systems"],
        ]),
    },
    "world-history-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Global trade today", "Modern shipping echoes Silk Road exchange"],
        ]),
    },
    "world-history-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Historic tourism", "Medieval castles are visited across Europe today"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 World History lessons (completing 30/30).")


if __name__ == "__main__":
    main()
