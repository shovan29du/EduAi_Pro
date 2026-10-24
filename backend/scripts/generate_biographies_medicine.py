#!/usr/bin/env python3
"""Populate the "Medicine & Public Health" biography category with real,
verified physicians and public-health pioneers. See _biography_engine.py
for the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_medicine.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="edward_jenner", name="Edward Jenner", years="1749-1823", nationality="English",
        field="physician, pioneer of vaccination", wiki_title="Edward Jenner",
        significance="his 1796 experiment demonstrating that cowpox exposure could protect against smallpox laid the foundation for vaccination, a medical breakthrough later credited with saving more lives than any other in history",
        facts=[
            "Edward Jenner was born in Berkeley, England, in 1749, and trained as a country doctor",
            "He observed that milkmaids who had previously contracted cowpox, a mild disease, seemed to be immune to the far deadlier smallpox",
            "In 1796 he tested this idea by inoculating a young boy, James Phipps, with material from a cowpox sore, and later exposing him to smallpox, finding he did not develop the disease",
            "He published his findings in 1798, coining the term 'vaccine' from the Latin word for cow, 'vacca'",
            "His method spread rapidly across Europe and eventually worldwide, becoming the basis for the broader practice of vaccination",
            "Smallpox vaccination campaigns building on his work eventually led to the World Health Organization declaring smallpox globally eradicated in 1980, the only human disease eradicated to date",
            "He died in 1823, and is often called 'the father of immunology' for his foundational contribution to vaccine science",
        ], related_subjects=["Health Education", "Biology"],
    ),
    dict(
        id="florence_nightingale_med_ref", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "florence_nightingale_med_ref"]

PEOPLE += [
    dict(
        id="alexander_fleming", name="Alexander Fleming", years="1881-1955", nationality="Scottish",
        field="physician and microbiologist", wiki_title="Alexander Fleming",
        significance="his accidental 1928 discovery of penicillin, the first widely used antibiotic, transformed medicine and is credited with saving hundreds of millions of lives",
        facts=[
            "Alexander Fleming was born near Darvel, Scotland, in 1881, and trained as a physician at St Mary's Hospital in London",
            "In September 1928 he noticed that a mold called Penicillium had contaminated one of his bacterial culture plates and had killed the surrounding bacteria",
            "He identified the active substance produced by the mold and named it penicillin, though he struggled for years to isolate and produce it in usable quantities",
            "In the early 1940s scientists Howard Florey and Ernst Boris Chain developed methods to mass-produce penicillin, making it widely available in time to treat wounded soldiers during World War II",
            "Penicillin became the first widely used antibiotic, dramatically reducing deaths from bacterial infections that had previously often been fatal",
            "He, Florey, and Chain jointly won the Nobel Prize in Physiology or Medicine in 1945 for the discovery and development of penicillin",
            "He warned in his 1945 Nobel lecture that overuse of antibiotics could lead to bacterial resistance, a concern that has proven increasingly significant in modern medicine",
        ], related_subjects=["Health Education", "Biology", "Chemistry"],
    ),
    dict(
        id="jonas_salk", name="Jonas Salk", years="1914-1995", nationality="American",
        field="medical researcher, developer of the polio vaccine", wiki_title="Jonas Salk",
        significance="he developed the first effective vaccine against polio, a disease that had paralyzed or killed hundreds of thousands of children worldwide each year, and chose not to patent it so it could be distributed as widely as possible",
        facts=[
            "Jonas Salk was born in New York City in 1914, the son of Russian Jewish immigrants",
            "He began researching a polio vaccine in the early 1950s at the University of Pittsburgh, at a time when polio epidemics caused widespread fear across the United States",
            "His vaccine used an inactivated (killed) form of the poliovirus, a safer approach than live-virus vaccines being developed by some rivals at the time",
            "In 1954 his vaccine was tested in one of the largest clinical trials in history, involving over 1.8 million American children",
            "The vaccine was announced as safe and effective in April 1955, prompting widespread public celebration and rapid nationwide vaccination campaigns",
            "When asked in a television interview who owned the patent to the vaccine, he famously replied, 'There is no patent. Could you patent the sun?', having deliberately chosen not to seek personal profit from the discovery",
            "He later founded the Salk Institute for Biological Studies in La Jolla, California, which remains a major biomedical research center today",
        ], related_subjects=["Health Education", "Biology"],
    ),
    dict(
        id="elizabeth_blackwell", name="Elizabeth Blackwell", years="1821-1910", nationality="American-British",
        field="physician", wiki_title="Elizabeth Blackwell",
        significance="she became the first woman to receive a medical degree in the United States, in 1849, and worked throughout her career to open the medical profession to other women",
        facts=[
            "Elizabeth Blackwell was born in Bristol, England, in 1821, and emigrated with her family to the United States as a child",
            "She applied to more than a dozen medical schools before being accepted, reportedly after the all-male student body at Geneva Medical College in New York voted, partly as a joke, to admit her",
            "She graduated first in her class in 1849, becoming the first woman to receive a medical degree from an American medical school",
            "She faced significant professional discrimination after graduating, including being denied hospital positions and patients because of her gender",
            "In 1857 she co-founded the New York Infirmary for Indigent Women and Children, a hospital staffed entirely by women, providing both medical care and training opportunities for female doctors",
            "She later helped establish a medical college for women, and returned to England to help found the London School of Medicine for Women in 1874",
            "Her example directly inspired other women to pursue medical careers, including her younger sister Emily Blackwell, who also became a physician",
        ], related_subjects=["Health Education"],
    ),
    dict(
        id="paul_farmer", name="Paul Farmer", years="1959-2022", nationality="American",
        field="physician and medical anthropologist", wiki_title="Paul Farmer",
        significance="co-founder of Partners In Health, he pioneered delivering high-quality medical care to some of the world's poorest communities, arguing that quality healthcare is a basic human right rather than a privilege",
        facts=[
            "Paul Farmer was born in North Adams, Massachusetts, in 1959, and spent part of his childhood living in a converted bus and a boat with his large family",
            "He co-founded the nonprofit organization Partners In Health in 1987, initially focused on providing healthcare in rural Haiti",
            "He argued forcefully against the common assumption at the time that complex medical treatments, including for tuberculosis and HIV, were too difficult or costly to deliver effectively in poor countries",
            "His organization's work in Haiti and later in Peru, Rwanda, and other countries demonstrated that community-based models could deliver effective treatment even for drug-resistant tuberculosis and HIV in resource-poor settings",
            "He held a joint MD and PhD in medical anthropology from Harvard University, combining clinical medicine with a deep understanding of the social causes of illness and poverty",
            "His work significantly influenced global health policy, including approaches later used by the World Health Organization and major international health funders",
            "He died suddenly in 2022 while working at a hospital he had helped establish in Rwanda",
        ], related_subjects=["Health Education", "Civics"],
    ),
    dict(
        id="hippocrates", name="Hippocrates", years="c. 460-370 BCE", nationality="Ancient Greek",
        field="physician", wiki_title="Hippocrates",
        significance="often called the 'Father of Medicine', he and his followers helped establish medicine as a discipline based on observation and reasoning rather than superstition, and the Hippocratic Oath still influences medical ethics today",
        facts=[
            "Hippocrates was born on the Greek island of Kos around 460 BCE",
            "He and his followers argued that diseases had natural causes rather than being punishments from the gods, a significant shift in medical thinking for the time",
            "The body of medical writings associated with him and his school, known as the Hippocratic Corpus, covers topics including diagnosis, prognosis, and medical ethics",
            "The Hippocratic Oath, an ethical code for physicians traditionally attributed to him, includes principles such as doing no harm to patients, which remain influential in medical ethics today",
            "He emphasized careful clinical observation of patients, including diet, environment, and symptoms, as the basis for diagnosis and treatment",
            "Much of what is directly known about his personal life is uncertain, and historians believe some works attributed to him were likely written by his students or followers",
            "The modern medical profession continues to reference him symbolically, and many medical schools have historically included some version of the Hippocratic Oath in graduation ceremonies",
        ], related_subjects=["Health Education", "World History"],
    ),
    dict(
        id="virginia_apgar", name="Virginia Apgar", years="1909-1974", nationality="American",
        field="physician, anesthesiologist", wiki_title="Virginia Apgar",
        significance="she developed the Apgar Score in 1952, a simple, rapid method for assessing the health of newborn infants immediately after birth, which remains standard practice in hospitals worldwide",
        facts=[
            "Virginia Apgar was born in Westfield, New Jersey, in 1909",
            "She became one of the first women to specialize in anesthesiology, and in 1949 became the first woman to hold a full professorship at Columbia University's College of Physicians and Surgeons",
            "In 1952 she developed the Apgar Score, a simple scoring system evaluating a newborn's heart rate, breathing, muscle tone, reflexes, and color one and five minutes after birth",
            "The Apgar Score allowed medical staff to quickly identify newborns who needed immediate medical attention, significantly improving early neonatal care",
            "The score remains in standard use in hospitals around the world today, over 70 years after she developed it",
            "Later in her career she worked with the March of Dimes Foundation, focusing on research into birth defects",
            "She died in 1974, and in 1994 the US Postal Service issued a postage stamp honoring her contribution to medicine",
        ], related_subjects=["Health Education"],
    ),
    dict(
        id="william_osler", name="William Osler", years="1849-1919", nationality="Canadian",
        field="physician and medical educator", wiki_title="William Osler",
        significance="often called the 'Father of Modern Medicine', he transformed medical education by insisting students learn directly at patients' bedsides rather than solely from lectures and textbooks",
        facts=[
            "William Osler was born in Bond Head, Ontario, Canada, in 1849",
            "He was one of the four founding professors of Johns Hopkins Hospital in Baltimore in 1889, alongside William Halsted, Howard Kelly, and William Welch",
            "He pioneered the modern medical residency training system, having young doctors live and work at the hospital to learn through direct clinical experience",
            "He insisted that medical students learn primarily through direct examination of patients at the bedside, rather than relying mainly on lectures, a philosophy captured in his phrase 'He who studies medicine without books sails an uncharted sea'",
            "His 1892 textbook, The Principles and Practice of Medicine, became a standard medical reference used for decades across the English-speaking world",
            "He later became Regius Professor of Medicine at Oxford University in England, one of the most prestigious medical positions in the world at the time",
            "He died in 1919, and the bedside teaching and residency training methods he championed remain foundational to modern medical education",
        ], related_subjects=["Health Education"],
    ),
    dict(
        id="frederick_banting", name="Frederick Banting", years="1891-1941", nationality="Canadian",
        field="physician, co-discoverer of insulin", wiki_title="Frederick Banting",
        significance="he co-discovered insulin in 1921, transforming diabetes from a nearly always fatal diagnosis into a manageable chronic condition, and became the youngest Nobel laureate in Physiology or Medicine at the time",
        facts=[
            "Frederick Banting was born near Alliston, Ontario, Canada, in 1891, and served as a medical officer during World War I, where he was wounded and decorated for bravery",
            "In 1921, working with medical student Charles Best at the University of Toronto, he successfully isolated insulin from animal pancreases",
            "Before this discovery, type 1 diabetes was essentially a fatal diagnosis, with patients, particularly children, often dying within a year or two of onset",
            "The first human patient treated with insulin, a 14-year-old boy named Leonard Thompson, showed dramatic improvement in January 1922",
            "He won the Nobel Prize in Physiology or Medicine in 1923, sharing it with biochemist John Macleod, whose laboratory had supported the research; Banting was, at the time, the youngest Nobel laureate in that category",
            "He controversially felt that his research partner Charles Best deserved the prize more than Macleod did, and shared his own prize money with Best in protest",
            "He and his colleagues chose not to personally profit from the discovery, selling the insulin patent to the University of Toronto for a nominal fee to ensure the treatment could be produced widely and affordably",
        ], related_subjects=["Health Education", "Biology"],
    ),
    dict(
        id="rene_laennec", name="Rene Laennec", years="1781-1826", nationality="French",
        field="physician, inventor of the stethoscope", wiki_title="Rene Laennec",
        significance="he invented the stethoscope in 1816, a simple wooden tube device that transformed physicians' ability to diagnose heart and lung conditions and remains, in updated form, one of the most recognizable tools in medicine",
        facts=[
            "Rene Laennec was born in Quimper, France, in 1781, and studied medicine in Nantes and Paris",
            "In 1816, needing to listen to the heart of a patient he felt was inappropriate to examine by placing his ear directly on her chest, he rolled a sheet of paper into a tube, inventing the first stethoscope",
            "He refined the device into a simple wooden cylinder, and used it extensively to study and document the sounds associated with various lung and heart conditions",
            "His 1819 treatise on mediate auscultation, describing his findings using the stethoscope, became a foundational text in the diagnosis of respiratory and cardiac disease",
            "His work significantly advanced the understanding and diagnosis of tuberculosis, a disease that would ultimately take his own life",
            "He served as a professor of medicine at the College de France and later at a hospital in Paris",
            "He died of tuberculosis in 1826, and the stethoscope he invented, though much modified since, remains a standard tool used by physicians worldwide today",
        ], related_subjects=["Health Education"],
    ),
    dict(
        id="ibn_sina", name="Ibn Sina (Avicenna)", years="980-1037", nationality="Persian",
        field="physician and philosopher", wiki_title="Avicenna",
        significance="his medical encyclopedia The Canon of Medicine became a standard medical textbook in both the Islamic world and Europe for over 600 years, and he is regarded as one of the most influential physicians in history",
        facts=[
            "Ibn Sina, known in the West by the Latinized name Avicenna, was born near Bukhara, in present-day Uzbekistan, in 980",
            "He reportedly memorized the entire Quran by age 10 and had mastered the medical knowledge of his time by his late teens",
            "His most famous work, The Canon of Medicine, completed around 1025, systematically organized medical knowledge from Greek, Persian, and Islamic sources into a comprehensive, structured reference text",
            "The Canon of Medicine was translated into Latin and used as a standard medical textbook in European universities from the 12th century until as late as the 17th century",
            "He also wrote extensively on philosophy, attempting to reconcile Aristotelian philosophy with Islamic theology, in a body of work that influenced later Islamic and European philosophers alike",
            "He served as a physician and government official for various rulers across Persia and Central Asia during a politically unstable period, and wrote much of his work while traveling",
            "He died in 1037, and remains widely regarded, alongside Hippocrates and Galen, as one of the most significant figures in the history of medicine",
        ], related_subjects=["Health Education", "Philosophy"],
    ),
    dict(
        id="christiaan_barnard", name="Christiaan Barnard", years="1922-2001", nationality="South African",
        field="cardiac surgeon", wiki_title="Christiaan Barnard",
        significance="he performed the world's first successful human-to-human heart transplant in 1967, a landmark achievement in cardiac surgery that captured worldwide attention",
        facts=[
            "Christiaan Barnard was born in Beaufort West, South Africa, in 1922, the son of a minister",
            "He trained as a surgeon in South Africa and later pursued advanced surgical training in the United States",
            "On December 3, 1967, at Groote Schuur Hospital in Cape Town, he led the surgical team that performed the world's first successful human-to-human heart transplant",
            "The patient, Louis Washkansky, survived the surgery and lived for 18 days afterward before dying of pneumonia related to the immunosuppressive drugs used to prevent organ rejection",
            "The operation drew immense worldwide media attention and made Barnard an international celebrity almost overnight",
            "His success helped drive rapid international interest in transplant surgery, though refinements in surgical technique and anti-rejection medication over subsequent decades were needed before heart transplantation became a reliably successful, widely available treatment",
            "He continued performing heart transplants and advocating for organ transplantation research until health issues, including severe arthritis, ended his surgical career, and he died in 2001",
        ], related_subjects=["Health Education", "Biology"],
    ),
    dict(
        id="marie_curie_med_ref_removed", name="__REMOVE__", years="", nationality="", field="", wiki_title="",
        significance="", facts=[], related_subjects=[],
    ),
]

PEOPLE = [p for p in PEOPLE if p["id"] != "marie_curie_med_ref_removed"]

PEOPLE += [
    dict(
        id="anthony_fauci", name="Anthony Fauci", years="1940-present", nationality="American",
        field="physician and immunologist", wiki_title="Anthony Fauci",
        significance="he directed the US National Institute of Allergy and Infectious Diseases for nearly 40 years, advising seven US presidents on public health responses to HIV/AIDS, Ebola, and COVID-19",
        facts=[
            "Anthony Fauci was born in Brooklyn, New York, in 1940, and earned his medical degree from Cornell University Medical College",
            "He became director of the US National Institute of Allergy and Infectious Diseases (NIAID) in 1984, a position he held for nearly 40 years",
            "He played a central role in the US government's response to the HIV/AIDS epidemic beginning in the 1980s, initially facing significant criticism from AIDS activists before later working closely with advocacy groups to accelerate treatment research",
            "He helped develop antiretroviral therapy research strategies that transformed HIV from a near-certain death sentence into a manageable chronic condition for many patients",
            "He advised US presidents from Ronald Reagan through Joe Biden on infectious disease policy, spanning seven administrations",
            "During the COVID-19 pandemic beginning in 2020, he became one of the most prominent public health voices in the United States, providing regular public briefings on the evolving pandemic",
            "He retired from government service in December 2022, after a career that made him one of the most recognized public health officials in modern American history",
        ], related_subjects=["Health Education", "Biology"],
    ),
    dict(
        id="norman_borlaug", name="Norman Borlaug", years="1914-2009", nationality="American",
        field="agricultural scientist", wiki_title="Norman Borlaug",
        significance="often called the 'Father of the Green Revolution', his development of high-yield disease-resistant wheat varieties is credited with saving an estimated one billion people from starvation, and he won the Nobel Peace Prize in 1970",
        facts=[
            "Norman Borlaug was born on a farm near Cresco, Iowa, in 1914",
            "He earned a PhD in plant pathology and genetics from the University of Minnesota before joining an agricultural research program in Mexico in the 1940s",
            "In Mexico he developed new wheat varieties that were resistant to disease and produced dramatically higher yields, particularly when combined with improved farming techniques",
            "These high-yield wheat varieties were later introduced to India and Pakistan in the 1960s, at a time when both countries faced severe famine risk, and rapidly and dramatically increased grain production",
            "His agricultural innovations, alongside similar work on rice, became known collectively as the Green Revolution, credited by many economists and historians with helping prevent mass famine across much of Asia and Latin America",
            "He won the Nobel Peace Prize in 1970, one of the few scientists to receive that award, in recognition of the humanitarian impact of his agricultural research",
            "He continued working on agricultural development, particularly in Africa, until his death in 2009, and is estimated by some historians to have contributed to saving up to a billion lives through increased food production",
        ], related_subjects=["Biology", "Environmental Science", "Health Education"],
    ),
]


def main() -> None:
    upsert_section(
        "medicine_public_health",
        "Medicine & Public Health",
        "🩺",
        "Physicians and public-health pioneers whose discoveries and advocacy saved and continue to save countless lives.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
