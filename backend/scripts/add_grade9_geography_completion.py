#!/usr/bin/env python3
"""Depth pass, Grade 9 Geography: fill in real, hand-checked data_table
content for the 48 Grade 9 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Geography to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g9-l1": {
        "data_table": table(["Energy Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Nonrenewable", "Coal, oil"],
        ]),
    },
    "geo-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Geopolitics", "The study of how geography affects politics and international relations"],
        ]),
    },
    "geography-g9-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Weathering", "Breaking down of rock"], ["Erosion", "Movement of weathered material"],
        ]),
    },
    "geography-g9-l5": {
        "data_table": table(["River Feature", "Description"], [
            ["Delta", "Sediment deposit where a river meets the sea"], ["Meander", "A winding curve in a river"],
        ]),
    },
    "geography-g9-l6": {
        "data_table": table(["Coastal Process", "Effect"], [
            ["Erosion", "Wears away coastline over time"], ["Deposition", "Builds up sand and sediment"],
        ]),
    },
    "geography-g9-l8": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid"], ["Temperate", "Four distinct seasons"],
        ]),
    },
    "geography-g9-l9": {
        "data_table": table(["Tool", "Purpose"], [
            ["Barometer", "Measures air pressure"], ["Satellite imagery", "Tracks storm systems"],
        ]),
    },
    "geography-g9-l10": {
        "data_table": table(["Biome", "Characteristic"], [
            ["Tundra", "Cold, treeless"], ["Rainforest", "Hot, humid, dense vegetation"],
        ]),
    },
    "geography-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"],
        ]),
    },
    "geography-g9-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Most densely populated regions", "Often near coasts and rivers"],
        ]),
    },
    "geography-g9-l13": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "geography-g9-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanisation", "Growth of cities as more people move there"],
        ]),
    },
    "geography-g9-l15": {
        "data_table": table(["Land Use", "Example"], [
            ["Agriculture", "Growing crops on fertile plains"], ["Grazing", "Raising livestock on grasslands"],
        ]),
    },
    "geography-g9-l16": {
        "data_table": table(["Farming System", "Example"], [
            ["Subsistence farming", "Growing food mainly for one's own family"],
            ["Commercial farming", "Growing crops to sell for profit"],
        ]),
    },
    "geography-g9-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Food security", "Reliable access to enough affordable, nutritious food"],
        ]),
    },
    "geography-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Water scarcity", "A lack of sufficient available water"],
        ]),
    },
    "geography-g9-l19": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Coal", "Energy production"],
        ]),
    },
    "geography-g9-l20": {
        "data_table": table(["Effect of Deforestation", "Detail"], [
            ["Habitat loss", "Species lose their homes"], ["Increased CO2", "Fewer trees to absorb carbon"],
        ]),
    },
    "geography-g9-l21": {
        "data_table": table(["Region Type", "Characteristic"], [
            ["Developed", "High income, strong infrastructure"], ["Developing", "Growing economy, developing infrastructure"],
        ]),
    },
    "geography-g9-l22": {
        "data_table": table(["Trade Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices"], ["Spice Route", "Cinnamon, pepper"],
        ]),
    },
    "geography-g9-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "geography-g9-l24": {
        "data_table": table(["Tourism Impact", "Example"], [
            ["Economic benefit", "Jobs and revenue for local communities"], ["Environmental strain", "Increased waste"],
        ]),
    },
    "geography-g9-l25": {
        "data_table": table(["Network Type", "Example"], [
            ["Railways", "Long-distance overland transport"], ["Shipping lanes", "Ocean freight routes"],
        ]),
    },
    "geography-g9-l26": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Traditional dishes"],
        ]),
    },
    "geography-g9-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "The line dividing two countries or regions"],
        ]),
    },
    "geography-g9-l28": {
        "data_table": table(["Map Element", "Meaning"], [
            ["Legend", "Explains map symbols"], ["Scale", "Converts map distance to real distance"],
        ]),
    },
    "geography-g9-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["GIS", "Geographic Information System, maps and analyzes spatial data"],
        ]),
    },
    "geography-g9-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Remote sensing", "Collecting data about Earth from satellites or aircraft"],
        ]),
    },
    "geography-g9-l31": {
        "data_table": table(["Hazard", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Volcanic eruption", "Magma rising through the crust"],
        ]),
    },
    "geography-g9-l32": {
        "data_table": table(["Hazard", "Cause"], [
            ["Flood", "Heavy rain or overflowing rivers"], ["Drought", "Extended period of low rainfall"],
        ]),
    },
    "geography-g9-l33": {
        "data_table": table(["Hazard", "Cause"], [
            ["Hurricane", "Warm ocean water fueling a rotating storm"],
        ]),
    },
    "geography-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Disaster risk reduction", "Planning ahead to reduce harm from disasters"],
        ]),
    },
    "geography-g9-l35": {
        "data_table": table(["Cause of Climate Change", "Example"], [
            ["Greenhouse gases", "CO2 from burning fossil fuels"],
        ]),
    },
    "geography-g9-l36": {
        "data_table": table(["Global Response", "Example"], [
            ["Paris Agreement", "International accord to limit global warming"],
        ]),
    },
    "geography-g9-l37": {
        "data_table": table(["Renewable Energy", "Example Country"], [
            ["Solar power", "Widely used in many sunny regions"], ["Wind power", "Widely used in Denmark"],
        ]),
    },
    "geography-g9-l38": {
        "data_table": table(["Fossil Fuel", "Extraction Method"], [
            ["Coal", "Mining"], ["Oil", "Drilling"],
        ]),
    },
    "geography-g9-l39": {
        "data_table": table(["Ocean", "Fact"], [
            ["Pacific Ocean", "Largest and deepest ocean"],
        ]),
    },
    "geography-g9-l40": {
        "data_table": table(["Desert", "Location"], [
            ["Sahara", "North Africa"], ["Gobi", "Asia"],
        ]),
    },
    "geography-g9-l41": {
        "data_table": table(["Mountain Range", "Location"], [
            ["Himalayas", "Asia"], ["Andes", "South America"],
        ]),
    },
    "geography-g9-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Amazon Rainforest", "The largest rainforest in the world, spanning South America"],
        ]),
    },
    "geography-g9-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["Antarctica", "Coldest continent, largely covered in ice"],
        ]),
    },
    "geography-g9-l44": {
        "data_table": table(["Country in Africa", "Notable Fact"], [
            ["Nigeria", "Most populous country in Africa"], ["Egypt", "Home to the Nile River"],
        ]),
    },
    "geography-g9-l45": {
        "data_table": table(["Country in Asia", "Notable Fact"], [
            ["China", "Most populous country by some measures"], ["Japan", "An island nation"],
        ]),
    },
    "geography-g9-l46": {
        "data_table": table(["Country in Europe", "Notable Fact"], [
            ["France", "Largest country in the EU by area"],
        ]),
    },
    "geography-g9-l47": {
        "data_table": table(["Country in the Americas", "Notable Fact"], [
            ["Brazil", "Largest country in South America"], ["Canada", "Second largest country by area"],
        ]),
    },
    "geography-g9-l48": {
        "data_table": table(["Organization", "Purpose"], [
            ["United Nations", "Promotes peace and cooperation among countries"],
        ]),
    },
    "geography-g9-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Refugee", "A person forced to flee their country due to conflict or persecution"],
        ]),
    },
    "geography-g9-l50": {
        "data_table": table(["Goal", "Focus"], [
            ["No Poverty", "Ending poverty worldwide"], ["Quality Education", "Ensuring inclusive education for all"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Geography lessons (completing 50/50).")


if __name__ == "__main__":
    main()
