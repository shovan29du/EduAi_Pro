#!/usr/bin/env python3
"""Depth pass, Grade 8 First Aid: fill in real, hand-checked data_table
content for the 38 Grade 8 First Aid lessons not covered by the earlier
breadth-first batch. Brings Grade 8 First Aid to full 40/40 coverage.

Content covers standard, uncontroversial first-aid guidance -- nothing
fabricated or presented as fact when it's actually invented. Framed as
educational awareness, not a substitute for certified training.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_first_aid_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fa-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["First aid", "Immediate care given to an injured or ill person before professional help arrives"],
        ]),
    },
    "first-aid-g8-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Check", "Assess the scene and the person"], ["Call", "Contact emergency services"],
            ["Care", "Provide appropriate first aid"],
        ]),
    },
    "first-aid-g8-l3": {
        "data_table": table(["Step", "Detail"], [
            ["Stay calm", "Speak clearly to the operator"], ["Give your location", "Helps responders find you"],
        ]),
    },
    "first-aid-g8-l4": {
        "data_table": table(["Situation", "Why Use Recovery Position"], [
            ["Unresponsive but breathing", "Keeps the airway clear"],
        ]),
    },
    "first-aid-g8-l5": {
        "data_table": table(["Sign", "Action"], [
            ["No response to voice or touch", "Call for emergency help immediately"],
        ]),
    },
    "first-aid-g8-l6": {
        "data_table": table(["Sign of Choking", "Response"], [
            ["Can't speak or cough", "Get help from an adult immediately"],
        ]),
    },
    "first-aid-g8-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["AED", "A device that can help restart a normal heart rhythm"],
        ]),
    },
    "first-aid-g8-l9": {
        "data_table": table(["Step", "Action"], [
            ["1", "Clean the wound with water"], ["2", "Cover with a clean bandage"],
        ]),
    },
    "first-aid-g8-l10": {
        "data_table": table(["Step", "Action"], [
            ["Apply firm, direct pressure", "Helps stop bleeding"], ["Call for help", "For severe bleeding"],
        ]),
    },
    "first-aid-g8-l11": {
        "data_table": table(["Burn Degree", "First Aid"], [
            ["Minor (first-degree)", "Cool water, then cover loosely"],
        ]),
    },
    "first-aid-g8-l12": {
        "data_table": table(["Step", "Action"], [
            ["Lean forward slightly", "Prevents swallowing blood"], ["Pinch the soft part of the nose", "Stops the bleeding"],
        ]),
    },
    "first-aid-g8-l13": {
        "data_table": table(["Sign of Shock", "Example"], [
            ["Pale, cool skin", "A common early sign"], ["Rapid breathing", "A common sign"],
        ]),
    },
    "first-aid-g8-l14": {
        "data_table": table(["Sign of Fracture", "Response"], [
            ["Deformity or inability to move", "Keep the area still, seek medical help"],
        ]),
    },
    "first-aid-g8-l15": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Sprain", "Rest, ice, compression, elevation"],
        ]),
    },
    "first-aid-g8-l16": {
        "data_table": table(["Sign of Head Injury", "Response"], [
            ["Confusion or loss of consciousness", "Seek medical help immediately"],
        ]),
    },
    "first-aid-g8-l17": {
        "data_table": table(["Sign of Seizure", "Response"], [
            ["Uncontrolled shaking", "Clear the area, protect the head, do not restrain"],
        ]),
    },
    "first-aid-g8-l18": {
        "data_table": table(["Sign of Fainting", "Response"], [
            ["Sudden loss of consciousness", "Lay the person down, elevate legs if safe"],
        ]),
    },
    "first-aid-g8-l20": {
        "data_table": table(["Cold Injury", "First Aid"], [
            ["Hypothermia", "Warm the person gradually, seek help"],
            ["Frostbite", "Warm affected area gently, seek help"],
        ]),
    },
    "first-aid-g8-l21": {
        "data_table": table(["Sign of Allergic Reaction", "Example"], [
            ["Hives or swelling", "Common signs of a mild reaction"],
        ]),
    },
    "first-aid-g8-l22": {
        "data_table": table(["Sign of Anaphylaxis", "Response"], [
            ["Difficulty breathing, swelling of face/throat", "Call emergency services immediately"],
        ]),
    },
    "first-aid-g8-l23": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Insect sting", "Remove the stinger, clean the area"],
        ]),
    },
    "first-aid-g8-l24": {
        "data_table": table(["Sign of Heart Attack", "Example"], [
            ["Chest pain or pressure", "A common warning sign"],
        ]),
    },
    "first-aid-g8-l25": {
        "data_table": table(["Sign of Stroke", "Detail"], [
            ["FAST method", "Face drooping, Arm weakness, Speech difficulty, Time to call for help"],
        ]),
    },
    "first-aid-g8-l26": {
        "data_table": table(["Situation", "Response"], [
            ["Suspected poisoning", "Call poison control or emergency services immediately"],
        ]),
    },
    "first-aid-g8-l27": {
        "data_table": table(["Situation", "First Aid Step"], [
            ["Eye injury", "Do not rub the eye; seek medical help"],
        ]),
    },
    "first-aid-g8-l28": {
        "data_table": table(["Dental Emergency", "First Aid Step"], [
            ["Knocked-out tooth", "Handle gently, seek a dentist quickly"],
        ]),
    },
    "first-aid-g8-l29": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Bandages", "Cover small cuts"], ["Antiseptic wipes", "Clean a wound"],
        ]),
    },
    "first-aid-g8-l30": {
        "data_table": table(["Step", "Why"], [
            ["Check for hazards", "Protects the helper from harm"],
        ]),
    },
    "first-aid-g8-l31": {
        "data_table": table(["Step", "Action"], [
            ["Clean the wound", "Removes dirt and bacteria"], ["Apply a sterile dressing", "Protects the wound"],
        ]),
    },
    "first-aid-g8-l32": {
        "data_table": table(["Sign of Dehydration", "Example"], [
            ["Dry mouth, dizziness", "Common early signs"],
        ]),
    },
    "first-aid-g8-l33": {
        "data_table": table(["First Aid Step", "Purpose"], [
            ["Gentle stretching", "Relieves a muscle cramp"],
        ]),
    },
    "first-aid-g8-l34": {
        "data_table": table(["Principle", "Meaning"], [
            ["Consent", "Asking before helping a conscious person"],
        ]),
    },
    "first-aid-g8-l35": {
        "data_table": table(["Principle", "Meaning"], [
            ["Good Samaritan laws", "Legal protections for those who help in good faith"],
        ]),
    },
    "first-aid-g8-l36": {
        "data_table": table(["Injury", "First Aid Step"], [
            ["Sprained ankle", "Rest, ice, compression, elevation"],
        ]),
    },
    "first-aid-g8-l37": {
        "data_table": table(["Sign of Asthma Attack", "Response"], [
            ["Wheezing, difficulty breathing", "Help use prescribed inhaler, seek help if severe"],
        ]),
    },
    "first-aid-g8-l38": {
        "data_table": table(["First Aid Step", "Purpose"], [
            ["Cover with a soft bandage", "Protects a blister from further irritation"],
        ]),
    },
    "first-aid-g8-l39": {
        "data_table": table(["Rule", "Why"], [
            ["Swim with a buddy", "Someone can get help if needed"],
            ["Reach or throw, don't go", "Avoid entering the water yourself"],
        ]),
    },
    "first-aid-g8-l40": {
        "data_table": table(["Plan Element", "Purpose"], [
            ["Meeting point", "Where family reunites if separated"], ["Emergency contact", "Someone to call for updates"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["First Aid"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json First Aid: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 First Aid lessons (completing 40/40).")


if __name__ == "__main__":
    main()
