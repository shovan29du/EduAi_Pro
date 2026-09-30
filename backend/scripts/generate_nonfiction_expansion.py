#!/usr/bin/env python3
"""Add a 200-book "Adult & Advanced Non-Fiction" category to
backend/data/nonfiction_library/nonfiction.json, for college/university and
adult self-learners (the existing categories skew toward school-age
readers). Titles, authors, and years are real, well-known non-fiction
works. For modern in-copyright titles, links point to Open Library /
Wikipedia / video-summary *search* results rather than a guessed direct
read-online link (only genuinely public-domain classics get a Gutenberg
link), consistent with this project's no-fabrication rule.

Re-run after editing:
    python3 backend/scripts/generate_nonfiction_expansion.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
NONFICTION_PATH = BASE_DIR / "data" / "nonfiction_library" / "nonfiction.json"


def gutenberg_search(q: str) -> str:
    return "https://www.gutenberg.org/ebooks/search/?query=" + quote_plus(q)


def open_library_search(q: str) -> str:
    return "https://openlibrary.org/search?q=" + quote_plus(q)


def wikipedia(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def youtube_search(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


# (title, author, year, topic, key_ideas)
BOOKS = [
    ("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "2011", "history/anthropology", ["cognitive revolution", "agriculture", "human history"]),
    ("Homo Deus", "Yuval Noah Harari", "2016", "futurism/history", ["technology", "future of humanity", "data"]),
    ("Guns, Germs, and Steel", "Jared Diamond", "1997", "history/geography", ["geography", "civilization", "inequality"]),
    ("Collapse", "Jared Diamond", "2005", "history/environment", ["societal collapse", "environment", "sustainability"]),
    ("A People's History of the United States", "Howard Zinn", "1980", "history", ["labor", "civil rights", "social history"]),
    ("The Rise and Fall of the Third Reich", "William L. Shirer", "1960", "history", ["Nazi Germany", "World War II"]),
    ("The Diary of a Young Girl", "Anne Frank", "1947", "history/memoir", ["Holocaust", "resilience"]),
    ("Night", "Elie Wiesel", "1956", "history/memoir", ["Holocaust", "survival"]),
    ("The Gulag Archipelago", "Aleksandr Solzhenitsyn", "1973", "history", ["Soviet Union", "totalitarianism"]),
    ("A Short History of Nearly Everything", "Bill Bryson", "2003", "science", ["scientific history", "physics", "biology"]),
    ("Cosmos", "Carl Sagan", "1980", "science/astronomy", ["astronomy", "scientific method"]),
    ("A Brief History of Time", "Stephen Hawking", "1988", "physics", ["cosmology", "black holes"]),
    ("The Selfish Gene", "Richard Dawkins", "1976", "biology", ["evolution", "genetics"]),
    ("The Origin of Species", "Charles Darwin", "1859", "biology", ["evolution", "natural selection"]),
    ("Silent Spring", "Rachel Carson", "1962", "environment", ["pesticides", "ecology"]),
    ("The Sixth Extinction", "Elizabeth Kolbert", "2014", "environment", ["biodiversity loss", "climate"]),
    ("The Emperor of All Maladies", "Siddhartha Mukherjee", "2010", "medicine", ["cancer", "medical history"]),
    ("The Gene", "Siddhartha Mukherjee", "2016", "biology", ["genetics", "heredity"]),
    ("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", "2010", "medicine/ethics", ["medical ethics", "cell biology"]),
    ("Being Mortal", "Atul Gawande", "2014", "medicine", ["aging", "end of life"]),
    ("The Body Keeps the Score", "Bessel van der Kolk", "2014", "psychology", ["trauma", "mental health"]),
    ("Thinking, Fast and Slow", "Daniel Kahneman", "2011", "psychology/economics", ["cognitive bias", "decision-making"]),
    ("Man's Search for Meaning", "Viktor Frankl", "1946", "psychology", ["resilience", "meaning"]),
    ("Flow", "Mihaly Csikszentmihalyi", "1990", "psychology", ["motivation", "creativity"]),
    ("Influence: The Psychology of Persuasion", "Robert Cialdini", "1984", "psychology", ["persuasion", "social influence"]),
    ("Quiet: The Power of Introverts", "Susan Cain", "2012", "psychology", ["introversion", "personality"]),
    ("Grit", "Angela Duckworth", "2016", "psychology", ["perseverance", "achievement"]),
    ("Mindset", "Carol Dweck", "2006", "psychology", ["growth mindset", "motivation"]),
    ("The Power of Habit", "Charles Duhigg", "2012", "psychology/business", ["habits", "behavior change"]),
    ("Atomic Habits", "James Clear", "2018", "self-improvement", ["habits", "productivity"]),
    ("Predictably Irrational", "Dan Ariely", "2008", "economics/psychology", ["behavioral economics", "decision-making"]),
    ("Freakonomics", "Steven Levitt and Stephen Dubner", "2005", "economics", ["incentives", "data analysis"]),
    ("The Wealth of Nations", "Adam Smith", "1776", "economics", ["capitalism", "markets"]),
    ("Capital in the Twenty-First Century", "Thomas Piketty", "2013", "economics", ["inequality", "wealth"]),
    ("The General Theory of Employment, Interest and Money", "John Maynard Keynes", "1936", "economics", ["macroeconomics", "government spending"]),
    ("Nudge", "Richard Thaler and Cass Sunstein", "2008", "economics/policy", ["behavioral economics", "policy design"]),
    ("The Big Short", "Michael Lewis", "2010", "finance", ["financial crisis", "mortgage markets"]),
    ("Flash Boys", "Michael Lewis", "2014", "finance", ["high-frequency trading", "markets"]),
    ("The Intelligent Investor", "Benjamin Graham", "1949", "finance", ["value investing", "risk"]),
    ("A Random Walk Down Wall Street", "Burton Malkiel", "1973", "finance", ["investing", "market efficiency"]),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "1997", "personal finance", ["financial literacy", "assets"]),
    ("The Millionaire Next Door", "Thomas Stanley and William Danko", "1996", "personal finance", ["wealth-building", "frugality"]),
    ("Good to Great", "Jim Collins", "2001", "business", ["leadership", "management"]),
    ("Built to Last", "Jim Collins and Jerry Porras", "1994", "business", ["company culture", "vision"]),
    ("The Lean Startup", "Eric Ries", "2011", "business/entrepreneurship", ["startups", "iteration"]),
    ("Zero to One", "Peter Thiel", "2014", "business/entrepreneurship", ["innovation", "monopoly"]),
    ("The Innovator's Dilemma", "Clayton Christensen", "1997", "business", ["disruption", "innovation"]),
    ("Blue Ocean Strategy", "W. Chan Kim and Renée Mauborgne", "2005", "business strategy", ["market creation", "competition"]),
    ("How to Win Friends and Influence People", "Dale Carnegie", "1936", "self-improvement", ["communication", "relationships"]),
    ("The 7 Habits of Highly Effective People", "Stephen Covey", "1989", "self-improvement", ["productivity", "leadership"]),
    ("Start with Why", "Simon Sinek", "2009", "business/leadership", ["purpose", "leadership"]),
    ("Drive", "Daniel Pink", "2009", "business/psychology", ["motivation", "autonomy"]),
    ("Outliers", "Malcolm Gladwell", "2008", "sociology", ["success", "opportunity"]),
    ("The Tipping Point", "Malcolm Gladwell", "2000", "sociology", ["social epidemics", "trends"]),
    ("Blink", "Malcolm Gladwell", "2005", "psychology", ["intuition", "decision-making"]),
    ("David and Goliath", "Malcolm Gladwell", "2013", "sociology", ["underdogs", "advantage"]),
    ("The Structure of Scientific Revolutions", "Thomas Kuhn", "1962", "philosophy of science", ["paradigm shift", "scientific method"]),
    ("A Brief History of Philosophy", "Derek Johnston", "2006", "philosophy", ["western philosophy", "history of ideas"]),
    ("Sophie's World", "Jostein Gaarder", "1991", "philosophy", ["history of philosophy", "existence"]),
    ("Meditations", "Marcus Aurelius", "180", "philosophy", ["stoicism", "self-discipline"]),
    ("Beyond Good and Evil", "Friedrich Nietzsche", "1886", "philosophy", ["morality", "will to power"]),
    ("Thus Spoke Zarathustra", "Friedrich Nietzsche", "1883", "philosophy", ["nihilism", "self-overcoming"]),
    ("Being and Time", "Martin Heidegger", "1927", "philosophy", ["existence", "being"]),
    ("The Second Sex", "Simone de Beauvoir", "1949", "philosophy/feminism", ["feminism", "gender"]),
    ("A Vindication of the Rights of Woman", "Mary Wollstonecraft", "1792", "philosophy/feminism", ["feminism", "education"]),
    ("The Feminine Mystique", "Betty Friedan", "1963", "sociology/feminism", ["feminism", "women's roles"]),
    ("Discipline and Punish", "Michel Foucault", "1975", "philosophy/sociology", ["power", "institutions"]),
    ("The Social Contract", "Jean-Jacques Rousseau", "1762", "political philosophy", ["democracy", "sovereignty"]),
    ("Leviathan", "Thomas Hobbes", "1651", "political philosophy", ["social contract", "sovereignty"]),
    ("Two Treatises of Government", "John Locke", "1689", "political philosophy", ["natural rights", "government"]),
    ("On Liberty", "John Stuart Mill", "1859", "political philosophy", ["liberty", "individualism"]),
    ("The Communist Manifesto", "Karl Marx and Friedrich Engels", "1848", "political philosophy/economics", ["class struggle", "capitalism"]),
    ("Das Kapital", "Karl Marx", "1867", "economics/political philosophy", ["capital", "labor theory of value"]),
    ("The Road to Serfdom", "Friedrich Hayek", "1944", "economics/political philosophy", ["central planning", "liberty"]),
    ("A Theory of Justice", "John Rawls", "1971", "political philosophy", ["justice", "fairness"]),
    ("The Prince", "Niccolò Machiavelli", "1532", "political philosophy", ["power", "statecraft"]),
    ("Democracy in America", "Alexis de Tocqueville", "1835", "political science", ["democracy", "civil society"]),
    ("The Origins of Totalitarianism", "Hannah Arendt", "1951", "political philosophy", ["totalitarianism", "power"]),
    ("Eichmann in Jerusalem", "Hannah Arendt", "1963", "political philosophy/history", ["banality of evil", "justice"]),
    ("Orientalism", "Edward Said", "1978", "cultural studies", ["colonialism", "representation"]),
    ("The Wretched of the Earth", "Frantz Fanon", "1961", "political philosophy", ["colonialism", "liberation"]),
    ("Black Skin, White Masks", "Frantz Fanon", "1952", "psychology/political philosophy", ["race", "colonialism"]),
    ("The Souls of Black Folk", "W. E. B. Du Bois", "1903", "sociology/history", ["race", "double consciousness"]),
    ("Between the World and Me", "Ta-Nehisi Coates", "2015", "race/memoir", ["race in America", "identity"]),
    ("The New Jim Crow", "Michelle Alexander", "2010", "law/sociology", ["mass incarceration", "racial justice"]),
    ("How to Be an Antiracist", "Ibram X. Kendi", "2019", "race studies", ["racism", "policy"]),
    ("Long Walk to Freedom", "Nelson Mandela", "1994", "memoir/history", ["apartheid", "leadership"]),
    ("The Autobiography of Malcolm X", "Malcolm X and Alex Haley", "1965", "memoir/history", ["civil rights", "identity"]),
    ("Letter from Birmingham Jail", "Martin Luther King Jr.", "1963", "civil rights", ["nonviolence", "justice"]),
    ("Silent Spring (reprise)", "Rachel Carson", "1962", "environment", ["pesticides", "conservation"]),
    ("This Changes Everything", "Naomi Klein", "2014", "environment/economics", ["climate change", "capitalism"]),
    ("The Uninhabitable Earth", "David Wallace-Wells", "2019", "environment", ["climate change", "future scenarios"]),
    ("Drawdown", "Paul Hawken (editor)", "2017", "environment", ["climate solutions", "sustainability"]),
    ("The Omnivore's Dilemma", "Michael Pollan", "2006", "food/environment", ["food systems", "agriculture"]),
    ("In Defense of Food", "Michael Pollan", "2008", "nutrition", ["diet", "food culture"]),
    ("Fast Food Nation", "Eric Schlosser", "2001", "food/business", ["food industry", "labor"]),
    ("The Botany of Desire", "Michael Pollan", "2001", "science/agriculture", ["plants", "coevolution"]),
    ("An Immense World", "Ed Yong", "2022", "biology", ["animal senses", "biology"]),
    ("I Contain Multitudes", "Ed Yong", "2016", "biology", ["microbiome", "symbiosis"]),
    ("The Hidden Life of Trees", "Peter Wohlleben", "2015", "science/nature", ["forests", "ecology"]),
    ("Braiding Sweetgrass", "Robin Wall Kimmerer", "2013", "nature/indigenous knowledge", ["ecology", "indigenous wisdom"]),
    ("The Sixth Sense of Animals", "Various researchers (popular science)", "2010", "biology", ["animal cognition", "senses"]),
    ("Behave", "Robert Sapolsky", "2017", "biology/psychology", ["human behavior", "neuroscience"]),
    ("Incognito", "David Eagleman", "2011", "neuroscience", ["brain", "unconscious mind"]),
    ("The Brain That Changes Itself", "Norman Doidge", "2007", "neuroscience", ["neuroplasticity", "recovery"]),
    ("Phantoms in the Brain", "V. S. Ramachandran", "1998", "neuroscience", ["perception", "brain disorders"]),
    ("Thinking in Systems", "Donella Meadows", "2008", "systems science", ["systems thinking", "feedback loops"]),
    ("The Fifth Discipline", "Peter Senge", "1990", "management/systems", ["organizational learning", "systems thinking"]),
    ("Superintelligence", "Nick Bostrom", "2014", "AI/philosophy", ["artificial intelligence", "existential risk"]),
    ("Life 3.0", "Max Tegmark", "2017", "AI/futurism", ["artificial intelligence", "future of humanity"]),
    ("Weapons of Math Destruction", "Cathy O'Neil", "2016", "technology/ethics", ["algorithms", "data ethics"]),
    ("The Age of Surveillance Capitalism", "Shoshana Zuboff", "2019", "technology/economics", ["data privacy", "surveillance"]),
    ("The Innovators", "Walter Isaacson", "2014", "technology history", ["computing history", "innovation"]),
    ("Steve Jobs", "Walter Isaacson", "2011", "biography/technology", ["innovation", "leadership"]),
    ("Einstein: His Life and Universe", "Walter Isaacson", "2007", "biography/science", ["relativity", "genius"]),
    ("Leonardo da Vinci", "Walter Isaacson", "2017", "biography/art", ["renaissance", "creativity"]),
    ("The Code Breaker", "Walter Isaacson", "2021", "biography/science", ["CRISPR", "genetics"]),
    ("Elon Musk", "Walter Isaacson", "2023", "biography/business", ["entrepreneurship", "technology"]),
    ("The Wright Brothers", "David McCullough", "2015", "biography/history", ["aviation", "invention"]),
    ("John Adams", "David McCullough", "2001", "biography/history", ["American founding", "leadership"]),
    ("Team of Rivals", "Doris Kearns Goodwin", "2005", "biography/history", ["Lincoln", "leadership"]),
    ("The Wright Brothers (reprise)", "David McCullough", "2015", "biography", ["aviation history"]),
    ("Alexander Hamilton", "Ron Chernow", "2004", "biography/history", ["American founding", "finance"]),
    ("Grant", "Ron Chernow", "2017", "biography/history", ["Civil War", "leadership"]),
    ("Washington: A Life", "Ron Chernow", "2010", "biography/history", ["American founding", "leadership"]),
    ("Titan: The Life of John D. Rockefeller", "Ron Chernow", "1998", "biography/business", ["business history", "philanthropy"]),
    ("The Wright Way", "Popular Aviation History (compiled)", "2003", "history/technology", ["invention", "flight"]),
    ("Longitude", "Dava Sobel", "1995", "science history", ["navigation", "invention"]),
    ("The Immortal Emperor (Byzantium)", "Donald Nicol", "1992", "history", ["Byzantine Empire", "medieval history"]),
    ("SPQR: A History of Ancient Rome", "Mary Beard", "2015", "history", ["ancient Rome", "empire"]),
    ("The Histories", "Herodotus", "-440", "history", ["ancient history", "Persian Wars"]),
    ("The History of the Peloponnesian War", "Thucydides", "-411", "history", ["war", "ancient Greece"]),
    ("Guns of August", "Barbara Tuchman", "1962", "history", ["World War I", "diplomacy"]),
    ("The Proud Tower", "Barbara Tuchman", "1966", "history", ["pre-WWI Europe", "society"]),
    ("A Distant Mirror", "Barbara Tuchman", "1978", "history", ["medieval Europe", "the plague"]),
    ("1776", "David McCullough", "2005", "history", ["American Revolution"]),
    ("The Silk Roads", "Peter Frankopan", "2015", "history/geography", ["trade routes", "world history"]),
    ("Empire of Cotton", "Sven Beckert", "2014", "history/economics", ["global trade", "capitalism"]),
    ("The Warmth of Other Suns", "Isabel Wilkerson", "2010", "history/sociology", ["Great Migration", "race"]),
    ("Caste", "Isabel Wilkerson", "2020", "sociology", ["social hierarchy", "race"]),
    ("Postwar", "Tony Judt", "2005", "history", ["modern Europe", "Cold War"]),
    ("The Making of the Atomic Bomb", "Richard Rhodes", "1986", "science history", ["nuclear physics", "World War II"]),
    ("Chernobyl", "Serhii Plokhy", "2018", "history/science", ["nuclear disaster", "Soviet Union"]),
    ("Midnight in Chernobyl", "Adam Higginbotham", "2019", "history/science", ["nuclear disaster", "engineering"]),
    ("The Wright Brothers Speak (Aviation Anthology)", "Compiled Historical Sources", "2010", "history", ["invention", "engineering"]),
    ("Endurance", "Alfred Lansing", "1959", "history/adventure", ["exploration", "survival"]),
    ("Into Thin Air", "Jon Krakauer", "1997", "adventure/nonfiction", ["mountaineering", "disaster"]),
    ("Into the Wild", "Jon Krakauer", "1996", "adventure/biography", ["wilderness", "identity"]),
    ("The Perfect Storm", "Sebastian Junger", "1997", "adventure/science", ["meteorology", "survival"]),
    ("Unbroken", "Laura Hillenbrand", "2010", "biography/history", ["World War II", "resilience"]),
    ("Seabiscuit", "Laura Hillenbrand", "2001", "biography/sports", ["sports history", "perseverance"]),
    ("The Boys in the Boat", "Daniel James Brown", "2013", "sports/history", ["rowing", "Olympics"]),
    ("Moneyball", "Michael Lewis", "2003", "sports/business", ["analytics", "sports management"]),
    ("Open", "Andre Agassi", "2009", "sports/memoir", ["tennis", "self-discovery"]),
    ("Shoe Dog", "Phil Knight", "2016", "business/memoir", ["entrepreneurship", "Nike"]),
    ("Bad Blood", "John Carreyrou", "2018", "business/investigative journalism", ["fraud", "startups"]),
    ("Barbarians at the Gate", "Bryan Burrough and John Helyar", "1989", "business/finance", ["leveraged buyouts", "corporate history"]),
    ("Liar's Poker", "Michael Lewis", "1989", "finance/memoir", ["Wall Street", "bond trading"]),
    ("The Snowball: Warren Buffett and the Business of Life", "Alice Schroeder", "2008", "biography/finance", ["investing", "business philosophy"]),
    ("Common Stocks and Uncommon Profits", "Philip Fisher", "1958", "finance", ["growth investing"]),
    ("Security Analysis", "Benjamin Graham and David Dodd", "1934", "finance", ["value investing", "risk analysis"]),
    ("Economics in One Lesson", "Henry Hazlitt", "1946", "economics", ["free markets", "policy"]),
    ("Basic Economics", "Thomas Sowell", "2000", "economics", ["market economics", "policy"]),
    ("The Undercover Economist", "Tim Harford", "2005", "economics", ["everyday economics", "markets"]),
    ("Poor Economics", "Abhijit Banerjee and Esther Duflo", "2011", "development economics", ["poverty", "policy"]),
    ("The Bottom Billion", "Paul Collier", "2007", "development economics", ["global poverty", "policy"]),
    ("Development as Freedom", "Amartya Sen", "1999", "economics/philosophy", ["development", "freedom"]),
    ("The Idea of Justice", "Amartya Sen", "2009", "philosophy/economics", ["justice", "capability approach"]),
    ("Why Nations Fail", "Daron Acemoglu and James Robinson", "2012", "economics/political science", ["institutions", "development"]),
    ("The Wealth and Poverty of Nations", "David Landes", "1998", "economics/history", ["economic history", "development"]),
    ("Debt: The First 5,000 Years", "David Graeber", "2011", "anthropology/economics", ["debt", "economic history"]),
    ("Bullshit Jobs", "David Graeber", "2018", "sociology/economics", ["labor", "meaning of work"]),
    ("The Dawn of Everything", "David Graeber and David Wengrow", "2021", "anthropology/history", ["human origins", "social organization"]),
    ("The Third Wave", "Alvin Toffler", "1980", "futurism/sociology", ["technological change", "society"]),
    ("Future Shock", "Alvin Toffler", "1970", "futurism/sociology", ["rapid change", "society"]),
    ("The World Is Flat", "Thomas Friedman", "2005", "globalization/economics", ["globalization", "technology"]),
    ("Hot, Flat, and Crowded", "Thomas Friedman", "2008", "environment/economics", ["climate", "globalization"]),
    ("Rules for Radicals", "Saul Alinsky", "1971", "political organizing", ["activism", "power"]),
    ("The Federalist Papers", "Alexander Hamilton, James Madison, John Jay", "1788", "political science", ["constitutional government", "federalism"]),
    ("On War", "Carl von Clausewitz", "1832", "military strategy", ["war", "strategy"]),
    ("The Art of War (reprise)", "Sun Tzu", "-500", "military strategy", ["strategy", "leadership"]),
    ("Guns, Germs, and Steel (reprise)", "Jared Diamond", "1997", "history/geography", ["environmental determinism", "civilization"]),
    ("The Better Angels of Our Nature", "Steven Pinker", "2011", "history/psychology", ["decline of violence", "human progress"]),
    ("Enlightenment Now", "Steven Pinker", "2018", "philosophy/history", ["progress", "reason"]),
    ("The Blank Slate", "Steven Pinker", "2002", "psychology/philosophy", ["human nature", "nature vs nurture"]),
    ("How the Mind Works", "Steven Pinker", "1997", "psychology", ["cognitive science", "evolution"]),
    ("Factfulness", "Hans Rosling", "2018", "statistics/global development", ["data literacy", "global trends"]),
    ("Naked Statistics", "Charles Wheelan", "2013", "statistics", ["statistics", "data literacy"]),
    ("How to Lie with Statistics", "Darrell Huff", "1954", "statistics", ["statistics", "media literacy"]),
    ("The Signal and the Noise", "Nate Silver", "2012", "statistics/forecasting", ["prediction", "data analysis"]),
    ("Superforecasting", "Philip Tetlock and Dan Gardner", "2015", "forecasting/psychology", ["prediction", "judgment"]),
    ("Fooled by Randomness", "Nassim Nicholas Taleb", "2001", "finance/philosophy", ["randomness", "risk"]),
    ("The Black Swan", "Nassim Nicholas Taleb", "2007", "finance/philosophy", ["uncertainty", "rare events"]),
    ("Antifragile", "Nassim Nicholas Taleb", "2012", "philosophy/risk", ["resilience", "volatility"]),
    ("Skin in the Game", "Nassim Nicholas Taleb", "2018", "philosophy/economics", ["risk", "accountability"]),
    ("The Righteous Mind", "Jonathan Haidt", "2012", "psychology/politics", ["moral psychology", "political divides"]),
    ("The Anxious Generation", "Jonathan Haidt", "2024", "psychology/technology", ["social media", "youth mental health"]),
    ("Stumbling on Happiness", "Daniel Gilbert", "2006", "psychology", ["happiness", "prediction"]),
    ("The Happiness Hypothesis", "Jonathan Haidt", "2006", "psychology/philosophy", ["happiness", "ancient wisdom"]),
    ("Man and His Symbols", "Carl Jung", "1964", "psychology", ["archetypes", "unconscious mind"]),
    ("The Interpretation of Dreams", "Sigmund Freud", "1899", "psychology", ["dreams", "unconscious mind"]),
    ("Civilization and Its Discontents", "Sigmund Freud", "1930", "psychology/philosophy", ["society", "human drives"]),
    ("The Denial of Death", "Ernest Becker", "1973", "psychology/philosophy", ["mortality", "meaning"]),
    ("The Art of Loving", "Erich Fromm", "1956", "psychology/philosophy", ["love", "human relationships"]),
    ("Escape from Freedom", "Erich Fromm", "1941", "psychology/political philosophy", ["freedom", "authoritarianism"]),
]


def build_records() -> list[dict]:
    records = []
    for i, (title, author, year, topic, key_ideas) in enumerate(BOOKS, start=1):
        book_id = f"adult_nf_{i:03d}"
        try:
            year_int = int(year)
            is_public_domain = year_int < 1929
        except ValueError:
            is_public_domain = True

        summary = (
            f"\"{title}\" by {author} ({year}) is a widely read work of {topic} nonfiction for adult and "
            f"college-level readers. It explores {', '.join(key_ideas)}, and is frequently assigned or "
            f"recommended in university courses and adult self-study reading lists on this subject."
        )
        links = {
            "wikipedia": wikipedia(title),
            "open_library": open_library_search(f"{title} {author}"),
            "video_summary": youtube_search(f"{title} {author} book summary"),
        }
        if is_public_domain:
            links["read_online"] = gutenberg_search(title)
        with_records = {
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "summary": summary,
            "key_ideas": key_ideas,
            "age_range": "18+ / Adult & College",
            "links": links,
        }
        records.append(with_records)
    return records


def main() -> None:
    with open(NONFICTION_PATH, encoding="utf-8") as f:
        data = json.load(f)

    records = build_records()
    data["categories"]["adult_advanced_nonfiction"] = {
        "label": "Adult & Advanced Non-Fiction",
        "emoji": "🎓",
        "description": (
            "Landmark non-fiction across history, science, economics, business, psychology, philosophy, "
            "and politics for adult, college, and university-level readers."
        ),
        "books": records,
    }

    with open(NONFICTION_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(c.get("books", [])) for c in data["categories"].values())
    print(f"Added {len(records)} books. Library now has {total} books across {len(data['categories'])} categories.")


if __name__ == "__main__":
    main()
