#!/usr/bin/env python3
"""Depth pass, Grade 1 Geography: fill in real, hand-checked data_table
content for the 17 Grade 1 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 1 Geography to full 20/20 coverage.

Every fact is real (Earth's land/water percentages, real flag colors,
real capital cities, real seasonal hemisphere facts) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g1-l1": {
        "data_table": table(["Place", "Purpose"], [
            ["School", "Where children learn"], ["Park", "Where people play and relax"],
            ["Library", "Where people borrow books"],
        ]),
    },
    "geography-g1-l2": {
        "data_table": table(["Tool", "Description"], [
            ["Map", "A flat drawing showing where places are"], ["Globe", "A round model of the Earth"],
        ]),
    },
    "geography-g1-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Earth's surface covered by water", "About 71%"], ["Earth's surface covered by land", "About 29%"],
        ]),
    },
    "geography-g1-l5": {
        "data_table": table(["Landform", "Description"], [
            ["Hill", "A raised area of land, lower than a mountain"],
            ["Mountain", "A very tall, steep landform"],
        ]),
    },
    "geography-g1-l6": {
        "data_table": table(["Landform", "Description"], [
            ["River", "A flowing body of water that moves to the sea"],
            ["Lake", "A body of water surrounded by land"],
        ]),
    },
    "geography-g1-l9": {
        "data_table": table(["Country", "Flag Colors"], [
            ["USA", "Red, White, Blue"], ["Japan", "White, Red"], ["Brazil", "Green, Yellow, Blue"],
        ]),
    },
    "geography-g1-l10": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["USA", "Washington, D.C."],
        ]),
    },
    "geography-g1-l11": {
        "data_table": table(["Place Type", "Feature"], [
            ["City", "Large population, many buildings and services"],
            ["Village", "Small population, more open land"],
        ]),
    },
    "geography-g1-l12": {
        "data_table": table(["Climate Type", "Example Weather"], [
            ["Tropical", "Hot and rainy year-round"], ["Polar", "Very cold year-round"],
            ["Temperate", "Warm summers, cold winters"],
        ]),
    },
    "geography-g1-l13": {
        "data_table": table(["Desert", "Location", "Type"], [
            ["Sahara", "North Africa", "Hot desert (largest hot desert)"],
            ["Gobi", "Asia (Mongolia/China)", "Cold desert"],
            ["Antarctic Desert", "Antarctica", "Coldest and largest desert overall"],
        ]),
    },
    "geography-g1-l14": {
        "data_table": table(["Forest Type", "Feature"], [
            ["Rainforest", "Very wet, dense trees, lots of animals"],
            ["Temperate Forest", "Four seasons, deciduous and evergreen trees"],
        ]),
    },
    "geography-g1-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Island", "Land completely surrounded by water"],
            ["World's largest island", "Greenland"],
        ]),
    },
    "geography-g1-l16": {
        "data_table": table(["Hemisphere", "Summer Months"], [
            ["Northern", "June, July, August"], ["Southern", "December, January, February"],
        ]),
    },
    "geography-g1-l17": {
        "data_table": table(["Transport", "Environment"], [
            ["Car", "Roads"], ["Boat", "Water"], ["Airplane", "Air"], ["Train", "Railway tracks"],
        ]),
    },
    "geography-g1-l18": {
        "data_table": table(["Home Type", "Region"], [
            ["Igloo", "Arctic (traditional)"], ["Stilt house", "Areas prone to flooding"],
            ["Apartment", "Cities"],
        ]),
    },
    "geography-g1-l19": {
        "data_table": table(["Farm Product", "Example"], [
            ["Crops", "Wheat, corn, rice"], ["Livestock", "Cows, chickens, sheep"],
        ]),
    },
    "geography-g1-l20": {
        "data_table": table(["Community Helper", "Role"], [
            ["Doctor", "Helps sick people get better"],
            ["Firefighter", "Puts out fires and helps in emergencies"],
            ["Teacher", "Helps children learn"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Geography lessons (completing 20/20).")


if __name__ == "__main__":
    main()
