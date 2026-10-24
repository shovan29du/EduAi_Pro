#!/usr/bin/env python3
"""Depth pass, C1 Survival Skills: fill in real, hand-checked data_table
content for the 69 C1 Survival Skills lessons not covered by the earlier
breadth-first batch. Brings C1 Survival Skills to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_survival_skills_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "survival-skills-c1-l1": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of threes", "3 minutes without air, 3 hours without shelter, 3 days without water, 3 weeks without food"],
        ]),
    },
    "survival-skills-c1-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Scene safety check", "Ensures the responder doesn't become a second victim"],
        ]),
    },
    "survival-skills-c1-l4": {
        "data_table": table(["Category", "Example Item"], [
            ["Fire-starting", "Ferro rod and tinder"], ["Signaling", "Whistle and mirror"],
        ]),
    },
    "survival-skills-c1-l5": {
        "data_table": table(["Method", "Effectiveness"], [
            ["Boiling", "Kills nearly all pathogens"], ["Filtration", "Removes particulates and many microorganisms"],
        ]),
    },
    "survival-skills-c1-l6": {
        "data_table": table(["Element", "Role"], [
            ["Fuel", "Material that burns"], ["Oxygen", "Sustains the combustion reaction"], ["Heat", "Ignites and sustains the fire"],
        ]),
    },
    "survival-skills-c1-l7": {
        "data_table": table(["Factor", "Consideration"], [
            ["Insulation", "Reduces heat loss to the ground and air"],
        ]),
    },
    "survival-skills-c1-l8": {
        "data_table": table(["Method", "Technique"], [
            ["Shadow-stick method", "Uses the sun's shadow movement to find direction"], ["Polaris method", "Uses the North Star to find true north"],
        ]),
    },
    "survival-skills-c1-l9": {
        "data_table": table(["Phase", "Focus"], [
            ["Search phase", "Locating the missing person"], ["Rescue phase", "Extracting and treating the person safely"],
        ]),
    },
    "survival-skills-c1-l10": {
        "data_table": table(["Stage", "Focus"], [
            ["Mitigation", "Reduces the impact of a future disaster"], ["Response", "Immediate actions taken during a disaster"],
        ]),
    },
    "survival-skills-c1-l11": {
        "data_table": table(["Hazard", "Terrain Type"], [
            ["Flash flooding", "Narrow canyons and dry riverbeds"], ["Rockfall", "Steep, loose scree slopes"],
        ]),
    },
    "survival-skills-c1-l12": {
        "data_table": table(["Nutrient", "Priority in Survival"], [
            ["Water", "Most urgent, needed within days"], ["Carbohydrates", "Provides quick usable energy"],
        ]),
    },
    "survival-skills-c1-l13": {
        "data_table": table(["Condition", "Cause"], [
            ["Hypothermia", "Core body temperature drops dangerously low"], ["Heat stroke", "Body's core temperature rises to dangerous levels"],
        ]),
    },
    "survival-skills-c1-l14": {
        "data_table": table(["Principle", "Meaning"], [
            ["Improvisation", "Using available materials creatively when proper equipment is absent"],
        ]),
    },
    "survival-skills-c1-l15": {
        "data_table": table(["Device", "Use"], [
            ["Satellite messenger", "Sends location and messages outside cell coverage"], ["Two-way radio", "Enables communication within a limited range"],
        ]),
    },
    "survival-skills-c1-l16": {
        "data_table": table(["Category", "Example"], [
            ["Water storage", "Stockpiling enough water for at least three days"],
        ]),
    },
    "survival-skills-c1-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Mutual aid networks", "Neighbors coordinate resources and support during a crisis"],
        ]),
    },
    "survival-skills-c1-l18": {
        "data_table": table(["Step", "Purpose"], [
            ["Reviewing a real incident", "Identifies decisions that worked and those that failed"],
        ]),
    },
    "survival-skills-c1-l19": {
        "data_table": table(["Factor", "Consideration"], [
            ["Likelihood", "How probable a hazard is to occur"], ["Severity", "How much harm the hazard could cause"],
        ]),
    },
    "survival-skills-c1-l20": {
        "data_table": table(["Material", "Property"], [
            ["Ripstop nylon", "Lightweight and resistant to tearing"], ["Titanium", "Strong and lightweight for cookware"],
        ]),
    },
    "survival-skills-c1-l21": {
        "data_table": table(["Knot", "Use"], [
            ["Bowline", "Creates a secure loop that won't slip"], ["Clove hitch", "Quickly secures rope to a post or pole"],
        ]),
    },
    "survival-skills-c1-l22": {
        "data_table": table(["Step", "Purpose"], [
            ["Taking a bearing", "Determines the direction to travel using a compass"],
        ]),
    },
    "survival-skills-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["GPS waypoint", "A saved coordinate marking a specific location"],
        ]),
    },
    "survival-skills-c1-l24": {
        "data_table": table(["Principle", "Meaning"], [
            ["Pack it in, pack it out", "Leave no trace of waste in the wilderness"],
        ]),
    },
    "survival-skills-c1-l25": {
        "data_table": table(["Step", "Purpose"], [
            ["Filing a trip plan", "Tells someone your route and expected return time"],
        ]),
    },
    "survival-skills-c1-l26": {
        "data_table": table(["Signal", "Meaning"], [
            ["Three of anything", "The universal distress signal (three fires, whistles, or flashes)"],
        ]),
    },
    "survival-skills-c1-l27": {
        "data_table": table(["Rule", "Guidance"], [
            ["When in doubt, don't eat it", "The safest approach to unfamiliar plants"],
        ]),
    },
    "survival-skills-c1-l28": {
        "data_table": table(["Principle", "Meaning"], [
            ["Sustainable harvesting", "Taking only what's needed without depleting the source"],
        ]),
    },
    "survival-skills-c1-l29": {
        "data_table": table(["Method", "Use"], [
            ["Snare trap", "Captures small game using a noose mechanism"], ["Hand-line fishing", "Simple fishing method using line, hook, and bait"],
        ]),
    },
    "survival-skills-c1-l30": {
        "data_table": table(["Layer", "Purpose"], [
            ["Base layer", "Wicks moisture away from skin"], ["Shell layer", "Blocks wind and precipitation"],
        ]),
    },
    "survival-skills-c1-l31": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Traveling during cooler hours", "Reduces risk of heat exhaustion"],
        ]),
    },
    "survival-skills-c1-l32": {
        "data_table": table(["Method", "Detail"], [
            ["Chemical treatment", "Iodine or chlorine tablets neutralize pathogens"],
        ]),
    },
    "survival-skills-c1-l33": {
        "data_table": table(["Method", "Technique"], [
            ["Bow drill", "Generates friction heat by spinning a spindle with a bow"], ["Ferro rod", "Produces hot sparks when scraped with a striker"],
        ]),
    },
    "survival-skills-c1-l34": {
        "data_table": table(["Environment", "Shelter Type"], [
            ["Snow", "Snow cave or quinzhee"], ["Forest", "Lean-to using available branches"],
        ]),
    },
    "survival-skills-c1-l35": {
        "data_table": table(["Category", "Priority"], [
            ["Immediate", "Life-threatening injuries requiring urgent care"], ["Delayed", "Serious but stable injuries"],
        ]),
    },
    "survival-skills-c1-l36": {
        "data_table": table(["Step", "Purpose"], [
            ["Cleaning the wound", "Reduces risk of infection in a remote setting"],
        ]),
    },
    "survival-skills-c1-l37": {
        "data_table": table(["Practice", "Reason"], [
            ["Making noise while hiking", "Alerts wildlife to your presence, reducing surprise encounters"],
        ]),
    },
    "survival-skills-c1-l38": {
        "data_table": table(["Sign", "Meaning"], [
            ["Triangular head", "Common indicator of many venomous snake species"],
        ]),
    },
    "survival-skills-c1-l39": {
        "data_table": table(["Sign", "Risk"], [
            ["Recent avalanche debris", "Indicates unstable snowpack nearby"],
        ]),
    },
    "survival-skills-c1-l40": {
        "data_table": table(["Technique", "Purpose"], [
            ["Facing upstream while crossing", "Maintains balance against the current's force"],
        ]),
    },
    "survival-skills-c1-l41": {
        "data_table": table(["Factor", "Consideration"], [
            ["Pack volume", "Should match trip length and gear needs"],
        ]),
    },
    "survival-skills-c1-l42": {
        "data_table": table(["Layer", "Function"], [
            ["Mid layer", "Traps warm air for insulation"],
        ]),
    },
    "survival-skills-c1-l43": {
        "data_table": table(["Factor", "Effect"], [
            ["Positive mindset", "Statistically correlates with higher survival rates"],
        ]),
    },
    "survival-skills-c1-l44": {
        "data_table": table(["Dynamic", "Effect"], [
            ["Clear leadership", "Improves decision-making speed in a group crisis"],
        ]),
    },
    "survival-skills-c1-l45": {
        "data_table": table(["Sign", "Meaning"], [
            ["Darkening cumulus clouds", "Often signal an approaching storm"],
        ]),
    },
    "survival-skills-c1-l46": {
        "data_table": table(["Cloud Type", "Indicates"], [
            ["Cirrus", "Fair weather, but may precede a change"], ["Cumulonimbus", "Thunderstorms"],
        ]),
    },
    "survival-skills-c1-l47": {
        "data_table": table(["Tool", "Use"], [
            ["Fixed-blade knife", "General cutting, carving, and food prep"], ["Folding saw", "Cutting larger branches for shelter or fire"],
        ]),
    },
    "survival-skills-c1-l48": {
        "data_table": table(["Practice", "Reason"], [
            ["Cutting away from the body", "Prevents accidental injury"],
        ]),
    },
    "survival-skills-c1-l49": {
        "data_table": table(["Priority", "Reason"], [
            ["Insulation from the ground", "Ground contact draws heat away faster than air"],
        ]),
    },
    "survival-skills-c1-l50": {
        "data_table": table(["Step", "Purpose"], [
            ["Building a debris layer", "Traps warm air for insulation using natural materials"],
        ]),
    },
    "survival-skills-c1-l51": {
        "data_table": table(["Method", "Use"], [
            ["Smoking", "Preserves meat by drying and adding antimicrobial compounds"], ["Drying", "Removes moisture to prevent spoilage"],
        ]),
    },
    "survival-skills-c1-l52": {
        "data_table": table(["Practice", "Purpose"], [
            ["Elevated cache", "Protects stored food from ground-based animals"],
        ]),
    },
    "survival-skills-c1-l53": {
        "data_table": table(["Skill", "Application"], [
            ["Situational awareness", "Recognizing threats in an urban emergency"],
        ]),
    },
    "survival-skills-c1-l54": {
        "data_table": table(["Category", "Example"], [
            ["Essentials", "Water, food, first aid, flashlight, documents"],
        ]),
    },
    "survival-skills-c1-l55": {
        "data_table": table(["Step", "Purpose"], [
            ["Designating a meeting point", "Reunites family members if separated during an emergency"],
        ]),
    },
    "survival-skills-c1-l56": {
        "data_table": table(["Category", "Example"], [
            ["Utility shutoffs", "Knowing how to turn off gas, water, and electricity"],
        ]),
    },
    "survival-skills-c1-l57": {
        "data_table": table(["Item", "Purpose"], [
            ["Sterile gauze", "Covers and protects a wound"],
        ]),
    },
    "survival-skills-c1-l58": {
        "data_table": table(["Material", "Use"], [
            ["Rigid material (stick, trekking pole)", "Stabilizes a suspected fracture"],
        ]),
    },
    "survival-skills-c1-l59": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Caloric rationing", "Extends limited food supply during prolonged emergencies"],
        ]),
    },
    "survival-skills-c1-l60": {
        "data_table": table(["Material", "Source"], [
            ["Plant fiber cordage", "Twisted from bark or plant stalks"], ["Sinew", "Made from animal tendon"],
        ]),
    },
    "survival-skills-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying Leave No Trace", "Choosing an established campsite over a fragile one"],
        ]),
    },
    "survival-skills-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Building a trip itinerary", "Mapping daily mileage and water sources"],
        ]),
    },
    "survival-skills-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Identifying local plants", "Comparing a region's edible and poisonous look-alikes"],
        ]),
    },
    "survival-skills-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Assigning group roles", "Designating a navigator and a first-aid lead"],
        ]),
    },
    "survival-skills-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Applying the rule of threes", "Prioritizing shelter over food in a survival scenario"],
        ]),
    },
    "survival-skills-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Performing a scene assessment", "Checking for hazards before approaching an injured hiker"],
        ]),
    },
    "survival-skills-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Managing panic", "Applying calming techniques during a simulated emergency"],
        ]),
    },
    "survival-skills-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Assembling a kit", "Selecting items by weight, priority, and versatility"],
        ]),
    },
    "survival-skills-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Locating a water source", "Reading terrain features to find likely water"],
        ]),
    },
    "survival-skills-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Explaining the fire triangle", "Diagnosing why a fire won't stay lit"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Survival Skills"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Survival Skills: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Survival Skills lessons (completing 70/70).")


if __name__ == "__main__":
    main()
