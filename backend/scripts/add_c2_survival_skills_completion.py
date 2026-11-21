#!/usr/bin/env python3
"""Depth pass, C2 Survival Skills: fill in real, hand-checked data_table
content for the 69 C2 Survival Skills lessons not covered by the
earlier breadth-first batch. Brings C2 Survival Skills to full 70/70
coverage.

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "survival-skills-c2-l1": {
        "data_table": table(["Skill", "Feature"], [
            ["Wilderness first response", "Provides initial medical stabilization when professional care is far away"],
        ]),
    },
    "survival-skills-c2-l2": {
        "data_table": table(["Skill", "Feature"], [
            ["Navigation & resource management", "Combines route-finding with careful allocation of limited supplies"],
        ]),
    },
    "survival-skills-c2-l4": {
        "data_table": table(["Principle", "Detail"], [
            ["Survival kit design", "Prioritizes multi-use, lightweight items covering core survival priorities"],
        ]),
    },
    "survival-skills-c2-l5": {
        "data_table": table(["Method", "Detail"], [
            ["Water procurement", "Filtration, boiling, and chemical treatment each address different contaminants"],
        ]),
    },
    "survival-skills-c2-l6": {
        "data_table": table(["Element", "Requirement"], [
            ["Fire triangle", "Heat, fuel, and oxygen must all be present for combustion"],
        ]),
    },
    "survival-skills-c2-l7": {
        "data_table": table(["Principle", "Detail"], [
            ["Shelter engineering", "Minimizes heat loss through insulation and wind protection"],
        ]),
    },
    "survival-skills-c2-l8": {
        "data_table": table(["Method", "Detail"], [
            ["Celestial navigation", "Uses the sun, stars, or moon position to determine direction"],
            ["Magnetic navigation", "Uses a compass needle aligned with Earth's magnetic field"],
        ]),
    },
    "survival-skills-c2-l9": {
        "data_table": table(["Phase", "Task"], [
            ["Search and rescue", "Systematically narrows probable location before physical search"],
        ]),
    },
    "survival-skills-c2-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Disaster risk reduction", "Reduces vulnerability and exposure before a hazard event occurs"],
        ]),
    },
    "survival-skills-c2-l11": {
        "data_table": table(["Hazard", "Assessment Factor"], [
            ["Terrain hazard", "Slope, drainage, and rockfall exposure affect route safety"],
        ]),
    },
    "survival-skills-c2-l12": {
        "data_table": table(["Nutrient", "Priority in Survival"], [
            ["Carbohydrates", "Fast energy source, first depleted"],
            ["Fat", "Dense long-term energy reserve"],
        ]),
    },
    "survival-skills-c2-l13": {
        "data_table": table(["Condition", "Cause"], [
            ["Hypothermia", "Core body temperature drop from prolonged cold exposure"],
            ["Heat illness", "Overheating from exertion or high ambient temperature"],
        ]),
    },
    "survival-skills-c2-l14": {
        "data_table": table(["Principle", "Detail"], [
            ["Wilderness medicine", "Adapts standard medical protocols to remote, resource-limited settings"],
        ]),
    },
    "survival-skills-c2-l15": {
        "data_table": table(["Device", "Use"], [
            ["Satellite messenger", "Sends location and distress signals outside cellular coverage"],
        ]),
    },
    "survival-skills-c2-l16": {
        "data_table": table(["Element", "Purpose"], [
            ["Urban disaster plan", "Prepares households and communities for infrastructure disruption"],
        ]),
    },
    "survival-skills-c2-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Community resilience", "A community's capacity to absorb and recover from a disruptive event"],
        ]),
    },
    "survival-skills-c2-l18": {
        "data_table": table(["Method", "Purpose"], [
            ["Case study analysis", "Extracts practical lessons from documented real survival incidents"],
        ]),
    },
    "survival-skills-c2-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Risk assessment", "Identifies hazards and estimates likelihood and severity of harm"],
        ]),
    },
    "survival-skills-c2-l20": {
        "data_table": table(["Material", "Property"], [
            ["Ripstop nylon", "Lightweight fabric resistant to tear propagation"],
        ]),
    },
    "survival-skills-c2-l21": {
        "data_table": table(["System", "Use"], [
            ["Rope rescue rigging", "Provides mechanical advantage for lifting or lowering in technical rescue"],
        ]),
    },
    "survival-skills-c2-l22": {
        "data_table": table(["Technique", "Detail"], [
            ["Off-trail route finding", "Combines map, compass, and terrain reading without marked trails"],
        ]),
    },
    "survival-skills-c2-l23": {
        "data_table": table(["Tool", "Use"], [
            ["Satellite phone", "Enables voice/data communication independent of ground infrastructure"],
        ]),
    },
    "survival-skills-c2-l24": {
        "data_table": table(["Principle", "Detail"], [
            ["Wilderness ethics", "Minimizing group impact scales with party size and frequency of use"],
        ]),
    },
    "survival-skills-c2-l25": {
        "data_table": table(["Step", "Task"], [
            ["Expedition planning", "Sequences logistics, permits, resupply, and contingency planning"],
        ]),
    },
    "survival-skills-c2-l26": {
        "data_table": table(["Method", "Use"], [
            ["Signal mirror", "Reflects sunlight over long distances to attract rescuer attention"],
        ]),
    },
    "survival-skills-c2-l27": {
        "data_table": table(["Source", "Detail"], [
            ["Plant-based nutrition", "Requires careful species identification to avoid toxic look-alikes"],
        ]),
    },
    "survival-skills-c2-l28": {
        "data_table": table(["Practice", "Purpose"], [
            ["Sustainable foraging", "Limits harvest to preserve plant population and ecosystem balance"],
        ]),
    },
    "survival-skills-c2-l29": {
        "data_table": table(["System", "Consideration"], [
            ["Trapping regulation", "Legal use varies sharply by jurisdiction and species protection status"],
        ]),
    },
    "survival-skills-c2-l30": {
        "data_table": table(["Layer", "Function"], [
            ["Base layer", "Wicks moisture away from skin"],
            ["Insulating layer", "Traps warm air near the body"],
            ["Shell layer", "Blocks wind and precipitation"],
        ]),
    },
    "survival-skills-c2-l31": {
        "data_table": table(["Strategy", "Detail"], [
            ["Heat stress management", "Prioritizes hydration, pacing, and shade to prevent heat illness"],
        ]),
    },
    "survival-skills-c2-l32": {
        "data_table": table(["Method", "Mechanism"], [
            ["Chlorine dioxide treatment", "Oxidizes and inactivates pathogens in water"],
        ]),
    },
    "survival-skills-c2-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Controlled burn", "Deliberately set fire reduces fuel load to prevent larger wildfires"],
        ]),
    },
    "survival-skills-c2-l34": {
        "data_table": table(["Climate", "Shelter Priority"], [
            ["Arctic", "Maximize insulation and minimize wind exposure"],
            ["Desert", "Maximize shade and airflow while minimizing direct sun"],
        ]),
    },
    "survival-skills-c2-l35": {
        "data_table": table(["Method", "Purpose"], [
            ["Primary trauma survey", "Rapidly identifies immediately life-threatening injuries"],
        ]),
    },
    "survival-skills-c2-l36": {
        "data_table": table(["Practice", "Purpose"], [
            ["Wound irrigation", "Flushes contaminants to reduce infection risk in the field"],
        ]),
    },
    "survival-skills-c2-l37": {
        "data_table": table(["Strategy", "Detail"], [
            ["Wildlife conflict avoidance", "Proper food storage and noise discipline reduce dangerous encounters"],
        ]),
    },
    "survival-skills-c2-l38": {
        "data_table": table(["Toxin Type", "Effect"], [
            ["Hemotoxic venom", "Damages blood cells and tissue"],
            ["Neurotoxic venom", "Disrupts nerve signal transmission"],
        ]),
    },
    "survival-skills-c2-l39": {
        "data_table": table(["Factor", "Risk Indicator"], [
            ["Slope angle", "Avalanche risk rises sharply between roughly 30-45 degrees"],
        ]),
    },
    "survival-skills-c2-l40": {
        "data_table": table(["Technique", "Purpose"], [
            ["Swiftwater rescue", "Uses throw bags and positioning to safely reach a swimmer in current"],
        ]),
    },
    "survival-skills-c2-l41": {
        "data_table": table(["Factor", "Detail"], [
            ["Pack load management", "Weight distribution close to the back reduces strain and improves balance"],
        ]),
    },
    "survival-skills-c2-l42": {
        "data_table": table(["Mechanism", "Detail"], [
            ["Thermoregulation", "The body balances heat production and loss to maintain core temperature"],
        ]),
    },
    "survival-skills-c2-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Crisis decision-making", "Stress narrows attention, favoring simple, well-rehearsed procedures"],
        ]),
    },
    "survival-skills-c2-l44": {
        "data_table": table(["Skill", "Purpose"], [
            ["Crisis leadership", "Maintains group cohesion and clear task delegation under pressure"],
        ]),
    },
    "survival-skills-c2-l45": {
        "data_table": table(["Pattern", "Indicator"], [
            ["Cloud formation trends", "Signal approaching fronts and changing weather"],
        ]),
    },
    "survival-skills-c2-l46": {
        "data_table": table(["Trend", "Meaning"], [
            ["Falling barometric pressure", "Often signals an approaching storm system"],
        ]),
    },
    "survival-skills-c2-l47": {
        "data_table": table(["Material", "Use"], [
            ["Flint/stone", "Shaped into cutting edges for improvised tools"],
        ]),
    },
    "survival-skills-c2-l48": {
        "data_table": table(["Task", "Purpose"], [
            ["Edge maintenance", "Regular sharpening preserves tool effectiveness and safety"],
        ]),
    },
    "survival-skills-c2-l49": {
        "data_table": table(["Principle", "Detail"], [
            ["Shelter structural engineering", "Load distribution and bracing determine stability under weather stress"],
        ]),
    },
    "survival-skills-c2-l50": {
        "data_table": table(["Material", "R-Value Trait"], [
            ["Dry leaf litter", "Traps air pockets for effective natural insulation"],
        ]),
    },
    "survival-skills-c2-l51": {
        "data_table": table(["Method", "Mechanism"], [
            ["Drying", "Removes moisture to inhibit microbial growth"],
            ["Salting", "Draws out moisture and creates an inhospitable environment for bacteria"],
        ]),
    },
    "survival-skills-c2-l52": {
        "data_table": table(["System", "Detail"], [
            ["Long-term food storage", "Balances shelf life, nutrition, and rotation planning"],
        ]),
    },
    "survival-skills-c2-l53": {
        "data_table": table(["Function", "Role"], [
            ["Incident command", "Coordinates multiple response agencies under a unified structure"],
        ]),
    },
    "survival-skills-c2-l54": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Bug-out route", "Pre-planned evacuation path avoiding likely bottlenecks"],
        ]),
    },
    "survival-skills-c2-l55": {
        "data_table": table(["System", "Purpose"], [
            ["Household resilience system", "Backup power, water, and supplies sustain a household through disruption"],
        ]),
    },
    "survival-skills-c2-l56": {
        "data_table": table(["Resource", "Management Approach"], [
            ["Community emergency resources", "Shared inventories and mutual aid agreements extend limited supplies"],
        ]),
    },
    "survival-skills-c2-l57": {
        "data_table": table(["Component", "Purpose"], [
            ["Wilderness medical kit", "Tailored to trip duration, group size, and remoteness"],
        ]),
    },
    "survival-skills-c2-l58": {
        "data_table": table(["Task", "Purpose"], [
            ["Splinting", "Immobilizes a fracture to prevent further injury during evacuation"],
        ]),
    },
    "survival-skills-c2-l59": {
        "data_table": table(["Factor", "Consideration"], [
            ["Caloric planning", "Expedition length and exertion level determine daily caloric needs"],
        ]),
    },
    "survival-skills-c2-l60": {
        "data_table": table(["Material", "Property"], [
            ["Natural cordage", "Fiber twist direction and ply count determine tensile strength"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Survival Priority (Rule of 3s)", "Time Limit"], [
    ["Air", "3 minutes"],
    ["Shelter (extreme conditions)", "3 hours"],
    ["Water", "3 days"],
    ["Food", "3 weeks"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"survival-skills-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"survival-skills-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"survival-skills-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Survival Skills lessons (completing 70/70).")


if __name__ == "__main__":
    main()
