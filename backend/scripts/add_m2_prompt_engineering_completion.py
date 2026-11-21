#!/usr/bin/env python3
"""Depth pass, M2 Prompt Engineering: fill in real, hand-checked
data_table content for the M2 Prompt Engineering lessons not covered
by the earlier breadth-first batch. Brings M2 Prompt Engineering to
full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning advanced
reasoning prompting techniques (tree-of-thought, ReAct, Reflexion),
prompt optimization and evaluation methodology, adversarial/security
prompting (jailbreaks, injection defenses), retrieval-augmented and
tool-use prompting, multimodal prompting, domain-specific prompt
libraries, and prompt engineering research methodology; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_prompt_engineering_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Constitutional AI", "Trains or prompts a model to critique and revise its own outputs against a written set of principles"],
    ["Self-critique prompting", "Explicitly instructs a model to evaluate and improve its own initial response before finalizing an answer"],
])

CHARTS: dict[str, dict] = {
    "prompt-engineering-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Agentic prompting", "Designs prompts that let a model plan, act, and adapt across multiple steps toward a goal, rather than answering a single query"],
        ["Advanced technique", "Combines planning, tool use, and self-monitoring instructions to support extended autonomous task execution"],
    ])},
    "prompt-engineering-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Prompt engineering capstone", "An applied culminating project demonstrating end-to-end prompt design and evaluation skill"],
        ["Deliverable", "Typically includes a prompt design, systematic evaluation against baselines, and analysis of failure modes"],
    ])},
    "prompt-engineering-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Tree-of-thought", "Generalizes chain-of-thought reasoning into a search tree of partial reasoning paths that can be expanded and evaluated"],
        ["Reasoning structure", "Allows exploring, comparing, and backtracking among multiple candidate reasoning paths rather than one fixed chain"],
    ])},
    "prompt-engineering-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Self-consistency", "Samples multiple independent reasoning paths and takes the majority final answer"],
        ["Chain-of-thought decoding", "Improves robustness over a single greedy chain-of-thought by reducing the impact of any one flawed reasoning path"],
    ])},
    "prompt-engineering-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["ReAct pattern", "Interleaves explicit reasoning steps with concrete actions (like tool calls), each informing the next"],
        ["Application", "Lets a model's reasoning be grounded and corrected by real observations from its actions, not pure internal deliberation"],
    ])},
    "prompt-engineering-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Reflexion", "An agent generates a verbal self-reflection on a failed attempt, then uses that reflection to improve its next attempt"],
        ["Verbal reinforcement learning", "Substitutes natural language self-critique for numeric reward signals as the mechanism for iterative improvement"],
    ])},
    "prompt-engineering-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Least-to-most prompting", "Decomposes a complex problem into a sequence of progressively harder subproblems, solving each in order"],
        ["Compositional task application", "Particularly effective for tasks requiring systematic generalization from simpler to more complex compositions"],
    ])},
    "prompt-engineering-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Program-aided language model", "Prompts a model to generate executable code as an intermediate reasoning step, then runs the code to get the final answer"],
        ["Application", "Offloads precise computation (like arithmetic) to a reliable interpreter rather than the model's own approximate reasoning"],
    ])},
    "prompt-engineering-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Contrastive chain-of-thought", "Provides both correct and incorrect example reasoning chains to help the model learn to avoid common reasoning errors"],
        ["Application", "The contrast between valid and invalid examples helps highlight what specifically makes a reasoning chain flawed"],
    ])},
    "prompt-engineering-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Automatic prompt optimization", "Algorithmically searches for effective prompt wording without requiring gradient access to the model"],
        ["Gradient-free search", "Uses techniques like evolutionary search or LLM-guided iteration to improve prompts through black-box optimization"],
    ])},
    "prompt-engineering-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Soft prompt tuning", "Learns a small set of continuous embedding vectors prepended to the input, rather than discrete text tokens"],
        ["Prefix tuning", "Learns task-specific continuous vectors inserted at each transformer layer, keeping the base model's weights frozen"],
    ])},
    "prompt-engineering-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Instruction induction", "Infers the underlying task instruction directly from a small set of input-output demonstration examples"],
        ["Few demonstrations", "Enables automatically discovering an effective natural-language task description without manual prompt authoring"],
    ])},
    "prompt-engineering-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Meta-prompting", "Uses a language model itself to generate or refine prompts for another (or the same) model"],
        ["Prompt generation", "Leverages the model's own language understanding to bootstrap effective prompt candidates automatically"],
    ])},
    "prompt-engineering-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Prompt compression", "Reduces a prompt's token length while preserving the information needed for the model to perform well"],
        ["Long context application", "Reduces cost and latency, and helps keep relevant content within a model's effective context window"],
    ])},
    "prompt-engineering-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-verification", "Prompts a model to generate an initial answer, then independently verify each factual claim before finalizing it"],
        ["Factual consistency application", "Reduces hallucination by explicitly checking claims rather than trusting the first-pass generation"],
    ])},
    "prompt-engineering-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Skeleton-of-thought", "First generates a high-level outline (skeleton), then expands each point in parallel"],
        ["Parallel generation", "Enables faster response generation by expanding independent outline points concurrently rather than sequentially"],
    ])},
    "prompt-engineering-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Step-back prompting", "First prompts the model to derive a general principle or abstraction, then applies it to the specific question"],
        ["Abstraction application", "Improves reasoning on specialized questions by first grounding the answer in relevant general knowledge"],
    ])},
    "prompt-engineering-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Analogical prompting", "Prompts a model to generate its own relevant worked examples before solving the target problem"],
        ["Self-generated exemplars", "Avoids needing hand-curated few-shot examples by having the model create its own relevant analogies"],
    ])},
    "prompt-engineering-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent debate", "Multiple model instances argue different positions on a question, with a final answer determined from the debate"],
        ["Answer verification", "Debate can surface errors in an initial answer that a single model instance might not catch on its own"],
    ])},
    "prompt-engineering-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Role-play prompting", "Instructs a model to respond as if it were a specific persona or character"],
        ["Persona conditioning limit", "Persona instructions can shift style and tone but have documented limits in reliably changing a model's underlying knowledge or safety behavior"],
    ])},
    "prompt-engineering-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Jailbreak taxonomy", "A structured classification of techniques used to bypass a model's safety training"],
        ["Adversarial prompt pattern", "Common categories include role-play framing, hypothetical scenarios, and encoding tricks to evade content filters"],
    ])},
    "prompt-engineering-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Prompt injection", "Embedding malicious instructions within input data to hijack a model's intended behavior"],
        ["Tool-using agent vulnerability", "Especially dangerous when an agent processes untrusted external content (like a webpage) that could contain hidden instructions"],
    ])},
    "prompt-engineering-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Defensive prompt design", "Structures a prompt to resist manipulation by clearly separating trusted instructions from untrusted content"],
        ["Injection defense", "Techniques include explicit delimiters and instructing the model to treat embedded content as data, not commands"],
    ])},
    "prompt-engineering-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Sandwich defense", "Places the trusted system instruction both before and after untrusted user content to reinforce the intended behavior"],
        ["Instruction hierarchy", "Establishes an explicit priority ordering so system-level instructions take precedence over lower-trust content"],
    ])},
    "prompt-engineering-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Canary token", "A unique marker embedded in a prompt to detect if the prompt's content has leaked into a model's output"],
        ["Prompt leakage detection", "If the canary appears in an output where it shouldn't, it signals the underlying system prompt may have been exposed"],
    ])},
    "prompt-engineering-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Formal evaluation rubric", "A structured, explicit set of criteria for scoring the quality of a model's prompted output"],
        ["Prompt quality assessment", "Enables consistent, reproducible evaluation across different prompts and evaluators rather than subjective impressions"],
    ])},
    "prompt-engineering-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["LLM-as-judge", "Uses a language model itself to evaluate the quality of another model's (or its own) outputs"],
        ["Evaluation methodology", "Scales evaluation beyond what human raters could feasibly do, though it inherits its own biases and limitations"],
    ])},
    "prompt-engineering-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Pairwise preference evaluation", "Compares two outputs directly against each other rather than scoring each in isolation"],
        ["Elo ranking", "Aggregates many pairwise comparison outcomes into a single relative ranking, similar to chess rating systems"],
    ])},
    "prompt-engineering-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Model confidence calibration", "The alignment between a model's expressed confidence and its actual likelihood of being correct"],
        ["Prompting for calibration", "Specific prompting strategies can encourage a model to express more accurately calibrated uncertainty"],
    ])},
    "prompt-engineering-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Uncertainty quantification", "Estimates how confident a model's generated output should be treated as"],
        ["Generated output application", "Harder to quantify for open-ended text generation than for classification with a fixed set of labels"],
    ])},
    "prompt-engineering-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Structured output prompting", "Instructs a model to produce output conforming to a specific format, like JSON"],
        ["Schema constraint", "Explicitly specifying a schema helps the model produce consistently parseable, well-formed structured output"],
    ])},
    "prompt-engineering-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Grammar-constrained decoding", "Restricts a model's token generation at each step to only those tokens consistent with a specified formal grammar"],
        ["Reliable parsing application", "Guarantees syntactically valid output, unlike prompting alone which offers no hard guarantee"],
    ])},
    "prompt-engineering-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Function-calling schema", "A structured specification of a tool's name, parameters, and expected types that a model can invoke"],
        ["Tool use design", "Well-designed schemas with clear descriptions significantly improve a model's accuracy in selecting and using the correct tool"],
    ])},
    "prompt-engineering-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tool orchestration", "Coordinates a model's use of several available tools within a single task"],
        ["Tool selection prompt", "Guides the model in choosing which tool is appropriate for a given subtask among multiple available options"],
    ])},
    "prompt-engineering-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Long-horizon agent planning", "Structures a prompt to help a model plan and execute a task spanning many sequential steps"],
        ["Subgoal decomposition", "Breaks a complex overall goal into a sequence of more manageable, individually achievable subgoals"],
    ])},
    "prompt-engineering-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Memory architecture (agents)", "A mechanism letting an agent store and retrieve information across an extended, multi-step interaction"],
        ["Persistent agent context", "Enables an agent to maintain relevant context beyond what fits within a single prompt's context window"],
    ])},
    "prompt-engineering-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Context window management", "Strategies for deciding what information to keep, summarize, or discard as a multi-turn conversation grows"],
        ["Multi-turn agent application", "Essential once conversation history exceeds a model's fixed context window limit"],
    ])},
    "prompt-engineering-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Prompt-based routing", "Uses a prompt to decide which specialized model or expert should handle a given input"],
        ["Mixture-of-expert pipeline", "Applies routing logic at the pipeline/application level, distinct from the architectural mixture-of-experts inside a single model"],
    ])},
    "prompt-engineering-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Prompt ensembling", "Combines outputs generated from the same prompt across multiple different models"],
        ["Cross-model family application", "Can improve robustness by aggregating diverse model families' differing strengths and error patterns"],
    ])},
    "prompt-engineering-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning theory", "Studies the mechanisms by which a model adapts its behavior to examples given in its prompt without weight updates"],
        ["Mechanism research", "Investigates whether in-context learning approximates implicit gradient descent or Bayesian inference over a latent task"],
    ])},
    "prompt-engineering-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Emergent ability", "A qualitative capability that appears abruptly once a model crosses a scale threshold, absent in smaller models"],
        ["Prompt sensitivity research", "Studies how a model's performance on a task can vary dramatically based on minor, seemingly inconsequential prompt wording changes"],
    ])},
    "prompt-engineering-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Prompt robustness testing", "Systematically evaluates whether a prompt's effectiveness holds across semantically equivalent rephrasings"],
        ["Paraphrase testing", "Reveals whether a prompt's success depends on brittle, specific wording rather than genuine task understanding"],
    ])},
    "prompt-engineering-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual prompt transfer", "Adapting a prompt effective in one language to work well in another"],
        ["Adaptation challenge", "Direct translation of a prompt doesn't always preserve its effectiveness across languages with different linguistic structures"],
    ])},
    "prompt-engineering-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Culturally-aware localization", "Adapts a prompt's examples and framing to be appropriate and relevant for a specific cultural context"],
        ["Application", "Goes beyond language translation to account for culturally specific norms, references, and sensitivities"],
    ])},
    "prompt-engineering-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Bias auditing", "Systematically tests prompted model outputs for unfair or skewed treatment across different demographic groups"],
        ["Application", "Reveals patterns of disparate output quality or content that might not be apparent from casual, unsystematic testing"],
    ])},
    "prompt-engineering-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Red-teaming", "Deliberately probes a system with adversarial inputs to discover safety or reliability failures before deployment"],
        ["Prompt-based system protocol", "Structured red-teaming protocols systematically explore known and novel attack categories against a prompted system"],
    ])},
    "prompt-engineering-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Prompt versioning", "Tracks changes to production prompts over time, similar to source code version control"],
        ["Regression testing pipeline", "Automatically re-evaluates a prompt against a test suite whenever it changes, catching unintended performance regressions"],
    ])},
    "prompt-engineering-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["A/B testing (prompts)", "Compares two prompt variants' real-world performance by randomly routing production traffic between them"],
        ["Production framework", "Enables data-driven prompt improvement decisions based on actual user outcomes rather than offline evaluation alone"],
    ])},
    "prompt-engineering-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Cost-latency tradeoff", "Balances a prompt chain's total token cost and response time against its accuracy and capability"],
        ["Prompt chain design", "Longer, more elaborate reasoning chains often improve accuracy but at increased cost and latency"],
    ])},
    "prompt-engineering-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Prompt caching", "Reuses previously computed results for a repeated prompt prefix, avoiding redundant computation"],
        ["Repeated prefix strategy", "Especially effective when many requests share a common, unchanging system prompt or context prefix"],
    ])},
    "prompt-engineering-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Query reformulation", "Rewrites a user's original query into a form better suited for retrieving relevant documents"],
        ["Retrieval prompting application", "Can expand ambiguous queries or rephrase them to better match how relevant documents are likely worded"],
    ])},
    "prompt-engineering-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Hypothetical document embedding", "Generates a hypothetical answer to a query, then uses that hypothetical text's embedding to search for real relevant documents"],
        ["Retrieval technique", "Often matches real documents better than embedding the original short query directly, since documents and hypothetical answers share more structural similarity"],
    ])},
    "prompt-engineering-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Query decomposition", "Breaks a complex question into a sequence of simpler sub-questions"],
        ["Multi-hop question answering", "Enables answering questions that require combining information retrieved across multiple separate steps or sources"],
    ])},
    "prompt-engineering-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Self-RAG", "A retrieval-augmented generation approach where the model actively decides when to retrieve and reflects on the usefulness of retrieved content"],
        ["Reflective retrieval-augmented generation", "Adds explicit self-assessment steps rather than always retrieving and using content uncritically"],
    ])},
    "prompt-engineering-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Toolformer-style prompting", "Trains or prompts a model to self-supervise learning when and how to invoke external tools during generation"],
        ["Self-supervised tool use", "The model learns tool-use patterns from its own generated examples rather than requiring extensive hand-labeled tool-use data"],
    ])},
    "prompt-engineering-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Code generation prompting", "Designs prompts to elicit correct, well-structured code from a language model"],
        ["Code repair application", "Prompting strategies for fixing bugs often provide error messages and relevant context alongside the broken code"],
    ])},
    "prompt-engineering-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Test-driven prompting", "Provides or generates test cases as part of the prompt, guiding the model toward code that satisfies them"],
        ["Code synthesis application", "Tests give the model concrete, verifiable success criteria beyond a natural-language description alone"],
    ])},
    "prompt-engineering-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification-assisted reasoning", "Prompts a model to produce reasoning that can be checked against a formal verification tool"],
        ["Application", "Combines the model's natural language fluency with the rigor of formal proof checking to catch reasoning errors"],
    ])},
    "prompt-engineering-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Socratic prompting", "Guides a learner toward an answer through a sequence of probing questions rather than directly stating the answer"],
        ["Tutoring system application", "Encourages active learner reasoning and self-discovery rather than passive reception of information"],
    ])},
    "prompt-engineering-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Scaffolded prompting", "Provides graduated levels of support, reducing assistance as the learner or task demonstrates increasing competence"],
        ["Progressive disclosure", "Reveals complexity gradually, showing only what's needed at each stage of the interaction"],
    ])},
    "prompt-engineering-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal prompting", "Designs prompts combining text with other modalities like images for vision-language models"],
        ["Vision-language application", "Must carefully specify how the model should integrate and reference visual content alongside textual instructions"],
    ])},
    "prompt-engineering-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Visual chain-of-thought", "Extends step-by-step textual reasoning to prompts that also incorporate visual evidence and image regions"],
        ["Visual reasoning application", "Requires the model to integrate visual and textual evidence coherently across its reasoning steps"],
    ])},
    "prompt-engineering-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Audio/speech model prompting", "Designs prompts tailored to models processing or generating audio and speech content"],
        ["Strategy", "Must account for prosodic and acoustic considerations distinct from purely text-based prompting"],
    ])},
    "prompt-engineering-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Negative prompting", "Specifies content that should be excluded or avoided in a diffusion model's generated image"],
        ["Diffusion image generation", "Steers the generation process away from unwanted elements without needing to positively describe every alternative"],
    ])},
    "prompt-engineering-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Prompt weighting", "Adjusts the relative influence of different terms within a diffusion model's text prompt"],
        ["Attention steering", "Directly manipulates the model's cross-attention to emphasize or de-emphasize specific concepts during generation"],
    ])},
    "prompt-engineering-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Textual inversion", "Learns a new embedding token representing a specific style or concept from example images, usable in future prompts"],
        ["Style transfer application", "Enables invoking a learned custom style or subject by name in subsequent generation prompts"],
    ])},
    "prompt-engineering-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Time-series forecasting LLM prompting", "Frames time-series forecasting as a language modeling task, prompting an LLM to predict future values"],
        ["Application", "An emerging approach leveraging LLMs' pattern recognition, distinct from traditional statistical forecasting models"],
    ])},
    "prompt-engineering-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Domain-specific prompt library (legal)", "A curated collection of prompt templates tailored to legal document analysis tasks"],
        ["Application", "Encodes domain expertise about legal terminology and document structure into reusable, tested prompt patterns"],
    ])},
    "prompt-engineering-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Domain-specific prompt library (clinical)", "A curated collection of prompt templates tailored to clinical text analysis tasks"],
        ["Application", "Must carefully account for clinical terminology and the high-stakes accuracy requirements of medical text"],
    ])},
    "prompt-engineering-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Financial document analysis prompting", "Designs prompts tailored to extracting and analyzing information from financial documents"],
        ["Application", "Must account for financial terminology, numerical precision, and the structured nature of financial reports"],
    ])},
    "prompt-engineering-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Scientific literature summarization prompting", "Designs prompts for accurately condensing complex scientific papers"],
        ["Application", "Must balance conciseness against preserving critical methodological and result details accurately"],
    ])},
    "prompt-engineering-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Prompt-based data augmentation", "Uses a model to generate additional synthetic training examples via prompting"],
        ["Fine-tuning application", "Can expand a limited training dataset, though risks amplifying existing model biases if not carefully curated"],
    ])},
    "prompt-engineering-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Prompted behavior distillation", "Fine-tunes a model to reproduce behavior originally elicited through careful prompting, without needing the prompt at inference time"],
        ["Application", "Bakes an effective prompting strategy's behavior directly into model weights, reducing per-request prompt overhead"],
    ])},
    "prompt-engineering-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional prompting", "Prompts a model to evaluate its outputs against a written set of principles for harm reduction"],
        ["Application", "Encodes safety guidance directly into the prompting process rather than relying solely on training-time alignment"],
    ])},
    "prompt-engineering-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Hallucination mitigation (prompt-level)", "Prompting strategies that reduce a model's tendency to generate confident but false content"],
        ["Technique", "Includes instructing the model to cite sources, express uncertainty, or verify claims before finalizing an answer"],
    ])},
    "prompt-engineering-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Abstention", "A model declines to answer when it lacks sufficient confidence or information"],
        ["Refusal calibration", "Tunes how readily a model abstains, balancing the cost of unhelpful over-refusal against the risk of confidently wrong answers"],
    ])},
    "prompt-engineering-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent negotiation prompting", "Designs prompts enabling multiple model agents to negotiate toward a mutually acceptable outcome"],
        ["Application", "Must specify each agent's goals and constraints clearly enough to produce coherent, purposeful negotiation behavior"],
    ])},
    "prompt-engineering-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Cooperative task allocation prompting", "Prompts multiple agents to divide a shared task efficiently among themselves"],
        ["Application", "Requires coordination mechanisms within the prompts to avoid duplicated or conflicting agent efforts"],
    ])},
    "prompt-engineering-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Simulated social agent prompting", "Designs prompts for models role-playing agents within a simulated social environment"],
        ["Application", "Used in research settings to study emergent social dynamics among interacting language model agents"],
    ])},
    "prompt-engineering-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Temporal consistency prompting", "Maintains a coherent timeline and consistent details across a long generated narrative"],
        ["Long narrative application", "Prevents contradictions (like character ages or event ordering) from accumulating over extended generated text"],
    ])},
    "prompt-engineering-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Counterfactual reasoning prompting", "Prompts a model to reason about hypothetical alternatives to what actually occurred"],
        ["Application", "Requires the model to correctly hold certain facts fixed while varying the specific counterfactual condition"],
    ])},
    "prompt-engineering-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Analogical reasoning prompt design", "Structures prompts that guide a model to solve a new problem by mapping it onto a structurally similar known problem"],
        ["Application", "Leverages the model's ability to recognize structural correspondence between superficially different problems"],
    ])},
    "prompt-engineering-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Causal inference query prompting", "Designs prompts asking a model to reason about cause-and-effect relationships rather than mere correlation"],
        ["Application", "Explicit prompting can help distinguish causal claims from the purely correlational patterns a model might otherwise conflate"],
    ])},
    "prompt-engineering-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Mathematical proof generation prompting", "Guides a model to produce rigorous, multi-step mathematical proofs"],
        ["Application", "Benefits from explicit step-by-step structuring and prompting the model to justify each logical step"],
    ])},
    "prompt-engineering-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Self-refine", "A model iteratively critiques and improves its own output across multiple rounds without external feedback"],
        ["Iterative improvement loop", "Repeated self-critique cycles can incrementally improve output quality up to a point of diminishing returns"],
    ])},
    "prompt-engineering-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Prompt chaining", "Connects the output of one prompted call as input to a subsequent prompted call, forming a multi-step pipeline"],
        ["Composability framework", "Well-designed chains break complex tasks into smaller, more reliable individual prompting steps"],
    ])},
    "prompt-engineering-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Declarative prompt programming", "Specifies desired outcomes and constraints rather than the exact step-by-step prompting logic to achieve them"],
        ["Paradigm", "Shifts prompt engineering toward higher-level frameworks that compile declarative specifications into concrete prompt chains"],
    ])},
    "prompt-engineering-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Prompt optimization via RL from feedback", "Uses reinforcement learning techniques to automatically improve a prompt based on observed outcome feedback"],
        ["Application", "Treats the prompt itself as an optimizable parameter guided by a reward signal derived from output quality"],
    ])},
    "prompt-engineering-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Active learning (prompt examples)", "Selectively chooses which examples to include in a few-shot prompt to maximize their informativeness"],
        ["Prompt example selection", "Prioritizes examples expected to be most helpful for the model's current performance gaps, rather than random selection"],
    ])},
    "prompt-engineering-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Semantic similarity retrieval", "Selects few-shot examples most semantically similar to the current query rather than using a fixed static example set"],
        ["Dynamic few-shot prompting", "Tailors the specific examples shown to each individual query, often improving performance over a fixed example set"],
    ])},
    "prompt-engineering-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Curriculum design (evaluation suite)", "Structures a prompt evaluation suite with tasks ordered from simpler to more challenging"],
        ["Application", "Reveals not just whether a model succeeds but at what difficulty level its performance begins to degrade"],
    ])},
    "prompt-engineering-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving query prompting", "Designs prompts that minimize exposure of sensitive information when interacting with a model"],
        ["Application", "May involve redacting or abstracting identifying details before including them in a prompt sent to an external model"],
    ])},
    "prompt-engineering-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy in prompt logging", "Applies formal privacy guarantees when storing or analyzing logs of user prompts"],
        ["Consideration", "Balances the utility of logged prompt data for system improvement against the privacy risk to users who submitted it"],
    ])},
    "prompt-engineering-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Regulatory compliance auditing prompting", "Designs prompts to evaluate whether content or processes meet specific regulatory requirements"],
        ["Application", "Encodes specific regulatory criteria into structured prompts for consistent, scalable compliance checking"],
    ])},
    "prompt-engineering-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Explainability prompting", "Instructs a model to justify its decision or output with an accompanying explanation"],
        ["Decision justification application", "Helps users understand and evaluate a model's reasoning, though the stated explanation may not always faithfully reflect the true underlying process"],
    ])},
    "prompt-engineering-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Prompt engineering research methodology", "Rigorous experimental design and reporting standards for studying prompting techniques"],
        ["Reproducibility", "Requires precisely documenting exact prompt wording, model version, and evaluation conditions to enable replication"],
    ])},
    "prompt-engineering-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Benchmark contamination", "Occurs when benchmark evaluation data has leaked into a model's training set, inflating its apparent performance"],
        ["Prompt evaluation risk", "A significant concern that can make reported prompting technique improvements appear larger than they actually are"],
    ])},
    "prompt-engineering-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-draft prompting", "Prompts a model to generate minimal, concise intermediate reasoning steps rather than verbose chain-of-thought"],
        ["Efficient concise reasoning", "Aims to preserve chain-of-thought's accuracy benefits while substantially reducing token generation cost"],
    ])},
    "prompt-engineering-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Needle-in-a-haystack evaluation", "Tests whether a model can accurately retrieve a specific fact planted within a very long context"],
        ["Long-context prompt engineering", "Reveals how retrieval accuracy varies by the needle's position and the overall context length, informing long-context prompt design"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Prompt Engineering"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"prompt-engineering-m2-l{base_n}"
        worked_key = f"prompt-engineering-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Prompt Engineering lessons.")


if __name__ == "__main__":
    main()
