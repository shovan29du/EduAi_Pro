#!/usr/bin/env python3
"""Depth pass, M2 Philosophy: fill in real, hand-checked data_table
content for the M2 Philosophy lessons not covered by the earlier
breadth-first batch. Brings M2 Philosophy to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
philosophy of language and mind (Kripke, Putnam, Chalmers, Jackson,
Nagel), personal identity, epistemology (contextualism, Bayesian
epistemology, Williamson), normative and metaethics (Parfit, Scanlon,
free will debates, expressivism), metaphysics (grounding, structural
realism, philosophy of time, causation, mathematics, vagueness),
social/political philosophy (social ontology, feminist epistemology,
environmental ethics, global justice), continental philosophy
(Heidegger, Levinas, Foucault, Derrida, Deleuze), further metaphysics
(Ship of Theseus, mereology, universals), and comparative/applied
philosophy (Buddhist philosophy, Confucian ethics, Anscombe, Murdoch,
MacIntyre, Thomson); l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_philosophy_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Modal semantics", "Studies the meaning of statements about necessity and possibility across possible worlds"],
    ["Necessity of identity", "Kripke argued that if a=b is true, it is necessarily true, since identity statements between rigid designators cannot be contingent"],
])

CHARTS: dict[str, dict] = {
    "philosophy-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Contemporary philosophy", "Philosophical work from roughly the mid-20th century onward, engaging with modern formal and scientific developments"],
        ["Scope", "Spans analytic and continental traditions, both continuing to develop distinct methods and central questions"],
    ])},
    "philosophy-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Philosophy capstone", "An applied culminating project demonstrating original philosophical argumentation and research skill"],
        ["Deliverable", "Typically a substantial paper defending an original thesis against the strongest anticipated objections"],
    ])},
    "philosophy-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Twin Earth thought experiment", "Putnam's scenario where a substance physically identical to water but chemically distinct (XYZ) challenges internalist meaning theories"],
        ["Semantic externalism", "The view that a term's meaning depends partly on facts about the external world, not solely on a speaker's internal mental state"],
    ])},
    "philosophy-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Rule-following paradox", "Kripke's reading of Wittgenstein: no fact about past usage seems to determine which rule a speaker is actually following"],
        ["Wittgenstein connection", "Raises a skeptical challenge about whether meaning is determinate at all, addressed through Wittgenstein's private language argument"],
    ])},
    "philosophy-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Hard problem of consciousness", "Chalmers's distinction between explaining cognitive functions (the easy problems) and explaining subjective experience itself"],
        ["Significance", "Argues that even a complete functional/physical explanation of the brain may not explain why there is subjective experience at all"],
    ])},
    "philosophy-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge argument", "Jackson's thought experiment: Mary, a scientist who knows all physical facts about color but has never seen color, learns something new upon first seeing red"],
        ["Physicalism challenge", "Suggests physical knowledge alone may not capture all facts about conscious experience, challenging strict physicalism"],
    ])},
    "philosophy-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Nagel's bat argument", "Argues we cannot know what it is subjectively like to be a bat, since its sensory experience (echolocation) is radically alien to ours"],
        ["Limits of objectivity", "Suggests subjective experience resists full capture by objective, third-person scientific description"],
    ])},
    "philosophy-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Personal identity (Parfit)", "Questions what makes a person at one time the same person at a later time"],
        ["Reductionist view", "Parfit argued personal identity consists in nothing more than psychological and physical continuity relations, not a further deep fact"],
    ])},
    "philosophy-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Teletransportation case", "A thought experiment where a person is scanned, destroyed, and an exact copy is reconstructed elsewhere, testing intuitions about survival"],
        ["Fission case", "A thought experiment where one person's brain is split and each half continues in a separate body, challenging simple identity criteria"],
    ])},
    "philosophy-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Modal realism", "David Lewis's view that all possible worlds are literally, concretely real, just as real as our own actual world"],
        ["Possible worlds", "Used to analyze modal claims (necessity, possibility) as quantification over these concretely existing worlds"],
    ])},
    "philosophy-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Two-dimensional semantics", "Analyzes meaning along two dimensions: how reference depends on the actual world, and how it varies across possible worlds"],
        ["A priori contingency", "Explains how some truths can be knowable a priori yet metaphysically contingent, resolving apparent tension in Kripke's framework"],
    ])},
    "philosophy-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Indeterminacy of translation", "Quine's thesis that multiple, mutually incompatible translation manuals could equally fit all possible behavioral evidence"],
        ["Implication", "Challenges the idea that there is a single objectively correct meaning or translation determined by the facts"],
    ])},
    "philosophy-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Externalist justification", "Epistemic justification depends on factors outside the believer's awareness, e.g. a reliable belief-forming process"],
        ["Contrast", "Distinguished from internalist views requiring the grounds for justification to be accessible to the believer's own reflection"],
    ])},
    "philosophy-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Contextualism", "The standards for correctly attributing knowledge shift depending on the conversational context"],
        ["Invariantism", "The standards for knowledge attribution remain fixed regardless of conversational context"],
    ])},
    "philosophy-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian epistemology", "Models rational belief updating using probability theory and Bayes' theorem"],
        ["Problem of old evidence", "Challenges Bayesian confirmation theory: evidence already known before a theory's proposal seems unable to confirm that theory under strict Bayesian updating"],
    ])},
    "philosophy-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Epistemic peer disagreement", "Arises when individuals with comparable evidence and reasoning ability reach conflicting conclusions"],
        ["Problem", "Raises the question of whether rationality requires revising one's credence toward a disagreeing peer's view"],
    ])},
    "philosophy-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Reliabilism", "A belief is justified if produced by a cognitive process that reliably yields true beliefs"],
        ["Responsibilism", "Locates justification in the exercise of intellectual virtues and responsible cognitive conduct, not just reliable process types"],
    ])},
    "philosophy-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Regress problem", "Any chain of justification for a belief seems to require justifying the justifiers, threatening an infinite regress"],
        ["Foundationalism versus coherentism", "Foundationalism halts the regress with basic self-justifying beliefs; coherentism rejects linear justification for a web of mutual support"],
    ])},
    "philosophy-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge-first epistemology", "Timothy Williamson's view that knowledge is the fundamental epistemic notion, not analyzable into more basic components like justified true belief"],
        ["Significance", "Reverses the traditional order of analysis, treating belief and evidence as explained partly in terms of knowledge rather than the reverse"],
    ])},
    "philosophy-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Repugnant conclusion", "Parfit's finding that total utilitarianism implies a sufficiently large population with barely worthwhile lives is better than a smaller, very happy population"],
        ["Population ethics", "A central challenge motivating extensive work on how to aggregate wellbeing across different possible population sizes"],
    ])},
    "philosophy-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Non-identity problem", "A policy that changes who is born cannot easily be said to harm the different people who exist because of it, even if their lives are worse"],
        ["Intergenerational ethics", "Complicates standard harm-based reasoning about obligations to future generations, such as in climate policy"],
    ])},
    "philosophy-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Contractualism", "Scanlon's view that an act is wrong if it would be disallowed by principles no one could reasonably reject"],
        ["What We Owe to Each Other", "Grounds morality in the justifiability of principles to each individual, rather than aggregate welfare or fixed duties"],
    ])},
    "philosophy-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Constructivism (Korsgaard)", "The view that normative truths are constructed through rational agency's own practical self-legislation, not discovered as mind-independent facts"],
        ["Sources of normativity", "Locates the ultimate source of moral obligation in the nature of reflective rational agency itself"],
    ])},
    "philosophy-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Particularism", "Moral reasons can vary in valence depending on context; no fixed general principles hold across all situations"],
        ["Generalism", "Moral judgments are ultimately grounded in and derivable from general, context-independent moral principles"],
    ])},
    "philosophy-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Doctrine of double effect", "An action with both good and harmful effects may be permissible if the harm is foreseen but not intended as a means"],
        ["Applied ethics application", "Used to distinguish morally between, for example, killing a civilian as a means versus as an unintended side effect"],
    ])},
    "philosophy-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Trolley problem", "A thought experiment testing intuitions about diverting harm from many to one, probing the limits of consequentialist reasoning"],
        ["Consequentialist limit", "Variations reveal that many people's intuitions diverge from pure aggregate-outcome reasoning in systematic ways"],
    ])},
    "philosophy-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Moral luck", "Factors outside an agent's control appear to affect the moral assessment of their actions, challenging strict control-based responsibility"],
        ["Limits of responsibility", "Raises tension between the intuitive view that responsibility requires control and the pervasive influence of luck on outcomes"],
    ])},
    "philosophy-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Frankfurt case", "A scenario where an agent acts freely even though a counterfactual intervener would have forced the same action if the agent had chosen otherwise"],
        ["Alternate possibilities challenge", "Challenges the principle that moral responsibility requires the ability to have done otherwise"],
    ])},
    "philosophy-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Compatibilism", "The view that free will and moral responsibility are compatible with causal determinism"],
        ["Consequence argument", "A key argument against compatibilism, contending that if determinism is true, our actions are the consequence of events beyond our control"],
    ])},
    "philosophy-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Reactive attitude", "Emotional responses like resentment or gratitude that presuppose viewing others as responsible agents"],
        ["Strawson's Freedom and Resentment", "Argues that our practice of holding people responsible is grounded in these natural reactive attitudes, not metaphysical facts about free will"],
    ])},
    "philosophy-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Metaethical constructivism", "Moral facts are constructed through rational agreement or agency rather than existing independently"],
        ["Moral realism", "The view that objective moral facts exist independently of what anyone believes or agrees to"],
    ])},
    "philosophy-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Open question argument", "G.E. Moore's argument that for any proposed natural property (e.g. pleasure), it remains an open question whether that property is actually good"],
        ["Anti-naturalism", "Used to argue that goodness cannot be reductively defined in purely natural, non-moral terms"],
    ])},
    "philosophy-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Error theory", "The view that moral claims purport to describe objective facts, but no such facts exist, so all moral claims are systematically false"],
        ["Argument from queerness", "Mackie's argument that objective moral properties would be metaphysically and epistemologically too strange to plausibly exist"],
    ])},
    "philosophy-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Expressivism", "Moral statements express attitudes (like approval or disapproval) rather than describing objective facts"],
        ["Frege-Geach problem", "Challenges expressivism to explain how moral statements function correctly in logical arguments if they don't express truth-apt propositions"],
    ])},
    "philosophy-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Quasi-realism", "Blackburn's project of showing expressivism can earn the right to speak as if moral claims are objectively true"],
        ["Projectivism", "The view that we project our attitudes onto the world, experiencing them as though they were objective features of it"],
    ])},
    "philosophy-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Reasons internalism", "A consideration counts as a genuine practical reason for an agent only if connected to that agent's existing motivations"],
        ["Reasons externalism", "Practical reasons can apply to an agent regardless of whether they connect to that agent's actual existing motivations"],
    ])},
    "philosophy-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Internal reason", "A reason for action grounded in an agent's existing subjective motivational set"],
        ["External reason (Williams)", "Bernard Williams argued genuine external reasons, independent of an agent's motivational set, are conceptually incoherent"],
    ])},
    "philosophy-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Grounding", "A relation of metaphysical dependence and explanation, where one fact holds in virtue of another more fundamental fact"],
        ["Grounding problem", "Asks how to precisely characterize this relation and what, ultimately, grounds everything else"],
    ])},
    "philosophy-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Structural realism", "The view that science reveals the structure or relations of reality, but is more agnostic about the intrinsic nature of the underlying entities"],
        ["Philosophy of science application", "Offers a middle path between full scientific realism and antirealism, especially given historical theory changes"],
    ])},
    "philosophy-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Pessimistic meta-induction", "Since many past successful scientific theories were later found false, current successful theories are also likely to eventually be overturned"],
        ["Scientific realism challenge", "A key historical argument against naive scientific realism's claim that our best current theories are approximately true"],
    ])},
    "philosophy-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Natural kind", "A category that reflects a genuine, objective grouping in nature, not merely an arbitrary human classification"],
        ["Scientific classification metaphysics", "Debates whether categories like biological species or chemical elements carve nature at genuinely objective joints"],
    ])},
    "philosophy-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Causal exclusion problem", "If a mental event's effect is fully explained by its underlying physical cause, the mental cause seems causally redundant"],
        ["Philosophy of mind challenge", "Threatens the causal efficacy of mental states given physicalism's commitment to the causal completeness of the physical"],
    ])},
    "philosophy-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Extended mind thesis", "Cognitive processes can extend beyond the brain into external tools and artifacts that are functionally integrated into thinking"],
        ["Example", "A notebook used to reliably store and retrieve information can function as part of an agent's memory system"],
    ])},
    "philosophy-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Predictive processing", "A theory of cognition where the brain continuously generates predictions about sensory input and updates based on prediction error"],
        ["Application", "Offers a unifying framework for perception, action, and learning as forms of ongoing prediction-error minimization"],
    ])},
    "philosophy-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Higher-order theory of consciousness", "A mental state is conscious only if it is the object of an appropriate higher-order representation or thought"],
        ["Application", "Distinguishes mere information processing from consciousness by requiring a meta-level representation of the first-order state"],
    ])},
    "philosophy-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Global workspace theory", "Consciousness arises when information is broadcast widely across specialized brain processes via a shared \"workspace\""],
        ["Attention connection", "Closely tied to theories of selective attention, since global broadcast typically follows attentional selection"],
    ])},
    "philosophy-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Integrated information theory", "Proposes consciousness corresponds to a system's integrated information (phi), which can in principle be measured"],
        ["Consciousness theory", "A prominent, mathematically formalized approach attempting to give consciousness a precise quantitative characterization"],
    ])},
    "philosophy-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Panpsychism", "The view that consciousness, or proto-consciousness, is a fundamental and ubiquitous feature of physical reality"],
        ["Combination problem", "The challenge of explaining how simple, fundamental units of proto-consciousness combine to produce complex, unified experiences like human consciousness"],
    ])},
    "philosophy-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Presentism", "Only the present moment is real; past and future do not exist"],
        ["Eternalism", "Past, present, and future are all equally real, existing as parts of a single four-dimensional block universe"],
    ])},
    "philosophy-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["McTaggart's argument", "Argues that time, understood as an A-series (past/present/future), is contradictory and therefore unreal"],
        ["Unreality of time", "A foundational and influential, if contested, argument in the philosophy of time"],
    ])},
    "philosophy-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Four-dimensionalism", "Objects extend not just through three spatial dimensions but also through time, having temporal as well as spatial parts"],
        ["Temporal part", "A slice of an object existing at a particular moment, analogous to a spatial part occupying a particular region"],
    ])},
    "philosophy-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Endurantism", "Objects persist by being wholly present at each moment of their existence, without temporal parts"],
        ["Perdurantism", "Objects persist by having different temporal parts existing at different times, only ever partially present at any moment"],
    ])},
    "philosophy-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Humean supervenience", "The view that all facts about the world, including laws, supervene on the total distribution of local, intrinsic properties across spacetime"],
        ["Metaphysics of laws", "Denies that laws of nature are governing forces, treating them instead as mere regularities in the pattern of local facts"],
    ])},
    "philosophy-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Dispositional essentialism", "Properties have their causal powers essentially, so the laws of nature follow necessarily from the nature of properties themselves"],
        ["Causation metaphysics", "Grounds causal necessity in the essential dispositional nature of properties, contrasting with Humean regularity views"],
    ])},
    "philosophy-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Counterfactual theory of causation", "Analyzes causation in terms of counterfactual dependence: if the cause hadn't occurred, the effect wouldn't have either"],
        ["Application", "Lewis's influential framework, which faces challenges from cases of causal preemption and overdetermination"],
    ])},
    "philosophy-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Interventionist theory of causation", "Defines causal relationships in terms of what would happen under a hypothetical intervention on the cause variable"],
        ["Causal explanation", "Widely used in both philosophy and statistics/science to formalize causal claims via manipulability"],
    ])},
    "philosophy-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Fictionalism (mathematics)", "Mathematical statements are useful fictions, not literally true descriptions of a mind-independent realm of abstract objects"],
        ["Application", "Avoids committing to the existence of abstract mathematical objects while preserving mathematics' practical usefulness"],
    ])},
    "philosophy-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Indispensability argument", "Since mathematics is indispensable to our best scientific theories, we should believe in the mathematical objects those theories quantify over"],
        ["Mathematical platonism", "The view that abstract mathematical objects exist independently of human minds, supported by this indispensability reasoning"],
    ])},
    "philosophy-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Structuralism (mathematics)", "Mathematical objects are defined entirely by their structural role within a system of relations, not by any intrinsic nature"],
        ["Application", "Numbers, for instance, are understood as positions within the structure of the number system, not standalone objects"],
    ])},
    "philosophy-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Liar paradox", "The sentence 'This sentence is false' appears to be true if and only if it is false, generating a logical contradiction"],
        ["Theories of truth", "A central test case that any adequate formal theory of truth must somehow resolve or accommodate"],
    ])},
    "philosophy-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Tarski's semantic theory of truth", "Defines truth for a formal language via a recursive definition satisfying Convention T: 'S' is true if and only if S"],
        ["Significance", "Provided a rigorous, mathematically precise foundation for formal semantics that avoids the Liar paradox within a formal language"],
    ])},
    "philosophy-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Deflationism about truth", "The view that truth is not a substantive property; saying 'P is true' adds nothing beyond simply asserting P"],
        ["Contrast", "Denies that a rich, explanatory theory of the nature of truth is needed or even possible"],
    ])},
    "philosophy-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Sorites paradox", "Repeated application of a seemingly valid small-change premise (removing one grain) leads from a heap to a non-heap"],
        ["Vagueness", "The paradox highlights the puzzling logical status of vague predicates that lack sharp boundaries"],
    ])},
    "philosophy-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Supervaluationism", "Treats a vague statement as true if it comes out true on every acceptable way of precisifying the vague term, false if false on all, and indeterminate otherwise"],
        ["Vagueness theory", "Preserves classical logic's laws (like excluded middle) while allowing for genuine indeterminacy in borderline cases"],
    ])},
    "philosophy-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Epistemicism", "Vague predicates actually do have sharp, precise boundaries, but we are simply unable to know exactly where they lie"],
        ["Vagueness theory", "Preserves classical bivalence entirely, locating the puzzle in our epistemic limitations rather than in the world or language itself"],
    ])},
    "philosophy-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Metaphysics of race", "Examines whether racial categories correspond to any objective biological or social reality, or are purely socially constructed"],
        ["Contemporary debate", "Contested between eliminativist, constructionist, and naturalist positions on the ontological status of race"],
    ])},
    "philosophy-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Social ontology", "Studies the nature and existence conditions of social entities like institutions, money, and nations"],
        ["Collective intentionality", "Analyzes how shared intentions among multiple individuals (\"we intend\") ground the existence of social facts"],
    ])},
    "philosophy-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Feminist standpoint epistemology", "Argues that marginalized social positions can provide epistemically advantageous perspectives on certain social realities"],
        ["Application", "Challenges the assumption that a purely neutral, unsituated standpoint is the best or only path to objective knowledge"],
    ])},
    "philosophy-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Critical race theory", "Examines how race and racism are embedded in legal systems and social structures, not merely individual prejudice"],
        ["Epistemic injustice", "Connects to how racialized individuals can be unfairly disadvantaged as knowers, e.g. through testimonial credibility deficits"],
    ])},
    "philosophy-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Ecofeminist philosophy", "Connects the domination of nature to patriarchal structures that also enable the domination of women"],
        ["Application", "Argues that addressing environmental exploitation requires also addressing the underlying logic of domination shared with gender oppression"],
    ])},
    "philosophy-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Deep ecology", "Holds that nature has intrinsic value independent of its usefulness to humans, requiring a fundamental shift from anthropocentrism"],
        ["Non-anthropocentric ethics", "Rejects human interests as the sole or primary basis for environmental ethical consideration"],
    ])},
    "philosophy-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Intergenerational justice", "Examines what obligations current generations owe to future generations who cannot represent their own interests today"],
        ["Climate ethics application", "Central to debates over how much current sacrifice is owed to mitigate harms that will primarily affect future generations"],
    ])},
    "philosophy-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Capabilities approach", "Measures justice and wellbeing by the real freedoms and opportunities (capabilities) people actually have, not just resources"],
        ["Sen and Nussbaum", "Developed jointly, with Nussbaum further specifying a list of central capabilities central to human dignity"],
    ])},
    "philosophy-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Original position", "Rawls's hypothetical choice situation where principles of justice are selected without knowledge of one's own social position"],
        ["Veil of ignorance", "Ensures impartiality by preventing choosers from favoring principles that benefit their own particular circumstances"],
    ])},
    "philosophy-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Cosmopolitanism", "Holds that principles of justice apply to all persons globally, not merely within the boundaries of one's own state"],
        ["Political realism (global justice)", "Emphasizes the primacy of state sovereignty and national interest, skeptical of robust global distributive obligations"],
    ])},
    "philosophy-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Analytic Marxism", "Applies rigorous analytic philosophical methods to reconstruct and evaluate Marxist claims about exploitation and history"],
        ["Exploitation theory", "Analyzes precisely what makes a labor relationship exploitative, moving beyond traditional Marxist labor theory of value"],
    ])},
    "philosophy-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Discourse ethics", "Habermas's view that moral norms are valid only if they could be agreed to by all affected parties in an ideal, unconstrained discourse"],
        ["Communicative rationality", "Grounds normative validity in the structure of genuine, undistorted communication among free and equal participants"],
    ])},
    "philosophy-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Genealogy of power", "Foucault's historical method tracing how power relations and forms of knowledge co-develop and shape what counts as truth"],
        ["Discipline", "Analyzes how modern institutions exercise power through subtle, normalizing surveillance and control rather than overt coercion"],
    ])},
    "philosophy-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Deconstruction", "Derrida's method of showing how texts undermine their own apparent stable meanings through internal tensions and contradictions"],
        ["Metaphysics of presence", "Derrida's critique of the Western philosophical tendency to privilege immediate presence over absence, writing, and difference"],
    ])},
    "philosophy-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Being and Time", "Heidegger's major work investigating the question of what it means for anything to be, through analysis of human existence (Dasein)"],
        ["Question of being", "Argues that Western philosophy has largely forgotten to properly ask this most fundamental of all questions"],
    ])},
    "philosophy-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Ethics of the Other", "Levinas grounds ethics in the primordial, pre-rational responsibility one has upon encountering the face of another person"],
        ["Face-to-face encounter", "The direct encounter with another's face is, for Levinas, the foundational ethical event prior to any rational deliberation"],
    ])},
    "philosophy-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Dialectic of Enlightenment", "Adorno and Horkheimer's argument that Enlightenment rationality, meant to liberate humanity, paradoxically produces new forms of domination"],
        ["Critical theory", "A foundational work of the Frankfurt School examining how instrumental reason can turn against its own emancipatory aims"],
    ])},
    "philosophy-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Rhizome", "Deleuze and Guattari's concept of a non-hierarchical, horizontally connected structure, contrasted with rigid tree-like hierarchies"],
        ["Application", "Used as a model for thinking about knowledge, culture, and organization without a single fixed root or center"],
    ])},
    "philosophy-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Ship of Theseus", "A classic puzzle about whether an object that has had all its parts gradually replaced remains the same object"],
        ["Contemporary interpretation", "Continues to inform contemporary debates about identity, composition, and persistence over time"],
    ])},
    "philosophy-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Mereological nihilism", "The view that only simple, partless entities truly exist; composite objects are not, strictly speaking, real"],
        ["Composition as identity", "The alternative view that a composite whole just is, in some sense, identical to its parts taken together"],
    ])},
    "philosophy-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Trope theory", "Properties are particular, non-shareable instances (tropes) rather than universal entities shared across different objects"],
        ["Realism (universals)", "The view that genuine universal properties exist and can be wholly present in multiple distinct objects simultaneously"],
    ])},
    "philosophy-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Modal fictionalism", "Treats talk of possible worlds as a useful fiction for analyzing modal claims, without committing to their literal existence"],
        ["Ontology of possibility", "Offers an alternative to Lewis's modal realism that avoids the metaphysical cost of believing in concretely existing other worlds"],
    ])},
    "philosophy-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Grounding", "A relation of metaphysical dependence and explanation between more and less fundamental facts"],
        ["Fundamentality", "Contemporary metaphysics increasingly uses grounding to structure a hierarchy of what is ultimately fundamental versus derivative"],
    ])},
    "philosophy-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["No-self (anatta)", "The Buddhist doctrine that there is no permanent, unchanging self underlying the stream of changing experiences"],
        ["Personal identity connection", "Engages directly with Western debates on personal identity by denying the metaphysical substrate many Western theories assume"],
    ])},
    "philosophy-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Confucian role ethics", "Grounds ethical conduct in fulfilling one's specific relational roles (parent, friend, ruler) well, rather than abstract universal principles"],
        ["Western virtue theory comparison", "Shares virtue theory's focus on character, but emphasizes relational roles more centrally than Western Aristotelian individual virtue"],
    ])},
    "philosophy-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Intention (Anscombe)", "Elizabeth Anscombe's influential analysis of what it is to act intentionally, revitalizing the philosophy of action"],
        ["Philosophy of action", "Her work distinguished intentional action from mere behavior, examining the special first-person knowledge agents have of their own intentional actions"],
    ])},
    "philosophy-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Anomalous monism", "Davidson's view that mental events are identical to physical events, yet there are no strict laws connecting mental and physical event types"],
        ["Logical form of action sentences", "His broader work analyzed how action sentences logically represent events, influencing philosophy of language and action"],
    ])},
    "philosophy-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Master's thesis research seminar", "A forum for presenting and defending original philosophical research to faculty and peers"],
        ["Philosophy research", "Emphasizes constructing a rigorous, well-defended argument for an original thesis, engaging seriously with objections"],
    ])},
    "philosophy-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Sovereignty of Good", "Iris Murdoch's argument that moral life centers on attentive perception of reality (especially other people) rather than pure will or choice"],
        ["Moral vision", "Emphasizes the moral significance of how one sees and attends to the world, prior to and shaping deliberate choice"],
    ])},
    "philosophy-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["After Virtue", "MacIntyre's critique arguing modern moral discourse is fragmented and incoherent, having lost its grounding in a shared tradition of virtue"],
        ["Critique of Enlightenment morality", "Argues the Enlightenment project of grounding morality in pure reason, detached from tradition, was bound to fail"],
    ])},
    "philosophy-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Violinist argument", "Judith Jarvis Thomson's thought experiment (being unwillingly connected to a violinist) arguing bodily autonomy can override even a right to life"],
        ["Applied ethics application", "A landmark argument in the abortion debate, notable for granting fetal personhood while still defending a right to abortion in some cases"],
    ])},
    "philosophy-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["View from Nowhere", "Thomas Nagel's exploration of the tension between the objective, impersonal standpoint and the irreducibly subjective, personal standpoint"],
        ["Problem of objectivity", "Investigates whether and how these two perspectives on reality and value can be reconciled"],
    ])},
    "philosophy-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Communitarian critique", "Michael Sandel's argument that Rawlsian liberalism's conception of the self as unencumbered by prior commitments is philosophically mistaken"],
        ["Rawlsian liberalism critique", "Argues that individuals are constituted by their communal attachments in ways Rawls's original position framework fails to capture"],
    ])},
    "philosophy-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Ethics of ambiguity", "Simone de Beauvoir's existentialist ethics grounding morality in embracing, rather than escaping, the fundamental ambiguity of human freedom and situation"],
        ["Existentialist ethics", "Argues genuine ethical life requires affirming one's own freedom while also willing the freedom of others"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Philosophy"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"philosophy-m2-l{base_n}"
        worked_key = f"philosophy-m2-l{worked_n}"
        if base_n == 3:
            CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
        elif base_key in CHARTS:
            CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}

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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Philosophy lessons.")


if __name__ == "__main__":
    main()
