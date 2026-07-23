MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "AI Tools": {
        "UG3": [
            ("AI Tools for Wildlife Camera-Trap Species Identification", "Explores how conservation biologists use AI-powered image classifiers to automatically identify species captured by remote camera traps."),
        ],
    },
    "Art": {
        "UG3": [
            ("Fore-edge Painting: Hidden Imagery on Book Edges", "Examines the historical technique of painting scenes on the fanned edges of a book's pages so the image appears only when the pages are splayed."),
        ],
    },
    "Artificial Intelligence": {
        "UG3": [
            ("The Perceptron Convergence Theorem", "Studies the mathematical proof guaranteeing that Rosenblatt's perceptron learning rule converges on linearly separable data."),
            ("AlphaGo's Move 37 and Its Impact on Go Theory", "Analyzes the famous unconventional move from the AlphaGo versus Lee Sedol match and its influence on human Go strategy."),
            ("The ELIZA Effect and Early Chatbot Psychology", "Investigates why users attributed understanding to Weizenbaum's simple ELIZA program and what this reveals about human-AI interaction."),
            ("Watson's Jeopardy! Victory: System Design", "Reviews the architecture behind IBM Watson's competition-winning performance on the quiz show Jeopardy!."),
            ("The AI Winter of the 1970s: Causes and Recovery", "Traces the funding collapse and renewed skepticism toward AI research during the 1970s and how the field eventually rebounded."),
            ("Moravec's Paradox in Robotics and Cognition", "Explores the observation that high-level reasoning requires little computation while sensorimotor skills demand enormous computational resources."),
        ],
    },
    "Big Data": {
        "UG3": [
            ("The CAP Theorem's Origins: Brewer's Conjecture", "Traces Eric Brewer's original conjecture about consistency, availability, and partition tolerance and its formalization in distributed systems."),
            ("The Netflix Prize and Its Legacy for Recommendation Research", "Examines the influential open competition that advanced collaborative filtering research and shaped modern recommender systems."),
            ("Google's MapReduce Paper and the Birth of Big Data Processing", "Studies the foundational 2004 paper that introduced the MapReduce programming model underlying much of big data infrastructure."),
            ("Big Data Pipelines Behind the Large Hadron Collider", "Reviews how CERN's Large Hadron Collider generates and processes petabytes of particle-collision data through distributed pipelines."),
        ],
    },
    "Biology": {
        "UG3": [
            ("The Human Genome Project: A Historical Case Study", "Reviews the international effort to sequence the human genome and its lasting impact on genomics and biotechnology."),
            ("The Asilomar Conference and the Governance of Recombinant DNA", "Examines the 1975 scientific conference that established early safety guidelines for recombinant DNA research."),
            ("Henrietta Lacks and the HeLa Cell Line", "Explores the origin of the HeLa immortal cell line and its scientific and ethical legacy in biomedical research."),
        ],
    },
    "Business Analytics": {
        "UG3": [
            ("The Moneyball Case Study: Analytics in Baseball Recruitment", "Analyzes how the Oakland Athletics used statistical analytics to identify undervalued baseball players on a limited budget."),
            ("Target's Pregnancy-Prediction Model: A Predictive Analytics Case Study", "Examines the retail analytics model that inferred customer pregnancy from purchase patterns and the privacy debate it sparked."),
            ("Zara's Fast-Fashion Demand-Sensing Analytics", "Studies how Zara's supply chain analytics rapidly translate sales data into design and inventory decisions."),
        ],
    },
    "Chemistry": {
        "UG3": [
            ("The Haber-Bosch Process: A Case Study in Industrial Chemistry", "Reviews the nitrogen-fixation process that revolutionized fertilizer production and its chemical and historical significance."),
            ("The Thalidomide Tragedy and Stereochemistry", "Examines how differing effects of drug enantiomers in thalidomide led to lasting changes in pharmaceutical chemistry regulation."),
            ("The Ozone Hole and the Chemistry of CFCs: The Montreal Protocol", "Studies the atmospheric chemistry of chlorofluorocarbons and the international agreement that phased them out."),
        ],
    },
    "Cloud Computing": {
        "UG3": [
            ("The 2017 AWS S3 Outage: A Case Study in Cloud Resilience", "Analyzes the widespread outage caused by a mistyped command and its lessons for designing resilient cloud storage systems."),
            ("Netflix's Chaos Monkey: Origins and Design Philosophy", "Examines the tool Netflix built to randomly terminate production instances and its role in shaping resilience engineering."),
        ],
    },
    "Coding": {
        "UG3": [
            ("The Y2K Bug: A Case Study in Legacy Code Risk", "Reviews the global effort to fix date-handling bugs before the year 2000 and its lessons for long-lived software systems."),
            ("The Therac-25 Software Failures: A Case Study in Safety-Critical Bugs", "Examines the radiation therapy machine's fatal software race conditions and their impact on safety-critical coding practices."),
            ("The Knight Capital Trading Glitch: A Case Study in Deployment Risk", "Studies how a botched software deployment caused a trading firm to lose hundreds of millions of dollars in minutes."),
        ],
    },
    "Computer Science Engineering": {
        "UG3": [
            ("The Morris Worm: A Case Study in Early Network Security Failures", "Analyzes the 1988 self-replicating program that disrupted the early internet and spurred formal incident response practices."),
            ("The Pentium FDIV Bug: A Case Study in Hardware Verification", "Reviews the floating-point division flaw in early Pentium processors and its impact on hardware testing methodology."),
            ("The Ariane 5 Flight 501 Failure: A Case Study in Software Reuse Risk", "Examines how a reused overflow-prone module caused the rocket's destruction seconds after launch."),
        ],
    },
    "Cooking": {
        "UG3": [
            ("Peking Duck: Historical Technique and Lacquering Method", "Traces the centuries-old preparation method for Peking duck, including air-drying and maltose-glaze lacquering."),
        ],
    },
    "Critical Thinking": {
        "UG3": [
            ("The Challenger Disaster: A Case Study in Groupthink and Risk Assessment", "Analyzes the organizational reasoning failures behind the decision to launch the Challenger despite engineering warnings."),
            ("The Sokal Affair and Its Lessons for Peer Review", "Examines the hoax paper submitted to expose weaknesses in academic peer review and editorial reasoning."),
            ("The Milgram Experiment and Its Implications for Obedience Reasoning", "Studies Stanley Milgram's obedience experiments and what they reveal about authority, conformity, and moral reasoning."),
        ],
    },
    "Cybersecurity": {
        "UG3": [
            ("The Stuxnet Worm: Anatomy of a Nation-State Cyberattack", "Dissects the sophisticated worm that sabotaged Iranian centrifuges and redefined state-sponsored cyber warfare."),
            ("The Mirai Botnet and IoT Device Exploitation", "Examines how default credentials on insecure IoT devices were exploited to build a massive DDoS botnet."),
            ("The Equifax Breach: A Case Study in Patch Management Failure", "Reviews how an unpatched vulnerability led to one of the largest consumer data breaches in history."),
            ("The SolarWinds Supply Chain Attack", "Analyzes the compromised software update mechanism used to infiltrate numerous government and corporate networks."),
            ("The WannaCry Ransomware Outbreak: EternalBlue Exploitation", "Studies how a leaked NSA exploit was weaponized into a self-propagating ransomware worm affecting systems worldwide."),
        ],
    },
    "Data Science": {
        "UG3": [
            ("The Signal and the Noise: Nate Silver's Election Forecasting Methodology", "Examines the statistical forecasting approach popularized in election prediction modeling."),
            ("The Google Flu Trends Failure: A Case Study in Model Overfitting", "Analyzes why a search-based flu prediction model dramatically overestimated outbreaks and what it teaches about overfitting."),
            ("The COMPAS Recidivism Algorithm Controversy", "Studies the criminal justice risk-assessment tool at the center of debates over algorithmic bias and fairness."),
            ("The Cambridge Analytica Case Study in Data Ethics", "Reviews the unauthorized use of social media data for political targeting and its impact on data ethics practice."),
        ],
    },
    "Digital Marketing": {
        "UG3": [
            ("The Old Spice 'The Man Your Man Could Smell Like' Campaign Case Study", "Analyzes the viral video advertising campaign and its impact on brand engagement and digital marketing strategy."),
            ("Dove's Real Beauty Campaign: Brand Strategy Case Study", "Examines how Dove's advertising campaign reshaped brand identity around inclusive beauty standards."),
            ("The Oreo 'Dunk in the Dark' Super Bowl Tweet Case Study", "Studies the real-time social media response during a stadium blackout that became a landmark case in reactive marketing."),
        ],
    },
    "English": {
        "UG3": [
            ("Oulipo and Constrained Writing Techniques", "Explores the literary movement that used self-imposed formal constraints, such as lipograms, to generate new writing."),
            ("The Pearl Poet and Sir Gawain and the Green Knight", "Studies the anonymous medieval poem's alliterative verse form and its themes of chivalry and temptation."),
        ],
    },
    "Finance": {
        "UG3": [
            ("The Long-Term Capital Management Collapse: A Case Study in Leverage Risk", "Examines how the highly leveraged hedge fund's near-collapse threatened the broader financial system in 1998."),
            ("The Flash Crash of 2010: High-Frequency Trading Case Study", "Analyzes the sudden intraday market plunge linked to high-frequency algorithmic trading behavior."),
        ],
    },
    "First Aid": {
        "UG3": [
            ("The Heimlich Maneuver: Origins and Development History", "Traces Dr. Henry Heimlich's development of the abdominal thrust technique for relieving choking."),
            ("The 1952 Copenhagen Polio Epidemic and the Birth of Modern Resuscitation", "Reviews how a polio epidemic drove the development of manual positive-pressure ventilation techniques."),
        ],
    },
    "General Knowledge": {
        "UG3": [
            ("The Dewey Decimal System: Origins and Structure", "Explores Melvil Dewey's library classification system and its enduring influence on organizing knowledge."),
            ("The Rosetta Stone and the Decipherment of Hieroglyphs", "Examines how the trilingual inscription enabled scholars to finally decode ancient Egyptian hieroglyphic writing."),
            ("The Antikythera Mechanism: An Ancient Analog Computer", "Studies the ancient Greek geared device used to predict astronomical positions and eclipses."),
        ],
    },
    "Geography": {
        "UG3": [
            ("The Aral Sea Disaster: A Case Study in Anthropogenic Environmental Change", "Analyzes how Soviet-era irrigation projects caused one of the world's largest inland seas to nearly vanish."),
            ("The Panama Canal: Geopolitics and Engineering Geography", "Reviews the canal's construction, its geographic significance, and its ongoing role in global trade routes."),
            ("The Nazca Lines: Geography and Archaeological Interpretation", "Examines the enormous geoglyphs etched into the Peruvian desert and competing theories about their purpose."),
        ],
    },
    "ICT & Computer Science": {
        "UG3": [
            ("The ARPANET's First Message: A Case Study in Network History", "Reviews the 1969 transmission between UCLA and Stanford that marked the beginning of packet-switched networking."),
        ],
    },
    "Islamic Studies": {
        "UG3": [
            ("Ibn Battuta's Travels and the Geography of the Islamic World", "Surveys the fourteenth-century scholar's extensive journeys across the Islamic world and their historical and geographic significance."),
        ],
    },
    "JavaScript": {
        "UG3": [
            ("The 10-Day Creation of JavaScript by Brendan Eich", "Traces the rapid original design of JavaScript at Netscape and how early constraints shaped the language."),
            ("The Left-Pad Incident: A Case Study in npm Package Fragility", "Examines how the removal of a tiny npm package broke countless builds and prompted changes to package registry policy."),
        ],
    },
    "MBA": {
        "UG3": [
            ("The Kodak Case Study: Disruptive Innovation and Strategic Failure", "Analyzes how Kodak's own invention of digital photography failed to prevent its strategic decline."),
        ],
    },
    "Machine Learning": {
        "UG3": [
            ("The ImageNet Moment: AlexNet and the 2012 Deep Learning Breakthrough", "Reviews how AlexNet's decisive ImageNet competition win in 2012 catalyzed the modern deep learning era."),
            ("Matrix Factorization Techniques Behind the Netflix Prize", "Examines the latent-factor matrix factorization methods that proved decisive in the Netflix Prize competition."),
            ("AlphaGo versus Lee Sedol: A Case Study in Deep Reinforcement Learning", "Studies the historic match in which AlphaGo defeated a world-champion Go player using deep reinforcement learning."),
            ("The Perceptron Winter: Minsky and Papert's Critique of Early Neural Networks", "Analyzes how a 1969 book's critique of perceptrons contributed to reduced neural network research funding."),
            ("Word2Vec's Skip-Gram Architecture: Origins and Design", "Explores the skip-gram model that popularized dense word embeddings learned from large text corpora."),
            ("The Viola-Jones Algorithm for Real-Time Face Detection", "Reviews the cascade-based algorithm that made real-time face detection practical on early consumer hardware."),
            ("LeNet-5 and the Origins of Convolutional Neural Networks", "Studies Yann LeCun's pioneering convolutional architecture developed for handwritten digit recognition."),
            ("The Universal Approximation Theorem for Neural Networks", "Examines the theoretical result showing that sufficiently large feedforward networks can approximate any continuous function."),
            ("Breiman's Original Random Forest Algorithm", "Traces Leo Breiman's formulation of the random forest ensemble method and its statistical foundations."),
            ("The Vapnik-Chervonenkis Dimension and Learning Theory", "Explores the VC dimension as a measure of model capacity underlying statistical learning theory."),
            ("The XOR Problem and the Limits of Single-Layer Perceptrons", "Studies the classic example demonstrating why single-layer perceptrons cannot represent non-linearly separable functions."),
            ("Cortes and Vapnik's Original Support Vector Machine Formulation", "Reviews the foundational paper that introduced the soft-margin support vector machine algorithm."),
            ("The MNIST Dataset: Origins and Its Role as a Benchmark", "Examines how the MNIST handwritten digit dataset became a standard benchmark for machine learning research."),
        ],
    },
    "Math": {
        "UG3": [
            ("The Bridges of Königsberg and the Birth of Graph Theory", "Traces Euler's solution to the Königsberg bridge puzzle and its founding role in graph theory."),
            ("The Banach-Tarski Paradox", "Explores the counterintuitive theorem showing a sphere can be decomposed and reassembled into two spheres of the same size."),
            ("Fermat's Last Theorem and Wiles' Proof", "Reviews the centuries-old conjecture and Andrew Wiles' eventual proof using modern algebraic techniques."),
        ],
    },
    "Music": {
        "UG3": [
            ("The Rite of Spring Premiere Riot of 1913", "Examines the notorious audience reaction to Stravinsky's ballet premiere and its impact on modernist music."),
            ("John Cage's 4'33\" and the Concept of Silence in Music", "Studies the composition consisting entirely of silence and its challenge to conventional definitions of music."),
            ("The Amen Break and Its Influence on Sampling Culture", "Traces the six-second drum break's outsized influence on hip-hop, jungle, and drum-and-bass production."),
            ("Threnody to the Victims of Hiroshima: Penderecki's Sound Mass Technique", "Analyzes Penderecki's use of dense tone clusters and extended string techniques in this landmark composition."),
        ],
    },
    "Natural Language Processing": {
        "UG3": [
            ("The ELIZA Program and Early Natural Language Understanding", "Reviews Joseph Weizenbaum's pattern-matching chatbot and its role in early natural language processing history."),
            ("The Georgetown-IBM Experiment and Early Machine Translation", "Examines the 1954 demonstration that translated Russian sentences into English and spurred early machine translation research."),
            ("The ALPAC Report and Its Impact on Machine Translation Funding", "Studies the 1966 report that curtailed U.S. funding for machine translation research for over a decade."),
            ("SHRDLU and Blocks World Language Understanding", "Explores Terry Winograd's program that understood natural language commands within a simulated block world."),
            ("The Chomsky Hierarchy and Its Role in NLP Grammar Formalisms", "Reviews the classification of formal grammars and its influence on parsing and language modeling approaches."),
            ("The Winograd Schema Challenge", "Examines the pronoun-resolution benchmark designed to test commonsense reasoning in language systems."),
            ("The Loebner Prize and the Turing Test in Practice", "Studies the annual competition that applies the Turing Test to evaluate conversational AI systems."),
        ],
    },
    "Operations Management": {
        "UG3": [
            ("Toyota's Andon Cord System: A Case Study in Quality Control", "Examines the Toyota Production System mechanism allowing any worker to halt the line upon detecting a defect."),
            ("The Ford Assembly Line: Historical Origins of Mass Production", "Traces the introduction of the moving assembly line at Ford and its transformation of manufacturing operations."),
            ("FedEx's Hub-and-Spoke Model: A Logistics Case Study", "Reviews how FedEx's centralized sorting hub design revolutionized overnight package delivery operations."),
            ("Dell's Build-to-Order Model: A Case Study in Mass Customization", "Studies how Dell's direct-sales, build-to-order model reduced inventory while enabling product customization."),
            ("Amazon's Fulfillment Center Slotting Strategy Case Study", "Examines Amazon's chaotic storage and slotting approach for optimizing warehouse pick efficiency."),
            ("Southwest Airlines' Point-to-Point Turnaround Time Case Study", "Reviews how Southwest's operational practices minimize aircraft turnaround time to increase fleet utilization."),
        ],
    },
    "Philosophy": {
        "UG3": [
            ("The Trial of Socrates: Philosophy and Civic Order", "Examines the historical and philosophical dimensions of Socrates' trial and its implications for the relationship between philosophy and the state."),
            ("Diogenes the Cynic and the Practice of Philosophical Provocation", "Studies Diogenes' unconventional lifestyle and public acts as a form of philosophical argument against social convention."),
            ("Boethius's Consolation of Philosophy: Fortune and Reason", "Reviews the classic work composed in prison and its meditation on fortune, fate, and rational consolation."),
            ("Pascal's Wager: Decision Theory and Belief in God", "Explores Pascal's pragmatic argument for belief in God framed as a decision under uncertainty."),
            ("The Euthyphro Dilemma: Divine Command and Morality", "Examines the classic dilemma questioning whether morality is grounded in divine will or independent of it."),
            ("The Gettier Problem and the Definition of Knowledge", "Studies Edmund Gettier's counterexamples challenging the traditional justified-true-belief account of knowledge."),
            ("Buridan's Ass and the Problem of Rational Choice", "Reviews the thought experiment about a perfectly rational agent unable to choose between equally attractive options."),
        ],
    },
    "Physics": {
        "UG3": [
            ("The Michelson-Morley Experiment and the Search for the Aether", "Examines the experiment that failed to detect the luminiferous aether and helped pave the way for relativity."),
            ("The Manhattan Project: Physics and the Development of the Atomic Bomb", "Reviews the scientific and organizational effort behind the development of the first nuclear weapons."),
        ],
    },
    "Project Management": {
        "UG3": [
            ("The Sydney Opera House: A Case Study in Project Cost Overruns", "Analyzes the famous building project's massive schedule delays and cost overruns relative to its original plan."),
            ("The Big Dig: Boston's Central Artery Project Case Study", "Examines the complex urban highway project's cost escalation and engineering management challenges."),
            ("The Denver International Airport Baggage System Failure", "Reviews the automated baggage handling system failure that delayed the airport's opening by over a year."),
            ("The Channel Tunnel Project: Cross-Border Project Governance", "Studies the binational governance and engineering coordination required to deliver the Channel Tunnel."),
            ("The Hoover Dam Project: Scheduling and Resource Management Lessons", "Examines how the Hoover Dam was completed ahead of schedule through innovative scheduling and resource planning."),
            ("The Apollo Program: Systems Integration and Project Governance", "Reviews how NASA's Apollo program coordinated thousands of contractors and systems toward a fixed deadline."),
            ("The Millau Viaduct: Engineering Project Management Case Study", "Studies the project management practices behind constructing the world's tallest bridge on schedule."),
        ],
    },
    "Prompt Engineering": {
        "UG3": [
            ("The GPT-3 Paper and the Origins of Few-Shot In-Context Learning", "Reviews the paper demonstrating that large language models could perform tasks from a few examples in the prompt alone."),
            ("The 'DAN' Jailbreak: A Case Study in Prompt Security", "Examines the 'Do Anything Now' jailbreak pattern and what it reveals about prompt-based safety bypass techniques."),
            ("AutoGPT and the Rise of Autonomous Agent Prompting", "Studies the early autonomous agent framework that chained prompts to pursue multi-step goals without human intervention."),
            ("Wei et al.'s Original Chain-of-Thought Prompting Paper", "Reviews the research paper that first demonstrated chain-of-thought prompting's effect on multi-step reasoning."),
            ("The Stanford Alpaca Project: An Instruction-Tuning Case Study", "Examines how a small instruction-following dataset was used to fine-tune an open language model efficiently."),
            ("The Anthropic Constitutional AI Paper: A Case Study in Rule-Based Alignment", "Studies the approach of training models to critique and revise their own outputs according to a written set of principles."),
        ],
    },
    "Python": {
        "UG3": [
            ("The Zen of Python: Origins and Design Philosophy (PEP 20)", "Explores the guiding aphorisms behind Python's design philosophy and their influence on the language's style."),
            ("PEP 703: The Debate Over Removing Python's Global Interpreter Lock", "Reviews the proposal to make the GIL optional and its implications for Python concurrency."),
            ("The Origins of Jupyter from the IPython Project", "Traces how the IPython interactive shell evolved into the language-agnostic Jupyter notebook ecosystem."),
            ("Guido van Rossum's BDFL Retirement: A Python Governance Case Study", "Examines the transition of Python's governance model after its creator stepped down as Benevolent Dictator for Life."),
            ("The Python 2 to 3 Migration: A Case Study in Language Transition", "Studies the decade-long, community-wide effort to migrate the Python ecosystem from version 2 to version 3."),
            ("NumPy's Origins from Numeric and Numarray", "Traces how two competing array libraries were unified into NumPy, establishing Python's scientific computing foundation."),
            ("The Python Software Foundation and Open-Source Governance", "Reviews the nonprofit organization's role in stewarding Python's development, trademark, and community funding."),
            ("The Log4j-Style Risk of Python's pickle Deserialization", "Examines the security risks of deserializing untrusted data with Python's pickle module."),
        ],
    },
    "R": {
        "UG3": [
            ("Ross Ihaka and Robert Gentleman: R's Origins at the University of Auckland", "Traces how two statisticians created the R language as a free implementation inspired by the S language."),
            ("The S Language at Bell Labs and Its Influence on R's Design", "Reviews the statistical programming language developed at Bell Labs that directly shaped R's syntax and semantics."),
            ("The Comprehensive R Archive Network: History and Governance", "Examines the mirrored repository system that distributes and governs R packages worldwide."),
        ],
    },
    "Social Studies": {
        "UG3": [
            ("The Stanford Prison Experiment: Ethics and Social Psychology", "Examines the controversial simulated-prison study and its lasting influence on research ethics and social psychology."),
        ],
    },
    "UI/UX Design": {
        "UG3": [
            ("The Xerox Star: Origins of the Graphical User Interface", "Reviews the influential 1981 workstation that pioneered windows, icons, and the desktop metaphor."),
            ("Susan Kare's Icon Design for the Original Macintosh", "Studies the pixel-art icon design work that shaped the visual language of early graphical computing."),
            ("The 'Norman Door': A Case Study in Affordance Failure", "Examines Don Norman's famous example of confusing door design as a lens for understanding interface affordances."),
            ("The Netflix Homepage Redesign: A Data-Driven UX Case Study", "Reviews how Netflix used experimentation and behavioral data to iteratively redesign its browsing interface."),
        ],
    },
    "World History": {
        "UG3": [
            ("The Defenestration of Prague and the Start of the Thirty Years' War", "Examines the 1618 incident in which Protestant nobles threw royal officials from a castle window, igniting a continental war."),
            ("The Sykes-Picot Agreement and the Modern Middle East", "Reviews the secret World War I-era agreement between Britain and France that shaped modern Middle Eastern borders."),
            ("The Treaty of Tordesillas: Dividing the New World", "Studies the 1494 treaty in which Spain and Portugal divided newly discovered lands outside Europe between themselves."),
            ("The Xinhai Revolution and the Fall of China's Qing Dynasty", "Examines the 1911 revolution that ended over two thousand years of imperial rule in China."),
        ],
    },
}
