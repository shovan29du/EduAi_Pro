#!/usr/bin/env python3
"""Depth pass, C2 Critical Thinking: fill in real, hand-checked
data_table content for the 99 C2 Critical Thinking lessons not covered
by the earlier breadth-first batch. Brings C2 Critical Thinking to
full 100/100 coverage.

Unlike most C2 subjects (70 lessons), Critical Thinking has 100
lessons: l1-l60 core topics, l61-l65 "Foundations 2" lessons revisiting
l11, l31, l32, l35, and l51, l66-l80 "Comparative Case Study" lessons
(topics 6-20 of a 20-topic list), and l81-l100 "Applied Research
Seminar" lessons (all 20 topics). l3 was already completed by an
earlier breadth-first batch, so its data_table is hard-coded for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "critical-thinking-c2-l1": {
        "data_table": table(["Topic", "Feature"], [
            ["Cognitive bias & fallacies foundations", "Identifies systematic reasoning errors that distort judgment"],
        ]),
    },
    "critical-thinking-c2-l2": {
        "data_table": table(["Topic", "Feature"], [
            ["Evidence evaluation & research literacy", "Assesses the reliability and relevance of supporting evidence"],
        ]),
    },
    "critical-thinking-c2-l4": {
        "data_table": table(["Rule", "Detail"], [
            ["Distributed middle term", "A valid categorical syllogism must distribute its middle term at least once"],
        ]),
    },
    "critical-thinking-c2-l5": {
        "data_table": table(["Operator", "Meaning"], [
            ["Necessity (□)", "True in all possible worlds"],
            ["Possibility (◇)", "True in at least one possible world"],
        ]),
    },
    "critical-thinking-c2-l6": {
        "data_table": table(["Theory", "View"], [
            ["Foundationalism", "Justified beliefs rest on basic, non-inferential beliefs"],
            ["Coherentism", "Justification comes from a belief's fit within a coherent web of beliefs"],
        ]),
    },
    "critical-thinking-c2-l7": {
        "data_table": table(["Challenge", "Detail"], [
            ["Radical skepticism", "Questions whether certain knowledge is possible at all"],
        ]),
    },
    "critical-thinking-c2-l8": {
        "data_table": table(["Element", "Role"], [
            ["Backing", "Supports the warrant connecting evidence to claim"],
            ["Qualifier", "Indicates the claim's degree of certainty"],
            ["Rebuttal", "Acknowledges conditions under which the claim would not hold"],
        ]),
    },
    "critical-thinking-c2-l9": {
        "data_table": table(["Step", "Purpose"], [
            ["Constructing a counterargument", "Identifies the strongest objection to strengthen or revise a position"],
        ]),
    },
    "critical-thinking-c2-l10": {
        "data_table": table(["Question", "Detail"], [
            ["What counts as proof?", "Standards of evidence vary by context, from casual claims to legal proof"],
        ]),
    },
    "critical-thinking-c2-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Falsifiability", "A scientific claim must be capable of being proven false by observation"],
        ]),
    },
    "critical-thinking-c2-l12": {
        "data_table": table(["Concept", "Formula"], [
            ["Basic probability", "P(A) = favorable outcomes / total outcomes"],
        ]),
        "formulae": ["P_A = favorable_outcomes / total_outcomes"],
    },
    "critical-thinking-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["p-value", "Probability of observing results this extreme if the null hypothesis is true"],
        ]),
    },
    "critical-thinking-c2-l14": {
        "data_table": table(["Method", "Limitation"], [
            ["Convenience sampling", "Easy to collect but may not represent the broader population"],
        ]),
    },
    "critical-thinking-c2-l15": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic dialogue", "Uses guided questioning to expose contradictions and refine beliefs"],
        ]),
    },
    "critical-thinking-c2-l16": {
        "data_table": table(["Loop Type", "Effect"], [
            ["Positive feedback", "Amplifies change in a system"],
            ["Negative feedback", "Counteracts change to maintain stability"],
        ]),
    },
    "critical-thinking-c2-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Emergent property", "A system-level feature not present in its individual components"],
        ]),
    },
    "critical-thinking-c2-l18": {
        "data_table": table(["Framework", "Focus"], [
            ["SCAMPER", "Prompts creative modification of an existing idea or product"],
        ]),
    },
    "critical-thinking-c2-l19": {
        "data_table": table(["Stage", "Purpose"], [
            ["Empathize", "Understand the user's needs before proposing a solution"],
            ["Prototype", "Build a testable version of a proposed solution"],
        ]),
    },
    "critical-thinking-c2-l20": {
        "data_table": table(["Technique", "Purpose"], [
            ["Lateral thinking", "Approaches a problem indirectly to escape conventional assumptions"],
        ]),
    },
    "critical-thinking-c2-l21": {
        "data_table": table(["Fallacy", "Form"], [
            ["Affirming the consequent", "If P then Q; Q; therefore P (invalid)"],
            ["Denying the antecedent", "If P then Q; not P; therefore not Q (invalid)"],
        ]),
    },
    "critical-thinking-c2-l22": {
        "data_table": table(["Element", "Purpose"], [
            ["Argument map", "Visually diagrams how premises support or attack a conclusion"],
        ]),
    },
    "critical-thinking-c2-l23": {
        "data_table": table(["Concept", "Formula"], [
            ["Bayes' theorem", "P(A|B) = P(B|A)P(A) / P(B)"],
        ]),
        "formulae": ["P_A_given_B = (P_B_given_A * P_A) / P_B"],
    },
    "critical-thinking-c2-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Nash equilibrium", "No player can benefit by unilaterally changing their strategy"],
        ]),
    },
    "critical-thinking-c2-l25": {
        "data_table": table(["Problem", "Detail"], [
            ["Is-ought problem", "Descriptive facts alone cannot logically establish a prescriptive conclusion"],
        ]),
    },
    "critical-thinking-c2-l26": {
        "data_table": table(["Bias", "Detail"], [
            ["Sunk cost fallacy", "Continuing an endeavor because of resources already invested rather than future value"],
        ]),
    },
    "critical-thinking-c2-l27": {
        "data_table": table(["Bias", "Detail"], [
            ["Framing effect", "Identical information leads to different decisions depending on presentation"],
        ]),
    },
    "critical-thinking-c2-l28": {
        "data_table": table(["Technique", "Detail"], [
            ["Loaded language", "Uses emotionally charged wording to influence political opinion"],
        ]),
    },
    "critical-thinking-c2-l29": {
        "data_table": table(["Practice", "Purpose"], [
            ["Peer review", "Independent experts evaluate a study before publication"],
            ["Replication", "Independent researchers reproduce a study's results"],
        ]),
    },
    "critical-thinking-c2-l30": {
        "data_table": table(["Concept", "Formula"], [
            ["Expected utility", "EU = sum(P(outcome) * utility(outcome))"],
        ]),
        "formulae": ["EU = sum(p_i * u_i for p_i, u_i in outcomes)"],
    },
    "critical-thinking-c2-l31": {
        "data_table": table(["Paradox", "Statement"], [
            ["Liar paradox", "'This statement is false' cannot be consistently true or false"],
        ]),
    },
    "critical-thinking-c2-l32": {
        "data_table": table(["Paradox", "Statement"], [
            ["Sorites paradox", "Removing one grain from a heap never makes it a non-heap, yet eventually it is"],
        ]),
    },
    "critical-thinking-c2-l33": {
        "data_table": table(["Stage", "Role"], [
            ["Thesis", "An initial claim or position"],
            ["Antithesis", "A contradicting position"],
            ["Synthesis", "A resolution integrating both"],
        ]),
    },
    "critical-thinking-c2-l34": {
        "data_table": table(["Threat", "Detail"], [
            ["Deepfake", "AI-generated media that convincingly fabricates a person's speech or actions"],
        ]),
    },
    "critical-thinking-c2-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Legal reasoning", "Applies precedent and statutory interpretation to resolve a dispute"],
        ]),
    },
    "critical-thinking-c2-l36": {
        "data_table": table(["Technique", "Detail"], [
            ["Bandwagon propaganda", "Persuades by implying that everyone else already agrees"],
        ]),
    },
    "critical-thinking-c2-l37": {
        "data_table": table(["Method", "Purpose"], [
            ["Five whys", "Repeatedly asks 'why' to trace a problem to its underlying root cause"],
        ]),
    },
    "critical-thinking-c2-l38": {
        "data_table": table(["Framework", "Focus"], [
            ["Consequentialism", "Judges actions by their outcomes"],
            ["Deontology", "Judges actions by adherence to moral duties or rules"],
        ]),
    },
    "critical-thinking-c2-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Scientific controversy", "Requires distinguishing genuine expert disagreement from manufactured doubt"],
        ]),
    },
    "critical-thinking-c2-l40": {
        "data_table": table(["Fallacy", "Detail"], [
            ["Base rate neglect", "Ignoring the underlying prevalence rate when judging a probability"],
        ]),
    },
    "critical-thinking-c2-l41": {
        "data_table": table(["Fallacy", "Detail"], [
            ["Gambler's fallacy", "Believing a random independent event is 'due' after a streak"],
        ]),
    },
    "critical-thinking-c2-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Unintended consequences", "Interventions in complex systems often produce unforeseen side effects"],
        ]),
    },
    "critical-thinking-c2-l43": {
        "data_table": table(["Factor", "Detail"], [
            ["Expert credibility", "Track record and relevant domain expertise matter more than general authority"],
        ]),
    },
    "critical-thinking-c2-l44": {
        "data_table": table(["Practice", "Purpose"], [
            ["Steelmanning", "Represents an opposing view in its strongest possible form before critiquing it"],
        ]),
    },
    "critical-thinking-c2-l45": {
        "data_table": table(["Tradition", "Feature"], [
            ["Western logic", "Emphasizes formal deductive structure"],
            ["Non-Western dialectical traditions", "May emphasize contextual and relational reasoning"],
        ]),
    },
    "critical-thinking-c2-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Cognitive dissonance", "Discomfort from holding contradictory beliefs, often resolved by rationalizing one away"],
        ]),
    },
    "critical-thinking-c2-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Risk communication", "Perceived risk often diverges sharply from statistical risk"],
        ]),
    },
    "critical-thinking-c2-l48": {
        "data_table": table(["Skill", "Purpose"], [
            ["Interest-based negotiation", "Focuses on underlying needs rather than fixed positions"],
        ]),
    },
    "critical-thinking-c2-l49": {
        "data_table": table(["Skill", "Purpose"], [
            ["Parsing legal structure", "Identifies conditions, exceptions, and obligations within policy text"],
        ]),
    },
    "critical-thinking-c2-l50": {
        "data_table": table(["Theory", "Focus"], [
            ["Reliabilism", "Justification depends on whether a belief was produced by a reliable process"],
            ["Virtue epistemology", "Justification depends on intellectual virtues of the believer"],
        ]),
    },
    "critical-thinking-c2-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Ethics of persuasion", "Distinguishes legitimate persuasion from manipulative exploitation of bias"],
        ]),
    },
    "critical-thinking-c2-l52": {
        "data_table": table(["Concern", "Detail"], [
            ["Algorithmic bias", "Automated systems can inherit and amplify bias present in training data"],
        ]),
    },
    "critical-thinking-c2-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Confounding variable", "An unaccounted factor that affects both cause and effect being studied"],
        ]),
    },
    "critical-thinking-c2-l54": {
        "data_table": table(["Method", "Purpose"], [
            ["Meta-analysis", "Statistically combines results across multiple studies for a stronger estimate"],
        ]),
    },
    "critical-thinking-c2-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Historical interpretation", "Requires weighing source reliability and the historian's own perspective"],
        ]),
    },
    "critical-thinking-c2-l56": {
        "data_table": table(["Fallacy", "Detail"], [
            ["Equivocation", "Shifts the meaning of a key term partway through an argument"],
            ["Amphiboly", "Exploits grammatical ambiguity to mislead"],
        ]),
    },
    "critical-thinking-c2-l57": {
        "data_table": table(["Skill", "Purpose"], [
            ["Defending a thesis", "Anticipates and responds to the strongest objections in advance"],
        ]),
    },
    "critical-thinking-c2-l58": {
        "data_table": table(["Feature", "Detail"], [
            ["Conspiracy theory", "Often unfalsifiable and treats contrary evidence as further proof of a cover-up"],
        ]),
    },
    "critical-thinking-c2-l59": {
        "data_table": table(["Concept", "Contrast"], [
            ["Wisdom of crowds", "Independent estimates can average to a highly accurate result"],
            ["Groupthink", "Social pressure toward consensus can suppress independent judgment"],
        ]),
    },
    "critical-thinking-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Extended argument capstone", "Constructs and defends a rigorous, well-supported position"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Syllogism Part", "Example"], [
    ["Major premise", "All mammals are warm-blooded"],
    ["Minor premise", "A dog is a mammal"],
    ["Conclusion", "Therefore, a dog is warm-blooded"],
])

# l61-l65 "Foundations 2" lessons revisit l11, l31, l32, l35, and l51.
FOUNDATIONS_2_MAP = {61: 11, 62: 31, 63: 32, 64: 35, 65: 51}
for worked_n, base_n in FOUNDATIONS_2_MAP.items():
    base_key = f"critical-thinking-c2-l{base_n}"
    CHARTS[f"critical-thinking-c2-l{worked_n}"] = {
        "data_table": CHARTS[base_key]["data_table"],
    }

# 20-topic list underlying the "Comparative Case Study" (l66-l80, topics
# 6-20) and "Applied Research Seminar" (l81-l100, topics 1-20) blocks.
TOPIC_TABLES: list[dict] = [
    table(["Topic", "Application"], [["Claims and evidence", "Distinguishes a bare assertion from a well-supported claim"]]),
    table(["Topic", "Application"], [["Deductive reasoning", "Draws a conclusion that necessarily follows from true premises"]]),
    table(["Topic", "Application"], [["Inductive reasoning", "Draws a probable conclusion from a pattern of specific observations"]]),
    table(["Topic", "Application"], [["Validity and soundness", "A sound argument must be both valid and have true premises"]]),
    table(["Topic", "Application"], [["Informal fallacies", "Errors in reasoning that arise from content or context rather than form"]]),
    table(["Topic", "Application"], [["Cognitive bias", "Systematic deviation from rational judgment shaped by mental shortcuts"]]),
    table(["Topic", "Application"], [["Causal reasoning", "Establishing that one factor genuinely produces an effect, not just correlates with it"]]),
    table(["Topic", "Application"], [["Statistical claims", "Evaluating whether numerical evidence actually supports the stated conclusion"]]),
    table(["Topic", "Application"], [["Scientific reasoning", "Testing hypotheses through falsifiable, replicable methods"]]),
    table(["Topic", "Application"], [["Source evaluation", "Assessing a source's credibility, bias, and relevance"]]),
    table(["Topic", "Application"], [["Media literacy", "Critically assessing how media framing shapes a message"]]),
    table(["Topic", "Application"], [["Argument mapping", "Visualizing the logical structure connecting claims and evidence"]]),
    table(["Topic", "Application"], [["Decision theory", "Choosing among options by weighing probability and value of outcomes"]]),
    table(["Topic", "Application"], [["Ethical reasoning", "Applying moral frameworks to evaluate the rightness of an action"]]),
    table(["Topic", "Application"], [["Legal reasoning", "Applying precedent and statute to resolve a specific case"]]),
    table(["Topic", "Application"], [["Systems thinking", "Analyzing how interacting parts produce outcomes beyond any one part"]]),
    table(["Topic", "Application"], [["Counterexamples", "A single case that disproves a general claim"]]),
    table(["Topic", "Application"], [["Uncertainty and risk", "Making sound decisions despite incomplete information"]]),
    table(["Topic", "Application"], [["Constructive debate", "Exchanging arguments to clarify and test positions rather than merely win"]]),
    table(["Topic", "Application"], [["Metacognition", "Reflecting on and regulating one's own thinking process"]]),
]

# l66-l80 "Comparative Case Study" lessons cover topics 6-20 (index 5-19).
for i, lesson_n in enumerate(range(66, 81)):
    CHARTS[f"critical-thinking-c2-l{lesson_n}"] = {
        "data_table": TOPIC_TABLES[5 + i],
    }

# l81-l100 "Applied Research Seminar" lessons cover all 20 topics.
for i, lesson_n in enumerate(range(81, 101)):
    CHARTS[f"critical-thinking-c2-l{lesson_n}"] = {
        "data_table": TOPIC_TABLES[i],
    }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Critical Thinking lessons (completing 100/100).")


if __name__ == "__main__":
    main()
