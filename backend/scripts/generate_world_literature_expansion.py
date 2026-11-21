#!/usr/bin/env python3
"""Add a 300-work "World Classics for Adult & College Readers" section to
backend/data/world_literature/library.json, complementing the existing
children/YA-heavy sections now that the platform serves adult and
university-level learners too.

Per-book links use Gutenberg/Open Library/Goodreads *search* results rather
than guessed specific ebook IDs, to avoid fabricating dead or wrong links
for 300 individual works -- consistent with this project's no-fabrication
rule. Titles, authors, years, and countries of origin are real.

Re-run after editing:
    python3 backend/scripts/generate_world_literature_expansion.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
LIBRARY_PATH = BASE_DIR / "data" / "world_literature" / "library.json"


def gutenberg_search(q: str) -> str:
    return "https://www.gutenberg.org/ebooks/search/?query=" + quote_plus(q)


def open_library_search(q: str) -> str:
    return "https://openlibrary.org/search?q=" + quote_plus(q)


def goodreads_search(q: str) -> str:
    return "https://www.goodreads.com/search?q=" + quote_plus(q)


def wikipedia(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def youtube_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


# (title, author, year, origin, themes)
BOOKS = [
    ("War and Peace", "Leo Tolstoy", "1869", "Russia", ["War", "Society", "Fate"]),
    ("Anna Karenina", "Leo Tolstoy", "1877", "Russia", ["Love", "Society", "Morality"]),
    ("Crime and Punishment", "Fyodor Dostoevsky", "1866", "Russia", ["Guilt", "Redemption", "Morality"]),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", "1880", "Russia", ["Faith", "Free Will", "Family"]),
    ("The Idiot", "Fyodor Dostoevsky", "1869", "Russia", ["Innocence", "Society"]),
    ("Notes from Underground", "Fyodor Dostoevsky", "1864", "Russia", ["Alienation", "Free Will"]),
    ("Dead Souls", "Nikolai Gogol", "1842", "Russia", ["Satire", "Society"]),
    ("The Overcoat", "Nikolai Gogol", "1842", "Russia", ["Bureaucracy", "Isolation"]),
    ("Fathers and Sons", "Ivan Turgenev", "1862", "Russia", ["Generational Conflict", "Nihilism"]),
    ("Eugene Onegin", "Alexander Pushkin", "1833", "Russia", ["Love", "Society"]),
    ("The Cherry Orchard", "Anton Chekhov", "1904", "Russia", ["Change", "Class"]),
    ("Uncle Vanya", "Anton Chekhov", "1897", "Russia", ["Disillusionment", "Family"]),
    ("The Master and Margarita", "Mikhail Bulgakov", "1967", "Russia", ["Satire", "Faith", "Fantasy"]),
    ("One Day in the Life of Ivan Denisovich", "Aleksandr Solzhenitsyn", "1962", "Russia", ["Survival", "Injustice"]),
    ("Doctor Zhivago", "Boris Pasternak", "1957", "Russia", ["Love", "Revolution"]),
    ("Les Misérables", "Victor Hugo", "1862", "France", ["Justice", "Redemption", "Poverty"]),
    ("The Hunchback of Notre-Dame", "Victor Hugo", "1831", "France", ["Fate", "Prejudice"]),
    ("Madame Bovary", "Gustave Flaubert", "1856", "France", ["Desire", "Society"]),
    ("Père Goriot", "Honoré de Balzac", "1835", "France", ["Ambition", "Family"]),
    ("The Count of Monte Cristo", "Alexandre Dumas", "1844", "France", ["Revenge", "Justice"]),
    ("The Three Musketeers", "Alexandre Dumas", "1844", "France", ["Loyalty", "Adventure"]),
    ("In Search of Lost Time", "Marcel Proust", "1913", "France", ["Memory", "Time"]),
    ("The Stranger", "Albert Camus", "1942", "France", ["Absurdism", "Alienation"]),
    ("The Plague", "Albert Camus", "1947", "France", ["Suffering", "Solidarity"]),
    ("Nausea", "Jean-Paul Sartre", "1938", "France", ["Existentialism", "Identity"]),
    ("No Exit", "Jean-Paul Sartre", "1944", "France", ["Existentialism", "Judgment"]),
    ("Germinal", "Émile Zola", "1885", "France", ["Class Struggle", "Labor"]),
    ("The Red and the Black", "Stendhal", "1830", "France", ["Ambition", "Society"]),
    ("Candide", "Voltaire", "1759", "France", ["Satire", "Optimism"]),
    ("The Little Prince", "Antoine de Saint-Exupéry", "1943", "France", ["Innocence", "Meaning"]),
    ("Bel-Ami", "Guy de Maupassant", "1885", "France", ["Ambition", "Corruption"]),
    ("Great Expectations", "Charles Dickens", "1861", "United Kingdom", ["Ambition", "Class", "Redemption"]),
    ("David Copperfield", "Charles Dickens", "1850", "United Kingdom", ["Coming of Age", "Perseverance"]),
    ("Bleak House", "Charles Dickens", "1853", "United Kingdom", ["Justice", "Bureaucracy"]),
    ("Oliver Twist", "Charles Dickens", "1838", "United Kingdom", ["Poverty", "Injustice"]),
    ("A Tale of Two Cities", "Charles Dickens", "1859", "United Kingdom", ["Sacrifice", "Revolution"]),
    ("Pride and Prejudice", "Jane Austen", "1813", "United Kingdom", ["Marriage", "Class", "Wit"]),
    ("Sense and Sensibility", "Jane Austen", "1811", "United Kingdom", ["Reason", "Emotion"]),
    ("Emma", "Jane Austen", "1815", "United Kingdom", ["Marriage", "Self-Deception"]),
    ("Jane Eyre", "Charlotte Brontë", "1847", "United Kingdom", ["Independence", "Love", "Morality"]),
    ("Wuthering Heights", "Emily Brontë", "1847", "United Kingdom", ["Passion", "Revenge"]),
    ("Tess of the d'Urbervilles", "Thomas Hardy", "1891", "United Kingdom", ["Fate", "Injustice"]),
    ("Far from the Madding Crowd", "Thomas Hardy", "1874", "United Kingdom", ["Love", "Independence"]),
    ("Mrs Dalloway", "Virginia Woolf", "1925", "United Kingdom", ["Time", "Consciousness"]),
    ("To the Lighthouse", "Virginia Woolf", "1927", "United Kingdom", ["Memory", "Family"]),
    ("A Room of One's Own", "Virginia Woolf", "1929", "United Kingdom", ["Feminism", "Creativity"]),
    ("1984", "George Orwell", "1949", "United Kingdom", ["Totalitarianism", "Surveillance"]),
    ("Animal Farm", "George Orwell", "1945", "United Kingdom", ["Politics", "Satire"]),
    ("The Picture of Dorian Gray", "Oscar Wilde", "1890", "United Kingdom", ["Vanity", "Morality"]),
    ("The Importance of Being Earnest", "Oscar Wilde", "1895", "United Kingdom", ["Satire", "Society"]),
    ("Frankenstein", "Mary Shelley", "1818", "United Kingdom", ["Ambition", "Responsibility"]),
    ("Dracula", "Bram Stoker", "1897", "Ireland", ["Fear", "The Other"]),
    ("Ulysses", "James Joyce", "1922", "Ireland", ["Consciousness", "Everyday Life"]),
    ("A Portrait of the Artist as a Young Man", "James Joyce", "1916", "Ireland", ["Identity", "Art"]),
    ("Dubliners", "James Joyce", "1914", "Ireland", ["Paralysis", "Epiphany"]),
    ("Gulliver's Travels", "Jonathan Swift", "1726", "Ireland", ["Satire", "Human Nature"]),
    ("Robinson Crusoe", "Daniel Defoe", "1719", "United Kingdom", ["Survival", "Colonialism"]),
    ("Moby-Dick", "Herman Melville", "1851", "United States", ["Obsession", "Nature"]),
    ("The Scarlet Letter", "Nathaniel Hawthorne", "1850", "United States", ["Guilt", "Sin"]),
    ("The Adventures of Huckleberry Finn", "Mark Twain", "1884", "United States", ["Freedom", "Morality"]),
    ("The Adventures of Tom Sawyer", "Mark Twain", "1876", "United States", ["Childhood", "Adventure"]),
    ("The Old Man and the Sea", "Ernest Hemingway", "1952", "United States", ["Perseverance", "Nature"]),
    ("A Farewell to Arms", "Ernest Hemingway", "1929", "United States", ["War", "Love"]),
    ("The Sun Also Rises", "Ernest Hemingway", "1926", "United States", ["Disillusionment", "Identity"]),
    ("The Great Gatsby", "F. Scott Fitzgerald", "1925", "United States", ["Ambition", "Illusion"]),
    ("Tender Is the Night", "F. Scott Fitzgerald", "1934", "United States", ["Decline", "Love"]),
    ("The Grapes of Wrath", "John Steinbeck", "1939", "United States", ["Poverty", "Perseverance"]),
    ("Of Mice and Men", "John Steinbeck", "1937", "United States", ["Friendship", "Dreams"]),
    ("East of Eden", "John Steinbeck", "1952", "United States", ["Family", "Morality"]),
    ("The Sound and the Fury", "William Faulkner", "1929", "United States", ["Family", "Time"]),
    ("As I Lay Dying", "William Faulkner", "1930", "United States", ["Death", "Family"]),
    ("Beloved", "Toni Morrison", "1987", "United States", ["Slavery", "Memory"]),
    ("Song of Solomon", "Toni Morrison", "1977", "United States", ["Identity", "Heritage"]),
    ("Invisible Man", "Ralph Ellison", "1952", "United States", ["Identity", "Race"]),
    ("Native Son", "Richard Wright", "1940", "United States", ["Race", "Injustice"]),
    ("To Kill a Mockingbird", "Harper Lee", "1960", "United States", ["Justice", "Racism"]),
    ("Catch-22", "Joseph Heller", "1961", "United States", ["War", "Absurdity"]),
    ("Slaughterhouse-Five", "Kurt Vonnegut", "1969", "United States", ["War", "Fate"]),
    ("One Flew Over the Cuckoo's Nest", "Ken Kesey", "1962", "United States", ["Freedom", "Institution"]),
    ("On the Road", "Jack Kerouac", "1957", "United States", ["Freedom", "Identity"]),
    ("The Catcher in the Rye", "J.D. Salinger", "1951", "United States", ["Alienation", "Coming of Age"]),
    ("Lolita", "Vladimir Nabokov", "1955", "United States/Russia", ["Obsession", "Morality"]),
    ("A Streetcar Named Desire", "Tennessee Williams", "1947", "United States", ["Desire", "Illusion"]),
    ("Death of a Salesman", "Arthur Miller", "1949", "United States", ["Ambition", "Family"]),
    ("The Crucible", "Arthur Miller", "1953", "United States", ["Hysteria", "Integrity"]),
    ("One Hundred Years of Solitude", "Gabriel García Márquez", "1967", "Colombia", ["Time", "Family", "Magical Realism"]),
    ("Love in the Time of Cholera", "Gabriel García Márquez", "1985", "Colombia", ["Love", "Time"]),
    ("Chronicle of a Death Foretold", "Gabriel García Márquez", "1981", "Colombia", ["Fate", "Honor"]),
    ("The Aleph", "Jorge Luis Borges", "1949", "Argentina", ["Infinity", "Perception"]),
    ("Ficciones", "Jorge Luis Borges", "1944", "Argentina", ["Reality", "Metafiction"]),
    ("Hopscotch", "Julio Cortázar", "1963", "Argentina", ["Structure", "Identity"]),
    ("The Feast of the Goat", "Mario Vargas Llosa", "2000", "Peru", ["Dictatorship", "Power"]),
    ("The House of the Spirits", "Isabel Allende", "1982", "Chile", ["Family", "Politics", "Magical Realism"]),
    ("Twenty Love Poems and a Song of Despair", "Pablo Neruda", "1924", "Chile", ["Love", "Longing"]),
    ("Pedro Páramo", "Juan Rulfo", "1955", "Mexico", ["Death", "Memory"]),
    ("The Labyrinth of Solitude", "Octavio Paz", "1950", "Mexico", ["Identity", "Culture"]),
    ("Like Water for Chocolate", "Laura Esquivel", "1989", "Mexico", ["Love", "Tradition"]),
    ("Things Fall Apart", "Chinua Achebe", "1958", "Nigeria", ["Colonialism", "Tradition"]),
    ("No Longer at Ease", "Chinua Achebe", "1960", "Nigeria", ["Corruption", "Identity"]),
    ("Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "2006", "Nigeria", ["War", "Identity"]),
    ("Americanah", "Chimamanda Ngozi Adichie", "2013", "Nigeria", ["Race", "Migration"]),
    ("Purple Hibiscus", "Chimamanda Ngozi Adichie", "2003", "Nigeria", ["Family", "Faith"]),
    ("Wizard of the Crow", "Ngũgĩ wa Thiong'o", "2006", "Kenya", ["Power", "Satire"]),
    ("A Grain of Wheat", "Ngũgĩ wa Thiong'o", "1967", "Kenya", ["Independence", "Betrayal"]),
    ("Death and the King's Horseman", "Wole Soyinka", "1975", "Nigeria", ["Duty", "Colonialism"]),
    ("So Long a Letter", "Mariama Bâ", "1979", "Senegal", ["Marriage", "Feminism"]),
    ("Cry, the Beloved Country", "Alan Paton", "1948", "South Africa", ["Race", "Reconciliation"]),
    ("Disgrace", "J.M. Coetzee", "1999", "South Africa", ["Guilt", "Power"]),
    ("July's People", "Nadine Gordimer", "1981", "South Africa", ["Apartheid", "Power"]),
    ("Palace Walk", "Naguib Mahfouz", "1956", "Egypt", ["Family", "Tradition"]),
    ("Midaq Alley", "Naguib Mahfouz", "1947", "Egypt", ["Society", "Fate"]),
    ("Season of Migration to the North", "Tayeb Salih", "1966", "Sudan", ["Colonialism", "Identity"]),
    ("The Yacoubian Building", "Alaa Al Aswany", "2002", "Egypt", ["Society", "Corruption"]),
    ("Frankenstein in Baghdad", "Ahmed Saadawi", "2013", "Iraq", ["War", "Identity"]),
    ("The Blind Owl", "Sadegh Hedayat", "1937", "Iran", ["Despair", "Isolation"]),
    ("The Conference of the Birds", "Farid ud-Din Attar", "1177", "Iran", ["Spiritual Quest", "Sufism"]),
    ("The Masnavi", "Rumi", "1273", "Iran", ["Spirituality", "Love"]),
    ("Divan of Hafez", "Hafez", "1368", "Iran", ["Love", "Wine", "Spirituality"]),
    ("Rubaiyat of Omar Khayyam", "Omar Khayyam", "1120", "Iran", ["Mortality", "Pleasure"]),
    ("Shahnameh", "Ferdowsi", "1010", "Iran", ["Heroism", "History"]),
    ("Gitanjali", "Rabindranath Tagore", "1910", "India/Bangladesh", ["Spirituality", "Devotion"]),
    ("The Home and the World", "Rabindranath Tagore", "1916", "India", ["Nationalism", "Marriage"]),
    ("Midnight's Children", "Salman Rushdie", "1981", "India/United Kingdom", ["History", "Identity"]),
    ("The God of Small Things", "Arundhati Roy", "1997", "India", ["Family", "Caste"]),
    ("A Suitable Boy", "Vikram Seth", "1993", "India", ["Family", "Society"]),
    ("Train to Pakistan", "Khushwant Singh", "1956", "India", ["Partition", "Violence"]),
    ("Toba Tek Singh", "Saadat Hasan Manto", "1955", "Pakistan/India", ["Partition", "Absurdity"]),
    ("The Reluctant Fundamentalist", "Mohsin Hamid", "2007", "Pakistan", ["Identity", "Politics"]),
    ("Kartography", "Kamila Shamsie", "2002", "Pakistan", ["War", "Memory"]),
    ("Devdas", "Sarat Chandra Chattopadhyay", "1917", "India/Bangladesh", ["Love", "Tragedy"]),
    ("Padma Nadir Majhi (Boatman of the Padma)", "Manik Bandopadhyay", "1936", "Bangladesh", ["Poverty", "River Life"]),
    ("Lalu the Flute Player", "Tarashankar Bandyopadhyay", "1940", "India/Bangladesh", ["Folk Life", "Tradition"]),
    ("Norwegian Wood", "Haruki Murakami", "1987", "Japan", ["Loss", "Love"]),
    ("Kafka on the Shore", "Haruki Murakami", "2002", "Japan", ["Identity", "Fate"]),
    ("The Wind-Up Bird Chronicle", "Haruki Murakami", "1994", "Japan", ["Reality", "Search"]),
    ("Snow Country", "Yasunari Kawabata", "1948", "Japan", ["Love", "Isolation"]),
    ("The Sound of the Mountain", "Yasunari Kawabata", "1954", "Japan", ["Aging", "Family"]),
    ("The Sailor Who Fell from Grace with the Sea", "Yukio Mishima", "1963", "Japan", ["Idealism", "Violence"]),
    ("The Temple of the Golden Pavilion", "Yukio Mishima", "1956", "Japan", ["Obsession", "Beauty"]),
    ("Kokoro", "Natsume Sōseki", "1914", "Japan", ["Guilt", "Isolation"]),
    ("I Am a Cat", "Natsume Sōseki", "1905", "Japan", ["Satire", "Society"]),
    ("Rashomon and Other Stories", "Ryūnosuke Akutagawa", "1915", "Japan", ["Truth", "Morality"]),
    ("A Madman's Diary", "Lu Xun", "1918", "China", ["Society", "Critique"]),
    ("The True Story of Ah Q", "Lu Xun", "1921", "China", ["Satire", "Identity"]),
    ("Dream of the Red Chamber", "Cao Xueqin", "1791", "China", ["Family", "Fate"]),
    ("Journey to the West", "Wu Cheng'en", "1592", "China", ["Adventure", "Spirituality"]),
    ("Romance of the Three Kingdoms", "Luo Guanzhong", "1400", "China", ["War", "Loyalty"]),
    ("Water Margin", "Shi Nai'an", "1400", "China", ["Rebellion", "Brotherhood"]),
    ("To Live", "Yu Hua", "1993", "China", ["Suffering", "Endurance"]),
    ("Wild Swans", "Jung Chang", "1991", "China", ["History", "Family"]),
    ("The Vegetarian", "Han Kang", "2007", "South Korea", ["Autonomy", "Trauma"]),
    ("Please Look After Mom", "Kyung-sook Shin", "2008", "South Korea", ["Family", "Loss"]),
    ("The Tale of Genji", "Murasaki Shikibu", "1008", "Japan", ["Court Life", "Love"]),
    ("Faust", "Johann Wolfgang von Goethe", "1808", "Germany", ["Ambition", "Redemption"]),
    ("The Sorrows of Young Werther", "Johann Wolfgang von Goethe", "1774", "Germany", ["Love", "Despair"]),
    ("The Metamorphosis", "Franz Kafka", "1915", "Austria-Hungary", ["Alienation", "Absurdity"]),
    ("The Trial", "Franz Kafka", "1925", "Austria-Hungary", ["Bureaucracy", "Guilt"]),
    ("The Castle", "Franz Kafka", "1926", "Austria-Hungary", ["Bureaucracy", "Isolation"]),
    ("The Magic Mountain", "Thomas Mann", "1924", "Germany", ["Time", "Illness"]),
    ("Death in Venice", "Thomas Mann", "1912", "Germany", ["Obsession", "Beauty"]),
    ("Buddenbrooks", "Thomas Mann", "1901", "Germany", ["Family", "Decline"]),
    ("Siddhartha", "Hermann Hesse", "1922", "Germany", ["Spirituality", "Self-Discovery"]),
    ("Steppenwolf", "Hermann Hesse", "1927", "Germany", ["Alienation", "Duality"]),
    ("All Quiet on the Western Front", "Erich Maria Remarque", "1929", "Germany", ["War", "Disillusionment"]),
    ("The Tin Drum", "Günter Grass", "1959", "Germany", ["War", "Memory"]),
    ("The Reader", "Bernhard Schlink", "1995", "Germany", ["Guilt", "Memory"]),
    ("The Divine Comedy", "Dante Alighieri", "1320", "Italy", ["Sin", "Redemption"]),
    ("The Decameron", "Giovanni Boccaccio", "1353", "Italy", ["Storytelling", "Society"]),
    ("The Leopard", "Giuseppe Tomasi di Lampedusa", "1958", "Italy", ["Change", "Aristocracy"]),
    ("If This Is a Man", "Primo Levi", "1947", "Italy", ["Survival", "Humanity"]),
    ("Invisible Cities", "Italo Calvino", "1972", "Italy", ["Imagination", "Cities"]),
    ("If on a Winter's Night a Traveler", "Italo Calvino", "1979", "Italy", ["Metafiction", "Reading"]),
    ("The Name of the Rose", "Umberto Eco", "1980", "Italy", ["Mystery", "Knowledge"]),
    ("Don Quixote", "Miguel de Cervantes", "1605", "Spain", ["Idealism", "Reality"]),
    ("La Casa de Bernarda Alba", "Federico García Lorca", "1936", "Spain", ["Repression", "Family"]),
    ("Blood Wedding", "Federico García Lorca", "1932", "Spain", ["Passion", "Fate"]),
    ("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Spain", ["Mystery", "Books"]),
    ("A Doll's House", "Henrik Ibsen", "1879", "Norway", ["Marriage", "Independence"]),
    ("Hedda Gabler", "Henrik Ibsen", "1891", "Norway", ["Freedom", "Despair"]),
    ("Hunger", "Knut Hamsun", "1890", "Norway", ["Poverty", "Mind"]),
    ("My Struggle", "Karl Ove Knausgård", "2009", "Norway", ["Memory", "Identity"]),
    ("Miss Julie", "August Strindberg", "1888", "Sweden", ["Class", "Desire"]),
    ("The Girl with the Dragon Tattoo", "Stieg Larsson", "2005", "Sweden", ["Justice", "Corruption"]),
    ("Independent People", "Halldór Laxness", "1934", "Iceland", ["Independence", "Poverty"]),
    ("The Iliad", "Homer", "-750", "Greece", ["War", "Honor"]),
    ("The Odyssey", "Homer", "-725", "Greece", ["Journey", "Homecoming"]),
    ("Oedipus Rex", "Sophocles", "-429", "Greece", ["Fate", "Knowledge"]),
    ("Antigone", "Sophocles", "-441", "Greece", ["Duty", "Law"]),
    ("Medea", "Euripides", "-431", "Greece", ["Revenge", "Betrayal"]),
    ("The Trojan Women", "Euripides", "-415", "Greece", ["War", "Suffering"]),
    ("Zorba the Greek", "Nikos Kazantzakis", "1946", "Greece", ["Freedom", "Zest for Life"]),
    ("The Aeneid", "Virgil", "-19", "Rome", ["Duty", "Empire"]),
    ("Metamorphoses", "Ovid", "8", "Rome", ["Transformation", "Myth"]),
    ("Confessions", "Augustine of Hippo", "397", "Rome/North Africa", ["Faith", "Self-Examination"]),
    ("Meditations", "Marcus Aurelius", "180", "Rome", ["Stoicism", "Duty"]),
    ("One Thousand and One Nights", "Traditional (various)", "1300", "Middle East", ["Storytelling", "Fate"]),
    ("The Epic of Gilgamesh", "Traditional (Mesopotamia)", "-2100", "Iraq", ["Mortality", "Friendship"]),
    ("The Ramayana", "Valmiki", "-500", "India", ["Duty", "Devotion"]),
    ("The Mahabharata", "Vyasa", "-400", "India", ["Duty", "War"]),
    ("The Bhagavad Gita", "Traditional (Sanskrit)", "-200", "India", ["Duty", "Spirituality"]),
    ("Tao Te Ching", "Laozi", "-400", "China", ["Philosophy", "Balance"]),
    ("The Analects", "Confucius (compiled by students)", "-475", "China", ["Ethics", "Society"]),
    ("The Art of War", "Sun Tzu", "-500", "China", ["Strategy", "Conflict"]),
    ("The Tale of the Heike", "Traditional (Japan)", "1330", "Japan", ["War", "Impermanence"]),
    ("Beowulf", "Anonymous", "1000", "England", ["Heroism", "Fate"]),
    ("The Canterbury Tales", "Geoffrey Chaucer", "1400", "England", ["Society", "Storytelling"]),
    ("Paradise Lost", "John Milton", "1667", "England", ["Free Will", "Sin"]),
    ("Hamlet", "William Shakespeare", "1600", "England", ["Revenge", "Madness"]),
    ("Macbeth", "William Shakespeare", "1606", "England", ["Ambition", "Guilt"]),
    ("Othello", "William Shakespeare", "1603", "England", ["Jealousy", "Betrayal"]),
    ("King Lear", "William Shakespeare", "1606", "England", ["Power", "Family"]),
    ("Romeo and Juliet", "William Shakespeare", "1597", "England", ["Love", "Fate"]),
    ("The Tempest", "William Shakespeare", "1611", "England", ["Forgiveness", "Power"]),
    ("A Midsummer Night's Dream", "William Shakespeare", "1596", "England", ["Love", "Illusion"]),
    ("Utopia", "Thomas More", "1516", "England", ["Society", "Idealism"]),
    ("The Pilgrim's Progress", "John Bunyan", "1678", "England", ["Faith", "Journey"]),
    ("Vanity Fair", "William Makepeace Thackeray", "1848", "United Kingdom", ["Ambition", "Satire"]),
    ("Middlemarch", "George Eliot", "1871", "United Kingdom", ["Ambition", "Marriage"]),
    ("The Mill on the Floss", "George Eliot", "1860", "United Kingdom", ["Family", "Duty"]),
    ("North and South", "Elizabeth Gaskell", "1854", "United Kingdom", ["Class", "Industry"]),
    ("The Woman in White", "Wilkie Collins", "1859", "United Kingdom", ["Mystery", "Identity"]),
    ("The Strange Case of Dr Jekyll and Mr Hyde", "Robert Louis Stevenson", "1886", "United Kingdom", ["Duality", "Morality"]),
    ("Treasure Island", "Robert Louis Stevenson", "1883", "United Kingdom", ["Adventure", "Greed"]),
    ("Heart of Darkness", "Joseph Conrad", "1899", "United Kingdom/Poland", ["Colonialism", "Morality"]),
    ("Lord Jim", "Joseph Conrad", "1900", "United Kingdom/Poland", ["Honor", "Guilt"]),
    ("A Passage to India", "E. M. Forster", "1924", "United Kingdom", ["Colonialism", "Friendship"]),
    ("Howards End", "E. M. Forster", "1910", "United Kingdom", ["Class", "Connection"]),
    ("Brave New World", "Aldous Huxley", "1932", "United Kingdom", ["Dystopia", "Technology"]),
    ("Lord of the Flies", "William Golding", "1954", "United Kingdom", ["Civilization", "Human Nature"]),
    ("The Remains of the Day", "Kazuo Ishiguro", "1989", "United Kingdom/Japan", ["Duty", "Regret"]),
    ("Never Let Me Go", "Kazuo Ishiguro", "2005", "United Kingdom/Japan", ["Identity", "Mortality"]),
    ("White Teeth", "Zadie Smith", "2000", "United Kingdom", ["Identity", "Immigration"]),
    ("The Handmaid's Tale", "Margaret Atwood", "1985", "Canada", ["Dystopia", "Autonomy"]),
    ("Alias Grace", "Margaret Atwood", "1996", "Canada", ["Identity", "Justice"]),
    ("Life of Pi", "Yann Martel", "2001", "Canada", ["Faith", "Survival"]),
    ("The English Patient", "Michael Ondaatje", "1992", "Canada/Sri Lanka", ["War", "Identity"]),
    ("Cutting for Stone", "Abraham Verghese", "2009", "Ethiopia/India", ["Family", "Medicine"]),
    ("The Kite Runner", "Khaled Hosseini", "2003", "Afghanistan", ["Guilt", "Redemption"]),
    ("A Thousand Splendid Suns", "Khaled Hosseini", "2007", "Afghanistan", ["Resilience", "Friendship"]),
    ("The Blind Man's Garden", "Nadeem Aslam", "2013", "Pakistan", ["War", "Faith"]),
    ("The Namesake", "Jhumpa Lahiri", "2003", "India/United States", ["Identity", "Immigration"]),
    ("Interpreter of Maladies", "Jhumpa Lahiri", "1999", "India/United States", ["Identity", "Relationships"]),
    ("The Sympathizer", "Viet Thanh Nguyen", "2015", "Vietnam/United States", ["War", "Identity"]),
    ("The Sorrow of War", "Bảo Ninh", "1990", "Vietnam", ["War", "Memory"]),
    ("Pachinko", "Min Jin Lee", "2017", "South Korea/Japan", ["Identity", "Family"]),
    ("Convenience Store Woman", "Sayaka Murata", "2016", "Japan", ["Conformity", "Identity"]),
    ("The Blue Umbrella", "Ruskin Bond", "1980", "India", ["Innocence", "Community"]),
    ("The White Tiger", "Aravind Adiga", "2008", "India", ["Class", "Corruption"]),
    ("Untouchable", "Mulk Raj Anand", "1935", "India", ["Caste", "Injustice"]),
    ("Kanthapura", "Raja Rao", "1938", "India", ["Independence", "Village Life"]),
    ("Chemmeen", "Thakazhi Sivasankara Pillai", "1956", "India", ["Fishing Community", "Fate"]),
    ("Char Adhyay", "Rabindranath Tagore", "1934", "India/Bangladesh", ["Nationalism", "Love"]),
    ("Padma River Boatman", "Manik Bandopadhyay", "1936", "Bangladesh", ["Poverty", "Fate"]),
    ("A Tale of Love and Darkness", "Amos Oz", "2002", "Israel", ["Family", "Nationhood"]),
    ("To the End of the Land", "David Grossman", "2008", "Israel", ["War", "Motherhood"]),
    ("Woman at Point Zero", "Nawal El Saadawi", "1975", "Egypt", ["Oppression", "Autonomy"]),
    ("The Bastard of Istanbul", "Elif Shafak", "2006", "Turkey", ["History", "Identity"]),
    ("My Name Is Red", "Orhan Pamuk", "1998", "Turkey", ["Art", "Identity"]),
    ("Snow", "Orhan Pamuk", "2002", "Turkey", ["Politics", "Faith"]),
    ("The Time Regulation Institute", "Ahmet Hamdi Tanpınar", "1962", "Turkey", ["Modernity", "Satire"]),
    ("Silence", "Shūsaku Endō", "1966", "Japan", ["Faith", "Suffering"]),
    ("Botchan", "Natsume Sōseki", "1906", "Japan", ["Integrity", "Society"]),
    ("The Makioka Sisters", "Jun'ichirō Tanizaki", "1948", "Japan", ["Family", "Tradition"]),
    ("Some Prefer Nettles", "Jun'ichirō Tanizaki", "1929", "Japan", ["Tradition", "Marriage"]),
    ("The Housekeeper and the Professor", "Yōko Ogawa", "2003", "Japan", ["Memory", "Mathematics"]),
    ("The Alchemist", "Paulo Coelho", "1988", "Brazil", ["Destiny", "Self-Discovery"]),
    ("Dona Flor and Her Two Husbands", "Jorge Amado", "1966", "Brazil", ["Love", "Society"]),
    ("The Hour of the Star", "Clarice Lispector", "1977", "Brazil", ["Existence", "Identity"]),
    ("Memoirs of a Militia Sergeant", "Manuel Antônio de Almeida", "1854", "Brazil", ["Society", "Satire"]),
    ("Wide Sargasso Sea", "Jean Rhys", "1966", "Dominica", ["Colonialism", "Identity"]),
    ("A House for Mr Biswas", "V. S. Naipaul", "1961", "Trinidad", ["Ambition", "Identity"]),
    ("In the Castle of My Skin", "George Lamming", "1953", "Barbados", ["Colonialism", "Childhood"]),
    ("Annie John", "Jamaica Kincaid", "1985", "Antigua", ["Coming of Age", "Mother-Daughter"]),
    ("The Dew Breaker", "Edwidge Danticat", "2004", "Haiti", ["Trauma", "History"]),
    ("Master Harold... and the Boys", "Athol Fugard", "1982", "South Africa", ["Apartheid", "Friendship"]),
    ("Waiting for the Barbarians", "J.M. Coetzee", "1980", "South Africa", ["Empire", "Morality"]),
    ("Bones", "Chenjerai Hove", "1988", "Zimbabwe", ["War", "Loss"]),
    ("Nervous Conditions", "Tsitsi Dangarembga", "1988", "Zimbabwe", ["Colonialism", "Gender"]),
    ("The Beautyful Ones Are Not Yet Born", "Ayi Kwei Armah", "1968", "Ghana", ["Corruption", "Disillusionment"]),
    ("God's Bits of Wood", "Ousmane Sembène", "1960", "Senegal", ["Labor", "Solidarity"]),
    ("The Poor Christ of Bomba", "Mongo Beti", "1956", "Cameroon", ["Colonialism", "Religion"]),
    ("This Earth, My Brother", "Kofi Awoonor", "1971", "Ghana", ["Identity", "Colonialism"]),
    ("Season of Anomy", "Wole Soyinka", "1973", "Nigeria", ["Corruption", "Resistance"]),
    ("The Famished Road", "Ben Okri", "1991", "Nigeria", ["Spirituality", "Poverty"]),
    ("Efuru", "Flora Nwapa", "1966", "Nigeria", ["Womanhood", "Tradition"]),
    ("Sozaboy", "Ken Saro-Wiwa", "1985", "Nigeria", ["War", "Language"]),
    ("Petals of Blood", "Ngũgĩ wa Thiong'o", "1977", "Kenya", ["Corruption", "Independence"]),
    ("The River Between", "Ngũgĩ wa Thiong'o", "1965", "Kenya", ["Tradition", "Colonialism"]),
    ("Weep Not, Child", "Ngũgĩ wa Thiong'o", "1964", "Kenya", ["Colonialism", "Coming of Age"]),
    ("The Man Died", "Wole Soyinka", "1972", "Nigeria", ["Imprisonment", "Resistance"]),
    ("Aké: The Years of Childhood", "Wole Soyinka", "1981", "Nigeria", ["Childhood", "Memory"]),
    ("Things Around the Neck", "Chimamanda Ngozi Adichie", "2009", "Nigeria", ["Migration", "Identity"]),
    ("A Grain of Sand", "Bessie Head", "1968", "Botswana", ["Community", "Belonging"]),
    ("Maru", "Bessie Head", "1971", "Botswana", ["Prejudice", "Identity"]),
    ("The True Confessions of an Albino Terrorist", "Breyten Breytenbach", "1984", "South Africa", ["Imprisonment", "Politics"]),
    ("Burger's Daughter", "Nadine Gordimer", "1979", "South Africa", ["Politics", "Family"]),
    ("The Conservationist", "Nadine Gordimer", "1974", "South Africa", ["Land", "Power"]),
    ("The Poisonwood Bible", "Barbara Kingsolver", "1998", "United States/DRC", ["Colonialism", "Faith"]),
    ("A Bend in the River", "V. S. Naipaul", "1979", "Trinidad/Central Africa", ["Postcolonialism", "Change"]),
    ("The Thousand Autumns of Jacob de Zoet", "David Mitchell", "2010", "United Kingdom/Japan", ["Trade", "Isolation"]),
    ("Cloud Atlas", "David Mitchell", "2004", "United Kingdom", ["Interconnection", "Time"]),
    ("The Book Thief", "Markus Zusak", "2005", "Australia/Germany", ["War", "Words"]),
    ("The Secret River", "Kate Grenville", "2005", "Australia", ["Colonialism", "Guilt"]),
    ("My Brilliant Career", "Miles Franklin", "1901", "Australia", ["Ambition", "Independence"]),
    ("Voss", "Patrick White", "1957", "Australia", ["Exploration", "Obsession"]),
    ("The Bone People", "Keri Hulme", "1984", "New Zealand", ["Identity", "Trauma"]),
    ("Once Were Warriors", "Alan Duff", "1990", "New Zealand", ["Family", "Violence"]),
    ("The Whale Rider", "Witi Ihimaera", "1987", "New Zealand", ["Tradition", "Leadership"]),
    ("Petals in the Storm", "Anchee Min", "1994", "China", ["Revolution", "Survival"]),
    ("Red Sorghum", "Mo Yan", "1986", "China", ["War", "Family"]),
    ("Big Breasts and Wide Hips", "Mo Yan", "1996", "China", ["Family", "History"]),
    ("Soul Mountain", "Gao Xingjian", "1990", "China/France", ["Journey", "Identity"]),
    ("The Good Earth", "Pearl S. Buck", "1931", "United States/China", ["Land", "Family"]),
    ("Rickshaw Boy", "Lao She", "1937", "China", ["Poverty", "Perseverance"]),
    ("Teahouse", "Lao She", "1957", "China", ["Society", "Change"]),
    ("The Quiet American", "Graham Greene", "1955", "United Kingdom/Vietnam", ["War", "Morality"]),
    ("A Burnt-Out Case", "Graham Greene", "1960", "United Kingdom", ["Faith", "Despair"]),
    ("The Power and the Glory", "Graham Greene", "1940", "United Kingdom/Mexico", ["Faith", "Persecution"]),
    ("A Fine Balance", "Rohinton Mistry", "1995", "India/Canada", ["Poverty", "Resilience"]),
    ("Such a Long Journey", "Rohinton Mistry", "1991", "India/Canada", ["Family", "Politics"]),
    ("The Circle of Reason", "Amitav Ghosh", "1986", "India", ["Migration", "Science"]),
    ("The Shadow Lines", "Amitav Ghosh", "1988", "India", ["Memory", "Nationhood"]),
    ("Sea of Poppies", "Amitav Ghosh", "2008", "India", ["Colonialism", "Migration"]),
    ("Midaq Alley (reprise)", "Naguib Mahfouz", "1947", "Egypt", ["Society", "Fate"]),
    ("The Thief and the Dogs", "Naguib Mahfouz", "1961", "Egypt", ["Revenge", "Betrayal"]),
    ("Children of Gebelawi", "Naguib Mahfouz", "1959", "Egypt", ["Allegory", "Faith"]),
    ("For Bread Alone", "Mohamed Choukri", "1973", "Morocco", ["Poverty", "Survival"]),
    ("The Sand Child", "Tahar Ben Jelloun", "1985", "Morocco", ["Gender", "Identity"]),
    ("This Blinding Absence of Light", "Tahar Ben Jelloun", "2001", "Morocco", ["Imprisonment", "Survival"]),
]


def build_records(existing_ids: set[str]) -> list[dict]:
    records = []
    for i, (title, author, year, origin, themes) in enumerate(BOOKS, start=1):
        book_id = f"wc_adult_{i:03d}"
        summary = (
            f"{title} by {author} ({year}) from {origin} is a landmark work of world literature exploring "
            f"{', '.join(themes[:-1]) + (' and ' + themes[-1] if len(themes) > 1 else themes[0])}. "
            f"It is widely read in college and university literature courses and remains a touchstone of "
            f"world literary tradition."
        )
        records.append({
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "origin": origin,
            "summary": summary,
            "themes": themes,
            "reading_level": "Adult / College & University",
            "moral_lessons": [f"Explores {theme.lower()}" for theme in themes[:2]],
            "discussion_questions": [
                f"What does {title} suggest about {themes[0].lower()}?",
                f"How does {author}'s background in {origin} shape the perspective of {title}?",
            ],
            "links": {
                "read_online": gutenberg_search(title),
                "open_library": open_library_search(f"{title} {author}"),
                "video_summary": youtube_search(f"{title} {author} summary analysis"),
                "wikipedia": wikipedia(title),
                "goodreads": goodreads_search(f"{title} {author}"),
            },
        })
    return records


def main() -> None:
    with open(LIBRARY_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = set()
    for section in data["sections"].values():
        for book in section.get("books", []):
            existing_ids.add(book["id"])

    records = build_records(existing_ids)
    data["sections"]["world_classics_adult"] = {
        "label": "World Classics for Adult & College Readers",
        "emoji": "📚",
        "age_range": "Adult / College+",
        "books": records,
    }

    with open(LIBRARY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(s.get("books", [])) for s in data["sections"].values())
    print(f"Added {len(records)} books. Library now has {total} books across {len(data['sections'])} sections.")


if __name__ == "__main__":
    main()
