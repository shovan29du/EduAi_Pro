#!/usr/bin/env python3
"""Depth pass, C2 Philosophy: fill in real, hand-checked data_table
content for the 69 C2 Philosophy lessons not covered by the earlier
breadth-first batch. Brings C2 Philosophy to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "philosophy-c2-l1": {
        "data_table": table(["Philosopher", "Contribution"], [
            ["Socrates", "The Socratic method of questioning"], ["Plato", "Theory of Forms"], ["Aristotle", "Systematic logic and virtue ethics"],
        ]),
    },
    "philosophy-c2-l2": {
        "data_table": table(["Philosopher", "Contribution"], [
            ["Augustine", "Synthesized Christian theology with Platonic thought"], ["Aquinas", "Synthesized Christian theology with Aristotelian logic"],
        ]),
    },
    "philosophy-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Valid argument", "The conclusion follows necessarily from the premises"], ["Sound argument", "Valid and all premises are true"],
        ]),
    },
    "philosophy-c2-l5": {
        "data_table": table(["Philosopher", "Idea"], [
            ["Thales", "Proposed water as the fundamental substance"], ["Democritus", "Proposed reality is composed of indivisible atoms"],
        ]),
    },
    "philosophy-c2-l6": {
        "data_table": table(["Class", "Role in the Republic"], [
            ["Guardians", "Rule through wisdom"], ["Auxiliaries", "Defend the city through courage"],
        ]),
    },
    "philosophy-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Forms", "Plato's perfect, unchanging archetypes that physical objects imperfectly reflect"],
        ]),
    },
    "philosophy-c2-l8": {
        "data_table": table(["Concept", "Meaning"], [
            ["Substance", "That which exists independently, the subject of change"],
        ]),
    },
    "philosophy-c2-l9": {
        "data_table": table(["Term", "Example"], [
            ["Syllogism", "All men are mortal; Socrates is a man; therefore Socrates is mortal"],
        ]),
    },
    "philosophy-c2-l10": {
        "data_table": table(["School", "Core Idea"], [
            ["Stoicism", "Virtue and acceptance of what's beyond one's control lead to tranquility"], ["Epicureanism", "Pleasure, understood as absence of pain, is the highest good"],
        ]),
    },
    "philosophy-c2-l11": {
        "data_table": table(["Concept", "Augustine's View"], [
            ["Time", "Exists only in the mind's perception of past, present, and future"],
        ]),
    },
    "philosophy-c2-l12": {
        "data_table": table(["Way", "Argument"], [
            ["First Way", "Argument from motion, requiring an unmoved mover"], ["Fifth Way", "Argument from design and purpose in nature"],
        ]),
    },
    "philosophy-c2-l13": {
        "data_table": table(["Concept", "Boethius's View"], [
            ["Divine foreknowledge", "God's timeless knowledge doesn't determine human free choices"],
        ]),
    },
    "philosophy-c2-l14": {
        "data_table": table(["Philosopher", "Contribution"], [
            ["Avicenna", "Synthesized Aristotelian metaphysics with Islamic theology"], ["Averroes", "Wrote influential commentaries on Aristotle"],
        ]),
    },
    "philosophy-c2-l15": {
        "data_table": table(["Concept", "Problem"], [
            ["Gettier problem", "Shows justified true belief can fail to count as knowledge under certain conditions"],
        ]),
    },
    "philosophy-c2-l16": {
        "data_table": table(["Philosopher", "Position"], [
            ["Descartes", "Knowledge derives primarily from reason"], ["Locke", "Knowledge derives primarily from sensory experience"],
        ]),
    },
    "philosophy-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Problem of induction", "Questions whether past observations justify predictions about the future"],
        ]),
    },
    "philosophy-c2-l18": {
        "data_table": table(["Type", "Focus"], [
            ["Cartesian skepticism", "Doubts based on the possibility of systematic deception"], ["Humean skepticism", "Doubts about the justification of inductive reasoning"],
        ]),
    },
    "philosophy-c2-l19": {
        "data_table": table(["Theory", "Structure"], [
            ["Foundationalism", "Beliefs rest on basic, self-justifying foundational beliefs"], ["Coherentism", "Beliefs are justified by their mutual coherence, with no foundation"],
        ]),
    },
    "philosophy-c2-l20": {
        "data_table": table(["Concept", "Meaning"], [
            ["Social epistemology", "Studies how knowledge is shaped by social processes like testimony"],
        ]),
    },
    "philosophy-c2-l21": {
        "data_table": table(["Theory", "Focus"], [
            ["Reliabilism", "A belief is justified if produced by a reliable cognitive process"], ["Virtue epistemology", "Justification depends on intellectual virtues of the believer"],
        ]),
    },
    "philosophy-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Modal realism", "The view that all possible worlds exist as concretely as the actual world"],
        ]),
    },
    "philosophy-c2-l23": {
        "data_table": table(["Theory", "Meaning"], [
            ["Psychological continuity theory", "Personal identity persists through continuity of memory and psychological states"],
        ]),
    },
    "philosophy-c2-l24": {
        "data_table": table(["Theory", "Meaning"], [
            ["Functionalism", "Mental states are defined by their functional role, not their physical substrate"],
        ]),
    },
    "philosophy-c2-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Hard problem of consciousness", "The difficulty explaining why physical processes give rise to subjective experience"],
        ]),
    },
    "philosophy-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Speech act", "An utterance that performs an action, like promising or declaring"],
        ]),
    },
    "philosophy-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Paradigm shift", "A fundamental change in the basic assumptions of a scientific field"],
        ]),
    },
    "philosophy-c2-l28": {
        "data_table": table(["Principle", "Meaning"], [
            ["Falsificationism", "A theory is scientific only if it can, in principle, be proven false"],
        ]),
    },
    "philosophy-c2-l29": {
        "data_table": table(["Theory", "Meaning"], [
            ["Institutional theory of art", "An object is art because the art world confers that status on it"],
        ]),
    },
    "philosophy-c2-l30": {
        "data_table": table(["Concept", "Meaning"], [
            ["Leap of faith", "Kierkegaard's idea that religious commitment requires a choice beyond rational proof"],
        ]),
    },
    "philosophy-c2-l31": {
        "data_table": table(["Concept", "Meaning"], [
            ["Being-toward-death", "Heidegger's view that authentic existence requires confronting one's mortality"],
        ]),
    },
    "philosophy-c2-l32": {
        "data_table": table(["Concept", "Meaning"], [
            ["The Absurd", "Camus's term for the tension between humans' search for meaning and an indifferent universe"],
        ]),
    },
    "philosophy-c2-l33": {
        "data_table": table(["Type", "Focus"], [
            ["Act utilitarianism", "Evaluates each individual action's consequences"], ["Rule utilitarianism", "Evaluates rules that generally maximize good outcomes"],
        ]),
    },
    "philosophy-c2-l34": {
        "data_table": table(["Formulation", "Statement"], [
            ["Universal law", "Act only according to a maxim you could will to be a universal law"], ["Humanity", "Treat humanity always as an end, never merely as a means"],
        ]),
    },
    "philosophy-c2-l35": {
        "data_table": table(["Approach", "Focus"], [
            ["Aristotelian virtue ethics", "Grounds virtue in human flourishing (eudaimonia)"], ["Neo-Aristotelian ethics", "Reapplies virtue concepts to modern moral questions"],
        ]),
    },
    "philosophy-c2-l36": {
        "data_table": table(["Concept", "Meaning"], [
            ["Contractualism", "An act is wrong if it violates principles no one could reasonably reject"],
        ]),
    },
    "philosophy-c2-l37": {
        "data_table": table(["Concept", "Meaning"], [
            ["Veil of ignorance", "A thought experiment for choosing fair principles without knowing one's own position in society"],
        ]),
    },
    "philosophy-c2-l38": {
        "data_table": table(["Critique", "Meaning"], [
            ["Nozick's entitlement theory", "Justice depends on how holdings were acquired, not their final distribution"],
        ]),
    },
    "philosophy-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Contractarianism", "Moral and political obligations arise from a hypothetical agreement among rational agents"],
        ]),
    },
    "philosophy-c2-l40": {
        "data_table": table(["Response", "Meaning"], [
            ["Reliabilist response", "Adds a reliability condition to address Gettier-style counterexamples"],
        ]),
    },
    "philosophy-c2-l41": {
        "data_table": table(["Concept", "Meaning"], [
            ["Genealogy of morals", "Nietzsche's project tracing the historical origins of moral concepts like good and evil"],
        ]),
    },
    "philosophy-c2-l42": {
        "data_table": table(["Concept", "Meaning"], [
            ["Being-for-itself", "Sartre's term for conscious, free human existence, as opposed to fixed objects"],
        ]),
    },
    "philosophy-c2-l43": {
        "data_table": table(["Concept", "Meaning"], [
            ["'One is not born, but rather becomes, a woman'", "Beauvoir's argument that gender is socially constructed"],
        ]),
    },
    "philosophy-c2-l44": {
        "data_table": table(["Concept", "Meaning"], [
            ["Ren", "Confucian virtue of benevolence, central to good governance"],
        ]),
    },
    "philosophy-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Wu wei", "Daoist principle of effortless action in harmony with the natural Way"],
        ]),
    },
    "philosophy-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Anatta", "The Buddhist doctrine that there is no permanent, unchanging self"],
        ]),
    },
    "philosophy-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Ubuntu", "'I am because we are' — an African philosophy emphasizing communal interdependence"],
        ]),
    },
    "philosophy-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Philosophy of liberation", "A Latin American tradition centering the perspective of the oppressed"],
        ]),
    },
    "philosophy-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Doctrine of double effect", "An action causing harm may be permissible if the harm isn't the intended means to a good end"],
        ]),
    },
    "philosophy-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Compatibilism", "The view that free will and determinism can coexist"],
        ]),
    },
    "philosophy-c2-l51": {
        "data_table": table(["Thought Experiment", "Question Raised"], [
            ["Teletransportation puzzle", "Whether a reconstructed copy of a person is truly the same individual"],
        ]),
    },
    "philosophy-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Just war theory", "A framework for evaluating the moral justification of entering and conducting war"],
        ]),
    },
    "philosophy-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Deep ecology", "Views nature as having intrinsic value independent of human usefulness"],
        ]),
    },
    "philosophy-c2-l54": {
        "data_table": table(["Question", "Focus"], [
            ["Genetic enhancement ethics", "Weighs autonomy and fairness against risks of inequality and coercion"],
        ]),
    },
    "philosophy-c2-l55": {
        "data_table": table(["Theory", "Focus"], [
            ["Legal positivism", "Law's validity depends on social facts, not morality"], ["Natural law", "Law's validity depends partly on its moral content"],
        ]),
    },
    "philosophy-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Intersectionality", "Overlapping social identities create distinct, compounding experiences of oppression"],
        ]),
    },
    "philosophy-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Divine hiddenness", "The philosophical puzzle of why a loving God would remain hidden from nonbelievers"],
        ]),
    },
    "philosophy-c2-l58": {
        "data_table": table(["Symbol", "Meaning"], [
            ["∀", "For all"], ["∃", "There exists"],
        ]),
    },
    "philosophy-c2-l59": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Straw man", "Misrepresenting an argument to make it easier to attack"],
        ]),
    },
    "philosophy-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Developing a thesis-driven argument", "Anchors a philosophy paper around a clear, defensible claim"],
        ]),
    },
    "philosophy-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying the hard problem", "Distinguishing the 'easy' and 'hard' problems in a case study"],
        ]),
    },
    "philosophy-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Applying entitlement theory", "Evaluating a redistribution policy through Nozick's lens"],
        ]),
    },
    "philosophy-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Applying the problem of induction", "Assessing whether a scientific generalization is justified"],
        ]),
    },
    "philosophy-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Comparing ancient schools", "Contrasting Stoic and Epicurean responses to adversity"],
        ]),
    },
    "philosophy-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a medieval synthesis", "Explaining how Aquinas merged faith and Aristotelian reason"],
        ]),
    },
    "philosophy-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Constructing a truth table", "Evaluating the truth value of a compound statement"],
        ]),
    },
    "philosophy-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Finding a counterexample", "Disproving an invalid argument form with a concrete case"],
        ]),
    },
    "philosophy-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing cosmologies", "Contrasting two Presocratic accounts of fundamental reality"],
        ]),
    },
    "philosophy-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Applying the tripartite soul", "Analyzing a modern dilemma using Plato's model of the soul"],
        ]),
    },
    "philosophy-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Critiquing the Forms", "Applying the Third Man Argument against Plato's theory"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Philosophy: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Philosophy lessons (completing 70/70).")


if __name__ == "__main__":
    main()
