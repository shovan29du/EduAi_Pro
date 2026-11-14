"""Module topics bringing Social Studies, Physical Education &
Self-Defense, First Aid, and Physics up to 20+ lessons per level (C1
through M1)."""

_LEVELS = ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1"]

# Each subject is defined as 18 "spines" (real, specific topic areas), and
# each spine holds exactly 7 (title, summary) tuples ordered C1 -> M1, with
# the title and summary reflecting increasing academic rigor at each level.
# Flattening by level below yields 18 modules per level (126 per subject).

_SOCIAL_STUDIES_SPINES: list[list[tuple[str, str]]] = [
    # 1. Sociology fundamentals
    [
        ("Introduction to Sociology", "Introduces the sociological perspective, key thinkers such as Durkheim, Marx, and Weber, and core concepts like social facts, norms, and institutions."),
        ("Sociological Perspectives: Functionalism, Conflict, and Interactionism", "Compares the three classical theoretical paradigms in sociology and how each explains social order, inequality, and everyday interaction."),
        ("Sociological Theory: Classical Foundations", "Examines primary texts and arguments from Durkheim, Marx, and Weber in depth, situating their theories in the historical context of industrializing Europe."),
        ("Applied Sociology: Analyzing Contemporary Social Problems", "Applies sociological concepts and theories to case studies of contemporary issues such as inequality, crime, and institutional change."),
        ("Advanced Sociological Analysis", "Engages with contemporary sociological theory, including Bourdieu's field and habitus and Giddens' structuration theory, applied to advanced case analysis."),
        ("Sociology Practicum: Fieldwork and Analysis", "Guides students through a supervised sociological fieldwork project, from research design to data collection and thematic analysis."),
        ("Graduate Seminar in Sociological Theory", "A graduate-level seminar critically engaging with major and emerging schools of sociological theory and their methodological implications."),
    ],
    # 2. Cultural anthropology fundamentals
    [
        ("Introduction to Cultural Anthropology", "Surveys the concept of culture, cultural relativism, and the method of ethnographic fieldwork pioneered by anthropologists such as Franz Boas and Bronislaw Malinowski."),
        ("Kinship, Ritual, and Symbolism", "Explores how anthropologists analyze kinship systems, rites of passage, and symbolic meaning across diverse cultural contexts."),
        ("Anthropological Theory: Core Debates", "Covers major theoretical schools in anthropology, including structuralism, cultural materialism, and interpretive anthropology."),
        ("Ethnographic Methods in Practice", "Trains students in participant observation, interviewing, and field-note analysis as core ethnographic research techniques."),
        ("Advanced Cultural Anthropology", "Analyzes contemporary anthropological debates on globalization, identity, and postcolonial critique of the discipline."),
        ("Anthropology Capstone: Ethnographic Case Study", "Requires students to design and present an original ethnographic case study drawing on secondary source material."),
        ("Graduate Seminar in Anthropological Theory", "A graduate seminar examining the historical development and current controversies within cultural anthropological theory."),
    ],
    # 3. Social stratification and class
    [
        ("Introduction to Social Stratification", "Introduces the concept of social stratification and the major dimensions along which societies rank individuals, including wealth, income, and status."),
        ("Social Class and Mobility", "Examines how social class is defined and measured, and the factors that promote or restrict intergenerational mobility."),
        ("Theories of Social Inequality", "Compares functionalist, conflict, and Weberian explanations for why social stratification exists and persists."),
        ("Measuring Inequality: Data and Methods", "Introduces quantitative measures of inequality such as the Gini coefficient and their use in comparative social research."),
        ("Advanced Studies in Class and Inequality", "Explores intersections between class, race, and gender in the reproduction of inequality across generations."),
        ("Capstone: Analyzing Inequality in a Chosen Society", "Requires an original research project analyzing patterns of stratification within a specific national or regional context."),
        ("Graduate Theory: Class and Power", "A graduate-level examination of contemporary theories linking class position to political and economic power."),
    ],
    # 4. Race and ethnicity studies
    [
        ("Introduction to Race and Ethnicity", "Introduces race and ethnicity as social constructs, distinguishing them from biological categories and outlining their historical formation."),
        ("Ethnic Identity and Group Boundaries", "Explores how ethnic identity is formed, maintained, and negotiated at group boundaries in multicultural societies."),
        ("Theories of Racial Formation", "Covers key theoretical frameworks, including Omi and Winant's racial formation theory, for understanding how racial categories change over time."),
        ("Applied Analysis: Race, Policy, and Institutions", "Applies theories of race and ethnicity to the study of institutional policy, including education and criminal justice."),
        ("Advanced Race and Ethnicity Studies", "Critically examines intersectionality and comparative approaches to race across different national contexts."),
        ("Capstone: Race and Ethnicity Case Study", "Guides an independent research project examining a specific historical or contemporary case of racial or ethnic dynamics."),
        ("Graduate Seminar: Critical Race Theory", "A graduate seminar surveying the origins and central arguments of critical race theory and its interdisciplinary influence."),
    ],
    # 5. Gender studies fundamentals
    [
        ("Introduction to Gender Studies", "Introduces the distinction between sex and gender and surveys how gender roles and expectations vary across cultures and history."),
        ("Gender Socialization and Identity", "Examines how gender identity develops through socialization processes in family, education, and media."),
        ("Feminist Theory: Core Frameworks", "Surveys major strands of feminist theory, including liberal, radical, and intersectional feminism."),
        ("Applied Gender Analysis", "Applies gender theory to case studies in the workplace, politics, and health policy."),
        ("Advanced Gender Studies", "Explores contemporary debates on masculinity studies, queer theory, and the social construction of gender categories."),
        ("Capstone: Gender and Social Institutions", "Requires an original analysis of how a chosen social institution shapes or is shaped by gender norms."),
        ("Graduate Theory: Gender and Power", "A graduate-level exploration of the relationship between gender, power, and social structure in contemporary theory."),
    ],
    # 6. Social psychology fundamentals
    [
        ("Introduction to Social Psychology", "Introduces how individual thought and behavior are shaped by social context, covering topics such as conformity and attribution."),
        ("Group Dynamics and Conformity", "Examines classic studies of group influence, including Asch's conformity experiments and Milgram's obedience studies, and their ethical legacy."),
        ("Theories of Attitude and Persuasion", "Covers cognitive dissonance theory and models of attitude change and persuasion."),
        ("Applied Social Psychology", "Applies social psychological principles to real-world settings such as organizations, health behavior, and intergroup conflict."),
        ("Advanced Social Psychology", "Explores contemporary research on implicit bias, social identity theory, and intergroup relations."),
        ("Capstone: Designing a Social Psychology Study", "Guides students through designing an ethical social psychology research proposal based on an existing body of literature."),
        ("Graduate Seminar in Social Psychology", "A graduate seminar critically reviewing current empirical research and theory in social psychology."),
    ],
    # 7. Social movements and collective action
    [
        ("Introduction to Social Movements", "Introduces the concept of social movements and surveys historical examples such as labor, civil rights, and environmental movements."),
        ("Collective Action and Mobilization", "Examines how movements mobilize resources and participants, drawing on resource mobilization theory."),
        ("Theories of Social Movements", "Covers political process theory and framing theory as explanations for the emergence and success of social movements."),
        ("Case Studies in Social Movements", "Analyzes specific historical social movements to evaluate competing theoretical explanations for their outcomes."),
        ("Advanced Studies in Collective Action", "Explores transnational social movements and the role of digital media in contemporary mobilization."),
        ("Capstone: Social Movement Case Analysis", "Requires an original comparative analysis of two or more social movements using course theoretical frameworks."),
        ("Graduate Theory: Contentious Politics", "A graduate-level examination of contentious politics theory linking social movements to broader political change."),
    ],
    # 8. Urban sociology
    [
        ("Introduction to Urban Sociology", "Introduces the sociological study of cities, including urbanization trends and the classic Chicago School approach to city life."),
        ("Neighborhoods and Community Life", "Examines how neighborhood structure and social ties shape community cohesion and everyday urban life."),
        ("Theories of the City", "Covers major urban theories, including the Chicago School's concentric zone model and later critiques."),
        ("Applied Urban Analysis", "Applies urban sociological concepts to case studies of housing, gentrification, and urban planning."),
        ("Advanced Urban Sociology", "Explores global urbanization, informal settlements, and comparative urban inequality."),
        ("Capstone: Urban Case Study", "Requires an original research project analyzing social dynamics within a specific city or urban district."),
        ("Graduate Seminar in Urban Theory", "A graduate seminar engaging with contemporary debates in urban theory and the political economy of city space."),
    ],
    # 9. Family and kinship structures
    [
        ("Introduction to Family and Kinship", "Introduces the diversity of family structures and kinship systems found across different cultures and historical periods."),
        ("Comparative Family Structures", "Compares nuclear, extended, and non-traditional family arrangements across societies."),
        ("Theories of Family and Kinship", "Covers structural-functionalist and conflict perspectives on the role of family in society."),
        ("Applied Family Studies", "Applies theories of family and kinship to contemporary issues such as divorce, blended families, and caregiving."),
        ("Advanced Studies in Family Sociology", "Examines how globalization and migration reshape family and kinship networks."),
        ("Capstone: Family Structure Case Study", "Requires an original comparative study of family structure in two distinct cultural contexts."),
        ("Graduate Theory: Kinship and Social Organization", "A graduate-level exploration of classical and contemporary kinship theory within anthropology and sociology."),
    ],
    # 10. Deviance and social control
    [
        ("Introduction to Deviance and Social Control", "Introduces the sociological concept of deviance and the formal and informal mechanisms societies use to enforce norms."),
        ("Labeling and Social Reaction", "Examines labeling theory and how societal reaction can shape deviant identity and behavior."),
        ("Theories of Deviance", "Covers strain theory, differential association, and control theory as explanations for deviant behavior."),
        ("Applied Criminology", "Applies theories of deviance to the study of crime patterns and the criminal justice system."),
        ("Advanced Studies in Deviance", "Explores critical criminology and the social construction of crime categories."),
        ("Capstone: Deviance Case Analysis", "Requires an original analysis applying deviance theory to a specific contemporary social problem."),
        ("Graduate Seminar in Criminological Theory", "A graduate seminar surveying the historical development of criminological theory and its policy implications."),
    ],
    # 11. Globalization and social change
    [
        ("Introduction to Globalization", "Introduces globalization as a process of increasing economic, cultural, and political interconnection among societies."),
        ("Cultural Globalization and Hybridity", "Examines how global cultural exchange produces hybrid identities and practices."),
        ("Theories of Social Change", "Covers modernization theory, dependency theory, and world-systems theory as frameworks for social change."),
        ("Applied Analysis of Global Social Change", "Applies theories of globalization to case studies of economic development and cultural change."),
        ("Advanced Globalization Studies", "Explores debates on global inequality, migration, and the role of transnational institutions."),
        ("Capstone: Globalization Case Study", "Requires an original research project analyzing globalization's impact on a specific region or sector."),
        ("Graduate Theory: World-Systems Analysis", "A graduate-level engagement with world-systems theory and its critics within global sociology."),
    ],
    # 12. Social research methods
    [
        ("Introduction to Social Research Methods", "Introduces the basic distinction between qualitative and quantitative research and the steps of the research process."),
        ("Survey Design and Sampling", "Covers the principles of questionnaire design and probability versus non-probability sampling techniques."),
        ("Qualitative Methods: Interviews and Ethnography", "Trains students in designing and conducting interviews and ethnographic observation."),
        ("Quantitative Methods: Data Analysis", "Introduces descriptive and inferential statistics as applied to social science survey data."),
        ("Advanced Research Design", "Covers mixed-methods research design and issues of validity, reliability, and research ethics."),
        ("Capstone: Original Research Proposal", "Requires students to design a complete original social research proposal, including methodology and ethical review considerations."),
        ("Graduate Seminar in Research Methodology", "A graduate-level seminar on advanced methodological debates in the social sciences."),
    ],
    # 13. Demography and population studies
    [
        ("Introduction to Demography", "Introduces basic demographic measures, including birth rate, death rate, and population growth rate."),
        ("Population Structure and Age Pyramids", "Examines how population age structure is represented and interpreted using population pyramids."),
        ("Theories of Population Change", "Covers the demographic transition model and its application to countries at different stages of development."),
        ("Applied Demographic Analysis", "Applies demographic methods to analyze fertility, mortality, and migration data from real populations."),
        ("Advanced Population Studies", "Explores population aging, urbanization trends, and their social and economic consequences."),
        ("Capstone: Demographic Case Study", "Requires an original demographic analysis of a specific country's population trends."),
        ("Graduate Theory: Population and Development", "A graduate-level examination of the relationship between population dynamics and economic development theory."),
    ],
    # 14. Media and society
    [
        ("Introduction to Media and Society", "Introduces how mass media shapes public opinion, culture, and social behavior."),
        ("Media Framing and Public Opinion", "Examines agenda-setting and framing theory as explanations for media's influence on public perception."),
        ("Theories of Media Effects", "Covers cultivation theory and uses-and-gratifications theory as frameworks for understanding audience response to media."),
        ("Applied Media Analysis", "Applies media theory to case studies of news coverage, advertising, and social media platforms."),
        ("Advanced Studies in Media and Society", "Explores the sociology of digital media, misinformation, and algorithmic content curation."),
        ("Capstone: Media Case Study", "Requires an original content analysis of media coverage on a chosen social issue."),
        ("Graduate Seminar in Media Sociology", "A graduate-level seminar examining contemporary theoretical debates on media's role in shaping society."),
    ],
    # 15. Education and society
    [
        ("Introduction to Sociology of Education", "Introduces how educational systems reflect and reproduce broader social structures and inequalities."),
        ("Schools and Socialization", "Examines the role of schools as agents of socialization alongside family and peer groups."),
        ("Theories of Education and Inequality", "Covers functionalist and conflict perspectives on the role of education in social mobility and reproduction."),
        ("Applied Analysis of Education Policy", "Applies sociological theory to the evaluation of education policy and school reform efforts."),
        ("Advanced Sociology of Education", "Explores comparative education systems and the effects of tracking and streaming on student outcomes."),
        ("Capstone: Education System Case Study", "Requires an original comparative study of educational outcomes across two school systems."),
        ("Graduate Theory: Education and Social Reproduction", "A graduate-level engagement with Bourdieu's theory of cultural capital and its application to education research."),
    ],
    # 16. Work and the economy (economic sociology)
    [
        ("Introduction to the Sociology of Work", "Introduces how work is socially organized and how occupational roles shape identity and status."),
        ("Labor Markets and Organizations", "Examines the structure of labor markets and how formal organizations shape work experience."),
        ("Theories of Economic Sociology", "Covers classical and contemporary theories on the relationship between economic activity and social structure."),
        ("Applied Economic Sociology", "Applies economic sociology to case studies of globalization's effect on labor and industry."),
        ("Advanced Studies in Work and Economy", "Explores the gig economy, automation, and their effects on employment relationships."),
        ("Capstone: Labor Market Case Study", "Requires an original analysis of labor market trends within a specific industry or region."),
        ("Graduate Seminar in Economic Sociology", "A graduate-level seminar on contemporary debates concerning markets, institutions, and social embeddedness."),
    ],
    # 17. Religion and society
    [
        ("Introduction to Sociology of Religion", "Introduces the sociological study of religion, including Durkheim's concept of the sacred and profane."),
        ("Religious Institutions and Practice", "Examines how religious institutions organize belief and practice within communities."),
        ("Theories of Religion and Society", "Covers Weber's Protestant ethic thesis and Durkheim's functionalist theory of religion."),
        ("Applied Analysis of Religion and Social Change", "Applies theories of religion to case studies of secularization and religious revival."),
        ("Advanced Sociology of Religion", "Explores religious pluralism, fundamentalism, and religion's role in political conflict."),
        ("Capstone: Religion and Society Case Study", "Requires an original analysis of a specific religious community's social role and organization."),
        ("Graduate Theory: Secularization Debates", "A graduate-level examination of competing theories on secularization and religious persistence in modern societies."),
    ],
    # 18. Social policy analysis & capstone project
    [
        ("Introduction to Social Policy", "Introduces the basic goals and tools of social policy, including welfare programs and public assistance."),
        ("Comparing Social Welfare Systems", "Compares approaches to social welfare provision across different national contexts."),
        ("Theories of the Welfare State", "Covers major typologies of welfare states and the political theories underpinning them."),
        ("Applied Social Policy Analysis", "Trains students in evaluating the intended and unintended effects of a specific social policy."),
        ("Advanced Social Policy Studies", "Explores debates on poverty reduction strategies and evidence-based policymaking."),
        ("Community Development Practicum", "Guides students through analyzing a community development initiative and proposing evidence-informed improvements."),
        ("Capstone Social Studies Research Project", "A graduate-level capstone requiring an original independent research project applying social science theory and methods to a chosen social issue."),
    ],
]

