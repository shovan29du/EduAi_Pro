#!/usr/bin/env python3
"""Depth pass, Grade 5 Geography: fill in real, hand-checked data_table
content for the 28 Grade 5 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 5 Geography to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g5-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Climate change", "Long-term shift in global temperatures and weather patterns"],
            ["Greenhouse gas", "Traps heat in the atmosphere, e.g. CO2"],
        ]),
    },
    "geo-g5-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "geography-g5-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Latitude", "Distance north/south of the equator"], ["Longitude", "Distance east/west of the prime meridian"],
        ]),
    },
    "geography-g5-l5": {
        "data_table": table(["Map Type", "Shows"], [
            ["Physical map", "Landforms, elevation, water"], ["Political map", "Borders, cities, countries"],
        ]),
    },
    "geography-g5-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanization", "Growth of cities as more people move there"],
        ]),
    },
    "geography-g5-l8": {
        "data_table": table(["Resource", "Region Example"], [
            ["Oil", "Middle East"], ["Timber", "Amazon Basin"],
        ]),
    },
    "geography-g5-l9": {
        "data_table": table(["Land Use", "Example"], [
            ["Agriculture", "Growing crops on fertile plains"], ["Grazing", "Raising livestock on grasslands"],
        ]),
    },
    "geography-g5-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Watershed", "An area of land that drains into a river system"],
        ]),
    },
    "geography-g5-l11": {
        "data_table": table(["Desert", "Location"], [
            ["Sahara", "North Africa"], ["Gobi", "Asia"],
        ]),
    },
    "geography-g5-l12": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia"], ["Andes", "South America"],
        ]),
    },
    "geography-g5-l13": {
        "data_table": table(["Ocean", "Fact"], [
            ["Pacific Ocean", "Largest and deepest ocean"], ["Atlantic Ocean", "Second largest"],
        ]),
    },
    "geography-g5-l14": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "geography-g5-l15": {
        "data_table": table(["Cultural Region", "Example"], [
            ["East Asia", "China, Japan, Korea"], ["Middle East", "Saudi Arabia, Iran, Egypt"],
        ]),
    },
    "geography-g5-l16": {
        "data_table": table(["Disaster", "Preparedness Step"], [
            ["Earthquake", "Have an emergency kit ready"], ["Flood", "Know evacuation routes"],
        ]),
    },
    "geography-g5-l17": {
        "data_table": table(["Renewable Energy", "Example Country"], [
            ["Solar power", "Widely used in many sunny regions"], ["Wind power", "Widely used in Denmark"],
        ]),
    },
    "geography-g5-l18": {
        "data_table": table(["Effect of Deforestation", "Detail"], [
            ["Habitat loss", "Species lose their homes"], ["Increased CO2", "Fewer trees to absorb carbon"],
        ]),
    },
    "geography-g5-l19": {
        "data_table": table(["Projection", "Distortion"], [
            ["Mercator", "Distorts size near the poles"], ["Robinson", "Balances shape and size distortion"],
        ]),
    },
    "geography-g5-l20": {
        "data_table": table(["Trade Route", "Goods"], [
            ["Silk Road", "Silk, spices"], ["Spice Route", "Cinnamon, pepper"],
        ]),
    },
    "geography-g5-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "The line dividing two countries or regions"],
        ]),
    },
    "geography-g5-l22": {
        "data_table": table(["Biome", "Characteristic"], [
            ["Tundra", "Cold, treeless"], ["Rainforest", "Hot, humid, dense vegetation"],
        ]),
    },
    "geography-g5-l23": {
        "data_table": table(["Coastal Landform", "Description"], [
            ["Cliff", "Steep rock face along the coast"], ["Beach", "Sandy or rocky shore"],
        ]),
    },
    "geography-g5-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Food security", "Reliable access to enough affordable, nutritious food"],
        ]),
    },
    "geography-g5-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Water scarcity", "A lack of sufficient available water"],
        ]),
    },
    "geography-g5-l26": {
        "data_table": table(["Network Type", "Example"], [
            ["Railways", "Long-distance overland transport"], ["Shipping lanes", "Ocean freight routes"],
        ]),
    },
    "geography-g5-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Indigenous peoples", "The original inhabitants of a land, e.g. Aboriginal Australians"],
        ]),
    },
    "geography-g5-l28": {
        "data_table": table(["Region Type", "Characteristic"], [
            ["Developed", "High income, strong infrastructure"], ["Developing", "Growing economy, developing infrastructure"],
        ]),
    },
    "geography-g5-l29": {
        "data_table": table(["Tourism Impact", "Example"], [
            ["Economic benefit", "Jobs and revenue for local communities"],
            ["Environmental strain", "Increased waste or habitat pressure"],
        ]),
    },
    "geography-g5-l30": {
        "data_table": table(["Map Feature", "Meaning"], [
            ["Contour line", "Connects points of equal elevation"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Geography lessons (completing 30/30).")


if __name__ == "__main__":
    main()
