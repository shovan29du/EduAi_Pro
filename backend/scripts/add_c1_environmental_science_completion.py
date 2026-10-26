#!/usr/bin/env python3
"""Depth pass, C1 Environmental Science: fill in real, hand-checked
data_table content for the 99 C1 Environmental Science lessons not
covered by the earlier breadth-first batch. Brings C1 Environmental
Science to full 100/100 coverage.

Note: this subject has 100 lessons structured as 20 topics x 5 modes:
l1-20 Conceptual Foundations, l21-40 Worked Analysis, l41-60 Evidence
and Data, l61-80 Comparative Case Study, l81-100 Applied Research
Seminar (topic N maps to lessons N, N+20, N+40, N+60, N+80).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_environmental_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


TOPICS: list[dict] = [
    {  # 1
        "name": "Earth Systems",
        "foundations": table(["Sphere", "Meaning"], [["Lithosphere", "The solid outer layer of Earth"], ["Hydrosphere", "All water on Earth's surface and atmosphere"]]),
        "worked": table(["Interaction", "Example"], [["Sphere interaction", "Volcanic eruptions release gases into the atmosphere"]]),
        "evidence": table(["Metric", "Insight"], [["Global temperature record", "Shows long-term shifts in Earth's climate system"]]),
        "case_study": table(["Event", "Insight"], [["Mount Pinatubo eruption", "Temporarily cooled global temperatures via aerosol release"]]),
        "seminar": table(["Step", "Focus"], [["Tracing a sphere interaction", "Documenting how one Earth system affects another in a real event"]]),
    },
    {  # 2
        "name": "Ecosystem Dynamics",
        "foundations": table(["Term", "Meaning"], [["Ecosystem", "A community of organisms interacting with their physical environment"]]),
        "worked": table(["Concept", "Example"], [["Trophic cascade", "Removing a top predator can reshape an entire food web"]]),
        "evidence": table(["Metric", "Insight"], [["Species population trends", "Reveal ecosystem health or stress over time"]]),
        "case_study": table(["Case", "Insight"], [["Yellowstone wolves", "Reintroduction triggered a well-documented trophic cascade"]]),
        "seminar": table(["Step", "Focus"], [["Researching a real trophic cascade", "Tracing effects through multiple levels of a food web"]]),
    },
    {  # 3
        "name": "Biodiversity",
        "foundations": table(["Term", "Meaning"], [["Biodiversity", "The variety of life at genetic, species, and ecosystem levels"]]),
        "worked": table(["Step", "Example"], [["Measuring diversity", "Comparing species richness across two habitats"]]),
        "evidence": table(["Metric", "Insight"], [["IUCN Red List status", "Tracks species at risk of extinction globally"]]),
        "case_study": table(["Region", "Insight"], [["Coral Triangle", "One of the world's most biodiverse marine regions"]]),
        "seminar": table(["Step", "Focus"], [["Assessing a local biodiversity survey", "Comparing species counts against historical baselines"]]),
    },
    {  # 4
        "name": "Biogeochemical Cycles",
        "foundations": table(["Cycle", "Key Process"], [["Carbon cycle", "Carbon moves between atmosphere, biosphere, and oceans"], ["Nitrogen cycle", "Nitrogen fixation converts atmospheric nitrogen to usable forms"]]),
        "worked": table(["Step", "Example"], [["Tracing carbon flow", "Following carbon from fossil fuel combustion into the atmosphere"]]),
        "evidence": table(["Metric", "Insight"], [["Atmospheric CO2 concentration", "Has risen sharply since industrialization"]]),
        "case_study": table(["Case", "Insight"], [["Keeling Curve", "Decades of direct CO2 measurement at Mauna Loa"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing Keeling Curve data", "Identifying seasonal and long-term CO2 trends"]]),
    },
    {  # 5
        "name": "Climate Science",
        "foundations": table(["Term", "Meaning"], [["Greenhouse effect", "Gases trap heat, warming the Earth's surface"]]),
        "worked": table(["Step", "Example"], [["Attributing warming", "Comparing modeled natural versus human-driven temperature trends"]]),
        "evidence": table(["Metric", "Insight"], [["Global average temperature anomaly", "Tracks warming relative to a historical baseline"]]),
        "case_study": table(["Report", "Insight"], [["IPCC assessment reports", "Synthesize global climate science for policymakers"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing an IPCC summary", "Extracting key findings on projected climate impacts"]]),
    },
    {  # 6
        "name": "Atmospheric Pollution",
        "foundations": table(["Pollutant", "Source"], [["Particulate matter", "Vehicle emissions and industrial combustion"], ["Ground-level ozone", "Formed by reactions between pollutants and sunlight"]]),
        "worked": table(["Step", "Example"], [["Reading an air quality index", "Interpreting pollutant levels against health thresholds"]]),
        "evidence": table(["Metric", "Insight"], [["PM2.5 concentration data", "Links directly to respiratory health outcomes"]]),
        "case_study": table(["Event", "Insight"], [["London Great Smog of 1952", "Led to modern clean air legislation"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing local air quality data", "Comparing pollution trends before and after a policy change"]]),
    },
    {  # 7
        "name": "Freshwater Systems",
        "foundations": table(["Term", "Meaning"], [["Watershed", "An area of land that drains into a common water body"]]),
        "worked": table(["Step", "Example"], [["Assessing water stress", "Comparing water demand against available supply"]]),
        "evidence": table(["Metric", "Insight"], [["Groundwater depletion rate", "Signals unsustainable freshwater use"]]),
        "case_study": table(["Case", "Insight"], [["Aral Sea", "Irrigation diversion caused near-total desiccation"]]),
        "seminar": table(["Step", "Focus"], [["Researching a watershed", "Mapping its water sources and major stressors"]]),
    },
    {  # 8
        "name": "Ocean Change",
        "foundations": table(["Term", "Meaning"], [["Ocean acidification", "Seawater pH decline from absorbing excess CO2"]]),
        "worked": table(["Step", "Example"], [["Linking cause and effect", "Connecting rising CO2 emissions to coral bleaching events"]]),
        "evidence": table(["Metric", "Insight"], [["Sea surface temperature trend", "Tracks ocean warming over recent decades"]]),
        "case_study": table(["Case", "Insight"], [["Great Barrier Reef bleaching", "Repeated mass bleaching linked to marine heatwaves"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing coral bleaching data", "Correlating bleaching events with temperature spikes"]]),
    },
    {  # 9
        "name": "Soil and Agriculture",
        "foundations": table(["Term", "Meaning"], [["Soil erosion", "The loss of topsoil through wind, water, or poor land use"]]),
        "worked": table(["Practice", "Effect"], [["Crop rotation", "Reduces soil nutrient depletion over time"]]),
        "evidence": table(["Metric", "Insight"], [["Soil organic matter content", "Indicates long-term soil fertility and health"]]),
        "case_study": table(["Event", "Insight"], [["Dust Bowl", "Poor farming practices caused catastrophic 1930s US soil erosion"]]),
        "seminar": table(["Step", "Focus"], [["Comparing farming practices", "Assessing soil health under conventional versus regenerative methods"]]),
    },
    {  # 10
        "name": "Forestry",
        "foundations": table(["Term", "Meaning"], [["Deforestation", "The permanent removal of forest cover for other land use"]]),
        "worked": table(["Step", "Example"], [["Measuring forest loss", "Comparing satellite imagery across two time periods"]]),
        "evidence": table(["Metric", "Insight"], [["Global forest cover loss data", "Tracks annual deforestation rates by region"]]),
        "case_study": table(["Region", "Insight"], [["Amazon rainforest", "Faces ongoing deforestation pressure from agriculture"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing satellite forest data", "Quantifying forest loss in a specific region over time"]]),
    },
    {  # 11
        "name": "Energy Systems",
        "foundations": table(["Source", "Type"], [["Solar", "Renewable"], ["Coal", "Non-renewable"]]),
        "worked": table(["Step", "Example"], [["Comparing energy sources", "Weighing cost, emissions, and reliability of two power sources"]]),
        "evidence": table(["Metric", "Insight"], [["Renewable energy share of grid", "Tracks a region's progress toward clean energy"]]),
        "case_study": table(["Country", "Approach"], [["Denmark", "High share of wind power in national electricity generation"]]),
        "seminar": table(["Step", "Focus"], [["Comparing two national energy grids", "Assessing renewable share and reliability trade-offs"]]),
    },
    {  # 12
        "name": "Waste and Circularity",
        "foundations": table(["Term", "Meaning"], [["Circular economy", "A model minimizing waste by reusing and recycling materials"]]),
        "worked": table(["Step", "Example"], [["Applying the waste hierarchy", "Prioritizing reduction and reuse over disposal"]]),
        "evidence": table(["Metric", "Insight"], [["Municipal recycling rate", "Reflects how effectively a region diverts waste from landfills"]]),
        "case_study": table(["Country", "Approach"], [["Sweden", "Advanced waste-to-energy and recycling infrastructure"]]),
        "seminar": table(["Step", "Focus"], [["Auditing a household's waste stream", "Categorizing and quantifying recyclable versus landfill waste"]]),
    },
    {  # 13
        "name": "Toxicology",
        "foundations": table(["Term", "Meaning"], [["Bioaccumulation", "A toxin building up in an organism faster than it's excreted"]]),
        "worked": table(["Step", "Example"], [["Tracing biomagnification", "Following a pollutant's rising concentration up a food chain"]]),
        "evidence": table(["Metric", "Insight"], [["Contaminant concentration data", "Reveals exposure risk across a population"]]),
        "case_study": table(["Case", "Insight"], [["DDT and bird populations", "Biomagnification thinned eggshells, crashing raptor populations"]]),
        "seminar": table(["Step", "Focus"], [["Researching a real contaminant case", "Tracing its biomagnification through a food chain"]]),
    },
    {  # 14
        "name": "Environmental Health",
        "foundations": table(["Term", "Meaning"], [["Environmental health", "The study of how environmental factors affect human health"]]),
        "worked": table(["Step", "Example"], [["Linking exposure to outcome", "Connecting industrial pollution to elevated local illness rates"]]),
        "evidence": table(["Metric", "Insight"], [["Disease incidence near pollution sources", "Reveals environmental health disparities"]]),
        "case_study": table(["Case", "Insight"], [["Flint water crisis", "Lead contamination caused a serious public health emergency"]]),
        "seminar": table(["Step", "Focus"], [["Researching an environmental health case", "Tracing the exposure pathway to health outcomes"]]),
    },
    {  # 15
        "name": "Conservation Biology",
        "foundations": table(["Term", "Meaning"], [["Conservation biology", "The science of protecting and restoring biodiversity"]]),
        "worked": table(["Strategy", "Example"], [["Protected area designation", "Legally shields habitat from development"]]),
        "evidence": table(["Metric", "Insight"], [["Population recovery data", "Measures success of a conservation intervention"]]),
        "case_study": table(["Case", "Insight"], [["Bald eagle recovery", "DDT ban and habitat protection reversed population decline"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a species recovery program", "Assessing which interventions drove measured recovery"]]),
    },
    {  # 16
        "name": "Urban Ecology",
        "foundations": table(["Term", "Meaning"], [["Urban heat island", "Cities experience higher temperatures than surrounding rural areas"]]),
        "worked": table(["Step", "Example"], [["Mitigating heat", "Adding green roofs and tree cover to reduce urban temperatures"]]),
        "evidence": table(["Metric", "Insight"], [["Urban tree canopy coverage", "Correlates with reduced local temperature and pollution"]]),
        "case_study": table(["City", "Approach"], [["Singapore", "Extensive urban greening as a core planning strategy"]]),
        "seminar": table(["Step", "Focus"], [["Mapping a city's green space", "Comparing tree canopy across different neighborhoods"]]),
    },
    {  # 17
        "name": "Environmental Economics",
        "foundations": table(["Term", "Meaning"], [["Externality", "A cost or benefit affecting a party who didn't choose to incur it"]]),
        "worked": table(["Tool", "Example"], [["Carbon pricing", "Assigns a cost to emitting carbon to account for its externality"]]),
        "evidence": table(["Metric", "Insight"], [["Cost of environmental damage estimates", "Informs policy trade-off decisions"]]),
        "case_study": table(["Policy", "Insight"], [["EU Emissions Trading System", "A large-scale cap-and-trade carbon market"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a carbon pricing policy", "Assessing its effect on emissions and economic activity"]]),
    },
    {  # 18
        "name": "Environmental Law",
        "foundations": table(["Term", "Meaning"], [["Environmental law", "Legal rules regulating human interaction with the environment"]]),
        "worked": table(["Law", "Purpose"], [["Clean Air Act", "Regulates air pollutant emissions in the United States"]]),
        "evidence": table(["Metric", "Insight"], [["Enforcement action data", "Shows how actively environmental laws are applied"]]),
        "case_study": table(["Case", "Insight"], [["Landmark pollution lawsuit", "Set precedent for corporate environmental liability"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing a real environmental case", "Identifying the legal basis for the ruling"]]),
    },
    {  # 19
        "name": "Climate Adaptation",
        "foundations": table(["Term", "Meaning"], [["Climate adaptation", "Adjusting systems to reduce harm from a changing climate"]]),
        "worked": table(["Strategy", "Example"], [["Sea wall construction", "Protects coastal infrastructure from rising seas"]]),
        "evidence": table(["Metric", "Insight"], [["Sea level rise projections", "Guide long-term coastal adaptation planning"]]),
        "case_study": table(["Country", "Approach"], [["Netherlands", "Extensive flood defense and water management systems"]]),
        "seminar": table(["Step", "Focus"], [["Researching a real adaptation project", "Assessing its design against local climate risks"]]),
    },
    {  # 20
        "name": "Sustainability Transitions",
        "foundations": table(["Term", "Meaning"], [["Just transition", "Shifting to sustainability while protecting affected workers and communities"]]),
        "worked": table(["Step", "Example"], [["Planning a transition", "Retraining fossil fuel workers for renewable energy jobs"]]),
        "evidence": table(["Metric", "Insight"], [["Green jobs growth data", "Tracks employment shifts toward sustainable industries"]]),
        "case_study": table(["Region", "Approach"], [["Germany's Energiewende", "A large-scale national shift toward renewable energy"]]),
        "seminar": table(["Step", "Focus"], [["Evaluating a real energy transition", "Assessing its economic and social impact on affected workers"]]),
    },
]

MODE_TO_OFFSET = {
    "foundations": 0,
    "worked": 20,
    "evidence": 40,
    "case_study": 60,
    "seminar": 80,
}

CHARTS: dict[str, dict] = {}
for idx, topic in enumerate(TOPICS, start=1):
    for mode, offset in MODE_TO_OFFSET.items():
        lesson_num = idx + offset
        lesson_id = f"environmental-science-c1-l{lesson_num}"
        CHARTS[lesson_id] = {"data_table": topic[mode]}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Environmental Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Environmental Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Environmental Science lessons (completing 100/100).")


if __name__ == "__main__":
    main()
