#!/usr/bin/env python3
"""Depth pass, Grade 8 Geography: fill in real, hand-checked data_table
content for the 38 Grade 8 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Geography to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g8-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"],
        ]),
    },
    "geo-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Food security", "Reliable access to enough affordable, nutritious food"],
        ]),
    },
    "geography-g8-l3": {
        "data_table": table(["Map Element", "Meaning"], [
            ["Legend", "Explains map symbols"], ["Scale", "Converts map distance to real distance"],
        ]),
    },
    "geography-g8-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Latitude", "Distance north/south of the equator"], ["Longitude", "Distance east/west of the prime meridian"],
        ]),
    },
    "geography-g8-l5": {
        "data_table": table(["Landform", "Description"], [
            ["Plateau", "A raised, flat area of land"], ["Valley", "Low land between hills or mountains"],
        ]),
    },
    "geography-g8-l6": {
        "data_table": table(["River", "Importance"], [
            ["Nile", "Water source for Egypt, ancient civilization"], ["Amazon", "Largest river by discharge volume"],
        ]),
    },
    "geography-g8-l7": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia"], ["Andes", "South America"],
        ]),
    },
    "geography-g8-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Weathering", "Breaking down of rock"], ["Erosion", "Movement of weathered material"],
        ]),
    },
    "geography-g8-l10": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid"], ["Temperate", "Four distinct seasons"],
        ]),
    },
    "geography-g8-l11": {
        "data_table": table(["Biome", "Characteristic"], [
            ["Tundra", "Cold, treeless"], ["Rainforest", "Hot, humid, dense vegetation"],
        ]),
    },
    "geography-g8-l12": {
        "data_table": table(["Desert", "Location"], [
            ["Sahara", "North Africa"], ["Gobi", "Asia"],
        ]),
    },
    "geography-g8-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanisation", "Growth of cities as more people move there"],
        ]),
    },
    "geography-g8-l15": {
        "data_table": table(["Community Type", "Feature"], [
            ["Rural", "Farms, open land"], ["Urban", "Densely populated, tall buildings"],
        ]),
    },
    "geography-g8-l16": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "geography-g8-l17": {
        "data_table": table(["Farming System", "Example"], [
            ["Subsistence farming", "Growing food mainly for one's own family"],
            ["Commercial farming", "Growing crops to sell for profit"],
        ]),
    },
    "geography-g8-l18": {
        "data_table": table(["Industry Type", "Example"], [
            ["Primary", "Farming, mining"], ["Secondary", "Manufacturing"],
        ]),
    },
    "geography-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "geography-g8-l20": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Coal", "Energy production"],
        ]),
    },
    "geography-g8-l21": {
        "data_table": table(["Energy Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Nonrenewable", "Coal, oil"],
        ]),
    },
    "geography-g8-l22": {
        "data_table": table(["Effect of Climate Change", "Example"], [
            ["Rising sea levels", "Threatens coastal communities"],
        ]),
    },
    "geography-g8-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Water scarcity", "A lack of sufficient available water"],
        ]),
    },
    "geography-g8-l24": {
        "data_table": table(["Effect of Deforestation", "Detail"], [
            ["Habitat loss", "Species lose their homes"], ["Increased CO2", "Fewer trees to absorb carbon"],
        ]),
    },
    "geography-g8-l25": {
        "data_table": table(["Tourism Impact", "Example"], [
            ["Economic benefit", "Jobs and revenue for local communities"], ["Environmental strain", "Increased waste"],
        ]),
    },
    "geography-g8-l26": {
        "data_table": table(["Network Type", "Example"], [
            ["Railways", "Long-distance overland transport"], ["Shipping lanes", "Ocean freight routes"],
        ]),
    },
    "geography-g8-l27": {
        "data_table": table(["Region Type", "Characteristic"], [
            ["Developed", "High income, strong infrastructure"], ["Developing", "Growing economy, developing infrastructure"],
        ]),
    },
    "geography-g8-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Poverty", "Lacking sufficient resources for basic needs"],
        ]),
    },
    "geography-g8-l29": {
        "data_table": table(["Continent", "Ocean"], [
            ["Asia", "Pacific Ocean"], ["Africa", "Indian Ocean"],
        ]),
    },
    "geography-g8-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "The line dividing two countries or regions"],
        ]),
    },
    "geography-g8-l31": {
        "data_table": table(["Hazard", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Flood", "Heavy rain or overflowing rivers"],
        ]),
    },
    "geography-g8-l32": {
        "data_table": table(["Coastal Process", "Effect"], [
            ["Erosion", "Wears away coastline over time"], ["Deposition", "Builds up sand and sediment"],
        ]),
    },
    "geography-g8-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Glacier", "A large, slow-moving mass of ice"],
        ]),
    },
    "geography-g8-l34": {
        "data_table": table(["Soil Type", "Characteristic"], [
            ["Loam", "Balanced mix, good for farming"], ["Clay", "Fine particles, retains water"],
        ]),
    },
    "geography-g8-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Most densely populated regions", "Often near coasts and rivers"],
        ]),
    },
    "geography-g8-l36": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"],
        ]),
    },
    "geography-g8-l37": {
        "data_table": table(["Protected Area Type", "Example"], [
            ["National park", "Yellowstone National Park"],
        ]),
    },
    "geography-g8-l38": {
        "data_table": table(["Projection", "Distortion"], [
            ["Mercator", "Distorts size near the poles"],
        ]),
    },
    "geography-g8-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["GIS", "Geographic Information System, maps and analyzes spatial data"],
        ]),
    },
    "geography-g8-l40": {
        "data_table": table(["Smart City Feature", "Example"], [
            ["Efficient public transit", "Reduces congestion and pollution"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Geography lessons (completing 40/40).")


if __name__ == "__main__":
    main()
