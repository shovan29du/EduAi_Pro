#!/usr/bin/env python3
"""Depth pass, M1 Critical Thinking: fill in real, hand-checked
data_table content for the 99 M1 Critical Thinking lessons not
covered by the earlier breadth-first batch. Brings M1 Critical
Thinking to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "critical-thinking-m1-l1": {
        "data_table": table(["Field", "Feature"], [
            ["Evidence evaluation & research literacy", "Assesses the reliability and relevance of supporting evidence"],
        ]),
    },
    "critical-thinking-m1-l2": {
        "data_table": table(["Field", "Feature"], [
            ["Applied decision analysis", "Structures real-world choices using formal decision-making frameworks"],
        ]),
    },
    "critical-thinking-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Testimonial knowledge", "Examines under what conditions belief based on others' word counts as knowledge"],
        ]),
    },
    "critical-thinking-m1-l5": {
        "data_table": table(["Concept", "Detail"], [
            ["Dialectical structure", "Models argumentation as a structured exchange of moves between parties"],
        ]),
    },
    "critical-thinking-m1-l6": {
        "data_table": table(["Concept", "Detail"], [
            ["Paradigm shift", "Kuhn's model of science advancing through periodic revolutionary reconceptualization"],
        ]),
    },
    "critical-thinking-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Underdetermination", "Available evidence can be equally consistent with more than one competing theory"],
        ]),
    },
    "critical-thinking-m1-l8": {
        "data_table": table(["Method", "Purpose"], [
            ["Multi-criteria decision analysis", "Weighs multiple competing objectives to reach a structured decision"],
        ]),
    },
    "critical-thinking-m1-l9": {
        "data_table": table(["Concept", "Detail"], [
            ["Evolutionary game theory", "Models how strategies spread through a population under selective pressure"],
        ]),
    },
    "critical-thinking-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Bounded rationality", "Behavioral economics critiques the assumption of perfectly rational choice"],
        ]),
    },
    "critical-thinking-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Complex adaptive system", "A system whose components adapt and interact to produce emergent collective behavior"],
        ]),
    },
    "critical-thinking-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Computational propaganda", "Automated accounts and algorithms can be used to manipulate public opinion at scale"],
        ]),
    },
    "critical-thinking-m1-l13": {
        "data_table": table(["Threat", "Detail"], [
            ["Deepfake", "AI-generated media that convincingly fabricates a person's speech or actions"],
        ]),
    },
    "critical-thinking-m1-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Epistemology of disagreement", "Examines how rational agents should respond upon learning a peer disagrees"],
        ]),
    },
    "critical-thinking-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Applied bioethics reasoning", "Applies ethical frameworks to concrete dilemmas in medicine and life science"],
        ]),
    },
    "critical-thinking-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Global justice", "Examines moral obligations that extend across national and cultural boundaries"],
        ]),
    },
    "critical-thinking-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Curriculum design", "Sequences learning objectives to build critical thinking skill progressively"],
        ]),
    },
    "critical-thinking-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Pedagogy research methods", "Studies which teaching approaches most effectively build reasoning skill"],
        ]),
    },
    "critical-thinking-m1-l19": {
        "data_table": table(["Step", "Purpose"], [
            ["Peer review in argumentation studies", "Independent experts evaluate scholarly work before publication"],
        ]),
    },
    "critical-thinking-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Applied case study capstone", "Synthesizes advanced reasoning tools into an original analysis and defense"],
        ]),
    },
    "critical-thinking-m1-l21": {
        "data_table": table(["Fallacy Type", "Example"], [
            ["Relevance fallacy", "Introduces an irrelevant consideration to distract from the actual argument"],
            ["Ambiguity fallacy", "Exploits unclear or shifting word meaning to mislead"],
        ]),
    },
    "critical-thinking-m1-l22": {
        "data_table": table(["Fallacy", "Form"], [
            ["Affirming the consequent", "If P then Q; Q; therefore P (invalid)"],
        ]),
    },
    "critical-thinking-m1-l23": {
        "data_table": table(["Fallacy", "Detail"], [
            ["Base rate neglect", "Ignoring the underlying prevalence rate when judging a probability"],
        ]),
    },
    "critical-thinking-m1-l24": {
        "data_table": table(["Element", "Role"], [
            ["Claim", "The conclusion being argued for"],
            ["Warrant", "The reasoning connecting evidence to the claim"],
        ]),
    },
    "critical-thinking-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Pragma-dialectics", "Models argumentation as a critical discussion aimed at resolving a difference of opinion"],
        ]),
    },
    "critical-thinking-m1-l26": {
        "data_table": table(["Appeal", "Meaning"], [
            ["Ethos", "Appeal to credibility/character"],
            ["Pathos", "Appeal to emotion"],
            ["Logos", "Appeal to logic/reason"],
        ]),
    },
    "critical-thinking-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Defeasible reasoning", "A conclusion held reasonable can be withdrawn upon learning new information"],
        ]),
    },
    "critical-thinking-m1-l28": {
        "data_table": table(["Concept", "Detail"], [
            ["Structure mapping theory", "Analogical reasoning transfers relational structure, not just surface similarity"],
        ]),
    },
    "critical-thinking-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Critical thinking disposition", "The willingness, not just ability, to engage in careful reasoning"],
        ]),
    },
    "critical-thinking-m1-l30": {
        "data_table": table(["Type", "Detail"], [
            ["Abusive ad hominem", "Attacks a person's character rather than their argument"],
            ["Circumstantial ad hominem", "Points to a person's circumstances to dismiss their argument"],
        ]),
    },
    "critical-thinking-m1-l31": {
        "data_table": table(["Technique", "Detail"], [
            ["Straw man", "Misrepresents an opponent's argument to make it easier to attack"],
            ["Steel man", "Represents an opponent's argument in its strongest possible form"],
        ]),
    },
    "critical-thinking-m1-l32": {
        "data_table": table(["Bias", "Detail"], [
            ["Anchoring bias", "Initial information disproportionately influences subsequent judgments"],
            ["Availability bias", "Easily recalled examples are judged as more probable than they are"],
        ]),
    },
    "critical-thinking-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Gettier problem", "Shows that justified true belief can fail to count as genuine knowledge"],
        ]),
    },
    "critical-thinking-m1-l34": {
        "data_table": table(["Theory", "View"], [
            ["Foundationalism", "Justified beliefs rest on basic, non-inferential beliefs"],
            ["Coherentism", "Justification comes from a belief's fit within a coherent web of beliefs"],
        ]),
    },
    "critical-thinking-m1-l35": {
        "data_table": table(["Theory", "Focus"], [
            ["Reliabilism", "Justification depends on whether a belief was produced by a reliable process"],
        ]),
    },
    "critical-thinking-m1-l36": {
        "data_table": table(["Concept", "Detail"], [
            ["Cartesian doubt", "Systematically questions all beliefs to find an indubitable foundation"],
        ]),
    },
    "critical-thinking-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Degree of belief", "Probabilistic argumentation represents confidence as a graded quantity rather than binary"],
        ]),
    },
    "critical-thinking-m1-l38": {
        "data_table": table(["Concept", "Detail"], [
            ["Fuzzy logic", "Allows truth values between 0 and 1 to model vague or graded predicates"],
        ]),
    },
    "critical-thinking-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Paraconsistent logic", "Permits reasoning in the presence of contradiction without trivializing the system"],
        ]),
    },
    "critical-thinking-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Argumentation scheme", "A stereotypical reasoning pattern paired with matching critical questions to evaluate it"],
        ]),
    },
    "critical-thinking-m1-l41": {
        "data_table": table(["Paradox", "Statement"], [
            ["Sorites paradox", "Removing one grain from a heap never makes it a non-heap, yet eventually it is"],
        ]),
    },
    "critical-thinking-m1-l42": {
        "data_table": table(["Condition", "Example"], [
            ["Necessary condition", "Oxygen is necessary for fire"],
            ["Sufficient condition", "Being a square is sufficient for being a rectangle"],
        ]),
    },
    "critical-thinking-m1-l43": {
        "data_table": table(["Method", "Purpose"], [
            ["Mill's method of agreement", "Identifies a common factor across multiple cases sharing an effect"],
        ]),
    },
    "critical-thinking-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Possible worlds semantics", "Evaluates counterfactual claims by comparing across hypothetical alternative worlds"],
        ]),
    },
    "critical-thinking-m1-l45": {
        "data_table": table(["Paradox", "Detail"], [
            ["Preface paradox", "An author may rationally believe each claim in a book yet believe the book contains an error"],
        ]),
    },
    "critical-thinking-m1-l46": {
        "data_table": table(["Concept", "Detail"], [
            ["Groupthink", "Social pressure toward consensus can suppress independent critical judgment"],
        ]),
    },
    "critical-thinking-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Deliberative democracy", "Legitimizes political decisions through open, reasoned public discussion"],
        ]),
    },
    "critical-thinking-m1-l48": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic questioning", "Uses repeated probing questions to expose assumptions and contradictions"],
        ]),
    },
    "critical-thinking-m1-l49": {
        "data_table": table(["Model", "Detail"], [
            ["Deductive-nomological model", "Explains an event by deducing it from general laws plus initial conditions"],
        ]),
    },
    "critical-thinking-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Inference to the best explanation", "Legal reasoning often favors the hypothesis best accounting for the evidence"],
        ]),
    },
    "critical-thinking-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Confounding variable", "An unaccounted factor that affects both cause and effect being studied"],
        ]),
    },
    "critical-thinking-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Risk perception psychology", "Perceived risk often diverges sharply from statistical risk"],
        ]),
    },
    "critical-thinking-m1-l53": {
        "data_table": table(["Bias", "Detail"], [
            ["Framing effect", "Identical information leads to different decisions depending on presentation"],
        ]),
    },
    "critical-thinking-m1-l54": {
        "data_table": table(["Heuristic", "Detail"], [
            ["Representativeness heuristic", "Judges probability by similarity to a prototype rather than base rates"],
        ]),
    },
    "critical-thinking-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Forensic evidence evaluation", "Requires careful scrutiny of chain of custody and scientific validity"],
        ]),
    },
    "critical-thinking-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Falsificationism", "Popper's criterion that scientific claims must be capable of being proven false"],
        ]),
    },
    "critical-thinking-m1-l57": {
        "data_table": table(["Tool", "Purpose"], [
            ["Argument map", "Visually diagrams how premises support or attack a conclusion"],
        ]),
    },
    "critical-thinking-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Legal dialectical argumentation", "Adversarial legal process structures opposing arguments toward a resolved verdict"],
        ]),
    },
    "critical-thinking-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Rhetoric of science", "Scientific persuasion relies on rhetorical strategy, not pure logical demonstration alone"],
        ]),
    },
    "critical-thinking-m1-l60": {
        "data_table": table(["Concept", "Detail"], [
            ["Emotion in deliberation", "Emotion can inform rather than merely distort rational decision-making"],
        ]),
    },
    "critical-thinking-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Cognitive load", "Time pressure can degrade reasoning quality by overtaxing working memory"],
        ]),
    },
    "critical-thinking-m1-l62": {
        "data_table": table(["Concept", "Detail"], [
            ["Nudge theory", "Shapes choices through subtle design changes while preserving freedom of choice"],
        ]),
    },
    "critical-thinking-m1-l63": {
        "data_table": table(["Concept", "Detail"], [
            ["Manipulation vs rational appeal", "Distinguishes legitimate persuasion from exploiting cognitive bias unfairly"],
        ]),
    },
    "critical-thinking-m1-l64": {
        "data_table": table(["Feature", "Detail"], [
            ["Conspiracy theory", "Often unfalsifiable and treats contrary evidence as further proof of a cover-up"],
        ]),
    },
    "critical-thinking-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Media statistics literacy", "Requires checking sample size, methodology, and framing before trusting a reported statistic"],
        ]),
    },
    "critical-thinking-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Problem of induction", "Hume argued past regularity cannot logically guarantee future occurrence"],
        ]),
    },
    "critical-thinking-m1-l67": {
        "data_table": table(["Operator", "Meaning"], [
            ["Necessarily (Box)", "True in all possible worlds"],
            ["Possibly (Diamond)", "True in at least one possible world"],
        ]),
    },
    "critical-thinking-m1-l68": {
        "data_table": table(["Operator", "Meaning"], [
            ["Obligatory", "It ought to be the case that..."],
            ["Permissible", "It is allowed that..."],
        ]),
    },
    "critical-thinking-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Common knowledge", "Epistemic logic formalizes what all agents know that all agents know"],
        ]),
    },
    "critical-thinking-m1-l70": {
        "data_table": table(["Concept", "Detail"], [
            ["Relevance theory", "Communication succeeds by conveying maximal relevant information for minimal processing effort"],
        ]),
    },
    "critical-thinking-m1-l71": {
        "data_table": table(["Concept", "Detail"], [
            ["Speech act", "An utterance can itself perform an action, not merely describe one"],
        ]),
    },
    "critical-thinking-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["Legal precedent reasoning", "Applies analogy from prior decided cases to resolve a current dispute"],
        ]),
    },
    "critical-thinking-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["Intelligence analysis reasoning", "Requires structured techniques to counter analytic bias under uncertainty"],
        ]),
    },
    "critical-thinking-m1-l74": {
        "data_table": table(["Practice", "Purpose"], [
            ["Red teaming", "Deliberately probes a plan or system for weaknesses before an adversary does"],
        ]),
    },
    "critical-thinking-m1-l75": {
        "data_table": table(["Method", "Purpose"], [
            ["Delphi method", "Aggregates structured, anonymous expert judgment through iterative rounds"],
        ]),
    },
    "critical-thinking-m1-l76": {
        "data_table": table(["Method", "Purpose"], [
            ["Scenario planning", "Explores multiple plausible futures to prepare for deep uncertainty"],
        ]),
    },
    "critical-thinking-m1-l77": {
        "data_table": table(["Method", "Purpose"], [
            ["Cost-benefit analysis", "Weighs quantified costs against benefits to guide a decision"],
        ]),
    },
    "critical-thinking-m1-l78": {
        "data_table": table(["Principle", "Detail"], [
            ["Precautionary principle", "Favors caution against serious harm even without full scientific certainty"],
        ]),
    },
    "critical-thinking-m1-l79": {
        "data_table": table(["Concept", "Detail"], [
            ["Prospect theory", "People evaluate outcomes relative to a reference point, weighing losses more heavily than gains"],
        ]),
    },
    "critical-thinking-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Availability cascade", "A repeated claim gains apparent plausibility through mere frequent public repetition"],
        ]),
    },
    "critical-thinking-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Standpoint epistemology", "Argues social position shapes what knowledge is accessible to a knower"],
        ]),
    },
    "critical-thinking-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Feminist epistemology", "Questions whether traditional objectivity ideals overlook situated knowledge"],
        ]),
    },
    "critical-thinking-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Naturalistic fallacy", "Mistakenly infers a moral conclusion directly from a natural fact"],
        ]),
    },
    "critical-thinking-m1-l84": {
        "data_table": table(["Problem", "Detail"], [
            ["Is-ought problem", "Descriptive facts alone cannot logically establish a prescriptive conclusion"],
        ]),
    },
    "critical-thinking-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["Problem of other minds", "We infer others have minds by analogy to our own, without direct access"],
        ]),
    },
    "critical-thinking-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Equal weight view", "Holds that peer disagreement should reduce confidence roughly equally for both parties"],
        ]),
    },
    "critical-thinking-m1-l87": {
        "data_table": table(["Use", "Detail"], [
            ["Legitimate appeal to authority", "Cites a genuine expert within their relevant field of competence"],
            ["Fallacious appeal to authority", "Cites a non-expert or a source outside their field"],
        ]),
    },
    "critical-thinking-m1-l88": {
        "data_table": table(["Version", "Detail"], [
            ["Logical slippery slope", "Claims one step logically necessitates an extreme conclusion"],
            ["Empirical slippery slope", "Claims one step will causally lead to an extreme outcome"],
        ]),
    },
    "critical-thinking-m1-l89": {
        "data_table": table(["Fallacy", "Detail"], [
            ["False dilemma", "Presents only two options when more actually exist"],
        ]),
    },
    "critical-thinking-m1-l90": {
        "data_table": table(["Fallacy", "Detail"], [
            ["Circular reasoning", "The conclusion is assumed within one of the premises"],
        ]),
    },
    "critical-thinking-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Burden of proof", "The party making a claim generally bears responsibility for supporting it"],
        ]),
    },
    "critical-thinking-m1-l92": {
        "data_table": table(["Instrument", "Purpose"], [
            ["California Critical Thinking Skills Test", "A standardized measure of core critical thinking competencies"],
        ]),
    },
    "critical-thinking-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Metacognition", "Reflecting on and regulating one's own thinking process"],
        ]),
    },
    "critical-thinking-m1-l94": {
        "data_table": table(["Concept", "Detail"], [
            ["Wisdom of crowds", "Independent estimates can average to a highly accurate result"],
        ]),
    },
    "critical-thinking-m1-l95": {
        "data_table": table(["Method", "Purpose"], [
            ["Adversarial collaboration", "Opposing researchers jointly design a study to resolve their disagreement"],
        ]),
    },
    "critical-thinking-m1-l96": {
        "data_table": table(["Method", "Purpose"], [
            ["Case-based reasoning", "Solves new problems by adapting solutions from similar past cases"],
        ]),
    },
    "critical-thinking-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Epistemic trespassing", "An expert in one field overreaches by making authoritative claims outside their expertise"],
        ]),
    },
    "critical-thinking-m1-l98": {
        "data_table": table(["Paradox", "Detail"], [
            ["Paradox of analysis", "A correct conceptual analysis seems either trivial or uninformative"],
        ]),
    },
    "critical-thinking-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Robustness analysis", "Confidence in a model's conclusion grows when it holds across varied model assumptions"],
        ]),
    },
    "critical-thinking-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Deep disagreement", "Disputes rooted in fundamentally different underlying frameworks resist ordinary resolution"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Modal Operator", "Meaning"], [
        ["Necessarily (Box)", "True in all possible worlds"],
        ["Possibly (Diamond)", "True in at least one possible world"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"critical-thinking-m1-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"critical-thinking-m1-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"critical-thinking-m1-l{worked_n}"] = dict(_l3_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Critical Thinking lessons (completing 120/120).")


if __name__ == "__main__":
    main()
