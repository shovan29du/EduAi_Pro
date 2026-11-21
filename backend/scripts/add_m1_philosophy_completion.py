#!/usr/bin/env python3
"""Depth pass, M1 Philosophy: fill in real, hand-checked data_table
content for the 119 M1 Philosophy lessons not covered by the earlier
breadth-first batch. Brings M1 Philosophy to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
contemporary philosophy of mind/language/logic, the history of
philosophy from Plato to 20th-century Continental thought, metaethics
and normative ethics, metaphysics, epistemology, and philosophy of
science; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping). l3 was already completed
by an earlier breadth-first batch, so its data_table is hard-coded
here for reuse (it falls within l1-l20, so it is also reused for
l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Modal logic", "Formal logic that reasons about necessity and possibility"],
    ["Possible worlds semantics", "Evaluates modal claims by considering how things are across alternative possible worlds"],
])

CHARTS: dict[str, dict] = {
    "philosophy-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Existentialism", "Emphasizes individual existence, freedom, and the responsibility to create one's own meaning"],
    ])},
    "philosophy-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Applied ethics", "Applies moral theory to concrete practical dilemmas in medicine, business, and technology"],
    ])},
    "philosophy-m1-l4": {"data_table": table(["Theorem", "Implication"], [
        ["Gödel's incompleteness", "Any sufficiently powerful formal system contains true statements it cannot prove"],
    ])},
    "philosophy-m1-l5": {"data_table": table(["Philosopher", "Claim"], [
        ["Quine", "Challenged the sharp line between analytic (true by meaning) and synthetic (true by fact) statements"],
    ])},
    "philosophy-m1-l6": {"data_table": table(["Philosopher", "Claim"], [
        ["Sellars", "Argued sense experience cannot justify belief without already being conceptually structured"],
    ])},
    "philosophy-m1-l7": {"data_table": table(["Philosopher", "Claim"], [
        ["Davidson", "Argued we interpret others' language and beliefs together, assuming they are largely rational"],
    ])},
    "philosophy-m1-l8": {"data_table": table(["Philosopher", "Claim"], [
        ["Parfit", "Argued personal identity is less metaphysically deep than we assume; what matters is psychological continuity"],
    ])},
    "philosophy-m1-l9": {"data_table": table(["View", "Claim"], [
        ["Presentism", "Only the present moment exists"],
        ["Eternalism", "Past, present, and future all exist equally"],
    ])},
    "philosophy-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Extended mind thesis", "Argues cognitive processes can extend beyond the brain into tools and environment"],
    ])},
    "philosophy-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Explanatory gap", "The unclear link between physical brain processes and subjective conscious experience"],
    ])},
    "philosophy-m1-l12": {"data_table": table(["Philosopher", "Claim"], [
        ["Levinas", "Argued ethics begins with the irreducible responsibility we owe to the face of the Other"],
    ])},
    "philosophy-m1-l13": {"data_table": table(["Philosopher", "Claim"], [
        ["Foucault", "Showed how power operates through knowledge and discourse to shape what counts as truth"],
    ])},
    "philosophy-m1-l14": {"data_table": table(["Philosopher", "Claim"], [
        ["Derrida", "Deconstruction exposes how texts undermine their own apparent stable meaning"],
    ])},
    "philosophy-m1-l15": {"data_table": table(["Philosopher", "Claim"], [
        ["Habermas", "Argued rational consensus can emerge through open, undistorted communication"],
    ])},
    "philosophy-m1-l16": {"data_table": table(["View", "Claim"], [
        ["Cosmopolitanism", "Moral obligations extend equally to all humans regardless of nationality"],
        ["Nationalism", "Special obligations are owed primarily to one's own nation"],
    ])},
    "philosophy-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Global justice", "Examines what fairness and obligation look like across national borders, including migration"],
    ])},
    "philosophy-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Genetic enhancement ethics", "Debates whether modifying human traits raises distinct issues of fairness and identity"],
    ])},
    "philosophy-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Machine consciousness", "Asks whether an artificial system could have genuine subjective experience"],
    ])},
    "philosophy-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Research seminar argument", "Constructs and defends an original philosophical thesis through rigorous argument"],
    ])},
    "philosophy-m1-l21": {"data_table": table(["Philosopher", "Claim"], [
        ["Aristotle", "Substance is the primary category of being; form and matter together constitute a thing"],
    ])},
    "philosophy-m1-l22": {"data_table": table(["Philosopher", "Claim"], [
        ["Plato", "True reality consists of unchanging Forms, of which physical things are imperfect copies"],
    ])},
    "philosophy-m1-l23": {"data_table": table(["Philosopher", "Claim"], [
        ["Hegel", "History and consciousness develop through a dialectical process toward absolute self-understanding"],
    ])},
    "philosophy-m1-l24": {"data_table": table(["Philosopher", "Claim"], [
        ["Descartes", "Doubted everything doubtable to find an indubitable foundation: 'I think, therefore I am'"],
    ])},
    "philosophy-m1-l25": {"data_table": table(["Philosopher", "Claim"], [
        ["Spinoza", "Argued there is only one substance, which is identical with God and nature"],
    ])},
    "philosophy-m1-l26": {"data_table": table(["Philosopher", "Claim"], [
        ["Berkeley", "Argued to exist is to be perceived; there is no matter independent of minds"],
    ])},
    "philosophy-m1-l27": {"data_table": table(["Philosopher", "Claim"], [
        ["Nietzsche", "Proposed imagining your life recurring eternally as a test of affirming it fully"],
    ])},
    "philosophy-m1-l28": {"data_table": table(["Philosopher", "Claim"], [
        ["Kierkegaard", "Described the aesthetic, ethical, and religious stages of an individual's existence"],
    ])},
    "philosophy-m1-l29": {"data_table": table(["Philosopher", "Claim"], [
        ["Heidegger", "Authentic existence requires confronting one's own inevitable death"],
    ])},
    "philosophy-m1-l30": {"data_table": table(["Philosopher", "Claim"], [
        ["Sartre", "Humans are radically free and fully responsible for creating their own values"],
    ])},
    "philosophy-m1-l31": {"data_table": table(["Philosopher", "Claim"], [
        ["Merleau-Ponty", "Perception and thought are grounded in our lived, embodied experience of the world"],
    ])},
    "philosophy-m1-l32": {"data_table": table(["Philosopher", "Claim"], [
        ["Husserl", "Developed a method of bracketing assumptions to study consciousness as it directly appears"],
    ])},
    "philosophy-m1-l33": {"data_table": table(["Philosopher", "Claim"], [
        ["Wittgenstein", "Meaning comes from how words are used within rule-governed social 'language games'"],
    ])},
    "philosophy-m1-l34": {"data_table": table(["Philosopher", "Claim"], [
        ["Austin", "Some utterances don't just describe the world, they perform an action (speech acts)"],
    ])},
    "philosophy-m1-l35": {"data_table": table(["Philosopher", "Claim"], [
        ["Grice", "Listeners infer implied meaning beyond literal words using shared conversational norms"],
    ])},
    "philosophy-m1-l36": {"data_table": table(["Philosopher", "Claim"], [
        ["Kripke", "Names rigidly refer to the same individual across all possible worlds"],
    ])},
    "philosophy-m1-l37": {"data_table": table(["Philosopher", "Claim"], [
        ["Putnam", "Meaning depends partly on the external world, not solely on what's in a speaker's head"],
    ])},
    "philosophy-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Frame problem", "The difficulty of specifying which facts an AI system should treat as unaffected by an action"],
    ])},
    "philosophy-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Multiple realizability", "The same mental state could in principle be realized by different physical substrates"],
    ])},
    "philosophy-m1-l40": {"data_table": table(["Argument", "Claim"], [
        ["Chinese Room", "Symbol manipulation alone, without understanding, could produce apparently intelligent output"],
    ])},
    "philosophy-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Hard problem of consciousness", "Explaining why physical processes give rise to subjective experience at all"],
    ])},
    "philosophy-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Panpsychism", "The view that consciousness, in some minimal form, is a fundamental feature of all matter"],
    ])},
    "philosophy-m1-l43": {"data_table": table(["Argument", "Claim"], [
        ["Mary's Room", "A scientist who knows all physical facts about color still learns something new upon seeing it"],
    ])},
    "philosophy-m1-l44": {"data_table": table(["View", "Claim"], [
        ["Compatibilism", "Free will and determinism can coexist if actions flow from one's own desires"],
    ])},
    "philosophy-m1-l45": {"data_table": table(["View", "Claim"], [
        ["Hard determinism", "All events, including choices, are fully determined, so free will and blame are illusions"],
    ])},
    "philosophy-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Frankfurt case", "Shows moral responsibility may not require the ability to have done otherwise"],
    ])},
    "philosophy-m1-l47": {"data_table": table(["Philosopher", "Claim"], [
        ["Scanlon", "An act is wrong if it could not be justified to others under principles they couldn't reasonably reject"],
    ])},
    "philosophy-m1-l48": {"data_table": table(["Philosopher", "Claim"], [
        ["Rawls", "Justice principles should be chosen behind a veil of ignorance about one's own position in society"],
    ])},
    "philosophy-m1-l49": {"data_table": table(["Philosopher", "Claim"], [
        ["Nozick", "Just holdings arise from just acquisition and voluntary transfer, not patterned redistribution"],
    ])},
    "philosophy-m1-l50": {"data_table": table(["Philosopher", "Claim"], [
        ["Sen and Nussbaum", "Justice should be measured by people's real capabilities to live a life they value"],
    ])},
    "philosophy-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Eudaimonia", "Human flourishing achieved through a life of virtuous activity"],
    ])},
    "philosophy-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Categorical imperative", "Act only according to a rule you could will to become a universal law"],
    ])},
    "philosophy-m1-l53": {"data_table": table(["View", "Feature"], [
        ["Act utilitarianism", "Evaluates each individual action by its consequences"],
        ["Rule utilitarianism", "Evaluates whether following a general rule maximizes good outcomes"],
    ])},
    "philosophy-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Person-affecting principle", "Holds that an outcome can only be worse if it is worse for some specific person"],
    ])},
    "philosophy-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Non-identity problem", "A choice can affect who is born, complicating claims that a person was 'harmed' by it"],
    ])},
    "philosophy-m1-l56": {"data_table": table(["View", "Claim"], [
        ["Moral particularism", "Denies moral judgments require fixed general rules; context determines what matters"],
    ])},
    "philosophy-m1-l57": {"data_table": table(["View", "Claim"], [
        ["Moral realism", "Moral facts exist independently of what anyone believes or desires"],
    ])},
    "philosophy-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Error theory", "All moral claims are systematically false because there are no moral facts"],
    ])},
    "philosophy-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Expressivism", "Moral statements express attitudes rather than describe objective facts"],
    ])},
    "philosophy-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Is-ought problem", "Descriptive facts alone cannot logically entail a prescriptive moral conclusion"],
    ])},
    "philosophy-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Doctrine of double effect", "A harmful side effect can be permissible if it isn't the intended means to a good end"],
    ])},
    "philosophy-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Jus ad bellum / jus in bello", "The justice of entering a war versus the justice of conduct within it"],
    ])},
    "philosophy-m1-l63": {"data_table": table(["View", "Claim"], [
        ["Political realism", "International relations are governed by power and self-interest, not shared moral norms"],
    ])},
    "philosophy-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Ethics of future generations", "Asks what moral obligations current people owe to people who don't yet exist"],
    ])},
    "philosophy-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Teletransportation puzzle", "Tests whether identity survives being destroyed and perfectly recreated elsewhere"],
    ])},
    "philosophy-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Ship of Theseus", "Asks whether an object remains the same after all its parts are gradually replaced"],
    ])},
    "philosophy-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Mereology", "The study of how parts relate to the wholes they compose"],
    ])},
    "philosophy-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Modal realism", "The view that all possible worlds are just as real as the actual world"],
    ])},
    "philosophy-m1-l69": {"data_table": table(["View", "Claim"], [
        ["Four-dimensionalism", "Objects extend through time as temporal parts, much like they extend through space"],
    ])},
    "philosophy-m1-l70": {"data_table": table(["View", "Claim"], [
        ["Realism about universals", "Properties shared by many things exist as real, mind-independent entities"],
        ["Nominalism", "Only particular things exist; universals are just names"],
    ])},
    "philosophy-m1-l71": {"data_table": table(["Theory", "Claim"], [
        ["Counterfactual theory of causation", "A causes B if B would not have occurred without A"],
    ])},
    "philosophy-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Problem of other minds", "How can we know other beings have conscious experiences like our own?"],
    ])},
    "philosophy-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Epistemic contextualism", "What counts as 'knowing' something can shift depending on the conversational context"],
    ])},
    "philosophy-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Reliabilism", "A belief is justified if it was produced by a reliably truth-conducive process"],
    ])},
    "philosophy-m1-l75": {"data_table": table(["View", "Claim"], [
        ["Foundationalism", "Justified beliefs rest on basic, self-justifying foundational beliefs"],
        ["Coherentism", "Beliefs are justified by fitting coherently with each other, with no privileged foundation"],
    ])},
    "philosophy-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Social epistemology (testimony)", "Studies how and when we're justified in believing what others tell us"],
    ])},
    "philosophy-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Epistemic injustice", "A wrong done to someone specifically in their capacity as a knower"],
    ])},
    "philosophy-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Feminist critique of objectivity", "Questions whether claimed 'neutral' knowledge actually reflects a particular perspective"],
    ])},
    "philosophy-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Metanarrative critique", "Postmodern skepticism toward grand, unifying explanations of history or truth"],
    ])},
    "philosophy-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Ren", "The Confucian virtue of benevolence and humaneness toward others"],
    ])},
    "philosophy-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Ubuntu", "An African philosophy holding that personhood is constituted through community"],
    ])},
    "philosophy-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Underdetermination", "Available evidence is often compatible with more than one scientific theory"],
    ])},
    "philosophy-m1-l83": {"data_table": table(["Philosopher", "Claim"], [
        ["Kuhn", "Science progresses through revolutionary paradigm shifts, not just steady accumulation"],
    ])},
    "philosophy-m1-l84": {"data_table": table(["Philosopher", "Claim"], [
        ["Popper", "A theory is scientific only if it can, in principle, be falsified by observation"],
    ])},
    "philosophy-m1-l85": {"data_table": table(["Concept", "Distinction"], [
        ["Sense", "The mode of presentation or meaning of a term"],
        ["Reference", "The actual object a term picks out in the world"],
    ])},
    "philosophy-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Philosophy of human enhancement", "Examines the ethical stakes of using technology to improve human capacities"],
    ])},
    "philosophy-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Deep ecology", "Holds that nature has intrinsic value independent of its usefulness to humans"],
    ])},
    "philosophy-m1-l88": {"data_table": table(["Debate", "Positions"], [
        ["Hart vs. Dworkin", "Whether law is a system of social rules, or is grounded in underlying moral principles"],
    ])},
    "philosophy-m1-l89": {"data_table": table(["Philosopher", "Claim"], [
        ["MacIntyre", "Modern moral discourse is fragmented because it has lost a shared teleological tradition"],
    ])},
    "philosophy-m1-l90": {"data_table": table(["Philosopher", "Claim"], [
        ["Bernard Williams", "Criticized utilitarianism for demanding people abandon personal integrity for the greater good"],
    ])},
    "philosophy-m1-l91": {"data_table": table(["Philosopher", "Claim"], [
        ["Iris Murdoch", "Moral life centers on the disciplined, loving attention we pay to others and reality"],
    ])},
    "philosophy-m1-l92": {"data_table": table(["Philosopher", "Claim"], [
        ["Martha Nussbaum", "Emotions are themselves forms of evaluative cognitive judgment, not mere feelings"],
    ])},
    "philosophy-m1-l93": {"data_table": table(["Philosopher", "Claim"], [
        ["Charles Taylor", "Modern identity is shaped by historically developed frameworks of value and meaning"],
    ])},
    "philosophy-m1-l94": {"data_table": table(["Philosopher", "Claim"], [
        ["Judith Butler", "Gender is not a fixed essence but is constituted through repeated performative acts"],
    ])},
    "philosophy-m1-l95": {"data_table": table(["Philosopher", "Claim"], [
        ["Jacques Rancière", "Politics arises through dissensus that disrupts an established distribution of the sensible"],
    ])},
    "philosophy-m1-l96": {"data_table": table(["Philosopher", "Claim"], [
        ["Alain Badiou", "Truth emerges through fidelity to an unpredictable, world-changing 'event'"],
    ])},
    "philosophy-m1-l97": {"data_table": table(["Philosopher", "Claim"], [
        ["Giorgio Agamben", "Sovereign power can suspend law itself, reducing subjects to 'bare life'"],
    ])},
    "philosophy-m1-l98": {"data_table": table(["Philosopher", "Claim"], [
        ["Deleuze and Guattari", "Used the rhizome as a model for non-hierarchical, decentralized thought and structure"],
    ])},
    "philosophy-m1-l99": {"data_table": table(["Philosopher", "Claim"], [
        ["Paul Ricoeur", "Selfhood is constituted through the narratives we tell to interpret our own lives"],
    ])},
    "philosophy-m1-l100": {"data_table": table(["Philosopher", "Claim"], [
        ["Simone Weil", "True attention is a rare, demanding form of selfless openness to reality and suffering"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"philosophy-m1-l{base_n}"
    worked_key = f"philosophy-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Philosophy: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Philosophy lessons (completing 120/120).")


if __name__ == "__main__":
    main()
