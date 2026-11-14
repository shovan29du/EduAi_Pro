#!/usr/bin/env python3
"""Depth pass, Grade 10 Survival Skills: fill in real, hand-checked
data_table content for the Grade 10 Survival Skills lessons not
covered by the earlier breadth-first batch. Brings Grade 10 Survival
Skills to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "sv-g10-l1": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Controlled breathing", "Helps manage stress during a crisis"],
        ]),
    },
    "survival-skills-g10-l2": {
        "data_table": table(["Step", "Action"], [
            ["Apply direct pressure", "Slows or stops bleeding"], ["Elevate the wound", "Reduces blood flow to the area"],
        ]),
    },
    "survival-skills-g10-l4": {
        "data_table": table(["Burn Degree", "Description"], [
            ["First-degree", "Affects only the outer skin layer"], ["Second-degree", "Affects deeper layers, causes blisters"],
        ]),
    },
    "survival-skills-g10-l5": {
        "data_table": table(["Sign of Shock", "Detail"], [
            ["Pale, clammy skin", "A common warning sign"],
        ]),
    },
    "survival-skills-g10-l6": {
        "data_table": table(["Tool", "Use"], [
            ["Compass", "Shows magnetic direction"], ["Topographic map", "Shows terrain features"],
        ]),
    },
    "survival-skills-g10-l7": {
        "data_table": table(["Natural Sign", "Direction Clue"], [
            ["Sun's path", "Rises roughly east, sets roughly west"],
        ]),
    },
    "survival-skills-g10-l8": {
        "data_table": table(["Shelter Type", "Best Use"], [
            ["Lean-to", "Quick shelter using a fixed support and branches"],
        ]),
    },
    "survival-skills-g10-l9": {
        "data_table": table(["Method", "How It Works"], [
            ["Friction (bow drill)", "Rubbing wood together to create heat"], ["Flint and steel", "Striking sparks onto tinder"],
        ]),
    },
    "survival-skills-g10-l11": {
        "data_table": table(["Principle", "Reason"], [
            ["Never eat unidentified plants", "Many toxic plants resemble edible ones"],
        ]),
    },
    "survival-skills-g10-l12": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of similar thickness"], ["Bowline", "Creates a fixed loop that won't slip"],
        ]),
    },
    "survival-skills-g10-l13": {
        "data_table": table(["Sign", "Possible Meaning"], [
            ["Dark, towering clouds", "Storm approaching"],
        ]),
    },
    "survival-skills-g10-l14": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three of anything (fires, whistle blasts)", "Universal distress signal"],
        ]),
    },
    "survival-skills-g10-l15": {
        "data_table": table(["Method", "Purpose"], [
            ["Canning", "Preserves food using heat and sealed jars"], ["Dry storage", "Keeps staples shelf-stable"],
        ]),
    },
    "survival-skills-g10-l16": {
        "data_table": table(["Step", "Purpose"], [
            ["Build a kit", "Gathers essentials before disaster strikes"], ["Make a plan", "Coordinates family response"],
        ]),
    },
    "survival-skills-g10-l17": {
        "data_table": table(["Guideline", "Reason"], [
            ["Drop, cover, hold on", "Protects from falling debris during shaking"],
        ]),
    },
    "survival-skills-g10-l18": {
        "data_table": table(["Guideline", "Reason"], [
            ["Move to higher ground", "Avoids rising water"],
        ]),
    },
    "survival-skills-g10-l19": {
        "data_table": table(["Guideline", "Reason"], [
            ["Have an evacuation route ready", "Speeds escape from a wildfire"],
        ]),
    },
    "survival-skills-g10-l20": {
        "data_table": table(["Guideline", "Reason"], [
            ["Seek sturdy shelter", "Protects from wind and debris"],
        ]),
    },
    "survival-skills-g10-l21": {
        "data_table": table(["Skill", "Purpose"], [
            ["Pitching a tent", "Provides shelter from weather"],
        ]),
    },
    "survival-skills-g10-l22": {
        "data_table": table(["Practice", "Reason"], [
            ["Tell someone your route", "Helps rescuers find you if needed"],
        ]),
    },
    "survival-skills-g10-l23": {
        "data_table": table(["Guideline", "Reason"], [
            ["Keep distance from wildlife", "Reduces risk of attack or disease"],
        ]),
    },
    "survival-skills-g10-l24": {
        "data_table": table(["Step", "Action"], [
            ["Remove the stinger", "Reduces further venom release from an insect sting"],
        ]),
    },
    "survival-skills-g10-l25": {
        "data_table": table(["Principle", "Reason"], [
            ["Layered clothing", "Traps warm air and can be adjusted"],
        ]),
    },
    "survival-skills-g10-l26": {
        "data_table": table(["Principle", "Reason"], [
            ["Stay hydrated", "Prevents heat exhaustion"],
        ]),
    },
    "survival-skills-g10-l27": {
        "data_table": table(["Practice", "Reason"], [
            ["Use the right tool for the job", "Reduces injury risk"],
        ]),
    },
    "survival-skills-g10-l28": {
        "data_table": table(["Tool", "Purpose"], [
            ["Two-way radio", "Communication when cell networks are down"],
        ]),
    },
    "survival-skills-g10-l29": {
        "data_table": table(["Element", "Purpose"], [
            ["Meeting point", "Where family reunites if separated"],
        ]),
    },
    "survival-skills-g10-l30": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Water", "Hydration, recommended 1 gallon per person per day"],
        ]),
    },
    "survival-skills-g10-l31": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify hazards", "First step in risk assessment"],
        ]),
    },
    "survival-skills-g10-l32": {
        "data_table": table(["Principle", "Meaning"], [
            ["Situational awareness", "Noticing your surroundings to avoid danger"],
        ]),
    },
    "survival-skills-g10-l33": {
        "data_table": table(["Principle", "Meaning"], [
            ["Avoidance first", "The best self-defense is avoiding dangerous situations"],
        ]),
    },
    "survival-skills-g10-l34": {
        "data_table": table(["Practice", "Reason"], [
            ["Use crosswalks and signals", "Reduces pedestrian and traffic accident risk"],
        ]),
    },
    "survival-skills-g10-l35": {
        "data_table": table(["Technique", "Purpose"], [
            ["Floating on back", "Conserves energy in open water"],
        ]),
    },
    "survival-skills-g10-l36": {
        "data_table": table(["Practice", "Reason"], [
            ["Wear a life jacket", "Prevents drowning if you fall overboard"],
        ]),
    },
    "survival-skills-g10-l37": {
        "data_table": table(["Principle", "Meaning"], [
            ["Trust your instincts", "A key part of avoiding dangerous urban situations"],
        ]),
    },
    "survival-skills-g10-l38": {
        "data_table": table(["Kit Item", "Purpose"], [
            ["Flashlight and batteries", "Provides light during an outage"],
        ]),
    },
    "survival-skills-g10-l39": {
        "data_table": table(["Map Feature", "Meaning"], [
            ["Contour lines", "Show elevation changes"],
        ]),
    },
    "survival-skills-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Search and rescue", "Organized effort to locate and assist people in distress"],
        ]),
    },
    "survival-skills-g10-l41": {
        "data_table": table(["Service", "Role"], [
            ["Emergency dispatch (e.g. 911)", "Connects callers to police, fire, or medical help"],
        ]),
    },
    "survival-skills-g10-l42": {
        "data_table": table(["Technique", "Purpose"], [
            ["Controlled breathing", "Helps manage stress during a crisis"],
        ]),
    },
    "survival-skills-g10-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Assess the situation quickly", "Guides the most effective emergency response"],
        ]),
    },
    "survival-skills-g10-l44": {
        "data_table": table(["Practice", "Reason"], [
            ["Clear, calm communication", "Reduces confusion during a crisis"],
        ]),
    },
    "survival-skills-g10-l45": {
        "data_table": table(["Skill", "Use"], [
            ["Basic tool repair", "Fixes minor mechanical failures in the field"],
        ]),
    },
    "survival-skills-g10-l46": {
        "data_table": table(["Principle", "Reason"], [
            ["Ration supplies early", "Extends how long limited resources last"],
        ]),
    },
    "survival-skills-g10-l47": {
        "data_table": table(["Step", "Purpose"], [
            ["Splinting", "Stabilizes a suspected fracture"],
        ]),
    },
    "survival-skills-g10-l48": {
        "data_table": table(["Condition", "Sign"], [
            ["Hypothermia", "Shivering, confusion, low body temperature"], ["Heatstroke", "High body temperature, confusion"],
        ]),
    },
    "survival-skills-g10-l49": {
        "data_table": table(["Element", "Purpose"], [
            ["Evacuation route", "Planned path to safety"],
        ]),
    },
    "survival-skills-g10-l50": {
        "data_table": table(["Habit", "Benefit"], [
            ["Regular preparedness drills", "Builds long-term resilience"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Survival Skills lessons (completing 50/50).")


if __name__ == "__main__":
    main()