_PE_SELF_DEFENSE_SPINES: list[list[tuple[str, str]]] = [
    # 1. Exercise physiology fundamentals
    [
        ("Introduction to Exercise Physiology", "Introduces how the muscular, cardiovascular, and respiratory systems respond and adapt to physical exercise."),
        ("Energy Systems and Exercise", "Examines the aerobic and anaerobic energy systems the body uses to fuel activity of different intensities and durations."),
        ("Core Theory: Cardiorespiratory Adaptation", "Covers how sustained aerobic training produces adaptations in heart rate, stroke volume, and oxygen uptake (VO2 max)."),
        ("Applied Exercise Physiology", "Applies physiological principles to interpreting fitness test results and designing evidence-based training responses."),
        ("Advanced Exercise Physiology", "Explores muscle fiber types, lactate threshold, and the physiological basis of training adaptations at an advanced level."),
        ("Capstone: Exercise Physiology Case Study", "Requires an original analysis of an athlete's physiological training data to evaluate program effectiveness."),
        ("Graduate Seminar in Exercise Physiology", "A graduate-level seminar reviewing current research on human physiological responses to chronic and acute exercise."),
    ],
    # 2. Biomechanics of movement
    [
        ("Introduction to Biomechanics", "Introduces basic mechanical concepts, including force, torque, and leverage, as they apply to human movement."),
        ("Analyzing Movement Patterns", "Examines how joint angles and muscle activation patterns are analyzed to describe common movement patterns like walking and jumping."),
        ("Core Theory: Kinetics and Kinematics", "Covers the kinetic and kinematic principles used to describe and quantify human motion."),
        ("Applied Biomechanical Analysis", "Applies biomechanical principles to evaluate and improve technique in selected sports movements."),
        ("Advanced Biomechanics", "Explores advanced topics such as ground reaction forces and the biomechanics of injury mechanisms."),
        ("Capstone: Movement Analysis Project", "Requires students to conduct an original biomechanical analysis of a specific athletic movement."),
        ("Graduate Theory: Biomechanics of Human Performance", "A graduate-level examination of biomechanical research methods applied to elite athletic performance."),
    ],
    # 3. Sports psychology fundamentals
    [
        ("Introduction to Sports Psychology", "Introduces core concepts in sports psychology, including motivation, arousal, and the mental demands of competition."),
        ("Motivation and Goal Setting in Sport", "Examines theories of motivation and effective goal-setting techniques for athletic performance."),
        ("Core Theory: Arousal and Performance", "Covers the inverted-U hypothesis and other models describing the relationship between arousal and athletic performance."),
        ("Applied Mental Skills Training", "Applies psychological skills training techniques such as visualization and self-talk to improve athletic performance."),
        ("Advanced Sports Psychology", "Explores team cohesion, leadership, and the psychology of performance under pressure at an advanced level."),
        ("Capstone: Mental Skills Program Design", "Requires students to design a mental skills training program for a specific athlete or team scenario."),
        ("Graduate Seminar in Sports Psychology", "A graduate-level seminar critically examining current research on the psychological factors influencing athletic performance."),
    ],
    # 4. Strength and conditioning / capstone program design
    [
        ("Introduction to Strength and Conditioning", "Introduces basic principles of resistance training, including overload, specificity, and progression."),
        ("Foundations of Program Design", "Examines how training variables such as sets, repetitions, and rest periods are manipulated to meet different training goals."),
        ("Core Theory: Resistance Training Principles", "Covers the physiological basis for strength, hypertrophy, and power adaptations to resistance training."),
        ("Applied Program Design", "Applies strength and conditioning principles to design training programs for specific sports and goals."),
        ("Advanced Strength and Conditioning", "Explores advanced programming concepts, including autoregulation and concurrent training considerations."),
        ("Capstone: Comprehensive Training Program Design", "Requires students to design, justify, and present a complete multi-phase strength and conditioning program for a specific athlete population."),
        ("Graduate Seminar in Strength and Conditioning", "A graduate-level seminar evaluating current research evidence behind popular strength and conditioning methodologies."),
    ],
    # 5. Injury prevention and rehabilitation science
    [
        ("Introduction to Injury Prevention", "Introduces common causes of sports injuries and basic strategies used to reduce injury risk."),
        ("Understanding Common Sports Injuries", "Examines the mechanisms and classification of common sports injuries such as sprains, strains, and overuse injuries."),
        ("Core Theory: Tissue Healing and Rehabilitation", "Covers the physiological stages of soft tissue healing and how they inform rehabilitation timelines."),
        ("Applied Rehabilitation Principles", "Applies rehabilitation science to designing a progressive return-to-activity protocol following a common injury."),
        ("Advanced Injury Prevention Science", "Explores evidence-based injury prevention programs and screening tools used to identify at-risk athletes."),
        ("Capstone: Rehabilitation Case Study", "Requires an original case analysis proposing a rehabilitation plan for a specific sports injury scenario."),
        ("Graduate Theory: Sports Injury Epidemiology", "A graduate-level review of research methods used to study injury incidence and prevention efficacy in athletic populations."),
    ],
    # 6. Nutrition for athletic performance
    [
        ("Introduction to Sports Nutrition", "Introduces the roles of macronutrients and hydration in supporting athletic training and performance."),
        ("Fueling for Training and Competition", "Examines nutrient timing strategies for fueling before, during, and after exercise."),
        ("Core Theory: Macronutrient Metabolism in Exercise", "Covers how carbohydrate, fat, and protein metabolism shift during exercise of varying intensity and duration."),
        ("Applied Sports Nutrition Planning", "Applies nutrition science to design a sample eating plan supporting a specific athlete's training goals."),
        ("Advanced Sports Nutrition", "Explores the evidence behind ergogenic aids and supplementation claims relevant to athletic performance."),
        ("Capstone: Athlete Nutrition Case Study", "Requires an original nutrition plan proposal tailored to a specific sport and competition schedule."),
        ("Graduate Seminar in Sports Nutrition Science", "A graduate-level seminar reviewing current research evidence on nutritional strategies for athletic performance and recovery."),
    ],
    # 7. Coaching pedagogy
    [
        ("Introduction to Coaching Pedagogy", "Introduces foundational principles of teaching sports skills, including demonstration, feedback, and practice structure."),
        ("Communication and Feedback in Coaching", "Examines effective communication styles and feedback techniques used by coaches to support athlete development."),
        ("Core Theory: Coaching Philosophies", "Covers major coaching philosophies and models, including athlete-centered and autocratic coaching approaches."),
        ("Applied Coaching Methods", "Applies coaching pedagogy principles to plan and deliver a structured practice session."),
        ("Advanced Coaching Pedagogy", "Explores long-term athlete development models and their application across different age groups."),
        ("Capstone: Coaching Practicum", "Requires students to design and reflect on a coaching session plan grounded in pedagogical theory."),
        ("Graduate Seminar in Coaching Science", "A graduate-level seminar examining research on effective coaching practices and athlete development pathways."),
    ],
    # 8. Sports officiating and rules literacy
    [
        ("Introduction to Sports Officiating", "Introduces the role of officials and the basic rule structures common across organized sports."),
        ("Understanding Rules and Fair Play", "Examines how rules are structured to promote fairness, safety, and consistent competition."),
        ("Core Theory: Officiating Principles", "Covers positioning, signal communication, and decision-making frameworks used by sports officials."),
        ("Applied Officiating Practice", "Applies rules knowledge to officiate or evaluate a mock competitive scenario in a selected sport."),
        ("Advanced Rules Literacy and Dispute Resolution", "Explores complex rule interpretations and the procedures used to resolve on-field disputes."),
        ("Capstone: Officiating Case Study", "Requires an original analysis of a controversial officiating decision using relevant rule frameworks."),
        ("Graduate Theory: Governance of Sport Rules", "A graduate-level examination of how sports governing bodies develop and revise rules over time."),
    ],
    # 9. Adaptive physical education
    [
        ("Introduction to Adaptive Physical Education", "Introduces the goals of adaptive physical education and common accommodations for students with disabilities."),
        ("Inclusive Activity Design", "Examines strategies for modifying activities and equipment to include participants of varying abilities."),
        ("Core Theory: Disability and Physical Activity", "Covers models of disability and their implications for designing inclusive physical activity programs."),
        ("Applied Adaptive Program Design", "Applies adaptive physical education principles to design a modified activity session for a specific need."),
        ("Advanced Adaptive Physical Education", "Explores evidence-based adaptive sports programs and their role in participant well-being and inclusion."),
        ("Capstone: Adaptive Program Case Study", "Requires an original proposal for an inclusive physical activity program tailored to a specific population."),
        ("Graduate Seminar in Adaptive Physical Activity", "A graduate-level seminar reviewing research on inclusive physical activity and disability sport policy."),
    ],
    # 10. Motor learning and skill acquisition
    [
        ("Introduction to Motor Learning", "Introduces how motor skills are acquired through practice and feedback."),
        ("Stages of Skill Acquisition", "Examines Fitts and Posner's stages of motor learning, from cognitive to autonomous skill execution."),
        ("Core Theory: Motor Control Models", "Covers theoretical models of motor control, including schema theory and dynamical systems theory."),
        ("Applied Practice Design", "Applies motor learning principles to design practice schedules, including blocked versus random practice."),
        ("Advanced Motor Learning", "Explores contextual interference effects and transfer of learning in complex skill environments."),
        ("Capstone: Skill Acquisition Case Study", "Requires an original practice plan designed to teach a specific complex motor skill."),
        ("Graduate Seminar in Motor Learning", "A graduate-level seminar reviewing current research on motor learning theory and its practical applications."),
    ],
    # 11. Periodization theory for training
    [
        ("Introduction to Periodization", "Introduces the concept of organizing training into planned cycles to manage fatigue and peak performance."),
        ("Training Cycles: Macro, Meso, and Micro", "Examines how macrocycles, mesocycles, and microcycles structure a season of training."),
        ("Core Theory: Classical Periodization Models", "Covers linear and undulating periodization models and their theoretical rationale."),
        ("Applied Periodization Planning", "Applies periodization theory to construct a season-long training plan for a specific sport."),
        ("Advanced Periodization Concepts", "Explores block periodization and conjugate training methods used in advanced athletic preparation."),
        ("Capstone: Annual Training Plan", "Requires students to design a complete annual periodized training plan for a chosen athlete."),
        ("Graduate Seminar in Periodization Theory", "A graduate-level seminar evaluating the research evidence supporting different periodization models."),
    ],
    # 12. Self-defense theory and legal considerations
    [
        ("Introduction to Self-Defense Theory", "Introduces the core principles of self-defense, including awareness, avoidance, and proportional response."),
        ("Situational Awareness and De-escalation", "Examines techniques for recognizing threats early and de-escalating potentially violent situations."),
        ("Core Theory: Legal Principles of Self-Defense", "Covers the general legal concept of reasonable and proportional force in self-defense across common legal frameworks."),
        ("Applied Self-Defense Decision-Making", "Applies self-defense theory to scenario-based decision-making exercises."),
        ("Advanced Self-Defense Theory", "Explores the psychological and physiological effects of stress on decision-making during a self-defense encounter."),
        ("Capstone: Self-Defense Scenario Analysis", "Requires an original analysis of a self-defense case scenario addressing both tactical and legal considerations."),
        ("Graduate Seminar: Law and Ethics of Self-Defense", "A graduate-level seminar examining the legal and ethical frameworks that govern the use of force in self-defense."),
    ],
    # 13. Martial arts philosophy and history overview
    [
        ("Introduction to Martial Arts History", "Surveys the historical origins of major martial arts traditions across different world regions."),
        ("Philosophy and Discipline in Martial Arts", "Examines the philosophical principles, such as discipline and respect, embedded in traditional martial arts training."),
        ("Core Theory: Comparative Martial Arts Traditions", "Compares the technical and philosophical approaches of different martial arts traditions."),
        ("Applied Martial Arts Ethics", "Applies martial arts philosophy to discussions of sportsmanship, restraint, and responsible use of trained skill."),
        ("Advanced Martial Arts Studies", "Explores the evolution of modern combat sports from traditional martial arts roots."),
        ("Capstone: Martial Arts Tradition Case Study", "Requires an original research profile of a specific martial arts tradition's history and guiding philosophy."),
        ("Graduate Seminar in Martial Arts History and Philosophy", "A graduate-level seminar examining scholarly perspectives on the cultural history and philosophy of martial arts."),
    ],
    # 14. Team sports strategy and tactics
    [
        ("Introduction to Team Sports Strategy", "Introduces basic offensive and defensive concepts common across invasion and net/wall team sports."),
        ("Formations and Positional Play", "Examines how team formations and positional responsibilities structure gameplay."),
        ("Core Theory: Tactical Models in Team Sports", "Covers tactical periodization and game-based approaches to understanding team sport strategy."),
        ("Applied Tactical Analysis", "Applies tactical frameworks to analyze gameplay footage or scenarios from a selected team sport."),
        ("Advanced Team Sports Tactics", "Explores advanced tactical concepts, including transition play and set-piece strategy."),
        ("Capstone: Team Strategy Case Study", "Requires an original tactical game plan proposal for a specific team sport matchup."),
        ("Graduate Seminar in Sports Tactics Analysis", "A graduate-level seminar reviewing analytical methods used to study tactical decision-making in team sports."),
    ],
    # 15. Individual sports technique analysis
    [
        ("Introduction to Individual Sports Technique", "Introduces fundamental technique principles in individual sports such as track and field, swimming, or tennis."),
        ("Technique Refinement and Feedback", "Examines how coaches use observation and feedback to refine an athlete's individual sport technique."),
        ("Core Theory: Technical Models in Individual Sports", "Covers biomechanical technique models used as benchmarks in individual sport coaching."),
        ("Applied Technique Analysis", "Applies technique analysis tools to evaluate and provide feedback on an individual athlete's performance."),
        ("Advanced Individual Sports Analysis", "Explores video and data-based analysis methods used to fine-tune elite individual sport technique."),
        ("Capstone: Technique Improvement Case Study", "Requires an original technique analysis and improvement plan for a chosen individual athlete."),
        ("Graduate Seminar in Sports Technique Analysis", "A graduate-level seminar examining research methods for quantifying and improving individual sport technique."),
    ],
    # 16. Fitness assessment and testing methods
    [
        ("Introduction to Fitness Assessment", "Introduces common fitness tests used to assess cardiovascular endurance, strength, and flexibility."),
        ("Administering Fitness Tests", "Examines proper protocols for administering standardized fitness assessments safely and accurately."),
        ("Core Theory: Test Validity and Reliability", "Covers the concepts of validity and reliability as applied to fitness testing protocols."),
        ("Applied Fitness Testing", "Applies a battery of fitness tests to assess an individual and interpret the resulting data."),
        ("Advanced Fitness Assessment", "Explores laboratory-based assessment methods, including metabolic and body composition testing."),
        ("Capstone: Fitness Testing Battery Design", "Requires students to design a complete fitness testing battery appropriate for a specific population."),
        ("Graduate Seminar in Fitness Assessment Science", "A graduate-level seminar reviewing current research on the validity of fitness assessment protocols."),
    ],
    # 17. Exercise for special populations
    [
        ("Introduction to Exercise for Special Populations", "Introduces how exercise recommendations are adapted for populations such as older adults, children, and pregnant individuals."),
        ("Exercise Considerations Across the Lifespan", "Examines how exercise prescription differs across childhood, adulthood, and older age."),
        ("Core Theory: Chronic Disease and Exercise", "Covers the evidence base for exercise as a management strategy for chronic conditions such as diabetes and hypertension."),
        ("Applied Exercise Prescription", "Applies exercise prescription guidelines to design a safe program for a client with a specific health consideration."),
        ("Advanced Clinical Exercise Science", "Explores exercise programming for populations with cardiovascular or musculoskeletal conditions under professional supervision."),
        ("Capstone: Special Population Program Design", "Requires an original exercise program proposal designed for a specific special population case."),
        ("Graduate Seminar in Clinical Exercise Physiology", "A graduate-level seminar reviewing research on exercise interventions for clinical and special populations."),
    ],
    # 18. Sports management & recreation studies
    [
        ("Introduction to Sports Management", "Introduces the basic organizational structures behind sports teams, leagues, and recreational programs."),
        ("Recreation and Leisure Program Planning", "Examines how community recreation and leisure programs are planned and organized to meet participant needs."),
        ("Core Theory: Sport Organization and Governance", "Covers the governance structures of amateur and professional sports organizations."),
        ("Applied Sports Event Management", "Applies management principles to plan the logistics of a sports or recreation event."),
        ("Advanced Sports Management", "Explores marketing, sponsorship, and financial management issues within the sports industry."),
        ("Capstone: Recreation Program Proposal", "Requires students to design a complete community recreation program proposal, including budget and staffing considerations."),
        ("Graduate Seminar in Sports and Recreation Management", "A graduate-level seminar examining current issues in the management of sports organizations and recreation services."),
    ],
]

