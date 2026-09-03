#!/usr/bin/env python3
"""Depth pass, C1 Critical Thinking: fill in real, hand-checked
data_table content for the 99 C1 Critical Thinking lessons not covered
by the earlier breadth-first batch. Brings C1 Critical Thinking to full
100/100 coverage.

Note: unlike most C1 subjects (70 lessons), Critical Thinking has 100
lessons: l1-l60 core topics, l61-l63 "Foundations 2" duplicates, l64-l80
"Comparative Case Study" lessons, and l81-l100 "Applied Research Seminar"
lessons.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "critical-thinking-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Argument", "A set of premises offered in support of a conclusion"],
        ]),
    },
    "critical-thinking-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Cognitive bias", "A systematic pattern of deviation from rational judgment"], ["Fallacy", "An error in reasoning that undermines an argument's logic"],
        ]),
    },
    "critical-thinking-c1-l4": {
        "data_table": table(["Connective", "Meaning"], [
            ["AND (∧)", "True only when both statements are true"], ["OR (∨)", "True when at least one statement is true"],
        ]),
    },
    "critical-thinking-c1-l5": {
        "data_table": table(["p", "q", "p AND q"], [
            ["T", "T", "T"], ["T", "F", "F"], ["F", "F", "F"],
        ]),
    },
    "critical-thinking-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Valid argument", "The conclusion follows logically from the premises"], ["Sound argument", "Valid and all premises are actually true"],
        ]),
    },
    "critical-thinking-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Predicate logic", "Extends propositional logic with quantifiers like 'all' and 'some'"],
        ]),
    },
    "critical-thinking-c1-l8": {
        "data_table": table(["Condition", "Example"], [
            ["Necessary condition", "Oxygen is necessary for fire"], ["Sufficient condition", "Being a square is sufficient for being a rectangle"],
        ]),
    },
    "critical-thinking-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Epistemology", "The branch of philosophy studying the nature and limits of knowledge"],
        ]),
    },
    "critical-thinking-c1-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Justified true belief", "The traditional definition of knowledge as a belief that is true and justified"],
        ]),
    },
    "critical-thinking-c1-l11": {
        "data_table": table(["Source", "Example"], [
            ["Perception", "Knowing it's raining by seeing it"], ["Testimony", "Knowing a historical fact because a reliable source reported it"],
        ]),
    },
    "critical-thinking-c1-l12": {
        "data_table": table(["Element", "Role"], [
            ["Claim", "The conclusion being argued for"], ["Warrant", "The reasoning connecting evidence to the claim"],
        ]),
    },
    "critical-thinking-c1-l13": {
        "data_table": table(["Element", "Role"], [
            ["Reason", "Supports the claim with evidence"], ["Warrant", "Justifies why the reason supports the claim"],
        ]),
    },
    "critical-thinking-c1-l14": {
        "data_table": table(["Step", "Purpose"], [
            ["Forming a testable hypothesis", "Allows a claim to be verified or falsified"],
        ]),
    },
    "critical-thinking-c1-l15": {
        "data_table": table(["Concept", "Meaning"], [
            ["Correlation", "Two variables change together"], ["Causation", "One variable directly produces a change in another"],
        ]),
    },
    "critical-thinking-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Statistical reasoning", "Drawing sound conclusions from numerical data"],
        ]),
    },
    "critical-thinking-c1-l17": {
        "data_table": table(["Practice", "Reason"], [
            ["Checking the sample size", "Small samples can produce misleading statistics"],
        ]),
    },
    "critical-thinking-c1-l18": {
        "data_table": table(["Method", "Purpose"], [
            ["Socratic questioning", "Uses repeated probing questions to expose assumptions"],
        ]),
    },
    "critical-thinking-c1-l19": {
        "data_table": table(["Question Type", "Purpose"], [
            ["Clarifying question", "Removes ambiguity in a claim"],
        ]),
    },
    "critical-thinking-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Systems thinking", "Analyzes how parts of a system interact rather than in isolation"],
        ]),
    },
    "critical-thinking-c1-l21": {
        "data_table": table(["Type", "Direction"], [
            ["Deductive reasoning", "General premises to a certain specific conclusion"], ["Inductive reasoning", "Specific observations to a probable general conclusion"],
        ]),
    },
    "critical-thinking-c1-l22": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Ad hominem", "Attacking the person instead of the argument"], ["Straw man", "Misrepresenting an argument to make it easier to attack"],
        ]),
    },
    "critical-thinking-c1-l23": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["False dilemma", "Presenting only two options when more exist"], ["Slippery slope", "Claiming one step inevitably leads to an extreme outcome"],
        ]),
    },
    "critical-thinking-c1-l24": {
        "data_table": table(["Sign", "Detail"], [
            ["One-sided evidence", "Only supporting facts are presented, contrary facts ignored"],
        ]),
    },
    "critical-thinking-c1-l25": {
        "data_table": table(["Part", "Role"], [
            ["Premise", "A statement offered as evidence"], ["Conclusion", "The claim the premises are meant to support"],
        ]),
    },
    "critical-thinking-c1-l26": {
        "data_table": table(["Criterion", "Question"], [
            ["Expertise", "Is the source qualified on this topic?"], ["Bias", "Does the source have a motive to mislead?"],
        ]),
    },
    "critical-thinking-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Analogical reasoning", "Drawing conclusions based on similarities between two cases"],
        ]),
    },
    "critical-thinking-c1-l28": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Circular reasoning", "The conclusion is restated as one of the premises"],
        ]),
    },
    "critical-thinking-c1-l29": {
        "data_table": table(["Type", "Example"], [
            ["Fact", "The boiling point of water is 100°C at sea level"], ["Opinion", "This is the best novel ever written"],
        ]),
    },
    "critical-thinking-c1-l30": {
        "data_table": table(["Principle", "Meaning"], [
            ["Burden of proof", "The obligation to provide evidence lies with the person making the claim"],
        ]),
    },
    "critical-thinking-c1-l31": {
        "data_table": table(["Type", "Feature"], [
            ["Formal fallacy", "An error in the logical structure of an argument"], ["Informal fallacy", "An error in the content or context of an argument"],
        ]),
    },
    "critical-thinking-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Confirmation bias", "The tendency to favor information that confirms existing beliefs"],
        ]),
    },
    "critical-thinking-c1-l33": {
        "data_table": table(["Bias", "Meaning"], [
            ["Anchoring", "Relying too heavily on the first piece of information encountered"], ["Availability heuristic", "Overestimating the likelihood of events that come easily to mind"],
        ]),
    },
    "critical-thinking-c1-l34": {
        "data_table": table(["Use", "Example"], [
            ["Venn diagram", "Visualizes overlap and relationships between categories or arguments"],
        ]),
    },
    "critical-thinking-c1-l35": {
        "data_table": table(["Rule", "Form"], [
            ["Modus ponens", "If p then q; p; therefore q"], ["Modus tollens", "If p then q; not q; therefore not p"],
        ]),
    },
    "critical-thinking-c1-l36": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Annotating while reading", "Tracks key claims and questions as they arise"],
        ]),
    },
    "critical-thinking-c1-l37": {
        "data_table": table(["Technique", "Example"], [
            ["Emotional appeal", "Using imagery that evokes happiness to sell a product"],
        ]),
    },
    "critical-thinking-c1-l38": {
        "data_table": table(["Skill", "Purpose"], [
            ["Media literacy", "Evaluates the credibility and intent behind news content"],
        ]),
    },
    "critical-thinking-c1-l39": {
        "data_table": table(["Framework", "Feature"], [
            ["Cost-benefit analysis", "Weighs expected gains against expected losses"],
        ]),
    },
    "critical-thinking-c1-l40": {
        "data_table": table(["Technique", "Example"], [
            ["Appeal to fear", "Suggesting a decision will lead to a frightening outcome"],
        ]),
    },
    "critical-thinking-c1-l41": {
        "data_table": table(["Element", "Purpose"], [
            ["Argument map", "Visually diagrams how claims and evidence connect"],
        ]),
    },
    "critical-thinking-c1-l42": {
        "data_table": table(["Practice", "Reason"], [
            ["Defining key terms early", "Prevents arguments over ambiguous language"],
        ]),
    },
    "critical-thinking-c1-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Reframing a problem", "Reveals new solutions by changing perspective"],
        ]),
    },
    "critical-thinking-c1-l44": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Hasty generalization", "Drawing a broad conclusion from too small a sample"],
        ]),
    },
    "critical-thinking-c1-l45": {
        "data_table": table(["Step", "Purpose"], [
            ["Listing all costs and benefits", "Ensures a comprehensive comparison before deciding"],
        ]),
    },
    "critical-thinking-c1-l46": {
        "data_table": table(["Claim Type", "Example"], [
            ["Correlation claim", "Ice cream sales and drowning rates both rise in summer"], ["Causal claim", "Smoking causes lung cancer"],
        ]),
    },
    "critical-thinking-c1-l47": {
        "data_table": table(["Framework", "Focus"], [
            ["Consequentialism", "Judges actions by their outcomes"], ["Deontology", "Judges actions by adherence to rules or duties"],
        ]),
    },
    "critical-thinking-c1-l48": {
        "data_table": table(["Element", "Role"], [
            ["Claim", "The position being defended"], ["Rebuttal", "A response countering the opposing argument"],
        ]),
    },
    "critical-thinking-c1-l49": {
        "data_table": table(["Skill", "Purpose"], [
            ["Critical listening", "Evaluates a speaker's reasoning while listening, not just their words"],
        ]),
    },
    "critical-thinking-c1-l50": {
        "data_table": table(["Practice", "Reason"], [
            ["Checking the baseline", "A percentage increase means little without the original number"],
        ]),
    },
    "critical-thinking-c1-l51": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Appeal to authority", "Assuming a claim is true because an authority figure said so"],
        ]),
    },
    "critical-thinking-c1-l52": {
        "data_table": table(["Technique", "Purpose"], [
            ["Brainstorming", "Generates many ideas quickly before evaluating them"],
        ]),
    },
    "critical-thinking-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Dunning-Kruger effect", "People with low ability at a task tend to overestimate their competence"],
        ]),
    },
    "critical-thinking-c1-l54": {
        "data_table": table(["Step", "Purpose"], [
            ["Estimating likelihood and impact", "Prioritizes which risks deserve the most attention"],
        ]),
    },
    "critical-thinking-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Explanation", "Describes why something happened"], ["Justification", "Argues why a belief or action is warranted"],
        ]),
    },
    "critical-thinking-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Groupthink", "A group's desire for harmony leads to poor collective decisions"],
        ]),
    },
    "critical-thinking-c1-l57": {
        "data_table": table(["Pitfall", "Example"], [
            ["Truncated axis", "A bar chart that exaggerates small differences by not starting at zero"],
        ]),
    },
    "critical-thinking-c1-l58": {
        "data_table": table(["Step", "Purpose"], [
            ["Testing a hypothesis", "Determines whether evidence supports or refutes a claim"],
        ]),
    },
    "critical-thinking-c1-l59": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Red herring", "Introducing an irrelevant point to distract from the argument"],
        ]),
    },
    "critical-thinking-c1-l60": {
        "data_table": table(["Term", "Meaning"], [
            ["Metacognition", "Thinking about and evaluating one's own thought processes"],
        ]),
    },
    "critical-thinking-c1-l61": {
        "data_table": table(["Connective", "Truth Condition"], [
            ["NOT", "Reverses the truth value of a statement"], ["XOR", "True only when exactly one input is true"],
        ]),
    },
    "critical-thinking-c1-l62": {
        "data_table": table(["Condition", "Example"], [
            ["Necessary but not sufficient", "Having wheels is necessary but not sufficient for being a car"],
        ]),
    },
    "critical-thinking-c1-l63": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Actively seeking disconfirming evidence", "Directly counters confirmation bias"],
        ]),
    },
    "critical-thinking-c1-l64": {
        "data_table": table(["Case", "Verdict"], [
            ["Argument A", "Valid but unsound (false premise)"], ["Argument B", "Valid and sound"],
        ]),
    },
    "critical-thinking-c1-l65": {
        "data_table": table(["Case", "Fallacy Identified"], [
            ["Political ad", "Ad hominem attack on the opposing candidate"],
        ]),
    },
    "critical-thinking-c1-l66": {
        "data_table": table(["Case", "Bias Identified"], [
            ["Investment decision", "Anchoring on the original purchase price"],
        ]),
    },
    "critical-thinking-c1-l67": {
        "data_table": table(["Case", "Analysis"], [
            ["Ice cream and drowning example", "A third variable (summer heat) explains both trends"],
        ]),
    },
    "critical-thinking-c1-l68": {
        "data_table": table(["Case", "Analysis"], [
            ["Misleading survey", "Small, non-representative sample undermines the claimed result"],
        ]),
    },
    "critical-thinking-c1-l69": {
        "data_table": table(["Case", "Analysis"], [
            ["Flawed experiment", "Missing control group weakens the causal conclusion"],
        ]),
    },
    "critical-thinking-c1-l70": {
        "data_table": table(["Case", "Analysis"], [
            ["Comparing two sources", "One cites primary data, the other an unverified blog"],
        ]),
    },
    "critical-thinking-c1-l71": {
        "data_table": table(["Case", "Analysis"], [
            ["Viral headline", "Sensational wording misrepresents the underlying study"],
        ]),
    },
    "critical-thinking-c1-l72": {
        "data_table": table(["Case", "Analysis"], [
            ["Policy debate", "Mapping shows an unsupported claim with no linked evidence"],
        ]),
    },
    "critical-thinking-c1-l73": {
        "data_table": table(["Case", "Analysis"], [
            ["Business decision", "Expected value calculation favors the higher-probability option"],
        ]),
    },
    "critical-thinking-c1-l74": {
        "data_table": table(["Case", "Analysis"], [
            ["Ethical dilemma", "Consequentialist and deontological analyses reach different verdicts"],
        ]),
    },
    "critical-thinking-c1-l75": {
        "data_table": table(["Case", "Analysis"], [
            ["Court case", "Precedent-based reasoning applied to a novel fact pattern"],
        ]),
    },
    "critical-thinking-c1-l76": {
        "data_table": table(["Case", "Analysis"], [
            ["Traffic congestion", "A systems view reveals feedback loops standard fixes ignore"],
        ]),
    },
    "critical-thinking-c1-l77": {
        "data_table": table(["Case", "Analysis"], [
            ["General claim", "A single counterexample disproves an unqualified universal claim"],
        ]),
    },
    "critical-thinking-c1-l78": {
        "data_table": table(["Case", "Analysis"], [
            ["Insurance decision", "Weighing low-probability, high-impact risk against premium cost"],
        ]),
    },
    "critical-thinking-c1-l79": {
        "data_table": table(["Case", "Analysis"], [
            ["Structured debate", "Each side responds directly to the opponent's strongest point"],
        ]),
    },
    "critical-thinking-c1-l80": {
        "data_table": table(["Case", "Analysis"], [
            ["Self-review", "Identifying where initial confidence exceeded actual accuracy"],
        ]),
    },
    "critical-thinking-c1-l81": {
        "data_table": table(["Step", "Focus"], [
            ["Gathering evidence", "Distinguishing primary sources from secondary commentary"],
        ]),
    },
    "critical-thinking-c1-l82": {
        "data_table": table(["Step", "Focus"], [
            ["Constructing a deductive proof", "Ensuring each step follows necessarily from the last"],
        ]),
    },
    "critical-thinking-c1-l83": {
        "data_table": table(["Step", "Focus"], [
            ["Generalizing from data", "Assessing whether the sample supports the broader claim"],
        ]),
    },
    "critical-thinking-c1-l84": {
        "data_table": table(["Step", "Focus"], [
            ["Testing an argument's soundness", "Verifying both validity and the truth of each premise"],
        ]),
    },
    "critical-thinking-c1-l85": {
        "data_table": table(["Step", "Focus"], [
            ["Auditing a real editorial", "Flagging informal fallacies used to persuade"],
        ]),
    },
    "critical-thinking-c1-l86": {
        "data_table": table(["Step", "Focus"], [
            ["Reviewing a personal decision", "Identifying which cognitive bias may have influenced it"],
        ]),
    },
    "critical-thinking-c1-l87": {
        "data_table": table(["Step", "Focus"], [
            ["Designing a controlled study", "Isolating a single variable to test a causal claim"],
        ]),
    },
    "critical-thinking-c1-l88": {
        "data_table": table(["Step", "Focus"], [
            ["Fact-checking a statistic", "Tracing a cited number back to its original source"],
        ]),
    },
    "critical-thinking-c1-l89": {
        "data_table": table(["Step", "Focus"], [
            ["Applying the scientific method", "Structuring a testable question and hypothesis"],
        ]),
    },
    "critical-thinking-c1-l90": {
        "data_table": table(["Step", "Focus"], [
            ["Rating source credibility", "Scoring a source against expertise and bias criteria"],
        ]),
    },
    "critical-thinking-c1-l91": {
        "data_table": table(["Step", "Focus"], [
            ["Comparing two news outlets", "Identifying framing differences on the same event"],
        ]),
    },
    "critical-thinking-c1-l92": {
        "data_table": table(["Step", "Focus"], [
            ["Building an argument map", "Diagramming a real op-ed's claims and support"],
        ]),
    },
    "critical-thinking-c1-l93": {
        "data_table": table(["Step", "Focus"], [
            ["Applying expected value", "Choosing between options with different probability and payoff"],
        ]),
    },
    "critical-thinking-c1-l94": {
        "data_table": table(["Step", "Focus"], [
            ["Analyzing a real dilemma", "Applying an ethical framework to a current events case"],
        ]),
    },
    "critical-thinking-c1-l95": {
        "data_table": table(["Step", "Focus"], [
            ["Reading a case brief", "Identifying the legal reasoning behind a court's ruling"],
        ]),
    },
    "critical-thinking-c1-l96": {
        "data_table": table(["Step", "Focus"], [
            ["Mapping a system", "Identifying feedback loops in a real-world process"],
        ]),
    },
    "critical-thinking-c1-l97": {
        "data_table": table(["Step", "Focus"], [
            ["Testing a claim's limits", "Searching actively for a disconfirming case"],
        ]),
    },
    "critical-thinking-c1-l98": {
        "data_table": table(["Step", "Focus"], [
            ["Assessing a real risk", "Estimating probability and consequence for a practical decision"],
        ]),
    },
    "critical-thinking-c1-l99": {
        "data_table": table(["Step", "Focus"], [
            ["Running a mock debate", "Practicing structured rebuttal and evidence use"],
        ]),
    },
    "critical-thinking-c1-l100": {
        "data_table": table(["Step", "Focus"], [
            ["Writing a reflection", "Evaluating one's own reasoning process after a decision"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Critical Thinking: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Critical Thinking lessons (completing 100/100).")


if __name__ == "__main__":
    main()
