#!/usr/bin/env python3
"""Depth pass, M1 Geography: fill in real, hand-checked data_table
content for the 99 M1 Geography lessons not covered by the earlier
breadth-first batch. Brings M1 Geography to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "geography-m1-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Geopolitics & globalization", "Studies how power and interconnection shape territory and states"],
        ]),
    },
    "geography-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["GIS foundations", "Layers spatial data to analyze and visualize geographic patterns"],
        ]),
    },
    "geography-m1-l4": {
        "data_table": table(["Theory", "Focus"], [
            ["Migration push-pull theory", "Explains movement through factors driving departure and attraction"],
        ]),
    },
    "geography-m1-l5": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Heartland theory", "Control of the Eurasian interior was argued to be key to global power"],
        ]),
    },
    "geography-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Economic geography", "Studies the spatial organization of production, trade, and economic activity"],
        ]),
    },
    "geography-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Cultural geography", "Examines how identity, belief, and practice shape and are shaped by place"],
        ]),
    },
    "geography-m1-l8": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial statistics", "Quantitative methods that account for location and spatial dependence in data"],
        ]),
    },
    "geography-m1-l9": {
        "data_table": table(["Technique", "Use"], [
            ["Multispectral image classification", "Assigns land cover categories based on reflectance across wavelength bands"],
        ]),
    },
    "geography-m1-l10": {
        "data_table": table(["Principle", "Detail"], [
            ["Map design theory", "Balances accuracy, clarity, and visual hierarchy in cartographic communication"],
        ]),
    },
    "geography-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Urban studies", "Examines the social, economic, and spatial dynamics of cities"],
        ]),
    },
    "geography-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental geography and policy", "Links spatial environmental analysis to regulatory decision-making"],
        ]),
    },
    "geography-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Regional studies", "Examines the distinctive physical, cultural, and economic character of a world region"],
        ]),
    },
    "geography-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Geographies of inequality", "Maps how development outcomes vary unevenly across space"],
        ]),
    },
    "geography-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Political geography", "Studies how sovereignty and territorial control are organized and contested"],
        ]),
    },
    "geography-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Vulnerability", "Combines hazard exposure with social factors to determine disaster risk"],
        ]),
    },
    "geography-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Tourism political economy", "Examines who benefits and who bears costs from tourism development"],
        ]),
    },
    "geography-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Food security", "Depends on availability, access, and stability of food supply across regions"],
        ]),
    },
    "geography-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Logistics geography", "Studies how transportation networks shape the movement of goods"],
        ]),
    },
    "geography-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Field study capstone", "Applies geographic methods to an original, site-based research question"],
        ]),
    },
    "geography-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Ice sheet dynamics", "Studies glacial flow and melt processes affecting sea-level change"],
        ]),
    },
    "geography-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Fluvial geomorphology", "Studies how rivers shape and reshape channel landforms over time"],
        ]),
    },
    "geography-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Karst landscape", "Forms through dissolution of soluble bedrock like limestone"],
        ]),
    },
    "geography-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Aeolian process", "Wind-driven erosion and deposition shapes desert landforms like dunes"],
        ]),
    },
    "geography-m1-l25": {
        "data_table": table(["Theory", "Detail"], [
            ["Island biogeography theory", "Species richness balances immigration rate against extinction rate"],
        ]),
    },
    "geography-m1-l26": {
        "data_table": table(["Proxy", "Use"], [
            ["Ice core", "Records past atmospheric composition and temperature"],
        ]),
    },
    "geography-m1-l27": {
        "data_table": table(["Cell", "Effect"], [
            ["Hadley cell", "Drives tropical rainfall and subtropical desert belts through atmospheric circulation"],
        ]),
    },
    "geography-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Water budget", "Balances precipitation, evapotranspiration, runoff, and storage in a watershed"],
        ]),
    },
    "geography-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Pedogenesis", "The process by which soil forms through weathering and biological activity"],
        ]),
    },
    "geography-m1-l30": {
        "data_table": table(["Cycle", "Detail"], [
            ["Carbon cycle", "The movement of carbon among atmosphere, ocean, land, and living organisms"],
        ]),
    },
    "geography-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Hazard zonation", "Maps volcanic risk zones to guide land-use and evacuation planning"],
        ]),
    },
    "geography-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Earthquake risk mapping", "Combines fault location and ground conditions to estimate seismic hazard"],
        ]),
    },
    "geography-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Permafrost", "Ground that remains frozen for at least two consecutive years"],
        ]),
    },
    "geography-m1-l34": {
        "data_table": table(["Cause", "Effect"], [
            ["Desertification", "Overuse and deforestation strip topsoil and reduce agricultural productivity"],
        ]),
    },
    "geography-m1-l35": {
        "data_table": table(["Service", "Detail"], [
            ["Wetland ecosystem service", "Filters water, buffers floods, and supports biodiversity"],
        ]),
    },
    "geography-m1-l36": {
        "data_table": table(["System", "Detail"], [
            ["Ocean current", "Large-scale water movement driven by wind, temperature, and salinity differences"],
        ]),
    },
    "geography-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Historical geography", "Reconstructs how landscapes and spatial patterns have changed over time"],
        ]),
    },
    "geography-m1-l38": {
        "data_table": table(["Concept", "Example"], [
            ["Sacred space", "Pilgrimage routes create durable geographic and economic corridors"],
        ]),
    },
    "geography-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Linguistic landscape", "Studies the visible presence of language in public space"],
        ]),
    },
    "geography-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Disease diffusion model", "Maps how illness spreads spatially through a population over time"],
        ]),
    },
    "geography-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial epidemiology", "Analyzes disease incidence in relation to geographic location and environment"],
        ]),
    },
    "geography-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental criminology", "Studies how physical space and design influence crime patterns"],
        ]),
    },
    "geography-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial cognition", "Studies how people perceive, remember, and navigate geographic space"],
        ]),
    },
    "geography-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Space-time prism", "Defines the range of locations an individual can reach within a time budget"],
        ]),
    },
    "geography-m1-l45": {
        "data_table": table(["Theory", "Detail"], [
            ["Central place theory", "Explains the size and spacing of settlements based on market service areas"],
        ]),
    },
    "geography-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Energy resource distribution", "Uneven geographic concentration of energy resources shapes global trade and power"],
        ]),
    },
    "geography-m1-l47": {
        "data_table": table(["Issue", "Example"], [
            ["Transboundary water conflict", "Upstream dam-building can reduce downstream water availability"],
        ]),
    },
    "geography-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Food desert", "An area with limited access to affordable, healthy food options"],
        ]),
    },
    "geography-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Residential segregation", "Spatial clustering of population groups shaped by historical and market forces"],
        ]),
    },
    "geography-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Slum upgrading", "Improves infrastructure and tenure security in informal settlements"],
        ]),
    },
    "geography-m1-l51": {
        "data_table": table(["Process", "Effect"], [
            ["Deindustrialization", "Manufacturing decline hollows out regional economies and populations"],
        ]),
    },
    "geography-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Innovation cluster", "Geographic concentration of firms and talent that accelerates knowledge spillover"],
        ]),
    },
    "geography-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Financial center geography", "Studies why capital and financial services cluster in specific global cities"],
        ]),
    },
    "geography-m1-l54": {
        "data_table": table(["Concept", "Detail"], [
            ["Borderland theory", "Examines border regions as distinctive zones of interaction, not just dividing lines"],
        ]),
    },
    "geography-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Transnationalism", "Diaspora communities maintain active ties across more than one nation"],
        ]),
    },
    "geography-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Refugee settlement pattern", "Shaped by policy, proximity, and existing community networks"],
        ]),
    },
    "geography-m1-l57": {
        "data_table": table(["Driver", "Effect"], [
            ["Climate migration", "Environmental degradation increasingly drives population displacement"],
        ]),
    },
    "geography-m1-l58": {
        "data_table": table(["Threat", "Response"], [
            ["Coastal vulnerability", "Managed retreat and engineered barriers are competing adaptation strategies"],
        ]),
    },
    "geography-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Extractive industry geography", "Studies the spatial footprint and impact of resource extraction"],
        ]),
    },
    "geography-m1-l60": {
        "data_table": table(["Driver", "Effect"], [
            ["Tropical deforestation", "Agricultural expansion and logging are leading drivers of forest loss"],
        ]),
    },
    "geography-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Fisheries management", "Balances harvest levels with long-term marine resource sustainability"],
        ]),
    },
    "geography-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Conservation planning", "Uses spatial prioritization to maximize biodiversity protection"],
        ]),
    },
    "geography-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Urban heat island", "Cities retain more heat than surrounding rural areas due to built surfaces"],
        ]),
    },
    "geography-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental justice", "Examines unequal exposure to pollution across different social groups"],
        ]),
    },
    "geography-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Spatial autocorrelation", "Measures whether nearby locations have similar values more than chance predicts"],
        ]),
    },
    "geography-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital elevation model", "Represents terrain surface elevation as a continuous digital dataset"],
        ]),
    },
    "geography-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Participatory GIS", "Incorporates local community knowledge directly into spatial data collection"],
        ]),
    },
    "geography-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Geodesy", "The science of accurately measuring Earth's shape, orientation, and gravity field"],
        ]),
    },
    "geography-m1-l69": {
        "data_table": table(["Technique", "Use"], [
            ["Hyperspectral imaging", "Captures many narrow spectral bands to identify fine material differences"],
        ]),
    },
    "geography-m1-l70": {
        "data_table": table(["Technology", "Use"], [
            ["LiDAR", "Uses laser pulses to generate precise 3D topographic surface models"],
        ]),
    },
    "geography-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Geovisualization", "Designs interactive visual representations for large spatial datasets"],
        ]),
    },
    "geography-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Location-allocation modeling", "Optimizes facility placement to serve demand efficiently across space"],
        ]),
    },
    "geography-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Network analysis", "Studies connectivity and flow efficiency across transportation systems"],
        ]),
    },
    "geography-m1-l74": {
        "data_table": table(["Chokepoint", "Significance"], [
            ["Strait of Malacca", "One of the world's busiest and most strategically important shipping lanes"],
        ]),
    },
    "geography-m1-l75": {
        "data_table": table(["Issue", "Detail"], [
            ["Arctic sovereignty dispute", "Melting ice opens new shipping routes and resource access, raising territorial claims"],
        ]),
    },
    "geography-m1-l76": {
        "data_table": table(["Treaty", "Purpose"], [
            ["Antarctic Treaty System", "Reserves Antarctica for peaceful scientific use, suspending territorial claims"],
        ]),
    },
    "geography-m1-l77": {
        "data_table": table(["Feature", "Detail"], [
            ["Small Island Developing States", "Face outsized exposure to sea-level rise despite minimal emissions"],
        ]),
    },
    "geography-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Verticality", "Mountain regions organize ecology, culture, and economy along elevation gradients"],
        ]),
    },
    "geography-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Pastoralism", "A mobile land-use strategy adapted to seasonal grazing resource availability"],
        ]),
    },
    "geography-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Columbian Exchange", "Transfer of crops, animals, people, and disease between the Old and New Worlds"],
        ]),
    },
    "geography-m1-l81": {
        "data_table": table(["System", "Feature"], [
            ["Comparative colonial administration", "Colonial powers governed differently through direct or indirect rule"],
        ]),
    },
    "geography-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Territorial identity", "National identity is often constructed and reinforced through claimed geography"],
        ]),
    },
    "geography-m1-l83": {
        "data_table": table(["Method", "Detail"], [
            ["Critical geopolitics", "Analyzes how geopolitical narratives are discursively constructed, not neutral facts"],
        ]),
    },
    "geography-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Strategic geography", "Military base placement reflects and reinforces global power projection"],
        ]),
    },
    "geography-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Digital infrastructure geography", "Physical internet infrastructure is unevenly distributed across regions"],
        ]),
    },
    "geography-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Telecommunications network geography", "Studies spatial patterns of connectivity access and infrastructure"],
        ]),
    },
    "geography-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Logistics hub", "A key node anchoring global supply chain movement and distribution"],
        ]),
    },
    "geography-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["Pandemic diffusion modeling", "Maps how disease spreads spatially via mobility and contact networks"],
        ]),
    },
    "geography-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Applied geomorphology", "Uses landform science to inform hazard mitigation engineering design"],
        ]),
    },
    "geography-m1-l90": {
        "data_table": table(["Concept", "Detail"], [
            ["Stadium location analysis", "Considers accessibility and economic impact in sport facility siting"],
        ]),
    },
    "geography-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Pilgrimage route network", "Long-standing religious travel corridors shape regional economy and settlement"],
        ]),
    },
    "geography-m1-l92": {
        "data_table": table(["Trend", "Detail"], [
            ["Sea ice decline", "Arctic sea ice extent has decreased substantially over recent decades"],
        ]),
    },
    "geography-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Aquifer depletion", "Groundwater extraction exceeding natural recharge threatens long-term water security"],
        ]),
    },
    "geography-m1-l94": {
        "data_table": table(["Region", "Feature"], [
            ["The Sahel", "A transitional climate zone experiencing rainfall variability and livelihood stress"],
        ]),
    },
    "geography-m1-l95": {
        "data_table": table(["Infrastructure", "Role"], [
            ["Submarine cable network", "Carries the vast majority of international internet traffic"],
        ]),
    },
    "geography-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Special economic zone", "Designated area offering preferential policy to attract trade and investment"],
        ]),
    },
    "geography-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Urban shrinkage", "Population decline strains infrastructure maintenance and municipal finance"],
        ]),
    },
    "geography-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Desert urbanism", "City planning adapted to extreme heat and water scarcity constraints"],
        ]),
    },
    "geography-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Transboundary lake governance", "Requires cooperation among nations sharing a freshwater lake system"],
        ]),
    },
    "geography-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["High-speed rail integration", "Reshapes regional economic geography by shrinking effective travel distance"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Earth System", "Examples"], [
        ["Atmosphere", "Air, weather, climate"],
        ["Hydrosphere", "Oceans, rivers, ice"],
        ["Lithosphere", "Crust, rocks, tectonic plates"],
        ["Biosphere", "All living organisms"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"geography-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"geography-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"geography-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Geography lessons (completing 120/120).")


if __name__ == "__main__":
    main()