_FIRST_AID_SPINES: list[list[tuple[str, str]]] = [
    # 1. Advanced wound care principles
    [
        ("Introduction to Wound Care", "Introduces the basic types of wounds and the general principles of cleaning and dressing them to prevent infection."),
        ("Wound Cleaning and Dressing Techniques", "Examines proper techniques for irrigating, dressing, and monitoring wounds for signs of infection."),
        ("Core Theory: Wound Healing Physiology", "Covers the physiological stages of wound healing, from hemostasis through tissue remodeling."),
        ("Applied Wound Management", "Applies wound care principles to select appropriate dressings and interventions for different wound types."),
        ("Advanced Wound Care Principles", "Explores complex wound presentations, including contaminated wounds and signs requiring urgent medical referral."),
        ("Capstone: Wound Care Scenario Training", "Requires students to work through a series of wound care scenarios and justify their chosen interventions."),
        ("Graduate Seminar in Wound Care Science", "A graduate-level seminar reviewing evidence-based practices in prehospital wound management."),
    ],
    # 2. Burns classification and management
    [
        ("Introduction to Burn Injuries", "Introduces the classification of burns by depth, from superficial to full-thickness injuries."),
        ("Recognizing and Cooling Burn Injuries", "Examines the immediate first aid steps for cooling a burn and preventing further tissue damage."),
        ("Core Theory: Burn Depth and Severity Assessment", "Covers methods for estimating burn surface area and severity to guide treatment decisions."),
        ("Applied Burn Care", "Applies burn management principles to a series of case scenarios involving different burn causes and severities."),
        ("Advanced Burns Classification and Management", "Explores complications of major burns, including fluid loss and infection risk, and criteria for emergency referral."),
        ("Capstone: Burn Injury Case Study", "Requires an original case analysis proposing first aid management for a complex burn scenario."),
        ("Graduate Seminar in Burn Injury Management", "A graduate-level seminar examining current clinical guidelines for prehospital and early burn care."),
    ],
    # 3. Fracture and sprain management
    [
        ("Introduction to Fractures and Sprains", "Introduces the difference between fractures, sprains, and strains and basic signs of each."),
        ("Immobilization Techniques", "Examines splinting and immobilization techniques used to stabilize a suspected fracture or sprain."),
        ("Core Theory: Musculoskeletal Injury Assessment", "Covers systematic assessment approaches for suspected musculoskeletal injuries in the field."),
        ("Applied Splinting and Stabilization", "Applies immobilization techniques to a range of simulated fracture and sprain scenarios."),
        ("Advanced Fracture and Sprain Management", "Explores complications such as compound fractures and compartment syndrome and their urgent management."),
        ("Capstone: Musculoskeletal Injury Scenario Training", "Requires students to manage a series of simulated musculoskeletal injury scenarios."),
        ("Graduate Seminar in Musculoskeletal Trauma Care", "A graduate-level seminar reviewing evidence-based prehospital management of fractures and soft tissue injuries."),
    ],
    # 4. Shock recognition and management
    [
        ("Introduction to Shock", "Introduces shock as a state of inadequate blood flow to tissues and its common early warning signs."),
        ("Recognizing Types of Shock", "Examines the different types of shock, including hypovolemic and septic shock, and their distinguishing features."),
        ("Core Theory: Physiology of Shock", "Covers the physiological mechanisms by which the body compensates for and eventually decompensates during shock."),
        ("Applied Shock Management", "Applies first aid principles to positioning, monitoring, and managing a patient showing signs of shock."),
        ("Advanced Shock Recognition and Management", "Explores subtle and late-stage signs of shock and their implications for field triage decisions."),
        ("Capstone: Shock Scenario Training", "Requires students to recognize and manage shock in a series of realistic simulated scenarios."),
        ("Graduate Seminar in Shock Pathophysiology", "A graduate-level seminar examining the pathophysiology of shock and its relevance to prehospital care decisions."),
    ],
    # 5. Anaphylaxis and allergic reaction response
    [
        ("Introduction to Allergic Reactions", "Introduces the difference between mild allergic reactions and severe, life-threatening anaphylaxis."),
        ("Recognizing Anaphylaxis", "Examines the rapid-onset symptoms of anaphylaxis, including airway swelling and cardiovascular collapse."),
        ("Core Theory: Immunology of Allergic Response", "Covers the basic immunological mechanism behind allergic and anaphylactic reactions."),
        ("Applied Epinephrine Auto-Injector Use", "Applies knowledge of anaphylaxis to correctly identify when and how to assist with an epinephrine auto-injector."),
        ("Advanced Anaphylaxis Management", "Explores biphasic reactions and the importance of continued monitoring after initial anaphylaxis treatment."),
        ("Capstone: Allergic Emergency Scenario Training", "Requires students to manage a series of simulated allergic emergency scenarios of increasing severity."),
        ("Graduate Seminar in Anaphylaxis Science", "A graduate-level seminar reviewing current clinical guidelines for recognizing and managing anaphylaxis."),
    ],
    # 6. Cardiac emergency response science
    [
        ("Introduction to Cardiac Emergencies", "Introduces the warning signs of a heart attack and the basic first aid response."),
        ("Recognizing Cardiac Arrest", "Examines how to distinguish cardiac arrest from other cardiac emergencies and the urgency of an immediate response."),
        ("Core Theory: Cardiac Chain of Survival", "Covers the chain of survival concept linking early recognition, CPR, defibrillation, and advanced care."),
        ("Applied Cardiac Emergency Response", "Applies chain-of-survival principles to a series of simulated cardiac emergency scenarios."),
        ("Advanced Cardiac Emergency Science", "Explores the physiological basis of common cardiac arrhythmias relevant to first aid response decisions."),
        ("Capstone: Cardiac Emergency Scenario Training", "Requires students to lead a simulated response to a witnessed cardiac emergency from recognition through handoff."),
        ("Graduate Seminar in Cardiac Emergency Science", "A graduate-level seminar reviewing current resuscitation science and guidelines for cardiac emergencies."),
    ],
    # 7. Stroke recognition (FAST protocol) science
    [
        ("Introduction to Stroke Recognition", "Introduces the FAST protocol (Face, Arms, Speech, Time) as a tool for recognizing possible stroke."),
        ("Understanding Stroke Warning Signs", "Examines the range of stroke symptoms beyond FAST, including sudden vision loss and severe headache."),
        ("Core Theory: Types of Stroke", "Covers the distinction between ischemic and hemorrhagic stroke and why the difference matters for treatment urgency."),
        ("Applied Stroke Response", "Applies FAST assessment and time-critical response protocols to simulated stroke scenarios."),
        ("Advanced Stroke Recognition Science", "Explores the importance of time-to-treatment windows and their effect on stroke recovery outcomes."),
        ("Capstone: Stroke Scenario Training", "Requires students to correctly recognize and respond to a series of simulated stroke presentations."),
        ("Graduate Seminar in Stroke Recognition Science", "A graduate-level seminar reviewing the evidence base behind rapid stroke recognition tools used in prehospital care."),
    ],
    # 8. Poisoning and toxicology basics
    [
        ("Introduction to Poisoning First Aid", "Introduces common routes of poisoning exposure and the basic first aid steps to take."),
        ("Recognizing Poisoning Symptoms", "Examines symptoms associated with common poisoning scenarios, including ingestion and inhalation exposures."),
        ("Core Theory: Basic Toxicology Principles", "Covers foundational toxicology concepts, including dose-response relationships and routes of exposure."),
        ("Applied Poisoning Response", "Applies first aid protocols and poison control resources to a series of simulated poisoning scenarios."),
        ("Advanced Poisoning and Toxicology", "Explores specific toxic exposures, such as carbon monoxide poisoning, and their distinct first aid considerations."),
        ("Capstone: Toxicology Scenario Training", "Requires students to manage a series of simulated poisoning scenarios and identify when to contact poison control."),
        ("Graduate Seminar in Toxicology for First Responders", "A graduate-level seminar reviewing toxicological principles relevant to prehospital emergency response."),
    ],
    # 9. Heat and cold emergency physiology
    [
        ("Introduction to Heat and Cold Emergencies", "Introduces heat exhaustion, heat stroke, and hypothermia as environmental temperature emergencies."),
        ("Recognizing Heat and Cold Illness", "Examines the progressive signs and symptoms distinguishing heat exhaustion from heat stroke, and frostbite from hypothermia."),
        ("Core Theory: Thermoregulation Physiology", "Covers how the human body regulates core temperature and how that system fails during extreme heat or cold exposure."),
        ("Applied Heat and Cold Emergency Response", "Applies cooling and rewarming first aid techniques to a series of simulated environmental emergency scenarios."),
        ("Advanced Heat and Cold Emergency Physiology", "Explores the physiological cascade of severe hypothermia and heat stroke and associated field management priorities."),
        ("Capstone: Environmental Emergency Scenario Training", "Requires students to manage a series of simulated heat and cold emergency scenarios in realistic conditions."),
        ("Graduate Seminar in Environmental Emergency Physiology", "A graduate-level seminar reviewing current research on thermoregulatory emergencies and prehospital management."),
    ],
    # 10. Bleeding control techniques (tourniquet use)
    [
        ("Introduction to Bleeding Control", "Introduces direct pressure as the primary first aid technique for controlling external bleeding."),
        ("Bleeding Control with Dressings and Pressure", "Examines the layered use of dressings, pressure, and elevation to control moderate external bleeding."),
        ("Core Theory: Severe Bleeding and Tourniquet Use", "Covers the physiological rationale and correct application technique for a tourniquet in life-threatening bleeding."),
        ("Applied Bleeding Control Techniques", "Applies bleeding control techniques, including tourniquets and wound packing, to simulated severe bleeding scenarios."),
        ("Advanced Hemorrhage Control", "Explores hemostatic dressings and advanced hemorrhage control techniques used in high-risk bleeding scenarios."),
        ("Capstone: Severe Bleeding Scenario Training", "Requires students to correctly manage a series of simulated severe bleeding scenarios under time pressure."),
        ("Graduate Seminar in Hemorrhage Control Science", "A graduate-level seminar reviewing evidence supporting modern hemorrhage control techniques such as tourniquet use."),
    ],
    # 11. Triage & mass casualty / disaster response
    [
        ("Introduction to Triage", "Introduces the basic concept of triage as a method for prioritizing care when resources are limited."),
        ("Triage Categories and Sorting", "Examines common triage categorization systems used to sort patients by treatment urgency."),
        ("Core Theory: Mass Casualty Triage Systems", "Covers structured triage systems such as START used in mass casualty incidents."),
        ("Applied Mass Casualty Response", "Applies triage principles to a simulated multiple-casualty incident scenario."),
        ("Advanced Disaster Response Principles", "Explores the coordination challenges of disaster first aid response, including resource allocation and communication."),
        ("Capstone: Mass Casualty Scenario Training", "Requires students to lead the triage and initial response for a simulated mass casualty exercise."),
        ("Graduate Seminar in Disaster Medicine Response", "A graduate-level seminar examining triage systems and coordination frameworks used in large-scale disaster response."),
    ],
    # 12. Pediatric first aid considerations
    [
        ("Introduction to Pediatric First Aid", "Introduces key differences between administering first aid to children versus adults."),
        ("Recognizing Pediatric Emergencies", "Examines how common emergencies, such as choking and fever, present differently in infants and children."),
        ("Core Theory: Pediatric Physiological Differences", "Covers anatomical and physiological differences in children that affect first aid assessment and technique."),
        ("Applied Pediatric First Aid Response", "Applies age-appropriate first aid techniques to a series of simulated pediatric emergency scenarios."),
        ("Advanced Pediatric First Aid Considerations", "Explores pediatric-specific emergencies, including febrile seizures and infant CPR technique differences."),
        ("Capstone: Pediatric Emergency Scenario Training", "Requires students to manage a series of simulated pediatric first aid scenarios across different age groups."),
        ("Graduate Seminar in Pediatric Emergency Care", "A graduate-level seminar reviewing current guidelines for pediatric first aid and resuscitation."),
    ],
    # 13. First aid for chronic condition emergencies (diabetes, seizures)
    [
        ("Introduction to Chronic Condition Emergencies", "Introduces basic first aid responses for common chronic condition emergencies, including diabetic emergencies and seizures."),
        ("Recognizing Diabetic Emergencies", "Examines the signs distinguishing hypoglycemia from hyperglycemia and the appropriate first aid response to each."),
        ("Core Theory: Seizure First Aid Principles", "Covers the phases of a generalized seizure and the correct first aid priorities during and after the event."),
        ("Applied Chronic Condition Emergency Response", "Applies first aid protocols to a series of simulated diabetic emergency and seizure scenarios."),
        ("Advanced Chronic Condition Emergency Care", "Explores status epilepticus and severe hypoglycemia as emergencies requiring urgent escalation of care."),
        ("Capstone: Chronic Condition Scenario Training", "Requires students to manage a series of simulated chronic condition emergency scenarios."),
        ("Graduate Seminar in Chronic Disease Emergency Response", "A graduate-level seminar reviewing evidence-based first aid protocols for diabetic and seizure emergencies."),
    ],
    # 14. Mental health crisis first aid
    [
        ("Introduction to Mental Health First Aid", "Introduces the basic principles of recognizing and responding supportively to a person experiencing a mental health crisis."),
        ("Active Listening and De-escalation", "Examines communication techniques used to calmly support someone in psychological distress."),
        ("Core Theory: Mental Health Crisis Recognition", "Covers warning signs associated with panic attacks, acute stress reactions, and suicidal ideation."),
        ("Applied Mental Health First Aid Response", "Applies mental health first aid frameworks to a series of simulated crisis scenarios."),
        ("Advanced Mental Health Crisis Response", "Explores the first aid responder's role in supporting someone through a severe psychiatric emergency until professional help arrives."),
        ("Capstone: Mental Health Crisis Scenario Training", "Requires students to practice supportive first aid responses across a series of simulated mental health crisis scenarios."),
        ("Graduate Seminar in Mental Health First Aid", "A graduate-level seminar reviewing evidence-based mental health first aid frameworks and their community applications."),
    ],
    # 15. Wilderness survival and extended field first aid
    [
        ("Introduction to Wilderness Survival Skills", "Introduces basic survival priorities, including shelter, signaling, and staying warm, when help is not immediately available."),
        ("Extended Care Away from Definitive Help", "Examines how first aid priorities shift when evacuation or professional help will be delayed for hours or longer."),
        ("Core Theory: Prolonged Field Care Principles", "Covers the principles of prolonged field care used when a patient must be monitored for an extended period before evacuation."),
        ("Applied Extended Field First Aid", "Applies extended care and improvised equipment techniques to a series of simulated backcountry scenarios."),
        ("Advanced Wilderness Survival and First Aid", "Explores decision-making frameworks for evacuation urgency in remote or resource-limited settings."),
        ("Capstone: Backcountry Scenario Training", "Requires students to manage a simulated extended first aid scenario in a remote setting from initial assessment through evacuation planning."),
        ("Graduate Seminar in Prolonged Field Care", "A graduate-level seminar reviewing current research and protocols guiding prolonged field care in austere environments."),
    ],
    # 16. First aid kit design & capstone scenario training
    [
        ("Introduction to First Aid Kit Essentials", "Introduces the essential items that should be included in a basic personal or household first aid kit."),
        ("Stocking a First Aid Kit for Specific Activities", "Examines how first aid kit contents should be adapted for activities such as travel, hiking, or workplace settings."),
        ("Core Theory: Kit Design Principles", "Covers principles for organizing and maintaining a first aid kit for quick access during an emergency."),
        ("Applied First Aid Kit Assessment", "Applies kit design principles to evaluate and improve a first aid kit for a specific use case."),
        ("Advanced First Aid Kit Design", "Explores designing specialized kits for group activities, workplaces, or extended travel scenarios."),
        ("Capstone: Comprehensive First Aid Scenario Training", "A culminating capstone requiring students to respond to a rotation of realistic first aid scenarios using a kit they have designed."),
        ("Graduate Seminar in First Aid Program Design", "A graduate-level seminar on designing comprehensive first aid preparedness programs for organizations and communities."),
    ],
    # 17. First responder legal/ethical considerations (Good Samaritan)
    [
        ("Introduction to First Responder Ethics", "Introduces the basic ethical duty to help and the concept of consent before providing first aid."),
        ("Understanding Good Samaritan Protections", "Examines the general concept behind Good Samaritan laws that encourage bystanders to assist in emergencies."),
        ("Core Theory: Consent and Duty to Act", "Covers the distinctions between implied consent, expressed consent, and duty to act in first aid contexts."),
        ("Applied Legal and Ethical Decision-Making", "Applies legal and ethical principles to a series of first aid scenarios involving consent and refusal of care."),
        ("Advanced First Responder Legal Considerations", "Explores documentation practices and the limits of a first aid responder's scope of practice."),
        ("Capstone: Legal and Ethical Scenario Training", "Requires students to navigate a series of simulated scenarios involving consent, refusal, and Good Samaritan considerations."),
        ("Graduate Seminar in First Responder Law and Ethics", "A graduate-level seminar examining the legal and ethical frameworks shaping first responder conduct."),
    ],
    # 18. CPR and AED science in depth
    [
        ("Introduction to CPR and AED Use", "Introduces the basic steps of adult CPR and the safe operation of an automated external defibrillator."),
        ("CPR Technique and Compression Quality", "Examines proper compression depth, rate, and recoil as key determinants of effective CPR."),
        ("Core Theory: The Science Behind CPR", "Covers the physiological rationale for chest compressions and defibrillation in restoring circulation during cardiac arrest."),
        ("Applied CPR and AED Scenarios", "Applies CPR and AED protocols to a series of simulated cardiac arrest scenarios, including team-based response."),
        ("Advanced CPR and AED Science", "Explores special CPR considerations, including scenarios involving drowning, pregnancy, and pediatric patients."),
        ("Capstone: CPR and AED Scenario Training", "Requires students to lead a full simulated cardiac arrest response integrating CPR, AED use, and team coordination."),
        ("Graduate Seminar in Resuscitation Science", "A graduate-level seminar reviewing current international resuscitation guidelines and the evidence behind them."),
    ],
]

