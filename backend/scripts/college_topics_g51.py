"""Absolute closing top-up: the last 4 lessons needed after all prior waves,
covering Machine Learning (UG2, needs 2), Natural Language Processing (UG2,
needs 1), and Philosophy (UG2, needs 1). Written directly rather than via
another agent dispatch, since the gap is trivially small.
"""

MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "Machine Learning": {
        "UG2": [
            ("The Elastic Weight Consolidation Method for Continual Learning", "Explains how this regularization technique lets a neural network learn new tasks sequentially without catastrophically forgetting earlier ones."),
        ],
    },
    "Natural Language Processing": {
        "UG2": [
            ("The Chomsky Hierarchy and Formal Grammar Classes in Parsing", "Covers how regular, context-free, and context-sensitive grammar classes shape the design and limits of parsing algorithms."),
        ],
    },
    "Philosophy": {
        "UG2": [
            ("The Sorites Paradox and the Problem of Vagueness", "Examines the paradox of the heap and what it reveals about vague predicates, borderline cases, and the logic of imprecise language."),
        ],
    },
}
