"""New (title, summary) topic tuples for a final top-up pass on 44 UG4
college subjects that fell slightly short of the 80-lesson minimum after
a prior mass-generation pass (independently-generated batches sometimes
picked a title that collided with another level, and the merge script
safely skips rather than duplicates such collisions).

Each subject maps to a dict with a "UG4" key holding new (title, summary)
tuples. Titles do not duplicate each other within a subject's UG4 list
and do not overlap with the lessons already present for that subject at
UG4 in backend/syllabus/level_ug4.json. Topics favor specific, less
obvious sub-areas to minimize accidental overlap with other levels
(C1, C2, UG1-UG3, M1, M2) not visible here. A later merge script
(backend/scripts/merge_all_subjects_expansion.py) reads this dict and
builds full lesson objects from these pairs.
"""

MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "AI Tools": {
        "UG4": [
            ("AI Tools for Podcast Production and Editing", "Surveys AI-assisted transcription, noise removal, and editing tools used in modern podcast workflows."),
            ("AI Tools for Patent Prior-Art Search", "Examines how AI search tools accelerate the discovery of relevant prior art during patent examination."),
            ("AI Tools for Clinical Documentation Assistance", "Covers AI scribes and summarization tools that draft clinical notes from patient encounters."),
            ("AI Tools for Museum Curation and Digital Exhibits", "Explores AI-assisted cataloging, tagging, and interactive exhibit design in museum settings."),
            ("AI Tools for Insurance Claims Triage", "Analyzes how AI tools classify and prioritize incoming insurance claims for faster adjudication."),
            ("AI Tools for Music Composition and Sample Generation", "Reviews AI systems that generate melodic ideas, samples, and backing tracks for composers."),
            ("AI Tools for Localization QA Testing", "Covers AI-assisted testing tools that flag translation, layout, and cultural issues in localized software."),
            ("AI Tools for Fleet Maintenance Scheduling", "Examines AI tools that predict vehicle maintenance needs and optimize fleet servicing schedules."),
        ],
    },
    "Art": {
        "UG4": [
            ("Tattoo Art and Skin as Medium", "Studies tattooing as a fine art practice, covering design tradition, technique, and skin as a living canvas."),
            ("Diorama and Miniature Model Making", "Covers techniques for constructing scaled dioramas and miniature scenes as narrative sculptural art."),
        ],
    },
    "Art History": {
        "UG4": [
            ("Etruscan Art and Its Influence on Roman Visual Culture", "Examines Etruscan tomb painting and bronze work as a precursor to Roman artistic conventions."),
            ("Minoan and Mycenaean Bronze Age Art", "Surveys Aegean Bronze Age fresco, pottery, and metalwork from Crete and mainland Greece."),
            ("Ottonian and Carolingian Manuscript Illumination", "Studies the revival of imperial manuscript art under the Carolingian and Ottonian dynasties."),
            ("Flemish Baroque: Rubens and Van Dyck", "Analyzes the dynamic compositions and portraiture of the seventeenth-century Flemish Baroque school."),
            ("Dutch Golden Age Genre Painting", "Examines everyday domestic scenes by artists such as Vermeer and de Hooch as social documents."),
            ("Neoclassicism: David and the Politics of Style", "Explores how Jacques-Louis David used classical restraint to serve revolutionary and imperial politics."),
            ("The Pre-Raphaelite Brotherhood", "Studies the Victorian revival of pre-Renaissance detail and medieval subject matter in British painting."),
            ("Fauvism and the Use of Color as Expression", "Analyzes Matisse and the Fauves' use of unnaturalistic, emotionally charged color."),
            ("German Expressionism: Die Brücke and Der Blaue Reiter", "Compares the two major German Expressionist groups and their approaches to color and form."),
            ("Suprematism and Constructivism in Russian Avant-Garde", "Examines Malevich's geometric abstraction alongside Constructivist design for a new social order."),
            ("Abstract Expressionism and the New York School", "Studies the postwar shift of the art world's center to New York through gesture and scale."),
            ("Minimalism in Postwar American Sculpture", "Analyzes the reductive geometric forms of Judd, Andre, and their minimalist contemporaries."),
            ("Korean Dansaekhwa and Monochrome Painting", "Surveys the Korean monochrome painting movement and its meditative material processes."),
        ],
    },
    "Artificial Intelligence": {
        "UG4": [
            ("Neurosymbolic AI: Combining Logic and Learning", "Explores hybrid architectures that integrate symbolic reasoning with neural network learning."),
            ("AI for Weather and Climate Forecasting", "Examines machine learning models applied to short-term weather prediction and climate simulation."),
            ("Test-Time Compute Scaling for Reasoning Models", "Analyzes how allocating additional inference-time computation improves reasoning performance in AI models."),
            ("Multi-Agent Debate for Improved Reasoning", "Studies protocols where multiple AI agents argue and critique each other to improve answer quality."),
            ("AI for Materials Discovery", "Covers machine learning approaches to predicting and screening novel material properties."),
            ("Constitutional Classifiers for Safety Filtering", "Examines classifier-based safeguards that screen model inputs and outputs against defined safety rules."),
        ],
    },
    "Big Data": {
        "UG4": [
            ("Data Mesh Federated Computational Governance", "Explains the federated governance model that balances domain autonomy with global data standards in a data mesh."),
            ("Change Data Capture Pipelines", "Covers techniques for capturing and propagating row-level database changes into downstream big data systems."),
            ("Apache Iceberg Table Maintenance and Compaction", "Examines file compaction, snapshot expiration, and manifest rewriting for healthy Iceberg tables."),
            ("Bloom Filters for Big Data Query Acceleration", "Explains how probabilistic membership filters reduce unnecessary data scans in large query engines."),
            ("Consistent Hashing for Distributed Data Partitioning", "Covers consistent hashing techniques used to minimize data movement when scaling distributed clusters."),
            ("Vector Databases for Large-Scale Similarity Search", "Examines architectures for indexing and querying high-dimensional embeddings at scale."),
            ("Data Contract Design Between Producers and Consumers", "Explains how formal data contracts enforce schema and quality expectations across pipeline boundaries."),
            ("Streaming Joins and Windowing Semantics", "Covers stateful join strategies and windowing models used in real-time stream processing."),
        ],
    },
    "Biology": {
        "UG4": [
            ("Xenotransplantation and Cross-Species Organ Science", "Examines the biological and immunological challenges of transplanting organs across species."),
        ],
    },
    "Business Analytics": {
        "UG4": [
            ("Prescriptive Analytics and Optimization-Based Decision Support", "Covers analytics methods that recommend optimal actions rather than merely predicting outcomes."),
            ("Marketing Mix Modeling with Bayesian Methods", "Examines Bayesian techniques for estimating channel contribution and uncertainty in marketing mix models."),
            ("Customer Churn Survival Modeling with Competing Risks", "Applies survival analysis with competing risks to model multiple distinct causes of customer attrition."),
            ("Analytics for Talent Retention and Attrition Prediction", "Covers predictive models that identify employees at risk of leaving and the drivers behind attrition."),
            ("Price Elasticity Estimation Techniques", "Explains statistical methods for estimating how demand responds to changes in price."),
            ("Analytics for Fraud Detection in Financial Transactions", "Covers supervised and anomaly-based analytics techniques for identifying fraudulent transactions."),
            ("Data-Driven Assortment Planning for Retail", "Examines analytics methods for selecting and optimizing product assortments across retail locations."),
            ("Real Options Analysis for Business Investment Decisions", "Applies option-pricing concepts to value managerial flexibility in staged business investments."),
            ("Analytics for Employee Engagement Survey Interpretation", "Covers statistical approaches to analyzing and acting on employee engagement survey data."),
            ("Cluster-Based Market Segmentation Validation Techniques", "Examines methods for validating the stability and business relevance of clustering-derived market segments."),
            ("Business Analytics for Environmental Sustainability Metrics", "Covers analytics approaches to tracking, modeling, and reporting corporate sustainability performance."),
        ],
    },
    "Chemistry": {
        "UG4": [
            ("Mechanochemistry and Solvent-Free Synthesis", "Examines reactions driven by mechanical force, such as ball milling, as a solvent-free synthesis route."),
            ("Chemistry of Metal-Organic Frameworks", "Covers the design and porous properties of metal-organic frameworks for gas storage and catalysis."),
            ("Isotope Labeling Techniques in Reaction Tracing", "Explains how isotopically labeled reagents are used to trace reaction mechanisms and metabolic pathways."),
            ("Chemiluminescence and Bioluminescent Assay Chemistry", "Examines the chemical basis of light-emitting reactions used in analytical and biological assays."),
        ],
    },
    "Cloud Computing": {
        "UG4": [
            ("Cloud Chaos Engineering Practices", "Covers deliberately injecting failures into cloud systems to validate resilience before real outages occur."),
            ("Cloud Data Mesh Implementation Patterns", "Examines practical architectural patterns for implementing domain-oriented data ownership on cloud platforms."),
            ("Confidential Computing and Trusted Execution in the Cloud", "Explains hardware-based trusted execution environments that protect data while it is being processed."),
            ("Cloud-Native Feature Flag Management Systems", "Covers architectures for managing and rolling out feature flags across distributed cloud services."),
            ("WebAssembly Workloads on Cloud Platforms", "Examines running WebAssembly modules as lightweight, portable compute units in cloud environments."),
            ("Cloud Queue-Based Load Leveling Patterns", "Covers using message queues to smooth bursty workloads across cloud-hosted services."),
            ("Cloud Bin Packing and Workload Scheduling Algorithms", "Explains algorithms that pack workloads efficiently onto cloud compute nodes to reduce waste."),
            ("Cloud Disaster Recovery Tiering (Pilot Light, Warm Standby)", "Compares disaster recovery strategies of varying cost and recovery-time tradeoffs in the cloud."),
            ("Cloud API Rate Limiting and Throttling Design", "Covers design patterns for protecting cloud APIs from overload through rate limiting and throttling."),
            ("Cloud Cost Forecasting Using Historical Usage Models", "Examines statistical approaches to projecting future cloud spend from historical consumption data."),
            ("Cloud Region and Availability Zone Selection Strategy", "Covers criteria for choosing cloud regions and zones based on latency, compliance, and resilience needs."),
            ("Cloud-Native Secrets Rotation Automation", "Examines automated workflows for rotating credentials and keys across cloud-native applications."),
        ],
    },
    "Coding": {
        "UG4": [
            ("Formal Grammar Design for Custom Configuration Languages", "Covers designing formal grammars to define readable, parseable configuration file languages."),
        ],
    },
    "Computer Science Engineering": {
        "UG4": [
            ("Time Synchronization Protocols in Distributed Systems (NTP, PTP)", "Examines protocols used to synchronize clocks across distributed systems with varying precision needs."),
            ("Persistent Data Structures for Functional Systems", "Covers immutable data structures that preserve prior versions efficiently under updates."),
        ],
    },
    "Cooking": {
        "UG4": [
            ("Advanced Tempura and Batter Frying Techniques", "Covers precision batter formulation and oil temperature control for light, crisp tempura frying."),
        ],
    },
    "Critical Thinking": {
        "UG4": [
            ("The Paradox of the Heap and Sorites Reasoning", "Examines the sorites paradox and its implications for reasoning about vague predicates."),
            ("Signal Detection Theory in Judgment Under Uncertainty", "Applies signal detection theory to analyze how people distinguish signal from noise in uncertain judgments."),
            ("The Base Rate Fallacy in Risk Communication", "Examines how neglecting base rates distorts risk judgments in medical and legal contexts."),
            ("Epistemic Bubbles versus Echo Chambers", "Distinguishes information environments that merely exclude other views from those that actively discredit them."),
            ("Inference to the Best Explanation (Abductive Reasoning)", "Examines how abductive reasoning selects the most plausible explanation among competing hypotheses."),
            ("The Framing Effect and Its Influence on Choice", "Analyzes how the presentation of identical information can shift judgment and decision-making."),
            ("Dialectical Reasoning and the Synthesis of Opposing Views", "Covers dialectical methods for reconciling opposing arguments into a more refined position."),
            ("Critical Thinking in Algorithmic and AI-Mediated Decision Environments", "Examines how algorithmic recommendation systems shape and constrain human reasoning and choice."),
        ],
    },
    "Cybersecurity": {
        "UG4": [
            ("Container Runtime Security and Isolation Techniques", "Covers securing container runtimes through namespace isolation, seccomp profiles, and runtime monitoring."),
            ("Attack Surface Management Programs", "Examines continuous discovery and monitoring programs that reduce an organization's exposed attack surface."),
            ("Threat Hunting Methodologies", "Covers proactive, hypothesis-driven techniques for uncovering threats not caught by automated defenses."),
            ("Security Chaos Engineering", "Applies chaos engineering principles to deliberately test and strengthen security controls."),
            ("Insider Threat Detection Programs", "Examines behavioral analytics and policy frameworks for detecting malicious or negligent insider activity."),
            ("Cryptographic Key Lifecycle Management", "Covers the generation, distribution, rotation, and retirement of cryptographic keys in secure systems."),
            ("Cyber Risk Quantification Models", "Examines quantitative models for expressing cybersecurity risk in financial and probabilistic terms."),
        ],
    },
    "Data Science": {
        "UG4": [
            ("Uplift Modeling for Targeted Interventions", "Covers modeling techniques that estimate the incremental effect of an intervention on individual outcomes."),
        ],
    },
    "Digital Marketing": {
        "UG4": [
            ("Zero-Party Data Collection Strategy", "Examines strategies for collecting data that customers intentionally and proactively share with brands."),
            ("Marketing for the Creator Economy", "Covers marketing strategies built around independent content creators and their audiences."),
            ("Programmatic Advertising and Real-Time Bidding", "Explains the automated auction mechanics behind programmatic ad buying and real-time bidding."),
            ("Conversational Commerce via Messaging Apps", "Examines marketing and sales strategies conducted through messaging platforms and chat interfaces."),
        ],
    },
    "Economics": {
        "UG4": [
            ("Milton Friedman and Monetarism", "Examines Friedman's monetarist theory and its influence on central bank policy debates."),
            ("Joseph Schumpeter and Creative Destruction", "Explores Schumpeter's theory of innovation-driven economic renewal through the destruction of old structures."),
            ("Friedrich Hayek and the Knowledge Problem", "Examines Hayek's argument that decentralized markets solve information problems central planning cannot."),
            ("Elinor Ostrom and the Governance of the Commons", "Studies Ostrom's empirical work on how communities sustainably self-govern shared resources."),
            ("Amartya Sen's Capability Approach to Development", "Examines Sen's reframing of development in terms of expanding human capabilities and freedoms."),
            ("The Latin American Debt Crisis of the 1980s", "Analyzes the causes and consequences of the sovereign debt crisis across Latin America in the 1980s."),
            ("The Asian Financial Crisis of 1997", "Examines the currency and banking crisis that swept East Asian economies in 1997."),
            ("Bretton Woods System and Its Collapse", "Traces the postwar fixed exchange rate system and the economic pressures that led to its 1971 collapse."),
            ("The Economics of German Reunification", "Analyzes the fiscal and structural economic challenges of integrating East and West Germany."),
            ("The Postwar Japanese Economic Miracle", "Examines the institutional and policy factors behind Japan's rapid postwar economic growth."),
            ("The Panic of 1907 and the Founding of the Federal Reserve", "Traces how the 1907 banking panic led directly to the creation of the U.S. Federal Reserve System."),
            ("The Economics of Nineteenth-Century Railway Expansion", "Examines the capital financing, speculation, and economic transformation driven by railway building."),
        ],
    },
    "English": {
        "UG4": [
            ("The Picaresque Novel Tradition", "Examines the episodic, roguish protagonist tradition originating in early modern Spanish and English fiction."),
            ("Ecocriticism and Environmental Literary Studies", "Applies ecological perspectives to the analysis of literary representations of nature and environment."),
            ("The Country House Novel in English Fiction", "Studies the English country house as a recurring symbolic and social setting in the novel."),
            ("Trauma Theory and Literary Narrative", "Examines how narrative form represents and works through psychological trauma in literature."),
            ("The Anti-Novel and Experimental Prose Forms", "Surveys works that deliberately subvert conventional novelistic structure and expectation."),
        ],
    },
    "Finance": {
        "UG4": [
            ("Factor Investing and Smart Beta Strategies", "Examines rules-based investment strategies that target specific risk factors such as value and momentum."),
        ],
    },
    "First Aid": {
        "UG4": [
            ("Anaphylaxis Recognition and Epinephrine Auto-Injector Use", "Covers recognizing severe allergic reactions and administering epinephrine via auto-injector."),
            ("Traumatic Asphyxia and Chest Compression Injury Recognition", "Explains recognizing crush-related chest compression injuries that impair breathing."),
            ("Cold Water Immersion and Hypothermia Rewarming Protocols", "Covers field protocols for safely rewarming patients after cold water immersion."),
            ("Field Triage for Multi-Vehicle Collisions", "Examines rapid triage decision-making when responding to multiple casualties from vehicle collisions."),
            ("Recognizing and Managing Anaphylactic Shock in Children", "Covers pediatric-specific signs and first response steps for anaphylactic shock."),
            ("Improvised Airway Adjuncts in Austere Environments", "Examines improvised techniques for maintaining an open airway when standard equipment is unavailable."),
        ],
    },
    "Foreign Languages": {
        "UG4": [
            ("Basque Language Isolate Typology and Ergativity", "Examines the unique ergative case system and non-Indo-European structure of the Basque language."),
        ],
    },
    "Geography": {
        "UG4": [
            ("Geography of Cryptocurrency Mining and Energy Load", "Examines the spatial distribution of cryptocurrency mining operations and their regional energy demands."),
            ("Biogeography and Island Species Distribution (MacArthur-Wilson Theory)", "Applies the theory of island biogeography to explain species diversity on isolated landmasses."),
            ("Geography of Semiconductor Manufacturing Clusters", "Examines the geographic concentration of semiconductor fabrication and its supply chain implications."),
            ("Fluvial Geomorphology and River Meander Dynamics", "Covers the processes that shape meandering river channels and floodplain evolution."),
            ("Geography of Food Deserts and Urban Access", "Examines the spatial distribution of limited access to affordable, healthy food in urban areas."),
            ("Aeolian Landform Processes in Arid Regions", "Covers wind-driven erosion and deposition processes that shape dune and desert landforms."),
            ("Cryospheric Geography and Ice Sheet Dynamics", "Examines the distribution and movement of the world's ice sheets, glaciers, and permafrost."),
        ],
    },
    "Health Education": {
        "UG4": [
            ("Health Coaching Techniques for Behavior Change Maintenance", "Covers coaching methods that help individuals sustain health behavior changes over the long term."),
        ],
    },
    "ICT & Computer Science": {
        "UG4": [
            ("Digital Twin Systems for ICT Infrastructure Management", "Examines virtual replicas of ICT infrastructure used to simulate, monitor, and optimize operations."),
        ],
    },
    "Islamic Studies": {
        "UG4": [
            ("Islamic Astronomy and the Determination of Prayer Times", "Examines how classical Islamic astronomers developed methods for determining prayer times and qibla direction."),
            ("The Science of Quranic Recitation (Tajwid) as a Discipline", "Surveys the rules and scholarly tradition governing correct oral recitation technique."),
            ("Zakat Administration in Historical Islamic States", "Examines how historical Islamic polities organized the collection and distribution of obligatory almsgiving."),
            ("The Shari'a Court System in Ottoman Administration", "Studies the structure and function of religious courts within Ottoman imperial governance."),
            ("Islamic Perspectives on Bioethics and Medical Consent", "Examines juristic reasoning on medical consent, treatment, and end-of-life bioethical questions."),
            ("The Andalusian Translation Movement and Its Transmission to Europe", "Traces how scholarship translated in Islamic Spain reached and influenced medieval European learning."),
            ("Ibn al-Haytham and the Foundations of Optics", "Examines Ibn al-Haytham's experimental methods and contributions to the science of vision and light."),
            ("Contemporary Halal Certification Standards and Practice", "Surveys the institutions and standards governing modern halal certification across industries."),
        ],
    },
    "JavaScript": {
        "UG4": [
            ("Temporal API for Modern Date and Time Handling", "Introduces the Temporal API as a more reliable replacement for legacy JavaScript date handling."),
        ],
    },
    "MBA": {
        "UG4": [
            ("Zero-Based Budgeting for Corporate Cost Management", "Examines building budgets from a zero base each cycle rather than adjusting prior-year figures."),
            ("Activity-Based Costing for Strategic Decision-Making", "Covers assigning overhead costs to activities to reveal true product and service profitability."),
            ("Real Options Valuation in Strategic Investment Decisions", "Applies option-pricing logic to value managerial flexibility embedded in strategic investments."),
            ("Talent Analytics and Succession Planning", "Examines data-driven approaches to identifying and developing future organizational leaders."),
            ("Crisis Leadership During Reputational Events", "Covers leadership decision-making and communication during events that threaten organizational reputation."),
            ("Strategic Sourcing and Supplier Relationship Management", "Examines frameworks for selecting, managing, and developing strategic supplier partnerships."),
            ("International Transfer Pricing Strategy", "Covers how multinational firms price intercompany transactions across tax jurisdictions."),
        ],
    },
    "Machine Learning": {
        "UG4": [
            ("Conformal Prediction for Uncertainty Quantification", "Covers distribution-free methods for producing prediction intervals with guaranteed coverage."),
        ],
    },
    "Math": {
        "UG4": [
            ("Combinatorial Design Theory and Block Designs", "Examines the construction and properties of balanced incomplete block designs in combinatorics."),
            ("p-adic Numbers and Number-Theoretic Analysis", "Introduces the p-adic number system and its role in modern number-theoretic analysis."),
            ("Optimal Transport Theory", "Covers the mathematics of optimally moving mass between distributions, from Monge to Kantorovich."),
            ("Random Matrix Theory", "Examines the statistical behavior of eigenvalues of large random matrices and its applications."),
        ],
    },
    "Music": {
        "UG4": [
            ("Turntablism and DJ Performance as Compositional Practice", "Examines turntables and mixing as instruments of live musical composition and performance."),
            ("Microtonal Tuning Systems and Just Intonation", "Covers tuning systems beyond twelve-tone equal temperament, including just intonation ratios."),
        ],
    },
    "Natural Language Processing": {
        "UG4": [
            ("Speculative Decoding for Faster LLM Inference", "Examines using a smaller draft model to accelerate autoregressive generation in large language models."),
            ("Constrained Decoding and Grammar-Guided Generation", "Covers decoding techniques that force model output to conform to a specified grammar or schema."),
            ("Model Editing and Knowledge Updating in Language Models", "Examines techniques for directly editing factual knowledge stored in a trained language model."),
            ("Cross-Lingual Information Retrieval Techniques", "Covers retrieval methods that match queries in one language to documents in another."),
            ("Text-to-SQL Semantic Parsing Systems", "Examines systems that translate natural language questions into executable database queries."),
            ("Toxicity Detection and Content Moderation Models", "Covers models trained to identify harmful or policy-violating text for content moderation."),
            ("Stylometry and Authorship Attribution with NLP", "Examines computational techniques for identifying likely authorship from stylistic text features."),
            ("Numeracy and Mathematical Reasoning in Language Models", "Covers approaches for improving and evaluating arithmetic and mathematical reasoning in language models."),
            ("Sign Language Translation and Generation Systems", "Examines NLP and computer vision systems that translate between spoken language and sign language."),
        ],
    },
    "Operations Management": {
        "UG4": [
            ("Digital Supply Network Visibility Platforms", "Examines platforms that provide real-time end-to-end visibility across multi-tier supply networks."),
            ("Operations Analytics for Perishable Inventory Management", "Covers analytics techniques tailored to managing inventory with limited shelf life."),
            ("Nearshoring and Reshoring Operations Strategy", "Examines the operational tradeoffs driving decisions to relocate production closer to home markets."),
            ("Human-Robot Collaboration in Production Environments", "Covers the design and management of workflows where humans and robots share production tasks."),
            ("Operations Management for Humanitarian Logistics", "Examines operations principles applied to disaster relief and humanitarian supply chains."),
            ("Capacity Hedging Strategies Under Demand Uncertainty", "Covers strategies for building flexible capacity buffers to manage uncertain future demand."),
        ],
    },
    "Philosophy": {
        "UG4": [
            ("Thomas Nagel and the Subjective Character of Experience", "Examines Nagel's argument that subjective conscious experience resists purely objective description."),
            ("John Searle's Chinese Room Argument", "Analyzes Searle's thought experiment challenging claims that symbol manipulation constitutes understanding."),
            ("Derek Parfit on Personal Identity and Ethics", "Examines Parfit's reductionist view of personal identity and its implications for ethical reasoning."),
            ("Bernard Williams and Moral Luck", "Explores Williams's argument that factors beyond our control can affect moral judgment."),
            ("Simone de Beauvoir and the Ethics of Ambiguity", "Examines Beauvoir's existentialist ethics grounded in freedom and situated ambiguity."),
            ("Hannah Arendt on the Banality of Evil", "Analyzes Arendt's account of how ordinary bureaucratic conformity can enable atrocity."),
            ("Confucian Relational Ethics and the Concept of Ren", "Examines the Confucian concept of ren as a foundation for relational moral cultivation."),
            ("Daoist Metaphysics: Wu Wei and the Dao", "Explores the Daoist concepts of effortless action and the underlying way of the cosmos."),
            ("Buddhist Philosophy: The Doctrine of No-Self (Anatta)", "Examines the Buddhist rejection of a fixed, permanent self and its philosophical implications."),
        ],
    },
    "Physics": {
        "UG4": [
            ("Effective Field Theory Methods", "Covers the framework for building low-energy physical theories that remain valid without full knowledge of high-energy physics."),
            ("Topological Insulators and Quantum Hall Effect", "Examines materials that conduct on their surface while insulating in the bulk, and the quantized Hall effect."),
            ("Neutrino Oscillation Physics", "Covers the phenomenon and theory of neutrinos changing flavor as they propagate."),
            ("Holographic Principle and AdS/CFT Correspondence", "Introduces the conjectured duality between gravitational theories and lower-dimensional quantum field theories."),
            ("Physics of Metamaterials and Negative Refraction", "Examines engineered materials with electromagnetic properties not found in nature, including negative refraction."),
        ],
    },
    "Project Management": {
        "UG4": [
            ("Critical Path Drag and Drag Cost Analysis", "Covers quantifying how much each critical path activity delays the overall project schedule."),
            ("Monte Carlo Schedule Risk Simulation", "Examines using Monte Carlo simulation to model probabilistic project completion dates."),
            ("Resource Leveling versus Resource Smoothing", "Distinguishes techniques for resolving resource overallocation with and without extending the schedule."),
            ("Program Management and Benefits Realization", "Covers coordinating related projects as a program to deliver benefits beyond individual project scope."),
            ("Portfolio Prioritization Using Weighted Scoring Models", "Examines scoring models used to rank and select projects within a portfolio."),
            ("Risk Register Development and Maintenance", "Covers building and maintaining a living register of identified project risks and responses."),
            ("Qualitative versus Quantitative Risk Analysis Techniques", "Compares subjective risk ranking methods with numerical probability and impact modeling."),
            ("Decision Tree Analysis for Project Risk", "Examines using decision trees to evaluate project choices under uncertain outcomes."),
            ("Reserve Analysis: Contingency and Management Reserves", "Distinguishes budget reserves set aside for known risks from those held for unforeseen events."),
            ("Project Charter Development and Sponsor Alignment", "Covers drafting a project charter that secures sponsor authorization and objective alignment."),
            ("RACI Matrix Design for Role Clarity", "Examines building a Responsible-Accountable-Consulted-Informed matrix to clarify project roles."),
            ("Managing Virtual Teams Across Time Zones", "Covers practices for coordinating distributed project teams working across different time zones."),
            ("Conflict Resolution Techniques in Project Teams", "Examines structured approaches for resolving interpersonal and technical conflict on project teams."),
            ("Servant Leadership in Agile Project Environments", "Covers the servant leadership model as applied to supporting self-organizing agile teams."),
            ("Extreme Programming Practices in Project Delivery", "Examines XP practices such as pair programming and continuous integration within project delivery."),
            ("Feature-Driven Development Methodology", "Covers the feature-driven development approach to planning and delivering software by client-valued features."),
            ("Hybrid Agile-Waterfall Project Frameworks", "Examines frameworks that blend predictive and adaptive methods within a single project lifecycle."),
            ("Definition of Done and Acceptance Criteria Design", "Covers crafting clear completion and acceptance standards for agile project deliverables."),
            ("Retrospective Facilitation Techniques", "Examines facilitation methods for running effective team retrospectives that drive improvement."),
            ("Program Increment Planning in Scaled Agile", "Covers the cadence-based planning event used to align multiple agile teams in scaled frameworks."),
            ("Project Portfolio Governance Structures", "Examines governance bodies and processes that oversee an organization's project portfolio."),
            ("Project Risk Appetite and Tolerance Frameworks", "Covers defining an organization's willingness to accept risk within project decision-making."),
            ("Configuration Management for Project Deliverables", "Examines controlling and tracking changes to a project's technical deliverables over time."),
            ("Organizational Project Management Maturity Models", "Covers frameworks such as OPM3 for assessing and improving an organization's project management maturity."),
            ("Fast-Tracking and Schedule Crashing Techniques", "Compares overlapping activities and adding resources as techniques for compressing a project schedule."),
        ],
    },
    "Prompt Engineering": {
        "UG4": [
            ("Prompt Engineering for Code Review Assistants", "Covers designing prompts that guide models to give accurate, actionable code review feedback."),
            ("Negative Prompting and Exclusion Constraints", "Examines techniques for instructing models on what to avoid producing in their output."),
            ("Prompt Engineering for Structured Extraction from Unstructured Text", "Covers designing prompts that reliably pull structured fields out of free-form text."),
            ("Meta-Prompting: Prompts That Generate Prompts", "Examines using a model to design or refine prompts for another downstream task."),
            ("Prompt Engineering for Voice Assistant Interfaces", "Covers adapting prompt design for the constraints and turn-taking of spoken voice interactions."),
            ("Context Window Budget Management Strategies", "Examines strategies for allocating limited context window space among instructions, history, and retrieved content."),
            ("Prompt Engineering for Educational Tutoring Systems", "Covers designing prompts that guide models to scaffold learning rather than give direct answers."),
        ],
    },
    "Python": {
        "UG4": [
            ("Building Type-Safe Data Pipelines with mypy", "Covers using static type checking to catch data pipeline errors before runtime."),
            ("Python Async Web Frameworks (Starlette and AIOHTTP)", "Examines building asynchronous web applications with lightweight async-first Python frameworks."),
            ("Python Bindings for Rust Extensions with PyO3", "Covers writing performance-critical extensions in Rust and exposing them to Python via PyO3."),
            ("Python Interfacing with Hardware via GPIO and Serial Ports", "Examines controlling hardware devices from Python through GPIO pins and serial communication."),
            ("Python for Scientific Computing with SciPy Optimization", "Covers using SciPy's optimization routines for solving scientific and engineering problems."),
            ("Building Command Bots with Python (Discord and Slack APIs)", "Examines building interactive chat bots using the Discord and Slack platform APIs."),
            ("Python Memory Profiling with tracemalloc", "Covers using tracemalloc to trace memory allocations and diagnose memory growth in Python programs."),
        ],
    },
    "R": {
        "UG4": [
            ("Bayesian Network Modeling in R (bnlearn)", "Covers learning and inference with Bayesian networks using the bnlearn package."),
            ("Building R Packages with Compiled Fortran Code", "Examines integrating legacy compiled Fortran routines into R packages for performance."),
            ("R for Ecological Niche Modeling", "Covers using R to model species distributions based on environmental predictor variables."),
            ("Time-to-Event Machine Learning in R (randomForestSRC)", "Examines random forest methods for survival analysis using the randomForestSRC package."),
        ],
    },
    "Science": {
        "UG4": [
            ("The Anthropocene as a Geological and Scientific Concept", "Examines the scientific debate over defining a new geological epoch shaped by human activity."),
        ],
    },
    "Social Studies": {
        "UG4": [
            ("Sociology of Sport and Social Identity", "Examines how organized sport shapes and reflects social identity, class, and community belonging."),
            ("Diaspora Studies and Transnational Communities", "Covers how dispersed communities maintain identity and connection across national borders."),
            ("Sociology of Consumption and Material Culture", "Examines how consumption patterns and material goods construct social meaning and identity."),
            ("Youth Subcultures and Generational Identity", "Covers how youth subcultures form distinct identities in relation to mainstream generational norms."),
        ],
    },
    "UI/UX Design": {
        "UG4": [
            ("Biometric Authentication UX Patterns", "Examines interface design considerations for fingerprint, facial, and other biometric authentication flows."),
            ("Skeuomorphism versus Flat Design: Historical Design Debates", "Traces the design shift from realistic skeuomorphic interfaces to flat, minimal visual language."),
            ("Design for Wearable Device Interfaces", "Covers interface design constraints and patterns specific to small-screen wearable devices."),
            ("Progressive Disclosure Patterns for Complex Workflows", "Examines revealing interface complexity gradually to avoid overwhelming users in complex workflows."),
            ("Design Localization Beyond Translation (Cultural UX Adaptation)", "Covers adapting layout, imagery, and interaction patterns to different cultural contexts beyond text translation."),
            ("Zero UI and Ambient Interface Design", "Examines interfaces that minimize visible controls in favor of ambient, sensor-driven interaction."),
        ],
    },
    "Web Development": {
        "UG4": [
            ("Building Multiplayer Web Experiences with WebRTC Data Channels", "Covers using WebRTC data channels to build low-latency, peer-to-peer multiplayer web experiences."),
            ("Static Analysis for Web Bundle Size Auditing", "Examines tools and techniques for auditing and reducing JavaScript bundle size in web applications."),
        ],
    },
    "World History": {
        "UG4": [
            ("The Congress of Vienna and the Concert of Europe", "Examines the post-Napoleonic diplomatic settlement that shaped nineteenth-century European order."),
            ("The Suez Crisis and Postcolonial Middle East Politics", "Analyzes the 1956 Suez Crisis as a turning point in postcolonial Middle Eastern geopolitics."),
            ("The Bandung Conference and Afro-Asian Solidarity", "Examines the 1955 Bandung Conference as a foundation for postcolonial Afro-Asian political solidarity."),
        ],
    },
    "World Literature": {
        "UG4": [
            ("Dante's Divine Comedy and the Allegorical Tradition", "Examines Dante's journey through the afterlife as a landmark of medieval allegorical literature."),
            ("Cervantes and the Birth of the Modern Novel Form", "Studies how Don Quixote's narrative innovations shaped the emergence of the modern novel."),
            ("Goethe's Faust and the Literature of the Pact", "Examines the Faustian bargain narrative tradition through Goethe's dramatic poem."),
            ("Icelandic Sagas and Norse Narrative Tradition", "Surveys the medieval Icelandic saga tradition and its distinctive prose narrative style."),
            ("The Nibelungenlied and Germanic Epic Tradition", "Studies the medieval German epic and its place in the broader Germanic heroic tradition."),
            ("Chinese Vernacular Fiction: Journey to the West", "Examines the classic vernacular novel as a landmark of Ming-era Chinese fiction."),
            ("The Panchatantra and Fable Traditions Across Asia", "Traces the influence of the Panchatantra's animal fables across Asian and world literary traditions."),
            ("Ottoman Divan Poetry and Court Literary Culture", "Examines the formal conventions and courtly context of classical Ottoman Divan poetry."),
            ("Yiddish Literature and the Eastern European Jewish Experience", "Surveys Yiddish literary tradition as a record of Eastern European Jewish life and culture."),
            ("Scandinavian Modernism: Ibsen and the Problem Play", "Examines Ibsen's development of the problem play and its influence on modern drama."),
        ],
    },
}
