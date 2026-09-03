#!/usr/bin/env python3
"""Depth pass, M1 Survival Skills: fill in real, hand-checked
data_table content for the 99 M1 Survival Skills lessons not covered
by the earlier breadth-first batch. Brings M1 Survival Skills to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "survival-skills-m1-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Navigation & resource management", "Combines route-finding with careful allocation of limited supplies"],
        ]),
    },
    "survival-skills-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Expedition risk management", "Systematically identifies and mitigates hazards before and during travel"],
        ]),
    },
    "survival-skills-m1-l4": {
        "data_table": table(["Principle", "Detail"], [
            ["Survival kit design", "Prioritizes multi-use, lightweight items covering core survival priorities"],
        ]),
    },
    "survival-skills-m1-l5": {
        "data_table": table(["Method", "Detail"], [
            ["Water procurement science", "Filtration, boiling, and chemical treatment each address different contaminants"],
        ]),
    },
    "survival-skills-m1-l6": {
        "data_table": table(["Element", "Requirement"], [
            ["Fire triangle", "Heat, fuel, and oxygen must all be present for combustion"],
        ]),
    },
    "survival-skills-m1-l7": {
        "data_table": table(["Principle", "Detail"], [
            ["Shelter engineering", "Minimizes heat loss through insulation and wind protection"],
        ]),
    },
    "survival-skills-m1-l8": {
        "data_table": table(["Method", "Detail"], [
            ["Celestial navigation", "Uses the sun, stars, or moon position to determine direction"],
        ]),
    },
    "survival-skills-m1-l9": {
        "data_table": table(["Phase", "Task"], [
            ["Search and rescue", "Systematically narrows probable location before physical search"],
        ]),
    },
    "survival-skills-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Disaster risk reduction", "Reduces vulnerability and exposure before a hazard event occurs"],
        ]),
    },
    "survival-skills-m1-l11": {
        "data_table": table(["Hazard", "Assessment Factor"], [
            ["Terrain hazard", "Slope, drainage, and rockfall exposure affect route safety"],
        ]),
    },
    "survival-skills-m1-l12": {
        "data_table": table(["Nutrient", "Priority in Survival"], [
            ["Carbohydrates", "Fast energy source, first depleted"],
            ["Fat", "Dense long-term energy reserve"],
        ]),
    },
    "survival-skills-m1-l13": {
        "data_table": table(["Condition", "Cause"], [
            ["Hypothermia", "Core body temperature drop from prolonged cold exposure"],
            ["Heat illness", "Overheating from exertion or high ambient temperature"],
        ]),
    },
    "survival-skills-m1-l14": {
        "data_table": table(["Principle", "Detail"], [
            ["Wilderness medicine", "Adapts standard medical protocols to remote, resource-limited settings"],
        ]),
    },
    "survival-skills-m1-l15": {
        "data_table": table(["Device", "Use"], [
            ["Satellite messenger", "Sends location and distress signals outside cellular coverage"],
        ]),
    },
    "survival-skills-m1-l16": {
        "data_table": table(["Element", "Purpose"], [
            ["Urban disaster plan", "Prepares households and communities for infrastructure disruption"],
        ]),
    },
    "survival-skills-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Community resilience", "A community's capacity to absorb and recover from a disruptive event"],
        ]),
    },
    "survival-skills-m1-l18": {
        "data_table": table(["Method", "Purpose"], [
            ["Case study analysis", "Extracts practical lessons from documented real survival incidents"],
        ]),
    },
    "survival-skills-m1-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Risk assessment", "Identifies hazards and estimates likelihood and severity of harm"],
        ]),
    },
    "survival-skills-m1-l20": {
        "data_table": table(["Material", "Property"], [
            ["Ripstop nylon", "Lightweight fabric resistant to tear propagation"],
        ]),
    },
    "survival-skills-m1-l21": {
        "data_table": table(["Hazard", "Detail"], [
            ["Winter mountaineering hazard", "Combines cold exposure, avalanche risk, and terrain complexity"],
        ]),
    },
    "survival-skills-m1-l22": {
        "data_table": table(["Factor", "Risk Indicator"], [
            ["Slope angle", "Avalanche risk rises sharply between roughly 30-45 degrees"],
        ]),
    },
    "survival-skills-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Desert physiology", "Sweat rate and water loss accelerate rapidly under high heat and low humidity"],
        ]),
    },
    "survival-skills-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Jungle survival ecology", "High humidity and dense canopy complicate navigation, hydration, and wound care"],
        ]),
    },
    "survival-skills-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Maritime survival science", "Cold water immersion and dehydration are the primary open-water survival risks"],
        ]),
    },
    "survival-skills-m1-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Cold water immersion", "Cold shock response can trigger involuntary gasping within seconds of entry"],
        ]),
    },
    "survival-skills-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Acclimatization", "The body gradually adapts to reduced oxygen availability at high altitude"],
        ]),
    },
    "survival-skills-m1-l28": {
        "data_table": table(["Factor", "Effect"], [
            ["Wildland fire behavior", "Wind, fuel load, and slope steepness together determine fire spread rate"],
        ]),
    },
    "survival-skills-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Structural collapse rescue", "Requires careful assessment of void spaces and secondary collapse risk"],
        ]),
    },
    "survival-skills-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Confined space rescue", "Demands specialized air monitoring and extraction equipment"],
        ]),
    },
    "survival-skills-m1-l31": {
        "data_table": table(["Technique", "Detail"], [
            ["Swiftwater rescue", "Uses throw bags and positioning to safely reach a swimmer in current"],
        ]),
    },
    "survival-skills-m1-l32": {
        "data_table": table(["Category", "Meaning"], [
            ["Immediate", "Life-threatening injury requiring urgent treatment"],
            ["Delayed", "Serious injury that can safely wait for treatment"],
        ]),
    },
    "survival-skills-m1-l33": {
        "data_table": table(["Toxin Type", "Effect"], [
            ["Hemotoxic venom", "Damages blood cells and tissue"],
            ["Neurotoxic venom", "Disrupts nerve signal transmission"],
        ]),
    },
    "survival-skills-m1-l34": {
        "data_table": table(["Skill", "Detail"], [
            ["Edible plant identification", "Requires precise species-level knowledge to avoid dangerous look-alikes"],
        ]),
    },
    "survival-skills-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethnobotany", "Studies how cultures traditionally use plants for food, medicine, and materials"],
        ]),
    },
    "survival-skills-m1-l36": {
        "data_table": table(["Method", "Mechanism"], [
            ["Chlorine dioxide treatment", "Oxidizes and inactivates pathogens in water"],
        ]),
    },
    "survival-skills-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Solar still", "Uses evaporation and condensation to extract drinkable water from moist ground or plants"],
        ]),
    },
    "survival-skills-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Load-bearing rigging", "Knot selection and rope strength must match the expected load and failure mode"],
        ]),
    },
    "survival-skills-m1-l39": {
        "data_table": table(["Technique", "Detail"], [
            ["Terrain association", "Matches observed landscape features to a map without relying on instruments"],
        ]),
    },
    "survival-skills-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["GPS/GNSS", "Multiple satellite constellations now provide redundant global positioning"],
        ]),
    },
    "survival-skills-m1-l41": {
        "data_table": table(["Method", "Use"], [
            ["Signal mirror", "Reflects sunlight over long distances to attract rescuer attention"],
        ]),
    },
    "survival-skills-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Radio propagation", "Signal range varies with frequency, terrain, and atmospheric conditions"],
        ]),
    },
    "survival-skills-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Isolation psychology", "Prolonged confinement can produce measurable cognitive and emotional strain"],
        ]),
    },
    "survival-skills-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Group dynamics in crisis", "Clear roles and communication reduce conflict when resources are scarce"],
        ]),
    },
    "survival-skills-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Stress decision-making", "Acute stress narrows attention, favoring simple, well-rehearsed procedures"],
        ]),
    },
    "survival-skills-m1-l46": {
        "data_table": table(["Bias", "Detail"], [
            ["Normalcy bias", "Underestimating the likelihood or effect of a genuine emergency"],
        ]),
    },
    "survival-skills-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Sleep deprivation management", "Impaired judgment from fatigue can be as dangerous as physical hazards"],
        ]),
    },
    "survival-skills-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Extended expedition nutrition", "Balances caloric density against pack weight over multi-day travel"],
        ]),
    },
    "survival-skills-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Caloric deficit management", "The body prioritizes vital functions as sustained energy shortfall progresses"],
        ]),
    },
    "survival-skills-m1-l50": {
        "data_table": table(["Layer", "Function"], [
            ["Base layer", "Wicks moisture away from skin"],
            ["Shell layer", "Blocks wind and precipitation"],
        ]),
    },
    "survival-skills-m1-l51": {
        "data_table": table(["Material", "Property"], [
            ["Dry insulation", "Traps air pockets for effective thermal resistance"],
        ]),
    },
    "survival-skills-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Shelter thermodynamics", "Minimizing surface area and convective loss preserves interior heat"],
        ]),
    },
    "survival-skills-m1-l53": {
        "data_table": table(["Challenge", "Detail"], [
            ["Fire-starting in wet conditions", "Requires dry tinder preparation and moisture-resistant ignition sources"],
        ]),
    },
    "survival-skills-m1-l54": {
        "data_table": table(["Material", "Use"], [
            ["Flint/stone", "Shaped into cutting edges for improvised bushcraft tools"],
        ]),
    },
    "survival-skills-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethical wildlife procurement", "Balances survival need with regulation and minimizing unnecessary suffering"],
        ]),
    },
    "survival-skills-m1-l56": {
        "data_table": table(["Method", "Mechanism"], [
            ["Drying", "Removes moisture to inhibit microbial growth in field-preserved food"],
        ]),
    },
    "survival-skills-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Waterborne pathogen risk", "Untreated natural water sources can carry bacteria, viruses, and parasites"],
        ]),
    },
    "survival-skills-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Zoonotic disease risk", "Wildlife contact can transmit disease directly to humans in the field"],
        ]),
    },
    "survival-skills-m1-l59": {
        "data_table": table(["Practice", "Purpose"], [
            ["Field sanitation", "Proper waste disposal reduces disease transmission risk in group settings"],
        ]),
    },
    "survival-skills-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Wilderness first responder protocol", "Extends standard first aid for delayed evacuation scenarios"],
        ]),
    },
    "survival-skills-m1-l61": {
        "data_table": table(["Category", "Criteria"], [
            ["START triage", "Sorts patients rapidly using respiration, perfusion, and mental status"],
        ]),
    },
    "survival-skills-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Earthquake preparedness engineering", "Retrofitting structures reduces collapse risk during seismic events"],
        ]),
    },
    "survival-skills-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Flood evacuation planning", "Pre-identified routes and timing thresholds guide safe evacuation decisions"],
        ]),
    },
    "survival-skills-m1-l64": {
        "data_table": table(["System", "Purpose"], [
            ["Tsunami warning system", "Detects seismic activity to provide early alert before wave arrival"],
        ]),
    },
    "survival-skills-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Hurricane preparedness", "Categorization scales guide the intensity of evacuation and shelter response"],
        ]),
    },
    "survival-skills-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Wildfire evacuation planning", "Requires pre-designated routes given fire's unpredictable spread rate"],
        ]),
    },
    "survival-skills-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Volcanic hazard preparedness", "Monitors precursor signs like seismicity and gas emission for early warning"],
        ]),
    },
    "survival-skills-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Radiological emergency preparedness", "Combines shielding, distance, and time to minimize radiation exposure"],
        ]),
    },
    "survival-skills-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Hazmat response basics", "Identifying the hazard class first determines the appropriate response protocol"],
        ]),
    },
    "survival-skills-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Pandemic logistics planning", "Requires stockpiling, isolation protocols, and supply chain contingency"],
        ]),
    },
    "survival-skills-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Long-term food security planning", "Balances storage life, nutrition, and rotation for sustained crisis periods"],
        ]),
    },
    "survival-skills-m1-l72": {
        "data_table": table(["System", "Detail"], [
            ["Off-grid energy system", "Combines generation and storage to provide power independent of the grid"],
        ]),
    },
    "survival-skills-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Water storage rotation", "Regular rotation prevents stagnation and maintains a usable emergency supply"],
        ]),
    },
    "survival-skills-m1-l74": {
        "data_table": table(["Factor", "Detail"], [
            ["Pack load management", "Weight distribution close to the back reduces strain and improves balance"],
        ]),
    },
    "survival-skills-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Vehicle-based preparedness", "Stocks essential survival supplies accessible during a roadside emergency"],
        ]),
    },
    "survival-skills-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Urban foraging ethics", "Balances resource need with legal and community considerations"],
        ]),
    },
    "survival-skills-m1-l77": {
        "data_table": table(["Concept", "Detail"], [
            ["Barter economics", "Direct goods exchange often replaces currency when formal markets collapse"],
        ]),
    },
    "survival-skills-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Mutual aid network design", "Coordinates shared resources and skills across a resilient community"],
        ]),
    },
    "survival-skills-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Communication protocol", "Standardized codes ensure clarity when normal channels are disrupted"],
        ]),
    },
    "survival-skills-m1-l80": {
        "data_table": table(["Method", "Detail"], [
            ["Instrument-free navigation", "Uses sun position, stars, and terrain features to maintain direction"],
        ]),
    },
    "survival-skills-m1-l81": {
        "data_table": table(["Technique", "Purpose"], [
            ["Map and compass triangulation", "Determines precise position from bearings to multiple known landmarks"],
        ]),
    },
    "survival-skills-m1-l82": {
        "data_table": table(["Pattern", "Indicator"], [
            ["Cloud formation trend", "Signals approaching fronts and changing weather"],
        ]),
    },
    "survival-skills-m1-l83": {
        "data_table": table(["Cloud Type", "Signal"], [
            ["Cumulonimbus", "Indicates severe weather including thunderstorms"],
        ]),
    },
    "survival-skills-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Animal behavior indicators", "Unusual wildlife activity can precede seismic or weather events"],
        ]),
    },
    "survival-skills-m1-l85": {
        "data_table": table(["Strategy", "Detail"], [
            ["Predator encounter management", "Proper food storage and noise discipline reduce dangerous encounters"],
        ]),
    },
    "survival-skills-m1-l86": {
        "data_table": table(["System", "Use"], [
            ["Rappel/belay system", "Provides controlled, protected descent or fall arrest on technical terrain"],
        ]),
    },
    "survival-skills-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Ice/snow travel safety", "Requires assessing surface stability before crossing frozen terrain"],
        ]),
    },
    "survival-skills-m1-l88": {
        "data_table": table(["Concept", "Detail"], [
            ["River crossing risk assessment", "Evaluates current speed, depth, and footing before attempting a crossing"],
        ]),
    },
    "survival-skills-m1-l89": {
        "data_table": table(["Concept", "Detail"], [
            ["Lightning safety", "The 30-30 rule guides when to seek shelter and when it is safe to resume activity"],
        ]),
    },
    "survival-skills-m1-l90": {
        "data_table": table(["Strategy", "Detail"], [
            ["Heat stress management", "Prioritizes hydration, pacing, and shade to prevent heat illness"],
        ]),
    },
    "survival-skills-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Frostbite pathophysiology", "Ice crystal formation damages tissue as extremities lose blood flow"],
        ]),
    },
    "survival-skills-m1-l92": {
        "data_table": table(["Practice", "Purpose"], [
            ["Wound irrigation", "Flushes contaminants to reduce infection risk in the field"],
        ]),
    },
    "survival-skills-m1-l93": {
        "data_table": table(["Technique", "Purpose"], [
            ["Improvised splinting", "Immobilizes a suspected fracture using available field materials"],
        ]),
    },
    "survival-skills-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Psychological first aid", "Provides immediate emotional stabilization following a disaster event"],
        ]),
    },
    "survival-skills-m1-l95": {
        "data_table": table(["Pattern", "Use"], [
            ["Grid search pattern", "Systematically covers an area to maximize the probability of locating a missing person"],
        ]),
    },
    "survival-skills-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Canine search coordination", "Handler and dog teams require synchronized training and search protocol"],
        ]),
    },
    "survival-skills-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Drone-assisted search", "Aerial imaging extends search coverage in difficult or dangerous terrain"],
        ]),
    },
    "survival-skills-m1-l98": {
        "data_table": table(["Method", "Purpose"], [
            ["Field equipment evaluation", "Tests gear under realistic conditions rather than only manufacturer claims"],
        ]),
    },
    "survival-skills-m1-l99": {
        "data_table": table(["Case", "Lesson"], [
            ["Historical polar expedition", "Documented survival and failure cases reveal recurring decision-making patterns"],
        ]),
    },
    "survival-skills-m1-l100": {
        "data_table": table(["Principle", "Detail"], [
            ["Leave No Trace", "Minimizing impact scales with group size and frequency of wilderness use"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Survival Priority (Rule of 3s)", "Time Limit"], [
        ["Air", "3 minutes"],
        ["Shelter (extreme conditions)", "3 hours"],
        ["Water", "3 days"],
        ["Food", "3 weeks"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"survival-skills-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"survival-skills-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"survival-skills-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Survival Skills lessons (completing 120/120).")


if __name__ == "__main__":
    main()
