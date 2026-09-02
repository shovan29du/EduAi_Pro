#!/usr/bin/env python3
"""Depth pass, Grade 9 First Aid: fill in real, hand-checked data_table
content for the 48 Grade 9 First Aid lessons not covered by the earlier
breadth-first batch. Brings Grade 9 First Aid to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fa-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["AED", "Automated External Defibrillator, delivers a shock to restore heart rhythm"],
        ]),
    },
    "first-aid-g9-l2": {
        "data_table": table(["Principle", "Meaning"], [
            ["Preserve life", "The primary goal of first aid"],
        ]),
    },
    "first-aid-g9-l3": {
        "data_table": table(["Step", "Focus"], [
            ["Airway", "Is it open?"], ["Breathing", "Is the person breathing?"], ["Circulation", "Is there a pulse?"],
        ]),
    },
    "first-aid-g9-l4": {
        "data_table": table(["Info to Give", "Reason"], [
            ["Location", "Helps responders find the scene"], ["Nature of emergency", "Helps dispatch the right help"],
        ]),
    },
    "first-aid-g9-l5": {
        "data_table": table(["Step", "Action"], [
            ["Heimlich maneuver", "Abdominal thrusts to dislodge an obstruction"],
        ]),
    },
    "first-aid-g9-l6": {
        "data_table": table(["Step", "Action"], [
            ["Clean the wound", "Reduces infection risk"], ["Apply a bandage", "Protects the wound"],
        ]),
    },
    "first-aid-g9-l7": {
        "data_table": table(["Bandage Type", "Use"], [
            ["Adhesive bandage", "Small cuts"], ["Roller bandage", "Larger wounds or to secure a dressing"],
        ]),
    },
    "first-aid-g9-l8": {
        "data_table": table(["Step", "Action"], [
            ["Apply direct pressure", "Slows or stops bleeding"], ["Elevate the wound", "Reduces blood flow to the area"],
        ]),
    },
    "first-aid-g9-l9": {
        "data_table": table(["Burn Degree", "Description"], [
            ["First-degree", "Affects only the outer skin layer"], ["Second-degree", "Affects deeper skin layers, causes blisters"],
        ]),
    },
    "first-aid-g9-l10": {
        "data_table": table(["Sign of Shock", "Detail"], [
            ["Pale, clammy skin", "A common warning sign"],
        ]),
    },
    "first-aid-g9-l11": {
        "data_table": table(["Step", "Action"], [
            ["Immobilize the area", "Prevents further injury"],
        ]),
    },
    "first-aid-g9-l12": {
        "data_table": table(["Step", "Purpose"], [
            ["Splinting", "Stabilizes a suspected fracture"],
        ]),
    },
    "first-aid-g9-l14": {
        "data_table": table(["Warning Sign", "Detail"], [
            ["Confusion or memory loss", "Possible sign of concussion after head injury"],
        ]),
    },
    "first-aid-g9-l16": {
        "data_table": table(["Sign", "Detail"], [
            ["Chest pain or pressure", "A common heart attack symptom"],
        ]),
    },
    "first-aid-g9-l17": {
        "data_table": table(["Step", "Action"], [
            ["Use a rescue inhaler", "Opens the airways during an asthma attack"],
        ]),
    },
    "first-aid-g9-l18": {
        "data_table": table(["Sign", "Detail"], [
            ["Anaphylaxis", "A severe, potentially life-threatening allergic reaction"],
        ]),
    },
    "first-aid-g9-l19": {
        "data_table": table(["Step", "Action"], [
            ["Inject into outer thigh", "Standard site for an epinephrine auto-injector"],
        ]),
    },
    "first-aid-g9-l20": {
        "data_table": table(["Step", "Action"], [
            ["Clear the area", "Prevents injury during a seizure"], ["Time the seizure", "Important information for responders"],
        ]),
    },
    "first-aid-g9-l21": {
        "data_table": table(["Sign", "Detail"], [
            ["Confusion, shakiness", "May indicate low blood sugar in a diabetic emergency"],
        ]),
    },
    "first-aid-g9-l22": {
        "data_table": table(["Condition", "Sign"], [
            ["Hypothermia", "Shivering, confusion, low body temperature"], ["Frostbite", "Numb, pale, hardened skin"],
        ]),
    },
    "first-aid-g9-l23": {
        "data_table": table(["Condition", "Sign"], [
            ["Heat exhaustion", "Heavy sweating, weakness"], ["Heat stroke", "High body temperature, confusion, medical emergency"],
        ]),
    },
    "first-aid-g9-l24": {
        "data_table": table(["Step", "Action"], [
            ["Call poison control", "Provides guidance for the specific poison"],
        ]),
    },
    "first-aid-g9-l25": {
        "data_table": table(["Step", "Action"], [
            ["Remove the stinger", "Reduces further venom release"],
        ]),
    },
    "first-aid-g9-l26": {
        "data_table": table(["Step", "Action"], [
            ["Clean the wound thoroughly", "Reduces infection risk from animal bites"],
        ]),
    },
    "first-aid-g9-l27": {
        "data_table": table(["Step", "Action"], [
            ["Lean forward, pinch nostrils", "Standard first response to a nosebleed"],
        ]),
    },
    "first-aid-g9-l28": {
        "data_table": table(["Step", "Action"], [
            ["Do not rub the eye", "Prevents further damage"],
        ]),
    },
    "first-aid-g9-l29": {
        "data_table": table(["Step", "Action"], [
            ["Preserve a knocked-out tooth in milk", "Increases chance of saving it"],
        ]),
    },
    "first-aid-g9-l30": {
        "data_table": table(["Priority Step", "Reason"], [
            ["Reach or throw before going in", "Reduces risk to the rescuer"],
        ]),
    },
    "first-aid-g9-l31": {
        "data_table": table(["Step", "Action"], [
            ["Lay the person down, elevate legs", "Standard response to fainting"],
        ]),
    },
    "first-aid-g9-l32": {
        "data_table": table(["Sign", "Detail"], [
            ["Chest pain radiating to arm or jaw", "Warning sign of a heart emergency"],
        ]),
    },
    "first-aid-g9-l33": {
        "data_table": table(["Precaution", "Reason"], [
            ["Avoid moving the person", "Reduces risk of worsening a spinal injury"],
        ]),
    },
    "first-aid-g9-l34": {
        "data_table": table(["Use", "Purpose"], [
            ["Recovery position", "Keeps an unconscious but breathing person's airway clear"],
        ]),
    },
    "first-aid-g9-l35": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Gloves", "Protects against contact with blood or fluids"],
        ]),
    },
    "first-aid-g9-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Clean and cover wounds", "Reduces the risk of infection"],
        ]),
    },
    "first-aid-g9-l37": {
        "data_table": table(["Step", "Action"], [
            ["Clean and cover", "Prevents blister infection"],
        ]),
    },
    "first-aid-g9-l38": {
        "data_table": table(["Step", "Action"], [
            ["Cool the skin, apply aloe", "Soothes sunburn"],
        ]),
    },
    "first-aid-g9-l39": {
        "data_table": table(["Step", "Action"], [
            ["Stay hydrated, rest", "Supports recovery from food poisoning"],
        ]),
    },
    "first-aid-g9-l40": {
        "data_table": table(["Injury", "First Response"], [
            ["Sprained ankle", "RICE (Rest, Ice, Compression, Elevation)"],
        ]),
    },
    "first-aid-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Mental health first aid", "Initial support offered to someone experiencing a mental health crisis"],
        ]),
    },
    "first-aid-g9-l42": {
        "data_table": table(["Step", "Action"], [
            ["Stay calm and speak reassuringly", "Helps de-escalate a panic attack"],
        ]),
    },
    "first-aid-g9-l43": {
        "data_table": table(["Step", "Action"], [
            ["Flush with water", "Standard first response to a chemical burn"],
        ]),
    },
    "first-aid-g9-l44": {
        "data_table": table(["Step", "Action"], [
            ["Turn off the power source first", "Prevents further injury to the rescuer"],
        ]),
    },
    "first-aid-g9-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Good Samaritan law", "Legal protection for those who help in an emergency in good faith"],
        ]),
    },
    "first-aid-g9-l46": {
        "data_table": table(["Step", "Purpose"], [
            ["Check for danger before approaching", "Protects the responder"],
        ]),
    },
    "first-aid-g9-l47": {
        "data_table": table(["Equipment", "Purpose"], [
            ["Gloves and mask", "Reduces exposure to bodily fluids"],
        ]),
    },
    "first-aid-g9-l48": {
        "data_table": table(["Practice", "Reason"], [
            ["Stay on the line, follow instructions", "Dispatchers can guide care until help arrives"],
        ]),
    },
    "first-aid-g9-l49": {
        "data_table": table(["Consideration", "Reason"], [
            ["Adjust technique for smaller bodies", "Infant and child anatomy differs from adults"],
        ]),
    },
    "first-aid-g9-l50": {
        "data_table": table(["Step", "Action"], [
            ["Gently stretch and hydrate", "Common treatment for muscle cramps"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["First Aid"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 First Aid lessons (completing 50/50).")


if __name__ == "__main__":
    main()
