#!/usr/bin/env python3
"""Populate the "Literature & Writers" biography category with real,
verified authors and poets. See _biography_engine.py for the
no-fabrication template approach.

Re-run after editing:
    python3 backend/scripts/generate_biographies_literature.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _biography_engine import upsert_section  # noqa: E402

PEOPLE = [
    dict(
        id="william_shakespeare", name="William Shakespeare", years="1564-1616", nationality="English",
        field="playwright and poet", wiki_title="William Shakespeare",
        significance="widely regarded as the greatest writer in the English language, his roughly 39 plays and 154 sonnets remain among the most performed and studied works in world literature",
        facts=[
            "William Shakespeare was born in Stratford-upon-Avon, England, in 1564, and baptized on April 26 of that year",
            "By the early 1590s he was working in London as an actor and playwright, and became a shareholder in the acting company the Lord Chamberlain's Men",
            "His plays include tragedies such as Hamlet, Macbeth, and King Lear, comedies such as A Midsummer Night's Dream, and histories such as Henry V",
            "The Globe Theatre, where many of his plays were performed, was built in London in 1599 by his acting company",
            "He introduced or popularized an estimated 1,700 words into the English language, including terms still in common use today",
            "The First Folio, a collection of 36 of his plays, was published in 1623, seven years after his death, and is credited with preserving many works that might otherwise have been lost",
            "He died in Stratford-upon-Avon in 1616, reportedly on his birthday, April 23",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="jane_austen", name="Jane Austen", years="1775-1817", nationality="English",
        field="novelist", wiki_title="Jane Austen",
        significance="her novels of manners, including Pride and Prejudice, offered sharp social observation of the English gentry and remain widely read and adapted more than two centuries later",
        facts=[
            "Jane Austen was born in Steventon, England, in 1775, the seventh of eight children of a clergyman",
            "She began writing fiction as a teenager, producing short comic pieces for her family's entertainment",
            "Her novels were published anonymously during her lifetime, credited only to 'A Lady'",
            "Pride and Prejudice, published in 1813, is one of the most widely read novels in the English language",
            "Her other major novels include Sense and Sensibility (1811), Emma (1815), and the posthumously published Persuasion and Northanger Abbey (both 1817)",
            "She never married, and her novels often explored the economic pressures on women to marry well in early 19th-century England",
            "She died in 1817 at age 41, likely from Addison's disease, before her authorship was widely publicly acknowledged",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="leo_tolstoy", name="Leo Tolstoy", years="1828-1910", nationality="Russian",
        field="novelist and philosopher", wiki_title="Leo Tolstoy",
        significance="his novels War and Peace and Anna Karenina are widely considered among the greatest works of world literature, and his later philosophy of nonviolence influenced figures such as Mahatma Gandhi",
        facts=[
            "Leo Tolstoy was born into an aristocratic Russian family at Yasnaya Polyana in 1828",
            "He served as an artillery officer in the Crimean War in the 1850s, an experience that shaped his later writing on war",
            "He published War and Peace between 1865 and 1869, a sprawling novel following several families through the Napoleonic Wars",
            "He published Anna Karenina in 1877, a novel exploring love, marriage, and Russian society",
            "In his later life he underwent a profound spiritual crisis and developed a philosophy of Christian anarchism and nonviolent resistance",
            "His writings on nonviolence directly influenced Mahatma Gandhi, who corresponded with him",
            "He died in 1910 at a remote railway station after leaving his family estate, having attempted to live out his philosophy of simplicity and renunciation",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="charles_dickens", name="Charles Dickens", years="1812-1870", nationality="English",
        field="novelist", wiki_title="Charles Dickens",
        significance="his novels, often published in serial installments, vividly depicted the social conditions of Victorian England and remain among the most widely read works of English literature",
        facts=[
            "Charles Dickens was born in Portsmouth, England, in 1812, and as a child was sent to work in a boot-blacking factory after his father was imprisoned for debt",
            "He began his writing career as a journalist before achieving fame with The Pickwick Papers, published in serial form starting in 1836",
            "His novels include Oliver Twist (1838), A Christmas Carol (1843), David Copperfield (1850), and Great Expectations (1861)",
            "Many of his novels were originally published in monthly or weekly installments, a format that shaped his cliffhanger-driven style",
            "His depictions of poverty, child labor, and social inequality helped draw public attention to conditions in Victorian industrial England",
            "He gave public readings of his own works across Britain and the United States, drawing enormous crowds",
            "He died in 1870, leaving his novel The Mystery of Edwin Drood unfinished",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="mark_twain", name="Mark Twain", years="1835-1910", nationality="American",
        field="novelist and humorist", wiki_title="Mark Twain",
        significance="his novels The Adventures of Tom Sawyer and Adventures of Huckleberry Finn are considered foundational works of American literature, and Ernest Hemingway called Huckleberry Finn the source of 'all modern American literature'",
        facts=[
            "Mark Twain was the pen name of Samuel Langhorne Clemens, born in Florida, Missouri, in 1835",
            "He worked as a riverboat pilot on the Mississippi River as a young man, and took his pen name from a term used to measure river depth",
            "His novel The Adventures of Tom Sawyer was published in 1876, drawing on his own childhood in Hannibal, Missouri",
            "Its sequel, Adventures of Huckleberry Finn, published in 1884, is widely regarded as one of the great American novels, though it has also been controversial and frequently banned over its use of racial language",
            "He was also a popular public lecturer and humorist, known for sharp, often satirical social commentary",
            "He suffered severe financial losses later in life due to failed investments, and undertook a global lecture tour to repay his debts",
            "He died in 1910, the year Halley's Comet returned, having predicted years earlier that he would 'go out with it', since he was born the year of its previous appearance in 1835",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="virginia_woolf", name="Virginia Woolf", years="1882-1941", nationality="English",
        field="novelist and essayist", wiki_title="Virginia Woolf",
        significance="a pioneer of modernist fiction and stream-of-consciousness narrative technique, her essay A Room of One's Own became a foundational text of feminist literary criticism",
        facts=[
            "Virginia Woolf was born in London in 1882 and was largely educated at home in her father's extensive library",
            "She was a central figure of the Bloomsbury Group, a circle of English writers, intellectuals, and artists active in the early 20th century",
            "Her novels Mrs Dalloway (1925) and To the Lighthouse (1927) are known for their innovative stream-of-consciousness narrative style",
            "Her 1929 essay A Room of One's Own argued that a woman needs money and a room of her own in order to write fiction, and became a landmark feminist text",
            "She co-founded the Hogarth Press with her husband Leonard Woolf in 1917, which published works by T.S. Eliot and Sigmund Freud among others",
            "She experienced recurring severe mental illness throughout her life, which she wrote about in letters and diaries",
            "She died by suicide in 1941, drowning herself in the River Ouse near her home in Sussex, England",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="ernest_hemingway", name="Ernest Hemingway", years="1899-1961", nationality="American",
        field="novelist and journalist", wiki_title="Ernest Hemingway",
        significance="his spare, understated prose style, developed partly through his early work as a journalist, influenced generations of writers, and he won both the Pulitzer Prize and the Nobel Prize in Literature",
        facts=[
            "Ernest Hemingway was born in Oak Park, Illinois, in 1899, and began his career as a newspaper reporter",
            "He served as an ambulance driver on the Italian front during World War I and was seriously wounded, an experience that shaped his novel A Farewell to Arms (1929)",
            "He lived among the expatriate literary community in Paris in the 1920s, alongside writers like F. Scott Fitzgerald and Gertrude Stein",
            "His novel The Old Man and the Sea, published in 1952, won the Pulitzer Prize for Fiction in 1953",
            "He won the Nobel Prize in Literature in 1954, cited for his mastery of narrative style",
            "He survived two plane crashes during a single trip to Africa in 1954, injuries from which affected his health for the rest of his life",
            "He died by suicide at his home in Ketchum, Idaho, in 1961",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="gabriel_garcia_marquez", name="Gabriel Garcia Marquez", years="1927-2014", nationality="Colombian",
        field="novelist", wiki_title="Gabriel Garcia Marquez",
        significance="his novel One Hundred Years of Solitude helped establish the literary genre of magical realism and became one of the best-selling and most influential Spanish-language novels of the 20th century",
        facts=[
            "Gabriel Garcia Marquez was born in Aracataca, Colombia, in 1927, and was raised largely by his grandparents",
            "He worked as a journalist for several Colombian and international newspapers before turning to fiction",
            "His novel One Hundred Years of Solitude, published in 1967, sold more than 50 million copies and was translated into dozens of languages",
            "The novel is considered a defining work of magical realism, a genre blending realistic narrative with fantastical elements",
            "He won the Nobel Prize in Literature in 1982, cited for novels and short stories in which fantasy and reality combine to reflect Latin American life",
            "He was a close friend of Cuban leader Fidel Castro, a relationship that drew both admiration and criticism",
            "He died in Mexico City in 2014, and was mourned across the Spanish-speaking world as one of its greatest writers",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="rabindranath_tagore_lit", name="Rabindranath Tagore", years="1861-1941", nationality="Indian (Bengali)",
        field="poet, writer, and composer", wiki_title="Rabindranath Tagore",
        significance="he became the first non-European to win the Nobel Prize in Literature, in 1913, for his collection of poems Gitanjali, and composed the national anthems of both India and Bangladesh",
        facts=[
            "Rabindranath Tagore was born in Calcutta in 1861 into a wealthy and culturally prominent Bengali family",
            "He began writing poetry as a child and published his first substantial poetry collection as a teenager",
            "In 1913 he won the Nobel Prize in Literature for Gitanjali (Song Offerings), becoming the first non-European laureate in the category",
            "He composed 'Jana Gana Mana', which became the national anthem of India, and 'Amar Shonar Bangla', which became the national anthem of Bangladesh",
            "He founded Visva-Bharati University in Santiniketan, West Bengal, in 1921, based on his own progressive educational philosophy",
            "He was a prolific writer across many forms, producing novels, short stories, plays, essays, and thousands of songs, in addition to poetry",
            "He renounced the British knighthood he had been given, in 1919, in protest against the Jallianwala Bagh massacre in Amritsar",
        ], related_subjects=["World Literature", "Music"],
    ),
    dict(
        id="maya_angelou", name="Maya Angelou", years="1928-2014", nationality="American",
        field="poet and memoirist", wiki_title="Maya Angelou",
        significance="her 1969 memoir I Know Why the Caged Bird Sings broke new ground in autobiographical writing about race and trauma, and she became one of the most celebrated American poets of her generation",
        facts=[
            "Maya Angelou was born Marguerite Annie Johnson in St. Louis, Missouri, in 1928",
            "Her 1969 memoir I Know Why the Caged Bird Sings recounted her childhood, including experiencing racism and sexual abuse, and became a landmark of American autobiographical writing",
            "Before becoming a writer, she worked as, among other things, a dancer, singer, and the first Black female cable car conductor in San Francisco",
            "She worked closely with civil rights leaders Martin Luther King Jr. and Malcolm X during the 1960s",
            "She wrote and delivered the poem 'On the Pulse of Morning' at President Bill Clinton's 1993 inauguration",
            "She received over 50 honorary degrees during her lifetime despite never completing a college degree herself",
            "President Barack Obama awarded her the Presidential Medal of Freedom in 2011",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="fyodor_dostoevsky", name="Fyodor Dostoevsky", years="1821-1881", nationality="Russian",
        field="novelist", wiki_title="Fyodor Dostoevsky",
        significance="his novels, including Crime and Punishment and The Brothers Karamazov, explored psychology, morality, and faith with a depth that profoundly influenced later philosophy and literature",
        facts=[
            "Fyodor Dostoevsky was born in Moscow in 1821, the son of a doctor",
            "In 1849 he was arrested for participating in a group discussing banned political literature and sentenced to death by firing squad",
            "His execution was halted at the last moment by a staged reprieve, a traumatic experience he later described in his fiction, and his sentence was commuted to exile and hard labor in Siberia",
            "He published Crime and Punishment in 1866, exploring the psychology of a man who commits murder and its moral aftermath",
            "He struggled with a gambling addiction for much of his life, which strongly informed his 1867 novella The Gambler",
            "His final novel, The Brothers Karamazov, published in 1880, is widely regarded as one of the supreme achievements in world literature",
            "He died in St. Petersburg in 1881, and tens of thousands of mourners reportedly attended his funeral",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="toni_morrison", name="Toni Morrison", years="1931-2019", nationality="American",
        field="novelist", wiki_title="Toni Morrison",
        significance="her novels, including Beloved, explored the Black American experience with a depth and lyricism that earned her the Nobel Prize in Literature in 1993, the first Black woman to receive the award",
        facts=[
            "Toni Morrison was born Chloe Ardelia Wofford in Lorain, Ohio, in 1931",
            "She worked for years as an editor at Random House, where she championed Black authors before her own novels achieved wide recognition",
            "Her 1987 novel Beloved, based loosely on the true story of an enslaved woman, won the Pulitzer Prize for Fiction in 1988",
            "She won the Nobel Prize in Literature in 1993, becoming the first Black woman to receive the honor",
            "Her other major novels include Song of Solomon (1977) and The Bluest Eye (1970), her debut novel",
            "She taught at Princeton University for many years as a professor of humanities",
            "President Barack Obama awarded her the Presidential Medal of Freedom in 2012",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="george_orwell", name="George Orwell", years="1903-1950", nationality="English",
        field="novelist and essayist", wiki_title="George Orwell",
        significance="his novels Animal Farm and Nineteen Eighty-Four became enduring warnings about totalitarianism, and terms he coined, such as 'Big Brother' and 'doublethink', entered everyday English usage",
        facts=[
            "George Orwell was the pen name of Eric Arthur Blair, born in Motihari, in British India, in 1903",
            "He served with the Indian Imperial Police in Burma in the 1920s, an experience that shaped his critical views on colonialism",
            "He fought with a socialist militia during the Spanish Civil War in the 1930s and was shot through the throat, nearly dying",
            "His 1945 novella Animal Farm satirized the Russian Revolution and its betrayal through the story of farm animals overthrowing their human owner",
            "His 1949 novel Nineteen Eighty-Four depicted a dystopian totalitarian surveillance state, introducing terms like 'Big Brother', 'thoughtcrime', and 'doublethink'",
            "The adjective 'Orwellian', describing oppressive or deceptive political practices, is derived from his name and remains in wide use today",
            "He died of tuberculosis in London in 1950, shortly after Nineteen Eighty-Four's publication had made him internationally famous",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="homer", name="Homer", years="c. 8th century BCE", nationality="Ancient Greek",
        field="epic poet", wiki_title="Homer",
        significance="the epic poems traditionally attributed to him, the Iliad and the Odyssey, are among the oldest surviving works of Western literature and profoundly shaped ancient Greek culture and later Western storytelling",
        facts=[
            "Very little is known for certain about Homer's life, and historians continue to debate when and whether a single person composed the poems attributed to him",
            "The Iliad tells the story of a period during the Trojan War, focusing on the anger of the Greek warrior Achilles",
            "The Odyssey follows the hero Odysseus's ten-year journey home after the fall of Troy",
            "Both poems were likely composed and transmitted orally for generations before being written down, drawing on a long tradition of oral epic poetry",
            "Ancient Greeks regarded Homer's works as foundational cultural and educational texts, comparable to how some cultures treat religious scripture",
            "The poems are written in a distinctive meter called dactylic hexameter, a form later Greek and Roman epic poets continued to use",
            "Scholars refer to the long-unresolved question of Homer's identity and authorship as the 'Homeric Question'",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="jk_rowling", name="J.K. Rowling", years="1965-present", nationality="British",
        field="novelist", wiki_title="J. K. Rowling",
        significance="her Harry Potter series became one of the best-selling book series in history, selling more than 600 million copies worldwide and reviving global interest in children's and young-adult fantasy fiction",
        facts=[
            "J.K. Rowling was born Joanne Rowling in Yate, England, in 1965",
            "She conceived the idea for Harry Potter during a delayed train journey between Manchester and London in 1990",
            "She wrote much of the first Harry Potter novel while a single parent living on public assistance in Edinburgh, Scotland",
            "Harry Potter and the Philosopher's Stone was rejected by twelve publishing houses before being accepted by Bloomsbury in 1997",
            "The seven-book Harry Potter series has sold more than 600 million copies and been translated into over 80 languages",
            "The book series was adapted into an eight-film series by Warner Bros. that became one of the highest-grossing film franchises of all time",
            "She has also written crime fiction under the pen name Robert Galbraith",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="chinua_achebe", name="Chinua Achebe", years="1930-2013", nationality="Nigerian",
        field="novelist", wiki_title="Chinua Achebe",
        significance="his 1958 novel Things Fall Apart is one of the most widely read works of African literature, credited with challenging colonial narratives about African societies and helping launch the modern African literary tradition in English",
        facts=[
            "Chinua Achebe was born in Ogidi, Nigeria, in 1930, when the country was still under British colonial rule",
            "His debut novel, Things Fall Apart, published in 1958, tells the story of an Igbo village confronting the arrival of British colonialism and Christian missionaries",
            "The novel has sold more than 20 million copies worldwide and been translated into over 50 languages",
            "He wrote it partly in response to European novels that portrayed Africa and Africans in what he considered distorted, dehumanizing terms",
            "He co-founded the influential Heinemann African Writers Series in the 1960s, which helped bring many African authors to a global audience",
            "He served as a professor at several universities, including Bard College and Brown University in the United States",
            "He was seriously injured in a car accident in Nigeria in 1990, which left him partially paralyzed and using a wheelchair for the rest of his life",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="pablo_neruda", name="Pablo Neruda", years="1904-1973", nationality="Chilean",
        field="poet and diplomat", wiki_title="Pablo Neruda",
        significance="one of the most influential Spanish-language poets of the 20th century, he won the Nobel Prize in Literature in 1971 for poetry that Colombian novelist Gabriel Garcia Marquez called 'the greatest poet of the 20th century in any language'",
        facts=[
            "Pablo Neruda was the pen name of Ricardo Eliecer Neftali Reyes Basoalto, born in Parral, Chile, in 1904",
            "He published his celebrated collection Twenty Love Poems and a Song of Despair in 1924, at just 20 years old, which became one of the best-selling poetry books in the Spanish language",
            "He served as a Chilean diplomat in several countries, including as consul in Spain during the outbreak of the Spanish Civil War in the 1930s",
            "His experience of the Spanish Civil War, including the death of his friend the poet Federico Garcia Lorca, radicalized his political views",
            "He was elected as a Chilean senator in 1945 and later joined the Communist Party, before being forced into hiding and exile in 1948 due to his political activities",
            "He won the Nobel Prize in Literature in 1971",
            "He died in Santiago, Chile, in 1973, just days after the military coup that overthrew his friend, President Salvador Allende",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="emily_dickinson", name="Emily Dickinson", years="1830-1886", nationality="American",
        field="poet", wiki_title="Emily Dickinson",
        significance="though almost entirely unpublished during her lifetime, her nearly 1,800 poems, discovered and published after her death, established her as one of the most original and influential poets in American literature",
        facts=[
            "Emily Dickinson was born in Amherst, Massachusetts, in 1830, and spent most of her life in her family's home there",
            "She became increasingly reclusive as she aged, and by her later years rarely left her house or interacted with visitors directly",
            "She wrote nearly 1,800 poems during her lifetime, but fewer than a dozen were published, and mostly anonymously and without her full approval",
            "Her poems are known for their unconventional use of dashes, capitalization, and slant rhyme, which departed from the poetic conventions of her time",
            "After her death in 1886, her sister Lavinia discovered the large collection of poems, mostly stored in small hand-sewn booklets",
            "The first collection of her poetry was published in 1890, four years after her death, and was heavily edited to conform to conventional grammar and punctuation of the time",
            "Later scholarly editions have restored her original unconventional punctuation, and she is now regarded as one of the most significant American poets",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="victor_hugo", name="Victor Hugo", years="1802-1885", nationality="French",
        field="novelist and poet", wiki_title="Victor Hugo",
        significance="his novels Les Miserables and The Hunchback of Notre-Dame combined social commentary with sweeping narrative, and he remains one of the most celebrated figures in French literature and public life",
        facts=[
            "Victor Hugo was born in Besancon, France, in 1802, and began publishing poetry as a teenager",
            "His 1831 novel The Hunchback of Notre-Dame drew public attention to the deteriorating condition of the Notre-Dame Cathedral, helping spur its restoration",
            "His 1862 novel Les Miserables follows the ex-convict Jean Valjean through decades of post-revolutionary France, and remains one of the longest and most translated novels in the world",
            "He was also active in French politics, serving in the National Assembly and later the Senate",
            "He was exiled from France for nearly 20 years, from 1851 to 1870, for his opposition to Napoleon III, spending much of that time on the Channel Islands",
            "Les Miserables was adapted into a hugely successful stage musical in 1980, which has since been performed in more than 40 countries",
            "His funeral in 1885 drew an estimated two million people to the streets of Paris, one of the largest public funerals in French history",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="agatha_christie", name="Agatha Christie", years="1890-1976", nationality="English",
        field="novelist", wiki_title="Agatha Christie",
        significance="the best-selling novelist of all time according to Guinness World Records, her detective novels featuring Hercule Poirot and Miss Marple helped define the modern murder mystery genre",
        facts=[
            "Agatha Christie was born in Torquay, England, in 1890, and was largely educated at home",
            "She began writing detective fiction during World War I, while working in a hospital dispensary, which gave her detailed knowledge of poisons she later used extensively in her plots",
            "Her 1920 novel The Mysterious Affair at Styles introduced her most famous detective character, the meticulous Belgian investigator Hercule Poirot",
            "She wrote 66 detective novels over her career, along with numerous short stories and plays, including her play The Mousetrap, which holds the record for the longest continuously running play in history",
            "Her 1926 disappearance for 11 days, which was never fully explained by her and remains debated by biographers, became a major media sensation in Britain at the time",
            "Her estimated book sales exceed two billion copies, placing her, according to Guinness World Records, as the best-selling novelist in history",
            "She died in 1976, and her novels, including Murder on the Orient Express and And Then There Were None, remain in print and continue to be adapted into films and television",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="franz_kafka", name="Franz Kafka", years="1883-1924", nationality="Bohemian (Austro-Hungarian, Czech)",
        field="novelist", wiki_title="Franz Kafka",
        significance="his surreal, unsettling depictions of bureaucratic alienation, especially in The Trial and The Metamorphosis, gave rise to the term 'Kafkaesque' and profoundly influenced 20th-century literature",
        facts=[
            "Franz Kafka was born in Prague, then part of the Austro-Hungarian Empire, in 1883, into a German-speaking Jewish family",
            "He worked for most of his life at an insurance institute, writing fiction largely in his limited free time",
            "His novella The Metamorphosis, published in 1915, tells the story of a man who wakes up transformed into an enormous insect, exploring themes of alienation and family obligation",
            "His novel The Trial, in which a man is arrested and prosecuted by an inaccessible, incomprehensible authority without ever learning the charges against him, was published posthumously in 1925",
            "He published relatively little during his own lifetime and asked his close friend Max Brod to destroy his unpublished manuscripts after his death, an instruction Brod chose not to follow",
            "The term 'Kafkaesque' entered common usage to describe surreal, oppressive bureaucratic or illogical situations reminiscent of his fiction",
            "He died of tuberculosis in 1924 at age 40, and his posthumously published novels later established him as one of the most influential writers of the 20th century",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="langston_hughes", name="Langston Hughes", years="1901-1967", nationality="American",
        field="poet and writer", wiki_title="Langston Hughes",
        significance="a leading figure of the Harlem Renaissance, his poetry captured the rhythms of jazz and blues while addressing racial identity and injustice, and remains among the most widely taught American poetry",
        facts=[
            "Langston Hughes was born in Joplin, Missouri, in 1901, and spent much of his childhood being raised primarily by his grandmother",
            "He became a central figure of the Harlem Renaissance, the flourishing of Black literary, artistic, and musical culture centered in Harlem, New York, during the 1920s",
            "His poetry frequently incorporated the rhythms and structures of jazz and blues music, a distinctive stylistic innovation in American poetry",
            "His 1926 essay 'The Negro Artist and the Racial Mountain' argued forcefully that Black artists should embrace their own cultural heritage rather than imitate white artistic standards",
            "His poem 'Harlem', which begins 'What happens to a dream deferred?', became one of the most widely quoted and taught poems in American literature, and later inspired the title of the play A Raisin in the Sun",
            "He wrote across many forms beyond poetry, including novels, plays, and newspaper columns, notably creating the recurring comic character Jesse B. Semple",
            "He died in New York City in 1967, and remains one of the most celebrated poets associated with the Harlem Renaissance",
        ], related_subjects=["World Literature", "English"],
    ),
    dict(
        id="dante_alighieri", name="Dante Alighieri", years="1265-1321", nationality="Italian (Florentine)",
        field="poet", wiki_title="Dante Alighieri",
        significance="his epic poem the Divine Comedy, describing an imagined journey through Hell, Purgatory, and Heaven, is considered one of the greatest works of world literature and helped establish the Tuscan dialect as the basis of modern standard Italian",
        facts=[
            "Dante Alighieri was born in Florence, in what is now Italy, in 1265",
            "He became involved in the bitter political conflicts between rival factions in Florence, and was exiled from the city in 1302, never to return",
            "He wrote the Divine Comedy, an epic poem in three parts (Inferno, Purgatorio, and Paradiso), largely during his years of exile",
            "The poem describes an imagined journey through Hell, Purgatory, and Heaven, guided first by the Roman poet Virgil and later by his idealized love, Beatrice",
            "He chose to write the Divine Comedy in the Tuscan Italian vernacular rather than Latin, the standard literary language of the time, a decision that significantly influenced the development of standard Italian",
            "The poem's detailed and imaginative depiction of Hell, including its structured circles of punishment, has profoundly influenced Western art, literature, and popular conceptions of the afterlife for centuries",
            "He died in Ravenna, Italy, in 1321, still in exile from Florence, which formally rescinded his sentence only in 2008, nearly 700 years later",
        ], related_subjects=["World Literature"],
    ),
    dict(
        id="miguel_de_cervantes", name="Miguel de Cervantes", years="1547-1616", nationality="Spanish",
        field="novelist", wiki_title="Miguel de Cervantes",
        significance="his novel Don Quixote, published in two parts in 1605 and 1615, is widely regarded as the first modern novel and remains one of the most translated and influential works in world literature",
        facts=[
            "Miguel de Cervantes was born near Madrid, Spain, in 1547",
            "He served as a soldier and was wounded at the 1571 Battle of Lepanto, permanently losing the use of his left hand",
            "He was captured by Barbary pirates in 1575 and held as a slave in Algiers for five years before being ransomed and returned to Spain",
            "He published the first part of Don Quixote in 1605, telling the story of a minor nobleman who, inspired by chivalric romance novels, sets out on absurd adventures believing himself a knight-errant",
            "The novel is widely regarded by literary scholars as the first modern novel, for its innovative blending of realism, parody, and complex characterization",
            "He published the second part of Don Quixote in 1615, a year before his death, partly in response to an unauthorized sequel written by another author",
            "He died in Madrid in 1616, reportedly within days of William Shakespeare's death, and Don Quixote remains, according to many surveys, among the most translated works of fiction in world history",
        ], related_subjects=["World Literature"],
    ),
]


def main() -> None:
    upsert_section(
        "literature_writers",
        "Literature & Writers",
        "📚",
        "Novelists, poets, and playwrights whose words shaped how we tell stories and understand the human experience.",
        PEOPLE,
    )


if __name__ == "__main__":
    main()
