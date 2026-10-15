#!/usr/bin/env python3
"""Depth pass, M2 Cooking: fill in real, hand-checked data_table
content for the M2 Cooking lessons not covered by the earlier
breadth-first batch. Brings M2 Cooking to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning food
chemistry and molecular gastronomy, fermentation science, food safety
engineering, and applied culinary technology/business; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls
within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_cooking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Maillard reaction", "A chemical reaction between amino acids and sugars that browns food and creates flavor"],
    ["Flavor compound formation", "Produces hundreds of new aroma and taste compounds as browning proceeds"],
])

CHARTS: dict[str, dict] = {
    "cooking-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Culinary arts management research", "Systematic scholarly methods for studying professional kitchen operations"],
    ])},
    "cooking-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Kitchen fundamentals/food safety research", "Rigorous study of the core principles underlying safe, professional food preparation"],
    ])},
    "cooking-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Enzymatic browning", "An oxidation reaction (e.g. in cut apples) controlled with acid or heat to slow discoloration"],
    ])},
    "cooking-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Spherification", "Uses alginate and calcium reactions to form a thin gel membrane around liquid droplets"],
    ])},
    "cooking-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Sous vide precision cooking", "Cooks food at a precisely controlled temperature to target exact protein denaturation points"],
    ])},
    "cooking-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Emulsification stability", "The mechanisms keeping oil and water dispersed together in a classical sauce"],
    ])},
    "cooking-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Hydrocolloid foam stabilization", "Uses gums to trap air bubbles and stabilize culinary foams"],
    ])},
    "cooking-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Sourdough fermentation ecology", "The interplay of wild yeast and bacteria that develops sourdough's characteristic flavor"],
    ])},
    "cooking-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Gluten network development", "Kneading develops gluten proteins into an elastic network that gives dough its structure"],
    ])},
    "cooking-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Starch retrogradation", "Recrystallization of starch molecules over time that causes baked goods to go stale"],
    ])},
    "cooking-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Fermentation pathway control", "Manages microbial activity to guide flavor development in pickling and brining"],
    ])},
    "cooking-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Koji fermentation", "A mold-based fermentation that breaks down starches and proteins to build umami flavor"],
    ])},
    "cooking-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Miso/soy sauce chemistry", "Long fermentation processes that develop deep umami and savory flavor complexity"],
    ])},
    "cooking-m2-l15": {"data_table": table(["Process", "Feature"], [
        ["Proteolysis", "Breaks down proteins during cheese ripening"],
        ["Lipolysis", "Breaks down fats during cheese ripening"],
    ])},
    "cooking-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Nitrite curing", "Preserves meat and inhibits botulism, with safety governed by specific concentration thresholds"],
    ])},
    "cooking-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Phenolic deposition (smoking)", "Smoke's phenolic compounds impart flavor and act as a natural preservative"],
    ])},
    "cooking-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Collagen-to-gelatin conversion", "Slow, moist heat breaks tough collagen into tender, rich gelatin"],
    ])},
    "cooking-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Myoglobin color transition", "Meat color changes as myoglobin's oxidation state shifts with cooking temperature"],
    ])},
    "cooking-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Dry-aging", "Controlled enzymatic breakdown that tenderizes meat and concentrates its flavor over time"],
    ])},
    "cooking-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Vacuum marination", "Reduced pressure accelerates mass transfer of marinade flavors into food"],
    ])},
    "cooking-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Osmotic dehydration", "Uses a concentrated solution to draw water out of fruit for preservation"],
    ])},
    "cooking-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Freeze-drying optimization", "Removes water via sublimation to preserve ingredients while retaining structure and flavor"],
    ])},
    "cooking-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Cryogenic freezing (plating)", "Uses liquid nitrogen for near-instant freezing effects in modernist presentation"],
    ])},
    "cooking-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Pressure cooking thermodynamics", "Elevated pressure raises boiling point, cooking food faster at higher temperature"],
    ])},
    "cooking-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Oil polymerization (frying)", "Repeated heating degrades frying oil, forming compounds that affect flavor and safety"],
    ])},
    "cooking-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Smoke point", "The temperature at which an oil begins to visibly smoke and break down, varying by fatty acid profile"],
    ])},
    "cooking-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Caramelization", "Sugar breaks down under heat alone (no protein needed) to form browned, complex flavors"],
    ])},
    "cooking-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Sugar crystallization control", "Manages crystal size and formation to achieve desired confectionery texture"],
    ])},
    "cooking-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Chocolate tempering", "Controls cocoa butter crystal structure for glossy, snapping chocolate"],
    ])},
    "cooking-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Ice cream overrun", "The percentage of air whipped into ice cream, affecting its texture and yield"],
    ])},
    "cooking-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Pectin gel network", "Pectin, sugar, and acid combine to form the gel structure of fruit preserves"],
    ])},
    "cooking-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Custard/curd thickening", "Egg proteins denature and coagulate under controlled heat to thicken a custard"],
    ])},
    "cooking-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Meringue/souffle aeration", "Whipped protein foams trap air that expands with heat to create rise and structure"],
    ])},
    "cooking-m2-l35": {"data_table": table(["Type", "Feature"], [
        ["Chemical leavening", "Baking soda/powder release gas via acid-base reaction"],
        ["Biological leavening", "Yeast ferments sugars to release carbon dioxide"],
    ])},
    "cooking-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Flavor infusion extraction", "Transfers volatile aroma compounds from an ingredient into a liquid medium"],
    ])},
    "cooking-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Sensory evaluation methodology", "Structured, standardized approaches for professionally testing and comparing food quality"],
    ])},
    "cooking-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Umami/glutamate synergy", "Glutamate combined with certain nucleotides produces a synergistic boost in umami taste"],
    ])},
    "cooking-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Retronasal aroma perception", "Aroma compounds travel from the mouth to the nose internally, shaping perceived flavor"],
    ])},
    "cooking-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Food pairing theory", "Proposes ingredients sharing key aromatic compounds tend to pair well together"],
    ])},
    "cooking-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Texture analysis instrumentation", "Uses mechanical devices to objectively measure food firmness, chewiness, and texture"],
    ])},
    "cooking-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Water activity", "Measures unbound water available for microbial growth, key to food shelf stability"],
    ])},
    "cooking-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["HACCP", "Hazard Analysis Critical Control Points; a systematic food safety management framework"],
    ])},
    "cooking-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Thermal death time curve", "Plots the time and temperature combinations needed to reduce pathogen levels to safe limits"],
    ])},
    "cooking-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Cross-contamination risk modeling", "Analyzes kitchen workflow to minimize pathogen transfer between food items"],
    ])},
    "cooking-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Modified atmosphere packaging", "Alters gas composition around food to extend its shelf life"],
    ])},
    "cooking-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Wild fermentation risk assessment", "Evaluates safety hazards specific to uncontrolled, naturally-occurring fermentation"],
    ])},
    "cooking-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Allergen cross-contact prevention", "Protocols preventing unintended allergen transfer in commercial kitchens"],
    ])},
    "cooking-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Plant-based protein extrusion", "A processing technology that structures plant proteins into meat-like textures"],
    ])},
    "cooking-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Fat replacement strategy", "Formulates reduced-calorie recipes while preserving mouthfeel and function of fat"],
    ])},
    "cooking-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Gluten-free structural substitution", "Uses alternative binders and starches to replace gluten's structural role in baking"],
    ])},
    "cooking-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Malolactic fermentation", "Converts sharp malic acid to softer lactic acid in wine, controlled for desired style"],
    ])},
    "cooking-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Mashing (beer brewing)", "Enzymes convert grain starches into fermentable sugars during the mashing process"],
    ])},
    "cooking-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Distillation fraction separation", "Separates alcohol and flavor compounds by their different boiling points"],
    ])},
    "cooking-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Coffee extraction kinetics", "Optimizes brewing variables (grind, time, temperature) to extract desired flavor compounds"],
    ])},
    "cooking-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Tea polyphenol oxidation", "Controlled oxidation level during processing determines tea type (green, oolong, black)"],
    ])},
    "cooking-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Sauce viscosity engineering", "Applies rheology to design a sauce's desired flow and thickness properties"],
    ])},
    "cooking-m2-l58": {"data_table": table(["Hydrocolloid", "Feature"], [
        ["Agar", "Sets firm at room temperature, derived from seaweed"],
        ["Xanthan", "Thickens without heat, very shear-thinning"],
        ["Gellan", "Forms brittle, clear gels"],
    ])},
    "cooking-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Vacuum impregnation", "Reduced pressure forces flavor liquid into porous food's internal air spaces"],
    ])},
    "cooking-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Ultrasonic processing", "Uses sound waves to emulsify, tenderize, or extract flavor in modern culinary technique"],
    ])},
    "cooking-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Centrifugation (clarification)", "Spins liquids at high speed to separate and clarify components in modernist cuisine"],
    ])},
    "cooking-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Rotary evaporation", "Distills at low temperature under vacuum to capture delicate culinary essences"],
    ])},
    "cooking-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Dehydrator airflow optimization", "Ensures even air circulation for uniform drying across a food dehydrator"],
    ])},
    "cooking-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Nixtamalization", "An alkaline treatment of corn that improves nutrition and flavor for traditional masa"],
    ])},
    "cooking-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Endangered culinary tradition codification", "Documents disappearing regional recipes and techniques for preservation"],
    ])},
    "cooking-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Historical recipe reconstruction", "Scholarly methods for accurately recreating dishes from historical written sources"],
    ])},
    "cooking-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Fish sauce fermentation", "Long proteolytic fermentation breaks down fish protein into savory, umami-rich sauce"],
    ])},
    "cooking-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Curing salt diffusion modeling", "Predicts how salt moves through whole-muscle meat during the curing process"],
    ])},
    "cooking-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Vegan egg replacement", "Matches the functional properties (binding, leavening) of eggs using plant alternatives"],
    ])},
    "cooking-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Nutrient retention across cooking methods", "Compares how different cooking techniques affect vitamin and mineral content"],
    ])},
    "cooking-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Glycemic response modulation", "Cooking and preparation technique can alter a food's blood sugar impact"],
    ])},
    "cooking-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Bitter compound masking", "Strategies for reducing perceived bitterness in functional food formulation"],
    ])},
    "cooking-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Menu engineering matrix", "Analyzes dishes by cost, popularity, and profitability to optimize a menu"],
    ])},
    "cooking-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Brigade system ergonomics", "Optimizes kitchen workflow and station organization for efficiency"],
    ])},
    "cooking-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Recipe scaling mathematics", "Mathematically converts recipes for volume production while preserving ratios"],
    ])},
    "cooking-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Sensory shelf-life testing", "Structured protocols for evaluating how food quality changes over storage time"],
    ])},
    "cooking-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Flavor encapsulation", "Technology that releases flavor compounds in a controlled, delayed manner"],
    ])},
    "cooking-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["3D food printing", "Requires specific rheological properties in food material to be extrudable and hold shape"],
    ])},
    "cooking-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Plating composition theory", "Uses visual balance and negative space to design an appealing plated dish"],
    ])},
    "cooking-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Temperature gradient control (plating)", "Manages differing temperatures of components assembled on the same plate"],
    ])},
    "cooking-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Wine and food structural pairing", "Analyzes how a wine's acidity, tannin, and body interact with a dish's structure"],
    ])},
    "cooking-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Spice blend formulation", "Balances volatile aroma compounds when designing a spice blend"],
    ])},
    "cooking-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Salt crystal structure", "Crystal shape and size affect how quickly and intensely saltiness is perceived"],
    ])},
    "cooking-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Acid balance theory", "Balances acidity against fat, salt, and sweetness in sauce and dressing formulation"],
    ])},
    "cooking-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Osmotic equilibrium (brining)", "Salt concentration gradients drive moisture retention in brined poultry and seafood"],
    ])},
    "cooking-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Pastry lamination physics", "Alternating fat and dough layers create steam-driven flakiness during baking"],
    ])},
    "cooking-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Choux pastry expansion", "Starch gelatinization and trapped steam drive choux pastry's characteristic puff"],
    ])},
    "cooking-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Transglutaminase bonding", "An enzyme that binds proteins together, used to fuse separate pieces of meat or food"],
    ])},
    "cooking-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Food waste valorization", "Converts kitchen byproducts and scraps into usable culinary products"],
    ])},
    "cooking-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Fermentation vessel material science", "Different vessel materials affect flavor development during fermentation"],
    ])},
    "cooking-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Vacuum distillation (alcohol removal)", "Removes alcohol from a liquid at low temperature while preserving flavor"],
    ])},
    "cooking-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Bread crust formation", "Maillard reaction and moisture loss combine to control crust color and thickness"],
    ])},
    "cooking-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Egg white whipping kinetics", "Protein denaturation and unfolding create the structure of whipped egg white foam"],
    ])},
    "cooking-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Anthocyanin pH stability", "Anthocyanin pigments change color depending on the acidity of their environment"],
    ])},
    "cooking-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Antioxidant additive stability (smoking)", "Studies how added antioxidants interact with the smoking process"],
    ])},
    "cooking-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Reverse spherification", "Forms a more durable gel membrane by reversing the standard spherification reaction order"],
    ])},
    "cooking-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Vacuum-sealed marinade modeling", "Predicts marinade penetration depth and uniformity under vacuum sealing"],
    ])},
    "cooking-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Liposomal flavor encapsulation", "Uses lipid vesicles to deliver flavor compounds in a controlled way"],
    ])},
    "cooking-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Hot sauce microbial succession", "Tracks how different microbial populations rise and fall as fermented hot sauce develops"],
    ])},
    "cooking-m2-l100": {"data_table": table(["Component", "Purpose"], [
        ["Thesis-level capstone", "Develops and evaluates an original culinary technique as graduate-level research"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"cooking-m2-l{base_n}"
    worked_key = f"cooking-m2-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Cooking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Cooking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Cooking lessons.")


if __name__ == "__main__":
    main()