_PHYSICS_SPINES: list[list[tuple[str, str]]] = [
    # 1. Kinematics and dynamics in depth
    [
        ("Introduction to Kinematics", "Introduces displacement, velocity, and acceleration and how they are related through the kinematic equations for constant acceleration."),
        ("Newton's Laws of Motion", "Examines Newton's three laws of motion and their application to analyzing forces acting on simple systems."),
        ("Core Theory: Dynamics of Particle Systems", "Covers free-body diagrams and Newtonian dynamics applied to systems of interacting particles."),
        ("Applied Kinematics and Dynamics", "Applies kinematic and dynamic principles to solve multi-step problems involving projectile motion and connected bodies."),
        ("Advanced Kinematics and Dynamics", "Explores motion in non-inertial reference frames and the pseudo-forces that arise within them."),
        ("Capstone: Dynamics Problem-Solving Project", "Requires students to model and solve a complex real-world dynamics problem using Newtonian methods."),
        ("Graduate Seminar in Classical Dynamics", "A graduate-level seminar introducing Lagrangian and Hamiltonian reformulations of classical dynamics."),
    ],
    # 2. Work-energy theorem and conservation laws
    [
        ("Introduction to Work and Energy", "Introduces the concepts of work, kinetic energy, and potential energy and their relationship in simple mechanical systems."),
        ("The Work-Energy Theorem", "Examines how the work-energy theorem connects the net work done on an object to its change in kinetic energy."),
        ("Core Theory: Conservation of Energy", "Covers the principle of conservation of mechanical energy and conditions under which it holds."),
        ("Applied Energy Methods", "Applies energy conservation methods to solve problems involving springs, collisions, and inclined planes."),
        ("Advanced Conservation Laws", "Explores conservation of momentum and energy together in the analysis of elastic and inelastic collisions."),
        ("Capstone: Energy Conservation Case Study", "Requires an original analysis applying conservation laws to a multi-stage mechanical system."),
        ("Graduate Seminar in Conservation Principles", "A graduate-level seminar connecting conservation laws to symmetries through Noether's theorem."),
    ],
    # 3. Rotational motion and angular momentum
    [
        ("Introduction to Rotational Motion", "Introduces angular displacement, angular velocity, and angular acceleration as rotational analogues of linear motion quantities."),
        ("Torque and Rotational Dynamics", "Examines how torque causes changes in rotational motion, analogous to how force causes changes in linear motion."),
        ("Core Theory: Moment of Inertia", "Covers how mass distribution determines an object's moment of inertia and its effect on rotational dynamics."),
        ("Applied Rotational Mechanics", "Applies rotational dynamics principles to solve problems involving rolling objects and rotating systems."),
        ("Advanced Angular Momentum", "Explores conservation of angular momentum and its application to phenomena such as a spinning skater's rotation rate."),
        ("Capstone: Rotational Systems Project", "Requires students to analyze a real-world rotational system using torque and angular momentum principles."),
        ("Graduate Seminar in Rigid Body Dynamics", "A graduate-level seminar examining the dynamics of rigid bodies, including precession and gyroscopic motion."),
    ],
    # 4. Oscillations and waves
    [
        ("Introduction to Oscillations", "Introduces simple harmonic motion using the example of a mass on a spring and a simple pendulum."),
        ("Wave Properties and Behavior", "Examines wavelength, frequency, amplitude, and wave speed and how waves transfer energy without transferring matter."),
        ("Core Theory: Simple Harmonic Motion", "Covers the mathematical description of simple harmonic motion and the conditions that produce it."),
        ("Applied Wave Analysis", "Applies wave equations to analyze interference, superposition, and standing wave patterns."),
        ("Advanced Oscillations and Waves", "Explores damped and driven oscillations, including the phenomenon of resonance."),
        ("Capstone: Wave Phenomena Investigation", "Requires an original investigation of a wave phenomenon such as standing waves on a string or in an air column."),
        ("Graduate Seminar in Wave Mechanics", "A graduate-level seminar examining the mathematical treatment of coupled oscillators and wave propagation."),
    ],
    # 5. Thermodynamics laws in depth
    [
        ("Introduction to Thermodynamics", "Introduces temperature, heat, and internal energy and the zeroth law of thermodynamics."),
        ("The First Law of Thermodynamics", "Examines the first law of thermodynamics as a statement of energy conservation applied to thermal systems."),
        ("Core Theory: The Second Law of Thermodynamics", "Covers the second law of thermodynamics, entropy, and the direction of natural thermodynamic processes."),
        ("Applied Thermodynamic Cycles", "Applies thermodynamic principles to analyze idealized engine cycles such as the Carnot cycle."),
        ("Advanced Thermodynamics", "Explores thermodynamic potentials, including enthalpy and free energy, and their use in predicting spontaneity."),
        ("Capstone: Thermodynamic System Analysis", "Requires an original analysis of the efficiency and entropy changes in a chosen thermodynamic system."),
        ("Graduate Seminar in Thermodynamics", "A graduate-level seminar examining the formal structure of classical thermodynamics and its connection to statistical mechanics."),
    ],
    # 6. Fluid mechanics
    [
        ("Introduction to Fluid Mechanics", "Introduces pressure, density, and buoyancy, including Archimedes' principle."),
        ("Fluids at Rest and in Motion", "Examines hydrostatic pressure and the basic distinction between laminar and turbulent flow."),
        ("Core Theory: Bernoulli's Principle", "Covers Bernoulli's equation and its application to fluid flow in pipes and around objects."),
        ("Applied Fluid Dynamics", "Applies fluid mechanics principles to problems involving flow rate, pressure differences, and continuity."),
        ("Advanced Fluid Mechanics", "Explores viscosity, the Reynolds number, and conditions that lead to turbulent flow."),
        ("Capstone: Fluid Systems Investigation", "Requires an original investigation of a fluid system, such as flow through a variable-diameter pipe."),
        ("Graduate Seminar in Fluid Dynamics", "A graduate-level seminar introducing the Navier-Stokes equations and their role in describing real fluid behavior."),
    ],
    # 7. Electromagnetism in depth
    [
        ("Introduction to Electric Fields and Forces", "Introduces electric charge, Coulomb's law, and the concept of an electric field."),
        ("Magnetic Fields and Forces", "Examines how moving charges create magnetic fields and experience forces within them."),
        ("Core Theory: Electromagnetic Induction", "Covers Faraday's law of electromagnetic induction and Lenz's law describing induced current direction."),
        ("Applied Circuit Analysis", "Applies electromagnetic principles to analyze circuits containing resistors, capacitors, and inductors."),
        ("Advanced Electromagnetism", "Explores the conceptual unification of electricity and magnetism achieved through Maxwell's equations."),
        ("Capstone: Electromagnetic Systems Project", "Requires an original analysis or design project involving an electromagnetic system such as a simple motor or generator."),
        ("Graduate Seminar in Electromagnetic Theory", "A graduate-level seminar examining Maxwell's equations and their prediction of electromagnetic waves."),
    ],
    # 8. Optics and wave phenomena
    [
        ("Introduction to Optics", "Introduces reflection and refraction of light and the basic law describing each."),
        ("Lenses and Image Formation", "Examines how converging and diverging lenses form images, using ray diagrams and the thin lens equation."),
        ("Core Theory: Wave Optics", "Covers diffraction and interference as evidence for the wave nature of light."),
        ("Applied Optical Systems", "Applies optical principles to analyze systems such as simple telescopes, microscopes, and cameras."),
        ("Advanced Optics", "Explores polarization of light and its applications in technology and everyday devices."),
        ("Capstone: Optical Systems Investigation", "Requires an original investigation or design project involving an optical instrument or phenomenon."),
        ("Graduate Seminar in Optical Physics", "A graduate-level seminar examining coherence, interferometry, and modern applications of wave optics."),
    ],
    # 9. Special relativity fundamentals
    [
        ("Introduction to Special Relativity", "Introduces Einstein's two postulates of special relativity and the constancy of the speed of light."),
        ("Time Dilation and Length Contraction", "Examines how time dilation and length contraction arise as consequences of special relativity's postulates."),
        ("Core Theory: Relativistic Kinematics", "Covers the Lorentz transformations and how they relate measurements between different inertial reference frames."),
        ("Applied Relativistic Problem Solving", "Applies relativistic kinematics to solve problems involving high-speed particles and simultaneity."),
        ("Advanced Special Relativity", "Explores mass-energy equivalence and relativistic momentum and energy relationships."),
        ("Capstone: Relativity Case Study", "Requires an original written analysis explaining a real experimental confirmation of special relativity, such as muon decay observations."),
        ("Graduate Seminar in Special Relativity", "A graduate-level seminar examining the four-vector formalism used in modern treatments of special relativity."),
    ],
    # 10. Quantum mechanics fundamentals
    [
        ("Introduction to Quantum Physics", "Introduces the photoelectric effect and the concept of quantized energy that motivated the development of quantum theory."),
        ("Wave-Particle Duality", "Examines evidence for wave-particle duality, including the double-slit experiment with electrons."),
        ("Core Theory: The Schrodinger Equation", "Covers the role of the Schrodinger equation in describing the quantum state of a system."),
        ("Applied Quantum Problem Solving", "Applies quantum mechanical models, such as the particle in a box, to calculate allowed energy levels."),
        ("Advanced Quantum Mechanics", "Explores the Heisenberg uncertainty principle and its implications for simultaneously measuring position and momentum."),
        ("Capstone: Quantum Phenomena Case Study", "Requires an original written analysis of a quantum phenomenon such as quantum tunneling."),
        ("Graduate Seminar in Quantum Theory", "A graduate-level seminar examining the mathematical formalism of quantum mechanics, including operators and eigenstates."),
    ],
    # 11. Nuclear physics basics
    [
        ("Introduction to Nuclear Physics", "Introduces the structure of the atomic nucleus, including protons, neutrons, and isotopes."),
        ("Radioactive Decay", "Examines the three common types of radioactive decay: alpha, beta, and gamma, and the concept of half-life."),
        ("Core Theory: Nuclear Binding Energy", "Covers nuclear binding energy and its relationship to nuclear stability across the periodic table."),
        ("Applied Nuclear Physics", "Applies decay equations and half-life calculations to problems involving radioactive dating and sample activity."),
        ("Advanced Nuclear Physics", "Explores nuclear fission and fusion reactions and the energy released in each process."),
        ("Capstone: Nuclear Physics Case Study", "Requires an original written analysis of a real application of nuclear physics, such as a nuclear power reactor or medical imaging technique."),
        ("Graduate Seminar in Nuclear Physics", "A graduate-level seminar examining nuclear models, including the shell model, used to explain nuclear structure."),
    ],
    # 12. Particle physics overview
    [
        ("Introduction to Particle Physics", "Introduces the basic classification of elementary particles into quarks, leptons, and force-carrying bosons."),
        ("The Standard Model Overview", "Examines the Standard Model of particle physics as the current framework describing known elementary particles and their interactions."),
        ("Core Theory: Fundamental Forces", "Covers the four fundamental forces and the particles thought to mediate each of them."),
        ("Applied Particle Physics Concepts", "Applies conservation laws, such as charge and baryon number conservation, to evaluate whether hypothetical particle interactions are allowed."),
        ("Advanced Particle Physics", "Explores how particle accelerators and detectors are used to discover and study subatomic particles."),
        ("Capstone: Particle Physics Case Study", "Requires an original written analysis of a landmark particle physics discovery, such as the Higgs boson."),
        ("Graduate Seminar in Particle Physics", "A graduate-level seminar examining the theoretical structure of the Standard Model and open questions beyond it."),
    ],
    # 13. Astrophysics fundamentals
    [
        ("Introduction to Astrophysics", "Introduces the basic life cycle of stars, from formation in nebulae to their eventual fate."),
        ("Stellar Classification", "Examines how stars are classified by temperature and luminosity using the Hertzsprung-Russell diagram."),
        ("Core Theory: Stellar Structure and Evolution", "Covers the physical processes, including nuclear fusion, that power stars throughout their evolutionary stages."),
        ("Applied Astrophysical Analysis", "Applies concepts such as parallax and the inverse-square law to estimate stellar distance and luminosity."),
        ("Advanced Astrophysics", "Explores the physics of compact objects, including white dwarfs, neutron stars, and black holes."),
        ("Capstone: Astrophysics Case Study", "Requires an original written analysis of a specific astronomical object or phenomenon using astrophysical principles."),
        ("Graduate Seminar in Astrophysics", "A graduate-level seminar examining current research topics in stellar and galactic astrophysics."),
    ],
    # 14. Condensed matter physics overview
    [
        ("Introduction to Condensed Matter Physics", "Introduces the basic distinction between crystalline and amorphous solids and how atomic arrangement affects material properties."),
        ("Electrical Properties of Materials", "Examines why materials are classified as conductors, insulators, or semiconductors based on their electronic structure."),
        ("Core Theory: Band Theory of Solids", "Covers band theory as the framework explaining the electrical and optical properties of crystalline solids."),
        ("Applied Semiconductor Physics", "Applies band theory concepts to explain the operation of basic semiconductor devices such as diodes."),
        ("Advanced Condensed Matter Physics", "Explores phenomena such as superconductivity and the conditions under which certain materials exhibit it."),
        ("Capstone: Materials Physics Case Study", "Requires an original written analysis of a specific material's physical properties and their underlying condensed matter physics explanation."),
        ("Graduate Seminar in Condensed Matter Physics", "A graduate-level seminar examining current research on electronic and structural properties of solid-state materials."),
    ],
    # 15. Statistical mechanics fundamentals
    [
        ("Introduction to Statistical Mechanics", "Introduces how statistical mechanics connects the microscopic behavior of particles to macroscopic thermodynamic properties."),
        ("Kinetic Theory of Gases", "Examines the kinetic theory of gases and how it explains pressure and temperature in terms of molecular motion."),
        ("Core Theory: Statistical Distributions", "Covers the Maxwell-Boltzmann distribution describing the range of molecular speeds in a gas."),
        ("Applied Statistical Mechanics", "Applies statistical mechanics concepts to calculate quantities such as average kinetic energy and pressure from molecular models."),
        ("Advanced Statistical Mechanics", "Explores quantum statistics, including Bose-Einstein and Fermi-Dirac distributions, and where each applies."),
        ("Capstone: Statistical Mechanics Case Study", "Requires an original written analysis connecting a macroscopic thermodynamic property to its statistical mechanical origin."),
        ("Graduate Seminar in Statistical Mechanics", "A graduate-level seminar examining the ensemble formalism used in modern statistical mechanics."),
    ],
    # 16. Computational physics methods
    [
        ("Introduction to Computational Physics", "Introduces how numerical methods and simple simulations are used to model physical systems that lack simple analytical solutions."),
        ("Numerical Methods for Motion", "Examines basic numerical integration techniques, such as the Euler method, used to simulate motion under changing forces."),
        ("Core Theory: Simulation Algorithms", "Covers common algorithms used in physics simulations, including improvements on basic numerical integration methods."),
        ("Applied Computational Modeling", "Applies computational methods to model and analyze a physical system, such as a pendulum with air resistance."),
        ("Advanced Computational Physics", "Explores Monte Carlo methods and their use in simulating systems with many interacting particles."),
        ("Capstone: Computational Physics Project", "Requires students to build and validate a computational model of a chosen physical system."),
        ("Graduate Seminar in Computational Physics", "A graduate-level seminar reviewing computational techniques used in current physics research."),
    ],
    # 17. Experimental physics techniques & capstone research project
    [
        ("Introduction to Experimental Physics", "Introduces basic laboratory skills, including measurement, uncertainty, and significant figures."),
        ("Data Collection and Error Analysis", "Examines systematic and random error and how they are accounted for when reporting experimental measurements."),
        ("Core Theory: Experimental Design", "Covers principles of controlled experimental design, including identifying variables and controlling confounds."),
        ("Applied Laboratory Techniques", "Applies experimental design principles to conduct and analyze the results of a hands-on physics experiment."),
        ("Advanced Experimental Physics", "Explores instrumentation and calibration techniques used to improve measurement precision in physics experiments."),
        ("Capstone: Physics Experiment Design Project", "Requires students to design, conduct, and report on an original physics experiment addressing a specific research question."),
        ("Capstone Physics Research Project", "A graduate-level capstone requiring an original independent physics research project, from literature review through data analysis and reporting."),
    ],
    # 18. Physics of everyday phenomena & history/philosophy of physics
    [
        ("Introduction to the Physics of Everyday Phenomena", "Introduces how physics principles explain common experiences, such as why a curveball curves or why ice floats."),
        ("Physics in the Kitchen and Home", "Examines everyday examples of thermodynamics and mechanics found in cooking and household activities."),
        ("Core Theory: Physics of Sports and Motion", "Covers how kinematics and dynamics explain the motion of everyday objects and athletic movements."),
        ("Applied Everyday Physics Analysis", "Applies physics principles to explain and analyze a chosen everyday phenomenon in detail."),
        ("Advanced Studies: History of Physics", "Explores the historical development of major physics theories, from Aristotelian to Newtonian to modern physics."),
        ("Capstone: Philosophy of Physics Case Study", "Requires an original written analysis of a philosophical question raised by physics, such as determinism or the interpretation of quantum measurement."),
        ("Graduate Seminar in History and Philosophy of Physics", "A graduate-level seminar examining how physics theories historically developed and the philosophical debates they have raised."),
    ],
]


def _build(spines: list[list[tuple[str, str]]]) -> dict[str, list[tuple[str, str]]]:
    """Flattens 18 spines of 7 (title, summary) tuples into a per-level dict."""
    return {
        level: [spine[i] for spine in spines]
        for i, level in enumerate(_LEVELS)
    }


MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "Social Studies": _build(_SOCIAL_STUDIES_SPINES),
    "Physical Education & Self-Defense": _build(_PE_SELF_DEFENSE_SPINES),
    "First Aid": _build(_FIRST_AID_SPINES),
    "Physics": _build(_PHYSICS_SPINES),
}
