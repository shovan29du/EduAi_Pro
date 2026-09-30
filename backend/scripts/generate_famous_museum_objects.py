#!/usr/bin/env python3
"""Add a large gallery of genuinely famous, individually-named real artworks
and artifacts to the Virtual Museum.

Every entry is a real, well-known work (not a generated placeholder like the
"World Collections" gallery from the previous batch). Each carries an
accurate ``wiki_title`` -- the real Wikipedia article title -- so the
existing ``WikiThumbnail`` component (frontend/src/components/VirtualMuseum.jsx)
fetches a genuine, live photo of the actual work from Wikipedia's public
REST API at render time. This project does not fabricate direct image URLs;
the live-fetch-with-fallback mechanism is the honest way to get a real
thumbnail for every entry without guessing file paths that might not exist.

Re-run after editing:
    python3 backend/scripts/generate_famous_museum_objects.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"


def wiki_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def commons_search(q: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(q)


def yt(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def smarthistory(q: str) -> str:
    return "https://smarthistory.org/?s=" + quote_plus(q)


# Each category is a list of:
#   (name, wiki_title, creator_or_culture, date, origin, one_line_description)
# `category` (the CAT_EMOJI-compatible facet) is assigned per-list below.

FAMOUS_PAINTINGS = [
    ("Mona Lisa", "Mona Lisa", "Leonardo da Vinci", "c. 1503-1519", "Italy", "The world's most famous portrait, housed in the Louvre, celebrated for its enigmatic expression and sfumato technique."),
    ("The Starry Night", "The Starry Night", "Vincent van Gogh", "1889", "Netherlands/France", "A swirling night sky over a village, painted from memory while van Gogh was at an asylum in Saint-Rémy."),
    ("The Last Supper", "The Last Supper (Leonardo)", "Leonardo da Vinci", "1495-1498", "Italy", "A mural depicting Jesus's final meal with his apostles, painted on a refectory wall in Milan."),
    ("Girl with a Pearl Earring", "Girl with a Pearl Earring", "Johannes Vermeer", "c. 1665", "Netherlands", "Sometimes called the 'Mona Lisa of the North', a luminous tronie of a girl in a turban."),
    ("The Night Watch", "The Night Watch", "Rembrandt", "1642", "Netherlands", "A dramatic group portrait of a civic militia company, famous for its use of light and shadow."),
    ("Las Meninas", "Las Meninas", "Diego Velázquez", "1656", "Spain", "A complex composition depicting the Spanish royal court, including a self-portrait of the artist."),
    ("The Birth of Venus", "The Birth of Venus", "Sandro Botticelli", "c. 1485", "Italy", "Venus emerging from the sea on a shell, one of the defining images of the Italian Renaissance."),
    ("The School of Athens", "The School of Athens", "Raphael", "1509-1511", "Italy", "A fresco gathering the great philosophers of antiquity in one idealized architectural space."),
    ("The Creation of Adam", "The Creation of Adam", "Michelangelo", "c. 1512", "Italy", "The iconic Sistine Chapel ceiling fresco showing God reaching toward Adam."),
    ("Guernica", "Guernica (Picasso)", "Pablo Picasso", "1937", "Spain", "A monumental anti-war painting responding to the bombing of the Basque town of Guernica."),
    ("The Persistence of Memory", "The Persistence of Memory", "Salvador Dalí", "1931", "Spain", "Surrealist melting clocks in a dreamlike landscape."),
    ("The Scream", "The Scream", "Edvard Munch", "1893", "Norway", "An expressionist depiction of anxiety, one of the most recognizable images in art."),
    ("American Gothic", "American Gothic", "Grant Wood", "1930", "United States", "A farmer and his daughter standing before a Gothic Revival house, an icon of American art."),
    ("Water Lilies", "Water Lilies (Monet series)", "Claude Monet", "1897-1926", "France", "A series of roughly 250 paintings of Monet's flower garden at Giverny."),
    ("Impression, Sunrise", "Impression, Sunrise", "Claude Monet", "1872", "France", "The painting that gave Impressionism its name, depicting the port of Le Havre at dawn."),
    ("A Sunday Afternoon on the Island of La Grande Jatte", "A Sunday Afternoon on the Island of La Grande Jatte", "Georges Seurat", "1884-1886", "France", "A landmark of pointillism depicting Parisians relaxing by the Seine."),
    ("The Kiss", "The Kiss (Klimt)", "Gustav Klimt", "1907-1908", "Austria", "A gold-leaf masterpiece of two embracing figures, an icon of Art Nouveau."),
    ("Liberty Leading the People", "Liberty Leading the People", "Eugène Delacroix", "1830", "France", "A Romantic allegory of the July Revolution, with Liberty personified carrying the French flag."),
    ("The Great Wave off Kanagawa", "The Great Wave off Kanagawa", "Hokusai", "c. 1831", "Japan", "The most famous work of Japanese ukiyo-e woodblock printing, part of Hokusai's '36 Views of Mount Fuji'."),
    ("Whistler's Mother", "Whistler's Mother", "James McNeill Whistler", "1871", "United States", "Formally titled 'Arrangement in Grey and Black No. 1', an icon of American portraiture."),
    ("Nighthawks", "Nighthawks", "Edward Hopper", "1942", "United States", "Late-night diner patrons captured in stark isolation, a defining image of American Realism."),
    ("Christina's World", "Christina's World", "Andrew Wyeth", "1948", "United States", "A woman in a field gazes toward a distant farmhouse, one of America's best-known paintings."),
    ("The Arnolfini Portrait", "Arnolfini Portrait", "Jan van Eyck", "1434", "Netherlands", "A richly detailed double portrait celebrated for its convex mirror and realistic detail."),
    ("Girl with a Pearl Earring (reprise)", "Girl with a Pearl Earring", "Johannes Vermeer", "c. 1665", "Netherlands", "Also known as the 'Mona Lisa of the North'."),
    ("The Anatomy Lesson of Dr. Nicolaes Tulp", "The Anatomy Lesson of Dr. Nicolaes Tulp", "Rembrandt", "1632", "Netherlands", "A group portrait of surgeons observing a dissection, an early masterpiece by Rembrandt."),
    ("Wanderer above the Sea of Fog", "Wanderer above the Sea of Fog", "Caspar David Friedrich", "c. 1818", "Germany", "The definitive image of German Romanticism, a solitary figure surveying a misty landscape."),
    ("The Fighting Temeraire", "The Fighting Temeraire", "J. M. W. Turner", "1839", "United Kingdom", "A warship being towed to be scrapped, voted Britain's favourite painting in a 2005 poll."),
    ("Ophelia", "Ophelia (painting)", "John Everett Millais", "1851-1852", "United Kingdom", "A Pre-Raphaelite depiction of Shakespeare's Ophelia drowning amid vivid botanical detail."),
    ("The Hay Wain", "The Hay Wain", "John Constable", "1821", "United Kingdom", "An idyllic English rural landscape, among the most reproduced British paintings."),
    ("Las Hilanderas", "Las Hilanderas", "Diego Velázquez", "c. 1657", "Spain", "The Spinners, a masterwork blending mythology and everyday labor."),
    ("The Third of May 1808", "The Third of May 1808", "Francisco Goya", "1814", "Spain", "A harrowing depiction of Spanish resistance fighters executed by Napoleon's soldiers."),
    ("Saturn Devouring His Son", "Saturn Devouring His Son", "Francisco Goya", "1819-1823", "Spain", "One of Goya's disturbing 'Black Paintings', painted directly on the walls of his home."),
    ("Las Meninas (reprise)", "Las Meninas", "Diego Velázquez", "1656", "Spain", "One of the most analyzed paintings in Western art history."),
    ("The Garden of Earthly Delights", "The Garden of Earthly Delights", "Hieronymus Bosch", "c. 1490-1510", "Netherlands", "A fantastical triptych depicting paradise, earthly pleasure, and hell."),
    ("Primavera", "Primavera (Botticelli)", "Sandro Botticelli", "c. 1480", "Italy", "An allegorical celebration of spring featuring Venus, the Graces, and mythological figures."),
    ("The Sistine Madonna", "Sistine Madonna", "Raphael", "1512", "Italy", "Famous for its two contemplative cherubs at the bottom of the composition."),
    ("Venus of Urbino", "Venus of Urbino", "Titian", "1538", "Italy", "A reclining nude that became a touchstone for later Western depictions of the female form."),
    ("Bacchus and Ariadne", "Bacchus and Ariadne", "Titian", "1520-1523", "Italy", "A dynamic mythological scene celebrated for its vivid color and composition."),
    ("Judith Slaying Holofernes", "Judith Slaying Holofernes (Artemisia Gentileschi)", "Artemisia Gentileschi", "c. 1614-1620", "Italy", "A powerful Baroque depiction of the biblical heroine Judith, by one of the era's foremost female painters."),
    ("The Calling of St Matthew", "The Calling of Saint Matthew", "Caravaggio", "1599-1600", "Italy", "A dramatic use of light (chiaroscuro) to depict Christ calling Matthew from his tax collector's table."),
    ("Bacchus", "Bacchus (Caravaggio)", "Caravaggio", "c. 1598", "Italy", "A youthful, sensuous depiction of the Roman god of wine."),
    ("The Ambassadors", "The Ambassadors (Holbein)", "Hans Holbein the Younger", "1533", "Germany", "Famous for its anamorphic skull hidden in the foreground."),
    ("Napoleon Crossing the Alps", "Napoleon Crossing the Alps", "Jacques-Louis David", "1801-1805", "France", "A heroic equestrian portrait commissioned to celebrate Napoleon's military campaign."),
    ("The Oath of the Horatii", "Oath of the Horatii", "Jacques-Louis David", "1784", "France", "A Neoclassical masterpiece depicting Roman brothers swearing loyalty before battle."),
    ("The Raft of the Medusa", "The Raft of the Medusa", "Théodore Géricault", "1818-1819", "France", "A monumental depiction of survivors of a shipwreck, a landmark of French Romanticism."),
    ("Bal du moulin de la Galette", "Bal du moulin de la Galette", "Pierre-Auguste Renoir", "1876", "France", "A joyful Impressionist scene of Parisians dancing in Montmartre."),
    ("Le Déjeuner sur l'herbe", "Le Déjeuner sur l'herbe", "Édouard Manet", "1863", "France", "A controversial painting of a nude woman picnicking with clothed men, a precursor to Impressionism."),
    ("Olympia", "Olympia (Manet)", "Édouard Manet", "1863", "France", "A confrontational reclining nude that scandalized the Paris Salon."),
    ("The Card Players", "The Card Players", "Paul Cézanne", "1890-1895", "France", "A series of paintings of Provençal peasants playing cards, foundational to Cubism's development."),
    ("Mont Sainte-Victoire", "Mont Sainte-Victoire (Cézanne)", "Paul Cézanne", "1882-1906", "France", "A series of landscapes exploring the mountain near Cézanne's studio."),
    ("Sunflowers", "Sunflowers (Van Gogh series)", "Vincent van Gogh", "1888-1889", "Netherlands/France", "A series of still-life paintings of sunflowers in a vase, among van Gogh's most beloved works."),
    ("Café Terrace at Night", "Café Terrace at Night", "Vincent van Gogh", "1888", "France", "A vividly lit café scene painted in Arles, France."),
    ("The Bedroom", "Bedroom in Arles", "Vincent van Gogh", "1888", "France", "Van Gogh's depiction of his own bedroom in the Yellow House at Arles."),
    ("Composition VII", "Composition VII", "Wassily Kandinsky", "1913", "Russia", "Considered one of the most complex abstract paintings Kandinsky ever created."),
    ("Black Square", "Black Square", "Kazimir Malevich", "1915", "Russia/Ukraine", "A founding work of Suprematism and radical geometric abstraction."),
    ("The Dance", "The Dance (Matisse)", "Henri Matisse", "1909-1910", "France", "Five dancing figures rendered in flat vivid color, an icon of Fauvism."),
    ("Les Demoiselles d'Avignon", "Les Demoiselles d'Avignon", "Pablo Picasso", "1907", "Spain", "A radical, fragmented depiction of five women that helped launch Cubism."),
    ("Girl Before a Mirror", "Girl Before a Mirror", "Pablo Picasso", "1932", "Spain", "A Cubist meditation on youth, mortality, and self-reflection."),
    ("The Weeping Woman", "The Weeping Woman", "Pablo Picasso", "1937", "Spain", "A companion piece to Guernica, exploring grief through Cubist fragmentation."),
    ("Composition with Red Blue and Yellow", "Composition II in Red, Blue, and Yellow", "Piet Mondrian", "1930", "Netherlands", "A defining example of De Stijl abstraction using primary colors and black grid lines."),
    ("Nude Descending a Staircase, No. 2", "Nude Descending a Staircase, No. 2", "Marcel Duchamp", "1912", "France", "A Cubo-Futurist depiction of motion that scandalized the 1913 Armory Show in New York."),
    ("The Son of Man", "The Son of Man", "René Magritte", "1964", "Belgium", "A self-portrait with a green apple obscuring the face, an icon of Surrealism."),
    ("The Treachery of Images", "The Treachery of Images", "René Magritte", "1929", "Belgium", "Famous for the caption 'Ceci n'est pas une pipe' ('This is not a pipe')."),
    ("The Elephants", "The Elephants (Dalí)", "Salvador Dalí", "1948", "Spain", "Surreal elephants with impossibly thin, elongated legs."),
    ("Autumn Rhythm", "Autumn Rhythm (Number 30)", "Jackson Pollock", "1950", "United States", "A monumental drip painting exemplifying Abstract Expressionism."),
    ("No. 5, 1948", "No. 5, 1948", "Jackson Pollock", "1948", "United States", "One of the most famous (and, at sale, most expensive) drip paintings ever made."),
    ("Marilyn Diptych", "Marilyn Diptych", "Andy Warhol", "1962", "United States", "Fifty repeated silkscreen images of Marilyn Monroe, an icon of Pop Art."),
    ("Campbell's Soup Cans", "Campbell's Soup Cans", "Andy Warhol", "1962", "United States", "Thirty-two canvases of soup cans that redefined what could be considered fine art."),
    ("Whaam!", "Whaam!", "Roy Lichtenstein", "1963", "United States", "A comic-book-style painting of a fighter plane attack, a Pop Art landmark."),
    ("Drowning Girl", "Drowning Girl", "Roy Lichtenstein", "1963", "United States", "A Ben-Day dot painting adapting a comic-book panel into fine art."),
    ("Broadway Boogie Woogie", "Broadway Boogie Woogie", "Piet Mondrian", "1942-1943", "Netherlands/United States", "A late Mondrian work reflecting the energy of New York City and jazz."),
    ("Number 1A, 1948", "Number 1A, 1948", "Jackson Pollock", "1948", "United States", "Includes Pollock's own handprints alongside his signature drip technique."),
    ("The Two Fridas", "The Two Fridas", "Frida Kahlo", "1939", "Mexico", "A double self-portrait exploring identity, heritage, and heartbreak."),
    ("Self-Portrait with Thorn Necklace and Hummingbird", "Self-Portrait with Thorn Necklace and Hummingbird", "Frida Kahlo", "1940", "Mexico", "One of Kahlo's most reproduced self-portraits."),
    ("Man at the Crossroads", "Man at the Crossroads", "Diego Rivera", "1933", "Mexico", "A monumental mural (destroyed and later recreated) exploring industry, science, and socialism."),
    ("Dance at Le Moulin de la Galette (reprise)", "Bal du moulin de la Galette", "Pierre-Auguste Renoir", "1876", "France", "One of Impressionism's largest and most celebrated compositions."),
    ("The Luncheon of the Boating Party", "Luncheon of the Boating Party", "Pierre-Auguste Renoir", "1880-1881", "France", "A joyful Impressionist gathering of friends on a terrace overlooking the Seine."),
    ("A Bar at the Folies-Bergère", "A Bar at the Folies-Bergère", "Édouard Manet", "1882", "France", "Manet's final major work, celebrated for its ambiguous mirror reflection."),
    ("The Fall of Icarus", "Landscape with the Fall of Icarus", "Pieter Bruegel the Elder", "c. 1560", "Netherlands", "Icarus's tiny legs are barely visible in a vast, indifferent landscape."),
    ("The Tower of Babel", "The Tower of Babel (Bruegel)", "Pieter Bruegel the Elder", "1563", "Netherlands", "A sweeping depiction of the biblical tower, celebrated for its architectural detail."),
    ("Hunters in the Snow", "Hunters in the Snow", "Pieter Bruegel the Elder", "1565", "Netherlands", "A winter landscape considered one of the greatest in Western art."),
    ("The Milkmaid", "The Milkmaid (Vermeer)", "Johannes Vermeer", "c. 1658", "Netherlands", "A quietly luminous depiction of domestic labor."),
    ("View of Delft", "View of Delft", "Johannes Vermeer", "c. 1660-1661", "Netherlands", "A rare Vermeer cityscape, praised by Proust as one of the most beautiful paintings in the world."),
    ("Self-Portrait with Two Circles", "Self-Portrait with Two Circles", "Rembrandt", "c. 1665-1669", "Netherlands", "One of Rembrandt's final and most contemplative self-portraits."),
    ("Danaë", "Danaë (Rembrandt)", "Rembrandt", "1636", "Netherlands", "A mythological nude celebrated for its warm, luminous handling of light."),
]

FAMOUS_SCULPTURES = [
    ("David", "David (Michelangelo)", "Michelangelo", "1501-1504", "Italy", "A 17-foot marble masterpiece depicting the biblical hero, an icon of Renaissance sculpture."),
    ("Venus de Milo", "Venus de Milo", "Alexandros of Antioch (attributed)", "c. 150-125 BCE", "Greece", "An armless marble Aphrodite discovered on the island of Milos, now in the Louvre."),
    ("The Thinker", "The Thinker", "Auguste Rodin", "1880-1904", "France", "A contemplative bronze figure, one of the most recognizable sculptures in the world."),
    ("The Kiss (Rodin)", "The Kiss (Rodin)", "Auguste Rodin", "1882", "France", "A marble embrace celebrated for its sensuous naturalism."),
    ("Pietà", "Pietà (Michelangelo)", "Michelangelo", "1498-1499", "Italy", "The Virgin Mary cradling the body of Christ, housed in St. Peter's Basilica."),
    ("Discobolus", "Discobolus", "Myron (original, lost; Roman copies survive)", "c. 460-450 BCE", "Greece", "The Discus Thrower, capturing an athlete at the peak of motion."),
    ("Winged Victory of Samothrace", "Winged Victory of Samothrace", "Unknown", "c. 200-190 BCE", "Greece", "A dramatic Hellenistic sculpture of the goddess Nike, displayed atop the Louvre's grand staircase."),
    ("Laocoön and His Sons", "Laocoön and His Sons", "Agesander, Athenodoros, and Polydorus", "1st century BCE-1st century CE", "Greece/Rome", "A dramatic depiction of a Trojan priest and his sons attacked by sea serpents."),
    ("Statue of Liberty", "Statue of Liberty", "Frédéric Auguste Bartholdi", "1886", "France/United States", "A gift from France to the United States, one of the most recognized statues in the world."),
    ("Christ the Redeemer", "Christ the Redeemer (statue)", "Paul Landowski", "1931", "Brazil", "An Art Deco statue overlooking Rio de Janeiro, one of the New Seven Wonders of the World."),
    ("The Little Mermaid", "The Little Mermaid (statue)", "Edvard Eriksen", "1913", "Denmark", "A bronze statue in Copenhagen harbor inspired by Hans Christian Andersen's fairy tale."),
    ("Moai", "Moai", "Rapa Nui people", "c. 1250-1500", "Easter Island (Chile)", "Monolithic stone figures carved by the Rapa Nui people, iconic symbols of Easter Island."),
    ("The Terracotta Army", "Terracotta Army", "Craftsmen of Qin Shi Huang", "c. 210 BCE", "China", "Thousands of life-sized clay soldiers buried to guard China's first emperor in the afterlife."),
    ("Bust of Nefertiti", "Nefertiti Bust", "Thutmose (sculptor)", "c. 1345 BCE", "Egypt", "One of the most famous surviving portraits of the ancient world, depicting the Egyptian queen."),
    ("The Great Sphinx of Giza", "Great Sphinx of Giza", "Ancient Egyptians", "c. 2558-2532 BCE", "Egypt", "A limestone statue with a lion's body and a human head, guarding the Giza pyramid complex."),
    ("Michelangelo's Moses", "Moses (Michelangelo)", "Michelangelo", "1513-1515", "Italy", "A powerful marble depiction of the biblical prophet, part of the tomb of Pope Julius II."),
    ("Apollo Belvedere", "Apollo Belvedere", "Leochares (attributed, Roman copy)", "2nd century CE (Roman copy of Greek original)", "Greece/Rome", "Long considered the epitome of male beauty in classical sculpture."),
    ("The Dying Gaul", "Dying Gaul", "Epigonus (attributed, Roman copy)", "3rd century BCE (Roman copy)", "Greece/Rome", "A Hellenistic sculpture depicting a mortally wounded Celtic warrior."),
    ("Farnese Hercules", "Farnese Hercules", "Glykon (Roman copy after Lysippos)", "3rd century CE (Roman copy)", "Greece/Rome", "A monumental depiction of Hercules resting after his labors."),
    ("Perseus with the Head of Medusa", "Perseus with the Head of Medusa (Cellini)", "Benvenuto Cellini", "1545-1554", "Italy", "A bronze Renaissance masterpiece displayed in the Loggia dei Lanzi, Florence."),
    ("The Rape of Proserpina", "The Rape of Proserpina", "Gian Lorenzo Bernini", "1621-1622", "Italy", "A Baroque marble group famous for the illusion of soft flesh yielding under fingers."),
    ("Apollo and Daphne", "Apollo and Daphne", "Gian Lorenzo Bernini", "1622-1625", "Italy", "Captures the instant of Daphne transforming into a laurel tree to escape Apollo."),
    ("Ecstasy of Saint Teresa", "Ecstasy of Saint Teresa", "Gian Lorenzo Bernini", "1647-1652", "Italy", "A dramatic Baroque sculpture depicting a mystical vision described by Saint Teresa of Ávila."),
    ("Michelangelo's Bacchus", "Bacchus (Michelangelo)", "Michelangelo", "1496-1497", "Italy", "One of Michelangelo's earliest surviving large-scale sculptures."),
    ("The Motherland Calls", "The Motherland Calls", "Yevgeny Vuchetich", "1967", "Russia", "One of the tallest statues in the world, commemorating the Battle of Stalingrad."),
    ("Spring Temple Buddha", "Spring Temple Buddha", "Modern craftsmen", "2002-2008", "China", "One of the tallest statues in the world, depicting Vairocana Buddha."),
    ("Leshan Giant Buddha", "Leshan Giant Buddha", "Hai Tong (commissioned)", "713-803 CE", "China", "A colossal stone Buddha carved into a cliff face, the tallest pre-modern statue in the world."),
    ("The Great Buddha of Kamakura", "Great Buddha of Kamakura", "Ono Goroemon (attributed)", "1252", "Japan", "A monumental bronze statue of Amida Buddha in Kamakura, Japan."),
    ("Angel of the North", "Angel of the North", "Antony Gormley", "1998", "United Kingdom", "A contemporary steel sculpture overlooking Gateshead, one of the UK's most viewed artworks."),
    ("Cloud Gate", "Cloud Gate", "Anish Kapoor", "2006", "United States", "Known as 'The Bean', a mirrored steel sculpture in Chicago's Millennium Park."),
    ("Balloon Dog", "Balloon Dog", "Jeff Koons", "1994-2000", "United States", "A stainless-steel sculpture resembling a balloon animal, an icon of contemporary art."),
    ("Nike of Samothrace (reprise)", "Winged Victory of Samothrace", "Unknown", "c. 200-190 BCE", "Greece", "Also displayed as the Winged Victory of Samothrace."),
    ("Boy with Thorn", "Spinario", "Unknown (Hellenistic/Roman)", "1st century BCE", "Greece/Rome", "A famous bronze depicting a boy pulling a thorn from his foot."),
    ("The Charioteer of Delphi", "Charioteer of Delphi", "Unknown", "c. 478-474 BCE", "Greece", "A rare surviving bronze from Classical Greece, praised for its serene expression."),
    ("Colossi of Memnon", "Colossi of Memnon", "Ancient Egyptians (Amenhotep III)", "c. 1350 BCE", "Egypt", "Two massive stone statues guarding the ruined mortuary temple of Amenhotep III."),
    ("Statue of Zeus at Olympia", "Statue of Zeus at Olympia", "Phidias", "c. 435 BCE", "Greece", "One of the Seven Wonders of the Ancient World, a colossal gold-and-ivory statue (now lost)."),
    ("Colossus of Rhodes", "Colossus of Rhodes", "Chares of Lindos", "c. 280 BCE", "Greece", "A giant bronze statue of the sun god Helios and one of the Seven Wonders of the Ancient World (now lost)."),
    ("Trajan's Column", "Trajan's Column", "Apollodorus of Damascus", "113 CE", "Italy (Rome)", "A monumental column with a spiraling relief depicting the Roman-Dacian wars."),
    ("Equestrian Statue of Marcus Aurelius", "Equestrian Statue of Marcus Aurelius", "Unknown", "c. 175 CE", "Italy (Rome)", "One of the few surviving bronze equestrian statues from antiquity."),
    ("The Kiss (Brancusi)", "The Kiss (Brâncuși)", "Constantin Brâncuși", "1907-1908", "Romania/France", "A radically simplified modernist depiction of an embracing couple."),
    ("Bird in Space", "Bird in Space", "Constantin Brâncuși", "1923", "Romania/France", "An abstract bronze form so minimal it sparked a famous US customs court case over 'what is art'."),
    ("Unique Forms of Continuity in Space", "Unique Forms of Continuity in Space", "Umberto Boccioni", "1913", "Italy", "A Futurist bronze capturing a striding figure in motion, later used on Italy's euro coin."),
    ("Woman I", "Woman I", "Willem de Kooning", "1950-1952", "Netherlands/United States", "An aggressive, gestural Abstract Expressionist painting-sculpture hybrid figure."),
    ("The Burghers of Calais", "The Burghers of Calais", "Auguste Rodin", "1884-1889", "France", "Commemorates six citizens who offered their lives to save their city during the Hundred Years' War."),
    ("The Gates of Hell", "The Gates of Hell", "Auguste Rodin", "1880-1917", "France", "A monumental bronze portal inspired by Dante's Inferno, containing 'The Thinker' among its figures."),
    ("Christ of the Abyss", "Christ of the Abyss", "Guido Galletti", "1954", "Italy", "An underwater bronze statue of Christ off the Italian coast."),
    ("The Awakening", "The Awakening (statue)", "J. Seward Johnson Jr.", "1980", "United States", "A giant figure appearing to emerge from the earth, now displayed in Maryland."),
    ("Mount Rushmore", "Mount Rushmore", "Gutzon Borglum", "1927-1941", "United States", "Sixty-foot sculptures of four US presidents carved into a South Dakota mountainside."),
    ("Crazy Horse Memorial", "Crazy Horse Memorial", "Korczak Ziolkowski", "1948-present (ongoing)", "United States", "An in-progress mountain carving honoring the Lakota leader Crazy Horse."),
]

EGYPTIAN_ARTIFACTS = [
    ("Rosetta Stone", "Rosetta Stone", "Ancient Egyptians", "196 BCE", "Egypt", "A granodiorite stele whose trilingual inscription unlocked the decipherment of Egyptian hieroglyphs."),
    ("Tutankhamun's Death Mask", "Mask of Tutankhamun", "Ancient Egyptians", "c. 1323 BCE", "Egypt", "A solid gold funerary mask, among the most famous archaeological objects ever found."),
    ("The Great Pyramid of Giza", "Great Pyramid of Giza", "Ancient Egyptians (Khufu)", "c. 2560 BCE", "Egypt", "The oldest and only largely intact Wonder of the Ancient World."),
    ("Book of the Dead of Ani", "Book of the Dead of Hunefer", "Ancient Egyptians", "c. 1275 BCE", "Egypt", "An illustrated funerary papyrus depicting the weighing of the heart ritual."),
    ("Narmer Palette", "Narmer Palette", "Ancient Egyptians", "c. 3100 BCE", "Egypt", "A ceremonial slate palette often cited as depicting the unification of Upper and Lower Egypt."),
    ("Bust of Ramesses II (Younger Memnon)", "Younger Memnon", "Ancient Egyptians", "c. 1250 BCE", "Egypt", "A colossal granite head of Ramesses II, held at the British Museum."),
    ("Canopic Jars of Tutankhamun", "Canopic jar", "Ancient Egyptians", "c. 1323 BCE", "Egypt", "Ritual vessels used to preserve a pharaoh's internal organs for the afterlife."),
    ("The Great Sphinx (reprise)", "Great Sphinx of Giza", "Ancient Egyptians", "c. 2558-2532 BCE", "Egypt", "The largest monolithic statue in the world."),
    ("Meidum Geese", "Meidum Geese", "Ancient Egyptians", "c. 2600 BCE", "Egypt", "One of the earliest and finest examples of ancient Egyptian painting."),
    ("Statue of Khafre", "Khafra statue", "Ancient Egyptians", "c. 2570 BCE", "Egypt", "A diorite statue of the pharaoh who commissioned the Second Pyramid of Giza."),
    ("Seated Scribe", "Seated Scribe", "Ancient Egyptians", "c. 2620-2500 BCE", "Egypt", "A vividly painted limestone statue in the Louvre, prized for its lifelike inlaid eyes."),
    ("Bust of Akhenaten", "Amarna art", "Ancient Egyptians", "c. 1350 BCE", "Egypt", "Reflects the distinctive naturalistic style of the Amarna Period."),
    ("Golden Throne of Tutankhamun", "Golden Throne of Tutankhamun", "Ancient Egyptians", "c. 1332-1323 BCE", "Egypt", "An elaborately decorated ceremonial throne found in Tutankhamun's tomb."),
    ("The Palermo Stone", "Palermo Stone", "Ancient Egyptians", "c. 2392-2283 BCE", "Egypt", "One of the earliest king lists, recording annals of early Egyptian rulers."),
    ("Colossi of Memnon (reprise)", "Colossi of Memnon", "Ancient Egyptians", "c. 1350 BCE", "Egypt", "Two massive seated statues that once guarded a ruined mortuary temple."),
    ("Deir el-Bahari Temple Reliefs", "Mortuary Temple of Hatshepsut", "Ancient Egyptians", "c. 1479-1458 BCE", "Egypt", "Elaborate relief carvings from Queen Hatshepsut's mortuary temple."),
]

GREEK_ROMAN_ARTIFACTS = [
    ("Elgin Marbles", "Elgin Marbles", "Phidias (workshop)", "c. 447-432 BCE", "Greece", "Sculptures from the Parthenon, a subject of long-running restitution debate between Greece and the UK."),
    ("Antikythera Mechanism", "Antikythera mechanism", "Ancient Greeks", "c. 150-100 BCE", "Greece", "An astonishingly advanced ancient analog computer used to predict astronomical positions."),
    ("Portland Vase", "Portland Vase", "Ancient Romans", "1-25 CE", "Italy", "A cameo-glass masterpiece considered one of the finest surviving pieces of Roman glasswork."),
    ("Warren Cup", "Warren Cup", "Ancient Romans", "5-15 CE", "Italy", "A silver Roman drinking cup notable for its detailed relief decoration."),
    ("Alexander Mosaic", "Alexander Mosaic", "Ancient Romans (Pompeii)", "c. 100 BCE", "Italy", "A floor mosaic from Pompeii depicting the Battle of Issus between Alexander and Darius III."),
    ("Riace Bronzes", "Riace bronzes", "Ancient Greeks", "c. 460-450 BCE", "Greece/Italy", "Two extraordinarily well-preserved bronze warrior statues recovered from the sea off Italy."),
    ("The Parthenon Frieze", "Parthenon Frieze", "Phidias (workshop)", "c. 443-437 BCE", "Greece", "A continuous relief depicting the Panathenaic procession, part of the Elgin Marbles collection."),
    ("Peplos Kore", "Peplos Kore", "Ancient Greeks", "c. 530 BCE", "Greece", "An Archaic Greek statue notable for traces of its original paint."),
    ("Kritios Boy", "Kritios Boy", "Ancient Greeks (Kritios, attributed)", "c. 480 BCE", "Greece", "A pivotal early Classical statue marking the shift from Archaic rigidity to naturalism."),
    ("Venus de Milo (reprise)", "Venus de Milo", "Alexandros of Antioch (attributed)", "c. 150-125 BCE", "Greece", "One of the most famous surviving works of ancient Greek sculpture."),
    ("The Barberini Faun", "Barberini Faun", "Unknown (Hellenistic)", "c. 220 BCE", "Greece", "A Hellenistic marble of a sleeping satyr, prized for its dynamic pose."),
    ("The Pompeii Cave Canem Mosaic", "Cave canem", "Ancient Romans (Pompeii)", "1st century CE", "Italy", "A famous 'Beware of the Dog' mosaic from a Pompeii doorway."),
    ("Ara Pacis", "Ara Pacis", "Ancient Romans", "13-9 BCE", "Italy", "The Altar of Augustan Peace, celebrated for its finely carved processional reliefs."),
    ("Column of Marcus Aurelius", "Column of Marcus Aurelius", "Ancient Romans", "c. 193 CE", "Italy", "A spiraling relief column commemorating Marcus Aurelius's military campaigns."),
    ("Boscoreale Treasure", "Boscoreale Treasure", "Ancient Romans", "1st century BCE-1st century CE", "Italy", "A hoard of exquisite Roman silverware buried by the eruption of Vesuvius."),
    ("Lycurgus Cup", "Lycurgus Cup", "Ancient Romans", "4th century CE", "Italy/Egypt", "A dichroic glass cup that changes color depending on the light passing through it."),
]

MESOPOTAMIAN_ARTIFACTS = [
    ("Code of Hammurabi Stele", "Code of Hammurabi", "Babylonians", "c. 1754 BCE", "Iraq (Babylon)", "One of the earliest and most complete written legal codes, inscribed on a basalt stele."),
    ("Standard of Ur", "Standard of Ur", "Sumerians", "c. 2600 BCE", "Iraq (Ur)", "A wooden box inlaid with shell and lapis lazuli depicting war and peace scenes."),
    ("Ishtar Gate", "Ishtar Gate", "Babylonians (Nebuchadnezzar II)", "c. 575 BCE", "Iraq (Babylon)", "A glazed-brick gate decorated with dragons and bulls, one of ancient Babylon's grandest monuments."),
    ("Lamassu of Nineveh", "Lamassu", "Assyrians", "c. 700 BCE", "Iraq", "Colossal human-headed winged bull statues that guarded Assyrian palace gates."),
    ("The Burney Relief", "Burney Relief", "Babylonians/Sumerians", "c. 1800-1750 BCE", "Iraq", "A terracotta plaque depicting a winged goddess, possibly Ishtar or Lilitu."),
    ("Epic of Gilgamesh Tablets", "Epic of Gilgamesh", "Sumerians/Babylonians", "c. 2100-1200 BCE", "Iraq", "Cuneiform tablets preserving one of the oldest surviving works of literature."),
    ("Royal Game of Ur", "Royal Game of Ur", "Sumerians", "c. 2600-2400 BCE", "Iraq (Ur)", "One of the oldest known board games, discovered in the royal tombs of Ur."),
    ("Statue of Gudea", "Gudea", "Sumerians", "c. 2144-2124 BCE", "Iraq (Lagash)", "Diorite statues of a Sumerian ruler, prized for their fine craftsmanship."),
    ("Cyrus Cylinder", "Cyrus Cylinder", "Persians (Achaemenid)", "c. 539 BCE", "Iran/Iraq", "A clay cylinder sometimes described as an early declaration of human rights."),
    ("Behistun Inscription", "Behistun Inscription", "Persians (Darius I)", "c. 522-486 BCE", "Iran", "A trilingual rock relief that was key to deciphering cuneiform script."),
]

ASIAN_ART_ARTIFACTS = [
    ("Terracotta Army (reprise)", "Terracotta Army", "Craftsmen of Qin Shi Huang", "c. 210 BCE", "China", "Thousands of individually detailed clay soldiers guarding China's first emperor."),
    ("Simuwu Ding", "Simuwu ding", "Shang dynasty craftsmen", "c. 1300-1046 BCE", "China", "The heaviest surviving piece of ancient Chinese bronze ware."),
    ("Jade Burial Suit", "Jade burial suit", "Han dynasty craftsmen", "2nd century BCE", "China", "Suits of jade plates sewn with gold or silver thread, believed to preserve the body for eternity."),
    ("Along the River During the Qingming Festival", "Along the River During the Qingming Festival", "Zhang Zeduan", "12th century", "China", "A panoramic handscroll depicting daily life in the Song-dynasty capital."),
    ("Dunhuang Diamond Sutra", "Diamond Sutra", "Tang dynasty printers", "868 CE", "China", "The world's oldest dated, complete printed book, found in the Mogao Caves."),
    ("Longmen Grottoes Buddhas", "Longmen Grottoes", "Northern Wei to Tang dynasty craftsmen", "493-907 CE", "China", "Tens of thousands of Buddhist statues carved into limestone cliffs."),
    ("Great Wall of China (Badaling section)", "Great Wall of China", "Various Chinese dynasties", "7th century BCE-17th century CE", "China", "A vast fortification system, among the most recognized structures in the world."),
    ("Forbidden City Throne", "Hall of Supreme Harmony", "Ming dynasty craftsmen", "1420", "China", "The imperial throne hall at the heart of Beijing's Forbidden City."),
    ("Ru Ware Brush Washer", "Ru ware", "Song dynasty potters", "c. 1086-1125", "China", "Among the rarest and most prized ceramics in Chinese art history."),
    ("The Great Buddha of Kamakura (reprise)", "Great Buddha of Kamakura", "Ono Goroemon (attributed)", "1252", "Japan", "A monumental bronze Amida Buddha in Kamakura, Japan."),
    ("Himeji Castle", "Himeji Castle", "Japanese feudal builders", "1333 (rebuilt 1601-1609)", "Japan", "Japan's best-preserved feudal-era castle, known as the 'White Heron Castle'."),
    ("The Great Wave (reprise)", "The Great Wave off Kanagawa", "Hokusai", "c. 1831", "Japan", "The most iconic work of Japanese ukiyo-e printmaking."),
    ("Golden Pavilion (Kinkaku-ji)", "Kinkaku-ji", "Ashikaga Yoshimitsu (commissioned)", "1397", "Japan", "A Zen Buddhist temple in Kyoto covered in gold leaf."),
    ("Himeji Byōbu Screens", "Byōbu", "Various Japanese artists", "16th-19th centuries", "Japan", "Folding screens that became a major format for Japanese painting."),
    ("Haniwa Figures", "Haniwa", "Kofun-period craftsmen", "3rd-6th centuries CE", "Japan", "Terracotta figures placed around ancient Japanese burial mounds."),
    ("Katana of the Kamakura Masters", "Katana", "Japanese swordsmiths", "13th century onward", "Japan", "Legendary Japanese swords prized for their folded-steel craftsmanship."),
    ("Celadon Ware of Goryeo", "Goryeo celadon", "Goryeo-dynasty potters", "10th-14th centuries", "Korea", "Renowned jade-green glazed ceramics considered among Korea's finest artistic achievements."),
    ("Hunminjeongeum Manuscript", "Hunminjeongeum", "King Sejong the Great", "1446", "Korea", "The original document introducing Hangul, the Korean alphabet."),
    ("Cheomseongdae Observatory", "Cheomseongdae", "Silla-dynasty astronomers", "7th century CE", "Korea", "One of the oldest surviving astronomical observatories in East Asia."),
    ("Angkor Wat Reliefs", "Angkor Wat", "Khmer Empire craftsmen", "12th century", "Cambodia", "Extensive bas-relief carvings depicting Hindu epics at the world's largest religious monument."),
    ("Bayon Face Towers", "Bayon", "Khmer Empire craftsmen", "late 12th-early 13th century", "Cambodia", "Towers carved with enormous serene stone faces at Angkor Thom."),
    ("Borobudur Reliefs", "Borobudur", "Sailendra dynasty craftsmen", "8th-9th century", "Indonesia", "The world's largest Buddhist temple, decorated with thousands of relief panels."),
    ("Emerald Buddha", "Emerald Buddha", "Unknown (Lanna artisans, attributed)", "14th-15th century", "Thailand", "Thailand's most sacred Buddha image, carved from a single block of jade."),
    ("Shwedagon Pagoda Stupa", "Shwedagon Pagoda", "Mon and Burmese builders", "6th century CE onward", "Myanmar", "A gilded stupa said to enshrine relics of four Buddhas."),
]

SOUTH_ASIAN_ARTIFACTS = [
    ("Pashupati Seal", "Pashupati seal", "Indus Valley Civilization", "c. 2500-2000 BCE", "Pakistan/India", "A steatite seal from the Indus Valley Civilization depicting a seated horned figure."),
    ("Dancing Girl of Mohenjo-daro", "Dancing Girl (sculpture)", "Indus Valley Civilization", "c. 2300-1750 BCE", "Pakistan", "A small bronze figure celebrated as one of the earliest known lost-wax castings."),
    ("Great Bath of Mohenjo-daro", "Great Bath (Mohenjo-daro)", "Indus Valley Civilization", "c. 2500 BCE", "Pakistan", "One of the earliest public water tanks in the ancient world."),
    ("Lion Capital of Ashoka", "Lion Capital of Ashoka", "Mauryan craftsmen (Ashoka)", "c. 250 BCE", "India (Sarnath)", "The capital of a column erected by Emperor Ashoka, now India's national emblem."),
    ("Sanchi Stupa", "Sanchi Stupa", "Mauryan and Sunga dynasties", "3rd century BCE onward", "India", "One of the oldest stone structures in India, an important Buddhist monument."),
    ("Ajanta Cave Paintings", "Ajanta Caves", "Buddhist monks and artisans", "2nd century BCE-6th century CE", "India", "Rock-cut Buddhist cave temples famous for their vivid murals."),
    ("Ellora Kailasa Temple", "Kailasa Temple, Ellora", "Rashtrakuta dynasty craftsmen", "8th century CE", "India", "A monolithic temple carved from a single rock, one of the largest such structures in the world."),
    ("Konark Sun Temple Wheels", "Konark Sun Temple", "Eastern Ganga dynasty craftsmen", "13th century", "India", "A temple designed as a colossal chariot with elaborately carved stone wheels."),
    ("Bronze Nataraja of Chola Dynasty", "Nataraja", "Chola dynasty bronze casters", "c. 10th-12th century", "India", "Iconic bronze depictions of Shiva as the cosmic dancer, celebrated worldwide as masterpieces of Indian art."),
    ("Taj Mahal", "Taj Mahal", "Ustad Ahmad Lahauri (chief architect)", "1632-1653", "India", "An ivory-white marble mausoleum, one of the most celebrated buildings in the world."),
    ("Red Fort Peacock Throne (historical)", "Peacock Throne", "Mughal craftsmen (Shah Jahan)", "1635", "India", "A legendary jewel-encrusted Mughal throne, later lost to Persian invasion."),
    ("Qutb Minar", "Qutb Minar", "Qutb al-Din Aibak (commissioned)", "1193 onward", "India", "The tallest brick minaret in the world, a landmark of early Indo-Islamic architecture."),
    ("Buddhas of Bamiyan (historical)", "Buddhas of Bamiyan", "Kushan-era craftsmen", "6th century CE", "Afghanistan", "Colossal rock-cut Buddha statues destroyed in 2001, mourned as an immense cultural loss."),
    ("Begram Ivories", "Begram ivories", "Kushan-era artisans", "1st-2nd century CE", "Afghanistan", "Exquisite carved ivory panels found along the ancient Silk Road."),
]

ISLAMIC_ART_ARTIFACTS = [
    ("The Blue Qur'an", "Blue Qur'an", "Unknown (Abbasid/Fatimid era)", "9th-10th century", "Tunisia/Iraq", "A rare gold-on-indigo illuminated manuscript, among the most celebrated Qur'ans ever produced."),
    ("Ardabil Carpet", "Ardabil Carpet", "Maqsud of Kashan (attributed)", "1539-1540", "Iran", "One of the world's oldest and largest dated Islamic carpets."),
    ("Alhambra Palace Tilework", "Alhambra", "Nasrid dynasty craftsmen", "13th-14th century", "Spain", "A Moorish palace complex celebrated for its intricate geometric tile and stucco work."),
    ("Dome of the Rock", "Dome of the Rock", "Umayyad craftsmen (Abd al-Malik)", "691-692 CE", "Jerusalem", "One of the oldest surviving works of Islamic architecture, renowned for its golden dome."),
    ("Great Mosque of Córdoba Mihrab", "Mezquita-Catedral de Córdoba", "Umayyad craftsmen", "8th-10th century", "Spain", "Famous for its forest of double-arched columns and richly decorated mihrab."),
    ("Süleymaniye Mosque", "Süleymaniye Mosque", "Mimar Sinan", "1550-1557", "Turkey", "A masterpiece of Ottoman architecture by the great architect Sinan."),
    ("Astrolabe of Ibn al-Sarraj", "Astrolabe", "Islamic astronomers/craftsmen", "13th-14th century", "Various (Islamic world)", "Precision brass instruments used for astronomy, navigation, and timekeeping."),
    ("Baptistère de Saint Louis", "Baptistère de Saint Louis", "Muhammad ibn al-Zayn", "c. 1320-1340", "Egypt/Syria (Mamluk)", "An intricately inlaid brass basin, one of the masterpieces of Mamluk metalwork."),
    ("Bahri Mamluk Qur'an of Sultan Baybars", "Baybars Qur'an", "Aydughdi ibn Abdallah al-Badri", "1304-1306", "Egypt", "A monumental seven-volume illuminated Qur'an from the Mamluk era."),
    ("Alcazar of Seville Tilework", "Alcázar of Seville", "Mudéjar craftsmen", "14th century onward", "Spain", "A royal palace blending Islamic and Christian architectural traditions."),
    ("Faisal Mosque", "Faisal Mosque", "Vedat Dalokay", "1976-1986", "Pakistan", "A modern landmark mosque known for its distinctive tent-like design."),
    ("Registan Ensemble", "Registan", "Timurid and Uzbek craftsmen", "15th-17th century", "Uzbekistan", "Three grand madrasas forming the heart of historic Samarkand."),
]

AFRICAN_ART_ARTIFACTS = [
    ("Benin Bronzes", "Benin Bronzes", "Edo craftsmen (Benin Kingdom)", "13th-16th century onward", "Nigeria", "Renowned brass and bronze plaques and sculptures from the Kingdom of Benin, subject of ongoing restitution efforts."),
    ("Ife Bronze Heads", "Ife art", "Yoruba craftsmen (Ife)", "12th-15th century", "Nigeria", "Extraordinarily naturalistic terracotta and bronze portrait heads from the ancient city of Ife."),
    ("Great Zimbabwe Ruins", "Great Zimbabwe", "Shona civilization builders", "11th-15th century", "Zimbabwe", "The largest ancient stone structure in sub-Saharan Africa, giving modern Zimbabwe its name."),
    ("Nok Terracotta Figures", "Nok culture", "Nok culture craftsmen", "c. 1500 BCE-500 CE", "Nigeria", "Among the earliest known sculptural traditions in sub-Saharan Africa."),
    ("Ashanti Golden Stool", "Golden Stool", "Ashanti craftsmen", "c. 1700", "Ghana", "The sacred symbol of the Ashanti nation's soul and authority."),
    ("Great Mosque of Djenné", "Great Mosque of Djenné", "Djenné craftsmen", "13th century (rebuilt 1907)", "Mali", "The largest mud-brick building in the world, an icon of Sudano-Sahelian architecture."),
    ("Lalibela Rock-Hewn Churches", "Rock-Hewn Churches, Lalibela", "Ethiopian craftsmen (King Lalibela)", "12th-13th century", "Ethiopia", "Eleven medieval monolithic churches carved directly into volcanic rock."),
    ("Axum Obelisks", "Obelisk of Axum", "Aksumite civilization", "c. 4th century CE", "Ethiopia", "Massive carved granite stelae marking royal graves of the ancient Kingdom of Aksum."),
    ("Dogon Kanaga Masks", "Dogon people", "Dogon craftsmen", "Traditional, ongoing", "Mali", "Ceremonial masks central to Dogon funerary and initiation rites."),
    ("Great Pyramid of Meroë", "Nubian pyramids", "Kingdom of Kush", "c. 300 BCE-300 CE", "Sudan", "Steep-sided pyramids built by the Nubian rulers of ancient Kush, more numerous than Egypt's."),
    ("Chokwe Mwana Pwo Mask", "Chokwe people", "Chokwe craftsmen", "Traditional, 19th-20th century", "Angola/DR Congo", "A ceremonial mask representing an idealized female ancestor."),
    ("Kongo Nkisi Nkondi Power Figures", "Nkisi", "Kongo craftsmen", "19th century", "DR Congo/Angola", "Wooden power figures studded with nails and blades, used in Kongo spiritual practice."),
]

PRECOLUMBIAN_NATIVE_AMERICAN_ARTIFACTS = [
    ("Aztec Sun Stone", "Aztec sun stone", "Aztec (Mexica) craftsmen", "c. 1502-1521", "Mexico", "A massive basalt disc long thought to be a calendar, now understood as a ceremonial monument."),
    ("Machu Picchu", "Machu Picchu", "Inca Empire builders", "c. 1450 CE", "Peru", "A 15th-century Inca citadel high in the Andes, one of the most iconic archaeological sites in the world."),
    ("Nazca Lines", "Nazca Lines", "Nazca culture", "c. 500 BCE-500 CE", "Peru", "Enormous geoglyphs etched into the desert, visible only from the air."),
    ("Chichen Itza (El Castillo)", "Chichen Itza", "Maya civilization", "c. 600-1200 CE", "Mexico", "A stepped pyramid dedicated to Kukulcán, one of the New Seven Wonders of the World."),
    ("Palenque Temple of Inscriptions", "Palenque", "Maya civilization", "7th century CE", "Mexico", "A Maya pyramid housing the tomb of King Pakal, discovered with an elaborately carved sarcophagus lid."),
    ("Tikal Temple I", "Tikal", "Maya civilization", "c. 732 CE", "Guatemala", "A towering Maya pyramid-temple rising above the rainforest canopy."),
    ("Moche Sipán Lord's Tomb Ornaments", "Lord of Sipán", "Moche civilization", "c. 100-300 CE", "Peru", "Elaborate gold and turquoise regalia from one of the richest tombs ever found in the Americas."),
    ("Paracas Textiles", "Paracas culture", "Paracas civilization", "c. 800-100 BCE", "Peru", "Extraordinarily well-preserved, intricately woven textiles used to wrap mummy bundles."),
    ("Olmec Colossal Heads", "Olmec colossal heads", "Olmec civilization", "c. 1200-900 BCE", "Mexico", "Giant carved basalt boulder heads, among the earliest monumental sculptures in the Americas."),
    ("Teotihuacan Pyramid of the Sun", "Pyramid of the Sun", "Teotihuacan civilization", "c. 100 CE", "Mexico", "One of the largest pyramids in Mesoamerica, part of the vast ancient city of Teotihuacan."),
    ("Quimbaya Gold Artifacts", "Quimbaya civilization", "Quimbaya civilization", "c. 300-1550 CE", "Colombia", "Finely worked gold ceremonial objects, some of the finest goldwork in the pre-Columbian Americas."),
    ("Muisca Raft (El Dorado)", "Muisca raft", "Muisca civilization", "c. 1200-1500 CE", "Colombia", "A small gold votive object depicting the ritual said to have inspired the legend of El Dorado."),
    ("Mississippian Birdman Tablet", "Mississippian culture", "Mississippian civilization", "c. 1200-1400 CE", "United States", "An engraved shell artifact from Cahokia, the largest pre-Columbian city north of Mexico."),
    ("Cliff Palace of Mesa Verde", "Cliff Palace", "Ancestral Puebloans", "c. 1190-1260 CE", "United States", "The largest cliff dwelling in North America, built by the Ancestral Puebloan people."),
    ("Chaco Canyon Great Houses", "Chaco Culture National Historical Park", "Ancestral Puebloans", "c. 850-1150 CE", "United States", "Monumental multi-story stone buildings at the center of Ancestral Puebloan civilization."),
    ("Haida Totem Poles", "Totem pole", "Haida people", "Traditional, 18th-19th century onward", "Canada", "Monumental carved cedar poles recording family lineage and stories among Pacific Northwest peoples."),
]

MANUSCRIPTS_DOCUMENTS = [
    ("Gutenberg Bible", "Gutenberg Bible", "Johannes Gutenberg", "c. 1454-1455", "Germany", "The first major book printed in Europe using movable metal type."),
    ("Book of Kells", "Book of Kells", "Celtic monks", "c. 800 CE", "Ireland/Scotland", "An illuminated manuscript of the four Gospels, celebrated for its intricate decoration."),
    ("Magna Carta", "Magna Carta", "King John and English barons", "1215", "England", "A foundational charter limiting royal power, influential on constitutional law worldwide."),
    ("Domesday Book", "Domesday Book", "Commissioned by William the Conqueror", "1086", "England", "A comprehensive survey of land and property in Norman England."),
    ("Declaration of Independence", "United States Declaration of Independence", "Thomas Jefferson (principal author)", "1776", "United States", "The founding document declaring the American colonies' independence from Britain."),
    ("United States Constitution", "Constitution of the United States", "Constitutional Convention delegates", "1787", "United States", "The supreme governing document of the United States, the oldest written national constitution still in use."),
    ("Codex Leicester", "Codex Leicester", "Leonardo da Vinci", "c. 1508-1510", "Italy", "A scientific notebook by Leonardo, later owned by Bill Gates, covering water, astronomy, and geology."),
    ("Voynich Manuscript", "Voynich manuscript", "Unknown", "early 15th century (est.)", "Central Europe", "A mysterious illustrated manuscript in an undeciphered writing system."),
    ("Lindisfarne Gospels", "Lindisfarne Gospels", "Eadfrith of Lindisfarne (attributed)", "c. 700 CE", "England", "An illuminated Latin manuscript of the Gospels, a masterpiece of Insular art."),
    ("Dead Sea Scrolls", "Dead Sea Scrolls", "Various Jewish scribes", "c. 3rd century BCE-1st century CE", "Israel/West Bank", "Ancient Jewish texts including the oldest known copies of the Hebrew Bible."),
    ("Diamond Sutra (reprise)", "Diamond Sutra", "Tang dynasty printers", "868 CE", "China", "The world's oldest complete dated printed book."),
    ("Bayeux Tapestry", "Bayeux Tapestry", "Anglo-Saxon or Norman embroiderers", "c. 1070s", "France/England", "A 70-meter embroidered narrative of the Norman Conquest of England."),
    ("Hunminjeongeum (reprise)", "Hunminjeongeum", "King Sejong the Great", "1446", "Korea", "The founding document of the Korean Hangul alphabet."),
    ("Egyptian Book of the Dead (reprise)", "Book of the Dead", "Ancient Egyptians", "c. 1550 BCE-50 BCE", "Egypt", "A collection of funerary texts intended to assist the deceased in the afterlife."),
    ("The Codex Mendoza", "Codex Mendoza", "Aztec scribes", "c. 1541", "Mexico", "A pictorial Aztec manuscript recording history, tribute, and daily life."),
    ("Papyrus of Ani", "Papyrus of Ani", "Ancient Egyptians", "c. 1250 BCE", "Egypt", "One of the largest and best-preserved Book of the Dead papyri."),
]

CROWN_JEWELS_AND_GEMS = [
    ("Crown Jewels of the United Kingdom", "Crown Jewels of the United Kingdom", "Various royal jewelers", "17th century onward", "United Kingdom", "Ceremonial regalia including crowns, orbs, and sceptres used at coronations."),
    ("Imperial State Crown", "Imperial State Crown", "Garrard & Co.", "1937", "United Kingdom", "Worn by the British monarch at the State Opening of Parliament, set with thousands of gems."),
    ("Koh-i-Noor Diamond", "Koh-i-Noor", "Unknown (Golconda mines, India)", "believed mined 13th century", "India", "One of the largest cut diamonds in the world, now set in a British crown, subject of ownership disputes."),
    ("Hope Diamond", "Hope Diamond", "Unknown (Kollur mine, India)", "17th century (cut)", "India/France", "A legendary deep-blue diamond associated with numerous myths of misfortune."),
    ("Cullinan Diamond", "Cullinan Diamond", "Unknown (discovered South Africa)", "1905 (discovered)", "South Africa", "The largest gem-quality rough diamond ever found, cut into several stones in the British Crown Jewels."),
    ("Fabergé Imperial Coronation Egg", "Fabergé egg", "Peter Carl Fabergé", "1897", "Russia", "One of the most celebrated of the Fabergé Imperial Easter Eggs made for the Russian Tsars."),
    ("Fabergé Winter Egg", "Fabergé egg", "Peter Carl Fabergé", "1913", "Russia", "An intricately carved rock-crystal egg from Fabergé's famous Imperial series."),
    ("French Crown Jewels", "French Crown Jewels", "Various royal jewelers", "16th-19th century", "France", "Historic royal regalia now largely displayed in the Louvre."),
    ("Iranian Crown Jewels", "Imperial Crown Jewels of Iran", "Various Persian/Iranian jewelers", "18th-20th century", "Iran", "One of the largest jewel collections in the world, including the Darya-i-Noor diamond."),
    ("Sancy Diamond", "Sancy", "Unknown (India, cut)", "c. 16th century", "India/France", "A historic pale yellow diamond that passed through French and English royal collections."),
    ("Regent Diamond", "Regent Diamond", "Unknown (India, cut)", "1698 (found)", "India/France", "Considered one of the purest and most beautiful diamonds in the world, displayed in the Louvre."),
    ("Topkapi Dagger", "Topkapi dagger", "Ottoman court jewelers", "1747", "Turkey", "An emerald-encrusted Ottoman ceremonial dagger, famed from the film 'Topkapi'."),
    ("Peacock Throne (historical, reprise)", "Peacock Throne", "Mughal craftsmen (Shah Jahan)", "1635", "India", "A legendary bejeweled Mughal throne, later carried off to Persia."),
]

PHOTOGRAPHS = [
    ("Migrant Mother", "Migrant Mother", "Dorothea Lange", "1936", "United States", "A defining image of the Great Depression, depicting a destitute mother of seven."),
    ("V-J Day in Times Square", "V-J Day in Times Square", "Alfred Eisenstaedt", "1945", "United States", "An iconic photograph of a sailor kissing a woman celebrating the end of World War II."),
    ("Earthrise", "Earthrise", "William Anders (Apollo 8)", "1968", "Space (photographed from lunar orbit)", "One of the most influential environmental photographs ever taken, showing Earth from the Moon."),
    ("The Blue Marble", "The Blue Marble", "Apollo 17 crew", "1972", "Space (photographed from lunar transit)", "A full-disk photograph of Earth that became an icon of the environmental movement."),
    ("Raising the Flag on Iwo Jima", "Raising the Flag on Iwo Jima", "Joe Rosenthal", "1945", "Japan (Iwo Jima)", "A Pulitzer Prize-winning photograph of US Marines raising a flag during World War II."),
    ("Tank Man", "Tank Man", "Jeff Widener (and others)", "1989", "China", "An anonymous man standing before a line of tanks near Tiananmen Square, a global symbol of civil resistance."),
    ("Lunch atop a Skyscraper", "Lunch atop a Skyscraper", "Unknown (Rockefeller Center photographers)", "1932", "United States", "Ironworkers eating lunch on a girder high above New York City."),
    ("Napalm Girl", "The Terror of War", "Nick Út", "1972", "Vietnam", "A Pulitzer Prize-winning photograph documenting the horror of the Vietnam War."),
    ("Guerrillero Heroico", "Guerrillero Heroico", "Alberto Korda", "1960", "Cuba", "A portrait of Che Guevara that became one of the most reproduced photographic images in history."),
    ("Dorothea Lange's White Angel Breadline", "White Angel Breadline", "Dorothea Lange", "1933", "United States", "An early Depression-era photograph documenting unemployment relief lines."),
    ("The Horse in Motion", "Sallie Gardner at a Gallop", "Eadweard Muybridge", "1878", "United States", "Pioneering stop-motion photography that settled a debate about horse locomotion."),
    ("First Photograph (View from the Window at Le Gras)", "View from the Window at Le Gras", "Nicéphore Niépce", "1826 or 1827", "France", "The oldest surviving photograph taken with a camera."),
    ("Pale Blue Dot", "Pale Blue Dot", "Voyager 1 (NASA)", "1990", "Space (photographed from beyond Saturn)", "A photograph of Earth as a tiny point of light, inspiring Carl Sagan's famous reflection on humanity's place in the cosmos."),
    ("Man on the Moon (Buzz Aldrin)", "Buzz Aldrin", "Neil Armstrong", "1969", "Moon", "One of the most iconic photographs from the Apollo 11 Moon landing."),
]

MONUMENTS_AND_LANDMARKS = [
    ("Eiffel Tower", "Eiffel Tower", "Gustave Eiffel", "1889", "France", "An iron lattice tower built for the 1889 World's Fair, now the symbol of Paris."),
    ("Stonehenge", "Stonehenge", "Neolithic Britons", "c. 3000-2000 BCE", "United Kingdom", "A prehistoric stone circle monument whose exact purpose remains debated."),
    ("Colosseum", "Colosseum", "Ancient Romans (Vespasian/Titus)", "70-80 CE", "Italy", "The largest amphitheater ever built, an enduring symbol of the Roman Empire."),
    ("Leaning Tower of Pisa", "Leaning Tower of Pisa", "Bonanno Pisano (attributed)", "1173-1372", "Italy", "A freestanding bell tower famous for its unintended tilt."),
    ("Golden Gate Bridge", "Golden Gate Bridge", "Joseph Strauss (chief engineer)", "1937", "United States", "One of the most photographed bridges in the world, spanning San Francisco Bay."),
    ("Sydney Opera House", "Sydney Opera House", "Jørn Utzon", "1973", "Australia", "A modernist masterpiece of expressionist architecture, a UNESCO World Heritage Site."),
    ("Big Ben and the Elizabeth Tower", "Big Ben", "Augustus Pugin (tower design)", "1859", "United Kingdom", "The Great Bell of the clock tower at the Palace of Westminster."),
    ("Petra Treasury", "Al-Khazneh", "Nabataeans", "c. 1st century CE", "Jordan", "A monumental facade carved directly into rose-colored rock in the ancient city of Petra."),
    ("Hagia Sophia", "Hagia Sophia", "Isidore of Miletus and Anthemius of Tralles", "537 CE", "Turkey", "A former cathedral and mosque, an architectural marvel that has influenced building for 1,500 years."),
    ("Neuschwanstein Castle", "Neuschwanstein Castle", "Eduard Riedel", "1869-1886", "Germany", "A 19th-century Bavarian castle that inspired Disney's Sleeping Beauty Castle."),
    ("Burj Khalifa", "Burj Khalifa", "Adrian Smith (SOM)", "2010", "United Arab Emirates", "The tallest building in the world, a modern architectural landmark."),
    ("Great Wall of China (reprise)", "Great Wall of China", "Various Chinese dynasties", "7th century BCE-17th century CE", "China", "A vast series of fortifications stretching thousands of kilometers."),
    ("Christ the Redeemer (reprise)", "Christ the Redeemer (statue)", "Paul Landowski", "1931", "Brazil", "An Art Deco statue overlooking Rio de Janeiro."),
    ("Moscow Kremlin and Red Square", "Moscow Kremlin", "Various Russian architects", "15th century onward", "Russia", "The historic fortified complex at the heart of Moscow."),
    ("Notre-Dame de Paris", "Notre-Dame de Paris", "Maurice de Sully (commissioned)", "1163-1345", "France", "A masterpiece of French Gothic architecture on the Île de la Cité."),
    ("St. Basil's Cathedral", "Saint Basil's Cathedral", "Barma and Postnik (attributed)", "1555-1561", "Russia", "A colorful onion-domed cathedral on Moscow's Red Square."),
    ("Alcatraz Island", "Alcatraz Island", "United States military/federal government", "1934-1963 (as federal prison)", "United States", "A former federal prison on an island in San Francisco Bay, now a historic site."),
    ("Empire State Building", "Empire State Building", "Shreve, Lamb & Harmon", "1931", "United States", "An Art Deco skyscraper that was the world's tallest building for nearly 40 years."),
    ("Mont Saint-Michel", "Mont-Saint-Michel", "Medieval Norman builders", "8th century onward", "France", "A tidal island abbey, one of France's most recognizable landmarks."),
    ("Potala Palace", "Potala Palace", "Tibetan builders (5th Dalai Lama)", "1645 onward", "Tibet (China)", "The former residence of the Dalai Lama, a monumental fortress-palace in Lhasa."),
]

MODERN_CONTEMPORARY_ART = [
    ("Fountain", "Fountain (Duchamp)", "Marcel Duchamp", "1917", "France", "A porcelain urinal signed 'R. Mutt', the founding work of conceptual readymade art."),
    ("The Persistence of Memory (reprise)", "The Persistence of Memory", "Salvador Dalí", "1931", "Spain", "Surrealist melting clocks, one of the most recognized images of the 20th century."),
    ("Composition VIII", "Composition VIII", "Wassily Kandinsky", "1923", "Russia", "A geometric abstraction reflecting Kandinsky's Bauhaus period."),
    ("Untitled (Skull)", "Untitled (Skull)", "Jean-Michel Basquiat", "1981", "United States", "A defining Neo-Expressionist work by one of the most influential American artists of the 1980s."),
    ("Flag", "Flag (Jasper Johns)", "Jasper Johns", "1954-1955", "United States", "A painting of the American flag that questioned the boundary between image and object."),
    ("Just What Is It That Makes Today's Homes So Different, So Appealing?", "Just What Is It That Makes Today's Homes So Different, So Appealing?", "Richard Hamilton", "1956", "United Kingdom", "Often cited as the first true work of Pop Art."),
    ("Spiral Jetty", "Spiral Jetty", "Robert Smithson", "1970", "United States", "A monumental earthwork spiral built from rock and earth in the Great Salt Lake."),
    ("The Physical Impossibility of Death in the Mind of Someone Living", "The Physical Impossibility of Death in the Mind of Someone Living", "Damien Hirst", "1991", "United Kingdom", "A tiger shark preserved in formaldehyde, an icon of the Young British Artists movement."),
    ("For the Love of God", "For the Love of God", "Damien Hirst", "2007", "United Kingdom", "A platinum cast of a human skull covered in diamonds."),
    ("Girl with Balloon", "Girl with Balloon", "Banksy", "2002", "United Kingdom", "One of the most recognized stencil works by the anonymous street artist Banksy."),
    ("Guernica (reprise)", "Guernica (Picasso)", "Pablo Picasso", "1937", "Spain", "A monumental anti-war painting, one of the most powerful political artworks of the 20th century."),
    ("Blue Poles", "Blue Poles", "Jackson Pollock", "1952", "United States", "A monumental drip painting, one of the most expensive paintings acquired by a public gallery when purchased by Australia."),
    ("Convergence", "Convergence (painting)", "Jackson Pollock", "1952", "United States", "A large-scale Abstract Expressionist drip painting."),
    ("Orange, Red, Yellow", "Orange, Red, Yellow", "Mark Rothko", "1961", "United States", "A luminous color-field painting by one of Abstract Expressionism's leading figures."),
    ("No. 61 (Rust and Blue)", "No. 61 (Rust and Blue)", "Mark Rothko", "1953", "United States", "A meditative color-field painting characteristic of Rothko's mature style."),
    ("Vir Heroicus Sublimis", "Vir Heroicus Sublimis", "Barnett Newman", "1950-1951", "United States", "A monumental color-field painting exploring the sublime through scale and color."),
    ("Interchange", "Interchange (painting)", "Willem de Kooning", "1955", "Netherlands/United States", "An Abstract Expressionist painting that became one of the most expensive paintings ever sold."),
    ("Les Femmes d'Alger", "Women of Algiers (Picasso)", "Pablo Picasso", "1955", "Spain", "One of a celebrated series reinterpreting Delacroix, which set auction records at sale."),
    ("Nafea Faa Ipoipo", "Nafea Faa Ipoipo", "Paul Gauguin", "1892", "France", "'When Will You Marry?', a Tahitian-period painting by Gauguin."),
    ("The Card Players (Cézanne, reprise)", "The Card Players", "Paul Cézanne", "1890-1895", "France", "A series exploring form and structure, foundational to Cubism."),
    ("Water Serpents II", "Water Serpents II", "Gustav Klimt", "1907", "Austria", "A golden, ornamental painting exemplifying Klimt's decorative Symbolist style."),
    ("Portrait of Adele Bloch-Bauer I", "Portrait of Adele Bloch-Bauer I", "Gustav Klimt", "1907", "Austria", "Known as 'The Woman in Gold', famously restituted to the sitter's heirs after decades in Austrian state hands."),
    ("Three Studies of Lucian Freud", "Three Studies of Lucian Freud", "Francis Bacon", "1969", "United Kingdom", "A triptych portrait that became one of the most expensive artworks ever sold at auction."),
    ("Study after Velázquez's Portrait of Pope Innocent X", "Study after Velázquez's Portrait of Pope Innocent X", "Francis Bacon", "1953", "United Kingdom", "A haunting reinterpretation of a Baroque papal portrait."),
    ("Nafea (reprise)", "Nafea Faa Ipoipo", "Paul Gauguin", "1892", "France", "A key work of Gauguin's Tahitian period."),
    ("Rabbit", "Rabbit (Koons)", "Jeff Koons", "1986", "United States", "A stainless-steel sculpture of an inflatable rabbit, among the most expensive works by a living artist."),
    ("Comedian", "Comedian (artwork)", "Maurizio Cattelan", "2019", "Italy", "A banana duct-taped to a wall, a provocative conceptual artwork that became a viral sensation."),
    ("Untitled Film Stills", "Untitled Film Stills", "Cindy Sherman", "1977-1980", "United States", "A landmark photographic series exploring identity and media representation."),
    ("The Weather Project", "The Weather Project", "Olafur Eliasson", "2003", "Denmark/Iceland", "A monumental indoor sun installation at Tate Modern that drew millions of visitors."),
    ("Rain Room", "Rain Room (installation)", "Random International", "2012", "United Kingdom", "An immersive installation letting visitors walk through simulated rain without getting wet."),
]

MUSICAL_AND_SCIENTIFIC_INSTRUMENTS = [
    ("Antikythera Mechanism (reprise)", "Antikythera mechanism", "Ancient Greeks", "c. 150-100 BCE", "Greece", "The world's oldest known analog computer, used to predict astronomical events."),
    ("Le Messie Stradivarius", "Messiah Stradivarius", "Antonio Stradivari", "1716", "Italy", "One of the best-preserved violins made by the legendary luthier Antonio Stradivari."),
    ("The Lady Blunt Stradivarius", "Lady Blunt Stradivarius", "Antonio Stradivari", "1721", "Italy", "One of the most pristine surviving Stradivarius violins."),
    ("Guarneri del Gesù 'Il Cannone'", "Il Cannone Guarnerius", "Giuseppe Guarneri", "1743", "Italy", "The violin favored by virtuoso Niccolò Paganini, prized for its powerful tone."),
    ("Beethoven's Broadwood Piano", "Ludwig van Beethoven's Broadwood piano", "John Broadwood & Sons", "1817", "United Kingdom", "A grand piano gifted to Beethoven, now preserved as a historic instrument."),
    ("The Galileo Telescope", "Galileo's telescopes", "Galileo Galilei", "1609", "Italy", "Among the earliest telescopes used for astronomical observation, revolutionizing our view of the cosmos."),
    ("Newton's Reflecting Telescope", "Newtonian telescope", "Isaac Newton", "1668", "United Kingdom", "The first practical reflecting telescope, a landmark in the history of astronomy."),
    ("The Antikythera Astrolabe Tradition", "Astrolabe", "Islamic and Greek astronomers", "Ancient through medieval era", "Greece/Islamic world", "Precision instruments for astronomical calculation, navigation, and timekeeping."),
    ("The Jaipur Observatory Instruments (Jantar Mantar)", "Jantar Mantar, Jaipur", "Maharaja Jai Singh II", "1734", "India", "Massive masonry astronomical instruments for tracking celestial bodies with the naked eye."),
    ("The Antique Chinese South-Pointing Chariot", "South-pointing chariot", "Ancient Chinese engineers", "c. 3rd century CE (recorded)", "China", "An early mechanical device using differential gears to always point south."),
    ("The Marine Chronometer of John Harrison (H4)", "H4 (chronometer)", "John Harrison", "1759", "United Kingdom", "The timepiece that solved the 'longitude problem', transforming maritime navigation."),
    ("The Gutenberg Printing Press (reconstruction)", "Printing press", "Johannes Gutenberg", "c. 1440", "Germany", "The movable-type press that revolutionized the spread of knowledge in Europe."),
    ("The Stradivari Guitar 'Sabionari'", "Stradivarius", "Antonio Stradivari", "1679", "Italy", "One of very few surviving guitars made by Stradivari."),
    ("Mozart's Fortepiano", "Fortepiano", "Anton Walter", "c. 1782", "Austria", "The type of keyboard instrument for which Mozart composed many of his concertos."),
    ("The Sitar of Ravi Shankar", "Sitar", "Traditional Indian craftsmen", "20th century", "India", "The classical Indian string instrument popularized worldwide by virtuoso Ravi Shankar."),
]

ARMOR_AND_WEAPONS = [
    ("Tutankhamun's Golden Dagger", "Tutankhamun's meteoric iron dagger", "Ancient Egyptians", "c. 1323 BCE", "Egypt", "A ceremonial dagger with an iron blade made from meteoric metal, found in Tutankhamun's tomb."),
    ("The Sutton Hoo Helmet", "Sutton Hoo helmet", "Anglo-Saxon craftsmen", "early 7th century CE", "England", "An iconic Anglo-Saxon ceremonial helmet from a royal ship burial."),
    ("The Honjo Masamune", "Honjo Masamune", "Masamune", "c. 14th century", "Japan", "A legendary katana by Japan's most celebrated swordsmith, lost after World War II."),
    ("The Sword of Goujian", "Sword of Goujian", "Ancient Chinese metalworkers", "c. 5th century BCE", "China", "A bronze sword remarkably free of rust after over 2,000 years, prized for its craftsmanship."),
    ("Excalibur (legendary, cultural artifact)", "Excalibur", "Legendary (King Arthur mythos)", "Medieval legend", "United Kingdom", "The legendary sword of King Arthur, one of the most famous weapons in Western folklore."),
    ("The Wallace Sword", "William Wallace Monument", "Attributed to William Wallace's era", "13th-14th century", "Scotland", "A greatsword associated with the Scottish independence hero William Wallace."),
    ("Napoleon's Sword of State", "Napoleon's sword", "French court jewelers", "1802", "France", "The ornate sword worn by Napoleon Bonaparte at his coronation."),
    ("The Terracotta Army Weapons Cache", "Terracotta Army", "Craftsmen of Qin Shi Huang", "c. 210 BCE", "China", "Real bronze weapons, remarkably preserved, found alongside the Terracotta Army."),
    ("Greenwich Armor of Henry VIII", "Greenwich armour", "Royal Almain Armoury, Greenwich", "16th century", "England", "Elaborately decorated ceremonial armor made for King Henry VIII."),
    ("The Maximilian Armor", "Maximilian armour", "German/Austrian armorers", "early 16th century", "Germany/Austria", "A distinctive fluted style of plate armor named for Holy Roman Emperor Maximilian I."),
    ("The Samurai Armor of the Date Clan", "Japanese armour", "Japanese armorers", "16th-17th century", "Japan", "Elaborate lacquered samurai armor reflecting the status of feudal Japanese warlords."),
    ("The Zulu Iklwa Spear (Shaka's design)", "Iklwa", "Zulu craftsmen (Shaka Zulu era)", "early 19th century", "South Africa", "A short stabbing spear credited to King Shaka, which transformed Zulu military tactics."),
]

TEXTILES_AND_TAPESTRIES = [
    ("Bayeux Tapestry (reprise)", "Bayeux Tapestry", "Anglo-Saxon or Norman embroiderers", "c. 1070s", "France/England", "A 70-meter embroidered chronicle of the Norman Conquest."),
    ("The Lady and the Unicorn Tapestries", "The Lady and the Unicorn", "Unknown (Flemish weavers)", "c. 1500", "France/Belgium", "A celebrated set of six medieval tapestries exploring the senses and courtly allegory."),
    ("The Hunt of the Unicorn Tapestries", "The Hunt of the Unicorn", "Unknown (Flemish weavers)", "c. 1495-1505", "Belgium/France", "A famous set of seven tapestries depicting the mythical unicorn hunt."),
    ("Ardabil Carpet (reprise)", "Ardabil Carpet", "Maqsud of Kashan (attributed)", "1539-1540", "Iran", "One of the world's oldest and largest dated Islamic carpets."),
    ("Pazyryk Carpet", "Pazyryk Carpet", "Scythian craftsmen", "c. 5th century BCE", "Siberia (Russia)", "The oldest known pile carpet in the world, preserved in permafrost burial mounds."),
    ("Paracas Textiles (reprise)", "Paracas culture", "Paracas civilization", "c. 800-100 BCE", "Peru", "Intricately woven burial textiles from ancient coastal Peru."),
    ("Chilkat Blanket", "Chilkat weaving", "Tlingit people", "Traditional, 19th century onward", "Canada/Alaska", "Ceremonial woven blankets from the Tlingit people of the Pacific Northwest."),
    ("Kente Cloth of the Ashanti", "Kente cloth", "Ashanti and Ewe weavers", "Traditional, 17th century onward", "Ghana", "Brightly patterned handwoven cloth associated with Ashanti royalty and ceremony."),
    ("Kashmir Shawls", "Kashmir shawl", "Kashmiri weavers", "Traditional, Mughal era onward", "India", "Intricately woven pashmina shawls once prized across royal courts of Europe and Asia."),
    ("The Overlord Embroidery", "Overlord Embroidery", "Royal School of Needlework", "1968-1974", "United Kingdom", "A modern embroidered chronicle of the D-Day landings, inspired by the Bayeux Tapestry."),
]

CERAMICS_AND_POTTERY = [
    ("Portland Vase (reprise)", "Portland Vase", "Ancient Romans", "1-25 CE", "Italy", "A masterpiece of Roman cameo glass."),
    ("Ru Ware Brush Washer (reprise)", "Ru ware", "Song dynasty potters", "c. 1086-1125", "China", "Among the rarest and most valuable ceramics in Chinese art history."),
    ("The David Vases", "David Vases", "Yuan dynasty potters", "1351", "China", "A pair of blue-and-white porcelain temple vases, key reference pieces for dating Yuan porcelain."),
    ("Meissen Porcelain Menagerie", "Meissen porcelain", "Johann Joachim Kändler", "1730s", "Germany", "Elaborate porcelain animal sculptures from Europe's first hard-paste porcelain factory."),
    ("Portland Vase Wedgwood Copies", "Wedgwood", "Josiah Wedgwood", "1790s", "United Kingdom", "Jasperware reproductions that helped popularize Neoclassical design in Britain."),
    ("Iznik Ware Tiles", "İznik pottery", "Ottoman Iznik potters", "16th century", "Turkey", "Vividly patterned ceramic tiles and vessels that decorated Ottoman mosques and palaces."),
    ("Moche Portrait Vessels", "Moche culture", "Moche civilization", "c. 100-700 CE", "Peru", "Strikingly lifelike ceramic portrait vessels from ancient Peru."),
    ("Greek Attic Black-Figure Amphorae", "Black-figure pottery", "Ancient Greek (Attic) potters", "6th century BCE", "Greece", "A defining style of ancient Greek vase painting depicting myth and daily life."),
    ("Greek Red-Figure Kylix", "Red-figure pottery", "Ancient Greek (Attic) potters", "5th century BCE", "Greece", "A refined Greek pottery style that succeeded black-figure technique."),
    ("Talavera Pottery of Puebla", "Talavera pottery", "Puebla artisans", "16th century onward", "Mexico", "Distinctive tin-glazed ceramics blending Spanish and Mesoamerican traditions."),
    ("Delftware Blue Pottery", "Delftware", "Dutch potters (Delft)", "17th century", "Netherlands", "Blue-and-white tin-glazed earthenware inspired by Chinese porcelain."),
    ("Raqqa Ware Islamic Ceramics", "Raqqa ware", "Islamic (Syrian) potters", "12th-13th century", "Syria", "Lustreware ceramics renowned for their iridescent metallic glaze."),
]

COINS_AND_CURRENCY = [
    ("Athenian Owl Tetradrachm", "Athenian coinage", "Ancient Athenians", "c. 5th century BCE", "Greece", "One of the most widely circulated and recognized coins of the ancient Mediterranean world."),
    ("Roman Aureus of Julius Caesar", "Roman currency", "Roman mints", "44 BCE", "Italy (Rome)", "Among the earliest Roman coins to depict a living individual, minted shortly before Caesar's assassination."),
    ("Gold Dinar of the Umayyad Caliphate", "Islamic coinage", "Umayyad Caliphate", "696-697 CE", "Syria", "Among the earliest purely epigraphic Islamic gold coins, marking a shift from Byzantine-style imagery."),
    ("1933 Double Eagle", "1933 double eagle", "United States Mint", "1933", "United States", "One of the rarest and most valuable coins in the world; nearly all examples were melted down."),
    ("Brasher Doubloon", "Brasher Doubloon", "Ephraim Brasher", "1787", "United States", "One of the first gold coins struck in the newly independent United States."),
    ("Ancient Lydian Electrum Coins", "Lydian coinage", "Kingdom of Lydia", "c. 600 BCE", "Turkey", "Among the earliest coins ever minted, made from electrum (a natural gold-silver alloy)."),
    ("Ming Dynasty Paper Currency (Da Ming Baochao)", "Jiaochao", "Ming dynasty government", "14th century", "China", "Among the world's earliest widely circulated paper currencies."),
    ("Song Dynasty Jiaozi Notes", "Jiaozi (currency)", "Song dynasty merchants/government", "11th century", "China", "Considered the first paper money used by a government in world history."),
]

FAMOUS_PAINTINGS_MORE = [
    ("The Two Gentlemen of Verona (illustration tradition)", "Pre-Raphaelite Brotherhood", "Pre-Raphaelite painters", "19th century", "United Kingdom", "Represents the detailed, literature-inspired style of the Pre-Raphaelite movement."),
    ("The Lady of Shalott", "The Lady of Shalott (painting)", "John William Waterhouse", "1888", "United Kingdom", "A Pre-Raphaelite masterpiece inspired by Tennyson's poem."),
    ("Ophelia (reprise)", "Ophelia (painting)", "John Everett Millais", "1851-1852", "United Kingdom", "Renowned for its meticulous botanical detail."),
    ("Nighthawks (reprise)", "Nighthawks", "Edward Hopper", "1942", "United States", "One of the most recognizable images of American solitude."),
    ("The Death of Marat", "The Death of Marat", "Jacques-Louis David", "1793", "France", "A Neoclassical depiction of the assassinated French Revolutionary leader."),
    ("Liberty Leading the People (reprise)", "Liberty Leading the People", "Eugène Delacroix", "1830", "France", "France's enduring Romantic image of revolution."),
    ("The Swing", "The Swing (Fragonard)", "Jean-Honoré Fragonard", "1767", "France", "A playful, flirtatious masterpiece of the French Rococo."),
    ("Pilgrimage to Cythera", "Pilgrimage to Cythera", "Jean-Antoine Watteau", "1717", "France", "A dreamlike Rococo scene that helped define the fête galante genre."),
    ("The Blue Boy", "The Blue Boy", "Thomas Gainsborough", "1770", "United Kingdom", "One of the most famous 18th-century English portraits."),
    ("Mr and Mrs Andrews", "Mr and Mrs Andrews", "Thomas Gainsborough", "c. 1750", "United Kingdom", "A celebrated double portrait set within an English landscape."),
    ("Portrait of Dr. Gachet", "Portrait of Dr. Gachet", "Vincent van Gogh", "1890", "France", "One of van Gogh's final portraits, later one of the most expensive paintings ever sold."),
    ("Irises", "Irises (painting)", "Vincent van Gogh", "1889", "France", "Painted during van Gogh's stay at the asylum in Saint-Rémy."),
    ("The Potato Eaters", "The Potato Eaters", "Vincent van Gogh", "1885", "Netherlands", "Van Gogh's early, somber masterpiece depicting peasant life."),
    ("Wheatfield with Crows", "Wheatfield with Crows", "Vincent van Gogh", "1890", "France", "Often (though not certainly) considered van Gogh's final painting."),
    ("Self-Portrait with Bandaged Ear", "Self-Portrait with Bandaged Ear", "Vincent van Gogh", "1889", "France", "Painted after the famous incident in which van Gogh injured his own ear."),
    ("The Old Guitarist", "The Old Guitarist", "Pablo Picasso", "1903-1904", "Spain", "A defining work of Picasso's melancholic Blue Period."),
    ("Family of Saltimbanques", "Family of Saltimbanques", "Pablo Picasso", "1905", "Spain", "A key painting of Picasso's Rose Period depicting circus performers."),
    ("Portrait of Gertrude Stein", "Portrait of Gertrude Stein", "Pablo Picasso", "1905-1906", "Spain", "A landmark portrait bridging Picasso's early style and Cubism."),
    ("Christina's World (reprise)", "Christina's World", "Andrew Wyeth", "1948", "United States", "One of the best-known American paintings of the 20th century."),
    ("A Bar at the Folies-Bergère (reprise)", "A Bar at the Folies-Bergère", "Édouard Manet", "1882", "France", "Manet's final major masterwork."),
    ("The Absinthe Drinker", "L'Absinthe", "Edgar Degas", "1875-1876", "France", "A stark depiction of Parisian café isolation."),
    ("The Ballet Class", "The Dance Class", "Edgar Degas", "1874", "France", "One of Degas's celebrated depictions of ballet dancers at practice."),
    ("L'Étoile (The Star)", "The Star (Degas)", "Edgar Degas", "1878", "France", "A luminous depiction of a solo ballerina on stage."),
    ("The Tub", "The Tub (Degas)", "Edgar Degas", "1886", "France", "Part of Degas's intimate series of bathers."),
    ("Bal du Moulin Rouge (Toulouse-Lautrec posters)", "Henri de Toulouse-Lautrec", "Henri de Toulouse-Lautrec", "1890s", "France", "Iconic Belle Époque posters capturing Parisian nightlife at the Moulin Rouge."),
    ("At the Moulin Rouge", "At the Moulin Rouge", "Henri de Toulouse-Lautrec", "1892-1895", "France", "A vivid painted scene of Parisian cabaret society."),
    ("Where Do We Come From? What Are We? Where Are We Going?", "Where Do We Come From? What Are We? Where Are We Going?", "Paul Gauguin", "1897-1898", "France (painted in Tahiti)", "Gauguin's philosophical Tahitian masterpiece, painted during a period of personal crisis."),
    ("Tahitian Women on the Beach", "Tahitian Women on the Beach", "Paul Gauguin", "1891", "France (painted in Tahiti)", "One of Gauguin's celebrated Post-Impressionist Tahitian paintings."),
    ("The Yellow Christ", "The Yellow Christ", "Paul Gauguin", "1889", "France", "A Symbolist religious painting rendered in Gauguin's Synthetist style."),
    ("A Wheatfield, with Cypresses", "Wheat Field with Cypresses", "Vincent van Gogh", "1889", "France", "A swirling landscape painted around the same time as The Starry Night."),
]

FAMOUS_SCULPTURES_MORE = [
    ("Michelangelo's Pietà (Rondanini)", "Rondanini Pietà", "Michelangelo", "1552-1564", "Italy", "Michelangelo's final, unfinished sculpture, worked on until days before his death."),
    ("The Dying Slave", "The Dying Slave", "Michelangelo", "1513-1516", "Italy", "One of Michelangelo's unfinished 'Slaves' series for the tomb of Pope Julius II."),
    ("Hermes and the Infant Dionysus", "Hermes of Praxiteles", "Praxiteles (attributed)", "4th century BCE", "Greece", "One of the finest surviving examples of Classical Greek sculpture."),
    ("The Barberini Ivory", "Barberini ivory", "Byzantine craftsmen", "c. 6th century CE", "Byzantine Empire", "An intricately carved ivory panel depicting a triumphant Byzantine emperor."),
    ("Michelangelo's Pietà (reprise)", "Pietà (Michelangelo)", "Michelangelo", "1498-1499", "Italy", "Housed in St. Peter's Basilica, one of the most revered sculptures in the world."),
    ("The Little Dancer of Fourteen Years", "Little Dancer Aged Fourteen", "Edgar Degas", "1878-1881", "France", "A remarkably lifelike wax and mixed-media sculpture, controversial when first exhibited."),
    ("Balzac Monument", "Monument to Balzac", "Auguste Rodin", "1898", "France", "A radically expressive sculpture of the novelist Honoré de Balzac."),
    ("The Age of Bronze", "The Age of Bronze", "Auguste Rodin", "1877", "France", "So lifelike it was initially accused of being cast directly from a live model."),
    ("Perseus Freeing Andromeda", "Perseus and Andromeda", "Various sculptors", "Various periods", "Italy/Greece", "A recurring mythological subject across Renaissance and Baroque sculpture."),
    ("The Rape of the Sabine Women (Giambologna)", "Rape of the Sabine Women (Giambologna)", "Giambologna", "1579-1583", "Italy", "A dynamic Mannerist marble carved from a single block of stone."),
    ("Neptune Fountain of Bologna", "Fontana del Nettuno, Bologna", "Giambologna", "1563-1567", "Italy", "A monumental bronze fountain celebrated as a masterpiece of Mannerist sculpture."),
    ("Menorah of the Arch of Titus", "Arch of Titus", "Ancient Romans", "81 CE", "Italy (Rome)", "A relief on the Arch of Titus depicting the plundered Temple Menorah of Jerusalem."),
    ("The Column of Trajan Reliefs (reprise)", "Trajan's Column", "Apollodorus of Damascus", "113 CE", "Italy", "One of the greatest relief-sculpture achievements of the ancient world."),
    ("Michelangelo's Slaves (Awakening Slave)", "The Slaves (Michelangelo)", "Michelangelo", "1520s", "Italy", "Unfinished figures seeming to emerge from the raw marble itself."),
]

MORE_EGYPTIAN_GREEK_ROMAN = [
    ("Amarna Letters", "Amarna letters", "Ancient Egyptians/Near Eastern scribes", "c. 1360-1332 BCE", "Egypt", "Diplomatic cuneiform correspondence revealing international relations of the ancient Near East."),
    ("Statue of Senenmut with Neferure", "Senenmut", "Ancient Egyptians", "c. 1470 BCE", "Egypt", "A block statue depicting the royal steward Senenmut with the princess he tutored."),
    ("The Fayum Mummy Portraits", "Fayum mummy portraits", "Romano-Egyptian painters", "1st-3rd century CE", "Egypt", "Strikingly lifelike painted portraits attached to mummies, blending Egyptian and Roman traditions."),
    ("Temple of Abu Simbel", "Abu Simbel temples", "Ancient Egyptians (Ramesses II)", "c. 1264-1244 BCE", "Egypt", "Massive rock-cut temples famously relocated in the 1960s to avoid flooding by the Aswan Dam."),
    ("Karnak Hypostyle Hall", "Karnak", "Ancient Egyptians", "c. 1290-1224 BCE", "Egypt", "A forest of 134 massive columns forming one of the grandest halls of the ancient world."),
    ("Statue of Hatshepsut", "Hatshepsut", "Ancient Egyptians", "c. 1479-1458 BCE", "Egypt", "Statues of one of ancient Egypt's few female pharaohs, often depicted with traditional royal regalia."),
    ("The Amphipolis Tomb Caryatids", "Amphipolis Tomb", "Ancient Macedonians", "4th century BCE", "Greece", "Monumental sculpted figures guarding a grand Macedonian-era tomb."),
    ("The Delphi Sphinx of Naxos", "Sphinx of Naxos", "Ancient Greeks", "c. 560 BCE", "Greece", "A monumental Archaic sphinx dedicated at the sanctuary of Delphi."),
    ("The Boxer at Rest", "Boxer at Rest", "Unknown (Hellenistic)", "c. 330-50 BCE", "Greece", "A remarkably expressive bronze depicting an exhausted, battered boxer."),
    ("The Terme Boxer (reprise variant)", "Boxer at Rest", "Unknown (Hellenistic)", "c. 330-50 BCE", "Greece", "Also known as the Terme Boxer, prized for its emotional realism."),
    ("The Artemision Bronze", "Artemision Bronze", "Unknown (Classical Greek)", "c. 460 BCE", "Greece", "A bronze depicting either Zeus or Poseidon, recovered from a shipwreck."),
    ("The Motya Charioteer", "Motya Charioteer", "Unknown (Greek/Punic)", "c. 470 BCE", "Sicily (Italy)", "A rare, exceptionally refined marble statue of a victorious charioteer."),
    ("The Pergamon Altar", "Pergamon Altar", "Ancient Greeks (Pergamene)", "c. 197-159 BCE", "Turkey", "A monumental altar famed for its dramatic frieze depicting the battle of gods and giants."),
    ("The Temple of Olympian Zeus (Athens)", "Temple of Olympian Zeus, Athens", "Ancient Greeks/Romans", "started 6th century BCE, completed 131 CE", "Greece", "Once the largest temple in Greece, dedicated to Zeus."),
    ("Pompeii's House of the Faun Mosaic (reprise)", "Alexander Mosaic", "Ancient Romans (Pompeii)", "c. 100 BCE", "Italy", "A celebrated floor mosaic depicting Alexander the Great in battle."),
    ("The Pantheon Dome", "Pantheon, Rome", "Ancient Romans (Hadrian)", "113-125 CE", "Italy", "The world's largest unreinforced concrete dome, a triumph of Roman engineering."),
    ("The Roman Forum Arch of Titus", "Arch of Titus", "Ancient Romans", "81 CE", "Italy (Rome)", "A triumphal arch commemorating the Roman conquest of Jerusalem."),
    ("The Baths of Caracalla", "Baths of Caracalla", "Ancient Romans", "212-216/217 CE", "Italy (Rome)", "One of the grandest public bathing complexes of the Roman world."),
    ("The Pont du Gard Aqueduct", "Pont du Gard", "Ancient Romans", "1st century CE", "France", "A monumental Roman aqueduct bridge, a landmark of Roman engineering."),
    ("The Hadrian's Wall Milecastles", "Hadrian's Wall", "Ancient Romans (Hadrian)", "122 CE", "England", "A fortified frontier wall marking the northern edge of Roman Britain."),
]

MORE_ASIAN_ARTIFACTS = [
    ("The Mawangdui Silk Paintings", "Mawangdui Silk Texts", "Han dynasty craftsmen", "2nd century BCE", "China", "Exceptionally preserved silk paintings and texts from a Han-dynasty tomb."),
    ("The Terracotta Army Bronze Chariots", "Bronze Chariot of Qin Shi Huang", "Craftsmen of Qin Shi Huang", "c. 210 BCE", "China", "Extraordinarily detailed half-scale bronze chariots buried near the Terracotta Army."),
    ("The Nine Dragon Screen", "Nine-Dragon Wall", "Ming dynasty craftsmen", "1756 (Beijing example)", "China", "Glazed-tile screens depicting nine dragons, symbols of imperial power."),
    ("The Yongle Encyclopedia", "Yongle Encyclopedia", "Ming dynasty scholars", "1403-1408", "China", "One of the largest encyclopedias in history, compiled under the Yongle Emperor."),
    ("The Mogao Caves Murals", "Mogao Caves", "Buddhist monks and artisans", "4th-14th century CE", "China", "A vast complex of Buddhist cave temples along the Silk Road, renowned for their murals."),
    ("The Terracotta Warriors of Xi'an (reprise)", "Terracotta Army", "Craftsmen of Qin Shi Huang", "c. 210 BCE", "China", "Also called the Terracotta Warriors and Horses."),
    ("The Ise Grand Shrine", "Ise Grand Shrine", "Japanese Shinto builders", "traditionally 4 BCE, rebuilt every 20 years", "Japan", "Japan's most sacred Shinto shrine, ritually rebuilt every two decades for over a millennium."),
    ("The Tale of Genji Scroll", "Tale of Genji scroll", "Heian-era court painters", "12th century", "Japan", "An illustrated handscroll of the world's first novel, the Tale of Genji."),
    ("The Himeji Byōbu (reprise)", "Byōbu", "Various Japanese artists", "16th-19th centuries", "Japan", "Folding screens central to Japanese interior art."),
    ("The Great Torii of Itsukushima", "Itsukushima Shrine", "Japanese Shinto builders", "1168 (current gate 1875)", "Japan", "A floating torii gate that appears to rise from the sea at high tide."),
    ("The Hoysaleswara Temple Carvings", "Hoysaleswara Temple", "Hoysala dynasty craftsmen", "1121 CE", "India", "Densely carved temple friezes considered among the finest in Indian sculpture."),
    ("The Sanchi Great Stupa Gateways", "Sanchi Stupa", "Mauryan/Sunga dynasties", "3rd-1st century BCE", "India", "Ornately carved gateways ('toranas') depicting scenes from the Buddha's life."),
    ("The Meenakshi Temple Gopurams", "Meenakshi Amman Temple", "Various Tamil dynasties", "6th century CE onward (rebuilt 1623-1655)", "India", "Towering, vividly painted temple gateways in Madurai, southern India."),
    ("The Brihadeeswarar Temple", "Brihadeeswarar Temple", "Chola dynasty (Rajaraja I)", "1010 CE", "India", "A UNESCO World Heritage Chola-dynasty temple famed for its massive granite vimana tower."),
    ("The Golden Temple (Harmandir Sahib)", "Golden Temple", "Sikh Gurus (Guru Arjan)", "1604 (current gold covering 19th century)", "India", "The holiest shrine in Sikhism, renowned for its gold-covered sanctum."),
]

FAMOUS_MAPS = [
    ("The Hereford Mappa Mundi", "Hereford Mappa Mundi", "Richard of Haldingham (attributed)", "c. 1300", "England", "The largest surviving medieval map, depicting the world as understood in 13th-century Europe."),
    ("The Waldseemüller Map", "Waldseemüller map", "Martin Waldseemüller", "1507", "Germany", "The first map to use the name 'America', sometimes called 'America's birth certificate'."),
    ("The Piri Reis Map", "Piri Reis map", "Piri Reis", "1513", "Turkey (Ottoman Empire)", "A remarkable Ottoman world map noted for its detail of the Atlantic coastlines."),
    ("The Tabula Peutingeriana", "Peutinger Map", "Roman cartographers (medieval copy)", "medieval copy of a 4th/5th-century original", "Italy (Rome)", "A schematic map of the Roman road network stretching from Britain to India."),
    ("The Cantino Planisphere", "Cantino planisphere", "Unknown Portuguese cartographer", "1502", "Portugal", "One of the earliest surviving maps showing Portuguese discoveries, including Brazil."),
    ("The Fra Mauro Map", "Fra Mauro map", "Fra Mauro", "c. 1450", "Italy", "One of the greatest works of medieval cartography, remarkably detailed for its era."),
    ("The Al-Idrisi World Map (Tabula Rogeriana)", "Tabula Rogeriana", "Muhammad al-Idrisi", "1154", "Sicily (Italy)/Islamic world", "A landmark medieval Islamic world map compiled for King Roger II of Sicily."),
]

EUROPEAN_MEDIEVAL_ARTIFACTS = [
    ("The Crown of the Holy Roman Empire", "Imperial Crown of the Holy Roman Empire", "Ottonian craftsmen", "10th century", "Germany/Austria", "The coronation crown used for Holy Roman Emperors for centuries."),
    ("The Stone of Scone", "Stone of Scone", "Medieval Scots", "unknown antiquity, used from medieval era", "Scotland", "A historic coronation stone used in the crowning of Scottish and later British monarchs."),
    ("The Alfred Jewel", "Alfred Jewel", "Anglo-Saxon craftsmen", "late 9th century", "England", "An exquisite gold and enamel Anglo-Saxon jewel linked to King Alfred the Great."),
    ("The Staffordshire Hoard", "Staffordshire Hoard", "Anglo-Saxon craftsmen", "7th century CE", "England", "The largest hoard of Anglo-Saxon gold and silver metalwork ever discovered."),
    ("The Utrecht Psalter", "Utrecht Psalter", "Carolingian monks", "c. 820-835 CE", "France", "An influential illuminated manuscript famed for its vivid pen-and-ink drawings."),
    ("The Trier Ivory", "Trier Ivory", "Byzantine or Carolingian craftsmen", "c. 6th-9th century CE", "Germany", "A finely carved ivory panel depicting a relic procession."),
    ("The Shroud of Turin", "Shroud of Turin", "Unknown", "disputed, radiocarbon-dated to medieval era", "Italy", "A linen cloth bearing a faint image, venerated by some and studied extensively by scientists and historians."),
    ("The Externsteine Rock Formation Reliefs", "Externsteine", "Medieval Saxon carvers", "c. 12th century (relief)", "Germany", "Sandstone pillars with a notable medieval relief of the Descent from the Cross."),
    ("The Bury Bible", "Bury Bible", "Master Hugo", "c. 1135", "England", "One of the finest surviving examples of English Romanesque manuscript illumination."),
    ("The Winchester Bible", "Winchester Bible", "English monks", "c. 1150-1175", "England", "The largest surviving 12th-century English illuminated Bible."),
    ("The Ghent Altarpiece", "Ghent Altarpiece", "Hubert and Jan van Eyck", "1432", "Belgium", "One of the most influential and frequently stolen artworks in history, a landmark of early Netherlandish painting."),
    ("The Isenheim Altarpiece", "Isenheim Altarpiece", "Matthias Grünewald", "c. 1512-1516", "France/Germany", "A harrowing, expressive altarpiece originally made for a hospital treating plague victims."),
    ("The Unicorn in Captivity (reprise)", "The Hunt of the Unicorn", "Unknown (Flemish weavers)", "c. 1495-1505", "Belgium/France", "The final and most famous panel of the Unicorn Tapestries series."),
    ("The Book of Durrow", "Book of Durrow", "Celtic monks", "c. 650-700 CE", "Ireland", "One of the earliest surviving fully illuminated Insular gospel manuscripts."),
    ("The Ardagh Chalice", "Ardagh Chalice", "Early medieval Irish craftsmen", "8th century CE", "Ireland", "An exceptional example of early medieval Irish metalwork and design."),
    ("The Tara Brooch", "Tara Brooch", "Early medieval Irish craftsmen", "c. 700 CE", "Ireland", "One of the finest surviving pieces of Insular jewelry, showcasing intricate Celtic metalwork."),
]

OCEANIA_AND_MORE_AMERICAS = [
    ("Uluru (Ayers Rock)", "Uluru", "Anangu people (sacred site)", "geological, culturally significant for tens of thousands of years", "Australia", "A massive sandstone monolith sacred to the Anangu people, one of Australia's most recognized natural landmarks."),
    ("Aboriginal Bark Paintings of Arnhem Land", "Aboriginal art", "Yolngu and other Aboriginal artists", "Traditional, ongoing", "Australia", "Ochre paintings on eucalyptus bark depicting Dreamtime stories, among the world's oldest continuous art traditions."),
    ("The Rapa Nui Rongorongo Tablets", "Rongorongo", "Rapa Nui people", "believed 19th century or earlier", "Easter Island (Chile)", "An undeciphered script found on wooden tablets from Easter Island."),
    ("Maori Meeting House Carvings (Whare Whakairo)", "Wharenui", "Māori craftsmen", "Traditional, 19th century examples", "New Zealand", "Elaborately carved ancestral meeting houses central to Māori communal life."),
    ("The Hawaiian Feather Cloaks ('Ahu 'ula)", "'Ahu'ula", "Native Hawaiian craftsmen", "Traditional, 18th-19th century", "United States (Hawaii)", "Feathered cloaks worn by Hawaiian ali'i (chiefs), among the most prized objects of Polynesian material culture."),
    ("The Papua New Guinea Sepik River Masks", "Sepik", "Sepik River peoples", "Traditional, ongoing", "Papua New Guinea", "Elaborately carved ceremonial masks and objects from the Sepik River region."),
    ("Inca Quipu Recording Devices", "Quipu", "Inca Empire", "c. 1400-1532 CE", "Peru", "Knotted cord devices used by the Inca to record numerical and possibly narrative information."),
    ("The Gold of El Dorado (Museo del Oro collection)", "Museo del Oro", "Various pre-Columbian cultures", "Various, pre-16th century", "Colombia", "A vast collection of pre-Columbian goldwork inspiring the legend of El Dorado."),
    ("The Great Serpent Mound", "Serpent Mound", "Native American mound builders", "c. 300 BCE-1070 CE (disputed)", "United States", "A quarter-mile-long earthwork effigy mound depicting a serpent."),
    ("Cahokia Mounds", "Cahokia", "Mississippian civilization", "c. 1050-1350 CE", "United States", "The largest pre-Columbian settlement north of Mexico, centered on massive earthen mounds."),
    ("Navajo Chief's Blanket", "Navajo weaving", "Navajo weavers", "Traditional, 19th century examples", "United States", "Finely woven wool blankets that became iconic symbols of Native American textile art."),
    ("The Hopewell Culture Effigy Pipes", "Hopewell tradition", "Hopewell culture", "c. 100 BCE-500 CE", "United States", "Elaborately carved ceremonial pipes reflecting a sophisticated exchange network across ancient North America."),
]

MORE_SCULPTURE_AND_ARCHITECTURE = [
    ("The Vatican Belvedere Torso", "Belvedere Torso", "Apollonios (signed)", "1st century BCE", "Greece/Italy", "A fragmentary but hugely influential Hellenistic sculpture admired by Michelangelo."),
    ("The Farnese Bull", "Farnese Bull", "Apollonius and Tauriscus (Roman copy)", "2nd century BCE-2nd century CE", "Greece/Italy", "One of the largest sculptural groups surviving from antiquity, depicting a mythological punishment scene."),
    ("The Capitoline Wolf", "Capitoline Wolf", "Etruscan craftsmen (statue); twins added later", "5th century BCE (wolf); 15th century CE (twins)", "Italy", "A bronze depicting the she-wolf nursing Romulus and Remus, a symbol of Rome itself."),
    ("Donatello's David", "David (Donatello)", "Donatello", "c. 1440s", "Italy", "The first freestanding nude bronze statue since antiquity, a landmark of the early Renaissance."),
    ("Gattamelata Equestrian Statue", "Equestrian statue of Gattamelata", "Donatello", "1453", "Italy", "The first large bronze equestrian statue cast since ancient Rome."),
    ("The Fountain of the Four Rivers", "Fontana dei Quattro Fiumi", "Gian Lorenzo Bernini", "1651", "Italy", "A dramatic Baroque fountain in Rome's Piazza Navona personifying four great rivers."),
    ("The Trevi Fountain", "Trevi Fountain", "Nicola Salvi", "1732-1762", "Italy", "Rome's largest and most famous Baroque fountain, a major tourist landmark."),
    ("Michelangelo's Medici Chapel Tombs", "Medici Chapel", "Michelangelo", "1520-1534", "Italy", "Allegorical figures of Day, Night, Dawn, and Dusk on the Medici family tombs."),
    ("The Colossus of Constantine (fragments)", "Colossus of Constantine", "Ancient Romans", "c. 312-315 CE", "Italy (Rome)", "Massive surviving fragments of a colossal statue of Emperor Constantine."),
    ("The Marble Faun (Praxitelean type)", "Resting Satyr", "Praxiteles (attributed, Roman copies)", "4th century BCE (original)", "Greece", "A celebrated Greek sculptural type of a languid, resting satyr, copied widely in Roman times."),
    ("The Ludovisi Throne", "Ludovisi Throne", "Unknown (Greek, possibly South Italian)", "c. 460 BCE", "Greece/Italy", "A finely carved marble relief believed to depict the birth of Aphrodite."),
    ("Chartres Cathedral West Portal Sculptures", "Chartres Cathedral", "Medieval French sculptors", "12th-13th century", "France", "Renowned Gothic sculptural programs considered among the finest of the Middle Ages."),
    ("Reims Cathedral Smiling Angel", "Reims Cathedral", "Medieval French sculptors", "13th century", "France", "A celebrated Gothic sculpture known for its uniquely serene, smiling expression."),
    ("The Bamberg Rider", "Bamberg Horseman", "Unknown (medieval German)", "c. 1225-1237", "Germany", "One of the first free-standing equestrian statues since antiquity, in Bamberg Cathedral."),
    ("Naumburg Cathedral Donor Figures", "Naumburg Cathedral", "Naumburg Master", "c. 1250", "Germany", "Strikingly individualized medieval sculpted portraits of the cathedral's noble donors."),
]

MORE_INSTRUMENTS_AND_SMALL_OBJECTS = [
    ("Napoleon's Death Mask", "Napoleon's death mask", "François Carlo Antommarchi", "1821", "France/Saint Helena", "A cast taken shortly after Napoleon's death, later widely reproduced."),
    ("Beethoven's Ear Trumpets", "Ludwig van Beethoven", "Johann Nepomuk Mälzel (maker)", "c. 1810s", "Austria", "Custom hearing aids made for Beethoven as his hearing declined."),
    ("The Stradivarius 'Vieuxtemps'", "Vieuxtemps Guarneri", "Giuseppe Guarneri", "1741", "Italy", "One of the most valuable violins in the world, associated with virtuoso Henri Vieuxtemps."),
    ("The Amati Family Violins", "Amati", "Andrea Amati and family", "16th-17th century", "Italy", "Instruments by the Cremonese family credited with establishing the modern violin form."),
    ("The Servette Bugatti Violin", "Ferdinando Bugatti", "Ettore Bugatti (design attribution, disputed)", "20th century", "Italy/France", "A rare ornamental violin blending fine lutherie with Art Deco design."),
    ("The Antique Chinese Guqin 'Nine Rays'", "Guqin", "Tang dynasty craftsmen", "8th century CE", "China", "Ancient seven-string zithers central to Chinese literati culture for millennia."),
    ("The Japanese Biwa of the Heike Tradition", "Biwa", "Traditional Japanese craftsmen", "Traditional, Heian era onward", "Japan", "A pear-shaped lute traditionally used to narrate the epic Tale of the Heike."),
    ("The West African Kora", "Kora (instrument)", "Mandinka griots", "Traditional, centuries old", "West Africa (Mali/Senegal/Guinea)", "A 21-string harp-lute central to West African griot storytelling traditions."),
    ("The Indian Veena", "Veena", "Traditional Indian craftsmen", "Ancient, referenced in Vedic texts", "India", "An ancient plucked string instrument central to Indian classical music."),
    ("The Andean Panpipes (Siku)", "Panpipes", "Andean cultures", "Traditional, pre-Columbian", "Peru/Bolivia", "Traditional panpipes central to Andean musical culture for millennia."),
]

CATEGORY_ASSIGNMENTS = [
    (FAMOUS_PAINTINGS, "painting"),
    (FAMOUS_PAINTINGS_MORE, "painting"),
    (FAMOUS_SCULPTURES, "sculpture"),
    (FAMOUS_SCULPTURES_MORE, "sculpture"),
    (EGYPTIAN_ARTIFACTS, "archaeology"),
    (GREEK_ROMAN_ARTIFACTS, "archaeology"),
    (MESOPOTAMIAN_ARTIFACTS, "archaeology"),
    (ASIAN_ART_ARTIFACTS, "archaeology"),
    (SOUTH_ASIAN_ARTIFACTS, "archaeology"),
    (ISLAMIC_ART_ARTIFACTS, "architecture"),
    (AFRICAN_ART_ARTIFACTS, "archaeology"),
    (PRECOLUMBIAN_NATIVE_AMERICAN_ARTIFACTS, "archaeology"),
    (MANUSCRIPTS_DOCUMENTS, "manuscript"),
    (CROWN_JEWELS_AND_GEMS, "jewelry"),
    (PHOTOGRAPHS, "photograph"),
    (MONUMENTS_AND_LANDMARKS, "architecture"),
    (MODERN_CONTEMPORARY_ART, "painting"),
    (MUSICAL_AND_SCIENTIFIC_INSTRUMENTS, "instrument"),
    (ARMOR_AND_WEAPONS, "weapon"),
    (TEXTILES_AND_TAPESTRIES, "textile"),
    (CERAMICS_AND_POTTERY, "ceremonial"),
    (COINS_AND_CURRENCY, "coin"),
    (MORE_EGYPTIAN_GREEK_ROMAN, "archaeology"),
    (MORE_ASIAN_ARTIFACTS, "archaeology"),
    (FAMOUS_MAPS, "map"),
    (EUROPEAN_MEDIEVAL_ARTIFACTS, "manuscript"),
    (OCEANIA_AND_MORE_AMERICAS, "archaeology"),
    (MORE_SCULPTURE_AND_ARCHITECTURE, "sculpture"),
    (MORE_INSTRUMENTS_AND_SMALL_OBJECTS, "instrument"),
]


def build_object(idx: int, name: str, wiki_title: str, creator: str, date: str, origin: str, description: str, category: str) -> dict:
    obj_id = f"fm_{idx:04d}"
    return {
        "id": obj_id,
        "name": name,
        "artist": creator,
        "year": date,
        "origin": origin,
        "material": category,
        "category": category,
        "description": description,
        "significance": f"Widely recognized as one of the famous works representing {origin} in world art and cultural history.",
        "fun_fact": f"{name} is frequently featured in art history and world history curricula as a landmark example of {category} from {origin}.",
        "museum": "See Wikipedia for current location",
        "educational_importance": f"A genuinely famous, real work -- useful for art history, world history, and cultural studies at every level.",
        "related_lesson": "Art History" if category in ("painting", "sculpture") else "World History",
        "activity": f"Research {name} further: who made it, where it is today, and why it became famous.",
        "quiz": {
            "question": f"Which culture or region does '{name}' come from?",
            "options": [origin, "Antarctica", "International Waters", "Unknown"],
            "answer": 0,
        },
        "related_subjects": ["Art History", "World History", "Geography"],
        "links": {
            "wikipedia": wiki_url(wiki_title),
            "image_search": commons_search(name),
            "video": yt(f"{name} art history explained"),
            "smarthistory": smarthistory(name),
        },
        "wiki_title": wiki_title,
    }


def build_objects() -> list[dict]:
    objects = []
    idx = 0
    seen_wiki_titles = set()
    for items, category in CATEGORY_ASSIGNMENTS:
        for name, wiki_title, creator, date, origin, description in items:
            if wiki_title in seen_wiki_titles:
                continue  # avoid listing the same real work twice under different card names
            seen_wiki_titles.add(wiki_title)
            idx += 1
            objects.append(build_object(idx, name, wiki_title, creator, date, origin, description, category))
    return objects


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    objects = build_objects()
    data["galleries"]["famous_masterpieces"] = {
        "label": "Famous Masterpieces",
        "emoji": "🏆",
        "description": (
            f"{len(objects)} genuinely famous, individually named real artworks and artifacts -- paintings, "
            f"sculpture, ancient artifacts, manuscripts, crown jewels, historic photographs, and monuments -- "
            f"each linked to its real Wikipedia page so the museum can show an actual live photo of the work."
        ),
        "objects": objects,
    }

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(g.get("objects", [])) for g in data["galleries"].values())
    print(f"Added {len(objects)} famous objects. Museum now has {total} objects across {len(data['galleries'])} galleries.")


if __name__ == "__main__":
    main()
