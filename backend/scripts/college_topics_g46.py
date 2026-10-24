"""
Top-up batch g46: fills remaining M2 lesson gaps for subjects that fell
slightly short of the 100-lesson minimum due to cross-level title
collisions in a previous mass-generation pass.

Each entry is a (title, summary) tuple. Titles are checked against each
subject's existing M2 titles in backend/syllabus/level_m2.json to avoid
duplication; topics favor specific, less-obvious sub-areas to minimize
accidental overlap with unseen topics at other levels (C1, C2, UG1-4, M1).
"""

MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "Biology": {
        "M2": [
            ("Metabolic Scaling Theory and the Physics of Biological Allometry", "Examines how organismal metabolic rate scales with body mass across taxa and the mechanistic models proposed to explain quarter-power scaling laws."),
        ],
    },
    "Chemistry": {
        "M2": [
            ("Photoelectrochemical Water Splitting Tandem Cell Design", "Explores the engineering of tandem photoelectrode architectures that pair light absorbers with catalytic junctions to achieve unassisted solar-driven water splitting."),
            ("Sonochemistry: Cavitation-Driven Reaction Mechanisms", "Investigates how acoustic cavitation generates transient extreme local conditions that drive otherwise inaccessible chemical transformations."),
        ],
    },
    "Critical Thinking": {
        "M2": [
            ("Bounded Rationality and Satisficing in Herbert Simon's Decision Theory", "Analyzes Simon's account of decision-making under cognitive and informational limits and its implications for models of rational choice."),
            ("The Paradox of the Preface and Rational Belief Sets", "Examines the tension between believing each individual claim in a body of work and believing that the work as a whole contains at least one error."),
            ("Argument by Analogy: Formal Models of Analogical Strength", "Surveys formal frameworks for evaluating when an analogical argument transfers justificatory force from a source case to a target case."),
            ("Epistemic Trespassing Across Disciplinary Boundaries", "Investigates the reliability problems that arise when experts in one field render confident judgments on questions belonging to another."),
        ],
    },
    "Cybersecurity": {
        "M2": [
            ("Voice Deepfake Detection for Vishing Attack Mitigation", "Covers acoustic and behavioral techniques for detecting synthetic voice impersonation used in social engineering and fraud campaigns."),
            ("Passwordless Authentication: FIDO2/WebAuthn Security Analysis", "Analyzes the cryptographic protocol design, phishing resistance, and deployment challenges of public-key-based passwordless authentication."),
        ],
    },
    "Economics": {
        "M2": [
            ("Mechanism Design and the Vickrey-Clarke-Groves Auction", "Studies how the VCG mechanism achieves truthful bidding and efficient allocation in multi-item auction and resource allocation settings."),
            ("Search and Matching Theory: The Diamond-Mortensen-Pissarides Model", "Examines the equilibrium search-and-matching framework used to model labor market frictions, vacancies, and unemployment dynamics."),
        ],
    },
    "English": {
        "M2": [
            ("Cognitive Narratology and Theory of Mind Attribution in Fiction", "Investigates how readers infer fictional characters' mental states and how narrative technique scaffolds theory-of-mind processing."),
            ("Linguistic Landscape Studies: Semiotics of Public Multilingual Signage", "Analyzes how language choice and placement on public signs encode power relations, identity, and language policy in multilingual spaces."),
            ("Slow Violence and Environmental Trauma in Contemporary Narrative", "Examines how literary form represents gradual, dispersed ecological harm that resists conventional narratives of catastrophe."),
        ],
    },
    "Finance": {
        "M2": [
            ("Market Microstructure of Cryptocurrency Exchanges: Order Book Dynamics", "Studies liquidity provision, price discovery, and order book behavior in centralized and decentralized cryptocurrency trading venues."),
            ("Green Swan Risk and Climate-Related Financial Stability", "Analyzes how climate-driven tail risks threaten systemic financial stability in ways that resist conventional risk modeling assumptions."),
        ],
    },
    "First Aid": {
        "M2": [
            ("Field Management of Traumatic Eye Injuries and Globe Rupture", "Covers prehospital assessment and stabilization protocols for open-globe injuries and other sight-threatening ocular trauma."),
        ],
    },
    "Foreign Languages": {
        "M2": [
            ("Basque Language Isolate: Ergative Morphosyntax", "Examines the ergative-absolutive alignment system and non-Indo-European grammatical structure of Basque as a linguistic isolate."),
            ("Quechua Grammatical Structure and Andean Language Contact", "Studies the agglutinative morphology of Quechua and its historical contact effects with Spanish and other Andean languages."),
        ],
    },
    "General Knowledge": {
        "M2": [
            ("The Voynich Manuscript: Decipherment Attempts and Historiographical Debates", "Surveys the history of scholarly attempts to decode the mysterious illustrated manuscript and the competing theories about its origin and meaning."),
        ],
    },
    "Geography": {
        "M2": [
            ("Urban Metabolism: Material and Energy Flow Analysis of Cities", "Applies industrial ecology methods to quantify the resource inputs, transformations, and waste outputs of urban systems."),
        ],
    },
    "Health Education": {
        "M2": [
            ("Precision Public Health: Multi-Omic Data for Targeted Interventions", "Explores how genomic, proteomic, and other molecular data streams are used to tailor population-level health interventions to subgroups."),
            ("Health Education Program Design for Refugee and Displaced Populations", "Examines the design and delivery of culturally responsive health education in humanitarian and forced-migration contexts."),
            ("Peer-Led Health Education Models: Design and Efficacy Evidence", "Reviews the theoretical basis and evaluation evidence for programs that train community members to deliver health education to peers."),
            ("Citizen Science Approaches in Community Health Surveillance", "Investigates how community-generated data collection contributes to public health surveillance and participatory health education."),
            ("Planetary Health Education: Linking Ecosystem and Human Wellbeing", "Examines curricula that frame human health outcomes as interdependent with the stability of Earth's natural systems."),
            ("Sleep Health Education and Circadian-Informed Public Health Curricula", "Covers the evidence base for incorporating circadian science into public health education on sleep, shift work, and chronic disease risk."),
            ("Menstrual Health Education Policy and Program Design", "Analyzes curriculum design, stigma reduction, and policy frameworks for menstrual health education programs."),
        ],
    },
    "ICT & Computer Science": {
        "M2": [
            ("Neuromorphic Computing Hardware Architectures for Spiking Neural Networks", "Examines brain-inspired hardware designs that implement spiking neuron models for energy-efficient, event-driven computation."),
        ],
    },
    "Islamic Studies": {
        "M2": [
            ("Comparative Study of Islamic Legal Schools' Approach to Custom (Urf)", "Examines how the major legal schools treat local custom as a subsidiary source of law and the limits placed on its authority."),
            ("Historical Development of Islamic Astronomy and Prayer-Time Determination", "Traces the development of astronomical instruments and calculation methods used historically to determine prayer times and the lunar calendar."),
            ("Sufi Music and Sama in Islamic Devotional Practice", "Explores the historical and theological debates surrounding musical and auditory practices within various Sufi devotional traditions."),
            ("Islamic Perspectives on Artificial Intelligence and Emerging Bioethical Frontiers", "Surveys contemporary scholarly engagement with questions raised by artificial intelligence, robotics, and other emerging technologies."),
            ("Muslim Minority Jurisprudence (Fiqh al-Aqalliyyat) in Non-Muslim Majority States", "Examines the modern jurisprudential framework developed to address the religious and legal needs of Muslim minority communities."),
        ],
    },
    "JavaScript": {
        "M2": [
            ("WebAssembly Component Model and Cross-Language Interoperability", "Examines the emerging component model standard for composing WebAssembly modules written in different source languages."),
            ("Advanced Import Assertions and JSON Module Loading Semantics", "Covers the specification and engine implementation details of type-asserted module imports for non-JavaScript resource types."),
            ("Formal Analysis of the Temporal Dead Zone in Lexical Scoping", "Provides a rigorous treatment of let/const binding initialization semantics and the scoping edge cases they introduce."),
        ],
    },
    "Math": {
        "M2": [
            ("Arithmetic Statistics and the Cohen-Lenstra Heuristics for Class Groups", "Studies the conjectural probabilistic model predicting the distribution of ideal class groups across families of number fields."),
        ],
    },
    "Music": {
        "M2": [
            ("Algorithmic Analysis of Voice Leading in Common-Practice Corpora", "Applies computational methods to large musical corpora to test and refine rules of voice leading derived from music theory."),
            ("Turntablism and DJ Practice as Compositional Method", "Examines turntable manipulation and live mixing as a distinct compositional and performative practice within contemporary music."),
        ],
    },
    "Natural Language Processing": {
        "M2": [
            ("Speech-to-Text Alignment and Forced Alignment Algorithms", "Covers algorithms that align transcribed text to audio at the phoneme or word level for speech corpus annotation and analysis."),
            ("Discourse Coherence Modeling with Entity Grid Representations", "Examines models that represent entity distribution across sentences to predict and evaluate local discourse coherence."),
            ("Neural Text Simplification for Accessibility Applications", "Studies sequence-to-sequence approaches for rewriting complex text into more accessible forms while preserving meaning."),
            ("Cross-Lingual Word Alignment for Low-Resource Bitext Mining", "Explores methods for aligning translated word pairs across languages to mine parallel text for low-resource machine translation."),
            ("Table-to-Text Generation and Structured Data Verbalization", "Covers neural architectures that generate fluent natural language descriptions from structured tabular or relational data."),
        ],
    },
    "Operations Management": {
        "M2": [
            ("Cold Chain Logistics Optimization for Pharmaceutical Distribution Networks", "Examines temperature-controlled supply chain design and optimization models for distributing perishable pharmaceutical products."),
            ("Humanitarian Relief Supply Chain Coordination Under Demand Surge", "Studies coordination mechanisms and inventory pre-positioning strategies for disaster relief logistics under sudden demand spikes."),
        ],
    },
    "Philosophy": {
        "M2": [
            ("Iris Murdoch's Moral Vision and the Sovereignty of Good", "Examines Murdoch's account of moral attention and the priority of perceiving reality accurately over rule-following in ethics."),
            ("Alasdair MacIntyre's After Virtue and the Critique of Enlightenment Morality", "Analyzes MacIntyre's argument that modern moral discourse is fragmented and his proposed return to a tradition-based virtue ethics."),
            ("Judith Jarvis Thomson's Violinist Argument in Applied Ethics", "Examines Thomson's influential thought experiment and its implications for arguments about bodily autonomy and moral obligation."),
            ("Thomas Nagel's The View from Nowhere and the Problem of Objectivity", "Studies Nagel's exploration of the tension between subjective, first-person experience and objective, detached understanding."),
            ("Michael Sandel's Communitarian Critique of Rawlsian Liberalism", "Examines Sandel's argument that Rawlsian liberalism presupposes an untenably unencumbered conception of the self."),
            ("Simone de Beauvoir's Existentialist Ethics of Ambiguity", "Explores Beauvoir's development of an existentialist ethics grounded in the ambiguity of human freedom and situatedness."),
        ],
    },
    "Physics": {
        "M2": [
            ("Casimir Effect and Quantum Vacuum Fluctuation Measurements", "Examines the theoretical origin and precision experimental measurement of the attractive force arising from quantum vacuum fluctuations between surfaces."),
        ],
    },
    "Project Management": {
        "M2": [
            ("Earned Schedule Method for Forecasting Project Completion", "Extends earned value management with a time-based metric that improves the accuracy of schedule forecasting on complex projects."),
            ("Organizational Project Management Maturity Model Assessment Frameworks", "Surveys frameworks used to assess and benchmark an organization's project management capability and process maturity."),
        ],
    },
    "Prompt Engineering": {
        "M2": [
            ("Chain-of-Draft Prompting for Efficient Concise Reasoning", "Examines prompting strategies that elicit terse intermediate reasoning steps to reduce token cost while preserving accuracy."),
            ("Prompt Engineering for Long-Context Needle-in-a-Haystack Evaluation", "Covers prompt design techniques for probing and improving a model's ability to retrieve specific facts embedded in very long contexts."),
        ],
    },
    "R": {
        "M2": [
            ("Advanced Survey Weighting and Calibration Estimation with the survey Package", "Covers calibration and raking methods for adjusting complex survey weights to match known population totals in R."),
        ],
    },
    "World Literature": {
        "M2": [
            ("Alice Munro's Short Story Cycles and the Architecture of Everyday Life", "Examines how Munro's interlinked short fiction builds cumulative narrative meaning out of ordinary domestic and rural experience."),
            ("José Saramago's Blindness and the Allegorical Dystopian Novel", "Analyzes Saramago's use of allegory and unconventional narrative voice to explore social collapse and moral responsibility."),
        ],
    },
}
