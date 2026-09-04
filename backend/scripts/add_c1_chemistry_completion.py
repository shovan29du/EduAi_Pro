#!/usr/bin/env python3
"""Depth pass, C1 Chemistry: fill in real, hand-checked data_table and
formulae content for the 69 C1 Chemistry lessons not covered by the
earlier breadth-first batch. Brings C1 Chemistry to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "chemistry-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Inorganic chemistry", "The study of compounds not primarily based on carbon-hydrogen bonds"],
        ]),
    },
    "chemistry-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Organic chemistry", "The study of carbon-containing compounds and their reactions"],
        ]),
    },
    "chemistry-c1-l4": {
        "data_table": table(["Feature", "Trend"], [
            ["Atomic radius", "Increases down a group, decreases across a period"],
        ]),
    },
    "chemistry-c1-l5": {
        "data_table": table(["Orbital", "Max Electrons"], [
            ["s", "2"], ["p", "6"], ["d", "10"],
        ]),
    },
    "chemistry-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Ionic bond", "Electrostatic attraction between oppositely charged ions"],
        ]),
    },
    "chemistry-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Covalent bond", "A bond formed by sharing electron pairs between atoms"],
        ]),
    },
    "chemistry-c1-l8": {
        "data_table": table(["Shape", "Example"], [
            ["Tetrahedral", "CH4, four bonding pairs, no lone pairs"], ["Bent", "H2O, two bonding pairs, two lone pairs"],
        ]),
    },
    "chemistry-c1-l9": {
        "data_table": table(["Term", "Value"], [
            ["Avogadro's number", "6.022 × 10^23 particles per mole"],
        ]),
        "formulae": ["N_A = 6.022e23"],
    },
    "chemistry-c1-l10": {
        "data_table": table(["Reaction", "Balanced Equation"], [
            ["Combustion of methane", "CH4 + 2 O2 -> CO2 + 2 H2O"],
        ]),
        "formulae": ["CH4 + 2*O2 -> CO2 + 2*H2O"],
    },
    "chemistry-c1-l11": {
        "data_table": table(["Type", "Example"], [
            ["Synthesis", "A + B -> AB"], ["Decomposition", "AB -> A + B"],
        ]),
    },
    "chemistry-c1-l12": {
        "data_table": table(["Phase Change", "Direction"], [
            ["Melting", "Solid to liquid"], ["Sublimation", "Solid directly to gas"],
        ]),
    },
    "chemistry-c1-l13": {
        "data_table": table(["Law", "Formula"], [
            ["Boyle's law", "P1 V1 = P2 V2"], ["Charles's law", "V1/T1 = V2/T2"],
        ]),
        "formulae": ["P1 * V1 = P2 * V2", "V1 / T1 = V2 / T2"],
    },
    "chemistry-c1-l14": {
        "data_table": table(["Quantity", "Formula"], [
            ["Molarity", "M = moles of solute / liters of solution"],
        ]),
        "formulae": ["M = moles_solute / liters_solution"],
    },
    "chemistry-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Acid", "A substance that donates protons or accepts electron pairs"], ["Base", "A substance that accepts protons or donates electron pairs"],
        ]),
    },
    "chemistry-c1-l16": {
        "data_table": table(["Process", "Detail"], [
            ["Oxidation", "Loss of electrons"], ["Reduction", "Gain of electrons"],
        ]),
    },
    "chemistry-c1-l17": {
        "data_table": table(["Type", "Detail"], [
            ["Exothermic", "Releases energy to the surroundings"], ["Endothermic", "Absorbs energy from the surroundings"],
        ]),
    },
    "chemistry-c1-l18": {
        "data_table": table(["Factor", "Effect"], [
            ["Temperature", "Higher temperature generally increases reaction rate"], ["Concentration", "Higher concentration generally increases reaction rate"],
        ]),
    },
    "chemistry-c1-l19": {
        "data_table": table(["Type", "Example"], [
            ["Alkane", "Methane, CH4, single bonds only"], ["Alkene", "Ethene, C2H4, contains a double bond"],
        ]),
    },
    "chemistry-c1-l20": {
        "data_table": table(["Rule", "Purpose"], [
            ["Always wear goggles", "Protects eyes from splashes and fumes"],
        ]),
    },
    "chemistry-c1-l21": {
        "data_table": table(["Quantum Number", "Describes"], [
            ["Principal (n)", "Energy level"], ["Azimuthal (l)", "Orbital shape"],
        ]),
    },
    "chemistry-c1-l22": {
        "data_table": table(["Trend", "Direction Across Period"], [
            ["Ionization energy", "Increases left to right"], ["Electronegativity", "Increases left to right"],
        ]),
    },
    "chemistry-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Formal charge", "The hypothetical charge assigned to an atom in a molecule"],
        ]),
    },
    "chemistry-c1-l24": {
        "data_table": table(["Type", "Example"], [
            ["Polar molecule", "Water, uneven charge distribution"], ["Nonpolar molecule", "Methane, even charge distribution"],
        ]),
    },
    "chemistry-c1-l25": {
        "data_table": table(["Compound Type", "Naming Rule"], [
            ["Ionic", "Cation name followed by anion name (e.g. sodium chloride)"], ["Molecular", "Uses prefixes like mono-, di-, tri-"],
        ]),
    },
    "chemistry-c1-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["Using mole ratios", "Converts moles of one substance to moles of another in a reaction"],
        ]),
        "formulae": ["moles_B = moles_A * (coeff_B / coeff_A)"],
    },
    "chemistry-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Limiting reactant", "The reactant that runs out first, limiting product formed"],
        ]),
        "formulae": ["percent_yield = (actual_yield / theoretical_yield) * 100"],
    },
    "chemistry-c1-l28": {
        "data_table": table(["Rule", "Example"], [
            ["Most nitrates are soluble", "NaNO3 dissolves readily in water"],
        ]),
    },
    "chemistry-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Precipitate", "An insoluble solid that forms when two solutions react"],
        ]),
    },
    "chemistry-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Titration", "A technique to determine concentration by neutralizing an acid or base"],
        ]),
        "formulae": ["M1 * V1 = M2 * V2"],
    },
    "chemistry-c1-l31": {
        "data_table": table(["Property", "Depends On"], [
            ["Colligative properties", "The number of solute particles, not their identity"],
        ]),
    },
    "chemistry-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Nuclear chemistry", "The study of reactions involving changes in atomic nuclei"],
        ]),
    },
    "chemistry-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Electrochemical cell", "A device that converts chemical energy into electrical energy or vice versa"],
        ]),
    },
    "chemistry-c1-l34": {
        "data_table": table(["Group", "Example"], [
            ["Hydroxyl (-OH)", "Found in alcohols"], ["Carboxyl (-COOH)", "Found in carboxylic acids"],
        ]),
    },
    "chemistry-c1-l35": {
        "data_table": table(["Type", "Bond Type"], [
            ["Alkane", "Single bonds only"], ["Alkene", "Contains a C=C double bond"], ["Alkyne", "Contains a C≡C triple bond"],
        ]),
    },
    "chemistry-c1-l36": {
        "data_table": table(["Feature", "Detail"], [
            ["Aromatic compound", "Contains a stable ring of delocalized pi electrons, like benzene"],
        ]),
    },
    "chemistry-c1-l37": {
        "data_table": table(["Group", "Structure"], [
            ["Alcohol", "R-OH"], ["Ether", "R-O-R'"],
        ]),
    },
    "chemistry-c1-l38": {
        "data_table": table(["Group", "Structure"], [
            ["Aldehyde", "R-CHO"], ["Ketone", "R-CO-R'"],
        ]),
    },
    "chemistry-c1-l39": {
        "data_table": table(["Group", "Structure"], [
            ["Carboxylic acid", "R-COOH"], ["Ester", "R-COO-R'"],
        ]),
    },
    "chemistry-c1-l40": {
        "data_table": table(["Group", "Structure"], [
            ["Amine", "R-NH2"], ["Amide", "R-CO-NH2"],
        ]),
    },
    "chemistry-c1-l41": {
        "data_table": table(["Type", "Detail"], [
            ["Structural isomer", "Same formula, different atom connectivity"], ["Stereoisomer", "Same connectivity, different spatial arrangement"],
        ]),
    },
    "chemistry-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Chirality", "A molecule's property of being non-superimposable on its mirror image"],
        ]),
    },
    "chemistry-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Polymer", "A large molecule made of repeating structural units called monomers"],
        ]),
    },
    "chemistry-c1-l44": {
        "data_table": table(["Method", "Use"], [
            ["Gravimetric analysis", "Determines composition by measuring mass"],
        ]),
    },
    "chemistry-c1-l45": {
        "data_table": table(["Technique", "Use"], [
            ["Spectroscopy", "Identifies compounds by analyzing their interaction with light"],
        ]),
    },
    "chemistry-c1-l46": {
        "data_table": table(["Technique", "Use"], [
            ["Chromatography", "Separates mixture components based on differing rates of movement"],
        ]),
    },
    "chemistry-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Buffer", "A solution that resists changes in pH when acid or base is added"],
        ]),
    },
    "chemistry-c1-l48": {
        "data_table": table(["Concept", "Meaning"], [
            ["Entropy", "A measure of disorder or randomness in a system"],
        ]),
    },
    "chemistry-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Reaction mechanism", "The step-by-step sequence of elementary reactions in an overall reaction"],
        ]),
    },
    "chemistry-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Catalyst", "A substance that speeds up a reaction without being consumed"],
        ]),
    },
    "chemistry-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental chemistry", "Studies chemical processes occurring in the natural environment"],
        ]),
    },
    "chemistry-c1-l52": {
        "data_table": table(["Principle", "Meaning"], [
            ["Atom economy", "Maximizing the proportion of reactant atoms incorporated into the final product"],
        ]),
    },
    "chemistry-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Materials chemistry", "Studies the synthesis and properties of new materials"],
        ]),
    },
    "chemistry-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Amino acid", "The building block of proteins, containing an amine and carboxyl group"],
        ]),
    },
    "chemistry-c1-l55": {
        "data_table": table(["Type", "Example"], [
            ["Monosaccharide", "Glucose, a single sugar unit"], ["Polysaccharide", "Starch, many linked sugar units"],
        ]),
    },
    "chemistry-c1-l56": {
        "data_table": table(["Type", "Example"], [
            ["Triglyceride", "Common fat, three fatty acids bonded to glycerol"],
        ]),
    },
    "chemistry-c1-l57": {
        "data_table": table(["Step", "Purpose"], [
            ["Identifying the endpoint", "Signals when the reaction has reached completion in a titration"],
        ]),
    },
    "chemistry-c1-l58": {
        "data_table": table(["Technique", "Purpose"], [
            ["Recrystallization", "Purifies a solid by dissolving and slowly reforming crystals"], ["Filtration", "Separates a solid from a liquid"],
        ]),
    },
    "chemistry-c1-l59": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Flammable symbol", "Warns the substance can easily catch fire"],
        ]),
    },
    "chemistry-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Analytical chemist", "Identifies and quantifies substances in a sample"],
        ]),
    },
    "chemistry-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Calculating freezing point depression", "Using a colligative property formula for a solution"],
        ]),
        "formulae": ["delta_T = i * K_f * m"],
    },
    "chemistry-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Writing a decay equation", "Balancing mass and atomic number in alpha decay"],
        ]),
    },
    "chemistry-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a functional group", "Recognizing a carboxyl group in a structure"],
        ]),
    },
    "chemistry-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Assessing pollution impact", "Tracing a pollutant's path through an ecosystem"],
        ]),
    },
    "chemistry-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Comparing material properties", "Contrasting conductivity of two engineered materials"],
        ]),
    },
    "chemistry-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Classifying a compound", "Determining if a substance is organic or inorganic"],
        ]),
    },
    "chemistry-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Naming an organic compound", "Applying IUPAC rules to a simple hydrocarbon"],
        ]),
    },
    "chemistry-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Determining atomic structure", "Finding the number of neutrons from mass number and atomic number"],
        ]),
        "formulae": ["neutrons = mass_number - atomic_number"],
    },
    "chemistry-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Predicting periodic trends", "Comparing atomic radius across a period"],
        ]),
    },
    "chemistry-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Writing an electron configuration", "Filling orbitals for a given element using the Aufbau principle"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Chemistry lessons (completing 70/70).")


if __name__ == "__main__":
    main()
