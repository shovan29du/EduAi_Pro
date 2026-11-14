#!/usr/bin/env python3
"""Depth pass, Grade 10 Geography: fill in real, hand-checked data_table
content for the Grade 10 Geography lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Geography to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geo-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "The growing interconnection of economies and cultures worldwide"],
        ]),
    },
    "geo-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Sustainability", "Meeting present needs without compromising future generations"],
        ]),
    },
    "geography-g10-l3": {
        "data_table": table(["Landform", "Formed By"], [
            ["Mountain range", "Collision of tectonic plates"], ["Rift valley", "Plates pulling apart"],
        ]),
    },
    "geography-g10-l5": {
        "data_table": table(["Process", "Description"], [
            ["Weathering", "Breakdown of rock in place"], ["Erosion", "Movement of weathered material"],
        ]),
    },
    "geography-g10-l6": {
        "data_table": table(["Feature", "Formed By"], [
            ["Meander", "River erosion and deposition over time"],
        ]),
    },
    "geography-g10-l7": {
        "data_table": table(["Process", "Result"], [
            ["Longshore drift", "Moves sediment along a coastline"],
        ]),
    },
    "geography-g10-l8": {
        "data_table": table(["Landform", "Formed By"], [
            ["U-shaped valley", "Glacial erosion"],
        ]),
    },
    "geography-g10-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Weather system", "A pattern of atmospheric conditions, e.g. a depression or anticyclone"],
        ]),
    },
    "geography-g10-l11": {
        "data_table": table(["Impact", "Example"], [
            ["Sea level rise", "Threatens low-lying coastal areas"],
        ]),
    },
    "geography-g10-l12": {
        "data_table": table(["Biome", "Feature"], [
            ["Tropical rainforest", "High rainfall, high biodiversity"], ["Tundra", "Cold, low vegetation"],
        ]),
    },
    "geography-g10-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Tropical rainforests", "Cover about 6% of Earth's land but hold immense biodiversity"],
        ]),
    },
    "geography-g10-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Desertification", "Land degradation into desert, often from overuse or climate change"],
        ]),
    },
    "geography-g10-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["World population", "Passed 8 billion in 2022"],
        ]),
    },
    "geography-g10-l16": {
        "data_table": table(["Factor", "Type"], [
            ["War", "Push factor"], ["Job opportunities", "Pull factor"],
        ]),
    },
    "geography-g10-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Urbanization in developing countries", "Often outpaces infrastructure, leading to informal settlements"],
        ]),
    },
    "geography-g10-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Urbanization in developed countries", "Often includes suburban growth and city center regeneration"],
        ]),
    },
    "geography-g10-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Urban regeneration", "Redeveloping declining urban areas"],
        ]),
    },
    "geography-g10-l20": {
        "data_table": table(["Indicator", "Measures"], [
            ["HDI", "Health, education, and income combined"], ["GNI per capita", "Average income level"],
        ]),
    },
    "geography-g10-l21": {
        "data_table": table(["Cause", "Example"], [
            ["Historical colonialism", "Shaped uneven resource distribution"],
        ]),
    },
    "geography-g10-l22": {
        "data_table": table(["Sector", "Example"], [
            ["Primary", "Farming"], ["Secondary", "Manufacturing"], ["Tertiary", "Services"],
        ]),
    },
    "geography-g10-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Trade interdependence", "Countries relying on each other for goods and resources"],
        ]),
    },
    "geography-g10-l24": {
        "data_table": table(["Impact", "Type"], [
            ["Job creation", "Positive economic impact of tourism"], ["Overcrowding", "Negative social impact"],
        ]),
    },
    "geography-g10-l25": {
        "data_table": table(["Resource", "Type"], [
            ["Oil", "Non-renewable"], ["Solar", "Renewable"],
        ]),
    },
    "geography-g10-l26": {
        "data_table": table(["Source", "Type"], [
            ["Solar power", "Renewable"], ["Wind power", "Renewable"],
        ]),
    },
    "geography-g10-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Freshwater", "Less than 3% of Earth's total water supply"],
        ]),
    },
    "geography-g10-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Food security", "Reliable access to sufficient, affordable, nutritious food"],
        ]),
    },
    "geography-g10-l29": {
        "data_table": table(["System", "Description"], [
            ["Subsistence farming", "Growing food for family use"], ["Commercial farming", "Growing food for sale"],
        ]),
    },
    "geography-g10-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Tropical storms", "Form over warm ocean water, called hurricanes/typhoons/cyclones by region"],
        ]),
    },
    "geography-g10-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Drought", "A prolonged period of abnormally low rainfall"],
        ]),
    },
    "geography-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Disaster risk management", "Reducing the impact of hazards through planning and mitigation"],
        ]),
    },
    "geography-g10-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Border", "A line dividing political or geographic territories"],
        ]),
    },
    "geography-g10-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Geopolitics", "The study of how geography influences politics and power"],
        ]),
    },
    "geography-g10-l35": {
        "data_table": table(["Tool", "Use"], [
            ["GIS", "Maps and analyzes spatial data digitally"],
        ]),
    },
    "geography-g10-l36": {
        "data_table": table(["Tool", "Use"], [
            ["Satellite imagery", "Monitors land use, weather, and environmental change"],
        ]),
    },
    "geography-g10-l37": {
        "data_table": table(["Projection", "Trade-off"], [
            ["Mercator projection", "Preserves angles but distorts size near the poles"],
        ]),
    },
    "geography-g10-l38": {
        "data_table": table(["Method", "Use"], [
            ["Field sketching", "Records observations directly at a site"],
        ]),
    },
    "geography-g10-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Rural land use change", "Farmland is increasingly converted for housing or industry"],
        ]),
    },
    "geography-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Superpower", "A state with significant global economic, political, and military influence"],
        ]),
    },
    "geography-g10-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["European Union", "Political and economic union of European countries, founded 1993"],
        ]),
    },
    "geography-g10-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Sub-Saharan Africa", "The region of Africa south of the Sahara Desert"],
        ]),
    },
    "geography-g10-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["South Asia", "Includes India, Pakistan, Bangladesh, and neighboring countries"],
        ]),
    },
    "geography-g10-l44": {
        "data_table": table(["Fact", "Detail"], [
            ["East Asia", "Includes China, Japan, and the Korean peninsula"],
        ]),
    },
    "geography-g10-l45": {
        "data_table": table(["Resource", "Example"], [
            ["Fisheries", "A major ocean resource"],
        ]),
    },
    "geography-g10-l46": {
        "data_table": table(["Cause", "Effect"], [
            ["Agricultural expansion", "A leading cause of deforestation"],
        ]),
    },
    "geography-g10-l47": {
        "data_table": table(["Pollutant", "Source"], [
            ["Particulate matter", "Vehicle and industrial emissions"],
        ]),
    },
    "geography-g10-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Protected area", "Land or sea set aside for conservation of biodiversity"],
        ]),
    },
    "geography-g10-l49": {
        "data_table": table(["Infrastructure Type", "Example"], [
            ["Transport network", "Roads, railways, and ports"],
        ]),
    },
    "geography-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural globalization", "The spread of ideas, values, and practices across the world"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Geography lessons (completing 50/50).")


if __name__ == "__main__":
    main()
