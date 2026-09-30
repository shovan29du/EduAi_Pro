#!/usr/bin/env python3
"""Expand Health Education from Grade 1 through Master's 1, adding real,
age-appropriate topics at each school grade (currently just 1 lesson per
grade) and additional academic public-health topics at each college level
(currently 10 lessons per level), for a combined ~99 new lessons across
the whole span -- within the requested 50-100 net-new lessons.

New lessons are written with a short seed reading_material; run
expand_lesson_reading_material.py afterwards (safe to re-run, it only
touches lessons under 700 words) to bring them to the same 700-2000 word
standard as every other lesson in the curriculum.

Re-run after editing:
    python3 backend/scripts/expand_health_education.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"
SUBJECT = "Health Education"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_advanced_curriculum import LEVEL_IDS, _lesson_for  # noqa: E402

# (title, unit, learning_objectives, reading_material_seed)
GRADE_TOPICS: dict[int, list[tuple[str, str, list[str], str]]] = {
    1: [
        ("Washing Hands Properly", "Personal Health", ["Demonstrate the correct handwashing steps", "Explain when to wash hands"], "Washing your hands the right way stops germs from spreading. Wet your hands, use soap, scrub for 20 seconds (about as long as singing 'Happy Birthday' twice), rinse, and dry."),
        ("Brushing Teeth", "Personal Health", ["Explain why we brush our teeth", "Describe a good brushing routine"], "Brushing your teeth twice a day, morning and night, keeps your teeth strong and your breath fresh. Use a pea-sized amount of toothpaste and brush all your teeth gently."),
        ("Eating Fruits and Vegetables", "Nutrition", ["Name different fruits and vegetables", "Explain why they are good for us"], "Fruits and vegetables give our bodies vitamins that help us grow, see well, and fight off sickness. Eating a rainbow of colours means getting many different vitamins."),
        ("Getting Enough Sleep", "Personal Health", ["Explain why sleep is important", "State how much sleep children need"], "Sleep helps your body and brain rest and grow. Young children need about 10 to 13 hours of sleep every night to feel their best."),
        ("Staying Safe Outdoors", "Safety", ["List outdoor safety rules", "Explain why adult supervision matters"], "Playing outside is fun and healthy, but it's important to stay safe: hold an adult's hand near roads, wear a helmet when biking, and tell a grown-up where you are going."),
    ],
    2: [
        ("Germs and How They Spread", "Personal Health", ["Explain what germs are", "Describe how germs spread from person to person"], "Germs are tiny living things too small to see that can make us sick. They spread through coughs, sneezes, and touching dirty surfaces, which is why washing hands and covering coughs matters."),
        ("Food Groups and My Plate", "Nutrition", ["Name the main food groups", "Build a balanced meal"], "Foods are grouped into fruits, vegetables, grains, protein, and dairy. A healthy plate has a good mix from each group, with more fruits and vegetables than anything else."),
        ("Why We Exercise", "Fitness", ["List benefits of physical activity", "Name ways to be active"], "Moving your body every day -- running, jumping, dancing, or playing sports -- makes your heart and muscles stronger and helps you feel happier."),
        ("Taking Care of Your Teeth", "Personal Health", ["Explain the role of a dentist", "Describe good dental habits"], "Along with brushing and flossing, visiting the dentist regularly helps catch problems early and keeps your smile healthy."),
        ("Medicine Safety Basics", "Safety", ["Explain why only adults should give medicine", "Describe safe medicine storage"], "Medicine can help you feel better when you're sick, but too much can be dangerous. Only a trusted adult should give you medicine, and it should always be stored out of children's reach."),
    ],
    3: [
        ("Human Body Systems Overview", "Body Systems", ["Name major body systems", "Describe one job of each system"], "Your body is made of systems that work together: the skeletal system holds you up, the muscular system lets you move, the digestive system breaks down food, and the circulatory system carries blood around your body."),
        ("Reading Nutrition Labels", "Nutrition", ["Locate key information on a nutrition label", "Compare two food labels"], "Nutrition labels tell you what's inside packaged food -- how much sugar, fat, and vitamins it has -- so you can make informed choices about what to eat."),
        ("Understanding Feelings and Emotions", "Mental Health", ["Name common emotions", "Describe healthy ways to express feelings"], "Everyone feels happy, sad, angry, or worried sometimes. Naming your feelings and talking about them with someone you trust is a healthy way to manage them."),
        ("Preventing Common Injuries", "Safety", ["List common childhood injuries", "Describe prevention strategies"], "Simple habits like wearing seatbelts, using playground equipment properly, and not running with sharp objects help prevent many common injuries."),
        ("Personal Hygiene Routines", "Personal Health", ["Build a daily hygiene checklist", "Explain why hygiene matters for health"], "A daily hygiene routine -- bathing, washing hands, brushing teeth, and wearing clean clothes -- helps prevent illness and keeps you feeling good."),
    ],
    4: [
        ("Introduction to Puberty", "Growth & Development", ["Describe body changes during puberty", "Explain that puberty timing varies"], "Puberty is the stage when a child's body starts changing into an adult body. It happens at different times for different people, and all of it is a normal part of growing up."),
        ("Screen Time and Health", "Personal Health", ["Explain effects of too much screen time", "Set a personal screen time goal"], "Spending too much time on screens can affect sleep, eyesight, and physical activity. Balancing screen time with outdoor play, reading, and family time supports overall health."),
        ("Basic First Aid Steps", "Safety", ["Describe first aid for a minor cut", "Explain when to get adult help"], "For a minor scrape, first aid means washing the wound, applying a clean bandage, and telling an adult. For anything serious, getting an adult's help right away is the priority."),
        ("Managing Stress in Healthy Ways", "Mental Health", ["Name signs of stress", "List healthy coping strategies"], "Feeling stressed sometimes is normal. Deep breathing, talking to someone you trust, exercise, and hobbies are healthy ways to manage stress."),
        ("Sun Safety and Skin Health", "Personal Health", ["Explain sun damage risks", "List sun protection methods"], "Too much sun exposure can damage skin. Wearing sunscreen, hats, and sunglasses, and seeking shade during peak sun hours, protects your skin."),
    ],
    5: [
        ("Human Body Systems in Depth", "Body Systems", ["Explain how two body systems work together", "Describe the nervous system's role"], "Body systems work as a team: the nervous system sends signals from your brain to control muscles, while the respiratory and circulatory systems work together to deliver oxygen throughout your body."),
        ("Building Healthy Relationships", "Social Health", ["Describe qualities of a healthy friendship", "Identify signs of an unhealthy relationship"], "Healthy friendships are built on respect, honesty, and kindness. Recognizing when a relationship feels unfair or unsafe is an important life skill."),
        ("Understanding Tobacco and Alcohol Risks", "Substance Awareness", ["Explain health risks of tobacco and alcohol", "Describe refusal skills"], "Tobacco and alcohol can seriously harm a developing body. Learning simple ways to say no to peer pressure helps protect your health."),
        ("The Science of Sleep", "Personal Health", ["Explain what happens during sleep", "Describe good sleep hygiene"], "During sleep, your brain processes memories and your body repairs itself. Good sleep hygiene includes a consistent bedtime and limiting screens before bed."),
        ("Body Image and Self-Esteem", "Mental Health", ["Define body image and self-esteem", "Discuss healthy self-talk"], "Body image is how you feel about your body, and self-esteem is your overall sense of self-worth. Practicing kind self-talk and focusing on what your body can do, not just how it looks, supports healthy self-esteem."),
    ],
    6: [
        ("Adolescent Growth and Development", "Growth & Development", ["Describe physical and emotional changes in adolescence", "Explain individual variation in development"], "Adolescence brings rapid physical growth alongside emotional and social changes. Everyone develops at their own pace, and that variation is entirely normal."),
        ("Nutrition and Fitness Planning", "Nutrition & Fitness", ["Design a simple balanced weekly meal plan", "Set a personal fitness goal"], "Combining balanced nutrition with regular physical activity supports growth, energy, and long-term health. Planning meals and workouts ahead of time makes healthy choices easier."),
        ("Recognizing and Managing Stress", "Mental Health", ["Identify personal stress triggers", "Practice a stress-management technique"], "Learning to recognize your own stress triggers -- schoolwork, social pressure, family changes -- is the first step toward managing stress effectively with techniques like deep breathing or journaling."),
        ("Safety and Risk-Taking Behavior", "Safety", ["Distinguish healthy risk-taking from dangerous risk-taking", "Describe peer pressure resistance strategies"], "As adolescents seek more independence, understanding the difference between exciting, healthy challenges and genuinely dangerous risks is an important safety skill."),
        ("Basic First Aid and CPR Awareness", "Safety", ["Describe the basic steps of CPR awareness", "Explain when to call emergency services"], "Knowing the basic outline of CPR and when to call for emergency help can make a critical difference in an emergency, even before a certified course."),
    ],
    7: [
        ("Reproductive Health Basics", "Growth & Development", ["Describe the basic biology of human reproduction", "Explain the importance of accurate health information"], "Understanding the basic biology of human reproduction, presented factually and age-appropriately, is a foundational part of health literacy."),
        ("Substance Abuse Prevention", "Substance Awareness", ["Describe how addiction affects the brain", "List prevention and refusal strategies"], "Understanding how substances affect the developing brain, and practicing refusal skills, are key parts of substance abuse prevention education."),
        ("Healthy Coping Strategies", "Mental Health", ["List several healthy coping strategies", "Distinguish healthy from unhealthy coping"], "Healthy coping strategies -- exercise, talking to someone, creative outlets -- help manage difficult emotions without turning to harmful behaviors."),
        ("Chronic Disease Awareness", "Personal Health", ["Name common chronic diseases", "Describe lifestyle factors that reduce risk"], "Chronic diseases like diabetes and heart disease often develop over many years; understanding risk factors like diet, activity, and smoking helps with long-term prevention."),
        ("Communication in Relationships", "Social Health", ["Practice assertive communication", "Identify healthy conflict-resolution skills"], "Clear, respectful communication -- expressing your feelings honestly while listening to others -- is a foundational skill for healthy relationships of every kind."),
    ],
    8: [
        ("Consent and Personal Boundaries", "Social Health", ["Define consent and personal boundaries", "Practice communicating boundaries respectfully"], "Understanding consent and personal boundaries -- and respecting them in others -- is an essential life skill for healthy relationships of every kind."),
        ("Nutrition Science for Teens", "Nutrition", ["Explain teen-specific nutritional needs", "Evaluate a sample daily diet"], "Adolescence brings increased nutritional needs for growth, including more calcium, iron, and protein than in earlier childhood."),
        ("Designing a Fitness Program", "Fitness", ["Design a balanced weekly fitness routine", "Explain the FITT principle (frequency, intensity, time, type)"], "A well-designed fitness program balances cardiovascular exercise, strength training, and flexibility work, following the FITT principle to build a sustainable routine."),
        ("Emergency Response Basics", "Safety", ["Describe steps to take in a common emergency", "Explain how to safely call for help"], "Knowing basic emergency response steps -- staying calm, assessing the situation, and calling for help -- prepares you to act effectively when it matters most."),
        ("Evaluating Health Claims in Media", "Health Literacy", ["Identify red flags in health marketing claims", "Practice fact-checking a health claim"], "Not all health information online or in advertising is accurate. Learning to check sources and spot exaggerated claims protects you from misinformation."),
    ],
    9: [
        ("Comprehensive Health Self-Assessment", "Personal Health", ["Complete a personal health self-assessment", "Set personal health goals"], "A comprehensive self-assessment across nutrition, fitness, sleep, and mental health helps identify areas for personal improvement and goal-setting."),
        ("Disease Prevention and Immunization", "Public Health", ["Explain how vaccines work", "Describe the concept of herd immunity"], "Vaccines train the immune system to recognize and fight specific diseases, and high vaccination rates in a community create herd immunity that protects vulnerable individuals."),
        ("Understanding Mental Health Disorders", "Mental Health", ["Name common mental health disorders", "Describe when and how to seek help"], "Learning about common mental health conditions like anxiety and depression, and reducing the stigma around them, encourages people to seek help when they need it."),
        ("The Science of Addiction", "Substance Awareness", ["Explain how addiction affects brain chemistry", "Describe factors that increase addiction risk"], "Addiction involves changes in brain chemistry that make quitting difficult without support; understanding this helps replace judgment with informed compassion and effective prevention."),
        ("Consumer Health Literacy", "Health Literacy", ["Evaluate health product marketing critically", "Understand basic health insurance concepts"], "Consumer health literacy includes critically evaluating health products and understanding basic concepts like health insurance and how to access reliable care."),
    ],
    10: [
        ("Public Health Basics", "Public Health", ["Define public health versus individual health care", "Describe a real public health success story"], "Public health focuses on protecting and improving the health of entire populations through prevention, policy, and education, distinct from treating individual patients."),
        ("Family Planning Overview", "Growth & Development", ["Describe the basic concepts of family planning", "Explain the importance of informed decision-making"], "Family planning education covers the basic biological and social concepts behind reproductive decision-making, presented factually to support informed choices later in life."),
        ("Mental Health First Aid", "Mental Health", ["Describe steps for supporting someone in a mental health crisis", "List local and national mental health resources"], "Mental health first aid teaches how to recognize warning signs in others and connect them with appropriate support and resources."),
        ("Exploring Health Careers", "Careers", ["List a range of careers in the health field", "Research the education path for one health career"], "The health field includes careers from nursing and medicine to public health, nutrition, and health administration, each requiring different educational paths."),
        ("Global Health Issues Overview", "Public Health", ["Name major global health challenges", "Describe an international health organization's role"], "Global health challenges like infectious disease outbreaks, malnutrition, and access to care are addressed by international organizations working across borders."),
    ],
}

# (title, summary) -- college-level additions, avoiding titles already present.
COLLEGE_TOPICS: dict[str, list[tuple[str, str]]] = {
    "C1": [
        ("Personal Hygiene and Disease Prevention", "Examines the role of personal hygiene practices in preventing the spread of common infectious diseases."),
        ("First Aid Certification Pathways", "Surveys standard first aid and CPR certification programs and their role in community emergency preparedness."),
        ("Health Literacy Fundamentals", "Introduces health literacy as a distinct competency and its documented link to health outcomes."),
        ("Vaccination Science", "Covers the immunological basis of vaccination and the population-level concept of herd immunity."),
        ("Consumer Health Products Safety", "Examines how to evaluate the safety and marketing claims of consumer health and wellness products."),
        ("Body Image and Self-Esteem in Health Education", "Studies the relationship between body image, self-esteem, and health behaviors."),
        ("Health Across the Lifespan: An Introduction", "Introduces how health needs and priorities shift across infancy, childhood, adulthood, and older age."),
    ],
    "C2": [
        ("Human Sexuality Education Frameworks", "Surveys comprehensive sexuality education frameworks used in health curricula internationally."),
        ("Family Life Education", "Examines curricular approaches to family life education, including relationships, communication, and family health."),
        ("Tobacco and Vaping Prevention", "Studies evidence-based prevention programs targeting tobacco and vaping use among youth."),
        ("Nutrition Labeling and Policy", "Examines the regulatory frameworks behind nutrition labeling and their effect on consumer choices."),
        ("Health Insurance Basics", "Introduces core concepts in health insurance systems and how they affect access to care."),
        ("Telehealth Fundamentals", "Surveys the growth of telehealth services and their implications for access to health education and care."),
        ("School Health Services", "Examines the role of school-based health services in supporting student wellbeing."),
    ],
    "UG1": [
        ("Global Burden of Disease", "Introduces the Global Burden of Disease framework for measuring health loss across populations."),
        ("Health Economics Fundamentals", "Introduces core concepts in health economics, including cost-effectiveness analysis in health decision-making."),
        ("Health Promotion Theory: PRECEDE-PROCEED", "Studies the PRECEDE-PROCEED model as a framework for planning and evaluating health promotion programs."),
        ("One Health Concept", "Introduces the One Health framework connecting human, animal, and environmental health."),
        ("Health in Humanitarian Emergencies", "Surveys public health response approaches during humanitarian crises and natural disasters."),
        ("Reproductive Health Policy", "Examines policy frameworks shaping access to reproductive health services and education."),
        ("Grant Writing for Health Programs", "Introduces practical grant-writing skills for public health and health education program funding."),
    ],
    "UG2": [
        ("Vector-Borne Disease Control", "Studies public health strategies for controlling diseases transmitted by insects and other vectors."),
        ("Water, Sanitation, and Hygiene (WASH)", "Examines WASH interventions and their central role in preventing infectious disease globally."),
        ("Mental Health Stigma Reduction", "Studies evidence-based approaches to reducing stigma around mental health conditions."),
        ("Adolescent Reproductive Health Programs", "Surveys program models for delivering reproductive health education to adolescents."),
        ("Nutrition-Sensitive Interventions", "Examines interventions that address the underlying causes of malnutrition beyond food access alone."),
        ("Health Surveillance Systems", "Introduces how public health surveillance systems track disease trends and inform response."),
        ("Community Health Worker Models", "Studies the community health worker model and its effectiveness in expanding health access."),
    ],
    "UG3": [
        ("Health Systems Strengthening", "Examines frameworks for strengthening the building blocks of national health systems."),
        ("Universal Health Coverage", "Studies the concept and policy pathways toward universal health coverage."),
        ("Non-Communicable Disease Policy", "Examines policy responses to the rising global burden of non-communicable diseases."),
        ("Health in All Policies Approach", "Studies the 'Health in All Policies' framework for embedding health considerations across sectors."),
        ("Digital Epidemiology", "Introduces the use of digital data sources for real-time disease surveillance and epidemiological research."),
        ("Behavioral Economics in Health", "Examines how behavioral economics informs the design of effective health interventions."),
        ("Health Communication Campaigns", "Studies the design and evaluation of large-scale public health communication campaigns."),
    ],
    "UG4": [
        ("Pandemic Preparedness Planning", "Examines the components of national and institutional pandemic preparedness plans."),
        ("Health Equity Metrics", "Surveys quantitative approaches to measuring and tracking health equity across populations."),
        ("Climate Change and Health", "Studies the documented health impacts of climate change and adaptation strategies."),
        ("Refugee and Migrant Health", "Examines the distinct health needs and access barriers faced by refugee and migrant populations."),
        ("Health Technology Assessment", "Introduces the methods used to evaluate the value and cost-effectiveness of new health technologies."),
        ("Precision Public Health", "Surveys the emerging field applying precision-medicine concepts to population-level health interventions."),
        ("Public Health Leadership Capstone", "A capstone module synthesizing leadership principles for public health practice."),
    ],
    "M1": [
        ("Advanced Health Policy Analysis Methods", "Graduate-level methods for analyzing the development and impact of health policy."),
        ("Global Health Diplomacy", "Examines the intersection of health policy and international diplomacy."),
        ("Health Systems Financing Reform", "Studies comparative approaches to reforming health system financing structures."),
        ("Implementation Science Frameworks II", "An advanced study of implementation science frameworks for translating research into health practice."),
        ("Causal Inference in Health Research", "Introduces graduate-level causal inference methods applied to observational health data."),
        ("Health Data Science and AI Applications", "Surveys applications of data science and artificial intelligence in public health research and practice."),
        ("Public Health Law", "Examines the legal frameworks underpinning public health authority and practice."),
    ],
}


def next_grade_lesson_index(lessons: list[dict]) -> int:
    max_idx = 0
    for lesson in lessons:
        m = re.search(r"-l(\d+)$", lesson.get("id", ""))
        if m:
            max_idx = max(max_idx, int(m.group(1)))
    return max_idx + 1


def build_grade_lesson(grade: int, index: int, title: str, unit: str, objectives: list[str], reading_material: str) -> dict:
    return {
        "id": f"hlt-g{grade}-l{index}",
        "title": title,
        "unit": unit,
        "grade": grade,
        "subject": SUBJECT,
        "difficulty": "beginner" if grade <= 5 else "intermediate",
        "estimated_time_minutes": 25 if grade <= 5 else 35,
        "learning_objectives": objectives,
        "reading_material": reading_material,
        "key_concepts": [w.strip(",.:&") for w in title.split() if len(w) > 3][:5] or [title],
        "practical_activities": [f"Class discussion and worksheet on {title.lower()}", f"Reflection journal entry about {title.lower()}"],
        "exercises": [{"q": f"In your own words, what is the main idea of '{title}'?", "type": "short_answer", "answer": reading_material.split(".")[0] + "."}],
        "homework": {"task": f"Talk with a family member about what you learned in '{title}' today.", "due": "next_class"},
        "revision": {"notes": reading_material.split(".")[0] + ".", "tip": f"Review '{title}' before the next health lesson."},
        "quiz": {"questions": [{"q": f"Which best describes '{title}'?", "options": [reading_material.split(".")[0] + ".", "Unrelated to this subject", "Not covered at this level", "None of the above"], "answer": reading_material.split(".")[0] + "."}]},
        "assessment": {"type": "written_test", "criteria": [f"Understands {title.lower()}", "Applies concept correctly", "Connects to real-world context"], "passing_score": 60},
        "prerequisites": [],
        "next_lessons": [],
        "textbook_references": [],
        "video_reference": "",
        "progress_tracking": {"completion_required": True, "min_quiz_score": 60},
    }


def main() -> None:
    grade_added = 0
    for grade, topics in GRADE_TOPICS.items():
        path = SYLLABUS_DIR / f"grade{grade}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data.get("subjects", data)
        content = subjects[SUBJECT]
        lessons = content.setdefault("lessons", [])
        existing_titles = {l.get("title") for l in lessons}
        idx = next_grade_lesson_index(lessons)
        for title, unit, objectives, reading_material in topics:
            if title in existing_titles:
                continue
            lessons.append(build_grade_lesson(grade, idx, title, unit, objectives, reading_material))
            existing_titles.add(title)
            idx += 1
            grade_added += 1
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    college_added = 0
    for level, modules in COLLEGE_TOPICS.items():
        path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        subjects = data["subjects"]
        content = subjects[SUBJECT]
        lessons = content.setdefault("lessons", [])
        existing_titles = {l.get("title") for l in lessons}
        max_idx = 0
        for lesson in lessons:
            m = re.search(r"-l(\d+)$", lesson.get("id", ""))
            if m:
                max_idx = max(max_idx, int(m.group(1)))
        idx = max_idx + 1
        for title, summary in modules:
            if title in existing_titles:
                continue
            lessons.append(_lesson_for(SUBJECT, level, idx, title, summary))
            existing_titles.add(title)
            idx += 1
            college_added += 1
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added {grade_added} K-12 Health Education lessons and {college_added} college-level lessons.")
    print(f"Total new lessons added: {grade_added + college_added}")


if __name__ == "__main__":
    main()
