#!/usr/bin/env python3
"""Pilot: add genuine, hand-checked data_table / formulae content to two
sample sets -- the Cooking pathway (Practical Skills) and the Outdoor &
Navigation category (Survival Skills) -- as the template for extending real
reference tables to other pathways/categories in later batches.

Every fact here is a standard, well-documented reference value (compass
bearings, CDC water-boiling guidance, standard vegetable blanching times,
the classic fire triangle, hypothermia staging, knot uses, etc.), not an
invented number.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_skills_pilot_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRACTICAL_PATH = BASE_DIR / "data" / "practical_skills" / "practical_skills.json"
SURVIVAL_PATH = BASE_DIR / "data" / "survival_skills" / "survival_skills.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


COOKING_CHARTS: dict[str, dict] = {
    "Kitchen Safety Basics": {
        "data_table": table(["Hazard", "Risk", "Prevention"], [
            ["Hot surfaces / pans", "Burns", "Use oven mitts; turn pot handles inward"],
            ["Sharp knives", "Cuts", "Use the claw grip; cut away from your body"],
            ["Raw meat", "Cross-contamination", "Separate cutting boards; wash hands after handling"],
            ["Wet hands near outlets", "Electric shock", "Dry hands before touching appliances"],
        ]),
    },
    "Balanced Meals & Nutrition": {
        "data_table": table(["Food Group", "Approximate Share of Plate"], [
            ["Vegetables", "~30%"], ["Fruits", "~20%"], ["Grains", "~25%"], ["Protein", "~25%"],
        ]),
        "formulae": ["Based on the USDA MyPlate guideline (approximate proportions, adjust to individual needs)"],
    },
    "Basic Knife Grip and Safety": {
        "data_table": table(["Grip", "How", "Purpose"], [
            ["Pinch grip", "Thumb and index finger pinch the blade just above the handle", "Maximum control of the blade"],
            ["Claw grip (guide hand)", "Fingertips curled under, knuckles guide the blade", "Protects fingers while holding food steady"],
        ]),
    },
    "Seasoning with Salt, Acid, and Herbs": {
        "data_table": table(["Herb", "Classic Pairing"], [
            ["Basil", "Tomatoes, Italian dishes"], ["Rosemary", "Roasted meats, potatoes"],
            ["Cilantro", "Mexican and Southeast Asian dishes"], ["Dill", "Fish, cucumber, yogurt sauces"],
            ["Thyme", "Soups, stews, roasted vegetables"],
        ]),
    },
    "Sauteing Vegetables Properly": {
        "data_table": table(["Vegetable", "Typical Sauté Time"], [
            ["Onions", "5–7 minutes"], ["Garlic", "30 seconds–1 minute (burns easily)"],
            ["Mushrooms", "5–8 minutes"], ["Bell peppers", "4–6 minutes"],
        ]),
    },
    "Boiling and Blanching Vegetables": {
        "data_table": table(["Vegetable", "Blanching Time"], [
            ["Broccoli florets", "2–3 minutes"], ["Green beans", "2–3 minutes"],
            ["Carrots (sliced)", "2 minutes"], ["Peas", "1–2 minutes"], ["Spinach", "30 seconds–1 minute"],
        ]),
    },
    "Cooking Perfect Rice and Grains": {
        "data_table": table(["Grain", "Water : Grain Ratio"], [
            ["White rice", "2:1"], ["Brown rice", "2.5:1"], ["Quinoa", "2:1"], ["Couscous", "1:1"], ["Rolled oats", "2:1"],
        ]),
    },
    "Building Flavor with Aromatics": {
        "data_table": table(["Aromatic Base", "Cuisine", "Ingredients"], [
            ["Mirepoix", "French", "Onion, carrot, celery (2:1:1)"],
            ["Holy trinity", "Cajun/Louisiana", "Onion, celery, bell pepper"],
            ["Sofrito", "Spanish/Latin", "Onion, garlic, tomato, pepper"],
            ["Aromatics base", "Chinese", "Ginger, garlic, scallion"],
        ]),
    },
    "Simmering and Making Basic Soup": {
        "formulae": ["Simmer ≈ 85–96°C (185–205°F) — small steady bubbles, below a full boil (100°C / 212°F)"],
    },
    "Roasting Vegetables in the Oven": {
        "data_table": table(["Vegetable", "Oven Temp", "Roast Time"], [
            ["Potatoes (cubed)", "200°C / 400°F", "35–40 minutes"],
            ["Carrots", "200°C / 400°F", "25–30 minutes"],
            ["Broccoli", "220°C / 425°F", "15–20 minutes"],
            ["Brussels sprouts", "200°C / 400°F", "25–30 minutes"],
        ]),
    },
    "Marinating for Flavor and Tenderness": {
        "data_table": table(["Protein/Food", "Typical Marinating Time"], [
            ["Chicken", "2–12 hours"], ["Beef or lamb", "2–24 hours"],
            ["Fish", "15–30 minutes (acidic marinades can start to \"cook\" fish if left too long)"],
            ["Vegetables", "30 minutes–2 hours"],
        ]),
    },
    "Baking Cookies": {
        "formulae": ["A common baker's ratio for simple cookie dough: 1 part fat : 2 parts sugar : 3 parts flour"],
    },
}

OUTDOOR_CHARTS: dict[str, dict] = {
    "Using a Compass": {
        "data_table": table(["Direction", "Bearing"], [
            ["North", "0° / 360°"], ["Northeast", "45°"], ["East", "90°"], ["Southeast", "135°"],
            ["South", "180°"], ["Southwest", "225°"], ["West", "270°"], ["Northwest", "315°"],
        ]),
    },
    "Learning the Four Cardinal Directions": {
        "data_table": table(["Direction", "Bearing", "Opposite"], [
            ["North", "0°", "South"], ["East", "90°", "West"], ["South", "180°", "North"], ["West", "270°", "East"],
        ]),
    },
    "Weather Awareness": {
        "data_table": table(["Cloud Type", "What It Often Signals"], [
            ["Cumulus", "Fair weather"], ["Cirrus (high, wispy)", "Fair now, change may be coming"],
            ["Stratus", "Overcast skies, possible drizzle"], ["Cumulonimbus", "Thunderstorms"],
        ]),
    },
    "Water Purification by Boiling": {
        "formulae": ["Boil water for at least 1 minute to kill most pathogens (CDC guidance); boil for 3 minutes at altitudes above 2,000 m / 6,500 ft"],
    },
    "Basic Rope Knots": {
        "data_table": table(["Knot", "Use"], [
            ["Square knot", "Joining two ropes of similar thickness"],
            ["Bowline", "Fixed loop at the end of a rope that won't slip or tighten"],
            ["Clove hitch", "Quickly attaching a rope to a post or pole"],
            ["Figure-eight", "A stopper knot that prevents a rope end from slipping through"],
        ]),
    },
    "Fire Safety Basics: Starting a Fire with Matches": {
        "data_table": table(["Fire Triangle Element", "Role"], [
            ["Heat", "Ignition source (match, spark)"], ["Fuel", "Tinder, kindling, then larger fuel wood"], ["Oxygen", "Airflow to sustain combustion"],
        ]),
        "formulae": ["Build fuel in stages: tinder (thin, dry material) → kindling (pencil-thick sticks) → fuel wood (larger logs)"],
    },
    "Recognizing and Preventing Hypothermia": {
        "data_table": table(["Stage", "Approx. Body Temp", "Signs"], [
            ["Mild", "35–32°C (95–90°F)", "Shivering, confusion, faster breathing"],
            ["Moderate", "32–28°C (90–82°F)", "Shivering may stop, worsening confusion, slurred speech"],
            ["Severe", "Below 28°C (82°F)", "Unconsciousness, very weak or absent pulse — life-threatening emergency"],
        ]),
    },
    "Finding North Using the Sun": {
        "formulae": ["Shadow-stick method: place a stick upright, mark the shadow tip, wait 15 minutes, mark the new tip — the line between marks runs roughly west to east"],
    },
    "Water Purification Tablets": {
        "formulae": ["Iodine tablets: typically need about 30 minutes of contact time before water is safe to drink (follow the product's instructions)"],
    },
    "Dressing for Outdoor Weather": {
        "data_table": table(["Layer", "Purpose"], [
            ["Base layer", "Wicks sweat away from skin"], ["Insulating layer", "Traps warm air (fleece, down)"],
            ["Outer shell", "Blocks wind and rain"],
        ]),
    },
}


def apply_charts(lessons_by_key: dict, charts: dict[str, dict]) -> int:
    updated = 0
    missing = [k for k in charts if k not in lessons_by_key]
    if missing:
        raise SystemExit(f"Entries not found: {missing}")
    for key, fields in charts.items():
        entry = lessons_by_key[key]
        for field_key, value in fields.items():
            if field_key not in entry:
                entry[field_key] = value
                updated += 1
    return updated


def main() -> None:
    practical = json.loads(PRACTICAL_PATH.read_text(encoding="utf-8"))
    cooking_modules = {m["title"]: m for m in practical["pathways"]["cooking"]["modules"]}
    practical_updated = apply_charts(cooking_modules, COOKING_CHARTS)
    PRACTICAL_PATH.write_text(json.dumps(practical, indent=2, ensure_ascii=False) + "\n")

    survival = json.loads(SURVIVAL_PATH.read_text(encoding="utf-8"))
    outdoor_skills = {s["name"]: s for s in survival["categories"]["outdoor_and_navigation"]}
    survival_updated = apply_charts(outdoor_skills, OUTDOOR_CHARTS)
    SURVIVAL_PATH.write_text(json.dumps(survival, indent=2, ensure_ascii=False) + "\n")

    print(f"Cooking pathway: added {practical_updated} chart/table/formula fields across {len(COOKING_CHARTS)} modules.")
    print(f"Outdoor & Navigation: added {survival_updated} chart/table/formula fields across {len(OUTDOOR_CHARTS)} skills.")


if __name__ == "__main__":
    main()
