#!/usr/bin/env python3
"""Depth pass, Grade 2 Geography: fill in real, hand-checked data_table
content for the 18 Grade 2 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 2 Geography to full 20/20 coverage.

Every fact is real (real landform definitions, the real Amazon Rainforest
fact, real polar region locations) -- nothing fabricated or presented as
fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "The day-to-day condition of the atmosphere"],
            ["Climate", "The typical weather pattern of a place over many years"],
        ]),
    },
    "geography-g2-l3": {
        "data_table": table(["Tool", "Description"], [
            ["Map", "A flat drawing showing where places are"], ["Globe", "A round model of the Earth"],
        ]),
    },
    "geography-g2-l4": {
        "data_table": table(["Direction", "Opposite"], [
            ["North", "South"], ["East", "West"],
        ]),
    },
    "geography-g2-l5": {
        "data_table": table(["Landform", "Description"], [
            ["Mountain", "A very tall, steep landform"],
            ["Valley", "Low land between hills or mountains"],
            ["Plain", "Flat, low-lying land"],
        ]),
    },
    "geography-g2-l6": {
        "data_table": table(["Landform", "Description"], [
            ["River", "A flowing body of water that moves to the sea"],
            ["Lake", "A body of water surrounded by land"],
        ]),
    },
    "geography-g2-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Largest rainforest", "Amazon Rainforest, South America"],
            ["Rainforest climate", "Hot and very wet year-round"],
        ]),
    },
    "geography-g2-l9": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["USA", "Washington, D.C."],
        ]),
    },
    "geography-g2-l10": {
        "data_table": table(["Place Type", "Feature"], [
            ["City", "Large population, many buildings and services"],
            ["Village", "Small population, more open land"],
        ]),
    },
    "geography-g2-l11": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Trees (wood)", "Building, paper"], ["Coal", "Energy"],
        ]),
    },
    "geography-g2-l12": {
        "data_table": table(["Home Type", "Region"], [
            ["Igloo", "Arctic (traditional)"], ["Stilt house", "Areas prone to flooding"],
            ["Apartment", "Cities"],
        ]),
    },
    "geography-g2-l13": {
        "data_table": table(["Transport", "Environment"], [
            ["Car", "Roads"], ["Boat", "Water"], ["Airplane", "Air"], ["Train", "Railway tracks"],
        ]),
    },
    "geography-g2-l14": {
        "data_table": table(["Community Helper", "Role"], [
            ["Doctor", "Helps sick people get better"],
            ["Firefighter", "Puts out fires and helps in emergencies"],
            ["Teacher", "Helps children learn"],
        ]),
    },
    "geography-g2-l15": {
        "data_table": table(["Landmark", "Country"], [
            ["Eiffel Tower", "France"], ["Great Wall", "China"], ["Statue of Liberty", "USA"],
        ]),
    },
    "geography-g2-l16": {
        "data_table": table(["Common Map Symbol", "Typical Meaning"], [
            ["Blue line", "River or stream"], ["Green area", "Park or forest"],
            ["Red square", "School or important building"], ["Black line", "Road"],
        ]),
    },
    "geography-g2-l17": {
        "data_table": table(["Climate", "Example Region"], [
            ["Hot", "Sahara Desert"], ["Cold", "Antarctica"],
        ]),
    },
    "geography-g2-l18": {
        "data_table": table(["Landform", "Description"], [
            ["Island", "Land completely surrounded by water"],
            ["Peninsula", "Land surrounded by water on three sides"],
        ]),
    },
    "geography-g2-l19": {
        "data_table": table(["Polar Region", "Location"], [
            ["Arctic", "Around the North Pole"], ["Antarctic", "Around the South Pole"],
        ]),
    },
    "geography-g2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Grid reference", "A letter and number used to find a location on a map"],
            ["Example", "B3 means column B, row 3"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Geography lessons (completing 20/20).")


if __name__ == "__main__":
    main()
