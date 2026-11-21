"""
Final top-up batch (Group 50) of college syllabus lesson tuples.

Each subject/level pair below adds a small number of new, narrowly-scoped
(title, summary) tuples that do not duplicate any existing lesson title
already present in that subject's list at that specific level.
"""

MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "Natural Language Processing": {
        "UG2": [
            ("The Winograd Schema Challenge", "An undergraduate survey of the pronoun-resolution benchmark designed to test commonsense reasoning beyond simple statistical cues."),
            ("SHRDLU and Early Natural Language Understanding Systems", "An examination of Terry Winograd's 1970s blocks-world program and what its narrow success revealed about the limits of rule-based language understanding."),
            ("The ALPAC Report and the 1966 NLP Funding Winter", "A study of the influential U.S. government report that curtailed machine translation funding and reshaped the direction of language technology research."),
            ("WordNet and Lexical Database Design", "An introduction to how WordNet organizes words into synsets linked by semantic relations, and its role in early NLP systems."),
        ],
    },
    "Machine Learning": {
        "UG2": [
            ("The Netflix Prize and Collaborative Filtering Breakthroughs", "A case study of the 2006-2009 competition that popularized matrix factorization and ensemble methods for recommendation systems."),
            ("Conformal Prediction for Uncertainty Quantification", "An introduction to the distribution-free framework for producing prediction sets with guaranteed coverage from any machine learning model."),
            ("The ImageNet Moment: AlexNet and the 2012 Deep Learning Breakthrough", "An analysis of how AlexNet's 2012 ImageNet victory demonstrated the practical power of deep convolutional networks trained on GPUs."),
        ],
    },
    "Economics": {
        "UG2": [
            ("The Panic of 1837 and the Free Banking Era", "An examination of the antebellum American financial crisis triggered by speculative lending and its effect on state banking policy."),
            ("The Diamond-Water Paradox and the Marginal Revolution", "A study of why water is cheap and diamonds expensive despite water's greater use-value, and how marginal utility theory resolved the paradox."),
            ("The Beer Game and the Bullwhip Effect in Supply Chains", "An introduction to the classic MIT simulation showing how small demand fluctuations amplify into large inventory swings up a supply chain."),
        ],
        "UG4": [
            ("The Assignat Hyperinflation of Revolutionary France", "A senior-level case study of how paper currency backed by confiscated church land collapsed into hyperinflation during the French Revolution."),
        ],
    },
    "Artificial Intelligence": {
        "UG2": [
            ("The Dartmouth Workshop of 1956 and the Founding of AI", "An account of the summer workshop where the term 'artificial intelligence' was coined and the field's founding research agenda was set."),
        ],
    },
    "Philosophy": {
        "UG2": [
            ("The Ship of Theseus and Identity Over Time", "An exploration of the classic thought experiment questioning whether an object that has had all its parts replaced remains the same object."),
        ],
    },
    "World Literature": {
        "UG2": [
            ("Naguib Mahfouz and the Cairo Trilogy", "A study of the Egyptian Nobel laureate's multigenerational saga and its portrayal of Egyptian society under British occupation and beyond."),
        ],
    },
    "Physics": {
        "UG2": [
            ("The Stern-Gerlach Experiment and Quantized Spin", "An analysis of the 1922 experiment that demonstrated space quantization of angular momentum and provided early evidence for electron spin."),
        ],
    },
    "Critical Thinking": {
        "UG2": [
            ("The Abilene Paradox and Mismanaged Agreement", "An examination of how groups can collectively decide on a course of action that contradicts what every individual member actually prefers."),
        ],
    },
    "World History": {
        "UG3": [
            ("The Sykes-Picot Agreement and the Partitioning of the Middle East", "An advanced study of the secret 1916 Anglo-French accord that shaped modern Middle Eastern borders and its lasting geopolitical consequences."),
        ],
    },
    "General Knowledge": {
        "UG3": [
            ("The Voynich Manuscript: History's Undeciphered Text", "An advanced look at the mysterious illustrated codex written in an unknown script that has resisted centuries of decipherment attempts."),
        ],
    },
    "Prompt Engineering": {
        "UG4": [
            ("DSPy and Programmatic Prompt Optimization Pipelines", "A senior-level introduction to the DSPy framework for treating prompts as optimizable programs rather than hand-tuned strings."),
        ],
    },
}
