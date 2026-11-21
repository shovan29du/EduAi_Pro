#!/usr/bin/env python3
"""Depth pass, Grade 7 Cooking: fill in real, hand-checked data_table
content for the 38 Grade 7 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 7 Cooking to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g7-l1": {
        "data_table": table(["Process", "Effect on Food"], [
            ["Heating protein", "Causes it to denature and firm up"], ["Caramelization", "Sugars brown and develop flavor with heat"],
        ]),
    },
    "cooking-g7-l2": {
        "data_table": table(["Rule", "Why"], [
            ["Wash hands before cooking", "Removes germs"], ["Ask an adult before using sharp tools", "Prevents injury"],
        ]),
    },
    "cooking-g7-l3": {
        "data_table": table(["Cut Type", "Description"], [
            ["Julienne", "Thin matchstick strips"], ["Dice", "Small cubes"],
        ]),
    },
    "cooking-g7-l4": {
        "data_table": table(["Measurement", "Equivalent"], [
            ["3 teaspoons", "1 tablespoon"], ["16 tablespoons", "1 cup"],
        ]),
    },
    "cooking-g7-l5": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"], ["Dairy", "Milk, cheese"],
        ]),
    },
    "cooking-g7-l6": {
        "data_table": table(["Recipe Part", "Purpose"], [
            ["Ingredients list", "What you need"], ["Instructions", "The steps to follow, in order"],
        ]),
    },
    "cooking-g7-l7": {
        "data_table": table(["Planning Step", "Purpose"], [
            ["List meals for the week", "Saves time and reduces waste"],
        ]),
    },
    "cooking-g7-l8": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooking in fully submerged simmering water"], ["Steaming", "Cooking with vapor over boiling water"],
        ]),
    },
    "cooking-g7-l10": {
        "data_table": table(["Method", "Description"], [
            ["Roasting", "Dry-heat cooking in an oven"], ["Grilling", "Cooking over direct heat"],
        ]),
    },
    "cooking-g7-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Baking", "Cooking food using dry heat in an oven"],
        ]),
    },
    "cooking-g7-l12": {
        "data_table": table(["Bread Ingredient", "Purpose"], [
            ["Flour", "Provides structure"], ["Yeast", "Makes the dough rise"],
        ]),
    },
    "cooking-g7-l14": {
        "data_table": table(["Seasoning", "Effect"], [
            ["Salt", "Enhances existing flavors"], ["Acid (lemon, vinegar)", "Adds brightness"],
        ]),
    },
    "cooking-g7-l15": {
        "data_table": table(["Sauce", "Common Use"], [
            ["Tomato sauce", "Pasta dishes"], ["Vinaigrette", "Salad dressing"],
        ]),
    },
    "cooking-g7-l16": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooked in the shell in water"], ["Scrambling", "Whisked and cooked in a pan"],
        ]),
    },
    "cooking-g7-l17": {
        "data_table": table(["Dairy Product", "Common Use"], [
            ["Milk", "Drinking, baking"], ["Cheese", "Melting, snacking"],
        ]),
    },
    "cooking-g7-l18": {
        "data_table": table(["Grain/Legume", "Common Use"], [
            ["Rice", "Side dish or base for many meals"], ["Lentils", "Soups and stews"],
        ]),
    },
    "cooking-g7-l19": {
        "data_table": table(["Step", "Why"], [
            ["Rinse under running water", "Removes dirt and bacteria"],
        ]),
    },
    "cooking-g7-l20": {
        "data_table": table(["Dish Type", "Example"], [
            ["Soup", "Chicken noodle soup"], ["Stew", "Beef stew"],
        ]),
    },
    "cooking-g7-l21": {
        "data_table": table(["Salad Element", "Example"], [
            ["Base", "Leafy greens"], ["Protein", "Grilled chicken or beans"],
        ]),
    },
    "cooking-g7-l22": {
        "data_table": table(["Dessert Type", "Example"], [
            ["Baked", "Cookies, cake"], ["No-bake", "Fruit salad, pudding"],
        ]),
    },
    "cooking-g7-l23": {
        "data_table": table(["Step", "Purpose"], [
            ["Creaming butter and sugar", "Adds air for a lighter texture"], ["Frosting", "Adds flavor and decoration"],
        ]),
    },
    "cooking-g7-l24": {
        "data_table": table(["Presentation Tip", "Why"], [
            ["Balanced colors", "Makes the dish visually appealing"], ["Clean plate edges", "Looks more professional"],
        ]),
    },
    "cooking-g7-l25": {
        "data_table": table(["Rule", "Why"], [
            ["Keep raw meat separate from other foods", "Prevents cross-contamination"],
            ["Cook food to a safe temperature", "Kills harmful bacteria"],
        ]),
    },
    "cooking-g7-l26": {
        "data_table": table(["Storage Method", "Purpose"], [
            ["Refrigeration", "Slows bacterial growth"], ["Freezing", "Preserves food for longer periods"],
        ]),
    },
    "cooking-g7-l27": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"], ["Sugar content", "How much sugar is in the food"],
        ]),
    },
    "cooking-g7-l28": {
        "data_table": table(["Tool", "Use"], [
            ["Measuring cup", "Measures liquids or dry ingredients"], ["Whisk", "Mixes ingredients together"],
        ]),
    },
    "cooking-g7-l29": {
        "data_table": table(["Protein Source", "Type"], [
            ["Lentils", "Plant-based"], ["Tofu", "Plant-based"],
        ]),
    },
    "cooking-g7-l30": {
        "data_table": table(["Breakfast Food", "Country"], [
            ["Congee", "China"], ["Full English breakfast", "United Kingdom"],
        ]),
    },
    "cooking-g7-l31": {
        "data_table": table(["Snack", "Key Ingredients"], [
            ["Energy balls", "Oats, honey, peanut butter"], ["Fruit skewers", "Cut fruit on a stick"],
        ]),
    },
    "cooking-g7-l32": {
        "data_table": table(["Fermented Food", "Made By"], [
            ["Yogurt", "Fermenting milk with bacteria cultures"], ["Bread (sourdough)", "Fermenting flour and water with wild yeast"],
        ]),
    },
    "cooking-g7-l33": {
        "data_table": table(["Street Food", "Country of Origin"], [
            ["Tacos", "Mexico"], ["Falafel", "Middle East"],
        ]),
    },
    "cooking-g7-l34": {
        "data_table": table(["Cuisine", "Signature Dish"], [
            ["Italian", "Pasta"], ["Indian", "Curry"],
        ]),
    },
    "cooking-g7-l35": {
        "data_table": table(["Holiday", "Traditional Food"], [
            ["Eid al-Fitr", "Sweet dishes like sheer khurma"], ["Thanksgiving", "Roast turkey"],
        ]),
    },
    "cooking-g7-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Farm-to-table", "Sourcing food directly from local farms"],
        ]),
    },
    "cooking-g7-l37": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Meal planning", "Reduces buying more than needed"], ["Composting scraps", "Reduces landfill waste"],
        ]),
    },
    "cooking-g7-l38": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Buying seasonal produce", "Often cheaper and fresher"], ["Cooking in bulk", "Saves money and time"],
        ]),
    },
    "cooking-g7-l39": {
        "data_table": table(["Allergen", "Common Substitute"], [
            ["Dairy milk", "Oat or almond milk"], ["Wheat flour", "Gluten-free flour blend"],
        ]),
    },
    "cooking-g7-l40": {
        "data_table": table(["Table Item", "Placement"], [
            ["Fork", "Left of the plate"], ["Knife and spoon", "Right of the plate"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Cooking lessons (completing 40/40).")


if __name__ == "__main__":
    main()
