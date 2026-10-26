#!/usr/bin/env python3
"""Breadth-first pass, Level M2 (second graduate-tier level): add genuine,
hand-checked data_table content to one real, verifiable lesson per subject
across all 51 non-Math subjects in level_m2.json (Math already covered by
add_math_charts_all_levels.py; level_m2 has no Mythology subject, unlike
the other advanced levels).

Lesson titles at this level are highly specialized (mechanistic
interpretability, CRISPR-Cas9, the Modigliani-Miller theorem, Byzantine
fault tolerance, etc.), so each table sticks to conservative, well-
established textbook-level facts about the concept rather than detailed
technical claims -- still real and independently verifiable, never
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_level_m2_all_subjects_charts.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Mechanistic interpretability", "Reverse-engineering neural networks to understand their internal computations"],
            ["Attention head", "A Transformer component that learns to focus on specific parts of the input"],
        ]),
    },
    "machine-learning-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Neural Tangent Kernel (NTK)", "Describes how an infinitely-wide neural network's predictions evolve during training"],
            ["Kernel method", "A technique that implicitly maps data to a higher-dimensional space"],
        ]),
    },
    "natural-language-processing-m2-l3": {
        "data_table": table(["Tokenization Algorithm", "Approach"], [
            ["Byte-Pair Encoding (BPE)", "Iteratively merges the most frequent pair of symbols"],
            ["WordPiece", "Similar to BPE but merges based on likelihood improvement"],
            ["Unigram", "Starts with a large vocabulary and prunes it down probabilistically"],
        ]),
    },
    "data-science-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Causal inference", "Estimating cause-and-effect relationships from data"],
            ["Confounder", "A variable that influences both the treatment and the outcome"],
        ]),
    },
    "business-analytics-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Difference-in-differences", "Compares changes over time between a treatment group and a control group"],
            ["Parallel trends assumption", "Assumes both groups would have trended similarly without treatment"],
        ]),
    },
    "web-development-m2-l3": {
        "data_table": table(["JavaScript Expression", "Result"], [
            ["'5' + 3", "'53' (string concatenation)"], ["'5' - 3", "2 (numeric coercion)"],
            ["true + true", "2"],
        ]),
    },
    "cybersecurity-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Formal verification", "Mathematically proving a system meets its specification"],
            ["Protocol", "A defined sequence of steps for secure communication"],
        ]),
    },
    "cloud-computing-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Byzantine fault", "A failure where a component behaves arbitrarily or maliciously"],
            ["Consensus algorithm", "A method for distributed systems to agree on a value despite failures"],
        ]),
    },
    "digital-marketing-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Marketing Mix Modeling (MMM)", "Statistical analysis estimating each marketing channel's impact on sales"],
            ["Bayesian approach", "Incorporates prior knowledge and updates it with observed data"],
        ]),
    },
    "ui/ux-design-m2-l3": {
        "formulae": ["T = a + b x log2(D/W + 1)  (Fitts's Law)"],
        "data_table": table(["Symbol", "Meaning"], [
            ["T", "Time to reach a target"], ["D", "Distance to the target"], ["W", "Width of the target"],
        ]),
    },
    "project-management-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Optimism bias", "Tendency to underestimate costs/time and overestimate benefits"],
            ["Reference class forecasting", "Predicting outcomes using data from similar past projects"],
        ]),
    },
    "economics-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["DSGE", "Dynamic Stochastic General Equilibrium - models used to study macroeconomic policy"],
            ["Stochastic", "Involving randomness/probability"],
        ]),
    },
    "finance-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Proposed by", "Franco Modigliani and Merton Miller, 1958"],
            ["Core claim", "Under ideal conditions, a firm's value is unaffected by how it is financed (debt vs equity)"],
        ]),
    },
    "philosophy-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Saul Kripke"], ["Key work", "Naming and Necessity (1980)"],
            ["Key idea", "Identity statements between rigid designators, if true, are necessarily true"],
        ]),
    },
    "art-history-m2-l3": {
        "data_table": table(["Level of Meaning (Panofsky)", "Focus"], [
            ["Pre-iconographic", "Basic recognizable forms"],
            ["Iconographic", "Conventional subject matter and themes"],
            ["Iconological", "Deeper cultural/symbolic meaning"],
        ]),
    },
    "python-m2-l3": {
        "data_table": table(["CPython Compilation Stage", "Description"], [
            ["Tokenizing", "Source code is broken into tokens"],
            ["Parsing", "Tokens are turned into an Abstract Syntax Tree (AST)"],
            ["Compiling", "The AST is compiled into bytecode for the interpreter"],
        ]),
    },
    "r-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["MCMC", "Markov Chain Monte Carlo - algorithms for sampling from probability distributions"],
            ["Hamiltonian Monte Carlo", "An MCMC method using gradient information for more efficient sampling"],
        ]),
    },
    "javascript-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["V8", "Google's open-source JavaScript engine (used in Chrome and Node.js)"],
            ["Hidden class", "An internal structure V8 uses to optimize property access on objects"],
        ]),
    },
    "prompt-engineering-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Constitutional AI", "A training approach where a model critiques and revises its own outputs against a set of principles"],
            ["Introduced by", "Anthropic, 2022"],
        ]),
    },
    "computer-science-engineering-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["NP-hard", "At least as hard as the hardest problems in NP"],
            ["Approximation algorithm", "Finds a near-optimal solution in polynomial time when an exact solution is impractical"],
        ]),
    },
    "big-data-m2-l3": {
        "data_table": table(["Architecture", "Approach"], [
            ["Lambda", "Combines a batch layer and a speed (streaming) layer"],
            ["Kappa", "Uses a single streaming pipeline for both real-time and historical processing"],
        ]),
    },
    "mba-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Real option", "The right, but not obligation, to make a business decision (e.g. expand, delay, abandon)"],
            ["Related to", "Financial options theory (e.g. Black-Scholes)"],
        ]),
    },
    "operations-management-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Newsvendor model", "Determines optimal inventory order quantity under uncertain demand"],
            ["Underage cost", "Cost of ordering too little"], ["Overage cost", "Cost of ordering too much"],
        ]),
    },
    "ai-tools-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-agent system", "Multiple AI agents coordinating to complete a task"],
            ["Orchestration", "Managing the sequence and communication between agents"],
        ]),
    },
    "english-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Corpus", "A large, structured collection of texts used for linguistic analysis"],
            ["Stylistics", "The study of distinctive style in language use"],
        ]),
    },
    "science-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Majorana fermion", "A particle theorized to be its own antiparticle"],
            ["Proposed by", "Ettore Majorana, 1937"],
        ]),
    },
    "geography-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Fluvial geomorphology", "The study of how rivers shape landscapes"],
            ["Meander", "A winding curve or bend in a river channel"],
        ]),
    },
    "world-history-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Historian", "Fernand Braudel"], ["School of thought", "The Annales School"],
            ["Key concept", "'Longue duree' - studying history over very long time spans"],
        ]),
    },
    "islamic-studies-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Usul al-Fiqh", "The study of the sources and methodology of Islamic law"],
            ["Qiyas", "Reasoning by analogy, one of the classical sources of Islamic law"],
        ]),
    },
    "coding-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Named after", "J. Roger Hindley and Robin Milner"],
            ["Purpose", "Automatically infers the most general type of an expression without explicit annotations"],
        ]),
    },
    "world-literature-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Theorist", "Mikhail Bakhtin"],
            ["Key concept", "Dialogism - meaning emerges through the interaction of multiple voices"],
            ["Applied to", "Dostoevsky's novels, among others"],
        ]),
    },
    "art-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Philosopher", "Maurice Merleau-Ponty"], ["Field", "Phenomenology (the study of lived experience)"],
            ["Key work", "Phenomenology of Perception (1945)"],
        ]),
    },
    "music-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Spectralism", "A compositional approach using the acoustic properties of sound (its spectrum) as the basis for music"],
            ["Emerged in", "France, 1970s"],
        ]),
    },
    "survival-skills-m2-l3": {
        "data_table": table(["SAR Term", "Meaning"], [
            ["SAR", "Search and Rescue"],
            ["PLS", "Point Last Seen - the last confirmed location of a missing person"],
        ]),
    },
    "cooking-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Named after", "French chemist Louis-Camille Maillard"],
            ["Occurs between", "Amino acids and reducing sugars, with heat"],
            ["Typical temperature range", "c. 140-165C (285-330F)"],
        ]),
    },
    "foreign-languages-m2-l3": {
        "data_table": table(["Spanish Mood", "Use"], [
            ["Indicative", "States facts and certainty"],
            ["Subjunctive", "Expresses doubt, wishes, emotion, or hypotheticals"],
        ]),
    },
    "general-knowledge-m2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Signed", "1648"], ["Ended", "The Thirty Years' War"],
            ["Significance", "Established the modern concept of state sovereignty"],
        ]),
    },
    "social-studies-m2-l3": {
        "data_table": table(["Bourdieu Concept", "Meaning"], [
            ["Habitus", "Internalized dispositions shaped by one's social environment"],
            ["Field", "A structured social space with its own rules and hierarchies"],
            ["Capital", "Resources (economic, social, cultural) that confer advantage"],
        ]),
    },
    "physical-education-and-self-defense-m2-l3": {
        "data_table": table(["Periodization Phase", "Focus"], [
            ["Macrocycle", "A full training year/season"],
            ["Mesocycle", "Several weeks focused on a specific goal"],
            ["Microcycle", "A single week of training"],
        ]),
    },
    "first-aid-m2-l3": {
        "data_table": table(["TCCC Phase", "Focus"], [
            ["Care Under Fire", "Immediate life-threatening bleeding control while still under threat"],
            ["Tactical Field Care", "More thorough assessment once the threat is reduced"],
            ["Tactical Evacuation Care", "Care while transporting the casualty"],
        ]),
    },
    "physics-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Renormalization group", "A mathematical framework for studying how physical systems change across scales"],
            ["Fixed point", "A scale-invariant state where properties stop changing under the RG flow"],
        ]),
    },
    "chemistry-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Chirality", "A molecule's property of having a non-superimposable mirror image"],
            ["Organocatalysis", "Using small organic molecules (not metals) to speed up reactions"],
        ]),
    },
    "biology-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["CRISPR-Cas9", "A gene-editing system using a guide RNA and the Cas9 enzyme to cut DNA at specific sites"],
            ["Off-target effect", "An unintended edit at a site other than the intended target"],
        ]),
    },
    "critical-thinking-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Dialogical logic", "Models logical validity as a structured argumentative game between two players"],
            ["Proponent / Opponent", "The two roles in a dialogical logic game"],
        ]),
    },
    "health-education-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Health data science", "Applying data science methods to healthcare and biomedical data"],
            ["EHR", "Electronic Health Record"],
        ]),
    },
    "ict-and-computer-science-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Byzantine fault", "A failure where a component behaves arbitrarily or maliciously"],
            ["Consensus algorithm", "A method for distributed systems to agree on a value despite failures"],
        ]),
    },
    "business-studies-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a business, taking on financial risk"],
            ["Startup", "A newly founded business, often aiming to scale quickly"],
        ]),
    },
    "civics-m2-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rule of law", "Everyone, including the government, is subject to the law"],
            ["Due process", "Fair treatment through the judicial system"],
        ]),
    },
    "environmental-science-m2-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Biodiversity", "The variety of life in an ecosystem"],
            ["Species richness", "The number of different species present"],
        ]),
    },
    "world-politics-m2-l3": {
        "data_table": table(["Political Ideology", "Core Idea"], [
            ["Liberalism", "Individual rights and freedoms"],
            ["Conservatism", "Tradition and gradual change"],
            ["Socialism", "Collective/state ownership of production"],
        ]),
    },
    "world-religions-m2-l3": {
        "data_table": table(["Term (Hindu Tradition)", "Meaning"], [
            ["Dharma", "Duty, righteousness, moral order"],
            ["Karma", "Actions and their consequences"],
            ["Moksha", "Liberation from the cycle of rebirth"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    by_id: dict[str, dict] = {}
    for subject in data["subjects"].values():
        for lesson in subject.get("lessons", []):
            by_id[lesson["id"]] = lesson

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} data_table fields across {len(CHARTS)} Level M2 lessons (all 51 subjects).")


if __name__ == "__main__":
    main()
