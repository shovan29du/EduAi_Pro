#!/usr/bin/env python3
"""Depth pass, M2 AI Tools: fill in real, hand-checked data_table
content for the M2 AI Tools lessons not covered by the earlier
breadth-first batch. Brings M2 AI Tools to full 120/120 coverage.

MILESTONE: this is the final M2 (Masters Year 2) subject -- completing
it brings the M2 depth pass to 52/52 subjects, 6,240/6,240 lessons,
finishing the M2 level and the entire "grade 1 to masters year 2"
depth-pass instruction.

Structure: l1-l100 are unique doctoral-level topics spanning agentic
tool architecture (orchestration, memory, self-correction), evaluation
and benchmarking methodology for AI tools, prompt engineering and
retrieval-augmented tool design, security (prompt injection,
sandboxing, red-teaming), deployment/MLOps for AI tools (CI/CD,
routing, cost attribution), human-AI interaction design, domain-
specific copilots (legal, clinical, financial, creative), multimodal
tool integration, on-device/efficiency engineering, and AI tool
ethics/governance/policy; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_ai_tools_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Multi-agent orchestration", "Coordinates multiple specialized AI agents working together toward a shared goal"],
    ["Framework comparison", "Different frameworks vary in how they handle agent communication, task delegation, and shared state management"],
])

CHARTS: dict[str, dict] = {
    "ai-tools-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Future of AI tooling", "Considers emerging trends and trajectories shaping how AI-powered tools will evolve"],
        ["Application", "Informs strategic planning for organizations investing in AI tool development and adoption"],
    ])},
    "ai-tools-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["AI Tools capstone", "An applied culminating project demonstrating end-to-end AI tool design, evaluation, and deployment skill"],
        ["Deliverable", "Typically a working AI tool or agent with rigorous evaluation against defined success criteria"],
    ])},
    "ai-tools-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical task decomposition", "Breaks a complex overall goal into a nested structure of progressively simpler subtasks"],
        ["Autonomous agent application", "Enables an agent to plan and execute long, complex tasks by managing manageable subtask units rather than the entire goal at once"],
    ])},
    "ai-tools-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Tool-calling function schema", "A structured specification of a tool's name, parameters, and expected types that a model can invoke"],
        ["Reliable execution design", "Well-designed schemas with clear descriptions significantly improve a model's accuracy in selecting and correctly using a tool"],
    ])},
    "ai-tools-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Episodic memory", "Stores specific past events or interactions an agent experienced, retrievable in their original context"],
        ["Semantic memory", "Stores generalized facts and knowledge abstracted away from the specific episode in which they were learned"],
    ])},
    "ai-tools-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Failure recovery", "Mechanisms allowing an agent to detect and recover from an unsuccessful action or plan"],
        ["Self-correction loop", "The agent evaluates its own output or action outcome and revises its approach when a failure is detected"],
    ])},
    "ai-tools-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Cost-aware agent planning", "Incorporates the token or compute cost of each potential action into an agent's planning decisions"],
        ["Token budget constraint", "Forces the agent to balance thoroughness against a limited budget, prioritizing the most valuable actions"],
    ])},
    "ai-tools-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Sandboxed code execution", "Runs agent-generated code in an isolated environment that limits its access to system resources"],
        ["Coding agent application", "Essential for safely executing untrusted, AI-generated code without risking the host system"],
    ])},
    "ai-tools-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Cross-tool state synchronization", "Keeps a consistent view of task state as an agent moves between different tools during a workflow"],
        ["Long-running workflow application", "Prevents inconsistencies that could arise if different tools maintain independent, unsynchronized views of progress"],
    ])},
    "ai-tools-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Reflexion-style self-critique", "An agent generates a verbal self-reflection on a failed attempt, then uses that reflection to improve its next attempt"],
        ["Agent tool application", "Substitutes natural language self-critique for numeric reward signals as the mechanism for iterative improvement"],
    ])},
    "ai-tools-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Emergent tool-use", "An agent trained via reinforcement learning spontaneously discovers effective strategies for using available tools"],
        ["Reinforcement-learned agent", "Suggests tool-use competence can arise from reward-driven learning rather than being explicitly hand-programmed"],
    ])},
    "ai-tools-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Benchmark contamination", "Occurs when benchmark evaluation data has leaked into a model's training set, inflating apparent performance"],
        ["Tool evaluation detection", "Requires careful methodology to distinguish genuine tool capability from memorized benchmark answers"],
    ])},
    "ai-tools-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["LLM-as-a-judge", "Uses a language model itself to evaluate the quality of another model's (or tool's) outputs"],
        ["Reliability study", "Investigates whether LLM judges' evaluations align consistently with human judgment and are robust to superficial output variations"],
    ])},
    "ai-tools-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Statistical power analysis", "Determines the sample size needed to reliably detect an effect of a given size, if it exists"],
        ["Copilot A/B test application", "Ensures a coding copilot experiment has enough users or trials to draw statistically valid conclusions about a change"],
    ])},
    "ai-tools-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Regression testing", "Re-runs a fixed test suite whenever a system changes to catch unintended performance degradations"],
        ["Prompt-sensitive tool framework", "Must account for the fact that small prompt or model changes can nonlinearly affect an AI tool's behavior across the test suite"],
    ])},
    "ai-tools-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Longitudinal drift measurement", "Tracks how an AI assistant's behavior or quality changes gradually over an extended deployment period"],
        ["Production AI assistant application", "Detects silent degradation caused by factors like underlying model updates or shifting user query patterns"],
    ])},
    "ai-tools-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial robustness testing", "Systematically probes a system with deliberately challenging inputs to find failure cases"],
        ["Retrieval-augmented tool application", "Tests whether a RAG tool remains accurate and safe when retrieved content is adversarially crafted or misleading"],
    ])},
    "ai-tools-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Inter-annotator agreement", "Measures how consistently different human raters agree when evaluating the same output"],
        ["Subjective tool quality application", "Low agreement signals that a quality criterion may be too subjective or ill-defined to evaluate reliably"],
    ])},
    "ai-tools-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Confidence score calibration", "The alignment between a model's stated confidence and its actual likelihood of being correct"],
        ["AI output analysis", "Well-calibrated confidence scores let users appropriately trust or scrutinize a tool's outputs based on stated certainty"],
    ])},
    "ai-tools-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Task-completion metric", "Measures whether an autonomous agent successfully achieved its assigned goal"],
        ["Browsing agent application", "Must account for partial success and different valid paths to completion, not just an exact expected trajectory"],
    ])},
    "ai-tools-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual benchmark design", "Constructs evaluation suites that fairly test an assistant's performance across multiple languages"],
        ["Multilingual assistant application", "Must avoid biases where the benchmark's construction itself favors certain languages over others"],
    ])},
    "ai-tools-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought failure mode", "A category of ways step-by-step reasoning can go wrong, such as unfaithful or inconsistent reasoning steps"],
        ["Taxonomy", "Systematically classifying failure modes helps target specific interventions to improve reasoning reliability"],
    ])},
    "ai-tools-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Automatic prompt optimization", "Algorithmically searches for effective prompt wording without requiring gradient access to the model"],
        ["Gradient-free search", "Uses techniques like evolutionary search or LLM-guided iteration to improve prompts through black-box optimization"],
    ])},
    "ai-tools-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning sensitivity", "A model's performance can vary based on the specific ordering of few-shot examples in a prompt"],
        ["Example ordering", "Reveals that in-context learning is not fully order-invariant, an important consideration for reliable prompt design"],
    ])},
    "ai-tools-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Grammar-constrained decoding", "Restricts a model's token generation at each step to only those tokens consistent with a specified formal grammar"],
        ["Structured output enforcement", "Guarantees syntactically valid output, unlike prompting alone which offers no hard guarantee"],
    ])},
    "ai-tools-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Prompt compression", "Reduces a prompt's token length while preserving the information needed for the model to perform well"],
        ["Long-context pipeline application", "Reduces cost and latency, and helps keep relevant content within a model's effective context window"],
    ])},
    "ai-tools-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Meta-prompting", "Uses a language model itself to generate or refine prompts for another (or the same) model"],
        ["Self-improving tool chain strategy", "Enables a tool chain to iteratively refine its own prompting strategy based on observed performance"],
    ])},
    "ai-tools-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Few-shot example selection algorithm", "Selects which examples to include in a few-shot prompt to maximize their informativeness for the current query"],
        ["Domain tool application", "Tailoring examples to each query, rather than using a fixed set, often improves domain-specific tool accuracy"],
    ])},
    "ai-tools-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Prompt versioning", "Tracks changes to prompts over time, similar to source code version control"],
        ["Research pipeline reproducibility", "Precisely documenting exact prompt wording used in an experiment is essential for others to reproduce reported results"],
    ])},
    "ai-tools-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Hybrid sparse-dense retrieval", "Combines traditional keyword-based (sparse) search with semantic embedding-based (dense) search"],
        ["Enterprise assistant application", "Captures both exact keyword matches and semantically related content that pure dense or sparse retrieval alone might miss"],
    ])},
    "ai-tools-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Chunking strategy", "Determines how a document is split into smaller segments for indexing and retrieval"],
        ["Document retrieval optimization", "Chunk size and boundaries significantly affect retrieval relevance and the coherence of retrieved context"],
    ])},
    "ai-tools-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge-graph-augmented retrieval", "Combines structured knowledge graph relationships with traditional document retrieval"],
        ["Grounded generation application", "Provides explicit relational context that can improve accuracy for queries requiring multi-entity reasoning"],
    ])},
    "ai-tools-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Citation attribution accuracy", "Measures whether a generated citation actually supports the specific claim it's attached to"],
        ["RAG research assistant application", "Critical for research tools, since incorrect citations can mislead users into trusting unsupported claims"],
    ])},
    "ai-tools-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["HNSW", "A graph-based approximate nearest neighbor index offering fast, high-recall search at the cost of higher memory usage"],
        ["IVF-PQ", "An inverted-file index with product quantization, offering lower memory usage at some cost to search accuracy"],
    ])},
    "ai-tools-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Query rewriting", "Reformulates a user's original query into a form better suited for retrieving relevant documents"],
        ["Query expansion", "Adds related terms to a query to broaden its match against relevant documents that don't share the exact original wording"],
    ])},
    "ai-tools-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Multi-hop reasoning", "Combines information retrieved across multiple separate steps or documents to answer a complex question"],
        ["Retrieval-augmented tool evaluation", "Requires benchmarks specifically designed to test whether a tool can correctly chain together evidence from multiple sources"],
    ])},
    "ai-tools-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Freshness management", "Ensures a retrieval index reflects recently updated information"],
        ["Staleness management (live-indexed tools)", "Balances the cost of frequent re-indexing against the risk of serving outdated information to users"],
    ])},
    "ai-tools-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Prompt injection", "Embedding malicious instructions within input data to hijack a model's intended behavior"],
        ["Tool-calling pipeline defense", "Requires clearly separating trusted system instructions from untrusted tool outputs or retrieved content"],
    ])},
    "ai-tools-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Indirect prompt injection", "Malicious instructions embedded in external content (like a webpage) that an agent processes during its task"],
        ["Browsing agent risk", "Especially dangerous since the agent may encounter and act on hidden instructions without the user ever seeing them"],
    ])},
    "ai-tools-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Red-teaming", "Deliberately probes a system with adversarial inputs to discover safety or reliability failures before deployment"],
        ["Autonomous tool deployment methodology", "Structured red-teaming protocols systematically explore known and novel attack categories against an autonomous agent"],
    ])},
    "ai-tools-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Sandboxing", "Runs an agent's actions in a restricted environment that limits its access to system resources"],
        ["Permission scoping (execution assistants)", "Grants only the minimum necessary permissions needed for a specific task, limiting potential damage from errors or attacks"],
    ])},
    "ai-tools-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Supply-chain risk (AI plugins)", "Risk introduced by relying on third-party plugins or tools of unknown or unverified trustworthiness"],
        ["Ecosystem application", "A compromised or malicious third-party plugin can undermine the security of the entire AI tool ecosystem built on top of it"],
    ])},
    "ai-tools-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Output sanitization", "Removes or neutralizes potentially dangerous content from a model's generated output before it's used or displayed"],
        ["Injected-script attack prevention", "Prevents a malicious payload embedded in model output from being executed if rendered in a downstream context like a browser"],
    ])},
    "ai-tools-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving logging", "Records system activity for debugging and auditing while minimizing exposure of sensitive user data"],
        ["Enterprise AI deployment application", "Balances the operational need for logs against privacy and regulatory requirements around sensitive data handling"],
    ])},
    "ai-tools-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Model extraction attack", "Reconstructs a functionally similar copy of a proprietary model by querying its API and observing outputs"],
        ["Hosted AI tool API risk", "A concern for companies offering proprietary AI capabilities through an API, since competitors could attempt to replicate the model"],
    ])},
    "ai-tools-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Jailbreak taxonomy", "A structured classification of techniques used to bypass a model's safety training"],
        ["Consumer assistant mitigation", "Understanding common jailbreak categories helps prioritize defenses for widely used consumer-facing assistants"],
    ])},
    "ai-tools-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Audit trail", "A recorded, chronological log of actions and decisions taken by a system"],
        ["Regulatory compliance design", "Enables demonstrating to regulators exactly what an AI tool did and why, supporting accountability requirements"],
    ])},
    "ai-tools-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["CI/CD integration", "Automatically builds, tests, and deploys changes with minimal manual intervention"],
        ["Prompt and model version control", "Treats prompts and model configurations as versioned artifacts subject to the same rigor as application code"],
    ])},
    "ai-tools-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Cost attribution", "Accurately assigns AI tool usage costs to the specific teams or features responsible for generating them"],
        ["Chargeback model", "Enables fair internal billing and improves visibility into which use cases drive the most AI infrastructure spend"],
    ])},
    "ai-tools-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag", "A mechanism to toggle functionality on or off in production without a separate code deployment"],
        ["Gradual AI tool rollout strategy", "Enables incrementally releasing a new AI tool capability to a growing percentage of users while monitoring for issues"],
    ])},
    "ai-tools-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Observability stack", "Combines logging, metrics, and tracing to provide visibility into a running system's behavior"],
        ["Multi-tool workflow tracing", "Enables diagnosing latency and error sources across complex workflows spanning multiple AI tools and services"],
    ])},
    "ai-tools-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Shadow deployment", "Runs a new system version alongside the current production version, comparing outputs without affecting real users"],
        ["New AI tool version testing", "Allows validating a new tool version's real-world performance before it actually serves live user traffic"],
    ])},
    "ai-tools-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Model routing", "Directs each request to the most appropriate model based on factors like task type, cost, or current load"],
        ["Fallback across providers", "Automatically switches to an alternative LLM provider if the primary provider experiences an outage or degraded performance"],
    ])},
    "ai-tools-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Rate limiting", "Restricts how many requests a client can make within a given time window"],
        ["Quota architecture (AI tool APIs)", "Ensures fair resource allocation across users and prevents any single consumer from overwhelming shared AI infrastructure"],
    ])},
    "ai-tools-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Data residency", "Legal or policy requirements that data be stored and processed within specific geographic boundaries"],
        ["Global AI tool deployment constraint", "Requires careful architecture design to route and store data compliant with each region's residency requirements"],
    ])},
    "ai-tools-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Vendor lock-in risk", "The risk of becoming excessively dependent on a single AI provider's proprietary technology or APIs"],
        ["Enterprise adoption assessment", "Evaluates the cost and difficulty of switching providers, informing architecture decisions that preserve future flexibility"],
    ])},
    "ai-tools-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Change management framework", "Structured processes for guiding an organization through adopting a significant new technology"],
        ["AI tool adoption application", "Addresses the human and organizational factors, not just technical ones, that determine successful AI tool rollout"],
    ])},
    "ai-tools-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Trust calibration", "The degree to which a user's trust in an AI system matches the system's actual reliability"],
        ["Collaborative writing tool application", "Poor calibration leads to either harmful over-reliance on AI suggestions or unnecessary distrust of genuinely good suggestions"],
    ])},
    "ai-tools-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive load", "The amount of mental effort required to process information and complete a task"],
        ["AI-assisted coding environment application", "Poorly designed AI suggestions can increase cognitive load by requiring developers to constantly evaluate unsolicited interruptions"],
    ])},
    "ai-tools-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Explainability interface", "Presents a model's reasoning or confidence in a way users can understand and act on"],
        ["Non-expert user design", "Must translate technical model behavior into accessible explanations understandable without specialized AI knowledge"],
    ])},
    "ai-tools-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Automation bias", "The tendency to over-trust automated system recommendations, even when they conflict with other available evidence"],
        ["Over-reliance in decision tools", "A significant risk in AI decision-support tools, where users may defer to incorrect AI suggestions rather than applying independent judgment"],
    ])},
    "ai-tools-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Interruption design", "Determines when and how an AI agent should interrupt a human user for input or clarification"],
        ["Handoff design (human-agent workflow)", "Structures the transition point where control passes between the human and the AI agent during a shared task"],
    ])},
    "ai-tools-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Longitudinal adaptation study", "Tracks how users' behavior and reliance on an AI tool change over an extended period of use"],
        ["Copilot adoption application", "Reveals whether initial productivity gains from a copilot tool persist, grow, or fade as users adapt to it over time"],
    ])},
    "ai-tools-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Accessibility design pattern", "Reusable design solutions ensuring a tool is usable by people with a wide range of abilities"],
        ["AI tool application", "Includes patterns for screen-reader compatibility and alternative interaction modes for AI assistant interfaces"],
    ])},
    "ai-tools-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Cross-cultural usability", "How well a conversational AI assistant's design and behavior translate across different cultural contexts"],
        ["Conversational AI application", "Must account for varying cultural norms around politeness, directness, and appropriate assistant behavior"],
    ])},
    "ai-tools-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Precision", "The proportion of a legal review tool's flagged items that are genuinely relevant"],
        ["Recall trade-off", "The proportion of genuinely relevant items the tool successfully flags; improving one often comes at some cost to the other"],
    ])},
    "ai-tools-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Clinical decision support tool", "Software providing clinicians with patient-specific assessments or recommendations to inform care decisions"],
        ["Validation methodology", "Requires rigorous clinical validation given the high stakes of errors in a healthcare decision-support context"],
    ])},
    "ai-tools-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["AI-assisted literature synthesis", "Uses AI to help identify, summarize, and synthesize findings across a body of research literature"],
        ["Research tool application", "Can accelerate systematic review processes while requiring careful validation of accuracy and completeness"],
    ])},
    "ai-tools-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Hallucination risk (financial analyst copilot)", "The risk that an AI tool generates confident but factually incorrect financial figures or analysis"],
        ["Quantitative application", "Especially consequential in financial contexts, where a plausible-sounding but wrong number could lead to costly decisions"],
    ])},
    "ai-tools-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive feedback loop", "Adjusts the difficulty or content of instruction based on a learner's demonstrated performance"],
        ["AI tutoring system design", "Enables personalizing the pace and focus of instruction to each individual learner's needs"],
    ])},
    "ai-tools-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Style-transfer fidelity", "Measures how accurately a creative writing tool preserves a target writing style while generating new content"],
        ["Evaluation", "Requires both automated metrics and human judgment to assess whether the generated style genuinely matches the target"],
    ])},
    "ai-tools-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Escalation threshold", "The point at which a customer support copilot hands off a conversation to a human agent"],
        ["Design consideration", "Must balance automation efficiency against the risk of frustrating customers with an AI unable to resolve their issue"],
    ])},
    "ai-tools-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Architectural design copilot", "An AI tool assisting architects within computer-aided design (CAD) workflows"],
        ["CAD-integrated workflow application", "Must integrate seamlessly with existing professional design tools and constraints specific to architectural practice"],
    ])},
    "ai-tools-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["AI-assisted grant writing tool evaluation", "Assesses how effectively an AI tool helps produce competitive grant or funding proposals"],
        ["Application", "Must evaluate both writing quality and whether the tool helps meet specific funder requirements and evaluation criteria"],
    ])},
    "ai-tools-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Originality (music composition copilot)", "Assesses whether AI-generated music constitutes genuinely novel creative work"],
        ["Copyright risk", "Raises legal questions about whether AI-generated compositions might infringe on copyrighted training data"],
    ])},
    "ai-tools-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Vision-language tool integration", "Combines visual and textual understanding within a single AI tool"],
        ["Document understanding application", "Enables tools to jointly interpret a document's layout, images, and text content together"],
    ])},
    "ai-tools-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Speech-to-action pipeline", "Converts spoken user commands directly into executable system actions"],
        ["Voice-controlled assistant application", "Must handle speech recognition errors gracefully to avoid executing unintended actions from misheard commands"],
    ])},
    "ai-tools-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Consistency across iterative edits", "Measures whether an image generation tool maintains coherent visual elements across a sequence of user-requested edits"],
        ["Application", "A key usability challenge, since users often expect unedited parts of an image to remain unchanged across iterations"],
    ])},
    "ai-tools-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Video understanding tool", "Analyzes video content to extract meaning, objects, or events"],
        ["Automated content moderation application", "Applies video understanding to flag policy-violating content at a scale manual review couldn't achieve"],
    ])},
    "ai-tools-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Cross-modal grounding", "The correctness with which a multimodal assistant connects textual references to the correct corresponding visual elements"],
        ["Evaluation", "Assesses whether a model's textual claims about an image are actually accurately grounded in the image's visual content"],
    ])},
    "ai-tools-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Diagram interpretation accuracy", "Measures how correctly a vision copilot extracts information from charts and diagrams"],
        ["Application", "Requires understanding structured visual conventions (axes, legends, flow) beyond simple natural image recognition"],
    ])},
    "ai-tools-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Screen-reading agent", "An AI agent that perceives and interprets a graphical user interface to perform automated actions"],
        ["GUI automation application", "Enables automating tasks in applications lacking a dedicated API, by directly interpreting the visual interface"],
    ])},
    "ai-tools-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal retrieval", "Retrieves relevant content spanning both text and image modalities from a combined knowledge base"],
        ["Mixed knowledge base application", "Requires unified representations enabling meaningful similarity comparison across both text and image content"],
    ])},
    "ai-tools-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Quantization", "Reduces the numerical precision of a model's weights and activations to shrink memory and compute cost"],
        ["On-device deployment trade-off", "Enables running capable AI tools on resource-constrained devices, at some cost to model accuracy"],
    ])},
    "ai-tools-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Query caching", "Stores previously computed results for repeated queries, avoiding redundant computation"],
        ["Repeated pattern strategy", "Especially effective for assistants handling many similar or identical queries from different users"],
    ])},
    "ai-tools-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Speculative decoding", "A small draft model proposes several tokens which a larger model verifies in parallel, speeding up generation"],
        ["Low-latency response generation", "Speeds up tool response time by exploiting the fact that verifying proposed tokens is cheaper than generating them one at a time"],
    ])},
    "ai-tools-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Batching strategy", "Groups multiple requests together to process them more efficiently as a single batch"],
        ["Cost-efficient enterprise serving application", "Improves throughput and reduces per-request cost, at some cost to individual request latency"],
    ])},
    "ai-tools-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Model distillation", "Trains a smaller student model to mimic a larger teacher model's output distribution"],
        ["Lightweight domain-specific copilot application", "Enables deploying a capable but efficient copilot tailored to a specific domain, without the cost of a large general-purpose model"],
    ])},
    "ai-tools-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Token budget optimization", "Manages the allocation of limited token budget across the steps of a multi-step tool chain"],
        ["Multi-step tool chain application", "Prevents earlier steps in a chain from consuming so many tokens that later, potentially important steps are starved of budget"],
    ])},
    "ai-tools-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Edge deployment constraint", "Limitations on compute, memory, and connectivity that shape how an AI tool can run on edge devices"],
        ["Offline assistant tool application", "Must function without reliable network connectivity, requiring the full model and any needed data to reside locally"],
    ])},
    "ai-tools-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["IP attribution framework", "Determines and documents the intellectual property status of content generated by an AI tool"],
        ["AI-generated content application", "An evolving legal area addressing questions of authorship and ownership for AI-assisted creative output"],
    ])},
    "ai-tools-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic accountability audit", "Systematically evaluates an AI tool's decisions for fairness, transparency, and unintended harms"],
        ["Enterprise AI tool application", "Provides structured oversight to help organizations identify and address problematic AI tool behavior before it causes harm"],
    ])},
    "ai-tools-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Bias propagation", "How biases present in one component of a system can be amplified or compounded as data flows through subsequent stages"],
        ["Chained AI tool pipeline application", "A significant concern in multi-tool pipelines, where a bias introduced early can compound through each subsequent processing stage"],
    ])},
    "ai-tools-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Regulatory compliance mapping", "Systematically identifies which specific legal requirements apply to a given AI tool or deployment"],
        ["Emerging AI act application", "Helps organizations navigate the rapidly evolving landscape of AI-specific regulation across different jurisdictions"],
    ])},
    "ai-tools-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Environmental impact assessment", "Quantifies the energy consumption and carbon footprint associated with running AI inference at scale"],
        ["Large-scale tool inference application", "An increasingly important consideration given the substantial cumulative energy cost of widely deployed AI tools"],
    ])},
    "ai-tools-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Informed consent model", "A structured process for obtaining meaningful user consent for how their data will be used"],
        ["AI tool personalization data application", "Must clearly communicate what personal data an AI tool collects and how it's used to personalize behavior"],
    ])},
    "ai-tools-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Labor displacement impact study", "Systematically researches how AI tool automation affects employment in specific occupations or industries"],
        ["AI tool automation application", "Informs policy discussions about the workforce transition implications of widespread AI tool adoption"],
    ])},
    "ai-tools-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Open-source AI governance", "Governance models for AI ecosystems built on openly available, community-developed models and tools"],
        ["Proprietary ecosystem comparison", "Open and proprietary models differ significantly in transparency, customizability, and centralized control over AI development"],
    ])},
    "ai-tools-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["AI tool manifest standardization", "Efforts to establish common, interoperable specifications for describing an AI tool's capabilities and interface"],
        ["Interoperability application", "Enables different AI systems and platforms to discover and use tools built by different developers consistently"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["AI Tools"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"ai-tools-m2-l{base_n}"
        worked_key = f"ai-tools-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 AI Tools lessons.")


if __name__ == "__main__":
    main()
