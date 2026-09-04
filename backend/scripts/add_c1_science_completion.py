#!/usr/bin/env python3
"""Depth pass, C1 Science: fill in real, hand-checked data_table content
for the 69 C1 Science lessons not covered by the earlier breadth-first
batch. Brings C1 Science to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "science-c1-l1": {
        "data_table": table(["Step", "Purpose"], [
            ["Hypothesis", "A testable prediction"], ["Measurement", "Quantifying observations with units"],
        ]),
    },
    "science-c1-l2": {
        "data_table": table(["Field", "Focus"], [
            ["Earth science", "Geology, weather, oceans"], ["Space science", "Astronomy and the solar system"],
        ]),
    },
    "science-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Independent variable", "What the experimenter changes"], ["Control", "Kept constant for comparison"],
        ]),
    },
    "science-c1-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Paradigm shift", "A fundamental change in scientific thinking, e.g. heliocentrism"],
        ]),
    },
    "science-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Interdisciplinary science", "Combines methods and knowledge from multiple scientific fields"],
        ]),
    },
    "science-c1-l7": {
        "data_table": table(["Skill", "Purpose"], [
            ["Science communication", "Translating technical findings for a general audience"],
        ]),
    },
    "science-c1-l8": {
        "data_table": table(["Quality", "Reason"], [
            ["Testable", "A good research question can be investigated with evidence"],
        ]),
    },
    "science-c1-l9": {
        "data_table": table(["Chart Type", "Best For"], [
            ["Bar chart", "Comparing categories"], ["Line graph", "Trends over time"],
        ]),
    },
    "science-c1-l10": {
        "data_table": table(["Rule", "Reason"], [
            ["Wear safety goggles", "Protects eyes from chemical splashes"],
        ]),
    },
    "science-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Reproducibility", "Getting the same result when an experiment is repeated"],
        ]),
    },
    "science-c1-l12": {
        "data_table": table(["Principle", "Meaning"], [
            ["Data integrity", "Reporting results accurately, without fabrication or omission"],
        ]),
    },
    "science-c1-l13": {
        "data_table": table(["Example", "Detail"], [
            ["Vaccine policy", "Informed by clinical trial evidence"],
        ]),
    },
    "science-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Citizen science", "Public participation in scientific data collection"],
        ]),
    },
    "science-c1-l15": {
        "data_table": table(["Question to Ask", "Purpose"], [
            ["Is this peer-reviewed?", "Assesses the credibility of a science claim"],
        ]),
    },
    "science-c1-l16": {
        "data_table": table(["Technology", "Field"], [
            ["CRISPR", "Genetic engineering"], ["Quantum computing", "Computer science"],
        ]),
    },
    "science-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental science", "The study of interactions between organisms and their environment"],
        ]),
    },
    "science-c1-l18": {
        "data_table": table(["Component", "Role"], [
            ["Atmosphere", "Regulates temperature and weather"], ["Ocean", "Absorbs heat and carbon dioxide"],
        ]),
    },
    "science-c1-l19": {
        "data_table": table(["Transmission Route", "Example"], [
            ["Airborne", "Influenza"], ["Waterborne", "Cholera"],
        ]),
    },
    "science-c1-l20": {
        "data_table": table(["Nutrient", "Role"], [
            ["Protein", "Builds and repairs tissue"], ["Carbohydrates", "Main energy source"],
        ]),
    },
    "science-c1-l21": {
        "data_table": table(["Quantity", "Formula"], [
            ["Force", "F = ma"],
        ]),
        "formulae": ["F = ma"],
    },
    "science-c1-l22": {
        "data_table": table(["Law", "Statement"], [
            ["Newton's First Law", "An object stays at rest or in motion unless acted on by a net force"],
        ]),
    },
    "science-c1-l23": {
        "data_table": table(["Law", "Statement"], [
            ["Conservation of energy", "Energy cannot be created or destroyed, only transformed"],
        ]),
    },
    "science-c1-l24": {
        "data_table": table(["Property", "Meaning"], [
            ["Wavelength", "Distance between successive crests"], ["Amplitude", "Height of a wave"],
        ]),
    },
    "science-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Refraction", "Bending of light between media of different densities"],
        ]),
    },
    "science-c1-l26": {
        "data_table": table(["Law", "Formula"], [
            ["Ohm's Law", "V = IR"],
        ]),
        "formulae": ["V = IR"],
    },
    "science-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Magnetic field", "The region around a magnet where magnetic force acts"],
        ]),
    },
    "science-c1-l28": {
        "data_table": table(["State", "Particle Arrangement"], [
            ["Solid", "Tightly packed, fixed positions"], ["Gas", "Widely spaced, moving freely"],
        ]),
    },
    "science-c1-l29": {
        "data_table": table(["Particle", "Charge"], [
            ["Proton", "Positive"], ["Neutron", "Neutral"], ["Electron", "Negative"],
        ]),
    },
    "science-c1-l30": {
        "data_table": table(["Trend", "Direction"], [
            ["Atomic radius", "Decreases across a period, increases down a group"],
        ]),
    },
    "science-c1-l31": {
        "data_table": table(["Bond Type", "Description"], [
            ["Ionic", "Transfer of electrons between atoms"], ["Covalent", "Sharing of electrons between atoms"],
        ]),
    },
    "science-c1-l32": {
        "data_table": table(["Rule", "Reason"], [
            ["Conservation of mass", "Atoms are neither created nor destroyed in a reaction"],
        ]),
    },
    "science-c1-l33": {
        "data_table": table(["pH Range", "Nature"], [
            ["0-6", "Acidic"], ["7", "Neutral"], ["8-14", "Basic"],
        ]),
    },
    "science-c1-l34": {
        "data_table": table(["Organelle", "Function"], [
            ["Nucleus", "Contains genetic material"], ["Mitochondria", "Produces energy (ATP)"],
        ]),
    },
    "science-c1-l35": {
        "data_table": table(["Feature", "Plant Cell", "Animal Cell"], [
            ["Cell wall", "Present", "Absent"],
        ]),
    },
    "science-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["DNA", "Deoxyribonucleic acid, carries genetic instructions"], ["Gene", "A unit of heredity"],
        ]),
    },
    "science-c1-l37": {
        "data_table": table(["Concept", "Proposed By"], [
            ["Natural selection", "Charles Darwin, 1859"],
        ]),
    },
    "science-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Ecosystem", "A community of organisms interacting with their environment"], ["Biome", "A large region defined by its climate and dominant vegetation"],
        ]),
    },
    "science-c1-l39": {
        "data_table": table(["System", "Function"], [
            ["Circulatory system", "Transports blood"], ["Respiratory system", "Exchanges gases"],
        ]),
    },
    "science-c1-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Plate tectonics", "The Earth's crust is divided into moving plates"],
        ]),
    },
    "science-c1-l41": {
        "data_table": table(["Rock Type", "Formation"], [
            ["Igneous", "Cooled magma or lava"], ["Sedimentary", "Compacted sediment layers"], ["Metamorphic", "Transformed by heat and pressure"],
        ]),
    },
    "science-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Atmosphere", "The layer of gases surrounding Earth"],
        ]),
    },
    "science-c1-l43": {
        "data_table": table(["Planet", "Order from Sun"], [
            ["Mercury", "1st"], ["Earth", "3rd"],
        ]),
    },
    "science-c1-l44": {
        "data_table": table(["Stage", "Description"], [
            ["Main sequence", "A star fusing hydrogen into helium, like the Sun"],
        ]),
    },
    "science-c1-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Big Bang", "The universe's expansion began about 13.8 billion years ago"],
        ]),
    },
    "science-c1-l46": {
        "data_table": table(["Quantity", "SI Unit"], [
            ["Mass", "Kilogram (kg)"], ["Length", "Meter (m)"], ["Time", "Second (s)"],
        ]),
    },
    "science-c1-l47": {
        "data_table": table(["Concept", "Meaning"], [
            ["Significant figures", "Digits that carry meaningful precision in a measurement"],
        ]),
    },
    "science-c1-l48": {
        "data_table": table(["Number", "Scientific Notation"], [
            ["6,000,000", "6 x 10^6"], ["0.00045", "4.5 x 10^-4"],
        ]),
    },
    "science-c1-l49": {
        "data_table": table(["Chart Type", "Best For"], [
            ["Scatter plot", "Showing correlation between two variables"],
        ]),
    },
    "science-c1-l50": {
        "data_table": table(["Equipment", "Use"], [
            ["Beaker", "Measuring and mixing liquids"], ["Microscope", "Magnifying small specimens"],
        ]),
    },
    "science-c1-l51": {
        "data_table": table(["Unit", "Measures"], [
            ["Meter", "Length"], ["Liter", "Volume"], ["Gram", "Mass"],
        ]),
    },
    "science-c1-l52": {
        "data_table": table(["Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Non-renewable", "Coal, oil"],
        ]),
    },
    "science-c1-l53": {
        "data_table": table(["Stage", "Process"], [
            ["Evaporation", "Water turns to vapor"], ["Precipitation", "Water falls as rain or snow"],
        ]),
    },
    "science-c1-l54": {
        "data_table": table(["Type", "Example"], [
            ["Bacteria", "Single-celled prokaryote"], ["Virus", "Requires a host cell to reproduce"],
        ]),
    },
    "science-c1-l55": {
        "data_table": table(["Component", "Function"], [
            ["White blood cells", "Fight infection"], ["Antibodies", "Target specific pathogens"],
        ]),
    },
    "science-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Dominant allele", "Expressed even with one copy"], ["Recessive allele", "Expressed only with two copies"],
        ]),
    },
    "science-c1-l57": {
        "data_table": table(["Process", "Reactants", "Products"], [
            ["Photosynthesis", "CO2 + H2O + light", "Glucose + O2"],
        ]),
        "formulae": ["6CO2 + 6H2O + light -> C6H12O6 + 6O2"],
    },
    "science-c1-l58": {
        "data_table": table(["Boundary Type", "Movement"], [
            ["Convergent", "Plates move toward each other"], ["Divergent", "Plates move apart"],
        ]),
    },
    "science-c1-l59": {
        "data_table": table(["Type", "Description"], [
            ["Shield volcano", "Broad, gently sloping, formed by fluid lava"],
        ]),
    },
    "science-c1-l60": {
        "data_table": table(["Principle", "Meaning"], [
            ["Informed consent", "Research subjects must knowingly agree to participate"],
        ]),
    },
    "science-c1-l61": {
        "data_table": table(["Organelle", "Function"], [
            ["Ribosome", "Makes proteins"], ["Chloroplast", "Site of photosynthesis"],
        ]),
    },
    "science-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Designing an experiment", "Testing how fertilizer amount affects plant growth"],
        ]),
    },
    "science-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a rock sample", "Identifying whether it is igneous, sedimentary, or metamorphic"],
        ]),
    },
    "science-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Applying the scientific method", "Testing whether a plant grows faster with more sunlight"],
        ]),
    },
    "science-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Identifying variables", "Labeling the independent, dependent, and control variables in a study"],
        ]),
    },
    "science-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a paradigm shift", "Comparing geocentric and heliocentric models of the solar system"],
        ]),
    },
    "science-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Cross-disciplinary case study", "Analyzing climate change using physics, chemistry, and biology"],
        ]),
    },
    "science-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Writing a lay summary", "Explaining a research finding for a non-expert audience"],
        ]),
    },
    "science-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Refining a research question", "Turning a broad topic into a specific, testable question"],
        ]),
    },
    "science-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting a graph", "Reading a line graph of global temperature change over time"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Science lessons (completing 70/70).")


if __name__ == "__main__":
    main()
