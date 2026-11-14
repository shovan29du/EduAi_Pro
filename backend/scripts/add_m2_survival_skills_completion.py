#!/usr/bin/env python3
"""Depth pass, M2 Survival Skills: fill in real, hand-checked
data_table content for the M2 Survival Skills lessons not covered by
the earlier breadth-first batch. Brings M2 Survival Skills to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
wilderness/expedition medicine, technical rescue systems, disaster
response and epidemiology, and applied survival science; l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Search and rescue coordination", "Organizes personnel, resources, and search strategy across a wilderness rescue operation"],
    ["Incident command", "A standardized structure for managing large-scale rescue and emergency response"],
])

CHARTS: dict[str, dict] = {
    "survival-skills-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Expedition risk management research", "Systematic methods for assessing and mitigating risk in extended wilderness expeditions"],
    ])},
    "survival-skills-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Outdoor safety fundamentals research", "Rigorous study of core principles underlying safe wilderness practice"],
    ])},
    "survival-skills-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Austere trauma life support", "Adapts trauma care protocols for settings with limited resources and delayed evacuation"],
    ])},
    "survival-skills-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["High-altitude physiology", "Studies how reduced oxygen availability affects the body and requires acclimatization management"],
    ])},
    "survival-skills-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Cold injury management", "Diagnoses and treats frostbite and hypothermia in polar expedition conditions"],
    ])},
    "survival-skills-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Avalanche terrain risk modeling", "Quantifies slope, snowpack, and weather factors to assess avalanche danger"],
    ])},
    "survival-skills-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Swiftwater rescue engineering", "Designs rope and equipment systems for safely rescuing people from fast-moving water"],
    ])},
    "survival-skills-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness toxicology", "Manages field treatment of envenomation and poisoning in remote settings"],
    ])},
    "survival-skills-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Disaster epidemiology", "Tracks disease patterns and health surveillance data during disaster response"],
    ])},
    "survival-skills-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Mass casualty triage (austere)", "Prioritizes limited medical resources across many casualties in resource-poor settings"],
    ])},
    "survival-skills-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Isolation psychology", "Studies how extended isolation affects individual and team mental functioning"],
    ])},
    "survival-skills-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Starvation/refeeding physiology", "Manages the metabolic risks of reintroducing food after prolonged starvation"],
    ])},
    "survival-skills-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Primitive iron smelting", "Bushcraft technique for extracting usable metal from ore using basic furnace methods"],
    ])},
    "survival-skills-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Celestial navigation", "Determines position and direction using the sun, stars, and moon without instruments"],
    ])},
    "survival-skills-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Desert water procurement", "Engineering techniques for extracting and conserving water in arid environments"],
    ])},
    "survival-skills-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Life raft group dynamics", "Manages resource rationing and psychological cohesion among survivors at sea"],
    ])},
    "survival-skills-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Jungle pathogen management", "Addresses the elevated disease and parasite risks specific to tropical survival settings"],
    ])},
    "survival-skills-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Fire ecology (wildland survival)", "Applies fire behavior science to survival decisions in fire-prone wildland areas"],
    ])},
    "survival-skills-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Cave rescue rope systems", "Technical rigging techniques for extracting injured people from cave environments"],
    ])},
    "survival-skills-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Structural collapse search and rescue", "Techniques for locating and extracting victims from collapsed buildings"],
    ])},
    "survival-skills-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Field debridement", "Removes dead or contaminated tissue from wounds to prevent infection in wilderness settings"],
    ])},
    "survival-skills-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Cold-water immersion timing", "Determines survival windows and rescue timing based on water temperature physiology"],
    ])},
    "survival-skills-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Terrain association navigation", "Uses landscape features rather than precise instruments to maintain position awareness"],
    ])},
    "survival-skills-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Shelter thermodynamics", "Applies heat transfer principles to design emergency shelters that conserve body heat"],
    ])},
    "survival-skills-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Water treatment log reduction", "Measures how effectively a water treatment method reduces pathogen concentration"],
    ])},
    "survival-skills-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Macronutrient prioritization", "Decides which nutrients to prioritize consuming when food is severely limited"],
    ])},
    "survival-skills-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["High-angle rescue rigging", "Sets up rope systems to safely lower or raise a patient on steep technical terrain"],
    ])},
    "survival-skills-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Evacuation decision algorithm", "A structured framework for deciding whether and how urgently to evacuate a patient"],
    ])},
    "survival-skills-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["TCCC principles (civilian adaptation)", "Applies combat casualty care lessons to civilian wilderness trauma medicine"],
    ])},
    "survival-skills-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Rescue load knot theory", "Analyzes knot strength and reliability for load-bearing rescue applications"],
    ])},
    "survival-skills-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Sea survival craft stability", "Engineering principles governing the design and stability of survival rafts"],
    ])},
    "survival-skills-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Volcanic hazard evacuation planning", "Plans evacuation routes and timing based on volcanic hazard zones"],
    ])},
    "survival-skills-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Field forensic anthropology", "Identifies disaster victims using skeletal and biological evidence in field conditions"],
    ])},
    "survival-skills-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Field formulary design", "Selects and organizes essential medications for wilderness medical practice"],
    ])},
    "survival-skills-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Remote telemedicine", "Connects expedition medics with distant physicians for real-time clinical guidance"],
    ])},
    "survival-skills-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Psychological first aid (disaster)", "Provides safety, comfort, and connection to survivors after a traumatic event"],
    ])},
    "survival-skills-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Thin-ice self-rescue", "Techniques for extracting oneself or others after falling through weak ice"],
    ])},
    "survival-skills-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Fire shelter deployment", "Emergency protective equipment and technique used when trapped by an advancing wildfire"],
    ])},
    "survival-skills-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Traditional ecological knowledge", "Indigenous accumulated environmental knowledge applied to modern survival practice"],
    ])},
    "survival-skills-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Field water balance modeling", "Estimates hydration needs and water loss rates in extreme environments"],
    ])},
    "survival-skills-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Micro-navigation", "Precise short-range navigation techniques for low-visibility terrain"],
    ])},
    "survival-skills-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Survival kit redundancy design", "Structures survival gear systems with backup capability for critical functions"],
    ])},
    "survival-skills-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Post-disaster water/sanitation engineering", "Rapidly restores safe water and waste management after a disaster"],
    ])},
    "survival-skills-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Fracture/dislocation reduction", "Field techniques for realigning broken bones or dislocated joints"],
    ])},
    "survival-skills-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["High-consequence weather forecasting", "Predicts severe weather events specifically relevant to expedition safety planning"],
    ])},
    "survival-skills-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Fire-by-friction thermodynamics", "Analyzes the heat generation physics underlying primitive friction fire-starting methods"],
    ])},
    "survival-skills-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Group decision-making under stress", "Studies how extreme stress affects collective survival decision quality"],
    ])},
    "survival-skills-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Search dog scent theory", "Applies canine scent detection science to wilderness search operations"],
    ])},
    "survival-skills-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Field traction splinting", "Advanced techniques for stabilizing long bone fractures with traction devices"],
    ])},
    "survival-skills-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Detection probability (signaling)", "Estimates how likely a rescue signal is to be seen given method and conditions"],
    ])},
    "survival-skills-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness anaphylaxis management", "Field protocols for treating severe allergic reactions with limited resources"],
    ])},
    "survival-skills-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Heat illness continuum", "Manages progression from heat exhaustion to life-threatening heat stroke"],
    ])},
    "survival-skills-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Polar expedition decision failure", "Analyzes historical case studies of fatal decision errors in polar exploration"],
    ])},
    "survival-skills-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["River crossing engineering", "Techniques for building rafts or bridges to safely cross bodies of water"],
    ])},
    "survival-skills-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Field outbreak investigation", "Methods for identifying the source and controlling spread of a disease outbreak"],
    ])},
    "survival-skills-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Unexploded ordnance awareness", "Identifies and avoids hazards from land mines and unexploded munitions"],
    ])},
    "survival-skills-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness dental emergencies", "Field management of dental trauma and pain when professional care is unavailable"],
    ])},
    "survival-skills-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Psychological adaptation to crisis", "Describes the stages people go through psychologically when adapting to survival crises"],
    ])},
    "survival-skills-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Rope access (vertical terrain)", "Advanced techniques for safely ascending and descending steep survival terrain"],
    ])},
    "survival-skills-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Field blood product alternatives", "Manages severe hemorrhage when standard blood products are unavailable"],
    ])},
    "survival-skills-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Search area probability mapping", "Statistically models the most likely location of a missing person"],
    ])},
    "survival-skills-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Survival trapping engineering", "Designs effective snares and traps for procuring food in survival scenarios"],
    ])},
    "survival-skills-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Extreme cold field surgery", "Addresses the physiological limits of performing emergency surgery in freezing conditions"],
    ])},
    "survival-skills-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Disaster supply chain resilience", "Models how relief supply chains withstand and recover from disruption"],
    ])},
    "survival-skills-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Snakebite antivenom logistics", "Manages the supply chain challenges of delivering antivenom in remote areas"],
    ])},
    "survival-skills-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Field radio communications", "Designs reliable communication systems for coordinating remote operations"],
    ])},
    "survival-skills-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Survivalist agroecology", "Rapid food production techniques for sustained survival scenarios"],
    ])},
    "survival-skills-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness burn management", "Advanced field treatment protocols for burn injuries away from hospital care"],
    ])},
    "survival-skills-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Shipwreck survival case analysis", "Studies historical shipwreck survival outcomes to identify success factors"],
    ])},
    "survival-skills-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Crevasse rescue systems", "Rope and pulley techniques for extracting a climber fallen into a glacier crevasse"],
    ])},
    "survival-skills-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Field triage documentation", "Systems for tracking casualty status and treatment during mass casualty events"],
    ])},
    "survival-skills-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Altitude cognitive degradation", "Studies how low oxygen at extreme altitude impairs decision-making ability"],
    ])},
    "survival-skills-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Water crossing hazard assessment", "Evaluates the risk of crossing a body of water given current and depth"],
    ])},
    "survival-skills-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Field-expedient tool fabrication", "Creates functional tools from available materials in survival scenarios"],
    ])},
    "survival-skills-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Disaster shelter camp public health", "Designs shelter camps to minimize disease spread among displaced populations"],
    ])},
    "survival-skills-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness spinal injury protocols", "Field assessment protocols to determine when spinal immobilization is needed"],
    ])},
    "survival-skills-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Field-expedient desalination", "Improvised techniques for removing salt from seawater in survival settings"],
    ])},
    "survival-skills-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Storm cellar/blast shelter engineering", "Designs protective structures for severe weather and blast events"],
    ])},
    "survival-skills-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Toxic plant identification", "Systematic methods for distinguishing edible from poisonous wild plants"],
    ])},
    "survival-skills-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Anesthesia-free pain management", "Field techniques for managing procedural pain without medical anesthesia"],
    ])},
    "survival-skills-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Interagency disaster coordination", "Frameworks for coordinating multiple response agencies during a disaster"],
    ])},
    "survival-skills-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Underwater cave diving protocols", "Advanced survival and safety protocols specific to cave diving hazards"],
    ])},
    "survival-skills-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Field antibiotic stewardship", "Responsibly manages limited antibiotic supplies in austere medical care"],
    ])},
    "survival-skills-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Camouflage and evasion", "Techniques for remaining undetected in survival or tactical scenarios"],
    ])},
    "survival-skills-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Hypothermia rewarming protocols", "Field methods for safely restoring core body temperature in severe hypothermia"],
    ])},
    "survival-skills-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Landslide geotechnical assessment", "Field evaluation methods for identifying landslide risk terrain"],
    ])},
    "survival-skills-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Free-diving blackout prevention", "Physiological principles for avoiding shallow-water blackout while free-diving"],
    ])},
    "survival-skills-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Long-shelf-life ration engineering", "Designs nutritionally complete rations that remain stable for extended storage"],
    ])},
    "survival-skills-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Snow blindness management", "Field treatment for temporary vision loss caused by UV exposure on snow"],
    ])},
    "survival-skills-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Field-expedient power generation", "Improvised methods for generating electricity in remote survival camps"],
    ])},
    "survival-skills-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Rescue helicopter hoist operations", "Coordinates the technical procedure of hoisting a patient into a rescue helicopter"],
    ])},
    "survival-skills-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness chest trauma management", "Field protocols for managing life-threatening chest injuries away from hospital care"],
    ])},
    "survival-skills-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Vector-borne disease control", "Manages mosquito and insect-borne disease risk in disaster response zones"],
    ])},
    "survival-skills-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Technical canyoneering rescue", "Specialized rope rescue systems adapted for narrow canyon terrain"],
    ])},
    "survival-skills-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Cold weather survival biochemistry", "Studies the metabolic nutrition needs specific to surviving in extreme cold"],
    ])},
    "survival-skills-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Wilderness team leadership", "Studies effective leadership decision-making under high-uncertainty survival conditions"],
    ])},
    "survival-skills-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Explosive remnant clearance", "Safety protocols for surviving in areas contaminated by post-conflict unexploded munitions"],
    ])},
    "survival-skills-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Field water contaminant analysis", "Tests and identifies chemical or biological contaminants in field water sources"],
    ])},
    "survival-skills-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Frostbite tissue salvage", "Advanced rewarming and treatment protocols aimed at preserving frostbitten tissue"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"survival-skills-m2-l{base_n}"
    worked_key = f"survival-skills-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Survival Skills lessons.")


if __name__ == "__main__":
    main()
