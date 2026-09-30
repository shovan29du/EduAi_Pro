#!/usr/bin/env python3
"""Depth pass, Grade 6 Cooking: fill in real, hand-checked data_table
content for the 28 Grade 6 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 6 Cooking to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g6-l1": {
        "data_table": table(["Cuisine", "Signature Dish"], [
            ["Italian", "Pasta"], ["Mexican", "Tacos"], ["Indian", "Curry"],
        ]),
    },
    "cooking-g6-l2": {
        "data_table": table(["Rule", "Why"], [
            ["Wash hands before cooking", "Removes germs"], ["Ask an adult before using sharp tools", "Prevents injury"],
        ]),
    },
    "cooking-g6-l3": {
        "data_table": table(["Rule", "Why"], [
            ["Cut away from your body", "Prevents injury"], ["Use a cutting board", "Protects the counter and knife"],
        ]),
    },
    "cooking-g6-l5": {
        "data_table": table(["Recipe Part", "Purpose"], [
            ["Ingredients list", "What you need"], ["Instructions", "The steps to follow, in order"],
        ]),
    },
    "cooking-g6-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Keep raw meat separate from other foods", "Prevents cross-contamination"],
            ["Cook food to a safe temperature", "Kills harmful bacteria"],
        ]),
    },
    "cooking-g6-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Baking", "Cooking food using dry heat in an oven"],
        ]),
    },
    "cooking-g6-l8": {
        "data_table": table(["Bread Ingredient", "Purpose"], [
            ["Flour", "Provides structure"], ["Yeast", "Makes the dough rise"],
        ]),
    },
    "cooking-g6-l9": {
        "data_table": table(["Breakfast Food", "Food Group"], [
            ["Oatmeal", "Grains"], ["Eggs", "Protein"],
        ]),
    },
    "cooking-g6-l10": {
        "data_table": table(["Cooking Method", "Example Vegetable"], [
            ["Steaming", "Broccoli"], ["Roasting", "Carrots"],
        ]),
    },
    "cooking-g6-l11": {
        "data_table": table(["Grain", "Common Use"], [
            ["Rice", "Side dish or base for many meals"], ["Quinoa", "Protein-rich grain alternative"],
        ]),
    },
    "cooking-g6-l12": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooking in fully submerged simmering water"], ["Scrambling", "Whisking and cooking in a pan"],
        ]),
    },
    "cooking-g6-l13": {
        "data_table": table(["Sauce", "Common Use"], [
            ["Tomato sauce", "Pasta dishes"], ["Vinaigrette", "Salad dressing"],
        ]),
    },
    "cooking-g6-l14": {
        "data_table": table(["Dish Type", "Example"], [
            ["Soup", "Chicken noodle soup"], ["Stew", "Beef stew"],
        ]),
    },
    "cooking-g6-l16": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"], ["Dairy", "Milk, cheese"],
        ]),
    },
    "cooking-g6-l17": {
        "data_table": table(["Ingredient", "Role"], [
            ["Olive oil", "Common cooking fat"], ["Basil", "Common herb"],
        ]),
    },
    "cooking-g6-l18": {
        "data_table": table(["Ingredient", "Role"], [
            ["Corn tortilla", "Base for many dishes"], ["Chili peppers", "Adds heat and flavor"],
        ]),
    },
    "cooking-g6-l19": {
        "data_table": table(["Ingredient", "Role"], [
            ["Cumin", "Common spice"], ["Lentils", "Common protein source"],
        ]),
    },
    "cooking-g6-l20": {
        "data_table": table(["Technique", "Description"], [
            ["Stir-frying", "Cooking quickly over high heat"],
        ]),
    },
    "cooking-g6-l21": {
        "data_table": table(["Ingredient", "Role"], [
            ["Tahini", "Sesame paste used in dishes like hummus"],
        ]),
    },
    "cooking-g6-l22": {
        "data_table": table(["Ingredient", "Role"], [
            ["Olive oil", "Common cooking fat"], ["Fresh vegetables", "Central to most dishes"],
        ]),
    },
    "cooking-g6-l23": {
        "data_table": table(["Dessert Type", "Example"], [
            ["Baked", "Cookies, cake"], ["No-bake", "Fruit salad, pudding"],
        ]),
    },
    "cooking-g6-l24": {
        "data_table": table(["Storage Method", "Purpose"], [
            ["Refrigeration", "Slows bacterial growth"], ["Freezing", "Preserves food for longer periods"],
        ]),
    },
    "cooking-g6-l25": {
        "data_table": table(["Tool", "Use"], [
            ["Measuring cup", "Measures liquids or dry ingredients"], ["Whisk", "Mixes ingredients together"],
        ]),
    },
    "cooking-g6-l26": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"], ["Sugar content", "How much sugar is in the food"],
        ]),
    },
    "cooking-g6-l27": {
        "data_table": table(["Protein Source", "Type"], [
            ["Lentils", "Plant-based"], ["Tofu", "Plant-based"],
        ]),
    },
    "cooking-g6-l28": {
        "data_table": table(["Leavening Agent", "How It Works"], [
            ["Yeast", "Ferments and releases gas over time"], ["Baking soda", "Reacts instantly with acid"],
        ]),
    },
    "cooking-g6-l29": {
        "data_table": table(["Table Item", "Placement"], [
            ["Fork", "Left of the plate"], ["Knife and spoon", "Right of the plate"],
        ]),
    },
    "cooking-g6-l30": {
        "data_table": table(["Tradition", "Example"], [
            ["Family recipes", "Passed down across generations"], ["Holiday meals", "Special dishes for celebrations"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Cooking lessons (completing 30/30).")


if __name__ == "__main__":
    main()
