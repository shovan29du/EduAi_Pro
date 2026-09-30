#!/usr/bin/env python3
"""Depth pass, Grade 10 Cooking: fill in real, hand-checked data_table
content for the Grade 10 Cooking lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Cooking to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "cook-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Food entrepreneurship", "Starting and running a food-related business"],
        ]),
    },
    "cooking-g10-l2": {
        "data_table": table(["Rule", "Reason"], [
            ["Wash hands before cooking", "Prevents contamination"], ["Keep raw meat separate", "Avoids cross-contamination"],
        ]),
    },
    "cooking-g10-l3": {
        "data_table": table(["Cut", "Description"], [
            ["Julienne", "Thin matchstick-sized strips"], ["Dice", "Small cube shapes"],
        ]),
    },
    "cooking-g10-l4": {
        "data_table": table(["Tool", "Use"], [
            ["Chef's knife", "General-purpose cutting"], ["Cutting board", "Protects surfaces and knives"],
        ]),
    },
    "cooking-g10-l6": {
        "data_table": table(["Method", "Description"], [
            ["Boiling", "Cooking in water at 100C / 212F"], ["Simmering", "Cooking just below boiling point"],
        ]),
    },
    "cooking-g10-l7": {
        "data_table": table(["Method", "Description"], [
            ["Sauteing", "Quick cooking in a small amount of fat over high heat"], ["Frying", "Cooking submerged in hot oil"],
        ]),
    },
    "cooking-g10-l8": {
        "data_table": table(["Method", "Description"], [
            ["Roasting", "Cooking with dry heat in an oven"], ["Baking", "Cooking with dry heat, often for breads and desserts"],
        ]),
    },
    "cooking-g10-l9": {
        "data_table": table(["Method", "Description"], [
            ["Grilling", "Cooking with direct heat from below"],
        ]),
    },
    "cooking-g10-l10": {
        "data_table": table(["Item", "Type"], [
            ["Basil", "Fresh herb"], ["Cumin", "Dried spice"],
        ]),
    },
    "cooking-g10-l12": {
        "data_table": table(["Sauce", "Base"], [
            ["Bechamel", "Milk and roux (butter and flour)"], ["Tomato sauce", "Cooked tomatoes"],
        ]),
    },
    "cooking-g10-l13": {
        "data_table": table(["Ingredient", "Role"], [
            ["Flour", "Provides structure"], ["Yeast", "Leavens the dough"],
        ]),
    },
    "cooking-g10-l14": {
        "data_table": table(["Ingredient", "Role"], [
            ["Baking powder", "Leavens the batter"], ["Sugar", "Sweetens and helps browning"],
        ]),
    },
    "cooking-g10-l15": {
        "data_table": table(["Technique", "Description"], [
            ["Poaching an egg", "Cooking in gently simmering water without the shell"],
        ]),
    },
    "cooking-g10-l16": {
        "data_table": table(["Grain", "Cooking Ratio (grain:water)"], [
            ["White rice", "1 : 2"], ["Quinoa", "1 : 2"],
        ]),
    },
    "cooking-g10-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Legumes", "Include beans, lentils, and chickpeas, high in fiber and protein"],
        ]),
    },
    "cooking-g10-l18": {
        "data_table": table(["Technique", "Purpose"], [
            ["Blanching", "Briefly boils then cools vegetables to preserve color and texture"],
        ]),
    },
    "cooking-g10-l19": {
        "data_table": table(["Practice", "Reason"], [
            ["Cook meat to safe internal temperature", "Kills harmful bacteria"],
        ]),
    },
    "cooking-g10-l20": {
        "data_table": table(["Practice", "Reason"], [
            ["Buy fresh, properly stored seafood", "Reduces spoilage-related illness"],
        ]),
    },
    "cooking-g10-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Plant-based cooking", "Uses ingredients derived entirely from plants"],
        ]),
    },
    "cooking-g10-l22": {
        "data_table": table(["Macronutrient", "Role"], [
            ["Protein", "Builds and repairs tissue"], ["Carbohydrates", "Main energy source"],
        ]),
    },
    "cooking-g10-l23": {
        "data_table": table(["Meal Element", "Purpose"], [
            ["Protein", "Supports muscle and tissue repair"], ["Vegetables", "Provide fiber and micronutrients"],
        ]),
    },
    "cooking-g10-l24": {
        "data_table": table(["Step", "Purpose"], [
            ["Plan meals ahead", "Saves money and reduces waste"],
        ]),
    },
    "cooking-g10-l25": {
        "data_table": table(["Practice", "Reason"], [
            ["Store meat below 4C / 40F", "Slows bacterial growth"],
        ]),
    },
    "cooking-g10-l26": {
        "data_table": table(["Label Element", "Meaning"], [
            ["Serving size", "The amount the nutrition facts are based on"],
        ]),
    },
    "cooking-g10-l27": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Olive oil", "Staple fat in Mediterranean cooking"],
        ]),
    },
    "cooking-g10-l28": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Soy sauce", "Common seasoning in East Asian cooking"],
        ]),
    },
    "cooking-g10-l29": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Curry spices", "Common in South Asian cooking"],
        ]),
    },
    "cooking-g10-l30": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Za'atar", "Common Middle Eastern spice blend"],
        ]),
    },
    "cooking-g10-l31": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Corn and beans", "Staples in Latin American cooking"],
        ]),
    },
    "cooking-g10-l32": {
        "data_table": table(["Cuisine Feature", "Example"], [
            ["Berbere spice blend", "Common in Ethiopian and East African cooking"],
        ]),
    },
    "cooking-g10-l33": {
        "data_table": table(["Fermented Food", "Fermenting Agent"], [
            ["Yogurt", "Bacterial culture"], ["Sauerkraut", "Naturally occurring bacteria"],
        ]),
    },
    "cooking-g10-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock", "Liquid made by simmering bones and vegetables"],
        ]),
    },
    "cooking-g10-l35": {
        "data_table": table(["Dressing", "Base"], [
            ["Vinaigrette", "Oil and vinegar"],
        ]),
    },
    "cooking-g10-l36": {
        "data_table": table(["Leavening Agent", "How It Works"], [
            ["Baking soda", "Reacts with acid to release CO2"], ["Yeast", "Ferments sugars to release CO2"],
        ]),
    },
    "cooking-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Maillard reaction", "Chemical reaction between amino acids and sugars that browns food"],
        ]),
    },
    "cooking-g10-l38": {
        "data_table": table(["Practice", "Benefit"], [
            ["Choosing seasonal produce", "Reduces environmental impact and often costs less"],
        ]),
    },
    "cooking-g10-l39": {
        "data_table": table(["Practice", "Benefit"], [
            ["Using vegetable scraps for stock", "Reduces waste"],
        ]),
    },
    "cooking-g10-l40": {
        "data_table": table(["Principle", "Reason"], [
            ["Balance color and height", "Makes a dish visually appealing"],
        ]),
    },
    "cooking-g10-l41": {
        "data_table": table(["Ingredient", "Role"], [
            ["Butter", "Adds richness and flavor to cookies"],
        ]),
    },
    "cooking-g10-l42": {
        "data_table": table(["Dessert Element", "Example"], [
            ["Custard base", "Used in creme brulee and ice cream"],
        ]),
    },
    "cooking-g10-l43": {
        "data_table": table(["Beverage", "Method"], [
            ["Mocktail", "Non-alcoholic mixed drink"],
        ]),
    },
    "cooking-g10-l44": {
        "data_table": table(["Restriction", "Common Substitute"], [
            ["Gluten-free", "Rice or almond flour"], ["Dairy-free", "Oat or almond milk"],
        ]),
    },
    "cooking-g10-l45": {
        "data_table": table(["Practice", "Benefit"], [
            ["Batch cooking", "Saves time across the week"],
        ]),
    },
    "cooking-g10-l46": {
        "data_table": table(["Tradition", "Example"], [
            ["Shared family meals", "Common cultural practice across many societies"],
        ]),
    },
    "cooking-g10-l47": {
        "data_table": table(["Concept", "Purpose"], [
            ["Cost per serving", "Helps price a menu item profitably"],
        ]),
    },
    "cooking-g10-l48": {
        "data_table": table(["Step", "Purpose"], [
            ["Substituting ingredients", "Adapts a recipe for taste or dietary needs"],
        ]),
    },
    "cooking-g10-l49": {
        "data_table": table(["Element", "Purpose"], [
            ["Natural lighting", "Makes food photography look more appetizing"],
        ]),
    },
    "cooking-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Farm-to-table", "Sourcing food directly from local producers"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Cooking lessons (completing 50/50).")


if __name__ == "__main__":
    main()
