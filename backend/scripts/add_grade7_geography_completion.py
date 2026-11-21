#!/usr/bin/env python3
"""Depth pass, Grade 7 Geography: fill in real, hand-checked data_table
content for the 38 Grade 7 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 7 Geography to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g7-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["GIS", "Geographic Information System, maps and analyzes spatial data"],
        ]),
    },
    "geography-g7-l3": {
        "data_table": table(["Continent", "Ocean"], [
            ["Asia", "Pacific Ocean"], ["Africa", "Indian Ocean"],
        ]),
    },
    "geography-g7-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Latitude", "Distance north/south of the equator"], ["Longitude", "Distance east/west of the prime meridian"],
        ]),
    },
    "geography-g7-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Standard time zones worldwide", "24"], ["International Date Line", "Roughly follows the 180th meridian"],
        ]),
    },
    "geography-g7-l6": {
        "data_table": table(["Landform", "Description"], [
            ["Plateau", "A raised, flat area of land"], ["Valley", "Low land between hills or mountains"],
        ]),
    },
    "geography-g7-l7": {
        "data_table": table(["River", "Importance"], [
            ["Nile", "Water source for Egypt, ancient civilization"], ["Amazon", "Largest river by discharge volume"],
        ]),
    },
    "geography-g7-l8": {
        "data_table": table(["Coastal Process", "Effect"], [
            ["Erosion", "Wears away coastline over time"], ["Deposition", "Builds up sand and sediment"],
        ]),
    },
    "geography-g7-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Day-to-day atmospheric conditions"], ["Climate", "Average weather over many years"],
        ]),
    },
    "geography-g7-l10": {
        "data_table": table(["Climate Zone", "Characteristic"], [
            ["Tropical", "Hot and humid"], ["Temperate", "Four distinct seasons"],
        ]),
    },
    "geography-g7-l12": {
        "data_table": table(["Stage", "Description"], [
            ["Evaporation", "Water turns to vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "geography-g7-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Most densely populated regions", "Often near coasts and rivers"],
        ]),
    },
    "geography-g7-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Most populous country (as of recent data)", "India"],
        ]),
    },
    "geography-g7-l15": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "geography-g7-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanisation", "Growth of cities as more people move there"],
        ]),
    },
    "geography-g7-l17": {
        "data_table": table(["Land Use", "Example"], [
            ["Agriculture", "Growing crops on fertile plains"], ["Grazing", "Raising livestock on grasslands"],
        ]),
    },
    "geography-g7-l18": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Coal", "Energy production"],
        ]),
    },
    "geography-g7-l19": {
        "data_table": table(["Farming System", "Example"], [
            ["Subsistence farming", "Growing food mainly for one's own family"],
            ["Commercial farming", "Growing crops to sell for profit"],
        ]),
    },
    "geography-g7-l20": {
        "data_table": table(["Industry Type", "Example"], [
            ["Primary", "Farming, mining"], ["Secondary", "Manufacturing"],
        ]),
    },
    "geography-g7-l21": {
        "data_table": table(["Trade Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices"], ["Spice Route", "Cinnamon, pepper"],
        ]),
    },
    "geography-g7-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "geography-g7-l23": {
        "data_table": table(["Tourism Impact", "Example"], [
            ["Economic benefit", "Jobs and revenue for local communities"], ["Environmental strain", "Increased waste or habitat pressure"],
        ]),
    },
    "geography-g7-l24": {
        "data_table": table(["Energy Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Nonrenewable", "Coal, oil"],
        ]),
    },
    "geography-g7-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Food security", "Reliable access to enough affordable, nutritious food"],
        ]),
    },
    "geography-g7-l26": {
        "data_table": table(["Hazard", "Cause"], [
            ["Earthquake", "Movement of tectonic plates"], ["Volcanic eruption", "Magma rising through the crust"],
        ]),
    },
    "geography-g7-l27": {
        "data_table": table(["Hazard", "Cause"], [
            ["Hurricane", "Warm ocean water fueling a rotating storm"], ["Flood", "Heavy rain or overflowing rivers"],
        ]),
    },
    "geography-g7-l28": {
        "data_table": table(["Effect of Climate Change", "Example"], [
            ["Rising sea levels", "Threatens coastal communities"], ["More extreme weather", "More frequent severe storms"],
        ]),
    },
    "geography-g7-l29": {
        "data_table": table(["Protected Area Type", "Example"], [
            ["National park", "Yellowstone National Park"], ["Wildlife reserve", "Serengeti National Park"],
        ]),
    },
    "geography-g7-l30": {
        "data_table": table(["Effect of Deforestation", "Detail"], [
            ["Habitat loss", "Species lose their homes"], ["Increased CO2", "Fewer trees to absorb carbon"],
        ]),
    },
    "geography-g7-l31": {
        "data_table": table(["Desert", "Location"], [
            ["Sahara", "North Africa"], ["Gobi", "Asia"],
        ]),
    },
    "geography-g7-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Antarctica", "Coldest continent, largely covered in ice"], ["Glacier", "A large, slow-moving mass of ice"],
        ]),
    },
    "geography-g7-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "The line dividing two countries or regions"], ["Nation-state", "A country with its own government and defined territory"],
        ]),
    },
    "geography-g7-l34": {
        "data_table": table(["Aspect of Culture", "Example"], [
            ["Language", "Different languages spoken worldwide"], ["Food", "Traditional dishes"],
        ]),
    },
    "geography-g7-l35": {
        "data_table": table(["Network Type", "Example"], [
            ["Railways", "Long-distance overland transport"], ["Shipping lanes", "Ocean freight routes"],
        ]),
    },
    "geography-g7-l36": {
        "data_table": table(["Goal", "Focus"], [
            ["No Poverty", "Ending poverty worldwide"], ["Quality Education", "Ensuring inclusive education for all"],
        ]),
    },
    "geography-g7-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Smart city", "A city using technology to improve services and infrastructure"],
        ]),
    },
    "geography-g7-l38": {
        "data_table": table(["Current", "Effect"], [
            ["Gulf Stream", "Warms parts of Europe's climate"],
        ]),
    },
    "geography-g7-l39": {
        "data_table": table(["Fieldwork Step", "Purpose"], [
            ["Data collection", "Gathering information in the field"], ["Analysis", "Interpreting the collected data"],
        ]),
    },
    "geography-g7-l40": {
        "data_table": table(["Newly Industrialised Country", "Example"], [
            ["South Korea", "Rapid industrial growth since the mid-20th century"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Geography lessons (completing 40/40).")


if __name__ == "__main__":
    main()
