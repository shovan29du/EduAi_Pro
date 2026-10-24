#!/usr/bin/env python3
"""Depth pass, C2 Chemistry: fill in real, hand-checked data_table
content for the 69 C2 Chemistry lessons not covered by the earlier
breadth-first batch. Brings C2 Chemistry to full 70/70 coverage.

l61-l63 are "Foundations 2" lessons revisiting l17, l21, and l51;
l64-l70 are "Worked Analysis" companions to l1-l7. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_chemistry_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "chemistry-c2-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Organic chemistry foundations", "Studies carbon-based compounds and their reactions"],
        ]),
    },
    "chemistry-c2-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Physical chemistry foundations", "Applies physics principles to explain chemical behavior"],
        ]),
    },
    "chemistry-c2-l4": {
        "data_table": table(["Hybridization", "Geometry"], [
            ["sp", "Linear, 180°"],
            ["sp2", "Trigonal planar, 120°"],
            ["sp3", "Tetrahedral, 109.5°"],
        ]),
    },
    "chemistry-c2-l5": {
        "data_table": table(["Force", "Relative Strength"], [
            ["Hydrogen bonding", "Strongest common intermolecular force, raises boiling point notably"],
            ["London dispersion", "Weakest, present in all molecules"],
        ]),
    },
    "chemistry-c2-l6": {
        "data_table": table(["Law", "Statement"], [
            ["Hess's law", "Total enthalpy change is independent of the reaction pathway"],
        ]),
        "formulae": ["delta_H_total = sum(delta_H_steps)"],
    },
    "chemistry-c2-l7": {
        "data_table": table(["Concept", "Formula"], [
            ["Heat capacity", "q = mcΔT"],
        ]),
        "formulae": ["q = m * c * delta_T"],
    },
    "chemistry-c2-l8": {
        "data_table": table(["Order", "Rate Law Form"], [
            ["Zero order", "rate = k"],
            ["First order", "rate = k[A]"],
            ["Second order", "rate = k[A]^2"],
        ]),
    },
    "chemistry-c2-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Rate-determining step", "The slowest elementary step controls the overall reaction rate"],
        ]),
    },
    "chemistry-c2-l10": {
        "data_table": table(["Concept", "Effect"], [
            ["Catalyst", "Lowers activation energy without being consumed in the reaction"],
        ]),
    },
    "chemistry-c2-l11": {
        "data_table": table(["Stress", "Equilibrium Shift"], [
            ["Increased pressure", "Shifts toward the side with fewer gas moles"],
            ["Increased temperature (exothermic)", "Shifts toward reactants"],
        ]),
    },
    "chemistry-c2-l12": {
        "data_table": table(["Constant", "Applies To"], [
            ["Kc", "Concentration-based equilibrium constant"],
            ["Kp", "Partial-pressure-based equilibrium constant"],
        ]),
    },
    "chemistry-c2-l13": {
        "data_table": table(["Quantity", "Formula"], [
            ["pH", "pH = -log10[H+]"],
        ]),
        "formulae": ["pH = -math.log10(H_concentration)"],
    },
    "chemistry-c2-l14": {
        "data_table": table(["Equation", "Use"], [
            ["Henderson-Hasselbalch", "pH = pKa + log([A-]/[HA])"],
        ]),
        "formulae": ["pH = pKa + math.log10(A_minus / HA)"],
    },
    "chemistry-c2-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Ksp", "Solubility product constant describing a sparingly soluble salt's equilibrium"],
        ]),
    },
    "chemistry-c2-l16": {
        "data_table": table(["Law", "Statement"], [
            ["Second law of thermodynamics", "Entropy of an isolated system tends to increase over time"],
        ]),
    },
    "chemistry-c2-l17": {
        "data_table": table(["Concept", "Formula"], [
            ["Gibbs free energy", "ΔG = ΔH - TΔS"],
        ]),
        "formulae": ["delta_G = delta_H - T * delta_S"],
    },
    "chemistry-c2-l18": {
        "data_table": table(["Component", "Role"], [
            ["Galvanic cell", "Converts spontaneous chemical reaction energy into electrical current"],
        ]),
    },
    "chemistry-c2-l19": {
        "data_table": table(["Functional Group", "Example"], [
            ["Hydroxyl (-OH)", "Alcohols"],
            ["Carbonyl (C=O)", "Ketones and aldehydes"],
        ]),
    },
    "chemistry-c2-l20": {
        "data_table": table(["Rule", "Purpose"], [
            ["IUPAC nomenclature", "Provides a systematic, unambiguous name for any organic compound"],
        ]),
    },
    "chemistry-c2-l21": {
        "data_table": table(["Diagram Element", "Meaning"], [
            ["MO diagram", "Shows relative energies of bonding and antibonding molecular orbitals"],
        ]),
    },
    "chemistry-c2-l22": {
        "data_table": table(["Field Type", "Splitting Pattern"], [
            ["Octahedral field", "Splits d-orbitals into two energy sets"],
        ]),
    },
    "chemistry-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Ligand", "A molecule or ion bonded to a central metal atom in a complex"],
        ]),
    },
    "chemistry-c2-l24": {
        "data_table": table(["Definition", "Detail"], [
            ["Lewis acid", "An electron pair acceptor"],
            ["Lewis base", "An electron pair donor"],
        ]),
    },
    "chemistry-c2-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Simultaneous equilibria", "Multiple equilibrium reactions interact and share common species"],
        ]),
    },
    "chemistry-c2-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Reaction mechanism", "The sequence of elementary steps that make up an overall reaction"],
        ]),
    },
    "chemistry-c2-l27": {
        "data_table": table(["Model", "Detail"], [
            ["Michaelis-Menten kinetics", "Describes the rate of enzyme-catalyzed reactions"],
        ]),
    },
    "chemistry-c2-l28": {
        "data_table": table(["Equation", "Use"], [
            ["Nernst equation", "Calculates cell potential under non-standard conditions"],
        ]),
        "formulae": ["E = E0 - (R*T/(n*F)) * math.log(Q)"],
    },
    "chemistry-c2-l29": {
        "data_table": table(["Equation", "Use"], [
            ["Boltzmann entropy formula", "S = k ln(W)"],
        ]),
        "formulae": ["S = k * math.log(W)"],
    },
    "chemistry-c2-l30": {
        "data_table": table(["Feature", "Detail"], [
            ["Triple point", "The unique temperature/pressure where solid, liquid, and gas coexist"],
        ]),
    },
    "chemistry-c2-l31": {
        "data_table": table(["Mechanism", "Feature"], [
            ["SN1", "Two-step mechanism via a carbocation intermediate, favored by tertiary substrates"],
            ["SN2", "One-step concerted mechanism, favored by primary substrates"],
        ]),
    },
    "chemistry-c2-l32": {
        "data_table": table(["Mechanism", "Feature"], [
            ["E1", "Stepwise elimination via a carbocation intermediate"],
            ["E2", "Concerted elimination requiring anti-periplanar geometry"],
        ]),
    },
    "chemistry-c2-l33": {
        "data_table": table(["Rule", "Detail"], [
            ["Markovnikov's rule", "H adds to the carbon already bearing more hydrogens in HX addition"],
        ]),
    },
    "chemistry-c2-l34": {
        "data_table": table(["Reaction Type", "Detail"], [
            ["Electrophilic aromatic substitution", "Preserves the aromatic ring while replacing a hydrogen"],
        ]),
    },
    "chemistry-c2-l35": {
        "data_table": table(["Descriptor", "Meaning"], [
            ["R configuration", "Priority groups decrease clockwise when viewed from opposite the lowest priority"],
            ["S configuration", "Priority groups decrease counterclockwise"],
        ]),
    },
    "chemistry-c2-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Retrosynthetic analysis", "Works backward from the target molecule to simpler starting materials"],
        ]),
    },
    "chemistry-c2-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Multistep synthesis", "Combines a sequence of reactions to build a complex target molecule"],
        ]),
    },
    "chemistry-c2-l38": {
        "data_table": table(["Signal", "Meaning"], [
            ["NMR chemical shift", "Indicates the chemical environment of a given hydrogen or carbon"],
        ]),
    },
    "chemistry-c2-l39": {
        "data_table": table(["Feature", "Meaning"], [
            ["Mass spectrum molecular ion peak", "Indicates the molecular weight of the compound"],
        ]),
    },
    "chemistry-c2-l40": {
        "data_table": table(["Peak Region", "Bond Type"], [
            ["~3200-3550 cm-1", "O-H or N-H stretch"],
            ["~1650-1750 cm-1", "C=O stretch"],
        ]),
    },
    "chemistry-c2-l41": {
        "data_table": table(["Mechanism", "Feature"], [
            ["Step-growth polymerization", "Monomers react stepwise, building the polymer gradually"],
            ["Chain-growth polymerization", "Monomers add rapidly to an active growing chain end"],
        ]),
    },
    "chemistry-c2-l42": {
        "data_table": table(["Material", "Property"], [
            ["Nanomaterial", "Exhibits distinct properties due to extremely small particle size"],
        ]),
    },
    "chemistry-c2-l43": {
        "data_table": table(["Structure", "Feature"], [
            ["Crystal lattice", "Regular repeating arrangement defining a solid's structure"],
        ]),
    },
    "chemistry-c2-l44": {
        "data_table": table(["Method", "Use"], [
            ["Instrumental analysis", "Uses specialized equipment for precise quantitative chemical measurement"],
        ]),
    },
    "chemistry-c2-l45": {
        "data_table": table(["Technique", "Use"], [
            ["HPLC", "Separates and quantifies compounds in a liquid sample"],
            ["GC", "Separates and quantifies volatile compounds in a gas phase"],
        ]),
    },
    "chemistry-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Uncertainty", "Quantifies the range within which a true measured value likely falls"],
        ]),
    },
    "chemistry-c2-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Enzyme mechanism", "Active site geometry and residues stabilize a reaction's transition state"],
        ]),
    },
    "chemistry-c2-l48": {
        "data_table": table(["Pathway", "Purpose"], [
            ["Glycolysis", "Breaks down glucose into pyruvate, yielding ATP"],
            ["Citric acid cycle", "Oxidizes acetyl-CoA to generate electron carriers for ATP production"],
        ]),
    },
    "chemistry-c2-l49": {
        "data_table": table(["Process", "Purpose"], [
            ["Beta-oxidation", "Breaks down fatty acids to generate acetyl-CoA for energy production"],
        ]),
    },
    "chemistry-c2-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Photochemical reaction", "Driven by absorption of light rather than thermal energy"],
        ]),
    },
    "chemistry-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Organometallic compound", "Contains a direct bond between carbon and a metal atom"],
        ]),
    },
    "chemistry-c2-l52": {
        "data_table": table(["Method", "Use"], [
            ["Density functional theory", "Models molecular electronic structure computationally"],
        ]),
    },
    "chemistry-c2-l53": {
        "data_table": table(["Reaction", "Detail"], [
            ["Ozone formation", "Photochemical reactions between NOx and VOCs generate ground-level ozone"],
        ]),
    },
    "chemistry-c2-l54": {
        "data_table": table(["Principle", "Detail"], [
            ["Green chemistry", "Designs processes to minimize hazardous waste and solvent use"],
        ]),
    },
    "chemistry-c2-l55": {
        "data_table": table(["Process", "Feature"], [
            ["Fission", "Splits a heavy nucleus, releasing energy"],
            ["Fusion", "Combines light nuclei, releasing even greater energy"],
        ]),
    },
    "chemistry-c2-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Reactor design", "Balances reaction rate, heat transfer, and mixing at industrial scale"],
        ]),
    },
    "chemistry-c2-l57": {
        "data_table": table(["Practice", "Purpose"], [
            ["Reproducibility", "Ensures experimental results can be independently verified"],
        ]),
    },
    "chemistry-c2-l58": {
        "data_table": table(["Practice", "Purpose"], [
            ["Instrument calibration", "Ensures measurement accuracy against known reference standards"],
        ]),
    },
    "chemistry-c2-l59": {
        "data_table": table(["Practice", "Purpose"], [
            ["Chemical risk assessment", "Identifies hazards before they cause harm in the laboratory"],
        ]),
    },
    "chemistry-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Independent research project", "Applies the full experimental method to an original chemistry question"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Orbital Type", "Effect"], [
    ["Bonding orbital", "Lower energy, stabilizes the molecule"],
    ["Antibonding orbital", "Higher energy, destabilizes the molecule"],
])

# l61-l63 "Foundations 2" lessons revisit l17, l21, and l51.
FOUNDATIONS_2_MAP = {61: 17, 62: 21, 63: 51}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"chemistry-c2-l{base_n}"
    fields = {"data_table": CHARTS[base_key]["data_table"]}
    if "formulae" in CHARTS[base_key]:
        fields["formulae"] = CHARTS[base_key]["formulae"]
    CHARTS[f"chemistry-c2-l{worked_n}"] = fields

# l64-l70 "Worked Analysis" lessons reuse the data_table of l1-l7.
WORKED_ANALYSIS_MAP = {64: 1, 65: 2, 66: 3, 67: 4, 68: 5, 69: 6, 70: 7}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"chemistry-c2-l{base_n}"
    if base_key in CHARTS:
        fields = {"data_table": CHARTS[base_key]["data_table"]}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = CHARTS[base_key]["formulae"]
        CHARTS[f"chemistry-c2-l{worked_n}"] = fields
    elif base_n == 3:
        CHARTS[f"chemistry-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Chemistry"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Chemistry: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Chemistry lessons (completing 70/70).")


if __name__ == "__main__":
    main()
