#!/usr/bin/env python3
"""Depth pass, C2 First Aid: fill in real, hand-checked data_table
content for the 69 C2 First Aid lessons not covered by the earlier
breadth-first batch. Brings C2 First Aid to full 70/70 coverage.

l61 is a "Foundations 2" lesson revisiting l3; l62-l70 are "Worked
Analysis" companions to l1-l9 (l64 revisits l3 again). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "first-aid-c2-l1": {
        "data_table": table(["Step", "Action"], [
            ["Emergency response protocol", "Check scene safety, then assess the person before intervening"],
        ]),
    },
    "first-aid-c2-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Wilderness & remote medicine", "Adapts standard first aid when professional help is hours away"],
        ]),
    },
    "first-aid-c2-l4": {
        "data_table": table(["Degree", "Feature"], [
            ["First-degree burn", "Affects only the outer skin layer, causing redness"],
            ["Second-degree burn", "Affects deeper skin layers, causing blistering"],
        ]),
    },
    "first-aid-c2-l5": {
        "data_table": table(["Technique", "Purpose"], [
            ["Splinting", "Immobilizes a suspected fracture to prevent further injury"],
        ]),
    },
    "first-aid-c2-l6": {
        "data_table": table(["Type", "Cause"], [
            ["Hypovolemic shock", "Results from significant blood or fluid loss"],
            ["Anaphylactic shock", "Results from a severe allergic reaction"],
        ]),
    },
    "first-aid-c2-l7": {
        "data_table": table(["Sign", "Detail"], [
            ["Anaphylaxis", "Rapid-onset swelling, difficulty breathing, and potential circulatory collapse"],
        ]),
    },
    "first-aid-c2-l8": {
        "data_table": table(["Sign", "Detail"], [
            ["Cardiac arrest", "Sudden loss of responsiveness with no normal breathing or pulse"],
        ]),
    },
    "first-aid-c2-l9": {
        "data_table": table(["Letter (FAST)", "Meaning"], [
            ["F", "Face drooping"], ["A", "Arm weakness"], ["S", "Speech difficulty"], ["T", "Time to call emergency services"],
        ]),
    },
    "first-aid-c2-l10": {
        "data_table": table(["Symptom", "Consideration"], [
            ["Poisoning symptom", "Varies by substance; identifying the agent guides the response"],
        ]),
    },
    "first-aid-c2-l11": {
        "data_table": table(["Condition", "Sign"], [
            ["Heat exhaustion", "Heavy sweating, weakness, and cool clammy skin"],
            ["Frostbite", "Numbness and hardened, pale skin from cold exposure"],
        ]),
    },
    "first-aid-c2-l12": {
        "data_table": table(["Step", "Action"], [
            ["Direct pressure", "Applies firm, continuous pressure to control external bleeding"],
        ]),
    },
    "first-aid-c2-l13": {
        "data_table": table(["Category", "Meaning"], [
            ["Immediate", "Life-threatening injury requiring urgent treatment"],
            ["Delayed", "Serious injury that can safely wait for treatment"],
        ]),
    },
    "first-aid-c2-l14": {
        "data_table": table(["Concern", "Detail"], [
            ["Pediatric emergency", "Requires age-adjusted assessment and dosing considerations"],
        ]),
    },
    "first-aid-c2-l15": {
        "data_table": table(["Condition", "Sign"], [
            ["Hypoglycemia", "Shakiness, confusion, and sweating from low blood sugar"],
        ]),
    },
    "first-aid-c2-l16": {
        "data_table": table(["Skill", "Purpose"], [
            ["Active listening", "Builds trust and calm with a distressed person during a response"],
        ]),
    },
    "first-aid-c2-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Extended care", "Sustains a patient's condition when evacuation is delayed for hours or days"],
        ]),
    },
    "first-aid-c2-l18": {
        "data_table": table(["Activity", "Kit Priority"], [
            ["Backcountry hiking", "Prioritizes blister care, splinting material, and water treatment"],
        ]),
    },
    "first-aid-c2-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Good Samaritan law", "Offers legal protection to those who provide reasonable emergency aid in good faith"],
        ]),
    },
    "first-aid-c2-l20": {
        "data_table": table(["Metric", "Standard"], [
            ["Compression rate", "About 100-120 compressions per minute"],
            ["Compression depth", "At least 2 inches (5 cm) for an adult"],
        ]),
    },
    "first-aid-c2-l21": {
        "data_table": table(["Technique", "Purpose"], [
            ["Head-tilt chin-lift", "Opens the airway by repositioning the tongue away from the throat"],
        ]),
    },
    "first-aid-c2-l22": {
        "data_table": table(["Role", "Task"], [
            ["Two-rescuer CPR", "One rescuer compresses while the other manages the airway and ventilations"],
        ]),
    },
    "first-aid-c2-l23": {
        "data_table": table(["Rhythm", "Detail"], [
            ["Ventricular fibrillation", "Chaotic electrical activity requiring immediate defibrillation"],
        ]),
    },
    "first-aid-c2-l24": {
        "data_table": table(["Step", "Action"], [
            ["Tourniquet application", "Placed above the wound and tightened until bleeding stops"],
        ]),
    },
    "first-aid-c2-l25": {
        "data_table": table(["Technique", "Purpose"], [
            ["Wound packing", "Fills a deep wound cavity to maintain pressure on the bleeding source"],
        ]),
    },
    "first-aid-c2-l26": {
        "data_table": table(["Survey", "Purpose"], [
            ["Primary survey", "Identifies immediate life threats (airway, breathing, circulation)"],
            ["Secondary survey", "Systematic head-to-toe exam for additional injuries"],
        ]),
    },
    "first-aid-c2-l27": {
        "data_table": table(["Step", "Purpose"], [
            ["Shock management", "Positions and warms the patient while controlling the underlying cause"],
        ]),
    },
    "first-aid-c2-l28": {
        "data_table": table(["Rule", "Use"], [
            ["Rule of nines", "Estimates the percentage of body surface area affected by a burn"],
        ]),
    },
    "first-aid-c2-l29": {
        "data_table": table(["Injury", "Sign"], [
            ["Tension pneumothorax", "Progressive difficulty breathing with tracheal deviation"],
        ]),
    },
    "first-aid-c2-l30": {
        "data_table": table(["Sign", "Detail"], [
            ["Abdominal trauma", "Rigidity or bruising may indicate internal bleeding"],
        ]),
    },
    "first-aid-c2-l31": {
        "data_table": table(["Assessment", "Consideration"], [
            ["Pediatric assessment", "Normal vital sign ranges differ significantly from adults"],
        ]),
    },
    "first-aid-c2-l32": {
        "data_table": table(["Treatment", "Purpose"], [
            ["Epinephrine auto-injector", "Rapidly reverses the effects of severe anaphylaxis"],
        ]),
    },
    "first-aid-c2-l33": {
        "data_table": table(["Response", "Detail"], [
            ["Overdose response", "Focuses on airway support and rapid emergency activation"],
        ]),
    },
    "first-aid-c2-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Prolonged field care", "Sustains treatment over extended time when evacuation is delayed"],
        ]),
    },
    "first-aid-c2-l35": {
        "data_table": table(["Factor", "Consideration"], [
            ["Evacuation decision", "Weighs injury severity against terrain, weather, and available resources"],
        ]),
    },
    "first-aid-c2-l36": {
        "data_table": table(["Step", "Action"], [
            ["Drowning response", "Prioritizes rescue breathing since drowning primarily causes respiratory arrest"],
        ]),
    },
    "first-aid-c2-l37": {
        "data_table": table(["Condition", "Sign"], [
            ["Altitude illness", "Headache, nausea, and fatigue from rapid ascent to high elevation"],
        ]),
    },
    "first-aid-c2-l38": {
        "data_table": table(["Injury", "Detail"], [
            ["Lightning injury", "Can cause cardiac arrest even without visible burns"],
        ]),
    },
    "first-aid-c2-l39": {
        "data_table": table(["Category", "Criteria"], [
            ["START triage", "Sorts patients rapidly using respiration, perfusion, and mental status"],
        ]),
    },
    "first-aid-c2-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Mass casualty incident", "Requires resource allocation prioritized by triage rather than first-come basis"],
        ]),
    },
    "first-aid-c2-l41": {
        "data_table": table(["Technique", "Purpose"], [
            ["Spinal immobilization", "Limits movement of the spine to prevent worsening a suspected injury"],
        ]),
    },
    "first-aid-c2-l42": {
        "data_table": table(["Splint Type", "Use"], [
            ["Traction splint", "Stabilizes a femur fracture by applying steady pulling force"],
        ]),
    },
    "first-aid-c2-l43": {
        "data_table": table(["Concern", "Detail"], [
            ["Crush injury", "Risk of dangerous chemical release into circulation upon pressure release"],
        ]),
    },
    "first-aid-c2-l44": {
        "data_table": table(["Step", "Action"], [
            ["Amputation care", "Controls bleeding at the injury site and preserves the severed part for transport"],
        ]),
    },
    "first-aid-c2-l45": {
        "data_table": table(["Sign", "Detail"], [
            ["Sepsis", "Fever, rapid heart rate, and confusion following infection"],
        ]),
    },
    "first-aid-c2-l46": {
        "data_table": table(["Condition", "Response"], [
            ["Severe hypoglycemia", "Give fast-acting sugar if the person is conscious and able to swallow"],
        ]),
    },
    "first-aid-c2-l47": {
        "data_table": table(["Approach", "Detail"], [
            ["Mental health crisis response", "Prioritizes calm communication and safety over confrontation"],
        ]),
    },
    "first-aid-c2-l48": {
        "data_table": table(["Step", "Action"], [
            ["Overdose first aid", "Supports breathing and positions the patient to prevent airway obstruction"],
        ]),
    },
    "first-aid-c2-l49": {
        "data_table": table(["Component", "Purpose"], [
            ["Handoff report", "Ensures continuity of care by conveying key patient information to responders"],
        ]),
    },
    "first-aid-c2-l50": {
        "data_table": table(["Practice", "Purpose"], [
            ["Infection control", "Gloves and hand hygiene reduce risk to both patient and responder"],
        ]),
    },
    "first-aid-c2-l51": {
        "data_table": table(["Skill", "Purpose"], [
            ["Team coordination", "Assigns clear roles to prevent duplicated or missed actions during response"],
        ]),
    },
    "first-aid-c2-l52": {
        "data_table": table(["Concern", "Detail"], [
            ["Electrical injury", "Can cause internal damage disproportionate to visible surface burns"],
        ]),
    },
    "first-aid-c2-l53": {
        "data_table": table(["Concern", "Detail"], [
            ["Secondary drowning complication", "Fluid in the lungs can cause delayed respiratory distress"],
        ]),
    },
    "first-aid-c2-l54": {
        "data_table": table(["Approach", "Detail"], [
            ["Pain management", "Positioning and distraction can supplement limited field treatment options"],
        ]),
    },
    "first-aid-c2-l55": {
        "data_table": table(["Scale", "Use"], [
            ["AVPU scale", "Quickly assesses level of consciousness: Alert, Verbal, Pain, Unresponsive"],
        ]),
    },
    "first-aid-c2-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Multi-system trauma", "Requires prioritizing the most immediately life-threatening injury first"],
        ]),
    },
    "first-aid-c2-l57": {
        "data_table": table(["Step", "Purpose"], [
            ["Vehicle extrication basics", "Stabilizes the scene and vehicle before attempting patient removal"],
        ]),
    },
    "first-aid-c2-l58": {
        "data_table": table(["Principle", "Detail"], [
            ["First responder ethics", "Balances duty to act with responder safety and scope of training"],
        ]),
    },
    "first-aid-c2-l59": {
        "data_table": table(["Element", "Purpose"], [
            ["Disaster preparedness plan", "Pre-positions supplies and defines roles before an emergency occurs"],
        ]),
    },
    "first-aid-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Simulated multi-casualty scenario", "Integrates triage, treatment, and coordination under realistic pressure"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Wound Care Step", "Action"], [
    ["1", "Clean hands and wear gloves if available"],
    ["2", "Stop the bleeding with direct pressure"],
    ["3", "Clean the wound with water"],
    ["4", "Cover with a sterile dressing"],
])

# l61 "Foundations 2" lesson revisits l3.
CHARTS["first-aid-c2-l61"] = {
    "data_table": _l3_source_table,
}

# l62-l70 "Worked Analysis" lessons reuse the data_table of l1-l9.
WORKED_ANALYSIS_MAP = {62: 1, 63: 2, 64: 3, 65: 4, 66: 5, 67: 6, 68: 7, 69: 8, 70: 9}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"first-aid-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"first-aid-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"first-aid-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["First Aid"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 First Aid lessons (completing 70/70).")


if __name__ == "__main__":
    main()
