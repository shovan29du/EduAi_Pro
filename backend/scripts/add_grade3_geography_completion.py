#!/usr/bin/env python3
"""Depth pass, Grade 3 Geography: fill in real, hand-checked data_table
content for the 18 Grade 3 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 3 Geography to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g3-l1": {
        "data_table": table(["Landform", "Description"], [
            ["River", "A flowing body of fresh water"], ["Mountain", "A tall landform with steep sides"],
        ]),
    },
    "geo-g3-l2": {
        "data_table": table(["Settlement Type", "Example"], [
            ["Village", "Small, few people"], ["City", "Large, many people"],
        ]),
    },
    "geography-g3-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Map", "A flat drawing of a place"], ["Globe", "A 3D model of the Earth"],
        ]),
    },
    "geography-g3-l4": {
        "data_table": table(["Continent", "Ocean"], [
            ["Asia", "Pacific Ocean"], ["Africa", "Indian Ocean"], ["Europe", "Atlantic Ocean"],
            ["Antarctica", "Southern Ocean"],
        ]),
    },
    "geography-g3-l5": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Blue line", "River"], ["Green area", "Forest"], ["Star", "Capital city"],
        ]),
    },
    "geography-g3-l6": {
        "data_table": table(["Direction", "Symbol"], [
            ["North", "N"], ["South", "S"], ["East", "E"], ["West", "W"],
        ]),
    },
    "geography-g3-l7": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid year-round"], ["Polar", "Very cold year-round"],
            ["Temperate", "Four distinct seasons"],
        ]),
    },
    "geography-g3-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day conditions"], ["Climate", "Average weather over many years"],
        ]),
    },
    "geography-g3-l10": {
        "data_table": table(["Desert", "Location"], [
            ["Sahara", "North Africa"], ["Gobi", "Asia (China/Mongolia)"], ["Sonoran", "North America"],
        ]),
    },
    "geography-g3-l11": {
        "data_table": table(["Forest", "Location"], [
            ["Amazon Rainforest", "South America"], ["Congo Rainforest", "Central Africa"],
        ]),
    },
    "geography-g3-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Island", "Land surrounded by water on all sides"],
            ["Peninsula", "Land surrounded by water on three sides"],
        ]),
    },
    "geography-g3-l13": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Trees", "Wood, paper"], ["Coal", "Energy"],
        ]),
    },
    "geography-g3-l14": {
        "data_table": table(["Community Type", "Feature"], [
            ["Rural", "Fewer people, farms and open land"], ["Urban", "Many people, tall buildings"],
        ]),
    },
    "geography-g3-l15": {
        "data_table": table(["Transport", "Common Use"], [
            ["Car", "Short distance land travel"], ["Airplane", "Long distance travel"], ["Ship", "Sea travel"],
        ]),
    },
    "geography-g3-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Purpose of time zones", "Keep local clocks matched to the sun's position"],
            ["Number of standard time zones worldwide", "24"],
        ]),
    },
    "geography-g3-l18": {
        "data_table": table(["Human Impact", "Example"], [
            ["Deforestation", "Cutting down forests for land or wood"],
            ["Pollution", "Waste entering air, water, or soil"],
        ]),
    },
    "geography-g3-l19": {
        "data_table": table(["Disaster", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Flood", "Heavy rain or overflowing rivers"],
        ]),
    },
    "geography-g3-l20": {
        "data_table": table(["Coastal Feature", "Description"], [
            ["Beach", "Sandy or rocky shore along water"], ["Cliff", "A steep rock face along the coast"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Geography lessons (completing 20/20).")


if __name__ == "__main__":
    main()
