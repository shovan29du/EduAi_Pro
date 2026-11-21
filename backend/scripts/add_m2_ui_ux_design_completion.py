#!/usr/bin/env python3
"""Depth pass, M2 UI/UX Design: fill in real, hand-checked data_table
content for the M2 UI/UX Design lessons not covered by the earlier
breadth-first batch. Brings M2 UI/UX Design to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
theoretical HCI foundations (Fitts's Law, cognitive load, activity
theory), formal UX research methodology (Bayesian testing, causal
inference, eye-tracking), design systems and enterprise design
governance, ethics-oriented design (dark patterns, value-sensitive
design), multimodal/spatial/conversational interaction design,
perceptual and typographic design science, accessibility and inclusive
design, product strategy frameworks (Kano, JTBD, design sprints),
information architecture, and formal models of usability/trust/error
recovery; l101-l120 are "Worked Analysis" companions reusing the
data_table of l1-l20 (direct 1:1 mapping).

Lesson-id quirk (same as M1): l1-l100 use the "ui/ux-design-m2-"
prefix (literal slash character) while l101-l120 use the shorter
"ui-ux-design-m2-" prefix (no slash). l3 was already completed by an
earlier breadth-first batch, so its data_table is hard-coded here for
reuse (it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_ui_ux_design_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Fitts's Law", "A formal model predicting that the time to reach a target depends on distance and target size"],
    ["Target acquisition", "Interface elements that are larger and closer to the current cursor position are faster to reach and click"],
])

CHARTS: dict[str, dict] = {
    "ui/ux-design-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced UX research methods", "Rigorous, often mixed, qualitative and quantitative techniques for understanding user needs and behavior"],
        ["Application", "Selecting the right method depends on the research question, stage of design, and available resources"],
    ])},
    "ui/ux-design-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["UX design capstone", "An applied culminating project demonstrating end-to-end user experience research and design skill"],
        ["Deliverable", "Typically includes user research, design artifacts, and evaluation evidence for a real or simulated product"],
    ])},
    "ui/ux-design-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Information foraging theory", "Models users navigating an interface like animals foraging for food, following the strongest available scent"],
        ["Interface navigation", "Predicts users follow links and cues that appear most relevant to their information goal"],
    ])},
    "ui/ux-design-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive load theory", "Distinguishes intrinsic, extraneous, and germane load as contributors to a task's mental processing demand"],
        ["Complexity reduction", "Interface design should minimize extraneous load so users' limited working memory can focus on the task itself"],
    ])},
    "ui/ux-design-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Distributed cognition", "Views cognitive processes as spanning not just an individual's mind but also tools, artifacts, and other people"],
        ["Interface evaluation framework", "Evaluates how well an interface supports cognition distributed across the user and the system together"],
    ])},
    "ui/ux-design-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Activity theory", "Frames human activity as mediated by tools, motivated by objects, and shaped by social and cultural context"],
        ["HCI research application", "Analyzes how a tool's design supports or hinders the broader goal-directed activity it's embedded in"],
    ])},
    "ui/ux-design-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Ecological interface design", "Designs interfaces that make a complex system's underlying constraints directly perceivable to the operator"],
        ["Sociotechnical system", "Applied to complex, high-stakes domains like process control where operators must understand system state at a glance"],
    ])},
    "ui/ux-design-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Signal detection theory", "Distinguishes a user's sensitivity to detecting a signal from their response bias in reporting it"],
        ["Usability error analysis", "Separates genuine perceptual/comprehension failures from a user's cautious or liberal response tendency"],
    ])},
    "ui/ux-design-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian user intent model", "Infers a user's underlying goal by updating probabilistic beliefs based on their observed actions"],
        ["Intent prediction", "Enables an interface to proactively assist based on the most probable interpretation of ambiguous user behavior"],
    ])},
    "ui/ux-design-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Formal grammar-based model", "Represents valid interaction sequences using rules similar to a formal language grammar"],
        ["Interaction sequence modeling", "Enables systematic analysis of which action sequences are well-formed versus likely to indicate user confusion"],
    ])},
    "ui/ux-design-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["GOMS", "A modeling framework (Goals, Operators, Methods, Selection rules) predicting expert task completion time"],
        ["Keystroke-level modeling", "A simplified GOMS variant that estimates task time by summing standardized times for basic keystroke-level operations"],
    ])},
    "ui/ux-design-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Eye-tracking methodology", "Records where and how long a user looks at different parts of an interface"],
        ["Visual attention research", "Reveals which elements draw attention first and which are overlooked entirely, informing layout decisions"],
    ])},
    "ui/ux-design-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Psychophysiological measure", "Captures physical bodily responses (heart rate, skin conductance) as indicators of user emotional or cognitive state"],
        ["UX research application", "Complements self-report data with objective signals of stress, engagement, or frustration during interface use"],
    ])},
    "ui/ux-design-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian A/B testing", "Frames experiment analysis in terms of the probability one design variant is better, rather than a binary significance threshold"],
        ["Product experimentation framework", "Offers more intuitive interpretation and natural support for continuous monitoring compared with frequentist testing"],
    ])},
    "ui/ux-design-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Causal inference (product analytics)", "Estimates the true causal effect of a design change on user behavior, distinct from mere correlation"],
        ["Method", "Techniques like difference-in-differences help isolate a feature's genuine impact from confounding trends"],
    ])},
    "ui/ux-design-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Longitudinal diary study", "Participants record their experiences with a product over an extended period, capturing behavior in natural context"],
        ["Methodology", "Reveals patterns of use and pain points that a single lab session would miss entirely"],
    ])},
    "ui/ux-design-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Grounded theory", "A qualitative method that builds theory inductively from patterns discovered in the data itself"],
        ["Coding (qualitative UX research)", "Systematically labels and categorizes qualitative data to surface emergent themes without presupposing a framework"],
    ])},
    "ui/ux-design-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Mixed methods research", "Combines qualitative and quantitative approaches to draw on the strengths of both"],
        ["Product discovery design", "Uses qualitative insight to generate hypotheses and quantitative data to validate them at scale"],
    ])},
    "ui/ux-design-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility conformance auditing", "Systematically evaluates whether an interface meets established accessibility standards"],
        ["Formal methodology", "Combines automated scanning with manual expert and assistive-technology testing for comprehensive coverage"],
    ])},
    "ui/ux-design-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive walkthrough", "An expert evaluator steps through a task simulating a new user's thought process to identify likely points of confusion"],
        ["Expert usability evaluation", "Identifies learnability issues without requiring recruitment of actual test participants"],
    ])},
    "ui/ux-design-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Heuristic evaluation", "Expert evaluators assess an interface against a set of established usability principles"],
        ["Severity rating system", "Ranks identified issues by their impact and frequency to prioritize which problems to fix first"],
    ])},
    "ui/ux-design-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Design system governance", "The processes and roles that maintain consistency and quality of a design system over time"],
        ["Enterprise scale", "Large organizations require formal contribution, versioning, and review processes to keep a design system coherent"],
    ])},
    "ui/ux-design-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Design token", "A named, platform-agnostic value (e.g. a color or spacing unit) that represents a single design decision"],
        ["Token-based architecture", "Enables consistent styling across platforms by referencing shared tokens rather than hardcoded values"],
    ])},
    "ui/ux-design-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Cross-platform design language", "A shared visual and interaction vocabulary applied consistently across web, mobile, and other platforms"],
        ["Consistency modeling", "Balances platform-specific conventions against the benefits of a unified cross-platform brand experience"],
    ])},
    "ui/ux-design-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Service blueprint", "A diagram mapping all touchpoints, actors, and backstage processes involved in delivering a service"],
        ["Multi-touchpoint experience", "Reveals how frontstage user experience depends on backstage operational processes often invisible to the user"],
    ])},
    "ui/ux-design-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Systemic design", "Applies systems thinking to design problems that span multiple interconnected products, services, or stakeholders"],
        ["Complex product ecosystem", "Addresses design challenges that a single-product, single-touchpoint approach cannot adequately capture"],
    ])},
    "ui/ux-design-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Speculative design", "Creates provocative design artifacts depicting plausible future scenarios to provoke discussion and reflection"],
        ["Future scenario exploration", "Used to explore the implications of emerging technology before it is actually built"],
    ])},
    "ui/ux-design-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Critical design theory", "Uses design artifacts to challenge assumptions and provoke critical reflection rather than solve a practical problem"],
        ["Product strategy application", "Can surface unstated assumptions embedded in a product's current design direction"],
    ])},
    "ui/ux-design-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Participatory design", "Involves users directly as active co-creators throughout the design process, not just as research subjects"],
        ["Co-creation method", "Techniques like collaborative design workshops give users direct influence over design decisions"],
    ])},
    "ui/ux-design-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Design ethnography", "Immersive, in-context observation and interviewing to understand users' real-world practices and environment"],
        ["Deep contextual inquiry", "Reveals needs and workarounds that users themselves may not think to mention in a standard interview"],
    ])},
    "ui/ux-design-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Value sensitive design", "A framework that systematically accounts for human values throughout the design process"],
        ["Ethical interface design", "Explicitly considers stakeholder values like privacy, autonomy, and fairness alongside functional requirements"],
    ])},
    "ui/ux-design-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Dark pattern", "An interface design deliberately crafted to trick users into actions they wouldn't otherwise choose"],
        ["Regulatory countermeasure", "Increasing legal restrictions specifically prohibit deceptive design patterns like hidden costs or forced continuity"],
    ])},
    "ui/ux-design-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Persuasive technology", "Studies how interactive systems are designed to change users' attitudes or behaviors"],
        ["Ethical boundary", "Distinguishes legitimate persuasion that respects user autonomy from manipulative or coercive design"],
    ])},
    "ui/ux-design-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Nudge theory", "Alters the choice architecture to steer behavior in a beneficial direction without restricting options"],
        ["Digital interface application", "Examples include thoughtful defaults and framing that guide users toward beneficial choices"],
    ])},
    "ui/ux-design-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Trust calibration", "The degree to which a user's trust in an AI system matches the system's actual reliability"],
        ["AI-mediated interface formal model", "Poor calibration leads to either harmful over-reliance or unnecessary under-utilization of AI assistance"],
    ])},
    "ui/ux-design-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Explainable AI interface design", "Presents an AI system's reasoning or confidence in a way users can understand and act on"],
        ["Design pattern", "Includes patterns like confidence indicators and contrastive explanations tailored to the user's decision context"],
    ])},
    "ui/ux-design-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Conversational interface", "An interface where users interact through natural language dialogue rather than direct manipulation"],
        ["Dialogue state modeling", "Tracks the evolving context of a conversation to interpret user input correctly across multiple turns"],
    ])},
    "ui/ux-design-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Voice user interface prosody", "The rhythm, stress, and intonation patterns that shape how spoken interface responses are perceived"],
        ["Turn-taking design", "Manages the timing and cues that signal when the system versus the user should speak next"],
    ])},
    "ui/ux-design-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal fusion", "Combines input from multiple modalities (voice, touch, gesture) into a single interpreted user intent"],
        ["Fission architecture", "Decides how to distribute a single system response across multiple output modalities appropriately"],
    ])},
    "ui/ux-design-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Gestural interaction design", "Designs interfaces controlled through physical hand or body movements"],
        ["Spatial computing", "Gesture design for AR/VR must account for 3D space and the absence of physical surfaces to confirm actions"],
    ])},
    "ui/ux-design-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Haptic feedback", "Communicates information to a user through touch, such as vibration or resistance"],
        ["Tactile interface design principle", "Well-designed haptic feedback can confirm actions without requiring visual attention"],
    ])},
    "ui/ux-design-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["AR registration", "Accurately aligns virtual content with the real-world environment as perceived by the user"],
        ["Occlusion design", "Determines how virtual objects should be visually obscured by real-world objects positioned in front of them"],
    ])},
    "ui/ux-design-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["VR locomotion", "Methods for moving a user's viewpoint through a virtual environment"],
        ["Comfort design pattern", "Careful locomotion design (e.g. teleportation) reduces motion sickness common with unconstrained virtual movement"],
    ])},
    "ui/ux-design-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Wearable interface design", "Designs for devices worn on the body, with very limited screen space and attention"],
        ["Micro-interaction context", "Must convey information and accept input in extremely brief, glanceable interactions"],
    ])},
    "ui/ux-design-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Ambient interface", "Conveys information through the periphery of attention rather than demanding focused engagement"],
        ["Peripheral awareness system", "Allows users to stay informed of background information without interrupting their primary task"],
    ])},
    "ui/ux-design-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive interface personalization", "Algorithmically adjusts an interface's content or layout based on individual user behavior"],
        ["Algorithm", "Balances personalization benefits against the risk of reducing interface predictability and learnability"],
    ])},
    "ui/ux-design-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Interaction design pattern language", "A formal, structured vocabulary of reusable solutions to recurring interaction design problems"],
        ["Pattern construction", "Documents not just the solution but the specific context and forces that make it applicable"],
    ])},
    "ui/ux-design-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Motion design principle", "Guidelines for using animation to communicate state changes and spatial relationships in an interface"],
        ["Animation physics grounding", "Motion that mimics real-world physics (easing, momentum) tends to feel more natural and intuitive to users"],
    ])},
    "ui/ux-design-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Color science", "The study of how color is perceived and can be systematically measured and specified"],
        ["Perceptual uniformity", "A color space where equal numerical distances correspond to equal perceived differences, aiding consistent palette design"],
    ])},
    "ui/ux-design-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Typography legibility research", "Studies how typeface, size, and spacing affect how easily text can be read and comprehended"],
        ["Digital reading interface", "Screen-specific factors like resolution and viewing distance affect legibility differently than print"],
    ])},
    "ui/ux-design-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Grid system", "A structural framework of aligned columns and rows that organizes content placement in a layout"],
        ["Modular scale theory", "Uses a consistent mathematical ratio to derive harmonious spacing and sizing values throughout a design"],
    ])},
    "ui/ux-design-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Semiotics", "The study of how signs and symbols convey meaning"],
        ["Cross-cultural iconography", "An icon's meaning can vary or even reverse across cultures, requiring careful cross-cultural validation"],
    ])},
    "ui/ux-design-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Hofstede's cultural dimensions", "A framework characterizing cultures along dimensions like individualism and power distance"],
        ["Cross-cultural usability adaptation", "Informs how interface conventions like hierarchy and formality should adapt for different cultural contexts"],
    ])},
    "ui/ux-design-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Inclusive design", "Designs for the full range of human diversity from the start, rather than retrofitting for edge cases"],
        ["Beyond compliance accessibility", "Goes further than minimum legal accessibility standards to genuinely serve diverse user needs"],
    ])},
    "ui/ux-design-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive accessibility", "Designs interfaces to be usable by people with cognitive, learning, or attention differences"],
        ["Neurodivergent user design", "Considers needs like reduced complexity, clear structure, and flexible pacing for neurodivergent users"],
    ])},
    "ui/ux-design-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Aging-in-place interface design", "Designs technology that supports older adults living independently as cognitive and physical abilities change"],
        ["Age-related cognitive decline consideration", "Must accommodate changes in memory, processing speed, and vision that increase with age"],
    ])},
    "ui/ux-design-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Low-vision interaction model", "Designs interfaces usable by people with significant but not complete vision loss"],
        ["Screen reader interaction", "Requires interfaces to be structured so assistive technology can accurately convey content and navigation"],
    ])},
    "ui/ux-design-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["System Usability Scale (SUS)", "A widely used ten-item questionnaire producing a single usability score for an interface"],
        ["SUPR-Q and UMUX validity", "Alternative standardized usability questionnaires whose psychometric properties are compared against SUS in formal validity analysis"],
    ])},
    "ui/ux-design-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Structural equation modeling", "Models relationships among observed and latent variables, such as unobserved satisfaction driving observed behaviors"],
        ["User satisfaction driver", "Identifies which underlying factors most strongly influence overall user satisfaction with a product"],
    ])},
    "ui/ux-design-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Kano model", "Classifies product features by how their presence affects satisfaction: basic, performance, or delighter attributes"],
        ["Feature prioritization application", "Helps teams prioritize features that will meaningfully move satisfaction versus those users merely expect"],
    ])},
    "ui/ux-design-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Jobs-to-be-done theory", "Frames product decisions around the underlying job a customer is trying to accomplish, not just their stated wants"],
        ["Product design strategy", "Shifts focus from demographic segments to the functional and emotional job a product is hired to do"],
    ])},
    "ui/ux-design-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Design sprint", "A time-boxed, structured process for rapidly prototyping and testing a solution to a specific problem"],
        ["Rapid validation cycle", "Compresses months of typical process into days, testing a solution with real users before major investment"],
    ])},
    "ui/ux-design-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Lean UX", "An iterative design approach emphasizing rapid experimentation and validated learning over comprehensive upfront documentation"],
        ["Continuous delivery integration", "Aligns design iteration cadence with the frequent, incremental release cycles of continuous delivery"],
    ])},
    "ui/ux-design-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Design operations", "Practices and infrastructure that support scaling a design team's efficiency and impact"],
        ["Framework", "Addresses tooling, process, and team structure challenges that emerge as a design organization grows"],
    ])},
    "ui/ux-design-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Design critique", "A structured review process where designers give and receive feedback on work in progress"],
        ["Cross-functional facilitation model", "Effective critique formats include diverse stakeholders while keeping feedback constructive and actionable"],
    ])},
    "ui/ux-design-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Prototyping fidelity", "The degree to which a prototype resembles the final product in appearance and functionality"],
        ["Formal theory", "Different fidelity levels are appropriate for different research questions and stages of the design process"],
    ])},
    "ui/ux-design-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Wizard-of-Oz prototyping", "Tests a system concept by having a human secretly simulate its intelligent behavior behind the scenes"],
        ["AI-driven interface validation", "Lets teams evaluate an AI-powered concept's user experience before building the actual underlying AI system"],
    ])},
    "ui/ux-design-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Onboarding funnel", "The sequence of steps a new user passes through to reach full product engagement"],
        ["Formal optimization model", "Identifies where in the sequence users drop off, guiding targeted improvements to specific onboarding steps"],
    ])},
    "ui/ux-design-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral segmentation", "Groups users based on their observed actions and patterns of product usage rather than demographics"],
        ["Personalized UX modeling", "Enables tailoring experiences to how users actually behave, which often predicts needs better than stated attributes"],
    ])},
    "ui/ux-design-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Retention curve", "Plots the fraction of users still active over time since acquisition"],
        ["Habit formation design", "Well-designed products create triggers and rewards that build the recurring usage habits reflected in a strong retention curve"],
    ])},
    "ui/ux-design-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Emotional design theory", "Distinguishes visceral (appearance), behavioral (usability), and reflective (meaning) levels of emotional response to design"],
        ["Application", "A product can succeed at one level (attractive visceral design) while failing at another (poor behavioral usability)"],
    ])},
    "ui/ux-design-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Narrative theory", "Studies how stories are structured and how they create meaning for an audience"],
        ["Experience design application", "Frames a product's user journey as a narrative arc to create a more coherent and engaging experience"],
    ])},
    "ui/ux-design-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Flow state", "A state of complete absorption in an activity, occurring when challenge and skill are well matched"],
        ["Interactive system formal model", "Interfaces designed to maintain an appropriate challenge-skill balance can help sustain user flow"],
    ])},
    "ui/ux-design-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Design research repository", "A centralized, searchable archive of past research findings and insights"],
        ["Knowledge management architecture", "Prevents research insights from being lost or duplicated as design teams and projects evolve over time"],
    ])},
    "ui/ux-design-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Competitive teardown", "A systematic analysis of a competitor's product to understand its design decisions and trade-offs"],
        ["Strategic design analysis", "Informs one's own product strategy by understanding what alternatives the market has already explored"],
    ])},
    "ui/ux-design-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Card sorting", "A research method where participants group and label content items, revealing their mental model of a category structure"],
        ["Tree testing", "Evaluates whether users can find items within a proposed hierarchical navigation structure, tested statistically for success rate"],
    ])},
    "ui/ux-design-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Information architecture ontology", "A formal structure defining categories, relationships, and hierarchy for organizing content"],
        ["Large content system design", "Essential for making very large content collections navigable and findable"],
    ])},
    "ui/ux-design-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Faceted classification", "Organizes content along multiple independent dimensions (facets) that users can combine to filter"],
        ["Complex search interface", "Enables users to narrow results along several attributes simultaneously rather than a single fixed hierarchy"],
    ])},
    "ui/ux-design-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Search relevance ranking", "The algorithm determining the order in which search results are presented to a user"],
        ["Interface design consideration", "Result presentation must clearly convey why items are ranked as they are, supporting user trust in the ranking"],
    ])},
    "ui/ux-design-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Error recovery design", "Interface patterns that help users detect, understand, and correct their own mistakes"],
        ["Critical system formal model", "In high-stakes systems, formal models ensure recovery paths exist for every reachable error state"],
    ])},
    "ui/ux-design-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Human reliability analysis", "A methodology for predicting and quantifying the likelihood of human error in a given task"],
        ["Interface error prediction", "Applied to interface design to identify high-risk interaction points before deployment, especially in safety-critical systems"],
    ])},
    "ui/ux-design-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Situation awareness theory", "Models a user's perception, comprehension, and projection of a dynamic environment's state"],
        ["Dashboard and monitoring design", "Effective monitoring interfaces support all three levels of situation awareness, not just raw data display"],
    ])},
    "ui/ux-design-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Interruption and task resumption", "Studies how being interrupted affects a user's ability to later resume an interrupted task accurately"],
        ["Formal UI model", "Informs design features (like state-saving) that help users pick back up where they left off after an interruption"],
    ])},
    "ui/ux-design-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Data visualization perceptual effectiveness", "Ranks visual encodings (position, length, color) by how accurately humans can perceive the quantities they represent"],
        ["Ranking theory", "Position along a common scale is generally perceived most accurately, informing chart type selection"],
    ])},
    "ui/ux-design-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Dashboard design", "Presents key information in a format supporting rapid understanding and decision-making"],
        ["High-stakes decision support", "Must prioritize the most decision-relevant information clearly, avoiding clutter that could delay critical judgments"],
    ])},
    "ui/ux-design-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Interaction cost model", "Quantifies the effort (clicks, time, cognitive load) required to complete a workflow"],
        ["Multi-step workflow formal model", "Enables objectively comparing the efficiency of alternative workflow designs"],
    ])},
    "ui/ux-design-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Progressive disclosure", "Reveals interface complexity gradually, showing only what's needed at each step"],
        ["Cognitive justification", "Reduces initial cognitive load by deferring less-frequently-needed options until the user needs them"],
    ])},
    "ui/ux-design-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Skeuomorphism", "Design that mimics the appearance of real-world physical objects to leverage users' existing familiarity"],
        ["Flat design trade-off", "Flat design prioritizes simplicity and scalability at the cost of some of skeuomorphism's intuitive real-world cues"],
    ])},
    "ui/ux-design-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Affordance", "A property of an object that suggests how it can be used"],
        ["Signifier", "An explicit signal that communicates where an action should take place, distinct from the affordance itself"],
    ])},
    "ui/ux-design-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Usability benchmarking", "Systematically measures usability metrics to compare performance across time or product versions"],
        ["Longitudinal release comparison", "Tracks whether usability genuinely improves or regresses across successive product releases"],
    ])},
    "ui/ux-design-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Design debt", "Accumulated inconsistencies and shortcuts in a product's design that create ongoing usability and maintenance cost"],
        ["Quantification framework", "Attempts to measure design debt systematically, similar to how technical debt is tracked in engineering"],
    ])},
    "ui/ux-design-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Trust repair", "The process by which user trust can be rebuilt after an interface failure damages it"],
        ["Formal model", "Studies how factors like transparency and prompt acknowledgment of failure affect the speed and extent of trust recovery"],
    ])},
    "ui/ux-design-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Cross-device continuity", "Lets a user seamlessly pick up an activity on one device that they started on another"],
        ["Multi-screen ecosystem design", "Requires synchronized state and thoughtfully adapted interfaces across each device form factor"],
    ])},
    "ui/ux-design-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Discoverability", "The degree to which users can find features they need without prior instruction"],
        ["Feature-rich software formal model", "Complex software faces an inherent tension between exposing many features and keeping them discoverable"],
    ])},
    "ui/ux-design-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive scaffolding", "Temporary support structures that help a learner accomplish a task beyond their current independent ability"],
        ["Onboarding application", "Effective onboarding gradually removes scaffolding as users build competence and confidence"],
    ])},
    "ui/ux-design-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Design ethics review board", "A formal organizational body that reviews product designs for ethical concerns before launch"],
        ["Framework", "Provides structured oversight similar to research ethics boards, applied to commercial product design decisions"],
    ])},
    "ui/ux-design-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic fairness", "Ensures an algorithmic system treats different user groups equitably"],
        ["Personalized interface consideration", "Personalization algorithms must be audited to ensure they don't systematically disadvantage certain user groups"],
    ])},
    "ui/ux-design-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Interface localization", "Adapts an interface for a new language, region, or culture"],
        ["Beyond translation formal model", "True localization addresses layout direction, date/number formats, and culturally appropriate imagery, not just translated text"],
    ])},
    "ui/ux-design-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original design and execution of a UX research investigation"],
        ["Original research investigation", "Requires identifying a genuine gap in existing UX knowledge and rigorously investigating a novel research question"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["UI/UX Design"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"ui/ux-design-m2-l{base_n}"
        worked_key = f"ui-ux-design-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 UI/UX Design lessons.")


if __name__ == "__main__":
    main()
