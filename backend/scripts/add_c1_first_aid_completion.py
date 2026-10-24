#!/usr/bin/env python3
"""Depth pass, C1 First Aid: fill in real, hand-checked data_table
content for the 69 C1 First Aid lessons not covered by the earlier
breadth-first batch. Brings C1 First Aid to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "first-aid-c1-l1": {
        "data_table": table(["Step", "Action"], [
            ["Check", "Assess the scene and the person's responsiveness"], ["Call", "Contact emergency services"], ["Care", "Provide appropriate first aid"],
        ]),
    },
    "first-aid-c1-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Primary assessment", "Identifies immediately life-threatening conditions first"],
        ]),
    },
    "first-aid-c1-l4": {
        "data_table": table(["Degree", "Feature"], [
            ["First-degree burn", "Affects only the outer skin layer, redness without blisters"], ["Second-degree burn", "Affects deeper skin layers, causes blistering"],
        ]),
    },
    "first-aid-c1-l5": {
        "data_table": table(["Injury", "Sign"], [
            ["Fracture", "Deformity, severe pain, inability to bear weight"], ["Sprain", "Swelling and pain around a joint, ligament injury"],
        ]),
    },
    "first-aid-c1-l6": {
        "data_table": table(["Sign", "Detail"], [
            ["Shock", "Pale, cool, clammy skin with rapid weak pulse"],
        ]),
    },
    "first-aid-c1-l7": {
        "data_table": table(["Severity", "Response"], [
            ["Mild allergic reaction", "Monitor and consider antihistamine"], ["Anaphylaxis", "Administer epinephrine immediately and call emergency services"],
        ]),
    },
    "first-aid-c1-l8": {
        "data_table": table(["Emergency", "Key Sign"], [
            ["Heart attack", "Chest pain or pressure, often radiating to the arm"],
        ]),
    },
    "first-aid-c1-l9": {
        "data_table": table(["Letter", "Sign"], [
            ["F", "Face drooping"], ["A", "Arm weakness"], ["S", "Speech difficulty"], ["T", "Time to call emergency services"],
        ]),
    },
    "first-aid-c1-l10": {
        "data_table": table(["Step", "Purpose"], [
            ["Calling poison control", "Provides expert guidance specific to the substance involved"],
        ]),
    },
    "first-aid-c1-l11": {
        "data_table": table(["Condition", "Cause"], [
            ["Heat exhaustion", "Prolonged exposure to high heat with fluid loss"], ["Frostbite", "Tissue freezing from prolonged cold exposure"],
        ]),
    },
    "first-aid-c1-l12": {
        "data_table": table(["Step", "Purpose"], [
            ["Direct pressure", "The first-line method to control external bleeding"],
        ]),
    },
    "first-aid-c1-l13": {
        "data_table": table(["Category", "Priority"], [
            ["Immediate (red)", "Life-threatening injuries needing urgent care"], ["Minor (green)", "Walking wounded who can wait"],
        ]),
    },
    "first-aid-c1-l14": {
        "data_table": table(["Consideration", "Detail"], [
            ["Dosage differences", "Children require weight-based medication and technique adjustments"],
        ]),
    },
    "first-aid-c1-l15": {
        "data_table": table(["Condition", "First Aid Focus"], [
            ["Diabetes emergency", "Recognizing low versus high blood sugar symptoms"],
        ]),
    },
    "first-aid-c1-l16": {
        "data_table": table(["Step", "Purpose"], [
            ["Active listening", "Helps someone in crisis feel heard and supported"],
        ]),
    },
    "first-aid-c1-l17": {
        "data_table": table(["Priority", "Reason"], [
            ["Shelter before food", "Exposure kills faster than hunger in the wilderness"],
        ]),
    },
    "first-aid-c1-l18": {
        "data_table": table(["Category", "Example"], [
            ["Wound care", "Gauze, adhesive bandages, antiseptic wipes"],
        ]),
    },
    "first-aid-c1-l19": {
        "data_table": table(["Principle", "Meaning"], [
            ["Consent", "Ask before treating a conscious person whenever possible"],
        ]),
    },
    "first-aid-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Attaching AED pads", "Delivers a shock to restore normal heart rhythm"],
        ]),
    },
    "first-aid-c1-l21": {
        "data_table": table(["Step", "Purpose"], [
            ["Scene safety check", "Confirms the area is safe before approaching"],
        ]),
    },
    "first-aid-c1-l22": {
        "data_table": table(["Link", "Action"], [
            ["Early recognition", "Calling emergency services immediately"], ["Early CPR", "Maintaining blood flow to vital organs"],
        ]),
    },
    "first-aid-c1-l23": {
        "data_table": table(["Sign", "Meaning"], [
            ["Universal choking sign", "Hands clutched at the throat"],
        ]),
    },
    "first-aid-c1-l24": {
        "data_table": table(["Age Group", "Technique"], [
            ["Infant", "Back blows and chest thrusts"], ["Child", "Abdominal thrusts, adjusted for size"],
        ]),
    },
    "first-aid-c1-l25": {
        "data_table": table(["Step", "Purpose"], [
            ["Tilting the head back", "Opens the airway for rescue breaths"],
        ]),
    },
    "first-aid-c1-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["Following voice prompts", "AEDs guide the rescuer through each step automatically"],
        ]),
    },
    "first-aid-c1-l27": {
        "data_table": table(["Sign", "Detail"], [
            ["Chest discomfort", "Pressure, squeezing, or pain lasting more than a few minutes"],
        ]),
    },
    "first-aid-c1-l28": {
        "data_table": table(["Letter", "Meaning"], [
            ["F", "Face — ask the person to smile"], ["A", "Arms — ask them to raise both arms"],
        ]),
    },
    "first-aid-c1-l29": {
        "data_table": table(["Step", "Purpose"], [
            ["Cleaning with water", "Removes debris and reduces infection risk"],
        ]),
    },
    "first-aid-c1-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Leaning forward, pinching the nose", "Standard first response to control a nosebleed"],
        ]),
    },
    "first-aid-c1-l31": {
        "data_table": table(["Letter", "Step"], [
            ["R", "Rest"], ["I", "Ice"], ["C", "Compression"], ["E", "Elevation"],
        ]),
    },
    "first-aid-c1-l32": {
        "data_table": table(["Step", "Purpose"], [
            ["Immobilizing the area", "Prevents further damage before medical care"],
        ]),
    },
    "first-aid-c1-l33": {
        "data_table": table(["Practice", "Reason"], [
            ["Do not attempt to relocate the joint", "Improper handling can cause additional injury"],
        ]),
    },
    "first-aid-c1-l34": {
        "data_table": table(["Step", "Purpose"], [
            ["Cool running water", "Reduces heat damage to skin tissue"],
        ]),
    },
    "first-aid-c1-l35": {
        "data_table": table(["Practice", "Reason"], [
            ["Cover loosely, seek emergency care", "Severe burns require professional treatment"],
        ]),
    },
    "first-aid-c1-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Flush with clean water", "Removes irritants without additional damage"],
        ]),
    },
    "first-aid-c1-l37": {
        "data_table": table(["Step", "Purpose"], [
            ["Removing the stinger", "Reduces continued venom release"],
        ]),
    },
    "first-aid-c1-l38": {
        "data_table": table(["Step", "Purpose"], [
            ["Washing the wound thoroughly", "Reduces infection risk from bacteria in saliva"],
        ]),
    },
    "first-aid-c1-l39": {
        "data_table": table(["Sign", "Response"], [
            ["Difficulty breathing and swelling", "Administer epinephrine and call emergency services"],
        ]),
    },
    "first-aid-c1-l40": {
        "data_table": table(["Step", "Purpose"], [
            ["Using a rescue inhaler", "Opens airways during an asthma attack"],
        ]),
    },
    "first-aid-c1-l41": {
        "data_table": table(["Practice", "Reason"], [
            ["Clearing the area, not restraining", "Prevents injury during a seizure"],
        ]),
    },
    "first-aid-c1-l42": {
        "data_table": table(["Step", "Purpose"], [
            ["Laying the person flat and raising legs", "Restores blood flow to the brain"],
        ]),
    },
    "first-aid-c1-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Moving to a cool area and hydrating", "Reverses early heat-related illness"],
        ]),
    },
    "first-aid-c1-l44": {
        "data_table": table(["Sign", "Response"], [
            ["Confusion and very high body temperature", "A medical emergency requiring rapid cooling and urgent care"],
        ]),
    },
    "first-aid-c1-l45": {
        "data_table": table(["Sign", "Response"], [
            ["Shivering and confusion", "Warm the person gradually and seek medical care"],
        ]),
    },
    "first-aid-c1-l46": {
        "data_table": table(["Sign", "Response"], [
            ["Numb, pale skin", "Gently rewarm affected area, avoid rubbing"],
        ]),
    },
    "first-aid-c1-l47": {
        "data_table": table(["Condition", "Sign"], [
            ["Low blood sugar", "Shakiness, confusion, sweating"], ["High blood sugar", "Excessive thirst, fatigue, fruity breath odor"],
        ]),
    },
    "first-aid-c1-l48": {
        "data_table": table(["Step", "Purpose"], [
            ["Immobilizing above and below the injury", "Prevents movement that could worsen a fracture"],
        ]),
    },
    "first-aid-c1-l49": {
        "data_table": table(["Type", "Use"], [
            ["Roller bandage", "Secures dressings and provides compression"],
        ]),
    },
    "first-aid-c1-l50": {
        "data_table": table(["Sign", "Detail"], [
            ["Internal bleeding", "Bruising, swelling, or pain without a visible wound"],
        ]),
    },
    "first-aid-c1-l51": {
        "data_table": table(["Sign", "Detail"], [
            ["Concussion", "Confusion, headache, and dizziness after a head impact"],
        ]),
    },
    "first-aid-c1-l52": {
        "data_table": table(["Practice", "Reason"], [
            ["Minimizing movement", "Prevents worsening a possible spinal injury"],
        ]),
    },
    "first-aid-c1-l53": {
        "data_table": table(["Category", "Example Item"], [
            ["Wound care", "Bandages, gauze, antiseptic"], ["Tools", "Scissors, tweezers, gloves"],
        ]),
    },
    "first-aid-c1-l54": {
        "data_table": table(["Step", "Purpose"], [
            ["Giving a clear location", "Speeds up the emergency responder's arrival"],
        ]),
    },
    "first-aid-c1-l55": {
        "data_table": table(["Practice", "Reason"], [
            ["Not probing with tools", "Avoids pushing the object deeper or causing injury"],
        ]),
    },
    "first-aid-c1-l56": {
        "data_table": table(["Emergency", "First Aid Step"], [
            ["Knocked-out tooth", "Keep it moist and seek dental care immediately"],
        ]),
    },
    "first-aid-c1-l57": {
        "data_table": table(["Consideration", "Detail"], [
            ["Higher fall risk", "Older adults often need extra care for balance-related injuries"],
        ]),
    },
    "first-aid-c1-l58": {
        "data_table": table(["Injury", "Response"], [
            ["Suspected concussion", "Remove the athlete from play and seek evaluation"],
        ]),
    },
    "first-aid-c1-l59": {
        "data_table": table(["Practice", "Reason"], [
            ["Recovery position", "Keeps the airway clear for an unconscious, breathing person"],
        ]),
    },
    "first-aid-c1-l60": {
        "data_table": table(["Principle", "Meaning"], [
            ["Good Samaritan laws", "Protect people who give reasonable emergency aid from liability"],
        ]),
    },
    "first-aid-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying the check-call-care sequence", "Responding to a collapsed person in public"],
        ]),
    },
    "first-aid-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Prioritizing a response", "Deciding what to treat first in a multi-injury scenario"],
        ]),
    },
    "first-aid-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Treating a wound", "Cleaning and dressing a moderate cut correctly"],
        ]),
    },
    "first-aid-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Classifying a burn", "Determining burn degree from its appearance"],
        ]),
    },
    "first-aid-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Distinguishing a fracture from a sprain", "Assessing swelling, deformity, and pain level"],
        ]),
    },
    "first-aid-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Recognizing shock", "Identifying early signs before the condition worsens"],
        ]),
    },
    "first-aid-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Responding to anaphylaxis", "Deciding when to use an epinephrine auto-injector"],
        ]),
    },
    "first-aid-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Recognizing a cardiac emergency", "Distinguishing heart attack symptoms from other conditions"],
        ]),
    },
    "first-aid-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Applying FAST", "Assessing a person for stroke symptoms quickly"],
        ]),
    },
    "first-aid-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Handling a poisoning case", "Gathering key information before calling poison control"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["First Aid"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 First Aid lessons (completing 70/70).")


if __name__ == "__main__":
    main()
