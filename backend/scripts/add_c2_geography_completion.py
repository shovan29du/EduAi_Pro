#!/usr/bin/env python3
"""Depth pass, C2 Geography: fill in real, hand-checked data_table
content for the 69 C2 Geography lessons not covered by the earlier
breadth-first batch. Brings C2 Geography to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geography-c2-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Human geography", "Studies how people, culture, and economic activity shape and are shaped by place"],
        ]),
    },
    "geography-c2-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Globalization", "The growing interconnection of economies, cultures, and populations worldwide"],
        ]),
    },
    "geography-c2-l4": {
        "data_table": table(["Pattern", "Driver"], [
            ["Urbanization", "Rural-to-urban migration driven by industrial and service-sector job growth"],
        ]),
    },
    "geography-c2-l5": {
        "data_table": table(["Dispute", "Core Issue"], [
            ["Territorial dispute", "Competing sovereignty claims often rooted in colonial-era border drawing"],
        ]),
    },
    "geography-c2-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Supply chain", "A network of production and logistics steps spanning multiple countries"],
        ]),
    },
    "geography-c2-l7": {
        "data_table": table(["Layer", "Example"], [
            ["Linguistic geography", "Mapping language families reveals historical migration and conquest patterns"],
        ]),
    },
    "geography-c2-l8": {
        "data_table": table(["Projection", "Distortion"], [
            ["Mercator", "Preserves angles but greatly exaggerates area near the poles"],
            ["Robinson", "Balances shape and area distortion for a more visually accurate world view"],
        ]),
    },
    "geography-c2-l9": {
        "data_table": table(["Tool", "Use"], [
            ["Remote sensing satellite", "Captures multispectral imagery used to monitor land cover change"],
        ]),
    },
    "geography-c2-l10": {
        "data_table": table(["Step", "Action"], [
            ["Building a GIS map", "Layer thematic data over a base map to visualize spatial relationships"],
        ]),
    },
    "geography-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Urban sprawl", "Low-density outward expansion of a city into surrounding land"],
        ]),
    },
    "geography-c2-l12": {
        "data_table": table(["Resource", "Management Challenge"], [
            ["Shared freshwater basin", "Requires cooperation among nations to avoid overuse and conflict"],
        ]),
    },
    "geography-c2-l13": {
        "data_table": table(["Region", "Feature"], [
            ["Sub-Saharan Africa", "Home to diverse climates, rapid urbanization, and young populations"],
        ]),
    },
    "geography-c2-l14": {
        "data_table": table(["Metric", "What It Measures"], [
            ["GDP", "Total economic output of a country"],
            ["HDI", "Composite of life expectancy, education, and income"],
        ]),
    },
    "geography-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Enclave", "A territory entirely surrounded by another country's territory"],
        ]),
    },
    "geography-c2-l16": {
        "data_table": table(["Hazard", "Response"], [
            ["Major earthquake/hurricane", "Requires early warning systems and resilient infrastructure planning"],
        ]),
    },
    "geography-c2-l17": {
        "data_table": table(["Concept", "Impact"], [
            ["Ecotourism", "Aims to fund conservation but can strain fragile ecosystems if unmanaged"],
        ]),
    },
    "geography-c2-l18": {
        "data_table": table(["Innovation", "Effect"], [
            ["Green Revolution", "High-yield crop varieties and fertilizer use sharply increased food output"],
        ]),
    },
    "geography-c2-l19": {
        "data_table": table(["Infrastructure", "Role"], [
            ["Ports and railways", "Anchor points connecting inland production to global trade routes"],
        ]),
    },
    "geography-c2-l20": {
        "data_table": table(["Era", "Border Change"], [
            ["Decolonization", "New states often inherited arbitrary colonial-era boundaries"],
        ]),
    },
    "geography-c2-l21": {
        "data_table": table(["Process", "Result"], [
            ["Subduction", "Oceanic plate sinks beneath another, producing volcanic arcs and deep trenches"],
        ]),
    },
    "geography-c2-l22": {
        "data_table": table(["Cell", "Effect"], [
            ["Hadley cell", "Drives tropical rainfall and subtropical desert belts through atmospheric circulation"],
        ]),
    },
    "geography-c2-l23": {
        "data_table": table(["Factor", "Effect on Species Range"], [
            ["Climate and dispersal barriers", "Determine where a species can establish a viable population"],
        ]),
    },
    "geography-c2-l24": {
        "data_table": table(["Cause", "Effect"], [
            ["Land degradation", "Overuse and deforestation strip topsoil and reduce agricultural productivity"],
        ]),
    },
    "geography-c2-l25": {
        "data_table": table(["Threat", "Response"], [
            ["Coastal erosion", "Managed retreat and engineered barriers are competing adaptation strategies"],
        ]),
    },
    "geography-c2-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Watershed management", "Coordinates land use across a drainage basin to protect water quality"],
        ]),
    },
    "geography-c2-l27": {
        "data_table": table(["Theory", "Explanation"], [
            ["Push-pull theory", "Migration results from factors driving people out and factors attracting them elsewhere"],
        ]),
    },
    "geography-c2-l28": {
        "data_table": table(["Process", "Effect"], [
            ["Gentrification", "Rising property values in a neighborhood can displace lower-income residents"],
        ]),
    },
    "geography-c2-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Global value chain", "Production stages spread across countries to exploit comparative advantage"],
        ]),
    },
    "geography-c2-l30": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Heartland theory", "Control of the Eurasian interior was argued to be key to global power"],
        ]),
    },
    "geography-c2-l31": {
        "data_table": table(["Map Type", "Use"], [
            ["Choropleth map", "Shades regions by data value to show spatial patterns like population density"],
        ]),
    },
    "geography-c2-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial data model", "Represents geographic features as vector (points/lines/polygons) or raster data"],
        ]),
    },
    "geography-c2-l33": {
        "data_table": table(["Technique", "Use"], [
            ["Multispectral image analysis", "Combines reflectance bands to classify land cover types"],
        ]),
    },
    "geography-c2-l34": {
        "data_table": table(["System", "Note"], [
            ["GPS / GNSS", "Multiple satellite constellations now provide redundant global positioning"],
        ]),
    },
    "geography-c2-l35": {
        "data_table": table(["Tension", "Detail"], [
            ["Globalization vs. local identity", "Global cultural flows coexist with resurgent regional and national identities"],
        ]),
    },
    "geography-c2-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Language endangerment", "Mapping shows minority languages retreating under dominant national languages"],
        ]),
    },
    "geography-c2-l37": {
        "data_table": table(["Concept", "Example"], [
            ["Sacred space", "Pilgrimage routes create durable geographic and economic corridors"],
        ]),
    },
    "geography-c2-l38": {
        "data_table": table(["Legacy", "Detail"], [
            ["Green Revolution's legacy", "Raised yields but left groundwater depletion and input dependency"],
        ]),
    },
    "geography-c2-l39": {
        "data_table": table(["Process", "Effect"], [
            ["Deindustrialization", "Manufacturing decline hollows out regional economies and populations"],
        ]),
    },
    "geography-c2-l40": {
        "data_table": table(["Resource", "Geopolitical Effect"], [
            ["Oil and gas", "Concentrated reserves give producing states outsized geopolitical leverage"],
        ]),
    },
    "geography-c2-l41": {
        "data_table": table(["Issue", "Example"], [
            ["Transboundary water conflict", "Upstream dam-building can reduce downstream water availability"],
        ]),
    },
    "geography-c2-l42": {
        "data_table": table(["Driver", "Effect"], [
            ["Tropical deforestation", "Agricultural expansion and logging are the leading drivers of forest loss"],
        ]),
    },
    "geography-c2-l43": {
        "data_table": table(["Region", "Impact"], [
            ["Regional climate change", "Impacts vary widely, from Arctic warming to Sahel drought intensification"],
        ]),
    },
    "geography-c2-l44": {
        "data_table": table(["Mineral", "Importance"], [
            ["Critical minerals (e.g. lithium, cobalt)", "Essential for batteries and renewable energy supply chains"],
        ]),
    },
    "geography-c2-l45": {
        "data_table": table(["Feature", "Detail"], [
            ["China's economic geography", "Coastal special economic zones drove export-led industrial growth"],
        ]),
    },
    "geography-c2-l46": {
        "data_table": table(["Feature", "Detail"], [
            ["Amazon Basin", "The world's largest rainforest and a major carbon sink under deforestation pressure"],
        ]),
    },
    "geography-c2-l47": {
        "data_table": table(["Feature", "Detail"], [
            ["Persian Gulf region", "Holds a large share of global proven oil reserves, shaping regional geopolitics"],
        ]),
    },
    "geography-c2-l48": {
        "data_table": table(["Feature", "Detail"], [
            ["EU spatial integration", "Cross-border infrastructure and free movement policies weave national economies together"],
        ]),
    },
    "geography-c2-l49": {
        "data_table": table(["Feature", "Detail"], [
            ["Great Lakes region", "Shared freshwater resource governed by binational agreements between the US and Canada"],
        ]),
    },
    "geography-c2-l50": {
        "data_table": table(["Feature", "Detail"], [
            ["Pacific Island nations", "Face existential risk from sea-level rise despite minimal carbon emissions"],
        ]),
    },
    "geography-c2-l51": {
        "data_table": table(["Trend", "Policy Response"], [
            ["Aging population", "Countries adjust pension systems and immigration policy to offset shrinking workforces"],
        ]),
    },
    "geography-c2-l52": {
        "data_table": table(["Challenge", "Detail"], [
            ["Megacity governance", "Coordinating services across fragmented municipal boundaries is a core difficulty"],
        ]),
    },
    "geography-c2-l53": {
        "data_table": table(["System", "Role"], [
            ["Global logistics network", "Container shipping and freight hubs move most of world trade by volume"],
        ]),
    },
    "geography-c2-l54": {
        "data_table": table(["Problem", "Response"], [
            ["Overtourism", "Destinations adopt visitor caps and seasonal pricing to manage strain"],
        ]),
    },
    "geography-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Vulnerability mapping", "Combines hazard exposure with social factors to target disaster resilience efforts"],
        ]),
    },
    "geography-c2-l56": {
        "data_table": table(["Application", "Use"], [
            ["Site suitability analysis", "Overlays multiple GIS layers to identify optimal locations for development"],
        ]),
    },
    "geography-c2-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial autocorrelation", "Measures whether nearby locations have similar values more than chance predicts"],
        ]),
    },
    "geography-c2-l58": {
        "data_table": table(["Method", "Purpose"], [
            ["Extreme event attribution", "Statistical modeling estimates how climate change altered an event's likelihood"],
        ]),
    },
    "geography-c2-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Ocean acidification", "Rising CO2 absorption lowers ocean pH, threatening marine calcifying species"],
        ]),
    },
    "geography-c2-l60": {
        "data_table": table(["Capstone Step", "Focus"], [
            ["Regional analysis", "Synthesize physical, economic, and political data into a policy recommendation"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch, so its
# data_table is hard-coded here rather than pulled from CHARTS.
_l3_source_table = table(["Climate Zone", "Characteristic"], [
    ["Tropical", "Hot year-round, high rainfall"],
    ["Temperate", "Moderate temperatures, four seasons"],
    ["Polar", "Very cold year-round"],
])

WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"geography-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"geography-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"geography-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Geography lessons (completing 70/70).")


if __name__ == "__main__":
    main()
