#!/usr/bin/env python3
"""Populate the "Philosophy & Religion" biography category with real,
verified philosophers and religious figures. See _biography_engine.py for
the no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_philosophy_religion.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="socrates", name="Socrates", years="c. 470-399 BCE", nationality="Ancient Greek (Athenian)",
        field="philosopher", wiki_title="Socrates",
        significance="considered one of the founders of Western philosophy, his method of questioning to expose contradictions in belief, known as the Socratic method, remains a foundational technique in education and philosophy",
        facts=[
            "Socrates was born in Athens around 470 BCE, the son of a stonemason",
            "He left no writings of his own; almost everything known about his teachings comes from the accounts of his students, especially Plato and Xenophon",
            "He developed a method of teaching through repeated questioning, now called the Socratic method, aimed at exposing contradictions and clarifying ideas",
            "He famously claimed that his wisdom consisted only in knowing that he knew nothing, a stance now called 'Socratic ignorance'",
            "In 399 BCE he was tried by an Athenian jury on charges of corrupting the youth and impiety toward the city's gods",
            "He was found guilty and sentenced to death by drinking poison hemlock, a scene later described in detail by Plato in the dialogue Phaedo",
            "His trial and death, and his refusal to escape when given the opportunity, became one of the most discussed episodes in the history of philosophy",
        ], related_subjects=["Philosophy", "World History"],
    ),
    dict(
        id="plato", name="Plato", years="c. 428-348 BCE", nationality="Ancient Greek (Athenian)",
        field="philosopher", wiki_title="Plato",
        significance="a student of Socrates and teacher of Aristotle, his dialogues, especially The Republic, laid foundational groundwork for Western philosophy, political theory, and metaphysics",
        facts=[
            "Plato was born in Athens around 428 BCE, into an aristocratic family",
            "He was a devoted student of Socrates, and after Socrates's execution in 399 BCE, Plato left Athens for a period before eventually returning",
            "Around 387 BCE he founded the Academy in Athens, often considered the first institution of higher learning in the Western world",
            "His most famous work, The Republic, explores justice, the ideal state, and includes the well-known Allegory of the Cave describing human perception of reality",
            "He wrote almost entirely in the form of dialogues, often featuring Socrates as the central speaker, blending his own philosophy with his teacher's ideas",
            "His theory of Forms proposed that abstract, non-physical ideas represent the truest reality, more real than the physical world we perceive",
            "He taught Aristotle at the Academy, who would go on to become one of the most influential philosophers in history in his own right",
        ], related_subjects=["Philosophy", "World History"],
    ),
    dict(
        id="aristotle", name="Aristotle", years="384-322 BCE", nationality="Ancient Greek",
        field="philosopher and scientist", wiki_title="Aristotle",
        significance="a student of Plato and tutor to Alexander the Great, his writings on logic, ethics, biology, and politics formed the basis of much of Western intellectual thought for nearly two thousand years",
        facts=[
            "Aristotle was born in Stagira, in northern Greece, in 384 BCE, the son of a physician",
            "He studied under Plato at the Academy in Athens for roughly 20 years",
            "He served as a tutor to the young Alexander the Great at the court of Macedon",
            "He founded his own school in Athens, the Lyceum, around 335 BCE",
            "He wrote extensively across nearly every field of knowledge of his time, including logic, physics, biology, ethics, politics, and poetics",
            "His system of logical reasoning, including the syllogism, remained the dominant framework for formal logic in the Western world for over two thousand years",
            "His surviving works were preserved and transmitted in part through medieval Islamic scholars before returning to prominence in medieval European universities",
        ], related_subjects=["Philosophy", "Biology", "World History"],
    ),
    dict(
        id="confucius", name="Confucius", years="551-479 BCE", nationality="Ancient Chinese",
        field="philosopher and teacher", wiki_title="Confucius",
        significance="his teachings on ethics, family, and social harmony, compiled by his students in the Analects, formed the basis of Confucianism, which shaped Chinese society, government, and education for over two thousand years",
        facts=[
            "Confucius was born in the state of Lu, in present-day Shandong province, China, in 551 BCE",
            "He worked briefly in government positions before spending much of his life traveling and teaching students his philosophy",
            "His core teachings emphasized virtues including ren (benevolence), li (proper conduct), and filial piety, respect for one's parents and ancestors",
            "His sayings and conversations were compiled by his students after his death into a text known as the Analects",
            "His philosophy, later known as Confucianism, became the basis of the Chinese imperial civil service examination system for over a thousand years",
            "Confucian ideas about social hierarchy, education, and moral cultivation deeply influenced not only China but also Korea, Japan, and Vietnam",
            "He died in 479 BCE, and temples dedicated to him remain active sites of veneration across East Asia today",
        ], related_subjects=["Philosophy", "World History", "World Religions"],
    ),
    dict(
        id="the_buddha", name="Siddhartha Gautama (the Buddha)", years="c. 563-483 BCE", nationality="Ancient Indian (Nepalese)",
        field="spiritual teacher, founder of Buddhism", wiki_title="Gautama Buddha",
        significance="his teachings on the nature of suffering and the path to spiritual liberation formed the foundation of Buddhism, now practiced by hundreds of millions of people worldwide",
        facts=[
            "Siddhartha Gautama was born into a royal family in Lumbini, in present-day Nepal, around 563 BCE",
            "According to traditional accounts, he lived a sheltered life of privilege until encountering old age, sickness, and death for the first time, which prompted a spiritual crisis",
            "He left his royal life around age 29 to seek spiritual understanding, living for years as an ascetic before rejecting extreme self-denial as well",
            "He is said to have attained enlightenment while meditating under a Bodhi tree in Bodh Gaya, in present-day India, after which he became known as the Buddha, meaning 'the awakened one'",
            "His core teachings, known as the Four Noble Truths, address the nature of suffering and outline the Eightfold Path as a way to end it",
            "He spent decades traveling and teaching across the Ganges plain of northern India, gathering a large community of monks and lay followers",
            "He died around 483 BCE, and his teachings were later compiled by his followers, eventually spreading across Asia and, in modern times, worldwide",
        ], related_subjects=["World Religions", "Philosophy", "World History"],
    ),
    dict(
        id="jesus_of_nazareth", name="Jesus of Nazareth", years="c. 4 BCE-c. 30/33 CE", nationality="Judean (Roman province)",
        field="religious teacher, central figure of Christianity", wiki_title="Jesus",
        significance="his life and teachings, as recorded in the Christian New Testament, form the foundation of Christianity, now the world's largest religion with over two billion adherents",
        facts=[
            "According to the Christian New Testament, Jesus was born in Bethlehem and raised in Nazareth, in the Roman province of Judea",
            "He began a public ministry as an itinerant teacher and healer around age 30, according to the Gospel accounts",
            "His recorded teachings emphasized love of God and neighbor, compassion for the poor and marginalized, and forgiveness, often conveyed through parables",
            "He gathered a group of twelve close followers, known as the apostles, according to the Gospel narratives",
            "He was crucified by Roman authorities in Jerusalem, an event Christians commemorate as central to the religion's understanding of salvation",
            "Christians believe he rose from the dead three days after his crucifixion, an event known as the Resurrection and central to Christian faith",
            "His life and teachings, recorded primarily in the four Gospels of the New Testament, form the historical and theological foundation of Christianity, practiced today by over two billion people worldwide",
        ], related_subjects=["World Religions", "World History"],
    ),
    dict(
        id="prophet_muhammad", name="Prophet Muhammad", years="c. 570-632 CE", nationality="Arabian",
        field="religious leader, founder of Islam", wiki_title="Muhammad",
        significance="Muslims believe he received revelations from God that were compiled into the Quran, and his life and teachings form the foundation of Islam, now practiced by nearly two billion people worldwide",
        facts=[
            "Muhammad was born in Mecca, in present-day Saudi Arabia, around 570 CE, and was orphaned at a young age",
            "He worked as a merchant in his early adulthood before, according to Islamic tradition, receiving his first revelation from the angel Gabriel around 610 CE while meditating in a cave near Mecca",
            "The revelations he is believed to have received over the following 23 years were later compiled into the Quran, the central religious text of Islam",
            "Facing persecution in Mecca for his monotheistic teachings, he and his followers migrated to Medina in 622 CE, an event known as the Hijra, which marks the beginning of the Islamic calendar",
            "He built a growing community in Medina and eventually returned to Mecca in 630 CE, largely uniting the Arabian Peninsula under Islam by the time of his death",
            "His sayings and actions, known as the Hadith, form a second major source of Islamic teaching and law alongside the Quran",
            "He died in Medina in 632 CE, and Muslims regard him as the final prophet in a line that includes earlier figures such as Abraham, Moses, and Jesus",
        ], related_subjects=["World Religions", "World History"],
    ),
    dict(
        id="moses", name="Moses", years="traditionally c. 13th century BCE", nationality="Ancient Hebrew (Israelite)",
        field="religious leader and lawgiver", wiki_title="Moses",
        significance="according to the Hebrew Bible, he led the Israelites out of slavery in Egypt and received the Ten Commandments, making him a central figure in Judaism, Christianity, and Islam",
        facts=[
            "According to the biblical account in the Book of Exodus, Moses was born to Hebrew parents in Egypt during a period when Israelites were enslaved there",
            "The narrative describes him being placed in a basket on the Nile River as an infant to escape a decree ordering the death of Hebrew baby boys, and being raised in the Egyptian royal household",
            "He is described as leading the Israelites out of slavery in Egypt in an event known as the Exodus, a foundational narrative in Jewish tradition and celebrated annually at Passover",
            "According to the biblical account, he received the Ten Commandments from God on Mount Sinai, a central text of religious and ethical law in Judaism, Christianity, and Islam",
            "He is described as leading the Israelites for 40 years through the wilderness toward the Promised Land, though according to the text he himself did not enter it",
            "He is regarded as the most important prophet in Judaism and is also honored as a prophet in Christianity and Islam",
            "The five books traditionally attributed to him, the Torah or Pentateuch, form the foundational texts of Jewish law and tradition",
        ], related_subjects=["World Religions", "World History"],
    ),
    dict(
        id="thomas_aquinas", name="Thomas Aquinas", years="1225-1274", nationality="Italian",
        field="theologian and philosopher", wiki_title="Thomas Aquinas",
        significance="his synthesis of Christian theology with Aristotelian philosophy, especially in his Summa Theologica, became the dominant framework of Catholic theology and remains highly influential today",
        facts=[
            "Thomas Aquinas was born near Aquino, in the Kingdom of Sicily, in what is now Italy, around 1225",
            "He joined the Dominican religious order as a young man, against the wishes of his noble family, who reportedly held him captive for nearly a year in an attempt to change his mind",
            "He studied and later taught at the University of Paris, one of the leading centers of theological and philosophical study in medieval Europe",
            "His major work, the Summa Theologica, attempted a comprehensive synthesis of Christian doctrine with the philosophy of Aristotle, whose works had recently been reintroduced to Europe via Islamic and Byzantine scholars",
            "He developed 'the Five Ways', five philosophical arguments for the existence of God, which remain studied in philosophy and theology courses today",
            "He was canonized as a saint by the Catholic Church in 1323, less than 50 years after his death",
            "In 1879 Pope Leo XIII declared his theology to be the standard for Catholic education, and his influence on Catholic thought remains significant today",
        ], related_subjects=["Philosophy", "World Religions"],
    ),
    dict(
        id="guru_nanak", name="Guru Nanak", years="1469-1539", nationality="Indian (Punjabi)",
        field="spiritual teacher, founder of Sikhism", wiki_title="Guru Nanak",
        significance="he founded Sikhism, teaching the principles of one formless God, equality among all people, and honest living, and is revered as the first of the ten Sikh Gurus",
        facts=[
            "Guru Nanak was born in 1469 in Talwandi, in the Punjab region of what is now Pakistan",
            "He is said to have had a profound spiritual experience in his late twenties, after which he began preaching a message of one formless God and the equality of all people regardless of caste, gender, or religion",
            "He undertook extensive travels, known as udasis, across South Asia and reportedly as far as the Middle East, spreading his teachings",
            "He rejected many rigid ritual practices of the time and emphasized honest work, sharing with others, and remembering God, principles later summarized as core Sikh values",
            "He composed hymns that were later compiled, along with the writings of subsequent Gurus, into the Guru Granth Sahib, the central religious scripture of Sikhism",
            "He established a community at Kartarpur, in present-day Pakistan, that practiced communal living, worship, and equality regardless of social background",
            "He is revered as the first of the ten Sikh Gurus, and his birthday, Guru Nanak Gurpurab, remains one of the most important Sikh religious observances",
        ], related_subjects=["World Religions", "World History"],
    ),
    dict(
        id="immanuel_kant", name="Immanuel Kant", years="1724-1804", nationality="German (Prussian)",
        field="philosopher", wiki_title="Immanuel Kant",
        significance="his critical philosophy, especially the Critique of Pure Reason, reshaped Western philosophy's understanding of knowledge, ethics, and human reason, and remains central to philosophical study today",
        facts=[
            "Immanuel Kant was born in Konigsberg, Prussia, in 1724, and rarely traveled far from his hometown for his entire life",
            "He published his most influential work, the Critique of Pure Reason, in 1781, examining the limits and structure of human knowledge and reason",
            "He proposed that the human mind actively structures experience through inherent categories, rather than passively receiving raw information from the senses",
            "In ethics he developed the concept of the categorical imperative, a principle that moral actions should be based on rules one could will to be universal laws",
            "He argued for a form of perpetual peace among nations based on republican government and international cooperation, ideas later cited as influences on the League of Nations and United Nations",
            "He maintained a notoriously strict daily routine, reportedly so regular that neighbors were said to set their clocks by his afternoon walks",
            "He died in Konigsberg in 1804, and remains one of the most studied and influential philosophers in the Western tradition",
        ], related_subjects=["Philosophy"],
    ),
    dict(
        id="rumi", name="Rumi", years="1207-1273", nationality="Persian",
        field="poet and Islamic scholar", wiki_title="Rumi",
        significance="his mystical poetry, exploring themes of divine love and spiritual longing, made him one of the best-selling poets in the United States centuries after his death, and inspired the Sufi Mevlevi order known for whirling meditation",
        facts=[
            "Jalal ad-Din Muhammad Rumi was born in Balkh, in present-day Afghanistan, in 1207, and his family later settled in Konya, in present-day Turkey",
            "He was trained as an Islamic scholar and jurist, following in his father's footsteps, before his life took a profound spiritual turn",
            "His meeting with the wandering mystic Shams-e Tabrizi around 1244 transformed him into an ecstatic poet exploring themes of divine love and spiritual union",
            "His major poetic work, the Masnavi, spans six volumes and is sometimes called 'the Quran in Persian' for its spiritual depth within Islamic mystical tradition",
            "His followers founded the Mevlevi Sufi order after his death, known in the West for the practice of 'whirling', a form of physically turning meditation intended to induce spiritual focus",
            "His poetry has been translated into numerous languages, and English translations, particularly popularized versions, made him one of the best-selling poets in the United States by the late 20th century",
            "He died in Konya in 1273, and his shrine there remains a major site of pilgrimage today",
        ], related_subjects=["World Religions", "World Literature", "Philosophy"],
    ),
    dict(
        id="martin_luther", name="Martin Luther", years="1483-1546", nationality="German",
        field="theologian and religious reformer", wiki_title="Martin Luther",
        significance="his 1517 Ninety-Five Theses criticizing Catholic Church practices sparked the Protestant Reformation, permanently reshaping Christianity in Europe and beyond",
        facts=[
            "Martin Luther was born in Eisleben, in what is now Germany, in 1483, and became an Augustinian monk before turning to theology",
            "In 1517 he wrote the Ninety-Five Theses, a document criticizing the Catholic Church's practice of selling indulgences, which he reportedly posted on the door of Wittenberg's Castle Church",
            "His writings, spread rapidly by the recently invented printing press, sparked the Protestant Reformation, a movement that split Western Christianity",
            "He was excommunicated by the Pope in 1521 and declared an outlaw by the Holy Roman Empire, but was protected by sympathetic German princes",
            "He translated the New Testament, and later the entire Bible, into German, making scripture directly accessible to ordinary German speakers for the first time and significantly shaping the modern German language",
            "He argued for the doctrine of justification by faith alone, a central theological difference from Catholic teaching",
            "He died in Eisleben in 1546, and Lutheranism, the branch of Protestant Christianity that grew from his teachings, remains one of the largest Christian denominations today",
        ], related_subjects=["World Religions", "World History"],
    ),
    dict(
        id="rene_descartes", name="Rene Descartes", years="1596-1650", nationality="French",
        field="philosopher and mathematician", wiki_title="Rene Descartes",
        significance="often called the father of modern Western philosophy, his method of systematic doubt and famous conclusion 'I think, therefore I am' (Cogito, ergo sum) reshaped how philosophers approached questions of knowledge and certainty",
        facts=[
            "Rene Descartes was born in La Haye en Touraine, France, in 1596",
            "He served briefly as a soldier before dedicating himself to philosophy and mathematics",
            "In his 1637 work Discourse on the Method, he developed a systematic approach of doubting everything that could possibly be doubted, in order to find a foundation of certain knowledge",
            "He concluded that the one thing he could not doubt was his own thinking, expressed in the famous phrase 'Cogito, ergo sum' ('I think, therefore I am')",
            "He is credited with developing the Cartesian coordinate system, connecting algebra and geometry, which remains fundamental to mathematics today",
            "He proposed a strong distinction between mind and body, known as Cartesian dualism, which became a central and much-debated topic in later philosophy",
            "He died in Stockholm, Sweden, in 1650, while serving as a philosophy tutor to Queen Christina",
        ], related_subjects=["Philosophy", "Math"],
    ),
    dict(
        id="friedrich_nietzsche", name="Friedrich Nietzsche", years="1844-1900", nationality="German",
        field="philosopher", wiki_title="Friedrich Nietzsche",
        significance="his challenging critiques of traditional morality, religion, and truth, expressed in works like Thus Spoke Zarathustra, profoundly influenced 20th-century philosophy, literature, and psychology",
        facts=[
            "Friedrich Nietzsche was born in Rocken, in what is now Germany, in 1844, the son of a Lutheran pastor",
            "He became the youngest person ever appointed to a full professorship of classical philology at the University of Basel, at age 24",
            "His 1883-1885 work Thus Spoke Zarathustra introduced the concept of the 'ubermensch' (overman), an individual who creates their own values beyond conventional morality",
            "He famously declared 'God is dead' in his work The Gay Science, using the phrase to describe the declining cultural authority of traditional religious belief in modern society, not as a literal claim",
            "He developed the concept of 'will to power' as a fundamental driving force in human behavior and life more broadly",
            "He suffered a severe mental breakdown in 1889 and spent the last decade of his life in a state of significant mental incapacity, cared for by his mother and later his sister",
            "His work has been interpreted in widely varying and sometimes conflicting ways since his death in 1900, and remains among the most widely read and debated in modern philosophy",
        ], related_subjects=["Philosophy"],
    ),
    dict(
        id="karl_marx", name="Karl Marx", years="1818-1883", nationality="German",
        field="philosopher and economist", wiki_title="Karl Marx",
        significance="his critique of capitalism, developed with Friedrich Engels in works including The Communist Manifesto and Das Kapital, became the foundational theoretical basis for socialist and communist political movements worldwide",
        facts=[
            "Karl Marx was born in Trier, in what is now Germany, in 1818, and studied law and philosophy before turning to journalism and political economy",
            "He met Friedrich Engels in the 1840s, beginning a lifelong intellectual partnership and close friendship",
            "In 1848 he and Engels published The Communist Manifesto, arguing that human history is shaped by class struggle and calling for workers to unite against capitalist exploitation",
            "He spent much of his later life in London, where he conducted extensive research at the British Museum library while living in considerable poverty, often financially supported by Engels",
            "His major work, Das Kapital, the first volume of which was published in 1867, offered a detailed critique of capitalist economics, including his theory of surplus value",
            "His ideas provided the theoretical foundation for socialist and later communist political movements, including those that came to power in the Soviet Union, China, and elsewhere in the 20th century",
            "He died in London in 1883, and remains one of the most influential and controversial thinkers in modern history",
        ], related_subjects=["Philosophy", "Economics"],
    ),
    dict(
        id="hannah_arendt", name="Hannah Arendt", years="1906-1975", nationality="German-American",
        field="political philosopher", wiki_title="Hannah Arendt",
        significance="her analysis of totalitarianism and her controversial coverage of the Adolf Eichmann trial, in which she coined the phrase 'the banality of evil', made her one of the most significant political philosophers of the 20th century",
        facts=[
            "Hannah Arendt was born in Linden, Germany, in 1906, into a secular Jewish family",
            "She fled Nazi Germany in 1933 after briefly being detained by the Gestapo, eventually settling in the United States in 1941",
            "Her 1951 book The Origins of Totalitarianism analyzed the political and social conditions that allowed Nazi and Stalinist totalitarian regimes to arise",
            "She reported on the 1961 trial of Nazi official Adolf Eichmann in Jerusalem for The New Yorker magazine, later published as the book Eichmann in Jerusalem",
            "In that work she coined the phrase 'the banality of evil', arguing that Eichmann's crimes stemmed less from monstrous ideological fanaticism than from a disturbing, bureaucratic thoughtlessness",
            "The book generated significant controversy, including sharp criticism from some in the Jewish community over her characterization of both Eichmann and some Jewish community leaders during the Holocaust",
            "She taught at several American universities, including the New School for Social Research in New York, and died in 1975",
        ], related_subjects=["Philosophy", "World History", "Civics"],
    ),
    dict(
        id="simone_de_beauvoir", name="Simone de Beauvoir", years="1908-1986", nationality="French",
        field="philosopher and writer", wiki_title="Simone de Beauvoir",
        significance="her 1949 book The Second Sex, examining the historical and social construction of womanhood, became a foundational text of modern feminist philosophy",
        facts=[
            "Simone de Beauvoir was born in Paris, France, in 1908, and became one of the youngest people ever to pass the demanding agregation examination in philosophy in France",
            "She maintained a lifelong intellectual and personal partnership with philosopher Jean-Paul Sartre, though the two never married and maintained an openly non-monogamous relationship",
            "Her 1949 book The Second Sex offered a detailed philosophical and historical examination of how society constructs and constrains the category of 'woman', opening with the influential line 'One is not born, but rather becomes, a woman'",
            "The book was controversial upon publication, and was placed on the Catholic Church's list of banned books, but became a foundational text of 20th-century feminist philosophy",
            "She was closely associated with the existentialist philosophical movement, examining questions of freedom, choice, and ethical responsibility in works including her novel The Mandarins, which won France's Prix Goncourt in 1954",
            "She was active in political and social causes throughout her life, including advocacy for reproductive rights and involvement in French intellectual debates over colonialism, particularly regarding Algeria",
            "She died in Paris in 1986, and is buried alongside Jean-Paul Sartre in the Montparnasse Cemetery",
        ], related_subjects=["Philosophy", "Civics"],
    ),
    dict(
        id="soren_kierkegaard", name="Soren Kierkegaard", years="1813-1855", nationality="Danish",
        field="philosopher and theologian", wiki_title="Soren Kierkegaard",
        significance="often regarded as the first existentialist philosopher, his work on individual choice, anxiety, and religious faith profoundly influenced later existentialist and theological thought",
        facts=[
            "Soren Kierkegaard was born in Copenhagen, Denmark, in 1813, and inherited a substantial fortune from his father that allowed him to write without needing a conventional career",
            "He wrote extensively under various pseudonyms, using different invented authorial personas to explore ideas from multiple, sometimes conflicting, philosophical perspectives",
            "His work frequently focused on the nature of individual choice and commitment, particularly the difficulty and anxiety involved in making genuine, authentic decisions",
            "His 1843 book Fear and Trembling examined the biblical story of Abraham's near-sacrifice of Isaac as a way of exploring the tension between ethical duty and religious faith",
            "He was strongly critical of what he saw as the shallow, conformist Christianity of the official Danish state church of his time, arguing for a more demanding, personally committed form of faith",
            "His concept of 'anxiety' or 'dread' as a fundamental part of human freedom and self-awareness later strongly influenced 20th-century existentialist philosophers, including Jean-Paul Sartre and Martin Heidegger",
            "He died in Copenhagen in 1855 at age 42, and is now widely regarded as a foundational figure of existentialist philosophy",
        ], related_subjects=["Philosophy", "World Religions"],
    ),
    dict(
        id="al_ghazali", name="Al-Ghazali", years="1058-1111", nationality="Persian",
        field="Islamic theologian and philosopher", wiki_title="Al-Ghazali",
        significance="one of the most influential Islamic scholars in history, his synthesis of philosophy, theology, and Sufi mysticism in works such as The Incoherence of the Philosophers profoundly shaped later Islamic thought",
        facts=[
            "Al-Ghazali was born in Tus, in present-day Iran, in 1058",
            "He became a leading professor of Islamic law and theology at the prestigious Nizamiyyah Madrasa in Baghdad while still a young man",
            "His book The Incoherence of the Philosophers critically examined and challenged the ideas of earlier Islamic philosophers who had drawn heavily on Greek philosophical traditions, particularly Aristotle",
            "After reaching a position of significant intellectual authority, he underwent a profound spiritual crisis around 1095, leading him to abandon his prestigious teaching post and adopt a more austere, mystically-oriented Sufi lifestyle for a period of years",
            "His major later work, The Revival of the Religious Sciences, sought to integrate Islamic law, theology, and Sufi spiritual practice into a comprehensive framework for religious life",
            "He is often credited with helping bring Sufi mystical practice into closer harmony with mainstream Sunni Islamic theology, reducing tension between the two traditions",
            "He died in Tus in 1111, and remains one of the most widely studied and influential scholars in the history of Islamic thought, sometimes given the honorific title 'Proof of Islam'",
        ], related_subjects=["Philosophy", "World Religions"],
    ),
]


def main() -> None:
    upsert_section(
        "philosophy_religion",
        "Philosophy & Religion",
        "🕊️",
        "Philosophers and religious leaders whose ideas about reason, ethics, and the divine shaped civilizations and continue to guide billions of people today.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
