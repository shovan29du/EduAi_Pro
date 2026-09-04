#!/usr/bin/env python3
"""Depth pass, Grade 9 Cooking: fill in real, hand-checked data_table
content for the 48 Grade 9 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Cooking to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g9-l1": {
        "data_table": table(["Technique", "Description"], [
            ["Sous vide", "Cooking food sealed in a bag at a precise low temperature"],
        ]),
    },
    "cooking-g9-l2": {
        "data_table": table(["Rule", "Reason"], [
            ["Wash hands before cooking", "Prevents contamination"], ["Keep raw meat separate", "Avoids cross-contamination"],
        ]),
    },
    "cooking-g9-l3": {
        "data_table": table(["Cut", "Description"], [
            ["Julienne", "Thin matchstick-sized strips"], ["Dice", "Small cube shapes"],
        ]),
    },
    "cooking-g9-l4": {
        "data_table": table(["Practice", "Reason"], [
            ["Cook meat to safe internal temperature", "Kills harmful bacteria"],
        ]),
    },
    "cooking-g9-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Ingredient list", "What you need"], ["Method", "The steps to follow"],
        ]),
    },
    "cooking-g9-l7": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooking in water at 100C / 212F"], ["Simmering", "Cooking just below boiling point"],
        ]),
    },
    "cooking-g9-l8": {
        "data_table": table(["Method", "Description"], [
            ["Sauteing", "Quick cooking in a small amount of fat over high heat"], ["Frying", "Cooking submerged in hot oil"],
        ]),
    },
    "cooking-g9-l9": {
        "data_table": table(["Method", "Description"], [
            ["Roasting", "Cooking with dry heat in an oven, often meat or vegetables"], ["Baking", "Cooking with dry heat, often for breads and desserts"],
        ]),
    },
    "cooking-g9-l10": {
        "data_table": table(["Method", "Description"], [
            ["Grilling", "Cooking with direct heat from below"],
        ]),
    },
    "cooking-g9-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Water boils at", "100C / 212F at sea level"],
        ]),
    },
    "cooking-g9-l12": {
        "data_table": table(["Ingredient", "Role"], [
            ["Flour", "Provides structure"], ["Yeast", "Leavens the dough"],
        ]),
    },
    "cooking-g9-l13": {
        "data_table": table(["Pastry Type", "Example"], [
            ["Puff pastry", "Flaky, layered dough used in croissants"],
        ]),
    },
    "cooking-g9-l14": {
        "data_table": table(["Ingredient", "Role"], [
            ["Baking powder", "Leavens the cake batter"], ["Sugar", "Sweetens and helps browning"],
        ]),
    },
    "cooking-g9-l16": {
        "data_table": table(["Sauce", "Base"], [
            ["Bechamel", "Milk and roux (butter and flour)"], ["Tomato sauce", "Cooked tomatoes"],
        ]),
    },
    "cooking-g9-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock", "Liquid made by simmering bones and vegetables"], ["Broth", "Liquid made by simmering meat, often seasoned"],
        ]),
    },
    "cooking-g9-l18": {
        "data_table": table(["Soup Type", "Example"], [
            ["Clear soup", "Broth-based"], ["Cream soup", "Thickened with cream or a roux"],
        ]),
    },
    "cooking-g9-l19": {
        "data_table": table(["Dressing", "Base"], [
            ["Vinaigrette", "Oil and vinegar"],
        ]),
    },
    "cooking-g9-l20": {
        "data_table": table(["Technique", "Description"], [
            ["Poaching an egg", "Cooking in gently simmering water without the shell"],
        ]),
    },
    "cooking-g9-l21": {
        "data_table": table(["Dairy Product", "Use"], [
            ["Cream", "Adds richness to sauces and desserts"], ["Cheese", "Adds flavor and texture"],
        ]),
    },
    "cooking-g9-l22": {
        "data_table": table(["Practice", "Reason"], [
            ["Cook beef to a safe temperature", "Prevents foodborne illness"],
        ]),
    },
    "cooking-g9-l23": {
        "data_table": table(["Practice", "Reason"], [
            ["Cook poultry to 165F/74C internal temp", "Kills salmonella and other bacteria"],
        ]),
    },
    "cooking-g9-l24": {
        "data_table": table(["Practice", "Reason"], [
            ["Buy fresh, properly stored seafood", "Reduces the risk of spoilage-related illness"],
        ]),
    },
    "cooking-g9-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Vegetarian", "Diet that excludes meat but may include dairy and eggs"],
        ]),
    },
    "cooking-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Vegan", "Diet excluding all animal products, including dairy and eggs"],
        ]),
    },
    "cooking-g9-l27": {
        "data_table": table(["Grain", "Cooking Ratio (grain:water)"], [
            ["White rice", "1 : 2"], ["Quinoa", "1 : 2"],
        ]),
    },
    "cooking-g9-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Al dente", "Pasta cooked firm to the bite"],
        ]),
    },
    "cooking-g9-l29": {
        "data_table": table(["Item", "Type"], [
            ["Basil", "Fresh herb"], ["Cumin", "Dried spice"],
        ]),
    },
    "cooking-g9-l30": {
        "data_table": table(["Flavor", "Balances With"], [
            ["Sweet", "Sour or bitter"], ["Salty", "Acid or fat"],
        ]),
    },
    "cooking-g9-l31": {
        "data_table": table(["Macronutrient", "Role"], [
            ["Protein", "Builds and repairs tissue"], ["Carbohydrates", "Main energy source"],
        ]),
    },
    "cooking-g9-l32": {
        "data_table": table(["Step", "Purpose"], [
            ["Plan meals ahead", "Saves money and reduces waste"],
        ]),
    },
    "cooking-g9-l33": {
        "data_table": table(["Label Element", "Meaning"], [
            ["Serving size", "The amount the nutrition facts are based on"],
        ]),
    },
    "cooking-g9-l34": {
        "data_table": table(["Method", "How It Works"], [
            ["Canning", "Seals food in jars and heats to kill microbes"], ["Pickling", "Preserves food in an acidic vinegar brine"],
        ]),
    },
    "cooking-g9-l35": {
        "data_table": table(["Method", "How It Works"], [
            ["Freezing", "Slows microbial growth with cold"], ["Drying", "Removes moisture microbes need to grow"],
        ]),
    },
    "cooking-g9-l36": {
        "data_table": table(["Fermented Food", "Fermenting Agent"], [
            ["Yogurt", "Bacterial culture"], ["Sauerkraut", "Naturally occurring bacteria"],
        ]),
    },
    "cooking-g9-l37": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Olive oil", "Staple fat in Mediterranean cooking"],
        ]),
    },
    "cooking-g9-l38": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Soy sauce", "Common seasoning in East Asian cooking"],
        ]),
    },
    "cooking-g9-l39": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Curry spices", "Common in South Asian cooking"],
        ]),
    },
    "cooking-g9-l40": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Za'atar", "Common Middle Eastern spice blend"],
        ]),
    },
    "cooking-g9-l41": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Corn and beans", "Staples in Latin American cooking"],
        ]),
    },
    "cooking-g9-l42": {
        "data_table": table(["Flour", "Note"], [
            ["Almond flour", "Gluten-free, nutty flavor"],
        ]),
    },
    "cooking-g9-l43": {
        "data_table": table(["Principle", "Reason"], [
            ["Balance color and height", "Makes a dish visually appealing"],
        ]),
    },
    "cooking-g9-l44": {
        "data_table": table(["Practice", "Benefit"], [
            ["Use vegetable scraps for stock", "Reduces waste"],
        ]),
    },
    "cooking-g9-l45": {
        "data_table": table(["Practice", "Benefit"], [
            ["Choosing local, seasonal produce", "Reduces environmental impact"],
        ]),
    },
    "cooking-g9-l46": {
        "data_table": table(["Allergen", "Common Substitute"], [
            ["Dairy milk", "Oat or almond milk"], ["Wheat flour", "Gluten-free flour blend"],
        ]),
    },
    "cooking-g9-l47": {
        "data_table": table(["Dough Type", "Use"], [
            ["Shortcrust pastry", "Base for pies and tarts"],
        ]),
    },
    "cooking-g9-l48": {
        "data_table": table(["Dessert Element", "Example"], [
            ["Custard base", "Used in creme brulee and ice cream"],
        ]),
    },
    "cooking-g9-l49": {
        "data_table": table(["Beverage", "Method"], [
            ["Tea", "Steeping leaves in hot water"], ["Coffee", "Brewing ground beans with hot water"],
        ]),
    },
    "cooking-g9-l50": {
        "data_table": table(["Equipment", "Care"], [
            ["Cast iron pan", "Season with oil to prevent rust"], ["Knives", "Hand wash and dry immediately"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Cooking lessons (completing 50/50).")


if __name__ == "__main__":
    main()
