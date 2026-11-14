#!/usr/bin/env python3
"""Depth pass, M2 Geography: fill in real, hand-checked data_table
content for the M2 Geography lessons not covered by the earlier
breadth-first batch. Brings M2 Geography to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning physical
geography and geomorphology, GIS and spatial analysis, human/economic/
political geography, and applied regional geography; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls
within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_geography_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Fluvial geomorphology", "Studies how rivers shape landforms through erosion and sediment transport"],
    ["Channel migration", "The lateral movement of a river channel across its floodplain over time"],
])

CHARTS: dict[str, dict] = {
    "geography-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["GIS research methods", "Systematic approaches for analyzing spatial data with geographic information systems"],
    ])},
    "geography-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Physical geography research methods", "Systematic field and laboratory approaches to studying Earth's physical systems"],
    ])},
    "geography-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Karst geomorphology", "Landscape features (caves, sinkholes) formed by dissolution of soluble rock like limestone"],
    ])},
    "geography-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Moraine", "A ridge of debris deposited directly by a glacier as it advances or retreats"],
    ])},
    "geography-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Aeolian geomorphology", "Studies landforms shaped by wind, such as migrating sand dunes"],
    ])},
    "geography-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Longshore drift", "The movement of sediment along a coast driven by waves approaching at an angle"],
    ])},
    "geography-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Tectonic geomorphology", "Studies how landscapes respond to and record fault activity and crustal deformation"],
    ])},
    "geography-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Ice core proxy", "Trapped air bubbles and isotopes in ice cores reveal past atmospheric and climate conditions"],
    ])},
    "geography-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Dendroclimatology", "Reconstructs past climate from patterns in annual tree-ring growth"],
    ])},
    "geography-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Island biogeography theory", "Predicts species richness on islands as a balance between immigration and extinction"],
    ])},
    "geography-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Species-area relationship", "Larger habitat areas tend to support a greater number of species"],
    ])},
    "geography-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Patch-corridor-matrix framework", "Describes landscape structure as habitat patches connected by corridors within a matrix"],
    ])},
    "geography-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Pedogenesis", "The process by which soils form and develop distinct horizons over time"],
    ])},
    "geography-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Watershed water balance", "Accounts for inputs (precipitation) and outputs (runoff, evaporation) across a drainage basin"],
    ])},
    "geography-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Aquifer recharge", "The process by which water infiltrates and replenishes underground water-bearing rock"],
    ])},
    "geography-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["ENSO teleconnection", "El Niño-Southern Oscillation alters weather patterns across distant regions of the globe"],
    ])},
    "geography-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Hadley cell", "A large-scale atmospheric circulation loop moving warm air from the equator toward the subtropics"],
    ])},
    "geography-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Urban heat island", "Cities are measurably warmer than surrounding rural areas due to infrastructure and reduced vegetation"],
    ])},
    "geography-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Desertification monitoring", "Tracks land degradation processes that turn productive land into desert-like conditions"],
    ])},
    "geography-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Permafrost thaw feedback", "Thawing permafrost releases stored carbon, potentially accelerating further warming"],
    ])},
    "geography-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Volcanic hazard zonation", "Maps areas at risk from different types of volcanic hazards to inform planning"],
    ])},
    "geography-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Seismic hazard mapping", "Assesses geographic variation in earthquake risk to inform building codes and planning"],
    ])},
    "geography-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Multispectral classification", "Categorizes land cover types using satellite imagery captured across multiple wavelength bands"],
    ])},
    "geography-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["LiDAR", "Uses laser pulses to generate precise 3D terrain models, even beneath vegetation canopy"],
    ])},
    "geography-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Spatial interpolation", "Estimates unknown values at unsampled locations from known nearby data points"],
    ])},
    "geography-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Kriging", "A geostatistical interpolation method that accounts for spatial autocorrelation in its estimates"],
    ])},
    "geography-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Moran's I", "A statistic measuring whether nearby locations have similar or dissimilar values (spatial clustering)"],
    ])},
    "geography-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Digital elevation model accuracy", "Assesses how closely a DEM's modeled terrain matches real-world elevation"],
    ])},
    "geography-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Cartographic generalization", "Simplifies map features appropriately as scale decreases while preserving meaning"],
    ])},
    "geography-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Map projection distortion", "Every flat map projection distorts some combination of area, shape, distance, or direction"],
    ])},
    "geography-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Participatory GIS", "Involves local communities directly in collecting and interpreting spatial data"],
    ])},
    "geography-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Central place theory", "Explains the size and spacing of settlements based on the market areas they serve"],
    ])},
    "geography-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Bid-rent model", "Land value and use decline with distance from a city center as competing bids fall"],
    ])},
    "geography-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Gentrification", "The process by which rising property values displace lower-income residents from a neighborhood"],
    ])},
    "geography-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Global city network theory", "Analyzes how major cities are interconnected through economic and information flows"],
    ])},
    "geography-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Agglomeration economies", "Firms clustering together gain shared productivity advantages"],
    ])},
    "geography-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Global value chain analysis", "Traces how a product's production stages are distributed across different countries"],
    ])},
    "geography-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Uneven development theory", "Explains persistent economic disparity between regions as inherent to capitalist growth"],
    ])},
    "geography-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Heartland thesis", "Mackinder's theory that control of Eurasia's interior is key to global geopolitical power"],
    ])},
    "geography-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Territoriality (border studies)", "Examines how political control is asserted and contested over bounded space"],
    ])},
    "geography-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Gerrymandering analysis", "Uses spatial methods to detect electoral districts drawn to favor a particular outcome"],
    ])},
    "geography-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Migration systems theory", "Views migration flows as structured, self-sustaining links between sending and receiving regions"],
    ])},
    "geography-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Demographic transition model", "Describes how birth and death rates shift as a country develops economically"],
    ])},
    "geography-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Forced displacement mapping", "Tracks and visualizes the spatial movement of refugees and displaced populations"],
    ])},
    "geography-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Landscape as text", "Interprets the built and natural landscape as a system of cultural meaning to be 'read'"],
    ])},
    "geography-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Sense of place", "Studies the subjective, lived meaning people attach to particular locations"],
    ])},
    "geography-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Diaspora / transnational space", "Studies communities maintaining identity and ties across dispersed geographic locations"],
    ])},
    "geography-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Von Thünen's land use model", "Predicts agricultural land use rings around a market based on transport cost"],
    ])},
    "geography-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Land grabbing", "Large-scale acquisition of farmland, often by foreign investors, raising food security concerns"],
    ])},
    "geography-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Network connectivity analysis", "Measures how well-connected nodes are within a transportation network"],
    ])},
    "geography-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility modeling", "Quantifies how easily people can reach destinations given transport infrastructure"],
    ])},
    "geography-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Spatial epidemiology", "Analyzes the geographic distribution and spread of infectious disease"],
    ])},
    "geography-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Healthcare accessibility mapping", "Identifies geographic gaps in access to medical services"],
    ])},
    "geography-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Political ecology", "Examines how power relations shape environmental change and resource access"],
    ])},
    "geography-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Human-environment interaction theory", "Studies the reciprocal relationship between societies and their physical environment"],
    ])},
    "geography-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Vulnerability and adaptation mapping", "Identifies which populations and places are most at risk from climate change"],
    ])},
    "geography-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Coastal vulnerability assessment", "Evaluates which coastal areas face the greatest risk from sea level rise"],
    ])},
    "geography-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Ice sheet mass balance", "Compares snow accumulation against ice loss to determine if an ice sheet is growing or shrinking"],
    ])},
    "geography-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Exclusive Economic Zone", "A maritime zone where a coastal state has special rights over resource exploration and use"],
    ])},
    "geography-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Coral reef ecosystem mapping", "Uses remote sensing and field survey to map reef health and extent"],
    ])},
    "geography-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Transboundary water management", "Coordinates governance of rivers and aquifers shared across national borders"],
    ])},
    "geography-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Integrated river basin governance", "Manages an entire watershed's water resources through coordinated policy"],
    ])},
    "geography-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Geomorphometry", "Quantitatively analyzes terrain shape and form using digital elevation data"],
    ])},
    "geography-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Landslide susceptibility mapping", "Identifies terrain conditions that make an area prone to landslides"],
    ])},
    "geography-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Floodplain delineation", "Maps the area likely to be inundated during a flood of a given probability"],
    ])},
    "geography-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Fire regime analysis", "Characterizes the typical frequency, intensity, and pattern of wildfires in a region"],
    ])},
    "geography-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Global carbon cycle", "Traces the movement of carbon between atmosphere, oceans, land, and living organisms"],
    ])},
    "geography-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Global nitrogen cycle", "Traces the movement of nitrogen between atmosphere, soil, and living organisms"],
    ])},
    "geography-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Continental reconstruction", "Reconstructs the past positions of continents over geological time using plate tectonics"],
    ])},
    "geography-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Milankovitch forcing", "Cyclical changes in Earth's orbit and tilt that drive long-term ice age cycles"],
    ])},
    "geography-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Amazon Basin ecological systems", "One of Earth's most biodiverse and carbon-rich river basin ecosystems"],
    ])},
    "geography-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Sahel climate variability", "A semi-arid transition zone in Africa known for high rainfall variability and drought risk"],
    ])},
    "geography-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Himalayan water tower", "The Himalayas store and release freshwater that sustains billions downstream"],
    ])},
    "geography-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Mekong River geopolitics", "Upstream dam-building creates transboundary tension among Mekong basin countries"],
    ])},
    "geography-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Urban political ecology", "Examines how power shapes the flow of resources through urban infrastructure"],
    ])},
    "geography-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Time-space compression", "Describes how modern transport and communication shrink perceived distance"],
    ])},
    "geography-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["World-systems spatial analysis", "Maps global inequality through core-periphery economic relations"],
    ])},
    "geography-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Gendered space theory", "Examines how everyday spaces are shaped by and reinforce gender relations"],
    ])},
    "geography-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Critical GIS", "Examines the power dynamics and biases embedded in how spatial data is collected and used"],
    ])},
    "geography-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Volunteered geographic information", "Spatial data contributed by ordinary citizens rather than official agencies"],
    ])},
    "geography-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Site suitability analysis", "Uses GIS to evaluate and rank locations for a proposed land use"],
    ])},
    "geography-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Network analysis (GIS)", "Models routing and connectivity problems over road or utility networks"],
    ])},
    "geography-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Hot spot analysis", "Statistically identifies clusters of unusually high or low values in spatial data"],
    ])},
    "geography-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Geodetic datum", "A reference framework defining coordinates precisely on Earth's curved surface"],
    ])},
    "geography-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["GNSS accuracy", "Assesses the precision of satellite-based positioning systems under varying conditions"],
    ])},
    "geography-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Weathering", "The physical and chemical breakdown of rock at Earth's surface"],
    ])},
    "geography-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Soil erosion model", "Predicts soil loss from a landscape given rainfall, slope, and land cover factors"],
    ])},
    "geography-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Phylogeography", "Studies how a species' genetic lineages are distributed across geographic space"],
    ])},
    "geography-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Landscape genetics (spatial patterns)", "Maps how genetic variation correlates with landscape features across a region"],
    ])},
    "geography-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Urban sprawl measurement", "Quantifies low-density urban expansion using land use change detection"],
    ])},
    "geography-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Renewable resource siting", "Uses geographic analysis to identify optimal locations for wind or solar installations"],
    ])},
    "geography-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Environmental justice", "Examines how pollution exposure disproportionately affects certain communities"],
    ])},
    "geography-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Indigenous counter-mapping", "Uses cartography to assert Indigenous land claims against colonial map narratives"],
    ])},
    "geography-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Quantitative revolution (geography)", "A mid-20th-century shift toward statistical and modeling approaches in geography"],
    ])},
    "geography-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Humanistic geography", "Critiques positivist spatial science by emphasizing subjective human experience of place"],
    ])},
    "geography-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Disaster risk reduction planning", "Applies geographic analysis to reduce vulnerability before disasters strike"],
    ])},
    "geography-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Hägerstrand's space-time path", "Models an individual's daily movement as a continuous path through space and time"],
    ])},
    "geography-m2-l99": {"data_table": table(["Component", "Purpose"], [
        ["Doctoral thesis seminar", "Presents and defends original research contributing new knowledge to geography"],
    ])},
    "geography-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Urban metabolism", "Analyzes a city's material and energy flows like a living organism's metabolism"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"geography-m2-l{base_n}"
    worked_key = f"geography-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Geography"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Geography: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Geography lessons.")


if __name__ == "__main__":
    main()
