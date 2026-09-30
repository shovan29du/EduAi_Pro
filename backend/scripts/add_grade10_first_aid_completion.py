#!/usr/bin/env python3
"""Depth pass, Grade 10 First Aid: fill in real, hand-checked
data_table content for the Grade 10 First Aid lessons not covered by
the earlier breadth-first batch. Brings Grade 10 First Aid to full
50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fa-g10-l1": {
        "data_table": table(["Emergency", "Key First Step"], [
            ["Anaphylaxis", "Use an epinephrine auto-injector immediately"], ["Fracture", "Immobilize before moving the person"],
        ]),
    },
    "first-aid-g10-l3": {
        "data_table": table(["Step", "Purpose"], [
            ["Check for danger", "Protects the first aider before approaching"],
        ]),
    },
    "first-aid-g10-l4": {
        "data_table": table(["Info to Give", "Reason"], [
            ["Location", "Helps responders find the scene"], ["Nature of emergency", "Helps dispatch the right help"],
        ]),
    },
    "first-aid-g10-l5": {
        "data_table": table(["Step", "Focus"], [
            ["Airway", "Is it open?"], ["Breathing", "Is the person breathing?"], ["Circulation", "Is there a pulse?"],
        ]),
    },
    "first-aid-g10-l6": {
        "data_table": table(["Ratio", "Detail"], [
            ["30:2", "Standard chest compressions to rescue breaths ratio for adult CPR"],
        ]),
    },
    "first-aid-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["AED", "Automated External Defibrillator, delivers a shock to restore heart rhythm"],
        ]),
    },
    "first-aid-g10-l8": {
        "data_table": table(["Use", "Purpose"], [
            ["Recovery position", "Keeps an unconscious but breathing person's airway clear"],
        ]),
    },
    "first-aid-g10-l9": {
        "data_table": table(["Sign", "Detail"], [
            ["Universal choking sign", "Hands clutching the throat"],
        ]),
    },
    "first-aid-g10-l10": {
        "data_table": table(["Step", "Action"], [
            ["Heimlich maneuver", "Abdominal thrusts to dislodge an airway obstruction"],
        ]),
    },
    "first-aid-g10-l11": {
        "data_table": table(["Step", "Action"], [
            ["Apply direct pressure", "Slows or stops bleeding"], ["Elevate the wound", "Reduces blood flow to the area"],
        ]),
    },
    "first-aid-g10-l12": {
        "data_table": table(["Step", "Action"], [
            ["Clean the wound", "Reduces infection risk"], ["Apply a bandage", "Protects the wound"],
        ]),
    },
    "first-aid-g10-l13": {
        "data_table": table(["Step", "Action"], [
            ["Clean with water", "Removes debris from a minor cut"],
        ]),
    },
    "first-aid-g10-l14": {
        "data_table": table(["Sign of Shock", "Detail"], [
            ["Pale, clammy skin", "A common warning sign"],
        ]),
    },
    "first-aid-g10-l15": {
        "data_table": table(["Warning Sign", "Detail"], [
            ["Confusion or memory loss", "Possible sign of concussion after head injury"],
        ]),
    },
    "first-aid-g10-l16": {
        "data_table": table(["Precaution", "Reason"], [
            ["Avoid moving the person", "Reduces risk of worsening a spinal injury"],
        ]),
    },
    "first-aid-g10-l18": {
        "data_table": table(["Step", "Purpose"], [
            ["Splinting", "Stabilizes a suspected fracture before movement"],
        ]),
    },
    "first-aid-g10-l19": {
        "data_table": table(["Step", "Action"], [
            ["Do not attempt to relocate", "Only trained professionals should reposition a dislocated joint"],
        ]),
    },
    "first-aid-g10-l20": {
        "data_table": table(["Condition", "Sign"], [
            ["Heat exhaustion", "Heavy sweating, weakness"], ["Heat stroke", "High body temperature, confusion, medical emergency"],
        ]),
    },
    "first-aid-g10-l21": {
        "data_table": table(["Sign", "Detail"], [
            ["Hypothermia", "Shivering, confusion, low body temperature"],
        ]),
    },
    "first-aid-g10-l22": {
        "data_table": table(["Sign", "Detail"], [
            ["Frostbite", "Numb, pale, hardened skin"],
        ]),
    },
    "first-aid-g10-l23": {
        "data_table": table(["Step", "Action"], [
            ["Lean forward, pinch nostrils", "Standard first response to a nosebleed"],
        ]),
    },
    "first-aid-g10-l24": {
        "data_table": table(["Burn Degree", "Description"], [
            ["First-degree", "Affects only the outer skin layer"], ["Second-degree", "Affects deeper skin layers, causes blisters"],
        ]),
    },
    "first-aid-g10-l25": {
        "data_table": table(["Step", "Action"], [
            ["Flush with water", "Standard first response to a chemical burn or eye injury"],
        ]),
    },
    "first-aid-g10-l26": {
        "data_table": table(["Step", "Action"], [
            ["Turn off the power source first", "Prevents further injury to the rescuer"],
        ]),
    },
    "first-aid-g10-l27": {
        "data_table": table(["Step", "Action"], [
            ["Call poison control", "Provides guidance specific to the poison"],
        ]),
    },
    "first-aid-g10-l28": {
        "data_table": table(["Step", "Action"], [
            ["Inject into outer thigh", "Standard site for an epinephrine auto-injector"],
        ]),
    },
    "first-aid-g10-l29": {
        "data_table": table(["Step", "Action"], [
            ["Use a rescue inhaler", "Opens the airways during an asthma attack"],
        ]),
    },
    "first-aid-g10-l30": {
        "data_table": table(["Step", "Action"], [
            ["Clear the area", "Prevents injury during a seizure"], ["Time the seizure", "Important information for responders"],
        ]),
    },
    "first-aid-g10-l31": {
        "data_table": table(["Condition", "Sign"], [
            ["Hypoglycemia", "Low blood sugar, causes shakiness and confusion"], ["Hyperglycemia", "High blood sugar, causes thirst and fatigue"],
        ]),
    },
    "first-aid-g10-l32": {
        "data_table": table(["Step", "Action"], [
            ["Lay the person down, elevate legs", "Standard response to fainting"],
        ]),
    },
    "first-aid-g10-l33": {
        "data_table": table(["Sign", "Detail"], [
            ["Chest pain radiating to arm or jaw", "Warning sign of a heart attack"],
        ]),
    },
    "first-aid-g10-l34": {
        "data_table": table(["Letter", "Sign to Check"], [
            ["F", "Face drooping"], ["A", "Arm weakness"], ["S", "Speech difficulty"], ["T", "Time to call emergency services"],
        ]),
    },
    "first-aid-g10-l35": {
        "data_table": table(["Step", "Action"], [
            ["Remove the stinger", "Reduces further venom release"],
        ]),
    },
    "first-aid-g10-l36": {
        "data_table": table(["Step", "Action"], [
            ["Keep the person still and calm", "Slows venom spread after a snake bite"],
        ]),
    },
    "first-aid-g10-l37": {
        "data_table": table(["Priority Step", "Reason"], [
            ["Reach or throw before going in", "Reduces risk to the rescuer"],
        ]),
    },
    "first-aid-g10-l38": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Gloves", "Protects against contact with blood or fluids"],
        ]),
    },
    "first-aid-g10-l39": {
        "data_table": table(["Injury", "First Response"], [
            ["Sprained ankle", "RICE (Rest, Ice, Compression, Elevation)"],
        ]),
    },
    "first-aid-g10-l40": {
        "data_table": table(["Step", "Action"], [
            ["Clean and cover", "Prevents blister infection"],
        ]),
    },
    "first-aid-g10-l41": {
        "data_table": table(["Step", "Action"], [
            ["Do not rub the eye", "Prevents further damage from a foreign object"],
        ]),
    },
    "first-aid-g10-l42": {
        "data_table": table(["Step", "Action"], [
            ["Keep the person calm and hydrated", "Supports recovery from nausea and vomiting"],
        ]),
    },
    "first-aid-g10-l43": {
        "data_table": table(["Step", "Action"], [
            ["Monitor for internal injury signs", "Abdominal injuries may not be immediately visible"],
        ]),
    },
    "first-aid-g10-l44": {
        "data_table": table(["Step", "Action"], [
            ["Support breathing, seek help immediately", "Chest injuries can be life-threatening"],
        ]),
    },
    "first-aid-g10-l45": {
        "data_table": table(["Step", "Action"], [
            ["Stay calm and listen without judgment", "Core principle of psychological first aid"],
        ]),
    },
    "first-aid-g10-l46": {
        "data_table": table(["Consideration", "Reason"], [
            ["Adjust technique for smaller bodies", "Infant and child anatomy differs from adults"],
        ]),
    },
    "first-aid-g10-l47": {
        "data_table": table(["Principle", "Reason"], [
            ["Only move if necessary", "Reduces risk of worsening an injury"],
        ]),
    },
    "first-aid-g10-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Good Samaritan law", "Legal protection for those who help in an emergency in good faith"],
        ]),
    },
    "first-aid-g10-l49": {
        "data_table": table(["Equipment", "Purpose"], [
            ["Gloves and mask", "Reduces exposure to bodily fluids"],
        ]),
    },
    "first-aid-g10-l50": {
        "data_table": table(["Element", "Purpose"], [
            ["Emergency contact list", "Quick access to help during a personal emergency"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["First Aid"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 First Aid lessons (completing 50/50).")


if __name__ == "__main__":
    main()
