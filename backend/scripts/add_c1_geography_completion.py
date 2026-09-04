#!/usr/bin/env python3
"""Depth pass, C1 Geography: fill in real, hand-checked data_table
content for the 69 C1 Geography lessons not covered by the earlier
breadth-first batch. Brings C1 Geography to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geography-c1-l1": {
        "data_table": table(["Branch", "Focus"], [
            ["Physical geography", "Studies natural features: landforms, climate, water, and ecosystems"],
        ]),
    },
    "geography-c1-l2": {
        "data_table": table(["Branch", "Focus"], [
            ["Human geography", "Studies how people interact with and shape places"],
        ]),
    },
    "geography-c1-l4": {
        "data_table": table(["Stage", "Process"], [
            ["Evaporation", "Water turns to vapor from oceans, lakes, and land"], ["Precipitation", "Water falls back to Earth as rain, snow, or hail"],
        ]),
    },
    "geography-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Population distribution", "How people are spread across the Earth's surface"],
        ]),
    },
    "geography-c1-l6": {
        "data_table": table(["Type", "Meaning"], [
            ["Immigration", "Moving into a new country"], ["Emigration", "Leaving one's home country"],
        ]),
    },
    "geography-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "A boundary line separating two political territories or nations"],
        ]),
    },
    "geography-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Trade", "The exchange of goods and services between regions or countries"],
        ]),
    },
    "geography-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural landscape", "The visible imprint of human activity and culture on the land"],
        ]),
    },
    "geography-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Cartography", "The science and practice of drawing maps"],
        ]),
    },
    "geography-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Satellite imagery", "Images of Earth's surface captured from orbiting satellites"],
        ]),
    },
    "geography-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["GIS", "Geographic Information System, layers data onto maps for analysis"],
        ]),
    },
    "geography-c1-l13": {
        "data_table": table(["Element", "Purpose"], [
            ["Zoning", "Designates areas for residential, commercial, or industrial use"],
        ]),
    },
    "geography-c1-l14": {
        "data_table": table(["Resource", "Major Source Region"], [
            ["Oil", "Middle East, Russia, United States"], ["Iron ore", "Australia, Brazil, China"],
        ]),
    },
    "geography-c1-l15": {
        "data_table": table(["Feature", "Detail"], [
            ["Climate", "Mostly tropical, monsoon-influenced"], ["Economy", "Major exporter of electronics and agricultural goods"],
        ]),
    },
    "geography-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Global inequality", "Uneven distribution of wealth and resources between and within countries"],
        ]),
    },
    "geography-c1-l17": {
        "data_table": table(["Hazard", "Cause"], [
            ["Earthquake", "Sudden movement along tectonic plate boundaries"], ["Volcano", "Magma erupting through Earth's crust"],
        ]),
    },
    "geography-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Tourism geography", "Studies patterns and impacts of travel and tourism on places"],
        ]),
    },
    "geography-c1-l19": {
        "data_table": table(["Farming Type", "Feature"], [
            ["Subsistence farming", "Produces food mainly for the farmer's own family"], ["Commercial farming", "Produces crops for sale in markets"],
        ]),
    },
    "geography-c1-l20": {
        "data_table": table(["Mode", "Example"], [
            ["Maritime shipping", "Container ships moving goods across oceans"], ["Rail freight", "Trains moving bulk goods overland"],
        ]),
    },
    "geography-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Plate tectonics", "The theory that Earth's crust is divided into moving plates"],
        ]),
    },
    "geography-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather", "Short-term atmospheric conditions"], ["Climate", "Long-term average weather patterns in a region"],
        ]),
    },
    "geography-c1-l23": {
        "data_table": table(["Biome", "Feature"], [
            ["Tropical rainforest", "High rainfall and biodiversity near the equator"], ["Tundra", "Cold, treeless region near the poles"],
        ]),
    },
    "geography-c1-l24": {
        "data_table": table(["Soil Type", "Feature"], [
            ["Loam", "Balanced mix of sand, silt, and clay, ideal for farming"],
        ]),
    },
    "geography-c1-l25": {
        "data_table": table(["Landform", "Formation"], [
            ["Delta", "Sediment deposited where a river meets a larger body of water"], ["Cliff", "Steep rock face shaped by wave erosion"],
        ]),
    },
    "geography-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Drainage basin", "The area of land where all water drains to a common river or outlet"],
        ]),
    },
    "geography-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Population density", "The number of people per unit of land area"],
        ]),
    },
    "geography-c1-l28": {
        "data_table": table(["Pattern", "Feature"], [
            ["Urban settlement", "Dense, compact development with high population"], ["Rural settlement", "Dispersed, low-density development"],
        ]),
    },
    "geography-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic geography", "Studies the location and distribution of economic activity"],
        ]),
    },
    "geography-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Political geography", "Studies how political processes shape and are shaped by territory"],
        ]),
    },
    "geography-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Map projection", "A method for representing the curved Earth on a flat surface"],
        ]),
    },
    "geography-c1-l32": {
        "data_table": table(["Feature", "Meaning"], [
            ["Contour line", "A line connecting points of equal elevation on a topographic map"],
        ]),
    },
    "geography-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Remote sensing", "Collecting data about Earth's surface from a distance, often via satellite"],
        ]),
    },
    "geography-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["GPS", "Global Positioning System, satellites that provide location coordinates"],
        ]),
    },
    "geography-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural diffusion", "The spread of cultural beliefs and practices from one group to another"],
        ]),
    },
    "geography-c1-l36": {
        "data_table": table(["Family", "Example Languages"], [
            ["Indo-European", "English, Spanish, Hindi"], ["Sino-Tibetan", "Mandarin, Cantonese"],
        ]),
    },
    "geography-c1-l37": {
        "data_table": table(["Religion", "Major Region"], [
            ["Buddhism", "East and Southeast Asia"], ["Christianity", "Europe, the Americas"],
        ]),
    },
    "geography-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Agricultural geography", "Studies spatial patterns of farming and food production"],
        ]),
    },
    "geography-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Industrial geography", "Studies the location and organization of manufacturing activity"],
        ]),
    },
    "geography-c1-l40": {
        "data_table": table(["Energy Source", "Type"], [
            ["Coal", "Non-renewable fossil fuel"], ["Solar", "Renewable energy source"],
        ]),
    },
    "geography-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Water scarcity", "Insufficient available water to meet a region's demand"],
        ]),
    },
    "geography-c1-l42": {
        "data_table": table(["Cause", "Effect"], [
            ["Agricultural expansion", "Clears forest land, reducing biodiversity"],
        ]),
    },
    "geography-c1-l43": {
        "data_table": table(["Effect", "Example"], [
            ["Rising sea levels", "Threatens low-lying coastal communities"],
        ]),
    },
    "geography-c1-l44": {
        "data_table": table(["Resource", "Distribution Pattern"], [
            ["Freshwater", "Unevenly distributed, concentrated in few large basins"],
        ]),
    },
    "geography-c1-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["Population", "World's most populous region"], ["Economy", "Major manufacturing and technology hub"],
        ]),
    },
    "geography-c1-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["Geography", "Includes the Amazon rainforest and Andes mountains"],
        ]),
    },
    "geography-c1-l47": {
        "data_table": table(["Feature", "Detail"], [
            ["Climate", "Mostly arid and semi-arid"], ["Resource", "Rich oil and gas reserves"],
        ]),
    },
    "geography-c1-l48": {
        "data_table": table(["Feature", "Detail"], [
            ["Geography", "Varied terrain from Alpine mountains to lowland plains"],
        ]),
    },
    "geography-c1-l49": {
        "data_table": table(["Feature", "Detail"], [
            ["Geography", "Includes the Great Plains, Rocky Mountains, and Great Lakes"],
        ]),
    },
    "geography-c1-l50": {
        "data_table": table(["Feature", "Detail"], [
            ["Geography", "Includes Australia and thousands of Pacific islands"],
        ]),
    },
    "geography-c1-l51": {
        "data_table": table(["Stage", "Feature"], [
            ["Stage 1", "High birth and death rates, slow population growth"], ["Stage 4", "Low birth and death rates, stable population"],
        ]),
    },
    "geography-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanization", "The increasing share of a population living in cities"],
        ]),
    },
    "geography-c1-l53": {
        "data_table": table(["Network Type", "Example"], [
            ["Road network", "Highways connecting cities and regions"], ["Rail network", "Trains connecting distant regions"],
        ]),
    },
    "geography-c1-l54": {
        "data_table": table(["Impact Type", "Example"], [
            ["Positive", "Creates jobs and economic growth"], ["Negative", "Strains local infrastructure and resources"],
        ]),
    },
    "geography-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Vulnerability", "The degree to which a place or population is susceptible to harm from a hazard"],
        ]),
    },
    "geography-c1-l56": {
        "data_table": table(["Tool", "Use"], [
            ["GIS software", "Maps and analyzes spatial data digitally"],
        ]),
    },
    "geography-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Spatial analysis", "Examining patterns and relationships between locations"],
        ]),
    },
    "geography-c1-l58": {
        "data_table": table(["System", "Basis"], [
            ["Köppen classification", "Groups climates by temperature and precipitation patterns"],
        ]),
    },
    "geography-c1-l59": {
        "data_table": table(["Current", "Effect"], [
            ["Gulf Stream", "Warms coastal climates in Western Europe"],
        ]),
    },
    "geography-c1-l60": {
        "data_table": table(["Source", "Type of Data"], [
            ["Census records", "Population and demographic data"], ["Satellite imagery", "Land cover and environmental data"],
        ]),
    },
    "geography-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a landform", "Explaining how erosion shaped a coastal cliff"],
        ]),
    },
    "geography-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a settlement pattern", "Comparing rural and urban density in a region"],
        ]),
    },
    "geography-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Identifying landforms on a map", "Locating mountains, rivers, and plains from contour data"],
        ]),
    },
    "geography-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Tracing water flow", "Following a river from source to mouth on a map"],
        ]),
    },
    "geography-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting population data", "Reading a population density map for a country"],
        ]),
    },
    "geography-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing migration data", "Explaining push and pull factors behind a migration trend"],
        ]),
    },
    "geography-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a border dispute", "Examining the geographic origins of a territorial conflict"],
        ]),
    },
    "geography-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a trade route", "Mapping the flow of goods between two trading regions"],
        ]),
    },
    "geography-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a cultural landscape", "Identifying human modifications visible in a landscape photo"],
        ]),
    },
    "geography-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Reading a world map", "Identifying continents, oceans, and major latitude/longitude lines"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Geography lessons (completing 70/70).")


if __name__ == "__main__":
    main()
