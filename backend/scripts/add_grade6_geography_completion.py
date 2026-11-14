#!/usr/bin/env python3
"""Depth pass, Grade 6 Geography: fill in real, hand-checked data_table
content for the 28 Grade 6 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 6 Geography to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g6-l1": {
        "data_table": table(["Biome", "Characteristic"], [
            ["Tundra", "Cold, treeless"], ["Rainforest", "Hot, humid, dense vegetation"],
        ]),
    },
    "geo-g6-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanisation", "Growth of cities as more people move there"],
        ]),
    },
    "geography-g6-l3": {
        "data_table": table(["Map Element", "Meaning"], [
            ["Legend", "Explains map symbols"], ["Scale", "Converts map distance to real distance"],
        ]),
    },
    "geography-g6-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Latitude", "Distance north/south of the equator"], ["Longitude", "Distance east/west of the prime meridian"],
        ]),
    },
    "geography-g6-l5": {
        "data_table": table(["Continent", "Ocean"], [
            ["Asia", "Pacific Ocean"], ["Africa", "Indian Ocean"],
        ]),
    },
    "geography-g6-l6": {
        "data_table": table(["Landform", "Description"], [
            ["Plateau", "A raised, flat area of land"], ["Valley", "Low land between hills or mountains"],
        ]),
    },
    "geography-g6-l7": {
        "data_table": table(["River", "Importance"], [
            ["Nile", "Water source for Egypt, ancient civilization"], ["Amazon", "Largest river by discharge volume"],
        ]),
    },
    "geography-g6-l8": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia"], ["Andes", "South America"],
        ]),
    },
    "geography-g6-l10": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid year-round"], ["Polar", "Very cold year-round"],
        ]),
    },
    "geography-g6-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Most densely populated regions", "Often near coasts and rivers"],
        ]),
    },
    "geography-g6-l12": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "geography-g6-l13": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Coal", "Energy production"],
        ]),
    },
    "geography-g6-l14": {
        "data_table": table(["Land Use", "Example"], [
            ["Agriculture", "Growing crops on fertile plains"], ["Grazing", "Raising livestock on grasslands"],
        ]),
    },
    "geography-g6-l15": {
        "data_table": table(["Country", "Capital"], [
            ["Nigeria", "Abuja"], ["Egypt", "Cairo"], ["Kenya", "Nairobi"],
        ]),
    },
    "geography-g6-l16": {
        "data_table": table(["Country", "Capital"], [
            ["Japan", "Tokyo"], ["India", "New Delhi"], ["Bangladesh", "Dhaka"],
        ]),
    },
    "geography-g6-l18": {
        "data_table": table(["Country", "Capital"], [
            ["United States", "Washington, D.C."], ["Brazil", "Brasilia"], ["Canada", "Ottawa"],
        ]),
    },
    "geography-g6-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "The line dividing two countries or regions"],
        ]),
    },
    "geography-g6-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Standard time zones worldwide", "24"], ["Purpose", "Keeps clocks matched to the sun's position"],
        ]),
    },
    "geography-g6-l21": {
        "data_table": table(["Disaster", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Flood", "Heavy rain or overflowing rivers"],
        ]),
    },
    "geography-g6-l22": {
        "data_table": table(["Trade Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices"], ["Spice Route", "Cinnamon, pepper"],
        ]),
    },
    "geography-g6-l23": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Traditional dishes"],
        ]),
    },
    "geography-g6-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Water scarcity", "A lack of sufficient available water"],
        ]),
    },
    "geography-g6-l25": {
        "data_table": table(["Effect of Deforestation", "Detail"], [
            ["Habitat loss", "Species lose their homes"], ["Increased CO2", "Fewer trees to absorb carbon"],
        ]),
    },
    "geography-g6-l26": {
        "data_table": table(["Renewable Energy", "Example Country"], [
            ["Solar power", "Widely used in many sunny regions"], ["Wind power", "Widely used in Denmark"],
        ]),
    },
    "geography-g6-l27": {
        "data_table": table(["Tourism Impact", "Example"], [
            ["Economic benefit", "Jobs and revenue for local communities"],
            ["Environmental strain", "Increased waste or habitat pressure"],
        ]),
    },
    "geography-g6-l28": {
        "data_table": table(["Projection", "Distortion"], [
            ["Mercator", "Distorts size near the poles"], ["Robinson", "Balances shape and size distortion"],
        ]),
    },
    "geography-g6-l29": {
        "data_table": table(["Tool", "Use"], [
            ["GPS", "Pinpoints exact location using satellites"], ["GIS", "Maps and analyzes spatial data"],
        ]),
    },
    "geography-g6-l30": {
        "data_table": table(["Coastal Process", "Effect"], [
            ["Erosion", "Wears away coastline over time"], ["Deposition", "Builds up sand and sediment"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Geography lessons (completing 30/30).")


if __name__ == "__main__":
    main()
