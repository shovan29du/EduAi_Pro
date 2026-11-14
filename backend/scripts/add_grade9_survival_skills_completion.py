#!/usr/bin/env python3
"""Depth pass, Grade 9 Survival Skills: fill in real, hand-checked
data_table content for the 48 Grade 9 Survival Skills lessons not
covered by the earlier breadth-first batch. Brings Grade 9 Survival
Skills to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g9-l1": {
        "data_table": table(["Step", "Purpose"], [
            ["Build a kit", "Gathers essentials before disaster strikes"], ["Make a plan", "Coordinates family response"],
        ]),
    },
    "survival-skills-g9-l2": {
        "data_table": table(["Step (DRSABC)", "Meaning"], [
            ["D", "Check for Danger"], ["R", "Check Response"], ["S", "Send for help"],
        ]),
    },
    "survival-skills-g9-l4": {
        "data_table": table(["Tool", "Use"], [
            ["Compass", "Shows magnetic direction"], ["Topographic map", "Shows terrain features"],
        ]),
    },
    "survival-skills-g9-l5": {
        "data_table": table(["Natural Sign", "Direction Clue"], [
            ["Sun's path", "Rises roughly east, sets roughly west"], ["Moss growth", "Often more on the shaded side of trees"],
        ]),
    },
    "survival-skills-g9-l6": {
        "data_table": table(["Shelter Type", "Best Use"], [
            ["Lean-to", "Quick shelter using a fixed support and branches"],
        ]),
    },
    "survival-skills-g9-l7": {
        "data_table": table(["Method", "How It Works"], [
            ["Friction (bow drill)", "Rubbing wood together to create heat"], ["Flint and steel", "Striking sparks onto tinder"],
        ]),
    },
    "survival-skills-g9-l8": {
        "data_table": table(["Method", "How It Works"], [
            ["Boiling", "Kills pathogens with heat"], ["Filtration", "Removes particles and some microbes"],
        ]),
    },
    "survival-skills-g9-l9": {
        "data_table": table(["Principle", "Reason"], [
            ["Never eat unidentified plants", "Many toxic plants resemble edible ones"],
        ]),
    },
    "survival-skills-g9-l10": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of similar thickness"], ["Bowline", "Creates a fixed loop that won't slip"],
        ]),
    },
    "survival-skills-g9-l11": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three of anything (fires, whistle blasts)", "Universal distress signal"],
        ]),
    },
    "survival-skills-g9-l12": {
        "data_table": table(["Sign", "Possible Meaning"], [
            ["Dark, towering clouds", "Storm approaching"], ["Ring around the moon", "Precipitation may follow"],
        ]),
    },
    "survival-skills-g9-l14": {
        "data_table": table(["Guideline", "Reason"], [
            ["Keep distance from wildlife", "Reduces risk of attack or disease"],
        ]),
    },
    "survival-skills-g9-l15": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Water", "Hydration, recommended 1 gallon per person per day"], ["First aid supplies", "Treats injuries"],
        ]),
    },
    "survival-skills-g9-l16": {
        "data_table": table(["Skill", "Purpose"], [
            ["Pitching a tent", "Provides shelter from weather"],
        ]),
    },
    "survival-skills-g9-l17": {
        "data_table": table(["Practice", "Reason"], [
            ["Tell someone your route", "Helps rescuers find you if needed"],
        ]),
    },
    "survival-skills-g9-l18": {
        "data_table": table(["Technique", "Purpose"], [
            ["Floating on back", "Conserves energy in open water"],
        ]),
    },
    "survival-skills-g9-l19": {
        "data_table": table(["Principle", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings to avoid danger"],
        ]),
    },
    "survival-skills-g9-l20": {
        "data_table": table(["Practice", "Purpose"], [
            ["Smoke detectors", "Provide early warning of fire"], ["Fire escape plan", "Ensures a safe exit route"],
        ]),
    },
    "survival-skills-g9-l21": {
        "data_table": table(["Guideline", "Reason"], [
            ["Drop, cover, hold on", "Protects from falling debris during shaking"],
        ]),
    },
    "survival-skills-g9-l22": {
        "data_table": table(["Guideline", "Reason"], [
            ["Move to higher ground", "Avoids rising water"],
        ]),
    },
    "survival-skills-g9-l23": {
        "data_table": table(["Guideline", "Reason"], [
            ["Seek sturdy shelter", "Protects from wind and debris"],
        ]),
    },
    "survival-skills-g9-l24": {
        "data_table": table(["Item", "Purpose"], [
            ["Emergency contact list", "Quick access during city-wide disruption"],
        ]),
    },
    "survival-skills-g9-l25": {
        "data_table": table(["Element", "Purpose"], [
            ["Out-of-area contact", "Central point if local lines are down"],
        ]),
    },
    "survival-skills-g9-l26": {
        "data_table": table(["Element", "Purpose"], [
            ["Meeting point", "Where family reunites if separated"],
        ]),
    },
    "survival-skills-g9-l27": {
        "data_table": table(["Method", "Purpose"], [
            ["Canning", "Preserves food using heat and sealed jars"], ["Dry storage", "Keeps staples like rice and beans shelf-stable"],
        ]),
    },
    "survival-skills-g9-l28": {
        "data_table": table(["Skill", "Use"], [
            ["Sewing a button", "Repairs clothing without replacement"],
        ]),
    },
    "survival-skills-g9-l29": {
        "data_table": table(["Practice", "Reason"], [
            ["Use the right tool for the job", "Reduces injury risk"],
        ]),
    },
    "survival-skills-g9-l30": {
        "data_table": table(["Map Feature", "Meaning"], [
            ["Contour lines", "Show elevation changes"],
        ]),
    },
    "survival-skills-g9-l31": {
        "data_table": table(["Skill", "Purpose"], [
            ["Orienteering", "Navigating terrain using a map and compass"],
        ]),
    },
    "survival-skills-g9-l32": {
        "data_table": table(["Principle", "Reason"], [
            ["Layered clothing", "Traps warm air and can be adjusted"],
        ]),
    },
    "survival-skills-g9-l33": {
        "data_table": table(["Principle", "Reason"], [
            ["Stay hydrated", "Prevents heat exhaustion"],
        ]),
    },
    "survival-skills-g9-l34": {
        "data_table": table(["Safety Step", "Reason"], [
            ["Clear the area", "Prevents accidental spread of fire"],
        ]),
    },
    "survival-skills-g9-l35": {
        "data_table": table(["Skill", "Use"], [
            ["Rope coiling", "Keeps rope tangle-free and ready to use"],
        ]),
    },
    "survival-skills-g9-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Handwashing", "Prevents illness when resources are limited"],
        ]),
    },
    "survival-skills-g9-l37": {
        "data_table": table(["Principle", "Meaning"], [
            ["Trust your instincts", "A key part of avoiding dangerous situations"],
        ]),
    },
    "survival-skills-g9-l38": {
        "data_table": table(["Practice", "Reason"], [
            ["Wear a helmet", "Reduces head injury risk"],
        ]),
    },
    "survival-skills-g9-l39": {
        "data_table": table(["Injury", "First Response"], [
            ["Minor burn", "Cool with running water"], ["Cut", "Apply direct pressure to stop bleeding"],
        ]),
    },
    "survival-skills-g9-l40": {
        "data_table": table(["Step", "Action"], [
            ["Heimlich maneuver", "Abdominal thrusts to dislodge an airway obstruction"],
        ]),
    },
    "survival-skills-g9-l41": {
        "data_table": table(["Service", "Role"], [
            ["Emergency dispatch (e.g. 911)", "Connects callers to police, fire, or medical help"],
        ]),
    },
    "survival-skills-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["CERT", "Community Emergency Response Team, trained civilian volunteers"],
        ]),
    },
    "survival-skills-g9-l43": {
        "data_table": table(["Principle", "Meaning"], [
            ["Situational awareness", "Continuously observing your environment for risk"],
        ]),
    },
    "survival-skills-g9-l44": {
        "data_table": table(["Technique", "Purpose"], [
            ["Controlled breathing", "Helps manage stress during a crisis"],
        ]),
    },
    "survival-skills-g9-l45": {
        "data_table": table(["Guideline", "Reason"], [
            ["Give animals space", "Reduces the chance of a defensive reaction"],
        ]),
    },
    "survival-skills-g9-l46": {
        "data_table": table(["Practice", "Reason"], [
            ["Wear a life jacket", "Prevents drowning if you fall overboard"],
        ]),
    },
    "survival-skills-g9-l47": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Flashlight and batteries", "Provides light during an outage"],
        ]),
    },
    "survival-skills-g9-l48": {
        "data_table": table(["Element", "Purpose"], [
            ["Evacuation route", "Planned path to safety"],
        ]),
    },
    "survival-skills-g9-l49": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Bandages and antiseptic", "Treats wounds in the wilderness"],
        ]),
    },
    "survival-skills-g9-l50": {
        "data_table": table(["Skill", "Benefit"], [
            ["Growing food", "Reduces reliance on external food supplies"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Survival Skills lessons (completing 50/50).")


if __name__ == "__main__":
    main()
