#!/usr/bin/env python3
"""Depth pass, M2 Natural Language Processing: fill in real,
hand-checked data_table content for the M2 Natural Language Processing
lessons not covered by the earlier breadth-first batch. Brings M2
Natural Language Processing to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning tokenizer
and architecture internals, alignment/RLHF, reasoning and retrieval,
information extraction, multilingual/low-resource NLP, interpretability
and safety, efficient fine-tuning/inference, and applied NLP
(biomedical, legal, dialogue, generation); l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_natural_language_processing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Byte Pair Encoding (BPE)", "Iteratively merges the most frequent adjacent symbol pair to build a subword vocabulary"],
    ["WordPiece", "Similar to BPE but chooses merges that maximize training data likelihood rather than raw frequency"],
])

CHARTS: dict[str, dict] = {
    "natural-language-processing-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["NLP ethics", "Considers the societal impact of language technology, including consent, representation, and misuse potential"],
        ["Bias in NLP", "Systematic skew in model outputs favoring or disadvantaging particular groups, often inherited from training data"],
    ])},
    "natural-language-processing-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["NLP research methods", "Rigorous experimental design, ablation studies, and statistically sound comparison against baselines"],
        ["Capstone framing", "A graduate NLP capstone should isolate one clear research question and test it with controlled comparisons"],
    ])},
    "natural-language-processing-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Positional encoding", "Injects information about token order into a transformer, which otherwise treats tokens as an unordered set"],
        ["Rotary encoding", "A widely used scheme that encodes position by rotating query/key vectors, generalizing well to longer sequences"],
    ])},
    "natural-language-processing-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Sparse attention", "Restricts each token to attend to only a subset of other tokens, reducing quadratic attention cost"],
        ["Linear attention", "Reformulates attention to scale linearly with sequence length, trading some expressivity for efficiency"],
    ])},
    "natural-language-processing-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Mixture-of-experts routing", "A gating network decides which sparse subset of expert subnetworks processes each token"],
        ["Sparse language model", "Increases total parameter count while keeping per-token compute roughly constant"],
    ])},
    "natural-language-processing-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Multi-query attention", "Shares a single key/value projection across all attention heads, reducing memory bandwidth at inference"],
        ["Grouped-query attention", "A middle ground sharing key/value projections across small groups of heads, balancing speed and quality"],
    ])},
    "natural-language-processing-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Speculative decoding", "A small draft model proposes several tokens which a larger model verifies in parallel, speeding up generation"],
        ["Accelerated inference", "Exploits the fact that verifying proposed tokens is cheaper than generating them autoregressively one at a time"],
    ])},
    "natural-language-processing-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["KV-cache", "Stores previously computed attention keys and values to avoid recomputing them at each new generation step"],
        ["Cache compression", "Reduces the KV-cache's memory footprint, which otherwise grows linearly with context length"],
    ])},
    "natural-language-processing-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional AI", "Trains a model to critique and revise its own outputs against a written set of principles"],
        ["Preference-free alignment", "Reduces reliance on large volumes of human preference labels by encoding guidance as explicit rules"],
    ])},
    "natural-language-processing-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Direct preference optimization", "Fine-tunes a model directly on preference data using a closed-form loss, without training a separate reward model"],
        ["Language model alignment", "Simplifies the RLHF pipeline by removing the reinforcement learning step and its associated instability"],
    ])},
    "natural-language-processing-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Reward model", "A model trained to predict human preference scores from pairwise comparisons of language model outputs"],
        ["RLHF failure mode", "A miscalibrated or exploitable reward model can be gamed by the policy without truly satisfying human intent"],
    ])},
    "natural-language-processing-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Reward hacking", "The model finds a way to score highly on the learned reward model without genuinely satisfying human intent"],
        ["Specification gaming", "A broader term for optimizing literally against a stated objective in a way that violates its intended spirit"],
    ])},
    "natural-language-processing-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought prompting", "Prompts a model to generate intermediate reasoning steps before its final answer"],
        ["Emergent reasoning", "The benefit of chain-of-thought prompting tends to grow with model scale, appearing weakly or not at all in smaller models"],
    ])},
    "natural-language-processing-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Self-consistency", "Samples multiple reasoning paths and takes the majority answer, improving robustness over a single greedy decode"],
        ["Ensemble reasoning", "Combines multiple independent reasoning attempts to reduce the impact of any single flawed reasoning chain"],
    ])},
    "natural-language-processing-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Tree-of-thought", "Generalizes chain-of-thought into a search tree of partial reasoning paths that can be expanded, evaluated, and pruned"],
        ["Search-based reasoning", "Applies classical search algorithms to explore multiple candidate reasoning trajectories rather than one linear chain"],
    ])},
    "natural-language-processing-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Tool-augmented language model", "A model calls external tools (calculators, search, code execution) to solve parts of a problem it can't solve internally"],
        ["Function calling", "A structured interface letting the model invoke external functions with typed arguments and receive their results"],
    ])},
    "natural-language-processing-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Dense passage retrieval", "Retrieves relevant documents by comparing dense vector embeddings of the query and candidate passages"],
        ["Retrieval-augmented generation", "Conditions a language model's output on documents retrieved from an external knowledge source"],
    ])},
    "natural-language-processing-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Fusion-in-decoder", "Encodes each retrieved passage separately, then fuses information across all of them within the decoder"],
        ["Architecture benefit", "Scales to using many retrieved passages without the quadratic cost of concatenating them all into one encoder input"],
    ])},
    "natural-language-processing-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical attention", "Applies attention at multiple granularities (e.g. sentence-level then document-level) to manage long inputs"],
        ["Long-document summarization", "Must condense information spread across many more tokens than a model's local attention window can directly compare"],
    ])},
    "natural-language-processing-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Faithfulness", "Whether a generated summary's claims are actually supported by the source document"],
        ["Hallucination detection", "Automated methods to flag generated content not grounded in or contradicted by the source text"],
    ])},
    "natural-language-processing-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Factual consistency metric", "An automated score estimating whether a generated text's claims align with a reference or source document"],
        ["Evaluation challenge", "Correlating automated metrics with human judgments of factual accuracy remains an open research problem"],
    ])},
    "natural-language-processing-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Named entity recognition", "Identifies and classifies spans of text referring to entities such as people, organizations, or locations"],
        ["Nested and discontinuous spans", "Handles entities that overlap or are split by other text, which standard flat-span tagging schemes cannot represent"],
    ])},
    "natural-language-processing-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Coreference resolution", "Identifies which mentions in a text refer to the same real-world entity"],
        ["End-to-end neural model", "Jointly scores mention detection and coreference linking within a single trained model, rather than separate pipeline stages"],
    ])},
    "natural-language-processing-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Semantic role labeling", "Identifies who did what to whom by labeling the semantic roles of sentence constituents relative to a predicate"],
        ["Predicate-argument structure", "The underlying representation of an event and its participants that semantic role labeling aims to recover"],
    ])},
    "natural-language-processing-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Universal Dependencies", "A cross-linguistically consistent grammatical annotation scheme used to compare syntax across many languages"],
        ["Cross-lingual parsing", "Trains or transfers syntactic parsers across languages using this shared annotation framework"],
    ])},
    "natural-language-processing-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Constituency parsing", "Recovers the hierarchical phrase structure of a sentence"],
        ["Chart-based model", "Uses dynamic programming over a chart of possible sub-parses to efficiently find the best overall parse"],
    ])},
    "natural-language-processing-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Cross-document coreference", "Links mentions of the same entity across multiple separate documents, not just within one"],
        ["Entity linking at scale", "Requires efficient candidate retrieval and disambiguation methods to handle large document collections"],
    ])},
    "natural-language-processing-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge graph embedding", "Represents entities and relations as vectors such that graph structure is preserved in vector space"],
        ["Link prediction", "Uses the learned embeddings to infer missing or likely relations between entities in the graph"],
    ])},
    "natural-language-processing-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Entity linking", "Maps an ambiguous textual mention to the correct entry in a knowledge base"],
        ["Contextualized candidate ranking", "Uses the surrounding context to rank plausible knowledge-base candidates for an ambiguous mention"],
    ])},
    "natural-language-processing-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Relation extraction", "Identifies semantic relationships between entity pairs mentioned in text"],
        ["Distant supervision", "Automatically generates noisy training labels by aligning text with facts from an existing knowledge base"],
    ])},
    "natural-language-processing-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Open information extraction", "Extracts relational facts from text without a predefined schema of relation types"],
        ["Unstructured text", "Must discover both the relation type and its arguments directly from free-form sentences"],
    ])},
    "natural-language-processing-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Neural machine translation", "Translates text using an end-to-end trained neural network rather than rule-based or statistical phrase methods"],
        ["Attention and alignment", "Attention weights in NMT often approximately correspond to word alignments between source and target sentences"],
    ])},
    "natural-language-processing-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Low-resource translation", "Building translation systems for language pairs with limited parallel training data"],
        ["Cross-lingual transfer", "Leverages knowledge from high-resource languages to improve translation quality for low-resource ones"],
    ])},
    "natural-language-processing-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Unsupervised machine translation", "Learns to translate without any parallel sentence pairs, using only monolingual corpora"],
        ["Weakly supervised translation", "Uses limited or noisy parallel signal to improve upon a purely unsupervised starting point"],
    ])},
    "natural-language-processing-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Multilingual pretraining", "Trains a single language model on text from many languages simultaneously"],
        ["Pretraining strategy", "Choices like language sampling ratios and shared vocabulary size significantly affect cross-lingual performance balance"],
    ])},
    "natural-language-processing-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual transfer learning", "Applies knowledge learned in one language to improve performance in another"],
        ["Zero-shot generalization", "A model performs a task in a language it saw no task-specific labeled examples for, using only its multilingual pretraining"],
    ])},
    "natural-language-processing-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Code-switching", "Text or speech that alternates between two or more languages within a single utterance or document"],
        ["Mixed-language processing", "Requires models robust to vocabulary and grammar shifts occurring mid-sentence"],
    ])},
    "natural-language-processing-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Morphologically rich language", "A language where words carry extensive grammatical information through inflection, producing very large vocabularies"],
        ["Processing challenge", "Standard word-level tokenization struggles with the combinatorial explosion of possible word forms"],
    ])},
    "natural-language-processing-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Low-resource language", "A language with limited digital text data available for training NLP models"],
        ["Endangered language computation", "Faces the added challenge of very small or shrinking speaker communities and scarce documentation"],
    ])},
    "natural-language-processing-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Word sense disambiguation", "Determines which meaning of an ambiguous word is intended in a given context"],
        ["Contextual embedding", "Modern embeddings assign different vector representations to the same word depending on its surrounding context"],
    ])},
    "natural-language-processing-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Lexical semantics", "Studies the meaning of words and the relationships between them"],
        ["Distributional hypothesis", "The foundational idea that words appearing in similar contexts tend to have similar meanings"],
    ])},
    "natural-language-processing-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Contextualized word embedding", "A word representation that varies depending on the surrounding sentence, unlike static embeddings"],
        ["ELMo to modern encoders", "ELMo pioneered contextual embeddings via bidirectional LSTMs, later superseded by transformer-based encoders"],
    ])},
    "natural-language-processing-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Probing classifier", "A simple classifier trained on frozen model representations to test what linguistic information they encode"],
        ["Interpreting representations", "A high probing accuracy suggests the underlying information is linearly recoverable from the model's representations"],
    ])},
    "natural-language-processing-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Mechanistic interpretability", "Reverse-engineers a trained network's weights into human-understandable algorithms"],
        ["Circuit", "A minimal subgraph of connected components (attention heads, neurons) implementing a specific computation"],
    ])},
    "natural-language-processing-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Sparse autoencoder", "Decomposes a network's dense internal activations into a larger set of sparse, more interpretable features"],
        ["Interpretable feature discovery", "Aims to recover individually meaningful concepts from otherwise entangled, superposed representations"],
    ])},
    "natural-language-processing-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Activation patching", "Replaces a specific internal activation during a forward pass to test its causal effect on the model's output"],
        ["Causal tracing", "Systematically patches activations at different locations to localize where a specific computation happens in the network"],
    ])},
    "natural-language-processing-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge editing", "Directly modifies a specific fact stored in a trained model's weights"],
        ["Fact correction technique", "Aims to change one fact without degrading unrelated model behavior elsewhere"],
    ])},
    "natural-language-processing-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Membership inference attack", "Determines whether a specific text was part of a model's training set from its output behavior"],
        ["Training data extraction", "More aggressive attacks that attempt to recover verbatim training examples directly from a model's outputs"],
    ])},
    "natural-language-processing-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Differentially private training", "Bounds how much any single training example can influence the final model's parameters"],
        ["Privacy-utility trade-off", "Stronger privacy guarantees generally come at the cost of somewhat reduced model quality"],
    ])},
    "natural-language-processing-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial robustness (NLP)", "A model's ability to maintain correct predictions under small, adversarially crafted textual perturbations"],
        ["Textual perturbation", "Includes character swaps, synonym substitutions, and paraphrasing designed to fool the model while preserving meaning"],
    ])},
    "natural-language-processing-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Jailbreaking", "Crafting inputs designed to bypass a model's safety training and elicit disallowed behavior"],
        ["Prompt injection", "Embedding malicious instructions within input data to hijack a model's intended behavior"],
    ])},
    "natural-language-processing-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Watermarking", "Embeds a statistically detectable signal into a generative model's output for later identification"],
        ["Machine-generated text detection", "Watermarks aim to be robust to light editing while remaining invisible to a human reader"],
    ])},
    "natural-language-processing-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Machine-generated text detection at scale", "Classifiers or statistical tests that distinguish AI-generated from human-written text across large volumes"],
        ["Robustness challenge", "Detection reliability tends to degrade as generative models improve and text is lightly edited"],
    ])},
    "natural-language-processing-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Toxicity measurement", "Quantifies harmful, offensive, or abusive content in a language model's generated outputs"],
        ["Bias measurement", "Assesses systematic differences in model outputs across demographic groups referenced in the input"],
    ])},
    "natural-language-processing-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Debiasing technique", "Methods that reduce unwanted stereotypical associations encoded in word or sentence embeddings"],
        ["Embedding debiasing", "Common approaches project out or neutralize a learned bias direction within the embedding space"],
    ])},
    "natural-language-processing-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Fairness-aware evaluation", "Measures a model's performance separately across demographic subgroups to detect disparities"],
        ["Cross-demographic evaluation", "Aggregate accuracy can mask substantial performance gaps for specific groups"],
    ])},
    "natural-language-processing-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional classifier", "A classifier trained to flag content violating a written set of policy principles, used for moderation"],
        ["Real-time content moderation", "Must operate with low latency to filter or flag harmful content as it is generated or posted"],
    ])},
    "natural-language-processing-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning", "A model adapts its behavior to new task examples given in its prompt, without any parameter updates"],
        ["Theoretical limitation", "Performance can be sensitive to example order, formatting, and the specific examples chosen, unlike stable weight updates"],
    ])},
    "natural-language-processing-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Instruction tuning", "Fine-tunes a model on a diverse set of tasks phrased as natural language instructions"],
        ["Multi-task generalization", "Improves a model's ability to follow novel instructions it was not explicitly trained on"],
    ])},
    "natural-language-processing-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["LoRA", "Low-rank adaptation fine-tunes a model by learning small low-rank update matrices rather than all original weights"],
        ["Parameter-efficient fine-tuning", "Achieves strong task performance while updating only a small fraction of the model's parameters"],
    ])},
    "natural-language-processing-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Prompt engineering", "The practice of designing input prompts to elicit desired behavior from a language model"],
        ["Formal optimization framing", "Treats prompt design as a search problem over the space of possible input text, sometimes automated"],
    ])},
    "natural-language-processing-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Soft prompting", "Learns a small set of continuous embedding vectors prepended to the input, rather than discrete text tokens"],
        ["Prefix tuning", "Learns task-specific continuous vectors inserted at each transformer layer, keeping the base model frozen"],
    ])},
    "natural-language-processing-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Model distillation", "Trains a smaller student model to mimic a larger teacher model's output distribution"],
        ["Compact deployment", "Enables running capable language models under tighter memory and latency budgets"],
    ])},
    "natural-language-processing-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Quantization", "Reduces the numerical precision of a model's weights and activations to shrink memory and compute cost"],
        ["Efficient inference", "Enables running large language models on hardware with limited memory using lower-bit-width representations"],
    ])},
    "natural-language-processing-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Structured pruning", "Removes entire structural units (attention heads, layers) rather than individual weights"],
        ["Transformer compression", "Yields a smaller dense model that runs faster on standard hardware without specialized sparse-matrix support"],
    ])},
    "natural-language-processing-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Continual learning", "Trains a model on a sequence of tasks over time without access to all past data at once"],
        ["Catastrophic forgetting", "Learning a new task can overwrite parameters important for previously learned capabilities"],
    ])},
    "natural-language-processing-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Machine unlearning", "Removes the influence of specific training examples from a trained model without full retraining"],
        ["Data removal", "Motivated by privacy regulations granting individuals the right to have their data's influence deleted"],
    ])},
    "natural-language-processing-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Evaluation benchmark design", "Constructing standardized task suites that reliably measure a targeted model capability"],
        ["Contamination detection", "Identifies whether benchmark data leaked into a model's training set, which would inflate reported scores"],
    ])},
    "natural-language-processing-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Model calibration", "The alignment between a model's predicted confidence and its actual accuracy"],
        ["Confidence estimate", "A well-calibrated model's stated probability should match its empirical correctness rate across many predictions"],
    ])},
    "natural-language-processing-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Uncertainty quantification", "Estimates how confident a model's generated output should be treated as"],
        ["Neural text generation", "Uncertainty is harder to quantify for open-ended generation than for fixed-label classification"],
    ])},
    "natural-language-processing-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Dialogue state tracking", "Maintains a structured representation of user goals and constraints across a multi-turn conversation"],
        ["Task-oriented system", "Uses the tracked state to determine what information is still needed to fulfill the user's request"],
    ])},
    "natural-language-processing-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Vision-language pretraining", "Trains a model jointly on paired image and text data to learn cross-modal representations"],
        ["Cross-modal alignment", "Optimizes matched image-text pairs to be more similar in embedding space than mismatched pairs"],
    ])},
    "natural-language-processing-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal chain-of-thought", "Extends step-by-step reasoning to inputs combining text with images or other modalities"],
        ["Cross-modal reasoning", "Requires integrating visual and textual evidence coherently across the reasoning steps"],
    ])},
    "natural-language-processing-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Compositional generalization", "A model's ability to correctly handle novel combinations of components it has only seen individually"],
        ["Sequence model challenge", "Many neural sequence models struggle to systematically generalize compositions beyond training combinations"],
    ])},
    "natural-language-processing-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Formal language theory", "Studies classes of languages (regular, context-free, etc.) and the automata that recognize them"],
        ["Transformer expressivity", "Analyzes which formal language classes a transformer architecture can, in principle, represent or recognize"],
    ])},
    "natural-language-processing-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Targeted syntactic evaluation", "Tests a model on carefully constructed minimal sentence pairs that isolate a single grammatical phenomenon"],
        ["Syntactic generalization", "Reveals whether a model has learned an underlying grammatical rule or merely surface statistical patterns"],
    ])},
    "natural-language-processing-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Pragmatics", "Studies how context contributes to meaning beyond the literal content of an utterance"],
        ["Implicature", "Meaning that is implied by an utterance without being explicitly stated"],
    ])},
    "natural-language-processing-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Rational speech act model", "Models pragmatic reasoning as a recursive process of listeners and speakers reasoning about each other's beliefs and goals"],
        ["Pragmatic reasoning", "Formalizes how a cooperative speaker chooses utterances a rational listener would correctly interpret"],
    ])},
    "natural-language-processing-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Sentiment analysis", "Classifies the emotional polarity or attitude expressed in a piece of text"],
        ["Fine-grained aspect extraction", "Identifies sentiment toward specific aspects or attributes within a text, not just an overall polarity"],
    ])},
    "natural-language-processing-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Stance detection", "Determines whether a piece of text expresses support, opposition, or neutrality toward a given target"],
        ["Argument mining", "Automatically identifies argumentative components and their relationships within social or persuasive text"],
    ])},
    "natural-language-processing-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Misinformation detection", "Automated methods for identifying text likely to contain false or misleading claims"],
        ["Fake news modeling", "Combines linguistic, source-credibility, and propagation-pattern signals to flag likely misinformation"],
    ])},
    "natural-language-processing-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Grammatical error correction", "Automatically detects and corrects grammatical mistakes in a piece of text"],
        ["Sequence-to-sequence approach", "Treats correction as translating an erroneous sentence into its corrected form"],
    ])},
    "natural-language-processing-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Text-to-SQL", "Translates a natural language question into an executable database query"],
        ["Semantic parsing", "The broader task of converting natural language into a formal, machine-executable meaning representation"],
    ])},
    "natural-language-processing-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Neural program synthesis", "Automatically generates source code that satisfies a given natural language specification"],
        ["Specification-driven generation", "Must bridge the ambiguity of natural language with the precision required by executable code"],
    ])},
    "natural-language-processing-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Legal text analytics", "Applies NLP methods to analyze contracts, statutes, and case law"],
        ["Contract clause extraction", "Automatically identifies and classifies specific clause types within lengthy legal documents"],
    ])},
    "natural-language-processing-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Biomedical named entity recognition", "Identifies mentions of genes, diseases, drugs, and other biomedical entities in scientific text"],
        ["Relation extraction (biomedical)", "Identifies relationships between biomedical entities, such as drug-disease interactions"],
    ])},
    "natural-language-processing-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Clinical note understanding", "Extracts structured information from unstructured clinical documentation"],
        ["De-identification", "Automatically removes personally identifiable information from clinical text to protect patient privacy"],
    ])},
    "natural-language-processing-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Scientific literature mining", "Automatically extracts structured knowledge from the scientific publication corpus"],
        ["Automated claim extraction", "Identifies specific factual or experimental claims made within a scientific paper"],
    ])},
    "natural-language-processing-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Conversational agent safety alignment", "Ensures a dialogue system's responses remain helpful, honest, and harmless across varied user inputs"],
        ["Red-teaming", "Deliberately probes a system with adversarial inputs to discover safety failures before deployment"],
    ])},
    "natural-language-processing-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Scalable oversight", "Techniques for humans to reliably supervise AI systems whose capabilities exceed direct human evaluation"],
        ["Weak-to-strong generalization", "Studies whether a strong model trained on labels from a weaker supervisor can still learn to exceed the supervisor's own performance"],
    ])},
    "natural-language-processing-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Agentic language model planning", "A model decomposes a complex goal into a sequence of executable sub-steps"],
        ["Multi-step task execution", "Requires maintaining state and adapting the plan as intermediate steps succeed or fail"],
    ])},
    "natural-language-processing-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Memory architecture", "A mechanism letting a conversational agent store and retrieve information across a long interaction"],
        ["Long-horizon conversational agent", "Must manage limited context windows by summarizing or selectively retrieving past conversation history"],
    ])},
    "natural-language-processing-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Nucleus sampling", "Samples the next token from the smallest set of high-probability candidates whose cumulative probability exceeds a threshold"],
        ["Contrastive search", "A decoding strategy that balances output likelihood against representation diversity to reduce repetitive generation"],
    ])},
    "natural-language-processing-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Master's thesis research seminar", "A forum for presenting and defending an original NLP research contribution to faculty and peers"],
        ["NLP research", "Emphasizes a clearly stated hypothesis, appropriate baselines, and a rigorous experimental evaluation"],
    ])},
    "natural-language-processing-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Speech-to-text alignment", "Determines the precise timing correspondence between spoken audio and its transcribed text"],
        ["Forced alignment", "Given a known transcript, algorithmically aligns each word or phoneme to its exact position in the audio"],
    ])},
    "natural-language-processing-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Discourse coherence", "The property of a text being logically connected and easy to follow across sentences"],
        ["Entity grid representation", "Models coherence by tracking how entities are referenced across successive sentences"],
    ])},
    "natural-language-processing-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Neural text simplification", "Automatically rewrites text to be easier to read while preserving its core meaning"],
        ["Accessibility application", "Supports readers with lower literacy levels, language learners, or cognitive accessibility needs"],
    ])},
    "natural-language-processing-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual word alignment", "Identifies which words in a source sentence correspond to which words in its translation"],
        ["Low-resource bitext mining", "Automatically discovers parallel sentence pairs across languages with limited existing parallel data"],
    ])},
    "natural-language-processing-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Table-to-text generation", "Automatically generates natural language descriptions from structured tabular data"],
        ["Structured data verbalization", "Must faithfully convert precise structured values into fluent, accurate natural language statements"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Natural Language Processing"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"natural-language-processing-m2-l{base_n}"
        worked_key = f"natural-language-processing-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Natural Language Processing lessons.")


if __name__ == "__main__":
    main()
