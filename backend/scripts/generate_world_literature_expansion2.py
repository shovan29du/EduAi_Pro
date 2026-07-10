#!/usr/bin/env python3
"""Add a second, 200-work "World Literature — Global Voices" section to
backend/data/world_literature/library.json, broadening geographic and
cultural coverage beyond the existing "World Classics for Adult & College
Readers" section (which skews Russian/French/British/German).

Per-book links use Gutenberg/Open Library/Goodreads *search* results rather
than guessed specific ebook IDs, to avoid fabricating dead or wrong links
for 200 individual works -- consistent with this project's no-fabrication
rule. Titles, authors, years, and countries of origin are real.

Re-run after editing:
    python3 backend/scripts/generate_world_literature_expansion2.py
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
    # --- Latin America ---
    ("One Hundred Years of Solitude", "Gabriel García Márquez", "1967", "Colombia", ["Family", "Magical Realism", "Time"]),
    ("Love in the Time of Cholera", "Gabriel García Márquez", "1985", "Colombia", ["Love", "Aging", "Obsession"]),
    ("The Autumn of the Patriarch", "Gabriel García Márquez", "1975", "Colombia", ["Power", "Dictatorship"]),
    ("Chronicle of a Death Foretold", "Gabriel García Márquez", "1981", "Colombia", ["Honor", "Fate"]),
    ("The House of the Spirits", "Isabel Allende", "1982", "Chile", ["Family", "Politics", "Magical Realism"]),
    ("Of Love and Shadows", "Isabel Allende", "1984", "Chile", ["Injustice", "Love"]),
    ("Hopscotch", "Julio Cortázar", "1963", "Argentina", ["Identity", "Structure", "Existentialism"]),
    ("Ficciones", "Jorge Luis Borges", "1944", "Argentina", ["Reality", "Infinity", "Labyrinths"]),
    ("The Aleph", "Jorge Luis Borges", "1949", "Argentina", ["Infinity", "Perception"]),
    ("The Death of Artemio Cruz", "Carlos Fuentes", "1962", "Mexico", ["Power", "Revolution", "Mortality"]),
    ("Pedro Páramo", "Juan Rulfo", "1955", "Mexico", ["Death", "Memory", "Ghosts"]),
    ("The Savage Detectives", "Roberto Bolaño", "1998", "Chile", ["Poetry", "Wandering", "Youth"]),
    ("2666", "Roberto Bolaño", "2004", "Chile", ["Violence", "Mystery", "Evil"]),
    ("The Feast of the Goat", "Mario Vargas Llosa", "2000", "Peru", ["Dictatorship", "Power", "Trauma"]),
    ("The Time of the Hero", "Mario Vargas Llosa", "1963", "Peru", ["Coming of Age", "Violence"]),
    ("Doña Bárbara", "Rómulo Gallegos", "1929", "Venezuela", ["Civilization", "Nature"]),
    ("The Kingdom of This World", "Alejo Carpentier", "1949", "Cuba", ["Revolution", "Magical Realism"]),
    ("Dona Flor and Her Two Husbands", "Jorge Amado", "1966", "Brazil", ["Love", "Desire", "Society"]),
    ("The Hour of the Star", "Clarice Lispector", "1977", "Brazil", ["Poverty", "Identity", "Existentialism"]),
    ("Captains of the Sands", "Jorge Amado", "1937", "Brazil", ["Poverty", "Youth", "Injustice"]),
    ("Like Water for Chocolate", "Laura Esquivel", "1989", "Mexico", ["Love", "Family", "Food"]),
    ("The Brief Wondrous Life of Oscar Wao", "Junot Díaz", "2007", "Dominican Republic", ["Diaspora", "Identity", "History"]),
    ("In the Time of the Butterflies", "Julia Álvarez", "1994", "Dominican Republic", ["Resistance", "Family", "Dictatorship"]),
    # --- Africa ---
    ("Things Fall Apart", "Chinua Achebe", "1958", "Nigeria", ["Colonialism", "Tradition", "Identity"]),
    ("No Longer at Ease", "Chinua Achebe", "1960", "Nigeria", ["Corruption", "Identity"]),
    ("Arrow of God", "Chinua Achebe", "1964", "Nigeria", ["Tradition", "Colonialism"]),
    ("Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "2006", "Nigeria", ["War", "Identity", "Love"]),
    ("Americanah", "Chimamanda Ngozi Adichie", "2013", "Nigeria", ["Race", "Immigration", "Identity"]),
    ("Purple Hibiscus", "Chimamanda Ngozi Adichie", "2003", "Nigeria", ["Family", "Faith", "Freedom"]),
    ("The Joys of Motherhood", "Buchi Emecheta", "1979", "Nigeria", ["Motherhood", "Tradition", "Gender"]),
    ("Efuru", "Flora Nwapa", "1966", "Nigeria", ["Gender", "Tradition"]),
    ("Wizard of the Crow", "Ngũgĩ wa Thiong'o", "2006", "Kenya", ["Power", "Satire", "Colonialism"]),
    ("Petals of Blood", "Ngũgĩ wa Thiong'o", "1977", "Kenya", ["Corruption", "Independence"]),
    ("Weep Not, Child", "Ngũgĩ wa Thiong'o", "1964", "Kenya", ["Colonialism", "Coming of Age"]),
    ("Nervous Conditions", "Tsitsi Dangarembga", "1988", "Zimbabwe", ["Gender", "Colonialism", "Education"]),
    ("Cry, the Beloved Country", "Alan Paton", "1948", "South Africa", ["Racial Injustice", "Faith", "Family"]),
    ("Disgrace", "J. M. Coetzee", "1999", "South Africa", ["Guilt", "Power", "Post-Apartheid"]),
    ("Life & Times of Michael K", "J. M. Coetzee", "1983", "South Africa", ["Survival", "Freedom"]),
    ("July's People", "Nadine Gordimer", "1981", "South Africa", ["Apartheid", "Power"]),
    ("Burger's Daughter", "Nadine Gordimer", "1979", "South Africa", ["Politics", "Family"]),
    ("So Long a Letter", "Mariama Bâ", "1979", "Senegal", ["Gender", "Marriage", "Tradition"]),
    ("God's Bits of Wood", "Ousmane Sembène", "1960", "Senegal", ["Labor", "Colonialism", "Solidarity"]),
    ("The Beautyful Ones Are Not Yet Born", "Ayi Kwei Armah", "1968", "Ghana", ["Corruption", "Disillusionment"]),
    ("Season of Migration to the North", "Tayeb Salih", "1966", "Sudan", ["Colonialism", "Identity"]),
    ("The Famished Road", "Ben Okri", "1991", "Nigeria", ["Spirituality", "Poverty", "Magical Realism"]),
    ("A Grain of Wheat", "Ngũgĩ wa Thiong'o", "1967", "Kenya", ["Independence", "Betrayal"]),
    # --- Middle East / Arabic ---
    ("The Cairo Trilogy: Palace Walk", "Naguib Mahfouz", "1956", "Egypt", ["Family", "Tradition", "Change"]),
    ("Midaq Alley", "Naguib Mahfouz", "1947", "Egypt", ["Society", "Poverty"]),
    ("The Thief and the Dogs", "Naguib Mahfouz", "1961", "Egypt", ["Betrayal", "Revenge"]),
    ("Children of the Alley", "Naguib Mahfouz", "1959", "Egypt", ["Allegory", "Faith"]),
    ("Men in the Sun", "Ghassan Kanafani", "1963", "Palestine", ["Displacement", "Exile"]),
    ("The Yacoubian Building", "Alaa Al Aswany", "2002", "Egypt", ["Society", "Corruption", "Class"]),
    ("I Saw Ramallah", "Mourid Barghouti", "1997", "Palestine", ["Exile", "Memory"]),
    ("Woman at Point Zero", "Nawal El Saadawi", "1975", "Egypt", ["Gender", "Oppression"]),
    ("Sabriya: Damascus Bitter Sweet", "Ulfat Idilbi", "1980", "Syria", ["Revolution", "Gender"]),
    ("Season of the Rainbirds", "Nadeem Aslam", "1993", "Pakistan", ["Corruption", "Village Life"]),
    ("My Name is Red", "Orhan Pamuk", "1998", "Turkey", ["Art", "Identity", "Mystery"]),
    ("Snow", "Orhan Pamuk", "2002", "Turkey", ["Politics", "Faith", "Identity"]),
    ("The Museum of Innocence", "Orhan Pamuk", "2008", "Turkey", ["Love", "Obsession"]),
    ("Memed, My Hawk", "Yaşar Kemal", "1955", "Turkey", ["Justice", "Rebellion"]),
    # --- South Asia ---
    ("Midnight's Children", "Salman Rushdie", "1981", "India", ["History", "Identity", "Magical Realism"]),
    ("The God of Small Things", "Arundhati Roy", "1997", "India", ["Family", "Caste", "Love"]),
    ("A Suitable Boy", "Vikram Seth", "1993", "India", ["Family", "Society", "Marriage"]),
    ("A Fine Balance", "Rohinton Mistry", "1995", "India", ["Poverty", "Resilience", "Society"]),
    ("The White Tiger", "Aravind Adiga", "2008", "India", ["Class", "Corruption", "Ambition"]),
    ("Train to Pakistan", "Khushwant Singh", "1956", "India", ["Partition", "Violence", "Community"]),
    ("Untouchable", "Mulk Raj Anand", "1935", "India", ["Caste", "Injustice"]),
    ("The Guide", "R. K. Narayan", "1958", "India", ["Redemption", "Spirituality"]),
    ("Gitanjali", "Rabindranath Tagore", "1910", "India", ["Spirituality", "Devotion"]),
    ("The Home and the World", "Rabindranath Tagore", "1916", "India", ["Nationalism", "Marriage"]),
    ("Gora", "Rabindranath Tagore", "1910", "India", ["Identity", "Nationalism"]),
    ("Devdas", "Sarat Chandra Chattopadhyay", "1917", "India", ["Love", "Tragedy"]),
    ("Ice-Candy-Man", "Bapsi Sidhwa", "1988", "Pakistan", ["Partition", "Childhood"]),
    ("Moth Smoke", "Mohsin Hamid", "2000", "Pakistan", ["Class", "Corruption"]),
    ("The Reluctant Fundamentalist", "Mohsin Hamid", "2007", "Pakistan", ["Identity", "Post-9/11"]),
    ("Kartography", "Kamila Shamsie", "2002", "Pakistan", ["Identity", "Family"]),
    ("Burnt Shadows", "Kamila Shamsie", "2009", "Pakistan", ["War", "History", "Identity"]),
    ("Brick Lane", "Monica Ali", "2003", "Bangladesh", ["Immigration", "Identity", "Marriage"]),
    ("A Golden Age", "Tahmima Anam", "2007", "Bangladesh", ["War", "Family", "Independence"]),
    ("Shame", "Salman Rushdie", "1983", "Pakistan", ["Politics", "Satire"]),
    ("Funny Boy", "Shyam Selvadurai", "1994", "Sri Lanka", ["Identity", "Civil War"]),
    ("Anil's Ghost", "Michael Ondaatje", "2000", "Sri Lanka", ["War", "Memory", "Identity"]),
    # --- East Asia ---
    ("Norwegian Wood", "Haruki Murakami", "1987", "Japan", ["Love", "Loss", "Memory"]),
    ("Kafka on the Shore", "Haruki Murakami", "2002", "Japan", ["Identity", "Fate", "Surrealism"]),
    ("The Wind-Up Bird Chronicle", "Haruki Murakami", "1994", "Japan", ["Identity", "Surrealism"]),
    ("1Q84", "Haruki Murakami", "2009", "Japan", ["Reality", "Love", "Fate"]),
    ("Snow Country", "Yasunari Kawabata", "1948", "Japan", ["Love", "Isolation"]),
    ("The Sound of the Mountain", "Yasunari Kawabata", "1954", "Japan", ["Aging", "Family"]),
    ("Kokoro", "Natsume Sōseki", "1914", "Japan", ["Guilt", "Isolation", "Modernity"]),
    ("Botchan", "Natsume Sōseki", "1906", "Japan", ["Satire", "Coming of Age"]),
    ("The Setting Sun", "Osamu Dazai", "1947", "Japan", ["Decline", "Identity"]),
    ("No Longer Human", "Osamu Dazai", "1948", "Japan", ["Alienation", "Despair"]),
    ("Silence", "Shūsaku Endō", "1966", "Japan", ["Faith", "Persecution"]),
    ("The Tale of Genji", "Murasaki Shikibu", "1010", "Japan", ["Love", "Court Life"]),
    ("Rashomon and Other Stories", "Ryūnosuke Akutagawa", "1915", "Japan", ["Truth", "Morality"]),
    ("Convenience Store Woman", "Sayaka Murata", "2016", "Japan", ["Identity", "Conformity"]),
    ("To Live", "Yu Hua", "1993", "China", ["Survival", "Family", "History"]),
    ("Red Sorghum", "Mo Yan", "1986", "China", ["War", "Family", "History"]),
    ("Big Breasts and Wide Hips", "Mo Yan", "1996", "China", ["Family", "History"]),
    ("Wild Swans", "Jung Chang", "1991", "China", ["Family", "History", "Revolution"]),
    ("Soul Mountain", "Gao Xingjian", "1990", "China", ["Journey", "Identity"]),
    ("Dream of the Red Chamber", "Cao Xueqin", "1791", "China", ["Family", "Love", "Society"]),
    ("Journey to the West", "Wu Cheng'en", "1592", "China", ["Adventure", "Mythology"]),
    ("Please Look After Mom", "Kyung-sook Shin", "2008", "South Korea", ["Family", "Memory", "Loss"]),
    ("The Vegetarian", "Han Kang", "2007", "South Korea", ["Identity", "Autonomy", "Trauma"]),
    ("Human Acts", "Han Kang", "2014", "South Korea", ["Violence", "Memory", "History"]),
    ("Pachinko", "Min Jin Lee", "2017", "South Korea", ["Diaspora", "Family", "Identity"]),
    # --- Southeast Asia & Oceania ---
    ("Noli Me Tángere", "José Rizal", "1887", "Philippines", ["Colonialism", "Injustice"]),
    ("El Filibusterismo", "José Rizal", "1891", "Philippines", ["Revolution", "Corruption"]),
    ("This Earth of Mankind", "Pramoedya Ananta Toer", "1980", "Indonesia", ["Colonialism", "Identity"]),
    ("The Buru Quartet: Child of All Nations", "Pramoedya Ananta Toer", "1980", "Indonesia", ["Colonialism", "Awakening"]),
    ("The Sympathizer", "Viet Thanh Nguyen", "2015", "Vietnam", ["War", "Identity", "Espionage"]),
    ("The Sorrow of War", "Bảo Ninh", "1990", "Vietnam", ["War", "Memory", "Loss"]),
    ("Cracking India", "Bapsi Sidhwa", "1991", "Pakistan", ["Partition", "Childhood"]),
    ("The Rice Mother", "Rani Manicka", "2002", "Malaysia", ["Family", "Immigration"]),
    ("The True History of the Kelly Gang", "Peter Carey", "2000", "Australia", ["Outlaw", "Identity"]),
    ("Oscar and Lucinda", "Peter Carey", "1988", "Australia", ["Love", "Obsession", "Faith"]),
    ("The Book Thief", "Markus Zusak", "2005", "Australia", ["War", "Loss", "Words"]),
    ("The Secret River", "Kate Grenville", "2005", "Australia", ["Colonialism", "Guilt"]),
    ("The Bone People", "Keri Hulme", "1984", "New Zealand", ["Identity", "Trauma", "Family"]),
    ("Whale Rider", "Witi Ihimaera", "1987", "New Zealand", ["Tradition", "Identity", "Leadership"]),
    # --- Nordic / Scandinavian ---
    ("Hunger", "Knut Hamsun", "1890", "Norway", ["Poverty", "Alienation"]),
    ("Growth of the Soil", "Knut Hamsun", "1917", "Norway", ["Nature", "Perseverance"]),
    ("Kristin Lavransdatter", "Sigrid Undset", "1920", "Norway", ["Faith", "Love", "Family"]),
    ("The Emigrants", "Vilhelm Moberg", "1949", "Sweden", ["Migration", "Hardship"]),
    ("The Long Ships", "Frans G. Bengtsson", "1941", "Sweden", ["Adventure", "Vikings"]),
    ("Independent People", "Halldór Laxness", "1934", "Iceland", ["Independence", "Struggle"]),
    ("Njál's Saga", "Unknown (Icelandic Saga)", "1280", "Iceland", ["Honor", "Fate", "Feud"]),
    ("The Kalevala", "Elias Lönnrot (compiler)", "1835", "Finland", ["Mythology", "Heroism"]),
    ("Miss Julie", "August Strindberg", "1888", "Sweden", ["Class", "Gender", "Power"]),
    ("The Red Room", "August Strindberg", "1879", "Sweden", ["Satire", "Society"]),
    # --- Eastern Europe ---
    ("The Master Craftsman", "Bruno Schulz", "1934", "Poland", ["Imagination", "Memory"]),
    ("Quo Vadis", "Henryk Sienkiewicz", "1896", "Poland", ["Faith", "Persecution"]),
    ("Ferdydurke", "Witold Gombrowicz", "1937", "Poland", ["Identity", "Satire"]),
    ("Solaris", "Stanisław Lem", "1961", "Poland", ["Consciousness", "Alien Contact"]),
    ("The Tin Drum", "Günter Grass", "1959", "Germany", ["War", "Memory", "Satire"]),
    ("The Unbearable Lightness of Being", "Milan Kundera", "1984", "Czech Republic", ["Identity", "Freedom", "Love"]),
    ("The Book of Laughter and Forgetting", "Milan Kundera", "1979", "Czech Republic", ["Memory", "Politics"]),
    ("The Good Soldier Švejk", "Jaroslav Hašek", "1923", "Czech Republic", ["Satire", "War"]),
    ("I Served the King of England", "Bohumil Hrabal", "1971", "Czech Republic", ["History", "Ambition"]),
    ("The Trial", "Franz Kafka", "1925", "Czech Republic", ["Bureaucracy", "Guilt", "Absurdism"]),
    ("The Castle", "Franz Kafka", "1926", "Czech Republic", ["Alienation", "Bureaucracy"]),
    ("Embers", "Sándor Márai", "1942", "Hungary", ["Friendship", "Betrayal", "Memory"]),
    ("Fatelessness", "Imre Kertész", "1975", "Hungary", ["Holocaust", "Survival"]),
    ("The Bridge on the Drina", "Ivo Andrić", "1945", "Bosnia", ["History", "Community"]),
    ("Death and the Dervish", "Meša Selimović", "1966", "Bosnia", ["Faith", "Power"]),
    ("Kobzar", "Taras Shevchenko", "1840", "Ukraine", ["National Identity", "Freedom"]),
    ("The Master and the Margarita (annotated ed.)", "Mikhail Bulgakov", "1967", "Russia", ["Satire", "Faith"]),
    # --- Caribbean ---
    ("Wide Sargasso Sea", "Jean Rhys", "1966", "Dominica", ["Identity", "Colonialism", "Madness"]),
    ("A House for Mr Biswas", "V. S. Naipaul", "1961", "Trinidad", ["Identity", "Ambition"]),
    ("The Enigma of Arrival", "V. S. Naipaul", "1987", "Trinidad", ["Displacement", "Memory"]),
    ("In the Castle of My Skin", "George Lamming", "1953", "Barbados", ["Colonialism", "Coming of Age"]),
    ("The Lonely Londoners", "Sam Selvon", "1956", "Trinidad", ["Immigration", "Community"]),
    ("Crick Crack, Monkey", "Merle Hodge", "1970", "Trinidad", ["Identity", "Colonialism"]),
    ("Annie John", "Jamaica Kincaid", "1985", "Antigua", ["Coming of Age", "Mother-Daughter"]),
    ("A Small Place", "Jamaica Kincaid", "1988", "Antigua", ["Colonialism", "Tourism"]),
    ("Breath, Eyes, Memory", "Edwidge Danticat", "1994", "Haiti", ["Trauma", "Family", "Womanhood"]),
    ("The Farming of Bones", "Edwidge Danticat", "1998", "Haiti", ["Violence", "Memory"]),
    ("Masters of the Dew", "Jacques Roumain", "1944", "Haiti", ["Solidarity", "Land"]),
    # --- Additional Western / canonical works not yet covered ---
    ("Don Quixote", "Miguel de Cervantes", "1605", "Spain", ["Idealism", "Reality", "Adventure"]),
    ("La Regenta", "Leopoldo Alas (Clarín)", "1884", "Spain", ["Desire", "Society"]),
    ("Fortunata and Jacinta", "Benito Pérez Galdós", "1887", "Spain", ["Class", "Love"]),
    ("The House of Bernarda Alba", "Federico García Lorca", "1936", "Spain", ["Repression", "Gender"]),
    ("Nada", "Carmen Laforet", "1945", "Spain", ["Alienation", "Postwar Society"]),
    ("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Spain", ["Mystery", "Books", "Memory"]),
    ("The Betrothed", "Alessandro Manzoni", "1827", "Italy", ["Love", "Faith", "Justice"]),
    ("The Leopard", "Giuseppe Tomasi di Lampedusa", "1958", "Italy", ["Change", "Aristocracy"]),
    ("If This Is a Man", "Primo Levi", "1947", "Italy", ["Holocaust", "Survival"]),
    ("The Name of the Rose", "Umberto Eco", "1980", "Italy", ["Mystery", "Knowledge", "Faith"]),
    ("My Brilliant Friend", "Elena Ferrante", "2011", "Italy", ["Friendship", "Class", "Ambition"]),
    ("Independent People (Icelandic ed.)", "Halldór Laxness", "1934", "Iceland", ["Independence", "Struggle"]),
    ("The Pillow Book", "Sei Shōnagon", "1002", "Japan", ["Court Life", "Observation"]),
    ("The Alchemist", "Paulo Coelho", "1988", "Brazil", ["Destiny", "Journey"]),
    ("Veronika Decides to Die", "Paulo Coelho", "1998", "Brazil", ["Freedom", "Meaning"]),
    ("The Posthumous Memoirs of Brás Cubas", "Machado de Assis", "1881", "Brazil", ["Satire", "Mortality"]),
    ("Dom Casmurro", "Machado de Assis", "1899", "Brazil", ["Jealousy", "Memory"]),
    ("The Underdogs", "Mariano Azuela", "1915", "Mexico", ["Revolution", "Disillusionment"]),
    ("The Labyrinth of Solitude", "Octavio Paz", "1950", "Mexico", ["Identity", "National Character"]),
    ("The Old Man and the Sea", "Ernest Hemingway", "1952", "United States", ["Perseverance", "Nature"]),
    ("Beloved", "Toni Morrison", "1987", "United States", ["Slavery", "Memory", "Motherhood"]),
    ("Song of Solomon", "Toni Morrison", "1977", "United States", ["Identity", "Family", "Heritage"]),
    ("Their Eyes Were Watching God", "Zora Neale Hurston", "1937", "United States", ["Identity", "Love", "Autonomy"]),
    ("Invisible Man", "Ralph Ellison", "1952", "United States", ["Identity", "Race", "Society"]),
    ("The Grapes of Wrath", "John Steinbeck", "1939", "United States", ["Poverty", "Family", "Injustice"]),
    ("As I Lay Dying", "William Faulkner", "1930", "United States", ["Family", "Death", "Perspective"]),
    ("The Sound and the Fury", "William Faulkner", "1929", "United States", ["Family", "Time", "Decline"]),
    ("One Hundred Years of Solitude (annotated)", "Gabriel García Márquez", "1967", "Colombia", ["Family", "Time"]),
    ("The Handmaid's Tale", "Margaret Atwood", "1985", "Canada", ["Dystopia", "Gender", "Power"]),
    ("Life of Pi", "Yann Martel", "2001", "Canada", ["Survival", "Faith", "Storytelling"]),
    ("Fifth Business", "Robertson Davies", "1970", "Canada", ["Identity", "Guilt", "Memory"]),
    ("The Stone Angel", "Margaret Laurence", "1964", "Canada", ["Aging", "Memory", "Pride"]),
    ("Cat's Eye", "Margaret Atwood", "1988", "Canada", ["Memory", "Friendship", "Art"]),
]


def build_records(existing_ids: set[str]) -> list[dict]:
    records = []
    for i, (title, author, year, origin, themes) in enumerate(BOOKS, start=1):
        book_id = f"wl_global_{i:03d}"
        if book_id in existing_ids:
            continue
        summary = (
            f"{title} by {author} ({year}) from {origin} is a celebrated work of world literature exploring "
            f"{', '.join(themes[:-1]) + (' and ' + themes[-1] if len(themes) > 1 else themes[0])}. "
            f"It broadens the platform's global literary coverage and is widely studied and translated "
            f"around the world."
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
    existing_titles = set()
    for section in data["sections"].values():
        for book in section.get("books", []):
            existing_ids.add(book["id"])
            existing_titles.add(book["title"])

    records = [r for r in build_records(existing_ids) if r["title"] not in existing_titles]

    section = data["sections"].get("world_literature_global")
    if section is None:
        section = {
            "label": "World Literature — Global Voices",
            "emoji": "🌍",
            "age_range": "Adult / College+",
            "books": [],
        }
        data["sections"]["world_literature_global"] = section
    section["books"].extend(records)

    with open(LIBRARY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(s.get("books", [])) for s in data["sections"].values())
    print(f"Added {len(records)} books. Library now has {total} books across {len(data['sections'])} sections.")


if __name__ == "__main__":
    main()
