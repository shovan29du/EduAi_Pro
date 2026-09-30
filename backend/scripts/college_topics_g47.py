MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "AI Tools": {
        "UG2": [
            ("AI Tools for Genealogy Record Transcription", "Explores how AI handwriting and OCR tools help genealogists transcribe historical civil and church records at scale."),
            ("AI Tools for Sommelier and Tasting Note Generation", "Examines AI tools that draft structured tasting notes and pairing suggestions from wine and food sensory descriptors."),
        ],
    },
    "Art": {
        "UG2": [
            ("Marbling (Ebru) and Suminagashi Paper Art Techniques", "Introduces the floating-pigment paper marbling traditions of Ebru and Suminagashi and their pattern-control methods."),
        ],
    },
    "Art History": {
        "UG2": [
            ("The Elgin Marbles Controversy: Parthenon Sculptures Dispute", "Examines the removal, display, and ongoing restitution debate surrounding the Parthenon sculptures held in London."),
            ("The Ghent Altarpiece: Theft, Recovery, and Restoration", "Traces the eventful history of the Van Eyck altarpiece through wartime theft, recovery, and modern conservation."),
        ],
    },
    "Artificial Intelligence": {
        "UG2": [
            ("AlphaGo and the Move 37 Phenomenon", "Analyzes the celebrated AlphaGo move that surprised human experts and what it revealed about learned strategy."),
            ("The Frame Problem in Classical AI", "Studies the classical difficulty of specifying which facts remain unchanged after an action in a logical AI system."),
            ("Case Study: IBM Watson's Jeopardy! Victory", "Examines how IBM Watson combined question analysis and evidence scoring to win a nationally televised quiz show."),
            ("Genetic Programming and Automatic Code Synthesis", "Introduces evolutionary methods that evolve executable program structures to satisfy a target specification."),
            ("Case Study: Deep Blue vs. Kasparov", "Reviews the search and evaluation techniques behind the first computer chess victory over a reigning world champion."),
            ("Answer Set Programming for Knowledge Representation", "Covers declarative logic programming used to represent knowledge and solve combinatorial search problems."),
            ("Case-Based Reasoning Systems", "Explores AI systems that solve new problems by adapting solutions retrieved from previously solved cases."),
        ],
    },
    "Big Data": {
        "UG2": [
            ("Big Data Case Study: The Netflix Prize Recommendation Challenge", "Examines the open recommender-system competition that advanced collaborative filtering research at scale."),
            ("Apache Pulsar as a Multi-Tenant Messaging Alternative to Kafka", "Introduces Pulsar's tiered storage and multi-tenancy model as an alternative streaming platform to Kafka."),
            ("Bloom Filters for Large-Scale Data Deduplication", "Explains how probabilistic Bloom filters efficiently detect likely duplicate records across massive datasets."),
        ],
    },
    "Biology": {
        "UG2": [
            ("Bioluminescence Mechanisms in Marine Organisms", "Explores the biochemical pathways that let deep-sea and coastal marine organisms produce their own light."),
            ("Case Study: The Discovery of Insulin by Banting and Best", "Traces the 1921 experiments that isolated insulin and transformed diabetes from a fatal to a manageable disease."),
            ("Tardigrade Cryptobiosis and Extremotolerance", "Examines how tardigrades enter a suspended metabolic state to survive desiccation, radiation, and vacuum exposure."),
        ],
    },
    "Business Analytics": {
        "UG2": [
            ("Case Study: Moneyball and Analytics in Baseball Recruitment", "Analyzes how sabermetric statistics reshaped player evaluation and roster-building strategy in professional baseball."),
        ],
    },
    "Chemistry": {
        "UG2": [
            ("Chemiluminescence in Glow Stick Reactions", "Explains the light-producing chemical reaction between a phenyl oxalate ester and hydrogen peroxide in glow sticks."),
            ("The Belousov-Zhabotinsky Oscillating Reaction", "Studies the classic self-sustaining chemical oscillator that cycles through color changes over time."),
            ("Fischer-Tropsch Synthesis of Synthetic Fuels", "Covers the catalytic conversion of syngas into liquid hydrocarbon fuels used in synthetic fuel production."),
            ("Ziegler-Natta Catalysis in Polyolefin Production", "Explains how Ziegler-Natta catalysts control stereochemistry in industrial polyethylene and polypropylene manufacturing."),
        ],
    },
    "Cloud Computing": {
        "UG2": [
            ("Cloud Egress Cost Optimization Strategies", "Covers techniques for reducing the cost of moving data out of cloud platforms across regions and providers."),
            ("Serverless Cold Start Mitigation Techniques", "Examines provisioned concurrency, warm pools, and runtime choices used to reduce serverless function cold-start latency."),
        ],
    },
    "Coding": {
        "UG2": [
            ("Skip Lists as a Probabilistic Data Structure", "Introduces the layered linked-list structure that gives expected logarithmic search using randomized levels."),
            ("The Byzantine Generals Problem in Distributed Coding", "Explores the classic fault-tolerance problem of reaching agreement despite unreliable or malicious participants."),
            ("Rope Data Structures for Efficient Text Editing", "Covers the binary-tree-based rope structure used to efficiently edit and concatenate very large strings."),
            ("Duff's Device and Loop Unrolling Tricks", "Examines the classic C loop-unrolling technique and what it reveals about manual performance optimization."),
        ],
    },
    "Computer Science Engineering": {
        "UG2": [
            ("The Dining Philosophers Problem in Concurrent Systems", "Studies the classic resource-allocation problem used to illustrate deadlock, starvation, and concurrency control."),
            ("Bloom Filter Applications in Systems Engineering", "Explains how probabilistic Bloom filters are applied to reduce lookups in caches, databases, and network systems."),
        ],
    },
    "Critical Thinking": {
        "UG2": [
            ("The Linda Problem and the Conjunction Fallacy", "Examines the classic experiment showing how narrative detail can lead people to misjudge probability."),
            ("The Monty Hall Problem and Probabilistic Intuition", "Analyzes the counterintuitive game-show puzzle that challenges everyday probabilistic reasoning."),
            ("Wason Selection Task and Confirmation Bias", "Studies the classic card-selection experiment revealing how people test rules in confirmation-biased ways."),
            ("The Ultimatum Game and Fairness Reasoning", "Explores how the ultimatum game experiment reveals the role of fairness perceptions in economic decision-making."),
            ("Chesterton's Fence and Reasoning About Existing Rules", "Examines the principle that existing rules or structures should be understood before being removed or changed."),
            ("The Sorites Paradox and Vagueness in Reasoning", "Studies the heap paradox and its implications for reasoning about vague predicates and borderline cases."),
            ("Munchausen Trilemma and the Regress of Justification", "Explores the three-horned dilemma facing any attempt to fully justify a belief through reasoning alone."),
            ("The Ecological Rationality Debate: Gigerenzer vs Kahneman", "Compares two influential views on whether heuristics are reasoning flaws or adaptive tools suited to real environments."),
        ],
    },
    "Cybersecurity": {
        "UG2": [
            ("The Stuxnet Worm: Anatomy of a Cyber-Physical Attack", "Analyzes the engineering of the Stuxnet worm and how it sabotaged industrial control systems physically."),
            ("The Morris Worm and the Birth of Incident Response", "Examines the 1988 internet worm that prompted the creation of formal computer security incident response teams."),
            ("The Mirai Botnet and IoT Device Compromise", "Studies how the Mirai malware hijacked insecure IoT devices to launch large-scale distributed denial-of-service attacks."),
            ("The SolarWinds Supply Chain Breach Case Study", "Examines the software build-process compromise that let attackers distribute malicious updates to thousands of organizations."),
            ("The Equifax Breach: Root Cause Analysis", "Analyzes the unpatched vulnerability and process failures behind one of the largest consumer data breaches."),
            ("Homomorphic Encryption for Privacy-Preserving Computation", "Introduces encryption schemes that allow computation directly on encrypted data without ever decrypting it."),
        ],
    },
    "Data Science": {
        "UG2": [
            ("Case Study: Target's Pregnancy Prediction Controversy", "Examines the retail analytics case where purchase-pattern models inferred sensitive customer information."),
            ("Benford's Law for Fraud Detection in Financial Data", "Explains how the expected distribution of leading digits is used to flag anomalies in financial datasets."),
            ("The Bass Diffusion Model for Product Adoption Forecasting", "Introduces the classic model for forecasting how new products spread through a population of adopters."),
        ],
    },
    "Digital Marketing": {
        "UG2": [
            ("Case Study: Old Spice's 'The Man Your Man Could Smell Like' Campaign", "Analyzes the viral video campaign that repositioned a legacy brand toward a younger audience."),
            ("Case Study: Dove's Real Beauty Campaign Analysis", "Examines how Dove's long-running campaign used authenticity messaging to build brand loyalty and controversy."),
            ("Case Study: Oreo's Real-Time 'Dunk in the Dark' Tweet", "Studies the widely cited real-time marketing response during a major televised event blackout."),
            ("Case Study: Airbnb's User-Generated Content Strategy Origins", "Traces how early user-generated photography and reviews shaped Airbnb's trust-driven marketing approach."),
            ("Case Study: Blendtec's 'Will It Blend?' Content Marketing", "Analyzes how a low-budget video series turned a niche appliance brand into a viral content phenomenon."),
            ("Newsjacking Techniques in Real-Time Marketing", "Covers the practice of aligning brand messaging with breaking news events to gain marketing attention."),
            ("Case Study: Wendy's Twitter Voice and Brand Personality", "Examines how a distinctive social media voice became a deliberate brand differentiation strategy."),
            ("Case Study: ALS Ice Bucket Challenge Viral Mechanics", "Analyzes the participatory structure that made the Ice Bucket Challenge spread rapidly across social networks."),
        ],
    },
    "Economics": {
        "UG2": [
            ("The South Sea Bubble of 1720", "Examines the speculative stock scheme and collapse that shaped early British financial regulation."),
            ("The Tulip Mania of 1637", "Studies the Dutch speculative bubble in tulip bulb futures often cited as an early asset-bubble example."),
            ("The 1997 Asian Financial Crisis", "Analyzes the currency and capital-flight crisis that swept through East Asian economies in the late 1990s."),
            ("The 2008 Subprime Mortgage Crisis: Causal Mechanisms", "Traces the securitization and lending practices that transformed a housing downturn into a global financial crisis."),
            ("The Weimar Republic Hyperinflation of 1923", "Examines the causes and social consequences of Germany's extreme post-World War I currency collapse."),
            ("The Bretton Woods System and Its Collapse", "Studies the postwar fixed exchange-rate system and the events leading to its breakdown in the early 1970s."),
            ("The OPEC Oil Embargo of 1973", "Analyzes how the 1973 oil embargo triggered stagflation and reshaped global energy economics."),
            ("Zimbabwe's Hyperinflation of the 2000s", "Examines the fiscal and monetary policy failures behind one of history's most extreme hyperinflation episodes."),
            ("The Plaza Accord of 1985", "Studies the coordinated currency intervention among major economies to depreciate the U.S. dollar."),
            ("The Latin American Debt Crisis of the 1980s", "Analyzes the sovereign default wave that followed excessive dollar-denominated borrowing across Latin America."),
            ("The Nixon Shock and the End of the Gold Standard", "Examines the 1971 decision to suspend dollar-gold convertibility and its lasting effect on global finance."),
            ("The Dot-Com Bubble of the Late 1990s", "Studies the speculative rise and collapse of internet company valuations at the turn of the millennium."),
        ],
    },
    "English": {
        "UG2": [
            ("The Oulipo Movement and Constrained Writing Techniques", "Introduces the literary movement that generates texts through deliberate mathematical and structural constraints."),
        ],
    },
    "Finance": {
        "UG2": [
            ("Case Study: The Long-Term Capital Management Collapse", "Examines how a highly leveraged hedge fund's models failed under extreme market stress in 1998."),
            ("Case Study: The Flash Crash of 2010", "Analyzes the rapid algorithmic-trading-driven market plunge and recovery of May 2010."),
            ("Case Study: Lehman Brothers Collapse and Systemic Risk", "Studies the failure of Lehman Brothers and its role in transmitting systemic risk through global finance."),
            ("Case Study: The GameStop Short Squeeze of 2021", "Examines how coordinated retail trading forced a historic short squeeze in a heavily shorted stock."),
            ("Covered Interest Rate Parity Arbitrage", "Explains the no-arbitrage relationship linking spot rates, forward rates, and interest rate differentials across currencies."),
        ],
    },
    "First Aid": {
        "UG2": [
            ("Avalanche Burial First Aid and Rescue Priorities", "Covers survival time factors, airway management, and rescue triage for avalanche burial victims."),
            ("High-Altitude Sickness Recognition and Response", "Explains recognition and field response to acute mountain sickness and its more severe high-altitude complications."),
        ],
    },
    "Geography": {
        "UG2": [
            ("The Aral Sea Desiccation Case Study", "Examines the human-driven shrinkage of the Aral Sea and its environmental and economic consequences."),
            ("The Nile River Basin Water-Sharing Disputes", "Analyzes the transboundary water allocation conflicts among Nile Basin countries."),
            ("The Panama Canal as a Geopolitical Chokepoint", "Studies the Panama Canal's role as a strategic global trade route and point of geopolitical leverage."),
        ],
    },
    "Health Education": {
        "UG2": [
            ("The Framingham Heart Study and Cardiovascular Risk Research", "Examines the long-running cohort study that established many modern cardiovascular risk factor concepts."),
        ],
    },
    "ICT & Computer Science": {
        "UG2": [
            ("Bring Your Own Device (BYOD) Policy Design for ICT Systems", "Covers the security, access control, and management considerations of employee-owned device policies."),
        ],
    },
    "Islamic Studies": {
        "UG2": [
            ("The Bayt al-Hikmah: The House of Wisdom in Abbasid Baghdad", "Examines the Abbasid-era institution renowned for translation and scholarship in the sciences and philosophy."),
        ],
    },
    "JavaScript": {
        "UG2": [
            ("The Same-Origin Policy and postMessage API Communication", "Explains browser origin isolation rules and how postMessage enables safe cross-origin window communication."),
            ("Web Animations API for Declarative Motion Design", "Introduces the browser API for creating and controlling animations declaratively through JavaScript."),
        ],
    },
    "MBA": {
        "UG2": [
            ("Case Study: Netflix's Pivot from DVD to Streaming", "Examines the strategic decisions behind Netflix's transformation from a mail-rental business to a streaming leader."),
            ("Case Study: Kodak's Failure to Adapt to Digital Photography", "Analyzes how Kodak's internal incentives contributed to missing the shift to digital imaging."),
            ("Case Study: Blockbuster's Decline Against Netflix", "Studies the strategic missteps that led a dominant video rental chain to lose ground to a streaming challenger."),
            ("Case Study: Southwest Airlines' Low-Cost Strategy", "Examines the operational choices behind Southwest's sustained low-cost competitive advantage."),
            ("Case Study: Nokia's Fall from Mobile Market Leadership", "Analyzes the organizational and strategic factors behind Nokia's loss of smartphone market leadership."),
        ],
    },
    "Machine Learning": {
        "UG2": [
            ("Platt Scaling for Probability Calibration", "Explains how a sigmoid transformation is fitted to calibrate classifier scores into reliable probabilities."),
            ("Conformal Prediction for Uncertainty Quantification", "Introduces a framework that produces prediction sets with statistically guaranteed coverage levels."),
            ("The No Free Lunch Theorem in Machine Learning", "Examines the theoretical result showing no single algorithm outperforms all others across every possible problem."),
            ("Locality-Sensitive Hashing for Approximate Nearest Neighbors", "Covers hashing techniques that speed up approximate similarity search in high-dimensional data."),
            ("Siamese Networks for Similarity Learning", "Introduces twin neural network architectures trained to learn similarity or distance between input pairs."),
            ("Curriculum Learning Strategies", "Explores training strategies that present examples in a structured order from easy to difficult."),
            ("Label Smoothing as a Regularization Technique", "Explains how softening target labels during training improves calibration and reduces overconfidence."),
            ("Focal Loss for Class Imbalance in Object Detection", "Covers a loss function that down-weights easy examples to address extreme class imbalance in detection tasks."),
            ("Elastic Weight Consolidation for Catastrophic Forgetting", "Introduces a technique that protects important weights to reduce forgetting when learning new tasks sequentially."),
            ("Federated Learning Across Distributed Devices", "Explains how models are trained collaboratively across decentralized devices without sharing raw data."),
            ("Contrastive Learning Frameworks (SimCLR)", "Covers self-supervised representation learning that pulls augmented views of the same example together."),
            ("Bayesian Optimization for Hyperparameter Search", "Introduces a sample-efficient search strategy that models the objective function to guide hyperparameter tuning."),
            ("Zero-Inflated Models for Sparse Count Data", "Explains statistical models designed for count data with an excess of zero observations."),
        ],
    },
    "Math": {
        "UG2": [
            ("The Banach-Tarski Paradox in Set-Theoretic Geometry", "Examines the counterintuitive result showing a solid ball can be decomposed and reassembled into two identical copies."),
            ("The Collatz Conjecture and Open Problems in Number Theory", "Introduces the famously simple yet unproven iterative sequence conjecture in elementary number theory."),
            ("The Four Color Theorem and Its Computer-Assisted Proof", "Studies the map-coloring theorem notable for being the first major result proved with computer assistance."),
        ],
    },
    "Natural Language Processing": {
        "UG2": [
            ("The ELIZA Effect and Early Chatbot Illusions", "Examines the classic 1960s chatbot and the tendency of users to attribute understanding to simple pattern matching."),
            ("Perplexity as a Language Model Evaluation Metric", "Explains how perplexity measures how well a probability model predicts held-out text."),
            ("The BLEU Score: Strengths and Limitations", "Analyzes the widely used machine translation metric and the criticisms of its correlation with human judgment."),
            ("Case Study: Google's BERT and the Transformer Revolution in Search", "Examines how the BERT model changed search query understanding and downstream NLP task performance."),
            ("Word Sense Disambiguation Techniques", "Covers methods for determining which meaning of a polysemous word applies in a given context."),
            ("Metaphor Identification in Computational Linguistics", "Explores computational approaches for detecting figurative and metaphorical language in text."),
            ("Text-to-Speech Synthesis Fundamentals", "Introduces the pipeline that converts written text into natural-sounding synthesized speech."),
            ("Sarcasm and Irony Detection in Text", "Examines the linguistic cues and models used to detect sarcastic or ironic intent in written text."),
            ("Emotion Detection Beyond Sentiment Polarity", "Covers models that classify fine-grained emotional categories rather than simple positive-negative sentiment."),
            ("Code-Switching Detection in Multilingual Text", "Explores methods for identifying and processing text that alternates between multiple languages."),
            ("Toxicity Detection and Content Moderation Models", "Covers NLP models trained to flag harmful or abusive language for automated content moderation."),
            ("Keyphrase Extraction Techniques", "Introduces methods for automatically identifying the most representative phrases within a document."),
        ],
    },
    "Operations Management": {
        "UG2": [
            ("Case Study: Toyota's Just-in-Time Response to the 1997 Aisin Fire", "Examines how Toyota's supplier network recovered production after a fire destroyed a sole-source parts plant."),
            ("Ford's Moving Assembly Line: Historical Origins of Line Balancing", "Traces how Ford's early assembly line innovations established foundational line-balancing concepts."),
            ("The Toyota Andon Cord System for Quality Stoppage", "Explains the andon cord mechanism that empowers workers to halt production when a defect is detected."),
            ("Dell's Direct-to-Consumer Build-to-Order Model", "Examines how Dell's build-to-order supply chain model reduced inventory and improved responsiveness."),
        ],
    },
    "Philosophy": {
        "UG2": [
            ("The Ship of Theseus and Identity Over Time", "Examines the ancient puzzle of whether an object remains the same after all its parts are replaced."),
            ("Zeno's Paradoxes of Motion", "Studies the ancient paradoxes challenging the coherence of motion, space, and infinite divisibility."),
            ("The Experience Machine Thought Experiment (Nozick)", "Explores Nozick's thought experiment questioning whether simulated pleasurable experience equals genuine wellbeing."),
            ("Pascal's Wager and Decision Theory Under Uncertainty", "Examines Pascal's decision-theoretic argument and its role in reasoning about belief under uncertainty."),
        ],
    },
    "Physical Education & Self-Defense": {
        "UG2": [
            ("Aikido Principles of Redirection and Blending", "Introduces the Aikido philosophy of blending with an opponent's momentum rather than opposing force directly."),
        ],
    },
    "Physics": {
        "UG2": [
            ("The Michelson-Morley Experiment and the Ether Hypothesis", "Examines the famous null-result experiment that undermined the luminiferous ether hypothesis."),
            ("The Double-Slit Experiment and Wave-Particle Duality", "Studies the foundational experiment demonstrating the wave-particle duality of light and matter."),
            ("The EPR Paradox and Quantum Nonlocality", "Analyzes the Einstein-Podolsky-Rosen thought experiment and its challenge to local realism in quantum theory."),
            ("Casimir Effect and Vacuum Energy", "Explains the measurable force arising between close-spaced plates due to quantum vacuum fluctuations."),
            ("The Cavendish Experiment and Measuring Gravity", "Examines the classic torsion-balance experiment that first measured the gravitational constant."),
            ("Hawking Radiation and Black Hole Thermodynamics", "Introduces the theoretical prediction that black holes emit radiation and slowly lose mass over time."),
        ],
    },
    "Project Management": {
        "UG2": [
            ("Case Study: The Sydney Opera House Cost Overrun", "Examines the scheduling and design decisions behind one of the most famous project cost overruns."),
            ("Case Study: The Big Dig Boston Highway Project", "Analyzes the scope, cost, and schedule challenges of Boston's major underground highway project."),
            ("Case Study: The Denver International Airport Baggage System Failure", "Studies the automated baggage system failure that delayed the airport's opening and inflated its budget."),
            ("Case Study: The Channel Tunnel Project Delivery", "Examines the cross-border engineering, financing, and delivery challenges of the Channel Tunnel project."),
            ("The Iron Triangle: Origins and Modern Critiques", "Traces the scope-cost-time constraint model and contemporary critiques of its limitations."),
            ("Parkinson's Law in Project Scheduling", "Explores how work tends to expand to fill the time allotted, and its implications for schedule estimation."),
            ("The Planning Fallacy in Megaproject Estimation", "Examines the systematic tendency to underestimate cost and duration in large infrastructure projects."),
            ("Case Study: The Berlin Brandenburg Airport Delays", "Analyzes the design changes and technical failures behind a decade of construction delays at a major airport."),
            ("Hofstadter's Law and Recurring Schedule Overruns", "Explores the recursive observation that tasks take longer than expected, even accounting for the expectation itself."),
            ("Case Study: The Concorde Project and Sunk Cost Fallacy", "Examines how continued investment in the Concorde illustrates the sunk cost fallacy in project decision-making."),
        ],
    },
    "Prompt Engineering": {
        "UG2": [
            ("Prompt Engineering for Chain-of-Verification Techniques", "Covers prompting strategies that ask a model to generate and check its own verification questions before answering."),
            ("Skeleton-of-Thought Prompting for Parallel Generation", "Introduces a prompting technique that first drafts an answer outline, then expands sections in parallel."),
            ("Prompt Engineering for Tool-Augmented Math Solvers", "Explores prompting patterns that combine language model reasoning with external calculator or solver tools."),
        ],
    },
    "Python": {
        "UG2": [
            ("The Walrus Operator and Assignment Expressions", "Explains the walrus operator syntax that assigns a value as part of a larger expression."),
            ("Building Plugin Systems with Python Entry Points", "Covers how packaging entry points enable discoverable, extensible plugin architectures in Python applications."),
        ],
    },
    "R": {
        "UG2": [
            ("Tail Call Optimization Limitations in R", "Examines why R does not natively optimize tail-recursive calls and the practical implications for recursive code."),
            ("The magrittr Pipe vs. Native R Pipe Operator", "Compares the tidyverse magrittr pipe with R's built-in native pipe operator for chaining function calls."),
            ("Building Custom ggplot2 Geoms", "Covers how to extend ggplot2 by writing custom geometric layer objects for specialized visualizations."),
            ("Working with Missing Data Using the mice Package", "Introduces multiple imputation by chained equations for handling missing values in R datasets."),
        ],
    },
    "Science": {
        "UG2": [
            ("The Miller-Urey Experiment and Origins of Life", "Examines the classic experiment that simulated early Earth conditions to synthesize organic molecules."),
            ("Case Study: The Discovery of Penicillin by Fleming", "Traces the accidental observation and subsequent development that launched the age of antibiotics."),
            ("The Milgram Obedience Experiment in Behavioral Science", "Examines the controversial psychology experiment studying obedience to authority and its ethical legacy."),
            ("Citizen Science and the Discovery of Exoplanets via Transit Photometry", "Explores how volunteer citizen scientists contribute to identifying exoplanets from telescope light-curve data."),
            ("The Tuskegee Study and Research Ethics Reform", "Examines the unethical study that drove major reforms in informed consent and research oversight."),
            ("The Human Genome Project: Milestones and Methods", "Traces the international effort to sequence the human genome and its lasting scientific impact."),
        ],
    },
    "Web Development": {
        "UG2": [
            ("Optimistic UI Updates for Perceived Performance", "Explains how updating the interface before server confirmation improves perceived application responsiveness."),
            ("The BFCache (Back/Forward Cache) and Navigation Performance", "Covers how browsers cache full page state to enable instant back and forward navigation."),
            ("Import Maps for Native ES Module Resolution", "Introduces import maps that let browsers resolve bare module specifiers without a build bundler."),
        ],
    },
    "World History": {
        "UG2": [
            ("The Sykes-Picot Agreement and the Modern Middle East", "Examines the secret wartime agreement that shaped colonial boundaries across the modern Middle East."),
            ("The Bandung Conference and the Non-Aligned Movement", "Studies the 1955 conference of newly independent nations that laid groundwork for the Non-Aligned Movement."),
            ("The Berlin Conference of 1884 and the Scramble for Africa", "Examines the European conference that formalized colonial partitioning of the African continent."),
        ],
    },
    "World Literature": {
        "UG2": [
            ("Naguib Mahfouz and the Cairo Trilogy's Social Realism", "Introduces the Nobel laureate's multigenerational Cairo novels and their portrayal of twentieth-century Egyptian society."),
        ],
    },
}
