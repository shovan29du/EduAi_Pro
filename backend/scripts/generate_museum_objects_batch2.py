#!/usr/bin/env python3
"""Add a second large batch of ~1000 genuinely famous, individually-named
real museum objects/artifacts to the Virtual Museum, in a new
"World Heritage Treasures" gallery, complementing the earlier
"Famous Masterpieces" (501 objects) and "World Collections" (1000
objects) galleries.

Every entry is a real, well-known work (not a generated placeholder).
Each carries an accurate ``wiki_title`` -- the real Wikipedia article
title -- so the existing ``WikiThumbnail`` component
(frontend/src/components/VirtualMuseum.jsx) fetches a genuine, live photo
of the actual work from Wikipedia's public REST API at render time. This
project does not fabricate direct image URLs; the live-fetch-with-fallback
mechanism is the honest way to get a real thumbnail for every entry
without guessing file paths that might not exist.

Re-run after editing:
    python3 backend/scripts/generate_museum_objects_batch2.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"
GALLERY_KEY = "world_heritage_treasures"


def wiki_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def commons_search(q: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(q)


def google_image_search(q: str) -> str:
    return "https://www.google.com/search?tbm=isch&q=" + quote_plus(q)


def yt(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def smarthistory(q: str) -> str:
    return "https://smarthistory.org/?s=" + quote_plus(q)


# Each entry is a tuple: (name, wiki_title, creator_or_culture, date, origin,
#                         one_line_description)
# CATEGORY_ASSIGNMENTS pairs each list with its museum "category" facet.
CATEGORY_ASSIGNMENTS: list[tuple[list[tuple], str]] = []

# 200 real, famous, individually-named paintings/prints/drawings not already
# covered by the "Famous Masterpieces" gallery (generate_famous_museum_objects.py)
# or by the most obvious blockbuster works. Organized by movement/region for
# readability; the build step below de-duplicates by wiki_title automatically.
MORE_PAINTINGS_BATCH2 = [
    # --- Northern Renaissance / early Netherlandish ---
    ("The Descent from the Cross", "The Descent from the Cross (van der Weyden)", "Rogier van der Weyden", "c. 1435-1443", "Belgium (Flanders)", "A tightly composed panel of mourners lowering Christ's body, among the most influential paintings of the Northern Renaissance."),
    ("Portrait of a Man in a Red Turban", "Portrait of a Man in a Red Turban", "Jan van Eyck", "1433", "Belgium (Flanders)", "Likely a self-portrait, celebrated for its meticulous realism and inscribed motto."),
    ("Madonna of Chancellor Rolin", "Madonna of Chancellor Rolin", "Jan van Eyck", "c. 1435", "Belgium (Flanders)", "A donor portrait masterpiece depicting Burgundian chancellor Nicolas Rolin kneeling before the Virgin and Child."),
    ("The Battle of Alexander at Issus", "The Battle of Alexander at Issus", "Albrecht Altdorfer", "1529", "Germany", "A sweeping panoramic battle scene famed for depicting a vast host of tiny soldiers beneath a dramatic sky."),
    ("Self-Portrait at Twenty-Eight", "Self-Portrait (Dürer, Munich)", "Albrecht Dürer", "1500", "Germany", "A frontal self-portrait deliberately styled to evoke images of Christ, asserting the dignity of the artist."),
    ("Melencolia I", "Melencolia I", "Albrecht Dürer", "1514", "Germany", "An enigmatic engraving packed with symbolic objects, long debated by scholars for its meaning."),
    ("Knight, Death and the Devil", "Knight, Death and the Devil", "Albrecht Dürer", "1513", "Germany", "One of Dürer's three 'Meisterstiche' engravings, depicting a knight riding steadfastly past death and the devil."),
    ("The Body of the Dead Christ in the Tomb", "The Body of the Dead Christ in the Tomb", "Hans Holbein the Younger", "1521-1522", "Germany/Switzerland", "A starkly realistic depiction of Christ's corpse that famously unsettled Dostoevsky."),
    ("Netherlandish Proverbs", "Netherlandish Proverbs", "Pieter Bruegel the Elder", "1559", "Belgium (Flanders)", "A crowded panel illustrating over 100 Dutch proverbs and idioms acted out literally."),
    ("The Peasant Wedding", "The Peasant Wedding", "Pieter Bruegel the Elder", "c. 1567", "Belgium (Flanders)", "A lively genre scene depicting a rural wedding feast, among Bruegel's best-known works."),
    ("Children's Games", "Children's Games (Bruegel)", "Pieter Bruegel the Elder", "1560", "Belgium (Flanders)", "A panoramic panel cataloguing over 80 children's games being played in a town square."),

    # --- Italian Renaissance (deeper cuts) ---
    ("Pallas and the Centaur", "Pallas and the Centaur", "Sandro Botticelli", "c. 1482", "Italy", "An allegorical painting of Wisdom taming brute force, likely commissioned by the Medici family."),
    ("The Flagellation of Christ", "The Flagellation of Christ (Piero della Francesca)", "Piero della Francesca", "c. 1455-1460", "Italy", "A small but celebrated panel renowned for its mysterious subject and mathematically precise perspective."),
    ("The Baptism of Christ", "The Baptism of Christ (Piero della Francesca)", "Piero della Francesca", "c. 1448-1450", "Italy", "A luminous early Renaissance panel prized for its clarity of light and geometric composition."),
    ("The Resurrection", "The Resurrection (Piero della Francesca)", "Piero della Francesca", "c. 1463-1465", "Italy", "A fresco showing Christ rising triumphantly above sleeping soldiers, called by Aldous Huxley 'the greatest picture in the world'."),
    ("Camera degli Sposi Frescoes", "Camera degli Sposi", "Andrea Mantegna", "1465-1474", "Italy", "An illusionistic frescoed chamber in the Palazzo Ducale of Mantua, famous for its painted oculus ceiling."),
    ("Assumption of the Virgin", "Assumption of the Virgin (Titian)", "Titian", "1515-1518", "Italy", "A monumental altarpiece in the Frari church, Venice, that established Titian's reputation as the city's leading painter."),
    ("The Tempest", "The Tempest (Giorgione)", "Giorgione", "c. 1508", "Italy", "A mysterious pastoral scene whose meaning has puzzled art historians for centuries."),
    ("The Marriage of the Virgin", "The Marriage of the Virgin (Raphael)", "Raphael", "1504", "Italy", "An early masterwork demonstrating Raphael's mastery of perspective and harmonious composition."),
    ("Madonna of the Meadow", "Madonna of the Meadow", "Raphael", "1506", "Italy", "A serene pyramidal composition of the Virgin, Christ Child, and infant St. John the Baptist."),
    ("The Last Judgment", "The Last Judgment (Michelangelo)", "Michelangelo", "1536-1541", "Italy", "A vast fresco covering the Sistine Chapel altar wall, depicting Christ's second coming and the fate of souls."),
    ("Lady with an Ermine", "Lady with an Ermine", "Leonardo da Vinci", "c. 1489-1491", "Italy", "A portrait of Cecilia Gallerani, mistress of the Duke of Milan, celebrated for its dynamic pose."),
    ("Virgin of the Rocks", "Virgin of the Rocks", "Leonardo da Vinci", "1483-1508", "Italy", "A devotional scene set in a grotto, painted in two versions now held in the Louvre and National Gallery, London."),
    ("Salvator Mundi", "Salvator Mundi (Leonardo)", "Leonardo da Vinci (attributed)", "c. 1500", "Italy", "A depiction of Christ as savior of the world that sold in 2017 for a record-breaking auction price."),
    ("The Battle of San Romano", "The Battle of San Romano", "Paolo Uccello", "c. 1438-1440", "Italy", "A three-panel depiction of a Florentine battle, celebrated for its bold experiments with perspective."),
    ("The Tribute Money", "The Tribute Money (Masaccio)", "Masaccio", "c. 1425", "Italy", "A Brancacci Chapel fresco whose naturalistic figures helped launch the early Renaissance."),
    ("Holy Trinity", "Holy Trinity (Masaccio)", "Masaccio", "c. 1427", "Italy", "One of the first paintings to use fully consistent linear perspective, in Santa Maria Novella, Florence."),

    # --- Baroque and Spanish Golden Age ---
    ("The Conversion of Saint Paul", "The Conversion of Saint Paul (Caravaggio)", "Caravaggio", "1601", "Italy", "A dramatically foreshortened depiction of Saul's conversion, painted for the Cerasi Chapel in Rome."),
    ("Judith Beheading Holofernes", "Judith Beheading Holofernes (Caravaggio)", "Caravaggio", "c. 1599", "Italy", "A violently realistic biblical scene rendered in Caravaggio's signature dramatic chiaroscuro."),
    ("Supper at Emmaus", "Supper at Emmaus (Caravaggio, London)", "Caravaggio", "1601", "Italy", "Depicts the moment two disciples recognize the resurrected Christ, rendered with startling immediacy."),
    ("Boy with a Basket of Fruit", "Boy with a Basket of Fruit", "Caravaggio", "c. 1593", "Italy", "An early Caravaggio work admired for its meticulous still-life detail and sensuous realism."),
    ("David with the Head of Goliath", "David with the Head of Goliath (Caravaggio)", "Caravaggio", "c. 1610", "Italy", "A haunting late work in which Goliath's severed head is believed to be a self-portrait of the artist."),
    ("The Art of Painting", "The Art of Painting", "Johannes Vermeer", "c. 1666-1668", "Netherlands", "An allegorical scene of an artist at work, considered Vermeer's most complex and personal composition."),
    ("Woman Holding a Balance", "Woman Holding a Balance", "Johannes Vermeer", "c. 1664", "Netherlands", "A quiet domestic scene celebrated for its symbolic use of light and a scale of judgment."),
    ("Girl with a Red Hat", "Girl with a Red Hat", "Johannes Vermeer", "c. 1665-1666", "Netherlands", "A small tronie noted for its vivid color and Vermeer's rare use of a wood panel support."),
    ("The Lacemaker", "The Lacemaker (Vermeer)", "Johannes Vermeer", "c. 1670-1671", "Netherlands", "An intimate portrayal of intense domestic concentration, among the smallest of Vermeer's works."),
    ("Descent from the Cross", "Descent from the Cross (Rubens)", "Peter Paul Rubens", "1612-1614", "Belgium (Flanders)", "A dynamic Baroque altarpiece for Antwerp Cathedral, prized for its diagonal composition."),
    ("The Garden of Love", "The Garden of Love (Rubens)", "Peter Paul Rubens", "c. 1633", "Belgium (Flanders)", "A joyful late work depicting elegantly dressed couples in a garden of courtship."),
    ("Charles I at the Hunt", "Charles I at the Hunt", "Anthony van Dyck", "c. 1635", "Belgium (Flanders)", "An informal yet majestic equestrian-style portrait of the English king, a landmark of court portraiture."),
    ("The Laughing Cavalier", "The Laughing Cavalier", "Frans Hals", "1624", "Netherlands", "A vividly animated portrait famous for its subject's enigmatic half-smile and elaborate embroidered sleeve."),
    ("The Cheat with the Ace of Diamonds", "The Cheat with the Ace of Diamonds", "Georges de La Tour", "c. 1636-1638", "France", "A candlelit morality scene depicting a card cheat, gambler, and courtesan conspiring together."),
    ("Agnus Dei", "Agnus Dei (Zurbarán)", "Francisco de Zurbarán", "c. 1635-1640", "Spain", "A stark, devotional still life of a bound lamb symbolizing Christ's sacrifice."),
    ("The Young Beggar", "The Young Beggar", "Bartolomé Esteban Murillo", "c. 1645-1650", "Spain", "A sympathetic genre portrait of a poor Seville street child, among the first of its kind."),
    ("Et in Arcadia ego", "Et in Arcadia ego", "Nicolas Poussin", "1637-1638", "France", "Also known as 'The Arcadian Shepherds', a meditation on mortality even amid pastoral idyll."),
    ("The Rape of the Sabine Women", "The Rape of the Sabine Women (Poussin)", "Nicolas Poussin", "1633-1634", "France", "A dynamic Baroque composition depicting the legendary abduction that founded Rome's early population."),
    ("The Return of the Prodigal Son", "The Return of the Prodigal Son (Rembrandt)", "Rembrandt", "c. 1661-1669", "Netherlands", "One of Rembrandt's final and most moving works, depicting the biblical parable of forgiveness."),
    ("Belshazzar's Feast", "Belshazzar's Feast (Rembrandt)", "Rembrandt", "c. 1635-1638", "Netherlands", "A dramatic depiction of the biblical king confronted by the mysterious handwriting on the wall."),
    ("The Storm on the Sea of Galilee", "The Storm on the Sea of Galilee", "Rembrandt", "1633", "Netherlands", "Rembrandt's only seascape, stolen in the notorious 1990 Isabella Stewart Gardner Museum heist."),
    ("The Jewish Bride", "The Jewish Bride", "Rembrandt", "c. 1665-1669", "Netherlands", "A tender double portrait admired by Van Gogh, who said he would give ten years of his life to sit before it."),
    ("The Syndics of the Drapers' Guild", "The Syndics of the Drapers' Guild", "Rembrandt", "1662", "Netherlands", "A masterful group portrait of textile merchants, celebrated for its naturalistic composition."),
    ("Portrait of Innocent X", "Portrait of Innocent X", "Diego Velázquez", "1650", "Spain/Italy", "A penetrating papal portrait Innocent X himself declared 'too truthful'."),
    ("View of Toledo", "View of Toledo", "El Greco", "c. 1596-1600", "Spain", "A dramatic, storm-lit landscape considered one of the greatest depictions of a city in Western art."),
    ("The Burial of the Count of Orgaz", "The Burial of the Count of Orgaz", "El Greco", "1586", "Spain", "A monumental altarpiece depicting a miraculous burial witnessed by saints, angels, and Toledo notables."),

    # --- Rococo ---
    ("The Progress of Love", "The Progress of Love (Fragonard)", "Jean-Honoré Fragonard", "1771-1772", "France", "A four-panel cycle of romantic courtship painted for Madame du Barry's pavilion."),
    ("Pierrot (Gilles)", "Pierrot (Watteau)", "Jean-Antoine Watteau", "c. 1718-1719", "France", "A large, poignant portrait of a melancholy stock comedy character, likely a shop sign for a theatrical costumer."),
    ("Diana Leaving the Bath", "Diana Leaving the Bath", "François Boucher", "1742", "France", "A refined Rococo mythological scene celebrated for its soft palette and sensuous elegance."),

    # --- Neoclassicism and Romanticism ---
    ("La Grande Odalisque", "La Grande Odalisque", "Jean-Auguste-Dominique Ingres", "1814", "France", "An elongated, idealized reclining nude that scandalized critics for its anatomical distortions."),
    ("The Turkish Bath", "The Turkish Bath", "Jean-Auguste-Dominique Ingres", "1862", "France", "A crowded circular composition of nude bathers, painted when Ingres was in his eighties."),
    ("The Death of Sardanapalus", "The Death of Sardanapalus", "Eugène Delacroix", "1827", "France", "A violent, opulent Romantic scene of an Assyrian king ordering the destruction of his possessions."),
    ("Rain, Steam and Speed", "Rain, Steam and Speed", "J. M. W. Turner", "1844", "United Kingdom", "A blurred, atmospheric vision of a steam locomotive crossing the Thames, anticipating Impressionism."),
    ("The Slave Ship", "The Slave Ship", "J. M. W. Turner", "1840", "United Kingdom", "A searing depiction of enslaved people thrown overboard, painted in swirling color to evoke moral horror."),
    ("Snow Storm: Hannibal and His Army Crossing the Alps", "Snow Storm: Hannibal and His Army Crossing the Alps", "J. M. W. Turner", "1812", "United Kingdom", "A turbulent landscape dwarfing Hannibal's army beneath a swirling Alpine storm."),
    ("The Sea of Ice", "The Sea of Ice", "Caspar David Friedrich", "1823-1824", "Germany", "A bleak arctic seascape of shattered ice floes, also known as 'The Wreck of Hope'."),
    ("The Abbey in the Oakwood", "The Abbey in the Oakwood", "Caspar David Friedrich", "1809-1810", "Germany", "A somber Romantic ruin scene evoking mortality and the passage of time."),
    ("Charles IV of Spain and His Family", "Charles IV of Spain and His Family", "Francisco Goya", "1800-1801", "Spain", "A royal group portrait notable for its unflattering candor toward the Spanish monarchy."),
    ("The Nude Maja", "La maja desnuda", "Francisco Goya", "c. 1797-1800", "Spain", "One of the earliest Western paintings of a nude woman's pubic hair depicted without mythological pretext."),
    ("The Clothed Maja", "La maja vestida", "Francisco Goya", "c. 1800-1807", "Spain", "A companion piece to the Nude Maja, painted with the same model in the same pose, fully dressed."),
    ("The Charging Chasseur", "The Charging Chasseur", "Théodore Géricault", "1812", "France", "A dynamic equestrian portrait of a Napoleonic officer that launched Géricault's career."),

    # --- Realism ---
    ("The Stone Breakers", "The Stone Breakers", "Gustave Courbet", "1849", "France", "A monumental depiction of anonymous laborers that helped define the Realist movement (destroyed in WWII)."),
    ("A Burial at Ornans", "A Burial at Ornans", "Gustave Courbet", "1849-1850", "France", "A vast, unidealized depiction of a provincial funeral that scandalized the Paris art establishment."),
    ("The Origin of the World", "The Origin of the World", "Gustave Courbet", "1866", "France", "A frankly explicit close-up nude that remained controversial for over a century."),
    ("The Gleaners", "The Gleaners", "Jean-François Millet", "1857", "France", "A sympathetic depiction of three peasant women gathering leftover grain after harvest."),
    ("The Angelus", "The Angelus (Millet)", "Jean-François Millet", "1857-1859", "France", "A quiet scene of peasants pausing in prayer at dusk, later reinterpreted by Salvador Dalí."),
    ("The Fifer", "The Fifer (Manet)", "Édouard Manet", "1866", "France", "A flatly rendered portrait of a young military musician that influenced later modernist painting."),
    ("The Execution of Emperor Maximilian", "The Execution of Emperor Maximilian", "Édouard Manet", "1868-1869", "France", "A politically charged series depicting the execution of the French-installed emperor of Mexico."),

    # --- Impressionism (deeper cuts) ---
    ("Rouen Cathedral Series", "Rouen Cathedral (Monet series)", "Claude Monet", "1892-1894", "France", "A series of over 30 canvases capturing the same Gothic façade under changing light."),
    ("Woman with a Parasol - Madame Monet and Her Son", "Woman with a Parasol - Madame Monet and Her Son", "Claude Monet", "1875", "France", "A breezy, sunlit portrait of Monet's wife and son, celebrated for its sense of movement."),
    ("The Water-Lily Pond", "The Water-Lily Pond", "Claude Monet", "1899", "France", "An early painting of Monet's Japanese footbridge at Giverny, precursor to his later Water Lilies series."),
    ("The Magpie", "The Magpie", "Claude Monet", "1868-1869", "France", "A snow-covered landscape prized for its subtle handling of shadow and light on white."),
    ("The Umbrellas", "The Umbrellas (Renoir)", "Pierre-Auguste Renoir", "c. 1881-1886", "France", "A Parisian street scene notable for spanning Renoir's transition from soft Impressionism to a crisper style."),
    ("Boulevard Montmartre at Night", "Boulevard Montmartre at Night", "Camille Pissarro", "1897", "France", "A rare nocturnal cityscape from Pissarro's celebrated Parisian boulevard series."),
    ("Snow at Louveciennes", "Snow at Louveciennes", "Alfred Sisley", "1878", "France", "A tranquil winter street scene exemplifying Sisley's mastery of snow-covered light."),
    ("The Cradle", "The Cradle (Morisot)", "Berthe Morisot", "1872", "France", "An intimate maternal scene and one of the defining works of the Impressionist movement's founding exhibition."),
    ("The Child's Bath", "The Child's Bath", "Mary Cassatt", "1893", "United States/France", "A tender domestic scene influenced by Japanese prints, showing a mother bathing her child."),
    ("The Boating Party", "The Boating Party (Cassatt)", "Mary Cassatt", "1893-1894", "United States/France", "An unusually bold composition depicting a sailing outing, notable for its flattened perspective."),

    # --- Post-Impressionism (deeper cuts) ---
    ("The Large Bathers", "The Large Bathers (Cézanne)", "Paul Cézanne", "1898-1905", "France", "A monumental late work of nude bathers that profoundly influenced the development of Cubism."),
    ("The Basket of Apples", "The Basket of Apples", "Paul Cézanne", "c. 1893", "France", "A still life exploring multiple, shifting perspectives that anticipated Cubist experimentation."),
    ("Vision of the Sermon", "Vision of the Sermon", "Paul Gauguin", "1888", "France", "A boldly flattened, non-naturalistic scene of Breton women envisioning Jacob wrestling the angel."),
    ("Spirit of the Dead Watching", "Spirit of the Dead Watching", "Paul Gauguin", "1892", "France (painted in Tahiti)", "A Tahitian-period painting exploring local spirit beliefs, among Gauguin's most discussed works."),
    ("Bathers at Asnières", "Bathers at Asnières", "Georges Seurat", "1884", "France", "An early large-scale work by Seurat depicting workers relaxing by the Seine, painted before his pointillist style matured."),
    ("The Circus", "The Circus (Seurat)", "Georges Seurat", "1891", "France", "Seurat's unfinished final painting, capturing the dynamism of a circus performance in pointillist technique."),
    ("Moulin Rouge: La Goulue", "Moulin Rouge: La Goulue", "Henri de Toulouse-Lautrec", "1891", "France", "A groundbreaking lithographic poster that helped elevate commercial printmaking to fine art."),
    ("The Sower", "The Sower (Van Gogh)", "Vincent van Gogh", "1888", "France", "A vividly colored homage to Millet, depicting a peasant sowing seed beneath a radiant sun."),
    ("Almond Blossoms", "Almond Blossoms", "Vincent van Gogh", "1890", "France", "A joyful painting made to celebrate the birth of van Gogh's nephew, inspired by Japanese prints."),
    ("Van Gogh's Chair", "Van Gogh's Chair", "Vincent van Gogh", "1888", "France", "A humble still life of the artist's own chair, symbolically paired with a painting of Gauguin's chair."),
    ("Starry Night Over the Rhône", "Starry Night Over the Rhône", "Vincent van Gogh", "1888", "France", "A nocturnal riverside scene painted in Arles, predating van Gogh's more famous asylum-period Starry Night."),

    # --- Symbolism ---
    ("The Cyclops", "The Cyclops (Redon)", "Odilon Redon", "c. 1914", "France", "A dreamlike Symbolist painting of the giant Polyphemus gazing tenderly at the sleeping nymph Galatea."),
    ("Oedipus and the Sphinx", "Oedipus and the Sphinx (Moreau)", "Gustave Moreau", "1864", "France", "A richly detailed Symbolist reimagining of the mythical riddle confrontation."),
    ("Isle of the Dead", "Isle of the Dead (painting)", "Arnold Böcklin", "1880-1886", "Switzerland", "A haunting, much-reproduced image of a boat approaching a mysterious funerary island."),
    ("Madonna", "Madonna (Munch)", "Edvard Munch", "1894-1895", "Norway", "A sensuous and unsettling reinterpretation of the Madonna, blending eroticism and mortality."),
    ("The Sick Child", "The Sick Child", "Edvard Munch", "1885-1886", "Norway", "A raw, emotionally charged painting inspired by the death of Munch's sister from tuberculosis."),
    ("Puberty", "Puberty (painting)", "Edvard Munch", "1894-1895", "Norway", "A stark portrait of an adolescent girl confronting the anxieties of adolescence."),

    # --- Expressionism ---
    ("Street, Berlin", "Street, Berlin", "Ernst Ludwig Kirchner", "1913", "Germany", "A jagged, anxious depiction of Berlin street life and prostitution, key to German Expressionism."),
    ("Self-Portrait as a Soldier", "Self-Portrait as a Soldier", "Ernst Ludwig Kirchner", "1915", "Germany", "A disturbing self-portrait with a severed hand, expressing Kirchner's psychological trauma from World War I."),
    ("On White II", "On White II", "Wassily Kandinsky", "1923", "Russia/Germany", "A geometric abstraction from Kandinsky's Bauhaus period, contrasting sharp forms against a white field."),
    ("Yellow-Red-Blue", "Yellow-Red-Blue", "Wassily Kandinsky", "1925", "Russia/Germany", "A large abstract composition balancing primary colors and geometric forms."),
    ("Self-Portrait with Physalis", "Self-Portrait with Physalis", "Egon Schiele", "1912", "Austria", "A raw, anxious self-portrait typical of Schiele's expressive, angular figuration."),
    ("The Embrace", "The Embrace (Schiele)", "Egon Schiele", "1917", "Austria", "A tender depiction of two entwined lovers, painted near the end of Schiele's short life."),
    ("The Last Supper", "The Last Supper (Nolde)", "Emil Nolde", "1909", "Germany", "A boldly colored Expressionist reimagining of the biblical scene, radically different from Renaissance treatments."),

    # --- Cubism ---
    ("Violin and Candlestick", "Violin and Candlestick", "Georges Braque", "1910", "France", "An early Analytic Cubist still life fracturing form into interlocking planes."),
    ("Houses at L'Estaque", "Houses at L'Estaque", "Georges Braque", "1908", "France", "A landscape whose blocky, geometric forms gave Cubism its name, coined by critic Louis Vauxcelles."),
    ("Portrait of Ambroise Vollard", "Portrait of Ambroise Vollard (Picasso)", "Pablo Picasso", "1910", "Spain/France", "An Analytic Cubist portrait of the influential Parisian art dealer, fragmenting his likeness into facets."),
    ("Three Musicians", "Three Musicians (Picasso)", "Pablo Picasso", "1921", "Spain/France", "A Synthetic Cubist composition of masked figures in flat, boldly colored shapes."),
    ("La Vie", "La Vie (Picasso)", "Pablo Picasso", "1903", "Spain", "A somber, allegorical painting from Picasso's Blue Period exploring love, poverty, and mortality."),
    ("Three Women", "Three Women (Léger)", "Fernand Léger", "1921-1922", "France", "A monumental Cubist-influenced painting of reclining nudes rendered in tubular, machine-like forms."),
    ("Portrait of Pablo Picasso", "Portrait of Pablo Picasso (Gris)", "Juan Gris", "1912", "Spain/France", "A geometric Cubist tribute portrait of Picasso by his friend and fellow Spanish Cubist."),

    # --- Fauvism ---
    ("Woman with a Hat", "Woman with a Hat", "Henri Matisse", "1905", "France", "A boldly colored portrait of Matisse's wife that gave the Fauvist movement its scandalous debut."),
    ("The Joy of Life", "The Joy of Life", "Henri Matisse", "1905-1906", "France", "A large, vividly colored pastoral scene celebrated as a landmark of early modern painting."),
    ("Charing Cross Bridge, London", "Charing Cross Bridge, London", "André Derain", "1906", "France", "A Fauvist view of London rendered in unnaturalistic, vibrant color."),

    # --- Futurism ---
    ("Dynamism of a Dog on a Leash", "Dynamism of a Dog on a Leash", "Giacomo Balla", "1912", "Italy", "A playful Futurist study of motion, multiplying a dachshund's legs to suggest movement."),
    ("The City Rises", "The City Rises", "Umberto Boccioni", "1910", "Italy", "A dynamic depiction of urban construction and labor, considered one of the first Futurist masterpieces."),

    # --- Surrealism beyond Dalí (and deeper Dalí cuts) ---
    ("The Temptation of St. Anthony", "The Temptation of St. Anthony (Dalí)", "Salvador Dalí", "1946", "Spain", "A hallucinatory scene of elephants on impossibly thin legs looming over a tormented saint."),
    ("Swans Reflecting Elephants", "Swans Reflecting Elephants", "Salvador Dalí", "1937", "Spain", "A double-image Surrealist landscape in which swans' reflections transform into elephants."),
    ("The Sacrament of the Last Supper", "The Sacrament of the Last Supper", "Salvador Dalí", "1955", "Spain", "A luminous, geometric reinterpretation of the Last Supper blending Surrealism and Catholic mysticism."),
    ("The Empire of Light", "The Empire of Light", "René Magritte", "1953-1954", "Belgium", "A series of paintings pairing a darkened nighttime street with a bright daytime sky, defying logic."),
    ("Golconda", "Golconda (painting)", "René Magritte", "1953", "Belgium", "A surreal scene of identical bowler-hatted men raining down over a townscape."),
    ("The Human Condition", "The Human Condition (Magritte)", "René Magritte", "1933", "Belgium", "A painting-within-a-painting exploring the boundary between representation and reality."),
    ("The Farm", "The Farm (Miró)", "Joan Miró", "1921-1922", "Spain", "A meticulously detailed depiction of Miró's family farm, later owned by Ernest Hemingway."),
    ("Harlequin's Carnival", "Harlequin's Carnival", "Joan Miró", "1924-1925", "Spain", "A whimsical, biomorphic Surrealist fantasy crowded with playful abstract creatures."),
    ("The Elephant Celebes", "The Elephant Celebes", "Max Ernst", "1921", "Germany/France", "An early Surrealist masterpiece combining a mechanical elephant-form with a headless female figure."),
    ("Europe After the Rain II", "Europe After the Rain II", "Max Ernst", "1940-1942", "Germany/France", "A haunting decalcomania landscape evoking the devastation of World War II."),
    ("Mama, Papa Is Wounded!", "Mama, Papa Is Wounded!", "Yves Tanguy", "1927", "France", "A biomorphic dreamscape populated by ambiguous, shadow-casting forms."),

    # --- Latin American modern art ---
    ("Dream of a Sunday Afternoon in Alameda Central Park", "Dream of a Sunday Afternoon in Alameda Central Park", "Diego Rivera", "1946-1947", "Mexico", "A vast mural gathering figures from four centuries of Mexican history in a single park scene."),
    ("The Flower Carrier", "The Flower Carrier", "Diego Rivera", "1935", "Mexico", "A depiction of a laborer straining beneath an enormous basket of flowers, a recurring Rivera theme."),
    ("Echo of a Scream", "Echo of a Scream", "David Alfaro Siqueiros", "1937", "Mexico", "A nightmarish anti-war image of a screaming child amid industrial wreckage."),
    ("Epic of American Civilization", "Epic of American Civilization", "José Clemente Orozco", "1932-1934", "Mexico/United States", "A monumental mural cycle at Dartmouth College tracing the history of the Americas."),
    ("The Jungle", "The Jungle (painting)", "Wifredo Lam", "1943", "Cuba", "A large, dense composition fusing Afro-Cuban imagery, Cubism, and Surrealism."),
    ("Abaporu", "Abaporu", "Tarsila do Amaral", "1928", "Brazil", "A foundational painting of Brazilian modernism that inspired the Anthropophagic Manifesto."),
    ("The Broken Column", "The Broken Column", "Frida Kahlo", "1944", "Mexico", "A searing self-portrait depicting Kahlo's chronic physical pain through a shattered classical column."),
    ("Self-Portrait with Cropped Hair", "Self-Portrait with Cropped Hair", "Frida Kahlo", "1940", "Mexico", "A defiant self-portrait painted after Kahlo's divorce from Diego Rivera, dressed in a man's suit."),
    ("Henry Ford Hospital", "Henry Ford Hospital (painting)", "Frida Kahlo", "1932", "Mexico", "A raw depiction of Kahlo's miscarriage, painted while she was recovering in a Detroit hospital."),
    ("The Wounded Deer", "The Wounded Deer", "Frida Kahlo", "1946", "Mexico", "A surreal self-portrait as a wounded stag pierced by arrows, symbolizing chronic suffering."),

    # --- American art ---
    ("Parson Weems' Fable", "Parson Weems' Fable", "Grant Wood", "1939", "United States", "A satirical retelling of the legend of young George Washington and the cherry tree."),
    ("Automat", "Automat (painting)", "Edward Hopper", "1927", "United States", "A solitary woman sits at a cafeteria table, embodying Hopper's recurring theme of urban isolation."),
    ("Early Sunday Morning", "Early Sunday Morning (painting)", "Edward Hopper", "1930", "United States", "A quiet streetscape of empty storefronts bathed in early light, an icon of American realism."),
    ("Black Iris", "Black Iris III", "Georgia O'Keeffe", "1926", "United States", "A dramatically enlarged, close-cropped flower painting central to O'Keeffe's modernist reputation."),
    ("Cow's Skull: Red, White, and Blue", "Cow's Skull: Red, White, and Blue", "Georgia O'Keeffe", "1931", "United States", "A stark desert skull painting O'Keeffe intended as a wry comment on American identity."),
    ("The Gulf Stream", "The Gulf Stream (painting)", "Winslow Homer", "1899", "United States", "A dramatic depiction of a lone sailor adrift amid sharks and a coming storm."),
    ("Snap the Whip", "Snap the Whip", "Winslow Homer", "1872", "United States", "A nostalgic scene of rural schoolchildren playing a game, evoking post-Civil War Americana."),
    ("Madame X", "Madame X (painting)", "John Singer Sargent", "1884", "United States/France", "A daringly elegant portrait whose scandalous reception drove Sargent to relocate to London."),
    ("Carnation, Lily, Lily, Rose", "Carnation, Lily, Lily, Rose", "John Singer Sargent", "1885-1886", "United States/United Kingdom", "A luminous twilight scene of two girls lighting Japanese lanterns in an English garden."),
    ("The Gross Clinic", "The Gross Clinic", "Thomas Eakins", "1875", "United States", "A stark, unflinching depiction of surgery in a teaching hospital, notable for its realism."),
    ("The Heart of the Andes", "The Heart of the Andes", "Frederic Edwin Church", "1859", "United States", "A monumental panoramic landscape that drew massive paying crowds when first exhibited."),
    ("Among the Sierra Nevada, California", "Among the Sierra Nevada, California", "Albert Bierstadt", "1868", "United States", "A luminous, idealized panorama celebrated for popularizing the grandeur of the American West."),
    ("Washington Crossing the Delaware", "Washington Crossing the Delaware (painting)", "Emanuel Leutze", "1851", "United States", "An iconic, historically embellished depiction of Washington's 1776 crossing of the Delaware River."),
    ("Nocturne in Black and Gold – The Falling Rocket", "Nocturne in Black and Gold – The Falling Rocket", "James McNeill Whistler", "1875", "United States/United Kingdom", "An abstract fireworks scene that sparked a famous libel suit after critic John Ruskin denounced it."),

    # --- Abstract Expressionism, Pop, and postwar American art ---
    ("White Center", "White Center (Yellow, Pink and Lavender on Rose)", "Mark Rothko", "1950", "United States", "A luminous color-field painting that sold in 2007 for a then-record price for a Rothko work."),
    ("Excavation", "Excavation (De Kooning)", "Willem de Kooning", "1950", "United States", "A monumental gestural abstraction of interlocking fragmented figures and forms."),
    ("Mountains and Sea", "Mountains and Sea", "Helen Frankenthaler", "1952", "United States", "A pioneering soak-stain painting that launched the Color Field movement."),
    ("The Liver Is the Cock's Comb", "The Liver is the Cock's Comb", "Arshile Gorky", "1944", "United States", "A biomorphic abstraction considered a bridge between Surrealism and Abstract Expressionism."),
    ("Eight Elvises", "Eight Elvises", "Andy Warhol", "1963", "United States", "A silkscreen repetition of Elvis Presley as a gunslinger, among the most expensive artworks ever privately sold."),
    ("Green Coca-Cola Bottles", "Green Coca-Cola Bottles", "Andy Warhol", "1962", "United States", "A grid of repeated soda bottles exploring mass production and consumer culture."),
    ("Look Mickey", "Look Mickey", "Roy Lichtenstein", "1961", "United States", "A comic-strip-derived painting widely regarded as Lichtenstein's breakthrough Pop Art work."),
    ("Boy and Dog in a Johnnypump", "Boy and Dog in a Johnnypump", "Jean-Michel Basquiat", "1982", "United States", "A large Neo-Expressionist canvas exemplifying Basquiat's raw, graffiti-inflected style."),

    # --- British art ---
    ("Portrait of Omai", "Portrait of Omai", "Joshua Reynolds", "c. 1776", "United Kingdom", "A grand portrait of a Pacific Islander visitor to Britain, blending classical pose with ethnographic curiosity."),
    ("Marriage A-la-Mode", "Marriage A-la-Mode (Hogarth)", "William Hogarth", "c. 1743", "United Kingdom", "A satirical series of six paintings chronicling the disastrous marriage of an arranged aristocratic match."),
    ("A Rake's Progress", "A Rake's Progress", "William Hogarth", "1732-1734", "United Kingdom", "A moralizing series depicting a young heir's descent into debauchery and ruin."),
    ("The Ancient of Days", "The Ancient of Days", "William Blake", "1794", "United Kingdom", "A visionary frontispiece depicting a divine figure measuring the universe with a compass."),
    ("Newton", "Newton (Blake)", "William Blake", "1795-1805", "United Kingdom", "A color-printed depiction of the scientist as a heroic yet critically limited figure of pure reason."),
    ("Beata Beatrix", "Beata Beatrix", "Dante Gabriel Rossetti", "c. 1864-1870", "United Kingdom", "A Pre-Raphaelite memorial portrait symbolizing the death of Rossetti's wife through Dante's Beatrice."),
    ("Proserpine", "Proserpine (Rossetti)", "Dante Gabriel Rossetti", "1874", "United Kingdom", "A brooding portrait of the mythological queen of the underworld, modeled on Jane Morris."),
    ("The Light of the World", "The Light of the World (painting)", "William Holman Hunt", "1851-1853", "United Kingdom", "A widely reproduced allegorical image of Christ knocking at an overgrown, handle-less door."),
    ("The Golden Stairs", "The Golden Stairs", "Edward Burne-Jones", "1880", "United Kingdom", "A procession of eighteen similarly robed women descending a spiral staircase, prized for its rhythmic composition."),

    # --- Belgian Expressionism and Russian-French modernism ---
    ("Christ's Entry into Brussels in 1889", "Christ's Entry into Brussels in 1889", "James Ensor", "1888", "Belgium", "A chaotic, mask-filled carnival crowd satirizing modern society, with Christ nearly lost among the throng."),
    ("I and the Village", "I and the Village", "Marc Chagall", "1911", "Russia/France", "A dreamlike, fragmented vision of Chagall's Belarusian village rendered in vivid, folkloric color."),
    ("The Green Violinist", "Green Violinist", "Marc Chagall", "1923-1924", "Russia/France", "A whimsical, floating fiddler evoking Chagall's memories of Hasidic village life."),

    # --- Impressionism/Realism (additional) ---
    ("The Bellelli Family", "The Bellelli Family", "Edgar Degas", "1858-1867", "France", "An early masterwork portraying Degas's aunt's family with psychological tension beneath formal composition."),

    # --- Japanese ukiyo-e beyond Hokusai's Great Wave ---
    ("Plum Park in Kameido", "Plum Park in Kameido", "Utagawa Hiroshige", "1857", "Japan", "A striking close-up composition of a flowering plum tree, later copied in oil by Vincent van Gogh."),
    ("Sudden Shower over Shin-Ōhashi Bridge and Atake", "Sudden Shower over Shin-Ōhashi bridge and Atake", "Utagawa Hiroshige", "1857", "Japan", "A rain-swept bridge scene from '100 Famous Views of Edo', also copied by van Gogh."),
    ("The Fifty-three Stations of the Tōkaidō", "The Fifty-three Stations of the Tōkaidō", "Utagawa Hiroshige", "1833-1834", "Japan", "A celebrated woodblock series depicting the stations along the great road linking Edo and Kyoto."),
    ("Three Beauties of the Present Day", "Three Beauties of the Present Day", "Kitagawa Utamaro", "c. 1793", "Japan", "A refined bust portrait of three renowned beauties of Edo, epitomizing Utamaro's portraiture style."),
    ("Fine Wind, Clear Morning", "Fine Wind, Clear Morning", "Katsushika Hokusai", "c. 1830-1832", "Japan", "Also known as 'Red Fuji', a striking print from the Thirty-six Views of Mount Fuji series."),
    ("Thirty-six Views of Mount Fuji", "Thirty-six Views of Mount Fuji", "Katsushika Hokusai", "1830-1832", "Japan", "The landmark woodblock print series that includes both the Great Wave and Red Fuji."),
    ("Ōtani Oniji III", "Ōtani Oniji III", "Tōshūsai Sharaku", "1794", "Japan", "A vivid, psychologically intense kabuki actor portrait by ukiyo-e's most mysterious master."),

    # --- Chinese classical painting ---
    ("Admonitions of the Instructress to the Court Ladies", "Admonitions Scroll", "Attributed to Gu Kaizhi (early copy)", "c. 5th-8th century", "China", "One of the earliest and most celebrated surviving Chinese narrative handscroll paintings."),
    ("Travelers among Mountains and Streams", "Travelers among Mountains and Streams", "Fan Kuan", "c. 1000", "China", "A towering monumental landscape considered one of the greatest works of Chinese painting."),
    ("Early Spring", "Early Spring (painting)", "Guo Xi", "1072", "China", "A masterwork of Song-dynasty landscape painting celebrated for its atmospheric use of ink wash."),
    ("Autumn Colors on the Qiao and Hua Mountains", "Autumn Colors on the Qiao and Hua Mountains", "Zhao Mengfu", "1295", "China", "A Yuan-dynasty landscape scroll blending archaic style with personal expression."),

    # --- Indian miniature painting (Mughal / Rajput) ---
    ("Padshahnama Illustrations", "Padshahnama", "Mughal court painters", "17th century", "India", "A richly illustrated chronicle of Emperor Shah Jahan's reign, among the finest Mughal manuscripts."),
    ("Hamzanama Illustrations", "Hamzanama", "Mughal court painters (under Akbar)", "1562-1577", "India", "A vast illustrated manuscript cycle recounting the legendary adventures of Amir Hamza."),
    ("Bani Thani", "Bani Thani", "Nihal Chand", "c. 1750", "India", "A celebrated Rajasthani miniature portrait often called 'India's Mona Lisa'."),
    ("Jahangir Preferring a Sufi Shaikh to Kings", "Jahangir preferring a Sufi Shaikh to Kings", "Bichitr", "c. 1615-1618", "India", "An allegorical Mughal miniature depicting Emperor Jahangir favoring spiritual over worldly power."),
    ("Akbarnama Illustrations", "Akbarnama", "Mughal court painters", "c. 1590-1595", "India", "The richly illustrated official chronicle of Emperor Akbar's reign."),

    # --- African modern art ---
    ("Tutu", "Tutu (painting)", "Ben Enwonwu", "1974", "Nigeria", "A celebrated portrait of a Yoruba princess, often called the 'African Mona Lisa'."),

    # --- Aboriginal Australian art ---
    ("Warlugulong", "Warlugulong", "Clifford Possum Tjapaltjarri", "1977", "Australia", "A major Papunya Tula dot painting depicting ancestral fire and creation stories of the Western Desert."),
    ("Earth's Creation", "Earth's Creation", "Emily Kame Kngwarreye", "1994", "Australia", "A monumental abstract painting that set a record price for a work by an Australian female artist."),

    # --- Byzantine, medieval, and early icon painting ---
    ("Theotokos of Vladimir", "Theotokos of Vladimir", "Unknown (Byzantine icon painter)", "c. 1100", "Byzantine Empire/Russia", "One of the most venerated icons in Orthodox Christianity, believed to have miraculous powers."),
    ("The Trinity", "Trinity (Andrei Rublev)", "Andrei Rublev", "c. 1425-1427", "Russia", "Considered the greatest achievement of Russian icon painting, depicting three angels at Abraham's table."),
    ("Maestà", "Maestà (Duccio)", "Duccio di Buoninsegna", "1308-1311", "Italy", "A monumental altarpiece for Siena Cathedral that helped define the Sienese school of painting."),
    ("Lamentation of Christ", "Lamentation (Giotto)", "Giotto di Bondone", "c. 1305", "Italy", "A Scrovegni Chapel fresco whose emotional realism marked a turning point toward Renaissance painting."),
]
CATEGORY_ASSIGNMENTS.append((MORE_PAINTINGS_BATCH2, "painting"))

# Real, individually famous science / technology / transportation artifacts
# held in real museums (Smithsonian, Science Museum London, Deutsches
# Museum, Royal Museums Greenwich, etc.). Each wiki_title is the exact
# English Wikipedia article title used to fetch a live thumbnail.
SCIENCE_TECH_BATCH2: list[tuple] = [
    # --- Early computing & calculating machines ---
    ("Antikythera mechanism", "Antikythera mechanism", "Unknown Greek engineers", "c. 150-100 BC", "Greece", "An ancient Greek analog device used to predict astronomical positions and eclipses, considered the earliest known analog computer."),
    ("Difference Engine No. 2", "Difference engine", "Charles Babbage", "1849 (built 1991)", "United Kingdom", "A mechanical calculator designed by Charles Babbage to automatically compute polynomial tables without human error."),
    ("Analytical Engine", "Analytical Engine", "Charles Babbage", "1837 (design)", "United Kingdom", "A proposed mechanical general-purpose computer design that introduced concepts such as a central processing unit and memory, programmed via punched cards."),
    ("Jacquard loom", "Jacquard machine", "Joseph Marie Jacquard", "1804", "France", "A mechanical loom attachment that used punched cards to control weaving patterns, later inspiring early computer programming methods."),
    ("Enigma machine", "Enigma machine", "Arthur Scherbius", "1918", "Germany", "A cipher machine used by German military forces to encrypt secret communications during World War II."),
    ("Bombe", "Bombe", "Alan Turing and Gordon Welchman", "1939", "United Kingdom", "An electromechanical device used by British codebreakers at Bletchley Park to help decipher German Enigma-encrypted messages."),
    ("Colossus computer", "Colossus computer", "Tommy Flowers", "1943", "United Kingdom", "The world's first programmable electronic digital computer, built to break the German Lorenz cipher during World War II."),
    ("Harvard Mark I", "Harvard Mark I", "IBM and Howard Aiken", "1944", "United States", "An early electromechanical computer used to perform long calculations automatically for the U.S. Navy during World War II."),
    ("ENIAC", "ENIAC", "John Mauchly and J. Presper Eckert", "1945", "United States", "One of the earliest general-purpose electronic digital computers, capable of being reprogrammed to solve a wide range of numerical problems."),
    ("Manchester Baby", "Manchester Baby", "Frederic Williams and Tom Kilburn", "1948", "United Kingdom", "The first electronic computer to run a stored program, demonstrating the practicality of stored-program computing."),
    ("Z3 computer", "Z3 (computer)", "Konrad Zuse", "1941", "Germany", "The world's first working programmable, fully automatic digital computer, built using electromechanical relays."),
    ("UNIVAC I", "UNIVAC I", "J. Presper Eckert and John Mauchly", "1951", "United States", "The first commercially produced electronic digital computer in the United States, famous for predicting the 1952 presidential election."),
    ("IBM 701", "IBM 701", "IBM", "1952", "United States", "IBM's first commercial scientific computer, marking the company's entry into the electronic computer business."),
    ("Curta calculator", "Curta", "Curt Herzstark", "1948", "Austria", "A compact hand-cranked mechanical calculator small enough to fit in a pocket, prized for its precision engineering."),
    ("Pascaline", "Pascal's calculator", "Blaise Pascal", "1642", "France", "One of the earliest mechanical calculators, invented to help perform addition and subtraction automatically."),
    ("Napier's bones", "Napier's bones", "John Napier", "1617", "Scotland", "A manually operated calculating device using numbered rods to perform multiplication and division through a lattice method."),
    ("Cray-1", "Cray-1", "Seymour Cray", "1976", "United States", "A pioneering supercomputer known for its distinctive C-shaped design and record-breaking processing speed."),
    ("Xerox Alto", "Xerox Alto", "Xerox PARC", "1973", "United States", "An early personal computer that pioneered the graphical user interface, mouse, and Ethernet networking."),
    ("Kenbak-1", "Kenbak-1", "John Blankenbaker", "1971", "United States", "Widely regarded as the first personal computer, though it predated the microprocessor and sold only a small number of units."),
    ("Altair 8800", "Altair 8800", "Micro Instrumentation and Telemetry Systems", "1975", "United States", "An early microcomputer kit that sparked the home computer revolution and inspired the founding of Microsoft."),
    # --- Personal computing & consumer electronics ---
    ("Apple I", "Apple I", "Steve Wozniak and Steve Jobs", "1976", "United States", "A hand-built computer that launched Apple Computer, designed largely by Steve Wozniak and sold as an assembled circuit board."),
    ("Apple Lisa", "Apple Lisa", "Apple Computer", "1983", "United States", "One of the first personal computers to feature a graphical user interface and mouse aimed at business users."),
    ("Macintosh 128K", "Macintosh 128K", "Apple Computer", "1984", "United States", "The original Macintosh computer, introduced with a famous Super Bowl advertisement and a pioneering graphical interface."),
    ("Commodore 64", "Commodore 64", "Commodore International", "1982", "United States", "The best-selling single computer model of all time, popular for home computing and video games in the 1980s."),
    ("Commodore PET", "Commodore PET", "Commodore International", "1977", "United States", "One of the first all-in-one personal computers to reach mass production, combining a keyboard, monitor, and cassette drive."),
    ("TRS-80", "TRS-80", "Tandy Corporation", "1977", "United States", "An early mass-produced microcomputer sold through Radio Shack stores, one of the \"1977 Trinity\" of home computers."),
    ("ZX Spectrum", "ZX Spectrum", "Sinclair Research", "1982", "United Kingdom", "A popular low-cost home computer that helped launch the British video game industry."),
    ("Osborne 1", "Osborne 1", "Osborne Computer Corporation", "1981", "United States", "The first commercially successful portable computer, featuring a small built-in screen and carrying handle."),
    ("IBM Personal Computer", "IBM Personal Computer", "IBM", "1981", "United States", "The original IBM PC, model 5150, which established the dominant architecture for personal computers for decades."),
    ("Atari 2600", "Atari 2600", "Atari, Inc.", "1977", "United States", "A pioneering home video game console that popularized the use of interchangeable game cartridges."),
    ("Nintendo Entertainment System", "Nintendo Entertainment System", "Nintendo", "1985", "Japan", "A home video game console credited with revitalizing the video game industry in North America after the crash of 1983."),
    ("PalmPilot", "PalmPilot", "Palm, Inc.", "1997", "United States", "A popular early personal digital assistant that set the standard for handheld computing and touchscreen note-taking."),
    ("Motorola DynaTAC 8000x", "Motorola DynaTAC 8000x", "Motorola", "1983", "United States", "The first commercially available handheld mobile telephone, nicknamed \"the brick\" for its size and weight."),
    ("IBM Simon", "IBM Simon", "IBM and BellSouth", "1994", "United States", "Widely regarded as the first smartphone, combining a mobile phone with calendar, notepad, and touchscreen features."),
    ("Sony Walkman TPS-L2", "Walkman", "Sony", "1979", "Japan", "The original portable cassette player that popularized personal, on-the-go music listening worldwide."),
    # --- Robotics ---
    ("Unimate", "Unimate", "George Devol", "1961", "United States", "The first digitally operated and programmable industrial robot, installed on a General Motors assembly line."),
    ("Shakey the robot", "Shakey the robot", "Stanford Research Institute", "1966", "United States", "The first mobile robot able to reason about its own actions, considered a milestone in artificial intelligence research."),
    ("Sojourner rover", "Sojourner (rover)", "NASA Jet Propulsion Laboratory", "1997", "United States", "The first wheeled rover to operate on the surface of Mars, part of the Mars Pathfinder mission."),
    # --- Space exploration ---
    ("Sputnik 1", "Sputnik 1", "Soviet Union space program", "1957", "Soviet Union", "The first artificial satellite launched into orbit, marking the start of the Space Age."),
    ("Explorer 1", "Explorer 1", "Jet Propulsion Laboratory", "1958", "United States", "The first satellite launched by the United States, which discovered the Van Allen radiation belts."),
    ("Vostok 1", "Vostok 1", "Soviet Union space program", "1961", "Soviet Union", "The spacecraft that carried Yuri Gagarin on the first human spaceflight in history."),
    ("Freedom 7", "Freedom 7", "NASA / McDonnell Aircraft", "1961", "United States", "The Mercury capsule that carried Alan Shepard on the first American human spaceflight."),
    ("Friendship 7", "Friendship 7", "NASA / McDonnell Aircraft", "1962", "United States", "The Mercury spacecraft that carried John Glenn as the first American to orbit the Earth."),
    ("Telstar", "Telstar", "Bell Telephone Laboratories", "1962", "United States", "The first active communications satellite, which relayed the first live transatlantic television broadcast."),
    ("Luna 3", "Luna 3", "Soviet Union space program", "1959", "Soviet Union", "The Soviet probe that captured the first photographs of the far side of the Moon."),
    ("Gemini 3 spacecraft", "Gemini 3", "NASA / McDonnell Aircraft", "1965", "United States", "The first crewed mission of Project Gemini, nicknamed \"Molly Brown,\" testing orbital maneuvering techniques."),
    ("Ranger 7", "Ranger 7", "NASA Jet Propulsion Laboratory", "1964", "United States", "The first American spacecraft to successfully transmit close-up images of the Moon before impact."),
    ("Apollo 11 Command Module Columbia", "Columbia (spacecraft)", "NASA / North American Rockwell", "1969", "United States", "The Apollo 11 command module that carried astronauts to lunar orbit and safely returned them to Earth."),
    ("Apollo 11 Lunar Module Eagle", "Eagle (spacecraft)", "NASA / Grumman", "1969", "United States", "The Apollo 11 lunar module that carried Neil Armstrong and Buzz Aldrin to the first crewed Moon landing."),
    ("Apollo 13 Command Module Odyssey", "Odyssey (spacecraft)", "NASA / North American Rockwell", "1970", "United States", "The Apollo 13 command module that safely returned its crew to Earth after an onboard explosion."),
    ("Lunar Roving Vehicle", "Lunar Roving Vehicle", "Boeing and General Motors", "1971", "United States", "An electric vehicle used by Apollo astronauts to travel across the lunar surface during later Moon missions."),
    ("Skylab", "Skylab", "NASA", "1973", "United States", "The first American space station, used for scientific experiments and long-duration crewed missions in orbit."),
    ("Voyager Golden Record", "Voyager Golden Record", "NASA / Carl Sagan committee", "1977", "United States", "A phonograph record carried aboard the Voyager probes containing sounds and images meant to represent life on Earth to any extraterrestrial finder."),
    ("Pioneer 10", "Pioneer 10", "NASA Ames Research Center", "1972", "United States", "The first spacecraft to travel through the asteroid belt and make direct observations of Jupiter, carrying the Pioneer plaque."),
    ("Pioneer plaque", "Pioneer plaque", "Carl Sagan and Frank Drake", "1972", "United States", "An engraved plaque attached to the Pioneer 10 and 11 probes intended to convey information about humanity to any intelligent extraterrestrial life."),
    ("Viking 1", "Viking 1", "NASA", "1975", "United States", "The first spacecraft to successfully land on Mars and return usable images from the planet's surface."),
    ("Mars Pathfinder", "Mars Pathfinder", "NASA Jet Propulsion Laboratory", "1996", "United States", "A NASA mission that delivered the Sojourner rover to Mars and demonstrated low-cost landing technology."),
    ("Hubble Space Telescope", "Hubble Space Telescope", "NASA and ESA", "1990", "United States", "A space telescope launched into low Earth orbit that has produced some of the most detailed images of the universe ever recorded."),
    ("Space Shuttle Enterprise", "Space Shuttle Enterprise", "NASA / Rockwell International", "1976", "United States", "The first Space Shuttle orbiter built, used for approach and landing tests but never flown into orbit."),
    ("Space Shuttle Discovery", "Space Shuttle Discovery", "NASA / Rockwell International", "1984", "United States", "The Space Shuttle orbiter with the most spaceflights, which flew the Hubble Space Telescope into orbit."),
    ("Space Shuttle Atlantis", "Space Shuttle Atlantis", "NASA / Rockwell International", "1985", "United States", "A Space Shuttle orbiter that flew the final Space Shuttle program mission in 2011."),
    ("Space Shuttle Endeavour", "Space Shuttle Endeavour", "NASA / Rockwell International", "1991", "United States", "A Space Shuttle orbiter built to replace Challenger, which flew numerous missions to the International Space Station."),
    ("Saturn V", "Saturn V", "NASA / Wernher von Braun", "1967", "United States", "The powerful multistage rocket that launched the Apollo missions to the Moon, remaining the most powerful rocket ever successfully flown."),
    # --- Aviation ---
    ("Wright Flyer", "Wright Flyer", "Orville and Wilbur Wright", "1903", "United States", "The aircraft that made the first sustained, controlled, powered flight by a heavier-than-air machine."),
    ("Wright Military Flyer", "Wright Military Flyer", "Orville and Wilbur Wright", "1909", "United States", "The first military airplane, purchased by the U.S. Army Signal Corps after a series of demonstration flights by the Wright brothers."),
    ("Bleriot XI", "Blériot XI", "Louis Blériot", "1909", "France", "The aircraft in which Louis Blériot made the first flight across the English Channel."),
    ("Vickers Vimy", "Vickers Vimy", "Vickers Limited", "1917", "United Kingdom", "The bomber aircraft, later adapted for record flights, that made the first nonstop transatlantic flight piloted by Alcock and Brown."),
    ("Fokker Dr.I", "Fokker Dr.I", "Fokker", "1917", "Germany", "A World War I triplane fighter famously flown by the \"Red Baron,\" Manfred von Richthofen."),
    ("Sopwith Camel", "Sopwith Camel", "Sopwith Aviation Company", "1917", "United Kingdom", "A British fighter aircraft credited with shooting down more enemy aircraft than any other Allied fighter of World War I."),
    ("Curtiss JN-4", "Curtiss JN-4", "Curtiss Aeroplane Company", "1915", "United States", "A widely used biplane trainer nicknamed the \"Jenny,\" which introduced many pilots to flight in the early 20th century."),
    ("Spirit of St. Louis", "Spirit of St. Louis", "Ryan Airlines", "1927", "United States", "The single-engine aircraft that Charles Lindbergh flew on the first solo nonstop transatlantic flight."),
    ("Junkers F.13", "Junkers F.13", "Junkers", "1919", "Germany", "The world's first all-metal, cantilever-wing airliner, designed specifically for commercial passenger transport."),
    ("LZ 127 Graf Zeppelin", "LZ 127 Graf Zeppelin", "Luftschiffbau Zeppelin", "1928", "Germany", "A pioneering passenger airship that circumnavigated the globe and completed regular transatlantic crossings."),
    ("LZ 129 Hindenburg", "LZ 129 Hindenburg", "Luftschiffbau Zeppelin", "1936", "Germany", "A large passenger airship that was destroyed in a famous fire while attempting to dock in New Jersey in 1937."),
    ("Piper J-3 Cub", "Piper J-3 Cub", "Piper Aircraft", "1938", "United States", "A simple, lightweight training aircraft that became one of the most recognizable small planes in aviation history."),
    ("Gee Bee Model Z", "Gee Bee Model Z", "Granville Brothers Aircraft", "1931", "United States", "A stubby, powerful racing aircraft that set speed records during the golden age of air racing."),
    ("Supermarine Spitfire", "Supermarine Spitfire", "Supermarine", "1938", "United Kingdom", "An iconic British fighter aircraft that played a decisive role in the Battle of Britain during World War II."),
    ("Messerschmitt Bf 109", "Messerschmitt Bf 109", "Messerschmitt", "1937", "Germany", "The primary fighter aircraft of the German Luftwaffe throughout World War II and one of the most-produced fighters in history."),
    ("North American P-51 Mustang", "North American P-51 Mustang", "North American Aviation", "1940", "United States", "A long-range American fighter aircraft renowned for escorting bombers deep into enemy territory during World War II."),
    ("Enola Gay", "Enola Gay", "Boeing / Martin Company", "1945", "United States", "The B-29 Superfortress bomber that dropped the atomic bomb \"Little Boy\" on Hiroshima in 1945."),
    ("Bockscar", "Bockscar", "Boeing / Martin Company", "1945", "United States", "The B-29 Superfortress bomber that dropped the atomic bomb \"Fat Man\" on Nagasaki in 1945."),
    ("Spruce Goose", "Hughes H-4 Hercules", "Hughes Aircraft Company", "1947", "United States", "A giant wooden flying boat, nicknamed the \"Spruce Goose,\" that made a single flight and remains the aircraft with the largest wingspan ever flown."),
    ("Bell X-1", "Bell X-1", "Bell Aircraft Corporation", "1947", "United States", "The rocket-powered aircraft in which Chuck Yeager became the first pilot to break the sound barrier in level flight."),
    ("Sikorsky VS-300", "Sikorsky VS-300", "Igor Sikorsky", "1939", "United States", "An experimental helicopter that established the single main rotor and tail rotor design used by most modern helicopters."),
    ("Bell 47", "Bell 47", "Bell Aircraft Corporation", "1945", "United States", "The first helicopter certified for civilian use, widely produced and used in military, medical, and agricultural roles."),
    ("Douglas DC-3", "Douglas DC-3", "Douglas Aircraft Company", "1935", "United States", "A revolutionary propeller airliner credited with making passenger air travel profitable and safe for airlines."),
    ("de Havilland Comet", "de Havilland Comet", "de Havilland", "1949", "United Kingdom", "The world's first commercial jet airliner to enter regular service, ushering in the jet age of air travel."),
    ("Boeing 707", "Boeing 707", "Boeing", "1957", "United States", "A pioneering commercial jet airliner that helped establish Boeing as a leader in jet aviation and popularized jet travel."),
    ("Concorde", "Concorde", "BAC and Aérospatiale", "1969", "United Kingdom", "A supersonic passenger airliner jointly developed by Britain and France, capable of crossing the Atlantic in about three hours."),
    ("Lockheed SR-71 Blackbird", "Lockheed SR-71 Blackbird", "Lockheed Skunk Works", "1964", "United States", "A long-range, high-altitude reconnaissance aircraft that remains the fastest air-breathing crewed aircraft ever flown."),
    ("North American X-15", "North American X-15", "North American Aviation", "1959", "United States", "An experimental rocket-powered aircraft that set speed and altitude records and carried pilots to the edge of space."),
    ("Avro Vulcan", "Avro Vulcan", "Avro", "1952", "United Kingdom", "A distinctive delta-wing strategic bomber that served as part of Britain's nuclear deterrent during the Cold War."),
    ("Hawker Siddeley Harrier", "Hawker Siddeley Harrier", "Hawker Siddeley", "1967", "United Kingdom", "The first operational fixed-wing aircraft capable of vertical or short takeoff and landing."),
    # --- Rail transportation ---
    ("Puffing Billy", "Puffing Billy", "William Hedley", "1813", "United Kingdom", "One of the oldest surviving steam locomotives, built to haul coal and demonstrating the practicality of steam railway locomotion."),
    ("Locomotion No. 1", "Locomotion No. 1", "George Stephenson", "1825", "United Kingdom", "The first steam locomotive to haul a passenger train on a public railway, the Stockton and Darlington Railway."),
    ("Stephenson's Rocket", "Stephenson's Rocket", "Robert Stephenson and Company", "1829", "United Kingdom", "An early steam locomotive whose innovative design won the Rainhill Trials and influenced locomotive design for decades."),
    ("Tom Thumb locomotive", "Tom Thumb (locomotive)", "Peter Cooper", "1830", "United States", "An early American steam locomotive built to demonstrate the feasibility of steam power for the Baltimore and Ohio Railroad."),
    ("DeWitt Clinton locomotive", "DeWitt Clinton (locomotive)", "West Point Foundry", "1831", "United States", "One of the first steam locomotives to operate in New York State, pulling an early passenger train."),
    ("City of Truro", "City of Truro (locomotive)", "Great Western Railway", "1903", "United Kingdom", "A steam locomotive claimed to have been the first to reach 100 miles per hour, though the record remains disputed."),
    ("Flying Scotsman", "Flying Scotsman (locomotive)", "Doncaster Works, LNER", "1923", "United Kingdom", "A famous steam locomotive that became the first to be officially recorded exceeding 100 miles per hour."),
    ("Mallard locomotive", "LNER Class A4 4468 Mallard", "Nigel Gresley, LNER", "1938", "United Kingdom", "The steam locomotive that holds the world speed record for steam traction, reaching 126 miles per hour."),
    ("Union Pacific Big Boy", "Union Pacific Big Boy", "American Locomotive Company", "1941", "United States", "Among the largest steam locomotives ever built, designed to haul heavy freight trains over mountainous terrain."),
    # --- Automobiles ---
    ("Benz Patent-Motorwagen", "Benz Patent-Motorwagen", "Karl Benz", "1885", "Germany", "Widely recognized as the first true automobile, powered by an internal combustion engine and patented by Karl Benz."),
    ("Duryea Motor Wagon", "Duryea Motor Wagon", "Charles and Frank Duryea", "1893", "United States", "Considered the first gasoline-powered automobile built and driven in the United States."),
    ("Stanley Steamer", "Stanley Steamer", "Stanley Motor Carriage Company", "1897", "United States", "A popular early steam-powered automobile that set land speed records in the early 1900s."),
    ("Ford Model T", "Ford Model T", "Ford Motor Company", "1908", "United States", "The first mass-produced automobile using assembly line techniques, which made car ownership affordable for millions."),
    ("Rolls-Royce Silver Ghost", "Rolls-Royce Silver Ghost", "Rolls-Royce Limited", "1907", "United Kingdom", "A luxury motor car renowned for its smooth and quiet engine, helping establish Rolls-Royce's reputation for engineering excellence."),
    ("Volkswagen Beetle", "Volkswagen Beetle", "Volkswagen", "1938", "Germany", "One of the best-selling and most recognizable car designs in automotive history, produced for over six decades."),
    # --- Maritime ---
    ("Mary Rose", "Mary Rose", "Henry VIII's navy", "1511", "England", "A Tudor warship that sank in 1545 and was raised in 1982, offering a remarkably preserved snapshot of 16th-century naval life."),
    ("Vasa ship", "Vasa (ship)", "Swedish Navy", "1628", "Sweden", "A Swedish warship that sank on her maiden voyage and was salvaged nearly intact more than 300 years later."),
    ("USS Constitution", "USS Constitution", "Edmund Hartt shipyard", "1797", "United States", "The world's oldest commissioned naval vessel still afloat, nicknamed \"Old Ironsides\" for its resilience in battle."),
    ("HMS Victory", "HMS Victory", "Chatham Dockyard", "1765", "United Kingdom", "The Royal Navy flagship of Admiral Horatio Nelson at the Battle of Trafalgar, now preserved as a museum ship."),
    ("USS Monitor", "USS Monitor", "John Ericsson", "1862", "United States", "An innovative ironclad warship that fought the first battle between ironclad ships during the American Civil War."),
    ("Cutty Sark", "Cutty Sark", "Scott & Linton", "1869", "United Kingdom", "One of the last and fastest tea clippers built, now preserved as a museum ship in Greenwich, England."),
    ("SS Great Britain", "SS Great Britain", "Isambard Kingdom Brunel", "1843", "United Kingdom", "A groundbreaking passenger steamship that was the first to combine an iron hull with screw propeller propulsion."),
    ("Turbinia", "Turbinia", "Charles Algernon Parsons", "1894", "United Kingdom", "The first steam turbine-powered ship, which demonstrated unprecedented speed and revolutionized naval propulsion."),
    ("RMS Titanic", "RMS Titanic", "Harland and Wolff", "1912", "United Kingdom", "A luxury ocean liner that sank on its maiden voyage after striking an iceberg, whose recovered artifacts are displayed in museums worldwide."),
    ("RMS Queen Mary", "RMS Queen Mary", "John Brown & Company", "1936", "United Kingdom", "A transatlantic ocean liner famed for its speed and luxury, now preserved as a floating museum and hotel in Long Beach, California."),
    ("Golden Hind", "Golden Hind", "English shipwrights", "1577", "England", "The galleon in which Sir Francis Drake circumnavigated the globe between 1577 and 1580."),
    ("Santa Maria ship", "Santa María (ship)", "Spanish shipbuilders", "1460s", "Spain", "The largest of the three ships used by Christopher Columbus on his first voyage across the Atlantic in 1492."),
    ("HMS Beagle", "HMS Beagle", "Royal Navy", "1820", "United Kingdom", "The survey ship on which Charles Darwin sailed on his famous voyage that helped shape his theory of evolution."),
    ("Kon-Tiki", "Kon-Tiki", "Thor Heyerdahl", "1947", "Norway", "A balsawood raft sailed by Thor Heyerdahl across the Pacific Ocean to demonstrate that ancient South Americans could have reached Polynesia."),
    ("Endurance", "Endurance (1912 ship)", "Framnæs shipyard", "1912", "Norway", "The polar exploration ship of Ernest Shackleton's Imperial Trans-Antarctic Expedition, crushed by pack ice in 1915 and located on the seabed in 2022."),
    ("USS Nautilus (SSN-571)", "USS Nautilus (SSN-571)", "United States Navy", "1954", "United States", "The world's first operational nuclear-powered submarine, which became the first vessel to reach the geographic North Pole underwater."),
    ("Trieste bathyscaphe", "Trieste (bathyscaphe)", "Auguste Piccard", "1953", "Switzerland", "A deep-diving research submersible that became the first crewed vessel to reach the bottom of the Challenger Deep, the deepest known point in Earth's oceans."),
    ("Alvin submersible", "Alvin (submersible)", "Woods Hole Oceanographic Institution", "1964", "United States", "A deep-sea research submersible used in numerous scientific expeditions, including the exploration of the wreck of RMS Titanic."),
    # --- Scientific instruments & industrial machines ---
    ("Foucault pendulum", "Foucault pendulum", "Léon Foucault", "1851", "France", "A simple pendulum device that provided the first direct visual demonstration of the Earth's rotation."),
    ("Galileo's telescope", "Galileo's telescope", "Galileo Galilei", "1609", "Italy", "An early refracting telescope built and used by Galileo Galilei to make groundbreaking astronomical observations."),
    ("Leviathan of Parsonstown", "Leviathan of Parsonstown", "William Parsons, 3rd Earl of Rosse", "1845", "Ireland", "A giant reflecting telescope that was the largest in the world for over seventy years, used to discover spiral galaxy structures."),
    ("H4 marine chronometer", "H4 (chronometer)", "John Harrison", "1759", "United Kingdom", "A precision marine chronometer that solved the problem of determining longitude at sea."),
    ("Cavendish experiment apparatus", "Cavendish experiment", "Henry Cavendish", "1798", "United Kingdom", "A torsion balance apparatus used to measure the density of the Earth and effectively determine the gravitational constant."),
    ("Van de Graaff generator", "Van de Graaff generator", "Robert J. Van de Graaff", "1929", "United States", "An electrostatic generator capable of producing very high voltages, widely used for physics demonstrations and early particle accelerators."),
    ("Tesla coil", "Tesla coil", "Nikola Tesla", "1891", "United States", "A resonant transformer circuit invented by Nikola Tesla to produce high-voltage, low-current electrical discharges."),
    ("Wilson cloud chamber", "Cloud chamber", "Charles Thomson Rees Wilson", "1911", "United Kingdom", "A particle detector used to visualize the tracks of ionizing radiation, instrumental in early discoveries in particle physics."),
    ("Michelson interferometer", "Michelson interferometer", "Albert A. Michelson", "1881", "United States", "A precision optical instrument used in the famous Michelson-Morley experiment that helped disprove the theory of luminiferous ether."),
    ("Newcomen atmospheric engine", "Newcomen atmospheric engine", "Thomas Newcomen", "1712", "United Kingdom", "The first practical steam engine, used to pump water out of mines and a key precursor to the Industrial Revolution."),
    ("Watt steam engine", "Watt steam engine", "James Watt", "1776", "United Kingdom", "An improved steam engine design featuring a separate condenser, dramatically increasing efficiency and powering the Industrial Revolution."),
    ("Spinning Jenny", "Spinning Jenny", "James Hargreaves", "1764", "United Kingdom", "A multi-spindle spinning frame that greatly increased the productivity of yarn production during the early Industrial Revolution."),
    ("Spinning mule", "Spinning mule", "Samuel Crompton", "1779", "United Kingdom", "A machine that combined features of earlier spinning devices to produce strong, fine yarn, transforming textile manufacturing."),
    ("Cotton gin", "Cotton gin", "Eli Whitney", "1793", "United States", "A machine that mechanized the removal of seeds from cotton fibers, dramatically increasing cotton production in the American South."),
    ("Lovell Telescope", "Lovell Telescope", "Jodrell Bank Observatory, University of Manchester", "1957", "United Kingdom", "A large steerable radio telescope that was the first of its kind and remains a major instrument for radio astronomy research."),
    ("Cyclotron", "Cyclotron", "Ernest Lawrence", "1932", "United States", "An early type of particle accelerator that uses a magnetic field to spiral charged particles to high energies."),
    ("Geiger counter", "Geiger counter", "Hans Geiger and Walther Müller", "1928", "Germany", "An instrument used to detect and measure ionizing radiation, widely used in physics research and radiation safety."),
    ("Bunsen burner", "Bunsen burner", "Robert Bunsen and Peter Desaga", "1855", "Germany", "A laboratory gas burner that produces a single open flame, used for heating and sterilization in chemistry labs worldwide."),
    ("Slide rule", "Slide rule", "William Oughtred", "1622", "United Kingdom", "A mechanical analog calculating device used for multiplication, division, and other mathematical functions before electronic calculators."),
    ("Astrolabe", "Astrolabe", "Ancient Greek and Islamic astronomers", "c. 200 BC (refined in the medieval Islamic world)", "Greece", "An ancient astronomical instrument used to measure the position of celestial bodies and solve problems of time and location."),
    ("Orrery", "Orrery", "George Graham and John Rowley", "c. 1704", "United Kingdom", "A mechanical model of the solar system that demonstrates the relative positions and motions of the planets around the Sun."),
    ("Sextant", "Sextant", "John Hadley and Thomas Godfrey", "1730", "United Kingdom", "A navigational instrument used to measure the angle between celestial objects and the horizon to determine position at sea."),
    ("Gyrocompass", "Gyrocompass", "Elmer Sperry", "1908", "United States", "A type of compass that uses a fast-spinning rotor to find true north, unaffected by magnetic interference, and widely adopted by ships."),
    ("Iron lung", "Iron lung", "Philip Drinker and Louis Agassiz Shaw", "1928", "United States", "A negative-pressure mechanical respirator used to help patients, especially polio victims, breathe when their own muscles could not."),
    ("Crookes tube", "Crookes tube", "William Crookes", "1875", "United Kingdom", "An early experimental electrical discharge tube used to investigate cathode rays and which led to the discovery of X-rays."),
    ("Stethoscope", "Stethoscope", "René Laennec", "1816", "France", "A medical instrument invented to listen to internal body sounds, revolutionizing the diagnosis of heart and lung conditions."),
    ("Centrifugal governor", "Centrifugal governor", "James Watt", "1788", "United Kingdom", "A self-regulating device that automatically controls the speed of a steam engine, an early example of automatic feedback control."),
    ("Davy lamp", "Davy lamp", "Humphry Davy", "1815", "United Kingdom", "A safety lamp designed to reduce the risk of explosions in coal mines caused by flammable gases."),
    ("Wheatstone bridge", "Wheatstone bridge", "Samuel Hunter Christie and Charles Wheatstone", "1833", "United Kingdom", "An electrical circuit used to precisely measure an unknown electrical resistance, a fundamental tool in physics and engineering."),
    ("Leyden jar", "Leyden jar", "Ewald Georg von Kleist and Pieter van Musschenbroek", "1745", "Netherlands", "An early device used to store static electricity, considered the first form of capacitor."),
    ("Voltaic pile", "Voltaic pile", "Alessandro Volta", "1800", "Italy", "The first electrical battery capable of providing a continuous current, marking the beginning of modern electrochemistry."),
    ("Faraday disk", "Faraday disk", "Michael Faraday", "1831", "United Kingdom", "The first electric generator, demonstrating that a continuous electric current could be produced by moving a conductor through a magnetic field."),
    ("Kinetoscope", "Kinetoscope", "Thomas Edison and William Kennedy Dickson", "1891", "United States", "An early motion picture exhibition device that allowed a single viewer to watch a short film through a peephole viewer."),
    ("Magic lantern", "Magic lantern", "Christiaan Huygens (early development)", "17th century", "Netherlands", "An early type of image projector using a light source and glass slides, a precursor to modern film projection."),
    ("Cooke and Wheatstone telegraph", "Cooke and Wheatstone telegraph", "William Fothergill Cooke and Charles Wheatstone", "1837", "United Kingdom", "The first commercially successful electric telegraph system, used initially along British railways."),
    ("Intel 4004", "Intel 4004", "Intel Corporation", "1971", "United States", "The world's first commercially produced microprocessor, which laid the foundation for the modern computing industry."),
    ("Moog synthesizer", "Moog synthesizer", "Robert Moog", "1964", "United States", "A pioneering analog music synthesizer that transformed electronic music production."),
    # --- Nuclear history ---
    ("The Gadget", "Gadget (nuclear device)", "Manhattan Project", "1945", "United States", "The first nuclear device ever detonated, tested at the Trinity site in New Mexico."),
    ("Fat Man", "Fat Man", "Manhattan Project", "1945", "United States", "The codename for the atomic bomb dropped on Nagasaki, Japan, in August 1945."),
    ("Little Boy", "Little Boy", "Manhattan Project", "1945", "United States", "The codename for the atomic bomb dropped on Hiroshima, Japan, in August 1945."),
    # --- Photography & recording ---
    ("Kodak Brownie camera", "Brownie (camera)", "Eastman Kodak", "1900", "United States", "An inexpensive box camera that made photography accessible to the general public for the first time."),
    ("Leica I", "Leica I", "Ernst Leitz Optische Werke", "1925", "Germany", "One of the first commercially successful 35mm cameras, which helped establish the format still used in photography today."),
    ("Edison phonograph", "Phonograph", "Thomas Edison", "1877", "United States", "The first device capable of both recording and reproducing sound, invented by Thomas Edison."),
    # --- Land / air / space speed records ---
    ("Bluebird K7", "Bluebird K7", "Donald Campbell", "1955", "United Kingdom", "A jet-powered hydroplane in which Donald Campbell set seven world water speed records."),
    ("ThrustSSC", "ThrustSSC", "Richard Noble", "1997", "United Kingdom", "The first car to officially break the sound barrier on land, setting the current world land speed record."),
    ("SpaceShipOne", "SpaceShipOne", "Scaled Composites", "2004", "United States", "The first privately funded crewed spacecraft to reach space, winning the Ansari X Prize."),
    ("Rutan Voyager", "Rutan Voyager", "Scaled Composites", "1986", "United States", "The first aircraft to fly around the world nonstop without refueling."),
    ("Gossamer Albatross", "Gossamer Albatross", "Paul MacCready", "1979", "United States", "A human-powered aircraft that made the first successful crossing of the English Channel under human power alone."),
    ("Boeing 747", "Boeing 747", "Boeing", "1969", "United States", "A wide-body jet airliner nicknamed the \"Jumbo Jet\" that transformed long-distance commercial air travel."),
    # --- Ancient / pre-modern engineering ---
    ("South Pointing Chariot", "South Pointing Chariot", "Ancient Chinese engineers", "c. 3rd century AD", "China", "A non-magnetic directional device using a differential gear mechanism to keep a pointing figure oriented south regardless of the chariot's turns."),
    ("Aeolipile", "Aeolipile", "Hero of Alexandria", "c. 1st century AD", "Roman Egypt", "An early steam-powered device that spun using jets of steam, considered one of the first recorded steam engines."),
    ("Ishango bone", "Ishango bone", "Upper Paleolithic toolmakers", "c. 20,000 BC", "Democratic Republic of the Congo", "A bone tool marked with tallied notches that is considered one of the oldest known mathematical artifacts."),
    ("Houfeng didong yi", "Houfeng didong yi", "Zhang Heng", "132 AD", "China", "An ancient Chinese device credited as the world's first seismoscope, designed to detect the direction of distant earthquakes."),
    ("Galileo thermometer", "Galileo thermometer", "Attributed to the Accademia del Cimento", "17th century", "Italy", "A sealed glass thermometer that uses the temperature-dependent buoyancy of weighted glass bulbs, popularly (if loosely) associated with Galileo Galilei."),
]
CATEGORY_ASSIGNMENTS.append((SCIENCE_TECH_BATCH2, "science_technology"))




def build_object(idx: int, name: str, wiki_title: str, creator: str, date: str, origin: str, description: str, category: str) -> dict:
    obj_id = f"wht_{idx:04d}"
    return {
        "id": obj_id,
        "name": name,
        "artist": creator,
        "year": date,
        "origin": origin,
        "material": category,
        "category": category,
        "description": description,
        "significance": f"Widely recognized as one of the famous works representing {origin} in world art, science, or cultural history.",
        "fun_fact": f"{name} is frequently featured in museum collections and history curricula as a landmark example from {origin}.",
        "museum": "See Wikipedia for current location",
        "educational_importance": "A genuinely famous, real work -- useful for art history, world history, natural history, and cultural studies at every level.",
        "related_lesson": "Art History" if category in ("painting", "sculpture") else "World History",
        "activity": f"Research {name} further: who made or discovered it, where it is today, and why it became famous.",
        "quiz": {
            "question": f"Which culture or region does '{name}' come from?",
            "options": [origin, "Antarctica", "International Waters", "Unknown"],
            "answer": 0,
        },
        "related_subjects": ["Art History", "World History", "Geography"],
        "links": {
            "wikipedia": wiki_url(wiki_title),
            "image_search": commons_search(name),
            "google_image_search": google_image_search(f"{name} {origin}"),
            "video": yt(f"{name} explained documentary"),
            "smarthistory": smarthistory(name),
        },
        "wiki_title": wiki_title,
    }


def build_objects(existing_wiki_titles: set[str]) -> list[dict]:
    objects = []
    idx = 0
    seen = set()
    for items, category in CATEGORY_ASSIGNMENTS:
        for name, wiki_title, creator, date, origin, description in items:
            if wiki_title in seen or wiki_title in existing_wiki_titles:
                continue  # avoid duplicating a real work already in the museum
            seen.add(wiki_title)
            idx += 1
            objects.append(build_object(idx, name, wiki_title, creator, date, origin, description, category))
    return objects


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_wiki_titles = set()
    for gallery in data["galleries"].values():
        for obj in gallery.get("objects", []):
            wt = obj.get("wiki_title")
            if wt:
                existing_wiki_titles.add(wt)

    objects = build_objects(existing_wiki_titles)

    gallery = data["galleries"].get(GALLERY_KEY)
    if gallery is None:
        gallery = {
            "label": "World Heritage Treasures",
            "emoji": "🌐",
            "description": "",
            "objects": [],
        }
        data["galleries"][GALLERY_KEY] = gallery
    gallery["objects"].extend(objects)
    gallery["description"] = (
        f"{len(gallery['objects'])} genuinely famous, individually named real artworks, artifacts, natural "
        f"history specimens, and scientific/historic objects from around the world -- each linked to its real "
        f"Wikipedia page so the museum can show an actual live photo of the object."
    )

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(g.get("objects", [])) for g in data["galleries"].values())
    print(f"Added {len(objects)} new objects. {GALLERY_KEY} now has {len(gallery['objects'])} objects. "
          f"Museum total: {total} objects across {len(data['galleries'])} galleries.")


if __name__ == "__main__":
    main()
