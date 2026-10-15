#!/usr/bin/env python3
"""Depth pass, Grade 5 Cooking: fill in real, hand-checked data_table
content for the 28 Grade 5 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 5 Cooking to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g5-l1": {
        "data_table": table(["Food Group", "Example"], [
            ["Grains", "Bread, rice"], ["Protein", "Chicken, beans"], ["Dairy", "Milk, cheese"],
        ]),
    },
    "cooking-g5-l2": {
        "data_table": table(["Rule", "Why"], [
            ["Wash hands before cooking", "Removes germs"], ["Ask an adult before using sharp tools", "Prevents injury"],
        ]),
    },
    "cooking-g5-l3": {
        "data_table": table(["Recipe Part", "Purpose"], [
            ["Ingredients list", "What you need"], ["Instructions", "The steps to follow, in order"],
        ]),
    },
    "cooking-g5-l5": {
        "data_table": table(["MyPlate Section", "Example"], [
            ["Fruits", "Apples, bananas"], ["Vegetables", "Carrots, broccoli"], ["Grains", "Bread, rice"],
        ]),
    },
    "cooking-g5-l6": {
        "data_table": table(["Rule", "Why"], [
            ["Cut away from your body", "Prevents injury"], ["Use a cutting board", "Protects the counter and knife"],
        ]),
    },
    "cooking-g5-l7": {
        "data_table": table(["Salad Ingredient", "Example"], [
            ["Greens", "Lettuce, spinach"], ["Dressing", "Olive oil and vinegar"],
        ]),
    },
    "cooking-g5-l8": {
        "data_table": table(["Technique", "Description"], [
            ["Creaming", "Mixing butter and sugar until fluffy"], ["Folding", "Gently combining ingredients"],
        ]),
    },
    "cooking-g5-l9": {
        "data_table": table(["Label Info", "What It Tells You"], [
            ["Serving size", "How much counts as one portion"], ["Sugar content", "How much sugar is in the food"],
        ]),
    },
    "cooking-g5-l10": {
        "data_table": table(["Rule", "Why"], [
            ["Keep raw meat separate from other foods", "Prevents cross-contamination"],
            ["Use separate cutting boards", "Avoids spreading bacteria"],
        ]),
    },
    "cooking-g5-l11": {
        "data_table": table(["Storage Method", "Purpose"], [
            ["Refrigeration", "Slows bacterial growth"], ["Freezing", "Preserves food for longer periods"],
        ]),
    },
    "cooking-g5-l13": {
        "data_table": table(["Step", "Purpose"], [
            ["Read the whole recipe first", "Avoids surprises mid-cooking"], ["Prep ingredients ahead", "Speeds up cooking"],
        ]),
    },
    "cooking-g5-l14": {
        "data_table": table(["Planning Step", "Purpose"], [
            ["List meals for the week", "Saves time and reduces waste"],
        ]),
    },
    "cooking-g5-l15": {
        "data_table": table(["Cuisine", "Signature Dish"], [
            ["Italian", "Pasta"], ["Mexican", "Tacos"], ["Indian", "Curry"],
        ]),
    },
    "cooking-g5-l16": {
        "data_table": table(["Herb/Spice", "Common Use"], [
            ["Basil", "Italian dishes"], ["Cumin", "Middle Eastern and South Asian dishes"],
        ]),
    },
    "cooking-g5-l17": {
        "data_table": table(["Breakfast Food", "Food Group"], [
            ["Oatmeal", "Grains"], ["Eggs", "Protein"],
        ]),
    },
    "cooking-g5-l18": {
        "data_table": table(["Snack", "Key Ingredients"], [
            ["Fruit skewers", "Cut fruit on a stick"], ["Energy balls", "Oats, honey, peanut butter"],
        ]),
    },
    "cooking-g5-l19": {
        "data_table": table(["Food", "Example Portion"], [
            ["Cooked rice", "About the size of a fist"], ["Meat", "About the size of a deck of cards"],
        ]),
    },
    "cooking-g5-l20": {
        "data_table": table(["Bread Ingredient", "Purpose"], [
            ["Flour", "Provides structure"], ["Yeast", "Makes the dough rise"],
        ]),
    },
    "cooking-g5-l21": {
        "data_table": table(["Allergen", "Common Substitute"], [
            ["Dairy milk", "Oat or almond milk"], ["Wheat flour", "Gluten-free flour blend"],
        ]),
    },
    "cooking-g5-l22": {
        "data_table": table(["Table Item", "Placement"], [
            ["Fork", "Left of the plate"], ["Knife and spoon", "Right of the plate"],
        ]),
    },
    "cooking-g5-l23": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Meal planning", "Reduces buying more than needed"], ["Composting scraps", "Reduces landfill waste"],
        ]),
    },
    "cooking-g5-l24": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooking in fully submerged simmering water"], ["Scrambling", "Whisking and cooking in a pan"],
        ]),
    },
    "cooking-g5-l25": {
        "data_table": table(["Protein Source", "Type"], [
            ["Lentils", "Plant-based"], ["Tofu", "Plant-based"], ["Chicken", "Animal-based"],
        ]),
    },
    "cooking-g5-l26": {
        "data_table": table(["Benefit", "Detail"], [
            ["Seasonal produce", "Often fresher and less expensive"], ["Local produce", "Reduces transportation impact"],
        ]),
    },
    "cooking-g5-l27": {
        "data_table": table(["Dessert Type", "Example"], [
            ["Baked", "Cookies, cake"], ["No-bake", "Fruit salad, pudding"],
        ]),
    },
    "cooking-g5-l28": {
        "data_table": table(["Tool", "Use"], [
            ["Measuring cup", "Measures liquids or dry ingredients"], ["Whisk", "Mixes ingredients together"],
        ]),
    },
    "cooking-g5-l29": {
        "data_table": table(["Hosting Step", "Purpose"], [
            ["Plan the menu", "Ensures a balanced meal"], ["Set the table", "Prepares for guests"],
        ]),
    },
    "cooking-g5-l30": {
        "data_table": table(["Cleanup Step", "Purpose"], [
            ["Wash dishes promptly", "Prevents food from hardening"], ["Wipe down surfaces", "Removes germs and crumbs"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Cooking lessons (completing 30/30).")


if __name__ == "__main__":
    main()
