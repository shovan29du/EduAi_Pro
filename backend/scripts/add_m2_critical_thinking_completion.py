#!/usr/bin/env python3
"""Depth pass, M2 Critical Thinking: fill in real, hand-checked
data_table content for the M2 Critical Thinking lessons not covered by
the earlier breadth-first batch. Brings M2 Critical Thinking to full
120/120 coverage.

Structure differs from most M2 subjects: l1-l100 are unique doctoral-
level topics spanning formal/informal logic, argumentation theory,
epistemology, decision theory, and philosophy of science; l101-l120
are "Independent Capstone" lessons on 20 foundational critical-
thinking topics (Claims and Evidence, Deductive Reasoning, ... through
Metacognition) that are NOT reuses of l1-l20 content -- their titles
and content are distinct introductory topics, so all 120 lessons get
individually authored data_table entries. l3 was already completed by
an earlier breadth-first batch, so it is left untouched here.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_critical_thinking_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "critical-thinking-m2-l1": {"data_table": table(["Concept", "Key Point"], [
        ["Applied decision analysis", "Structures a choice into options, states of the world, probabilities, and payoffs to compute expected value"],
        ["Graduate research posture", "Treats every claim in the literature as provisionally justified, revisable under new evidence"],
    ])},
    "critical-thinking-m2-l2": {"data_table": table(["Concept", "Key Point"], [
        ["Argument structure", "Premises offer support for a conclusion; structure is displayed via standard form or argument diagrams"],
        ["Logic vs. rhetoric", "Logic evaluates whether premises support a conclusion; rhetoric studies how arguments persuade"],
    ])},
    "critical-thinking-m2-l4": {"data_table": table(["Concept", "Key Point"], [
        ["Pragma-dialectics", "Models argumentation as a critical discussion aimed at resolving a difference of opinion"],
        ["Ten discussion rules", "Van Eemeren & Grootendorst's rules bar moves such as unfalsifiable standpoints or irrelevant argumentation"],
    ])},
    "critical-thinking-m2-l5": {"data_table": table(["Concept", "Key Point"], [
        ["Formal dialectic", "Treats argument as a regulated dialogue game between a proponent and opponent with explicit commitment stores"],
        ["Commitment-based semantics", "A move's rationality is judged by consistency with a speaker's prior public commitments, not private belief"],
    ])},
    "critical-thinking-m2-l6": {"data_table": table(["Concept", "Key Point"], [
        ["Dung's abstract argumentation framework", "Represents arguments as nodes and attacks as directed edges, independent of internal content"],
        ["Extensions", "Grounded, preferred, and stable extensions define which argument sets can be jointly accepted"],
    ])},
    "critical-thinking-m2-l7": {"data_table": table(["Concept", "Key Point"], [
        ["Argumentation scheme", "A stereotypical pattern of defeasible reasoning, e.g. argument from expert opinion"],
        ["Critical questions", "Each scheme pairs with standard questions that, if unanswered, defeat the argument's presumptive force"],
    ])},
    "critical-thinking-m2-l8": {"data_table": table(["Concept", "Key Point"], [
        ["Bayesian argumentation", "Models argument strength as the degree to which evidence shifts a rational agent's credence via Bayes' theorem"],
        ["Degree of belief", "Represented as a subjective probability, updated by conditionalization as new evidence arrives"],
    ])},
    "critical-thinking-m2-l9": {"data_table": table(["Concept", "Key Point"], [
        ["Probabilistic epistemology", "Analyzes justified belief in terms of credences that satisfy the probability axioms"],
        ["Rational credence", "A credence is rational when it is coherent (obeys probability axioms) and responsive to evidence"],
    ])},
    "critical-thinking-m2-l10": {"data_table": table(["Concept", "Key Point"], [
        ["Epistemic circularity", "Occurs when a source of justification (e.g. perception) is used to justify trust in that same source"],
        ["Bootstrapping problem", "Track-record arguments for a faculty's reliability presuppose the faculty's outputs are already trustworthy"],
    ])},
    "critical-thinking-m2-l11": {"data_table": table(["Concept", "Key Point"], [
        ["Externalism", "Justification depends on factors outside the believer's awareness, e.g. reliable belief-forming processes"],
        ["Internalism", "Justification requires that the grounds for a belief be accessible to the believer's own reflection"],
    ])},
    "critical-thinking-m2-l12": {"data_table": table(["Concept", "Key Point"], [
        ["Reliabilism", "A belief is justified if produced by a process that reliably yields true beliefs"],
        ["Generality problem", "Every process token instantiates many process types with different reliability rates, and no principled way selects the relevant type"],
    ])},
    "critical-thinking-m2-l13": {"data_table": table(["Concept", "Key Point"], [
        ["Virtue epistemology", "Locates justification in stable intellectual character traits such as open-mindedness and intellectual courage"],
        ["Intellectual character", "Treats knowing as an achievement creditable to the agent's cognitive virtues, not just a lucky true belief"],
    ])},
    "critical-thinking-m2-l14": {"data_table": table(["Concept", "Key Point"], [
        ["Social epistemology", "Studies how social practices and institutions shape the production and distribution of knowledge"],
        ["Epistemology of testimony", "Asks whether believing on the word of others is a basic, reduction-proof source of justification"],
    ])},
    "critical-thinking-m2-l15": {"data_table": table(["Concept", "Key Point"], [
        ["Testimonial injustice", "A speaker's credibility is unfairly deflated due to prejudice about their social identity"],
        ["Hermeneutical injustice", "A gap in shared interpretive resources leaves someone unable to make sense of their own experience"],
    ])},
    "critical-thinking-m2-l16": {"data_table": table(["Concept", "Key Point"], [
        ["Groupthink", "Cohesive groups suppress dissent and critical evaluation to preserve consensus and morale"],
        ["Deliberation failure", "Symptoms include illusion of unanimity, self-censorship, and pressure on dissenters to conform"],
    ])},
    "critical-thinking-m2-l17": {"data_table": table(["Concept", "Key Point"], [
        ["Deliberative democracy", "Legitimacy of collective decisions rests on reasoned public exchange among free and equal citizens"],
        ["Rational consensus", "An idealized endpoint reached through argument alone, not bargaining or the exercise of power"],
    ])},
    "critical-thinking-m2-l18": {"data_table": table(["Concept", "Key Point"], [
        ["Ethics of belief", "Asks whether believing without sufficient evidence is itself morally blameworthy (Clifford's principle)"],
        ["Doxastic responsibility", "Holds agents accountable for the diligence with which they form and revise their beliefs"],
    ])},
    "critical-thinking-m2-l19": {"data_table": table(["Concept", "Key Point"], [
        ["Formal fallacy theory", "Analyzes invalid inference patterns (e.g. affirming the consequent) at the level of logical form"],
        ["Meta-level analysis", "Studies the theoretical adequacy of fallacy taxonomies themselves, not just individual fallacious arguments"],
    ])},
    "critical-thinking-m2-l20": {"data_table": table(["Concept", "Key Point"], [
        ["Relevance logic", "Requires premises to be logically relevant to the conclusion, blocking irrelevance-based paradoxes"],
        ["Rejection of explosion", "Denies ex falso quodlibet (from a contradiction, anything follows), which classical logic validates"],
    ])},
    "critical-thinking-m2-l21": {"data_table": table(["Concept", "Key Point"], [
        ["Paraconsistent logic", "Tolerates contradictions in a theory without the theory collapsing into triviality"],
        ["Contradiction tolerance", "Enables reasoning about inconsistent but non-trivial information sources, e.g. conflicting databases"],
    ])},
    "critical-thinking-m2-l22": {"data_table": table(["Concept", "Key Point"], [
        ["Dialetheism", "The view that some contradictions (dialetheias) are literally true, e.g. certain self-referential paradoxes"],
        ["True contradictions", "Graham Priest cites the Liar sentence as a candidate: it is both true and false under its own semantics"],
    ])},
    "critical-thinking-m2-l23": {"data_table": table(["Concept", "Key Point"], [
        ["Many-valued logic", "Admits truth values beyond true/false, e.g. a third 'indeterminate' value"],
        ["Bivalence", "Classical logic's assumption that every proposition is exactly true or false; many-valued logics reject it"],
    ])},
    "critical-thinking-m2-l24": {"data_table": table(["Concept", "Key Point"], [
        ["Intuitionistic logic", "Rejects the law of excluded middle; truth is identified with constructive provability"],
        ["Constructive proof", "Proving existence requires exhibiting a witness, not merely deriving a contradiction from non-existence"],
    ])},
    "critical-thinking-m2-l25": {"data_table": table(["Concept", "Key Point"], [
        ["Substructural logic", "Restricts structural rules of classical logic such as weakening or contraction"],
        ["Resource-sensitive reasoning", "Linear logic treats premises as consumable resources, tracking how many times each is used"],
    ])},
    "critical-thinking-m2-l26": {"data_table": table(["Concept", "Key Point"], [
        ["Default logic", "Allows conclusions to be drawn by default rules unless a specific exception blocks them"],
        ["Circumscription", "Minimizes the extension of predicates to formalize the assumption that only explicitly stated exceptions exist"],
    ])},
    "critical-thinking-m2-l27": {"data_table": table(["Concept", "Key Point"], [
        ["Belief revision", "Studies how a rational agent updates a belief set when new, possibly conflicting, information arrives"],
        ["AGM framework", "Alchourron-Gardenfors-Makinson postulates govern rational contraction, expansion, and revision of belief sets"],
    ])},
    "critical-thinking-m2-l28": {"data_table": table(["Concept", "Key Point"], [
        ["Truth maintenance system", "An automated reasoning component that tracks justifications for beliefs and retracts dependents when a premise is retracted"],
        ["Dependency-directed backtracking", "Efficiently identifies which conclusions must be revised after a contradiction is detected"],
    ])},
    "critical-thinking-m2-l29": {"data_table": table(["Concept", "Key Point"], [
        ["Argument mining", "NLP techniques that automatically identify argumentative components (claims, premises) in free text"],
        ["Pipeline stages", "Typically: argument component detection, boundary identification, then relation classification"],
    ])},
    "critical-thinking-m2-l30": {"data_table": table(["Concept", "Key Point"], [
        ["Computational persuasion", "Models how an automated system selects arguments to maximize a target audience's belief change"],
        ["User modeling", "Effective persuasion systems represent audience values and prior beliefs to tailor argument selection"],
    ])},
    "critical-thinking-m2-l31": {"data_table": table(["Concept", "Key Point"], [
        ["Rhetorical Structure Theory", "Analyzes text coherence via nucleus-satellite relations such as elaboration, contrast, and justification"],
        ["Discourse coherence", "A text is coherent when its parts are connected by recognizable rhetorical relations, not just grammatically correct"],
    ])},
    "critical-thinking-m2-l32": {"data_table": table(["Concept", "Key Point"], [
        ["Rationality of emotion", "Emotions can track normatively relevant features of a situation, functioning as fast evaluative judgments"],
        ["Emotional argumentation", "Appeals to emotion are fallacious only when the emotion is irrelevant to, or displaces, the evidential merits"],
    ])},
    "critical-thinking-m2-l33": {"data_table": table(["Concept", "Key Point"], [
        ["Motivated reasoning", "Directional goals bias the search for and evaluation of evidence toward a desired conclusion"],
        ["Identity-protective cognition", "People process politically charged evidence in ways that protect their group identity, even at the cost of accuracy"],
    ])},
    "critical-thinking-m2-l34": {"data_table": table(["Concept", "Key Point"], [
        ["Metacognition", "Awareness and regulation of one's own cognitive processes, including monitoring the quality of one's reasoning"],
        ["Confidence calibration", "Well-calibrated confidence matches stated probability to actual long-run accuracy across many judgments"],
    ])},
    "critical-thinking-m2-l35": {"data_table": table(["Concept", "Key Point"], [
        ["Dunning-Kruger effect", "Low performers are said to overestimate their ability due to the same skill deficit that causes poor performance"],
        ["Statistical critique", "Regression to the mean and noisy self-assessment measures can reproduce the pattern even without a true metacognitive deficit"],
    ])},
    "critical-thinking-m2-l36": {"data_table": table(["Concept", "Key Point"], [
        ["Heuristics-and-biases program", "Kahneman and Tversky's research documenting systematic deviations from normative rational choice models"],
        ["Replication debate", "Some classic bias findings (e.g. certain framing effects) show smaller or inconsistent effect sizes in large replications"],
    ])},
    "critical-thinking-m2-l37": {"data_table": table(["Concept", "Key Point"], [
        ["Ecological rationality", "Judges heuristics by their fit to the structure of real environments, not by conformity to abstract logical norms"],
        ["Fast-and-frugal heuristics", "Simple rules like 'take the best' can outperform complex models when information is scarce (Gigerenzer)"],
    ])},
    "critical-thinking-m2-l38": {"data_table": table(["Concept", "Key Point"], [
        ["Naturalistic decision making", "Studies how experts (firefighters, pilots) make rapid decisions under real time pressure and uncertainty"],
        ["Recognition-primed decision model", "Experts recognize a situation as typical and mentally simulate a single plausible course of action rather than comparing options"],
    ])},
    "critical-thinking-m2-l39": {"data_table": table(["Concept", "Key Point"], [
        ["Ambiguity aversion", "Decision makers prefer known-probability risks over equally-valued but ambiguous-probability options"],
        ["Ellsberg paradox", "Choices between colored-ball urns violate expected utility theory's independence axiom when ambiguity is introduced"],
    ])},
    "critical-thinking-m2-l40": {"data_table": table(["Concept", "Key Point"], [
        ["Newcomb's problem", "A predictor's near-perfect forecast creates a conflict between dominance reasoning and expected-value reasoning"],
        ["Causal decision theory", "Recommends the action with the best causal consequences, resolving Newcomb's problem by two-boxing"],
    ])},
    "critical-thinking-m2-l41": {"data_table": table(["Concept", "Key Point"], [
        ["Evidential decision theory", "Recommends the action that is the best news about the outcome, conditioning on the act itself"],
        ["Causal vs. evidential divergence", "The two theories disagree exactly when an act is correlated with, but does not cause, a good outcome"],
    ])},
    "critical-thinking-m2-l42": {"data_table": table(["Concept", "Key Point"], [
        ["Sure-thing principle", "If an act is preferred under every possible state of the world, it should be preferred overall"],
        ["Violations", "Allais-style experiments show real choices sometimes violate the principle under compound or framed lotteries"],
    ])},
    "critical-thinking-m2-l43": {"data_table": table(["Concept", "Key Point"], [
        ["Social choice theory", "Studies how individual preferences can be aggregated into a single collective ranking"],
        ["Arrow's impossibility theorem", "No ranked voting rule with 3+ options can simultaneously satisfy Pareto efficiency, independence of irrelevant alternatives, non-dictatorship, and unrestricted domain"],
    ])},
    "critical-thinking-m2-l44": {"data_table": table(["Concept", "Key Point"], [
        ["Judgment aggregation", "Generalizes social choice to aggregating logically connected propositional judgments, not just preference orders"],
        ["Discursive dilemma", "Premise-wise and conclusion-wise majority voting on connected propositions can yield inconsistent collective verdicts"],
    ])},
    "critical-thinking-m2-l45": {"data_table": table(["Concept", "Key Point"], [
        ["Condorcet's jury theorem", "If each voter is more likely right than wrong and votes independently, majority accuracy approaches certainty as group size grows"],
        ["Collective accuracy", "The theorem's guarantees fail if voter competence is below 50% or votes are correlated"],
    ])},
    "critical-thinking-m2-l46": {"data_table": table(["Concept", "Key Point"], [
        ["Wisdom of crowds", "Aggregated independent estimates can outperform most individual experts under the right conditions"],
        ["Conditions and limits", "Requires diversity, independence, and decentralization; social influence that induces correlated errors undermines the effect"],
    ])},
    "critical-thinking-m2-l47": {"data_table": table(["Concept", "Key Point"], [
        ["Adversarial collaboration", "Opposing researchers jointly pre-register a study design so that the result cannot be attributed to bias"],
        ["Scientific disputes", "Used to resolve long-running empirical disagreements where each side previously produced favorable but incompatible studies"],
    ])},
    "critical-thinking-m2-l48": {"data_table": table(["Concept", "Key Point"], [
        ["Preregistration", "Committing to hypotheses, methods, and analysis plans before data collection to prevent post hoc rationalization"],
        ["Replication crisis", "A substantial share of published findings, especially in psychology, fail to replicate at comparable effect sizes"],
    ])},
    "critical-thinking-m2-l49": {"data_table": table(["Concept", "Key Point"], [
        ["Questionable research practices", "Undisclosed flexibility such as optional stopping, selective outcome reporting, or dropping conditions"],
        ["p-hacking", "Exploiting analytic flexibility until a result crosses a conventional significance threshold, inflating false-positive rates"],
    ])},
    "critical-thinking-m2-l50": {"data_table": table(["Concept", "Key Point"], [
        ["Meta-analysis", "Statistically pools effect sizes across studies to produce a more precise combined estimate"],
        ["Publication bias", "Significant, positive findings are more likely to be published, systematically inflating pooled effect estimates unless corrected"],
    ])},
    "critical-thinking-m2-l51": {"data_table": table(["Concept", "Key Point"], [
        ["Demarcation problem", "Asks what distinguishes science from non-science or pseudoscience"],
        ["Post-Popperian views", "Move beyond simple falsifiability, e.g. Lakatos's progressive vs. degenerating research programmes"],
    ])},
    "critical-thinking-m2-l52": {"data_table": table(["Concept", "Key Point"], [
        ["Paradigm shift", "Kuhn's account of scientific revolutions as discontinuous replacements of a field's governing framework"],
        ["Incommensurability", "Successive paradigms may lack a shared standard for direct comparison, complicating claims of cumulative progress"],
    ])},
    "critical-thinking-m2-l53": {"data_table": table(["Concept", "Key Point"], [
        ["Research programme", "Lakatos's unit of appraisal: a hard core of assumptions protected by a revisable protective belt of auxiliary hypotheses"],
        ["Progress criteria", "A programme is progressive if it predicts novel facts, degenerating if it only accommodates anomalies after the fact"],
    ])},
    "critical-thinking-m2-l54": {"data_table": table(["Concept", "Key Point"], [
        ["Epistemological anarchism", "Feyerabend's claim that no single fixed scientific method has produced all genuine progress"],
        ["'Anything goes'", "A provocative slogan urging methodological pluralism against rigid rules that historically constrained inquiry"],
    ])},
    "critical-thinking-m2-l55": {"data_table": table(["Concept", "Key Point"], [
        ["Underdetermination", "Available evidence is compatible with more than one theory, so evidence alone cannot uniquely select a theory"],
        ["Duhem-Quine thesis", "Theories are tested only in conjunction with auxiliary assumptions, so a failed prediction never uniquely falsifies one hypothesis"],
    ])},
    "critical-thinking-m2-l56": {"data_table": table(["Concept", "Key Point"], [
        ["Inference to the best explanation", "Infers the hypothesis that would, if true, provide the best explanation of the evidence"],
        ["Formal models", "Bayesian reconstructions treat explanatory considerations (simplicity, scope) as evidence that shifts priors"],
    ])},
    "critical-thinking-m2-l57": {"data_table": table(["Concept", "Key Point"], [
        ["Abductive reasoning", "Generates a plausible explanatory hypothesis from an observed anomaly, distinct from deduction and induction"],
        ["Diagnostic contexts", "Medical diagnosis is a paradigm case: clinicians abduce the disease that best explains the presenting symptoms"],
    ])},
    "critical-thinking-m2-l58": {"data_table": table(["Concept", "Key Point"], [
        ["Causal graphical model", "Represents causal relationships among variables as a directed acyclic graph"],
        ["Do-calculus", "Pearl's rules for computing the effect of an intervention (do-operator) from observational data and the graph structure"],
    ])},
    "critical-thinking-m2-l59": {"data_table": table(["Concept", "Key Point"], [
        ["Counterfactual reasoning", "Evaluates what would have happened under conditions that did not actually occur"],
        ["Structural causal models", "Formalize counterfactuals via structural equations that can be manipulated to simulate alternative worlds"],
    ])},
    "critical-thinking-m2-l60": {"data_table": table(["Concept", "Key Point"], [
        ["Simpson's paradox", "A trend present in aggregated data reverses or disappears when the data are split by a confounding subgroup"],
        ["Causal confounding", "Resolving the paradox requires a causal model to determine which stratification level answers the intended question"],
    ])},
    "critical-thinking-m2-l61": {"data_table": table(["Concept", "Key Point"], [
        ["Instrumental variable", "A variable that affects the outcome only through its effect on the treatment, enabling causal identification amid confounding"],
        ["Causal identification", "IV methods estimate causal effects without requiring all confounders to be measured, given valid exclusion restrictions"],
    ])},
    "critical-thinking-m2-l62": {"data_table": table(["Concept", "Key Point"], [
        ["Mediation analysis", "Decomposes a total causal effect into direct and indirect (mediated) pathways"],
        ["Causal pathway", "Identifying mediators requires assumptions beyond those needed for total-effect estimation, since mediators can be confounded too"],
    ])},
    "critical-thinking-m2-l63": {"data_table": table(["Concept", "Key Point"], [
        ["Frame problem", "The challenge of formally specifying which facts remain unchanged after an action, without enumerating every non-effect"],
        ["AI relevance", "Central to classical planning: naive representations require an explosion of axioms stating what an action does not affect"],
    ])},
    "critical-thinking-m2-l64": {"data_table": table(["Concept", "Key Point"], [
        ["Dual-process theory", "Posits a fast, automatic System 1 and a slow, deliberate System 2 underlying judgment and reasoning"],
        ["Contemporary critique", "Some theorists argue the two-system dichotomy oversimplifies a more continuous or context-dependent set of processes"],
    ])},
    "critical-thinking-m2-l65": {"data_table": table(["Concept", "Key Point"], [
        ["Implicit bias", "Automatic, often unconscious associations that can influence judgment and behavior without deliberate endorsement"],
        ["Automatic processing", "Operates rapidly and outside conscious control, distinguishing it from deliberate, endorsed attitudes"],
    ])},
    "critical-thinking-m2-l66": {"data_table": table(["Concept", "Key Point"], [
        ["Debiasing intervention", "Techniques (e.g. consider-the-opposite, checklists) intended to reduce the influence of a known cognitive bias"],
        ["Efficacy and limits", "Many debiasing effects are modest and domain-specific; durable transfer to novel judgment tasks is often limited"],
    ])},
    "critical-thinking-m2-l67": {"data_table": table(["Concept", "Key Point"], [
        ["Forecasting accuracy", "Measured via calibration (do stated probabilities match outcome frequencies) and resolution (distinguishing events from non-events)"],
        ["Superforecasters", "A small subset of forecasters in Tetlock's Good Judgment Project consistently outperformed peers and domain experts"],
    ])},
    "critical-thinking-m2-l68": {"data_table": table(["Concept", "Key Point"], [
        ["Calibration training", "Structured feedback exercises that align stated confidence levels with actual accuracy over many judgments"],
        ["Probabilistic judgment", "Trained forecasters learn to express beliefs as graded probabilities rather than binary predictions"],
    ])},
    "critical-thinking-m2-l69": {"data_table": table(["Concept", "Key Point"], [
        ["Red teaming", "A designated team argues against a plan or conclusion to expose weaknesses before commitment"],
        ["Structured analytic techniques", "Formal procedures (e.g. key assumptions check) used in intelligence analysis to counteract cognitive bias"],
    ])},
    "critical-thinking-m2-l70": {"data_table": table(["Concept", "Key Point"], [
        ["Analysis of competing hypotheses", "Evaluates evidence against multiple hypotheses simultaneously rather than confirming a single favored one"],
        ["Diagnosticity", "Prioritizes evidence that discriminates between hypotheses over evidence merely consistent with all of them"],
    ])},
    "critical-thinking-m2-l71": {"data_table": table(["Concept", "Key Point"], [
        ["Cognitive trap", "Recurring reasoning failures in intelligence analysis, e.g. mirror-imaging or premature closure"],
        ["Intelligence analysis", "High-stakes, time-pressured judgment under uncertainty is especially vulnerable to confirmation-driven traps"],
    ])},
    "critical-thinking-m2-l72": {"data_table": table(["Concept", "Key Point"], [
        ["Scenario planning", "Constructs multiple plausible future narratives to stress-test strategy against uncertainty, rather than predicting one future"],
        ["Strategic foresight", "Aims to widen decision-makers' perceived range of possibilities rather than to forecast a single outcome"],
    ])},
    "critical-thinking-m2-l73": {"data_table": table(["Concept", "Key Point"], [
        ["Delphi method", "Iteratively collects and shares anonymous expert estimates across rounds, converging toward a group judgment"],
        ["Expert elicitation", "Anonymity and controlled feedback reduce dominance and conformity effects seen in face-to-face panels"],
    ])},
    "critical-thinking-m2-l74": {"data_table": table(["Concept", "Key Point"], [
        ["Wicked problem", "A problem with no definitive formulation, contested criteria for a solution, and no stopping rule"],
        ["Ill-structured domain", "Unlike well-structured puzzles, wicked problems resist decomposition into cleanly solvable sub-problems"],
    ])},
    "critical-thinking-m2-l75": {"data_table": table(["Concept", "Key Point"], [
        ["Systems thinking", "Analyzes a problem in terms of interacting components and feedback rather than isolated linear causes"],
        ["Feedback loop", "Reinforcing loops amplify change; balancing loops resist it and drive a system toward equilibrium"],
    ])},
    "critical-thinking-m2-l76": {"data_table": table(["Concept", "Key Point"], [
        ["Root cause analysis", "Traces an observed failure back through contributing factors to the underlying systemic cause"],
        ["Five whys", "A simple iterative technique that repeatedly asks 'why' to move from a symptom to its root cause"],
    ])},
    "critical-thinking-m2-l77": {"data_table": table(["Concept", "Key Point"], [
        ["Legal argumentation", "Reasons from prior case outcomes (precedent) and structural similarity (analogy) to justify a present ruling"],
        ["Precedent and analogy", "Stare decisis binds courts to relevantly similar past rulings, with analogical reasoning determining relevant similarity"],
    ])},
    "critical-thinking-m2-l78": {"data_table": table(["Concept", "Key Point"], [
        ["Defeasible reasoning", "Conclusions hold provisionally and can be overturned by new facts, unlike strict deductive entailment"],
        ["Case-based legal argument", "New cases are decided by retrieving and adapting the most relevantly similar precedent, subject to distinguishing facts"],
    ])},
    "critical-thinking-m2-l79": {"data_table": table(["Concept", "Key Point"], [
        ["Rhetoric of science", "Studies how scientific writing itself uses persuasive strategies (framing, metaphor) beyond pure logical demonstration"],
        ["Persuasion in research", "Even peer-reviewed papers deploy rhetorical choices to make findings appear more compelling or certain"],
    ])},
    "critical-thinking-m2-l80": {"data_table": table(["Concept", "Key Point"], [
        ["Critical discourse analysis", "Examines how language use encodes and reproduces social power relations"],
        ["Power in argument", "Analyzes whose voices and framings are privileged in a discourse, beyond the surface validity of individual arguments"],
    ])},
    "critical-thinking-m2-l81": {"data_table": table(["Concept", "Key Point"], [
        ["Epistemic bubble", "An information environment where contrary views are merely absent, not actively distrusted"],
        ["Echo chamber", "An environment where members are trained to actively discredit outside sources, insulating beliefs from correction"],
    ])},
    "critical-thinking-m2-l82": {"data_table": table(["Concept", "Key Point"], [
        ["Misinformation vs. disinformation", "Misinformation is false but not necessarily intentionally spread; disinformation is deliberately deceptive"],
        ["Epistemic vice", "Character traits like closed-mindedness or intellectual laziness that systematically obstruct the acquisition of knowledge"],
    ])},
    "critical-thinking-m2-l83": {"data_table": table(["Concept", "Key Point"], [
        ["Inoculation theory", "Pre-exposing people to a weakened version of a misleading argument builds resistance to the full version later"],
        ["Prebunking", "Applies inoculation before exposure to misinformation, contrasted with after-the-fact fact-checking (debunking)"],
    ])},
    "critical-thinking-m2-l84": {"data_table": table(["Concept", "Key Point"], [
        ["Fact-checking methodology", "Systematically verifies specific factual claims against primary sources and documented evidence"],
        ["Source triangulation", "Corroborates a claim across multiple independent sources to reduce reliance on any single, possibly biased, source"],
    ])},
    "critical-thinking-m2-l85": {"data_table": table(["Concept", "Key Point"], [
        ["Genetic fallacy", "Dismissing or endorsing a claim based on its origin rather than its current evidential merits"],
        ["Historical argument", "Especially tempting in historical debate, where a claim's ideological origin is conflated with its truth value"],
    ])},
    "critical-thinking-m2-l86": {"data_table": table(["Concept", "Key Point"], [
        ["Frequentist inference", "Defines probability as long-run relative frequency; evaluates procedures by their error rates over repeated sampling"],
        ["Bayesian inference", "Defines probability as degree of belief; updates a prior distribution into a posterior via the likelihood of observed data"],
    ])},
    "critical-thinking-m2-l87": {"data_table": table(["Concept", "Key Point"], [
        ["Likelihoodism", "Evidential support for a hypothesis is measured by the likelihood ratio between competing hypotheses, without priors or error rates"],
        ["Law of likelihood", "Evidence favors whichever hypothesis assigns the observed data the higher probability"],
    ])},
    "critical-thinking-m2-l88": {"data_table": table(["Concept", "Key Point"], [
        ["Model selection", "Chooses among competing statistical models by balancing goodness of fit against complexity"],
        ["Formalized Occam's razor", "Criteria like AIC and BIC penalize additional parameters, formalizing a preference for simpler models"],
    ])},
    "critical-thinking-m2-l89": {"data_table": table(["Concept", "Key Point"], [
        ["Problem of induction", "Hume's challenge: no non-circular justification exists for assuming the future will resemble the past"],
        ["Contemporary responses", "Include Bayesian reframings, reliabilist defenses, and pragmatic vindications of inductive practice"],
    ])},
    "critical-thinking-m2-l90": {"data_table": table(["Concept", "Key Point"], [
        ["Reflective equilibrium", "A state reached by mutually adjusting general principles and particular judgments until they cohere"],
        ["Moral and logical reasoning", "Applied both to ethical theorizing (Rawls) and to justifying which logical inference rules to accept"],
    ])},
    "critical-thinking-m2-l91": {"data_table": table(["Concept", "Key Point"], [
        ["Coherentism", "A belief is justified by fitting coherently within a web of mutually supporting beliefs, with no privileged foundation"],
        ["Foundationalism", "Justification traces back to basic beliefs that are self-justifying and do not depend on other beliefs"],
    ])},
    "critical-thinking-m2-l92": {"data_table": table(["Concept", "Key Point"], [
        ["Peer disagreement", "Arises when epistemic equals evaluate the same evidence and reach conflicting conclusions"],
        ["Epistemology of disagreement", "Conciliationist views recommend moving credence toward a disagreeing peer; steadfast views permit maintaining one's original credence"],
    ])},
    "critical-thinking-m2-l93": {"data_table": table(["Concept", "Key Point"], [
        ["Higher-order evidence", "Evidence about the reliability of one's own reasoning process, distinct from first-order evidence about the world"],
        ["Rational belief revision", "Discovering one reasoned poorly (e.g. while fatigued) can rationally require lowering confidence even without new first-order evidence"],
    ])},
    "critical-thinking-m2-l94": {"data_table": table(["Concept", "Key Point"], [
        ["Formal epistemology of trust", "Models how trust propagates and decays across a network of testifiers with varying reliability"],
        ["Testimony network", "Aggregate belief accuracy depends on network structure, e.g. how independent versus correlated the testifiers are"],
    ])},
    "critical-thinking-m2-l95": {"data_table": table(["Concept", "Key Point"], [
        ["Computational complexity of inference", "Determining satisfiability or entailment in expressive logics can be NP-hard or worse"],
        ["Practical implication", "Complexity bounds limit how much automated reasoning systems can scale for rich, expressive logical languages"],
    ])},
    "critical-thinking-m2-l96": {"data_table": table(["Concept", "Key Point"], [
        ["Doctoral thesis seminar", "A capstone forum for presenting and defending an original contribution to argumentation theory"],
        ["Original contribution", "Requires identifying a genuine gap in the existing literature and offering a novel, defensible resolution"],
    ])},
    "critical-thinking-m2-l97": {"data_table": table(["Concept", "Key Point"], [
        ["Bounded rationality", "Herbert Simon's view that decision makers operate under limits of information, time, and cognitive capacity"],
        ["Satisficing", "Choosing the first option that meets an acceptability threshold, rather than exhaustively optimizing over all alternatives"],
    ])},
    "critical-thinking-m2-l98": {"data_table": table(["Concept", "Key Point"], [
        ["Argument by analogy", "Infers a conclusion about a target case based on relevant similarities to a source case"],
        ["Formal models of analogical strength", "Weigh the number and relevance of shared properties against disanalogies to assess an analogy's evidential force"],
    ])},
    "critical-thinking-m2-l99": {"data_table": table(["Concept", "Key Point"], [
        ["Epistemic trespassing", "Occurs when someone with expertise in one field confidently pronounces on a different field without comparable expertise"],
        ["Disciplinary boundaries", "Trespassing is especially risky in interdisciplinary or public-facing argument where audiences may not track expertise limits"],
    ])},
    "critical-thinking-m2-l100": {"data_table": table(["Concept", "Key Point"], [
        ["Sorites paradox", "Repeated application of a seemingly valid small-change premise (removing one grain) leads from a heap to a non-heap"],
        ["Vagueness", "Philosophical logic offers competing responses: supervaluationism, epistemicism, and degree-theoretic (fuzzy) treatments"],
    ])},
    "critical-thinking-m2-l101": {"data_table": table(["Concept", "Key Point"], [
        ["Claims", "An assertion put forward as true, which argumentation either supports or challenges"],
        ["Evidence", "Data or observations offered in support of a claim; strength depends on relevance, sufficiency, and source credibility"],
    ])},
    "critical-thinking-m2-l102": {"data_table": table(["Concept", "Key Point"], [
        ["Deductive reasoning", "Draws conclusions that follow necessarily from the premises if the argument is valid"],
        ["Validity", "A deductive argument is valid when it is impossible for the premises to be true and the conclusion false"],
    ])},
    "critical-thinking-m2-l103": {"data_table": table(["Concept", "Key Point"], [
        ["Inductive reasoning", "Draws probable, not certain, conclusions by generalizing from observed instances"],
        ["Strength", "Inductive arguments are evaluated by strength (how probable the conclusion is given the premises), not validity"],
    ])},
    "critical-thinking-m2-l104": {"data_table": table(["Concept", "Key Point"], [
        ["Validity", "A property of argument form: the conclusion cannot be false while the premises are true"],
        ["Soundness", "A valid argument with all true premises; soundness guarantees a true conclusion"],
    ])},
    "critical-thinking-m2-l105": {"data_table": table(["Concept", "Key Point"], [
        ["Informal fallacy", "A reasoning error located in the content or context of an argument rather than its logical form"],
        ["Common examples", "Ad hominem, straw man, and false dilemma each undermine an argument without addressing its actual merits"],
    ])},
    "critical-thinking-m2-l106": {"data_table": table(["Concept", "Key Point"], [
        ["Cognitive bias", "A systematic, predictable deviation from normatively rational judgment"],
        ["Confirmation bias", "The tendency to seek, interpret, and recall information that confirms one's existing beliefs"],
    ])},
    "critical-thinking-m2-l107": {"data_table": table(["Concept", "Key Point"], [
        ["Causal reasoning", "Infers that one event brings about another, going beyond mere observed correlation"],
        ["Correlation vs. causation", "Two variables can move together due to a shared confounder without either causing the other"],
    ])},
    "critical-thinking-m2-l108": {"data_table": table(["Concept", "Key Point"], [
        ["Statistical claim", "An assertion grounded in numerical data, whose evaluation requires attention to sample size and methodology"],
        ["Common pitfalls", "Small samples, cherry-picked ranges, and misleading axes can make weak statistical claims appear compelling"],
    ])},
    "critical-thinking-m2-l109": {"data_table": table(["Concept", "Key Point"], [
        ["Scientific reasoning", "Forms and tests hypotheses against evidence through controlled, replicable observation"],
        ["Falsifiability", "A scientific hypothesis must, in principle, be capable of being shown false by some possible observation"],
    ])},
    "critical-thinking-m2-l110": {"data_table": table(["Concept", "Key Point"], [
        ["Source evaluation", "Assesses a source's credibility using criteria like expertise, track record, and potential bias"],
        ["Red flags", "Anonymous authorship, undisclosed conflicts of interest, and unverifiable claims all lower source reliability"],
    ])},
    "critical-thinking-m2-l111": {"data_table": table(["Concept", "Key Point"], [
        ["Media literacy", "The ability to critically analyze how media messages are constructed and for what purpose"],
        ["Framing", "The same facts can be presented to emphasize different aspects, shaping audience interpretation"],
    ])},
    "critical-thinking-m2-l112": {"data_table": table(["Concept", "Key Point"], [
        ["Argument mapping", "Visually represents the logical structure of an argument, showing how premises connect to a conclusion"],
        ["Benefit", "Makes hidden assumptions and structural gaps visible in a way linear prose often obscures"],
    ])},
    "critical-thinking-m2-l113": {"data_table": table(["Concept", "Key Point"], [
        ["Decision theory", "A formal framework for choosing among options under uncertainty by weighing outcomes and their probabilities"],
        ["Expected value", "The probability-weighted average payoff across all possible outcomes of a choice"],
    ])},
    "critical-thinking-m2-l114": {"data_table": table(["Concept", "Key Point"], [
        ["Ethical reasoning", "Evaluates actions or policies against moral principles such as consequences, duties, or virtues"],
        ["Key frameworks", "Consequentialism, deontology, and virtue ethics offer distinct standards for what makes an action right"],
    ])},
    "critical-thinking-m2-l115": {"data_table": table(["Concept", "Key Point"], [
        ["Legal reasoning", "Applies rules, statutes, and precedent to particular facts to reach a justified legal conclusion"],
        ["Precedent", "Prior binding decisions constrain how similar future cases must be decided"],
    ])},
    "critical-thinking-m2-l116": {"data_table": table(["Concept", "Key Point"], [
        ["Systems thinking", "Views a situation as an interconnected whole rather than a set of isolated, independent parts"],
        ["Unintended consequences", "Interventions in one part of a system often produce delayed or indirect effects elsewhere in the system"],
    ])},
    "critical-thinking-m2-l117": {"data_table": table(["Concept", "Key Point"], [
        ["Counterexample", "A case that satisfies an argument's premises or a claim's conditions while violating its conclusion"],
        ["Refutation role", "A single valid counterexample is sufficient to refute a universal claim or a purportedly valid argument form"],
    ])},
    "critical-thinking-m2-l118": {"data_table": table(["Concept", "Key Point"], [
        ["Uncertainty", "A state in which outcomes or their probabilities are not fully known"],
        ["Risk", "Distinguished from pure uncertainty by the availability of a known or estimable probability distribution over outcomes"],
    ])},
    "critical-thinking-m2-l119": {"data_table": table(["Concept", "Key Point"], [
        ["Constructive debate", "Structured disagreement aimed at clarifying issues and testing arguments rather than merely winning"],
        ["Steelmanning", "Engaging with the strongest possible version of an opposing argument rather than its weakest (straw man) version"],
    ])},
    "critical-thinking-m2-l120": {"data_table": table(["Concept", "Key Point"], [
        ["Metacognition", "Thinking about one's own thinking, including monitoring reasoning quality and knowing the limits of one's knowledge"],
        ["Self-regulation", "Using metacognitive monitoring to catch errors and revise a conclusion before acting on it"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Critical Thinking"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Missing lesson ids: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Critical Thinking lessons.")


if __name__ == "__main__":
    main()
