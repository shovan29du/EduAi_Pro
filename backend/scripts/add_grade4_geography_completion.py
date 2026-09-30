#!/usr/bin/env python3
"""Depth pass, Grade 4 Geography: fill in real, hand-checked data_table
content for the 28 Grade 4 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 4 Geography to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g4-l1": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Coal", "Energy production"], ["Forests", "Wood, paper"],
        ]),
    },
    "geo-g4-l2": {
        "data_table": table(["Event", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Volcanic eruption", "Magma rising through the crust"],
        ]),
    },
    "geography-g4-l3": {
        "data_table": table(["Map Element", "Meaning"], [
            ["Key/Legend", "Explains what map symbols mean"], ["Scale", "Shows real-world distance"],
        ]),
    },
    "geography-g4-l4": {
        "data_table": table(["Continent", "Ocean"], [
            ["Asia", "Pacific Ocean"], ["Africa", "Indian Ocean"], ["North America", "Atlantic Ocean"],
        ]),
    },
    "geography-g4-l6": {
        "data_table": table(["Landform", "Description"], [
            ["Plateau", "A raised, flat area of land"], ["Valley", "Low land between hills or mountains"],
        ]),
    },
    "geography-g4-l7": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid"], ["Polar", "Very cold"], ["Temperate", "Four seasons"],
        ]),
    },
    "geography-g4-l8": {
        "data_table": table(["River", "Importance"], [
            ["Nile", "Water source for Egypt, ancient civilization"], ["Amazon", "Largest river by discharge volume"],
        ]),
    },
    "geography-g4-l10": {
        "data_table": table(["Rainforest", "Location"], [
            ["Amazon Rainforest", "South America"], ["Congo Rainforest", "Central Africa"],
        ]),
    },
    "geography-g4-l11": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia"], ["Andes", "South America"], ["Rockies", "North America"],
        ]),
    },
    "geography-g4-l12": {
        "data_table": table(["Country", "Capital"], [
            ["France", "Paris"], ["Japan", "Tokyo"], ["Bangladesh", "Dhaka"],
        ]),
    },
    "geography-g4-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"], ["Most populous continent", "Asia"],
        ]),
    },
    "geography-g4-l14": {
        "data_table": table(["Community Type", "Feature"], [
            ["Urban", "Densely populated, tall buildings"], ["Rural", "Sparse population, farmland"],
        ]),
    },
    "geography-g4-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Standard time zones worldwide", "24"], ["Purpose", "Keeps clocks matched to the sun's position"],
        ]),
    },
    "geography-g4-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day conditions"], ["Climate", "Long-term average weather patterns"],
        ]),
    },
    "geography-g4-l17": {
        "data_table": table(["Ocean", "Fact"], [
            ["Pacific Ocean", "Largest and deepest ocean"], ["Atlantic Ocean", "Second largest ocean"],
        ]),
    },
    "geography-g4-l18": {
        "data_table": table(["Human Impact", "Example"], [
            ["Deforestation", "Cutting down forests"], ["Pollution", "Waste in air, water, or soil"],
        ]),
    },
    "geography-g4-l19": {
        "data_table": table(["Map Skill", "Purpose"], [
            ["Scale", "Converts map distance to real distance"], ["Compass rose", "Shows direction"],
        ]),
    },
    "geography-g4-l20": {
        "data_table": table(["Landmark", "Location"], [
            ["Great Wall", "China"], ["Eiffel Tower", "France"], ["Machu Picchu", "Peru"],
        ]),
    },
    "geography-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Choosing where to farm", "Fertile soil near a river"],
        ]),
    },
    "geography-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Building codes", "Earthquake-resistant buildings in high-risk zones"],
        ]),
    },
    "geography-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Road trip planning", "Using a map key to find rest stops"],
        ]),
    },
    "geography-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Shipping routes", "Ships crossing the Pacific between Asia and the Americas"],
        ]),
    },
    "geography-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["GPS", "Uses latitude and longitude to pinpoint location"],
        ]),
    },
    "geography-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["City planning", "Building on flat land rather than steep valleys"],
        ]),
    },
    "geography-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Choosing clothing", "Packing warm clothes for a polar climate trip"],
        ]),
    },
    "geography-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Irrigation", "Farmers use rivers to water crops"],
        ]),
    },
    "geography-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Desert farming", "Using drip irrigation to conserve water"],
        ]),
    },
    "geography-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Conservation", "Protecting rainforests preserves biodiversity"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Geography lessons (completing 30/30).")


if __name__ == "__main__":
    main()
