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

# Real, individually famous sculptures and architecture/monuments/landmarks,
# chosen to complement (not duplicate) the earlier "Famous Masterpieces"
# gallery's FAMOUS_SCULPTURES / FAMOUS_SCULPTURES_MORE / MORE_SCULPTURE_AND_ARCHITECTURE
# and MONUMENTS_AND_LANDMARKS lists (generate_famous_museum_objects.py).
MORE_SCULPTURE_BATCH2 = [
    ('Bust of Ramesses the Great (Turin)', 'Statue of Ramesses II', 'Ancient Egyptians', 'c. 1250 BCE', 'Egypt', 'A seated granite colossus of Ramesses II held in the Museo Egizio, Turin.'),
    ('Hermaphroditus (Sleeping Hermaphroditus)', 'Sleeping Hermaphroditus', 'Unknown (Hellenistic, Roman copy)', '2nd century BCE (Roman copy)', 'Greece/Italy', 'A Hellenistic marble exploring dual gender identity, later given a Baroque mattress by Bernini.'),
    ('The Ludovisi Gaul', 'Ludovisi Gaul', 'Epigonus (attributed, Roman copy)', '3rd century BCE (Roman copy)', 'Greece/Rome', 'A dramatic depiction of a Gallic chieftain killing himself and his wife rather than face capture.'),
    ('Augustus of Prima Porta', 'Augustus of Prima Porta', 'Unknown', '1st century CE (copy of c. 20 BCE original)', 'Italy (Rome)', 'An idealized marble portrait of Emperor Augustus in military dress, a landmark of Roman imperial propaganda.'),
    ('The Togatus Barberini', 'Togatus Barberini', 'Unknown (Roman)', '1st century CE', 'Italy (Rome)', 'A Roman patrician statue holding ancestral busts, exemplifying Roman ancestor veneration.'),
    ("Bernini's David", 'David (Bernini)', 'Gian Lorenzo Bernini', '1623-1624', 'Italy', "A twisting, dynamic David caught mid-action, contrasting sharply with the static poise of Michelangelo's version."),
    ('Truth Unveiled by Time', 'Truth Unveiled by Time', 'Gian Lorenzo Bernini', '1646-1652', 'Italy', 'An allegorical marble Bernini kept in his own home, left deliberately unfinished.'),
    ('The Elephant and Obelisk of Bernini', 'Pulcino della Minerva', 'Gian Lorenzo Bernini', '1667', 'Italy', 'A whimsical Baroque sculpture of a small elephant bearing an ancient Egyptian obelisk in Rome.'),
    ('Maman', 'Maman (sculpture)', 'Louise Bourgeois', '1999', 'France/United States', 'A monumental bronze and steel spider, one of the largest sculptures in the world, symbolizing maternal protection.'),
    ('Reclining Figure', 'Reclining Figure (Henry Moore)', 'Henry Moore', '1951', 'United Kingdom', "One of many monumental abstracted reclining figures that made Henry Moore Britain's leading modern sculptor."),
    ('King and Queen', 'King and Queen (sculpture)', 'Henry Moore', '1952-1953', 'United Kingdom', 'A pair of abstracted bronze figures seated in quiet, weathered majesty in the Scottish landscape.'),
    ('Large Two Forms', 'Large Two Forms', 'Henry Moore', '1966-1969', 'United Kingdom', 'Two massive abstract bronze forms exploring the interplay of positive and negative space.'),
    ('The Endless Column', 'Endless Column', 'Constantin Brâncuși', '1938', 'Romania', 'A towering modular steel column memorializing Romanian soldiers of World War I.'),
    ('Sleeping Muse', 'Sleeping Muse', 'Constantin Brâncuși', '1910', 'Romania/France', "A serenely simplified bronze head, among Brâncuși's most influential early modernist works."),
    ('Man Pointing', 'Man Pointing', 'Alberto Giacometti', '1947', 'Switzerland', 'An elongated, skeletal bronze figure emblematic of postwar existentialist sculpture.'),
    ('Walking Man I', "L'Homme qui marche I", 'Alberto Giacometti', '1960', 'Switzerland', 'An elongated striding bronze figure that became one of the most expensive sculptures ever sold at auction.'),
    ('The Palace at 4 a.m.', 'The Palace at 4 a.m.', 'Alberto Giacometti', '1932', 'Switzerland', "A delicate wood, glass, wire, and string construction from Giacometti's Surrealist period."),
    ('Bird Girl (Bonaventure Cemetery)', 'Bird Girl', 'Sylvia Shaw Judson', '1936', 'United States', "A bronze garden statue that became famous as the cover image of 'Midnight in the Garden of Good and Evil'."),
    ('Balloon Flower', 'Balloon Flower', 'Jeff Koons', '1995-2000', 'United States', 'A large mirror-polished stainless steel sculpture resembling a twisted balloon flower.'),
    ('Puppy', 'Puppy (sculpture)', 'Jeff Koons', '1992', 'United States/Spain', 'A 43-foot-tall topiary sculpture of a West Highland Terrier, permanently sited at the Guggenheim Bilbao.'),
    ('Chicago Picasso', 'Chicago Picasso', 'Pablo Picasso', '1967', 'United States', 'An untitled monumental Cubist steel sculpture gifted to the city of Chicago.'),
    ('Charging Bull', 'Charging Bull', 'Arturo Di Modica', '1989', 'United States', 'A guerrilla-installed bronze bull near Wall Street that became a symbol of financial optimism.'),
    ('Fearless Girl', 'Fearless Girl', 'Kristen Visbal', '2017', 'United States', 'A bronze statue of a defiant young girl, originally placed facing Charging Bull to promote gender diversity.'),
    ('Manneken Pis', 'Manneken Pis', 'Jérôme Duquesnoy the Elder', '1618-1619', 'Belgium', 'A small bronze fountain statue of a urinating boy, an iconic and beloved symbol of Brussels.'),
    ('Christ of the Andes', 'Christ the Redeemer of the Andes', 'Mateo Alonso', '1904', 'Argentina/Chile', 'A statue marking the border between Argentina and Chile, commemorating a peace treaty between the two nations.'),
    ('Cristo de la Concordia', 'Cristo de la Concordia', 'Various sculptors', '1987', 'Bolivia', 'One of the tallest statues of Jesus Christ in the world, overlooking Cochabamba.'),
    ('Ushiku Daibutsu', 'Ushiku Daibutsu', 'Modern craftsmen', '1993', 'Japan', 'One of the tallest bronze statues in the world, depicting Amida Buddha.'),
    ('Statue of Unity', 'Statue of Unity', 'Ram V. Sutar', '2018', 'India', 'The tallest statue in the world, depicting Indian statesman Sardar Vallabhbhai Patel.'),
    ('Bahubali Statue of Shravanabelagola', 'Gommateshvara statue', 'Western Ganga dynasty (Chavundaraya, commissioned)', '981 CE', 'India', 'A monolithic granite statue of the Jain figure Bahubali carved from a single rock.'),
    ('Tian Tan Buddha', 'Tian Tan Buddha', 'Modern craftsmen', '1993', 'Hong Kong (China)', 'A large bronze seated Buddha statue on Lantau Island, a major pilgrimage and tourist site.'),
    ("Sanjusangendo's Thousand Armed Kannon Statues", 'Sanjūsangen-dō', 'Kamakura-period sculptors (Tankei)', '13th century', 'Japan', 'A hall containing 1,001 life-sized statues of the bodhisattva Kannon, a landmark of Japanese Buddhist sculpture.'),
    ('Byodo-in Amida Nyorai Statue', 'Byōdō-in', 'Jōchō', '1053', 'Japan', 'A masterwork of Heian-period Buddhist sculpture housed in the Phoenix Hall.'),
    ('Todai-ji Great Buddha', 'Tōdai-ji', 'Nara-period craftsmen', '752 CE', 'Japan', "Houses the world's largest bronze statue of Vairocana Buddha, in the world's largest wooden building."),
    ('Bodhisattva Guanyin of the Southern Song', 'Guanyin', 'Song dynasty craftsmen', '10th-13th century', 'China', 'Elegant polychrome wood carvings of the bodhisattva of compassion, prized examples of Chinese Buddhist sculpture.'),
    ('Yungang Grottoes Buddhas', 'Yungang Grottoes', 'Northern Wei dynasty craftsmen', '460-525 CE', 'China', 'Thousands of Buddhist statues and niches carved into a sandstone cliff, a UNESCO World Heritage Site.'),
    ('Bingling Temple Grottoes Buddha', 'Bingling Temple', 'Various Chinese dynasties', '420 CE onward', 'China', 'A cliffside complex of Buddhist grottoes with a monumental seated Buddha carved into the rock.'),
    ('Seokguram Grotto Buddha', 'Seokguram', 'Silla-dynasty craftsmen', '8th century CE', 'Korea', 'A granite Buddhist grotto shrine renowned for its serene central Buddha statue.'),
    ('Benin Bronze Plaques (Oba portrait heads)', 'Benin ivory mask', 'Edo craftsmen (Benin Kingdom)', '16th century', 'Nigeria', 'An ivory pendant mask of a Benin queen mother, one of the most celebrated works of African court art.'),
    ('Djenné Terracotta Figures', 'Djenné terracottas', 'Djenné-Jeno culture', 'c. 1000-1600 CE', 'Mali', 'Enigmatic terracotta figures from the Inland Niger Delta, prized for their expressive, contorted poses.'),
    ('Bwa Plank Mask', 'Bwa people', 'Bwa craftsmen', 'Traditional, ongoing', 'Burkina Faso', 'Tall painted wooden plank masks used in initiation and harvest ceremonies.'),
    ('Fang Reliquary Guardian Figure', 'Fang people', 'Fang craftsmen', 'Traditional, 19th-20th century', 'Gabon/Cameroon', 'Wooden guardian figures once placed atop bark boxes containing ancestral relics, later a major influence on Picasso and Modigliani.'),
    ('Senufo Rhythm Pounder Figure', 'Senufo people', 'Senufo craftsmen', 'Traditional, 19th-20th century', 'Ivory Coast', 'Ceremonial figures used in agricultural rites among the Senufo people of West Africa.'),
    ('Luba Royal Stool', 'Luba people', 'Luba craftsmen', '19th century', 'DR Congo', 'A finely carved caryatid stool used as a symbol of Luba kingship.'),
    ('Baule Portrait Figure (Blolo Bla)', 'Baule people', 'Baule craftsmen', 'Traditional, 19th-20th century', 'Ivory Coast', "Wooden spirit-spouse figures carved to honor an individual's otherworld partner."),
    ('Mangbetu Anthropomorphic Vessel', 'Mangbetu people', 'Mangbetu craftsmen', 'Late 19th-early 20th century', 'DR Congo', 'Ceramic and carved vessels shaped as elongated human heads, reflecting Mangbetu ideals of beauty.'),
    ('Maori Tekoteko Carving', 'Māori carving', 'Māori craftsmen', 'Traditional, ongoing', 'New Zealand', 'Carved ancestor figures placed atop meeting houses, embodying Māori genealogy and mythology.'),
    ('Hawaiian Kū Feather Image', 'Kūkaʻilimoku', 'Native Hawaiian craftsmen', 'Late 18th century', 'United States (Hawaii)', 'A feathered image of the war god Kū, among the most sacred surviving Hawaiian sculptural objects.'),
    ('Easter Island Moai Kavakava', 'Moai kavakava', 'Rapa Nui people', '18th-19th century', 'Easter Island (Chile)', 'Small wooden emaciated ancestor figures distinct from the giant stone moai.'),
    ('New Ireland Malagan Carving', 'Malagan', 'New Ireland peoples', 'Traditional, ongoing', 'Papua New Guinea', 'Elaborately painted openwork carvings created for funerary ceremonies and then traditionally destroyed.'),
    ('Trobriand Islands Prow Board Carving', 'Trobriand Islands', 'Trobriand craftsmen', 'Traditional, ongoing', 'Papua New Guinea', 'Intricately carved canoe prow boards used in ceremonial kula exchange voyages.'),
    ('Vanuatu Slit Gong (Tam Tam)', 'Slit drum', 'Ni-Vanuatu craftsmen', 'Traditional, ongoing', 'Vanuatu', 'Tall carved wooden ceremonial drums topped with ancestor faces.'),
    ('Aztec Coatlicue Statue', 'Coatlicue', 'Aztec (Mexica) craftsmen', '15th century', 'Mexico', "A monumental basalt statue of the Aztec earth goddess, discovered beneath Mexico City's main square."),
    ('Aztec Xochipilli Statue', 'Xochipilli', 'Aztec (Mexica) craftsmen', '15th-16th century', 'Mexico', 'A statue of the Aztec god of flowers, art, and pleasure, found near Popocatépetl.'),
    ('Chac Mool Reclining Figure', 'Chac Mool', 'Toltec/Maya craftsmen', 'c. 9th-13th century', 'Mexico', 'A distinctive reclining figure type found at Toltec and Maya sites, believed to serve a ritual offering function.'),
    ('Zapotec Funerary Urns of Monte Albán', 'Monte Albán', 'Zapotec civilization', '500 BCE-800 CE', 'Mexico', 'Elaborate ceramic funerary urns depicting deities, found in Zapotec tombs.'),
    ('Moche Portrait Vessels', 'Moche portraiture', 'Moche civilization', 'c. 100-700 CE', 'Peru', 'Strikingly individualized ceramic portrait vessels depicting real Moche individuals.'),
    ('Tiwanaku Gate of the Sun', 'Gateway of the Sun', 'Tiwanaku civilization', 'c. 500-950 CE', 'Bolivia', 'A monolithic carved stone gateway with a central figure believed to represent a solar deity.'),
    ('San Agustín Stone Statues', 'San Agustín Archaeological Park', 'San Agustín culture', '1st-8th century CE', 'Colombia', 'The largest collection of monumental religious stone sculptures in South America.'),
    ('Toltec Atlantean Warrior Columns', 'Atlantean figures of Tula', 'Toltec civilization', 'c. 900-1150 CE', 'Mexico', 'Massive carved stone warrior columns that once supported the roof of a Toltec temple.'),
    ('Marble Cycladic Figurine', 'Cycladic art', 'Cycladic civilization', 'c. 2800-2300 BCE', 'Greece', 'Minimalist marble figures from the Aegean that profoundly influenced modern sculptors like Brâncuși and Moore.'),
    ('Lady of Elche', 'Lady of Elche', 'Iberians', '4th century BCE', 'Spain', 'An enigmatic painted limestone bust regarded as one of the finest works of Iberian sculpture.'),
    ('Venus of Willendorf (small Paleolithic figure)', 'Venus figurines', 'Paleolithic humans', 'c. 40,000-10,000 BCE', 'Europe', "A class of small prehistoric female figurines found across Ice Age Europe, among humanity's earliest sculptural art."),
    ('Löwenmensch (Lion Man) Figurine', 'Lion-man', 'Paleolithic humans (Aurignacian culture)', 'c. 40,000 years ago', 'Germany', 'One of the oldest known figurative sculptures in the world, carved from mammoth ivory.'),
    ('Eve (Rodin)', 'Eve (Rodin)', 'Auguste Rodin', '1881', 'France', 'A crouching, anguished figure originally intended to flank The Gates of Hell.'),
    ('The Prodigal Son (Rodin)', 'The Prodigal Son (Rodin)', 'Auguste Rodin', '1889', 'France', 'A dramatic bronze depicting a kneeling, imploring male figure.'),
    ("Camille Claudel's The Waltz", 'The Waltz (Claudel)', 'Camille Claudel', '1893', 'France', "A sinuous bronze of a dancing couple by Rodin's contemporary and collaborator Camille Claudel."),
    ("Sol LeWitt's Structures", 'Sol LeWitt', 'Sol LeWitt', '1960s-2000s', 'United States', 'Modular geometric structures and wall drawings that helped define Minimalist and Conceptual art.'),
    ("Richard Serra's Tilted Arc", 'Tilted Arc', 'Richard Serra', '1981', 'United States', 'A monumental curved steel wall sculpture whose removal after public controversy became a landmark art-law case.'),
    ('Cor-Ten Steel Sculpture Torqued Ellipses', 'Torqued Ellipses', 'Richard Serra', '1996-1999', 'United States', 'Massive spiraling steel plate sculptures visitors can walk through, exploring space and mass.'),
    ("Isamu Noguchi's Red Cube", 'Red Cube', 'Isamu Noguchi', '1968', 'United States', 'A tilted red steel cube balanced on one point outside a Manhattan skyscraper.'),
    ("Alexander Calder's Flamingo", 'Flamingo (sculpture)', 'Alexander Calder', '1973', 'United States', "A monumental vermilion stabile sculpture standing in Chicago's Federal Plaza."),
    ("Alexander Calder's La Grande Vitesse", 'La Grande Vitesse', 'Alexander Calder', '1969', 'United States', 'A large red stabile that became the symbol of Grand Rapids, Michigan.'),
    ("Barbara Hepworth's Single Form", 'Single Form (Barbara Hepworth)', 'Barbara Hepworth', '1961-1964', 'United Kingdom', 'A monumental bronze memorial to Dag Hammarskjöld outside the United Nations headquarters.'),
    ("Naum Gabo's Constructions", 'Naum Gabo', 'Naum Gabo', '1920s-1970s', 'Russia/United Kingdom', 'Pioneering geometric constructions foundational to the Constructivist sculptural movement.'),
    ("Auguste Bartholdi's Lion of Belfort", 'Lion of Belfort', 'Frédéric Auguste Bartholdi', '1880', 'France', 'A monumental sandstone lion commemorating the French resistance during the siege of Belfort.'),
    ("Rodin's Monument to Victor Hugo", 'Monument to Victor Hugo (Rodin)', 'Auguste Rodin', '1890s', 'France', 'One of several sculptural tributes Rodin created to the celebrated French writer.'),
    ("David Smith's Cubi Series", 'Cubi (David Smith)', 'David Smith', '1961-1965', 'United States', 'Stainless steel geometric sculptures widely regarded as a peak of postwar American sculpture.'),
    ("Donald Judd's Untitled Boxes (Marfa)", 'Donald Judd', 'Donald Judd', '1980s', 'United States', 'Rows of milled aluminum boxes installed at Marfa, Texas, defining works of Minimalist sculpture.'),
    ("Michelangelo's Genius of Victory", 'Genius of Victory', 'Michelangelo', '1532-1534', 'Italy', 'An unfinished marble group originally intended for the tomb of Pope Julius II.'),
    ('The Bargello David-Apollo', 'David-Apollo', 'Michelangelo', 'c. 1530', 'Italy', 'An ambiguous unfinished Michelangelo figure that could depict either David or Apollo.'),
    ("Verrocchio's David", 'David (Verrocchio)', 'Andrea del Verrocchio', 'c. 1473-1475', 'Italy', 'An early Renaissance bronze David, believed to have used the young Leonardo da Vinci as a model.'),
    ("Donatello's Judith and Holofernes", 'Judith and Holofernes (Donatello)', 'Donatello', 'c. 1457-1464', 'Italy', 'A bronze depicting the biblical heroine slaying the Assyrian general, symbolizing civic virtue over tyranny.'),
    ("Cellini's Saltcellar", 'Salt Cellar (Cellini)', 'Benvenuto Cellini', '1540-1543', 'Italy/France', 'An elaborate gold and enamel saltcellar considered a masterpiece of Mannerist goldsmithing.'),
    ("Giambologna's Mercury", 'Flying Mercury', 'Giambologna', '1580', 'Italy', 'A dynamic bronze depicting the messenger god seemingly in flight, balanced on a single toe.'),
    ('The Farnese Atlas', 'Farnese Atlas', 'Unknown (Roman copy)', '2nd century CE (Roman copy)', 'Greece/Rome', 'A Roman marble statue of Atlas bearing a celestial globe, notable for its detailed ancient star map.'),
    ('The Anavysos Kouros', 'Kroisos Kouros', 'Ancient Greeks', 'c. 530 BCE', 'Greece', 'An idealized Archaic Greek youth statue marking a grave, exemplifying the kouros sculptural type.'),
    ('Praying Boy of Berlin', 'Praying Boy', 'Unknown (Hellenistic, Rhodes)', 'c. 300 BCE', 'Greece', 'A Hellenistic bronze of a youth caught in prayerful gesture, later admired by Frederick the Great.'),
    ('The Ilissos River God', 'Ilissos (sculpture)', 'Phidias (workshop)', 'c. 438-432 BCE', 'Greece', 'A reclining pedimental figure from the Parthenon depicting a personified river god.'),
    ('The Terme Ruler', 'Terme Ruler', 'Unknown (Hellenistic)', '2nd century BCE', 'Greece', 'A rare surviving bronze portrait of a Hellenistic ruler, notable for its heroic nudity.'),
    ('The Getty Bronze (Victorious Youth)', 'Victorious Youth', 'Lysippos (attributed)', 'c. 300-100 BCE', 'Greece', 'A rare surviving large-scale Greek bronze of an athlete crowning himself with a victory wreath.'),
    ('The Piraeus Apollo', 'Piraeus Apollo', 'Unknown (Archaic Greek)', 'c. 530-520 BCE', 'Greece', 'One of the oldest known large hollow-cast bronze statues from ancient Greece.'),
    ('Hera of Samos', 'Hera of Samos', 'Unknown (Archaic Greek)', 'c. 570-560 BCE', 'Greece', 'A monumental Archaic marble statue of the goddess Hera from her sanctuary on Samos.'),
    ('The Getty Kouros', 'Getty kouros', 'Unknown (disputed authenticity)', 'disputed, possibly 530 BCE or modern forgery', 'Greece', 'A marble kouros statue whose authenticity has been debated by scholars for decades.'),
    ('Statue of Idrimi', 'Statue of Idrimi', 'Ancient Syrians (Alalakh)', 'c. 1500 BCE', 'Syria', 'An inscribed statue of a Bronze Age king, valuable for its autobiographical cuneiform text.'),
    ('The Priest-King of Mohenjo-daro', 'Priest-King (sculpture)', 'Indus Valley Civilization', 'c. 2300-1750 BCE', 'Pakistan', 'A small steatite bust regarded as one of the finest surviving Indus Valley sculptures.'),
    ('Sculptures of Khajuraho Temples', 'Khajuraho Group of Monuments', 'Chandela dynasty craftsmen', '10th-11th century', 'India', 'Temple sculptures renowned for their intricate and often erotic figural carvings.'),
    ('Elephanta Caves Trimurti', 'Elephanta Caves', 'Unknown (Hindu, likely Kalachuri dynasty)', '5th-8th century CE', 'India', 'A monumental three-faced sculpture of Shiva carved within rock-cut cave temples on Elephanta Island.'),
    ('Mahabalipuram Shore Temple Reliefs', 'Shore Temple', 'Pallava dynasty craftsmen', '8th century CE', 'India', 'A seaside Hindu temple famed for its finely carved granite reliefs facing the Bay of Bengal.'),
    ('Descent of the Ganges Relief', "Arjuna's Penance", 'Pallava dynasty craftsmen', '7th century CE', 'India', 'One of the largest open-air rock reliefs in the world, carved at Mahabalipuram.'),
    ('Guardian Lions of the Forbidden City', 'Chinese guardian lions', 'Ming dynasty craftsmen', '15th century onward', 'China', 'Paired stone lion statues traditionally placed to guard palaces, temples, and government buildings.'),
    ('Marble Boat of the Summer Palace', 'Marble Boat', 'Qing dynasty craftsmen (Empress Dowager Cixi)', '1755, rebuilt 1893', 'China', "An ornate marble-clad pavilion built in the shape of a boat at Beijing's Summer Palace."),
    ('Dogu Figurines of Jomon Japan', 'Dogū', 'Jōmon-period craftsmen', 'c. 10,000-300 BCE', 'Japan', "Enigmatic clay figurines with exaggerated features from Japan's prehistoric Jōmon culture."),
    ('Statue of King Sejong the Great', 'Statue of King Sejong the Great', 'Modern Korean sculptors', '2009', 'Korea', "A monumental bronze statue in Seoul's Gwanghwamun Square honoring the creator of Hangul."),
    ('Statue of Admiral Yi Sun-sin', 'Statue of Yi Sun-sin', 'Kim Se-jung', '1968', 'Korea', "A prominent bronze memorial in Seoul honoring Korea's celebrated naval commander."),
    ('Terracotta Figures of Ban Chiang', 'Ban Chiang', 'Ban Chiang culture', 'c. 1500 BCE-900 CE', 'Thailand', 'Painted pottery and bronze artifacts from an early Southeast Asian Bronze Age culture.'),
    ('Dvaravati Buddha Images', 'Dvaravati', 'Dvaravati culture craftsmen', '6th-11th century CE', 'Thailand', 'Early Buddhist stone and bronze images from the Mon Dvaravati culture of Southeast Asia.'),
    ('Cham Sculpture of My Son Sanctuary', 'Mỹ Sơn', 'Champa civilization', '4th-14th century CE', 'Vietnam', 'Hindu temple ruins and sandstone sculpture from the ancient Kingdom of Champa.'),
    ("Auguste Rodin's Adam", 'Adam (Rodin)', 'Auguste Rodin', '1880-1881', 'France', 'A monumental bronze figure of the biblical Adam, conceived alongside The Gates of Hell.'),
    ("Rodin's Meditation Without Arms", 'The Inner Voice', 'Auguste Rodin', '1896', 'France', 'An armless female figure representing poetic inspiration, originally part of a Victor Hugo monument.'),
    ("Antonio Canova's Psyche Revived by Cupid's Kiss", "Psyche Revived by Cupid's Kiss", 'Antonio Canova', '1787-1793', 'Italy', 'A Neoclassical marble capturing the tender moment Cupid revives Psyche with a kiss.'),
    ("Antonio Canova's The Three Graces", 'The Three Graces (Canova)', 'Antonio Canova', '1814-1817', 'Italy', 'A refined Neoclassical marble grouping of the mythological Graces, celebrated for its idealized beauty.'),
    ("Canova's Venus Victrix (Pauline Bonaparte)", 'Venus Victrix (Canova)', 'Antonio Canova', '1805-1808', 'Italy', "A reclining marble portrait of Napoleon's sister Pauline Bonaparte posed as the triumphant Venus."),
    ("Jean-Antoine Houdon's Voltaire Seated", 'Seated Voltaire', 'Jean-Antoine Houdon', '1781', 'France', "A penetrating marble portrait of the philosopher Voltaire, considered one of Houdon's masterpieces."),
    ("Houdon's George Washington", 'George Washington (Houdon)', 'Jean-Antoine Houdon', '1788-1792', 'France/United States', 'A life-sized marble statue of George Washington, still displayed in the Virginia State Capitol.'),
    ("Edmonia Lewis's The Death of Cleopatra", 'The Death of Cleopatra (Lewis)', 'Edmonia Lewis', '1876', 'United States', "A bold marble depicting Cleopatra's death, by the first African American and Native American sculptor to gain international fame."),
    ("Augustus Saint-Gaudens's Diana", 'Diana (Saint-Gaudens)', 'Augustus Saint-Gaudens', '1892-1893', 'United States', "A gilded weathervane statue of the goddess Diana that once crowned New York's Madison Square Garden."),
    ("Saint-Gaudens's Sherman Monument", 'Sherman Monument', 'Augustus Saint-Gaudens', '1892-1903', 'United States', 'A gilded bronze equestrian monument to Civil War general William Tecumseh Sherman in New York.'),
    ("Daniel Chester French's Lincoln Memorial Statue", 'Abraham Lincoln (Daniel Chester French)', 'Daniel Chester French', '1920', 'United States', 'The monumental seated marble statue of Abraham Lincoln housed within the Lincoln Memorial.'),
    ("Gutzon Borglum's Seated Lincoln", 'Seated Lincoln', 'James Earle Fraser', '1911', 'United States', 'A bronze memorial statue of Abraham Lincoln seated in contemplation in Newark, New Jersey.'),
    ("Frederic Remington's The Bronco Buster", 'The Bronco Buster', 'Frederic Remington', '1895', 'United States', 'A dynamic bronze depicting a cowboy taming a rearing horse, an icon of American Western art.'),
]

MORE_ARCHITECTURE_BATCH2 = [
    ('Angkor Thom City Gates', 'Angkor Thom', 'Khmer Empire (Jayavarman VII)', 'late 12th century', 'Cambodia', 'The fortified last capital of the Khmer Empire, entered through gates topped with giant carved faces.'),
    ('Ta Prohm Temple', 'Ta Prohm', 'Khmer Empire (Jayavarman VII)', '1186 CE', 'Cambodia', 'A jungle temple famous for enormous tree roots enveloping its ancient stone structures.'),
    ('Petra Ancient City', 'Petra', 'Nabataeans', 'c. 4th century BCE onward', 'Jordan', 'A rock-cut Nabataean city famous for its elaborate facades carved directly into rose-red sandstone cliffs.'),
    ('Prambanan Temple Complex', 'Prambanan', 'Mataram Kingdom', '9th century CE', 'Indonesia', 'The largest Hindu temple complex in Indonesia, dedicated to the Trimurti of Brahma, Vishnu, and Shiva.'),
    ('Edinburgh Castle', 'Edinburgh Castle', 'Medieval Scottish builders', '12th century onward', 'United Kingdom', "A historic fortress dominating the skyline of Edinburgh, one of Scotland's most visited sites."),
    ('Lalibela Rock-Hewn Churches (Bete Giyorgis)', 'Church of Saint George, Lalibela', 'Ethiopian builders (King Lalibela)', '12th-13th century', 'Ethiopia', 'A cross-shaped church carved downward out of a single block of volcanic rock.'),
    ('Tiwanaku Monumental Complex', 'Tiwanaku', 'Tiwanaku civilization', 'c. 300-1000 CE', 'Bolivia', 'The ceremonial and political center of a major pre-Inca Andean civilization near Lake Titicaca.'),
    ('Great Wall of China (Mutianyu section)', 'Mutianyu Great Wall', 'Ming dynasty builders', '6th century BCE-17th century CE', 'China', 'A well-preserved section of the Great Wall known for its watchtowers and forested surroundings.'),
    ("St. Peter's Basilica Dome", "St. Peter's Basilica", 'Donato Bramante, Michelangelo, and others', '1506-1626', 'Vatican City', "The largest church in the world by interior measure, capped by Michelangelo's soaring dome."),
    ('Milan Cathedral (Duomo di Milano)', 'Milan Cathedral', 'Various Gothic architects', '1386-1965 (completed over centuries)', 'Italy', 'One of the largest Gothic cathedrals in the world, adorned with thousands of statues and spires.'),
    ('Florence Cathedral Dome (Il Duomo)', 'Florence Cathedral', 'Filippo Brunelleschi (dome)', '1296-1436', 'Italy', "Brunelleschi's dome remains the largest brick dome ever constructed, a triumph of Renaissance engineering."),
    ('Palace of Westminster', 'Palace of Westminster', 'Charles Barry and Augustus Pugin', '1840-1876', 'United Kingdom', 'The Gothic Revival seat of the UK Parliament, home to the clock tower housing Big Ben.'),
    ('Windsor Castle', 'Windsor Castle', 'Medieval English builders (William the Conqueror)', '11th century onward', 'United Kingdom', 'The oldest and largest continuously inhabited castle in the world, an official royal residence.'),
    ('Tower of London', 'Tower of London', 'William the Conqueror (commissioned)', '1078 onward', 'United Kingdom', 'A historic fortress on the Thames famed for housing the Crown Jewels of England.'),
    ('Prague Castle', 'Prague Castle', 'Medieval Bohemian builders', '9th century onward', 'Czech Republic', 'The largest ancient castle complex in the world by area, seat of Czech rulers for over a millennium.'),
    ('Charles Bridge', 'Charles Bridge', 'Peter Parler', '1357-1402', 'Czech Republic', 'A medieval stone bridge across the Vltava River in Prague, lined with baroque statues.'),
    ('Cologne Cathedral', 'Cologne Cathedral', 'Medieval German builders', '1248-1880 (completed over centuries)', 'Germany', "A towering Gothic cathedral that was the world's tallest structure upon completion in 1880."),
    ('Brandenburg Gate', 'Brandenburg Gate', 'Carl Gotthard Langhans', '1788-1791', 'Germany', 'A Neoclassical triumphal arch in Berlin that became a symbol of German reunification.'),
    ('Peterhof Palace Fountains', 'Peterhof Palace', 'Various Russian and European architects', '1714 onward', 'Russia', "A grand imperial palace and garden estate known as the 'Russian Versailles'."),
    ('Winter Palace (Hermitage)', 'Winter Palace', 'Bartolomeo Rastrelli', '1754-1762', 'Russia', 'The former official residence of Russian tsars, now part of the State Hermitage Museum.'),
    ('Charles V Palace of Alhambra', 'Palace of Charles V', 'Pedro Machuca', '1527 onward', 'Spain', 'A Renaissance palace built within the Nasrid Alhambra complex, contrasting sharply with its Islamic surroundings.'),
    ('Alcázar of Segovia', 'Alcázar of Segovia', 'Medieval Spanish builders', '12th century onward', 'Spain', "A dramatic cliff-top castle said to have inspired Disney's Cinderella Castle."),
    ('Belém Tower', 'Belém Tower', 'Francisco de Arruda', '1514-1519', 'Portugal', 'A fortified tower in Lisbon marking the start of Portuguese voyages of exploration.'),
    ('Jerónimos Monastery', 'Jerónimos Monastery', 'Diogo de Boitaca and João de Castilho', '1501-1601', 'Portugal', "A Manueline-style monastery in Lisbon celebrating Portugal's Age of Discovery."),
    ('Topkapı Palace', 'Topkapı Palace', 'Ottoman sultans (Mehmed II)', '1459-1465', 'Turkey', 'The primary residence of Ottoman sultans for nearly 400 years, overlooking the Bosphorus.'),
    ('Imam Mosque of Isfahan', 'Shah Mosque', 'Safavid dynasty (Shah Abbas I)', '1611-1629', 'Iran', 'A masterpiece of Persian Islamic architecture renowned for its elaborate blue tilework.'),
    ('Sheikh Lotfollah Mosque', 'Sheikh Lotfollah Mosque', 'Safavid dynasty craftsmen', '1603-1619', 'Iran', 'A domed mosque in Isfahan celebrated for its exceptionally intricate tilework and lack of minarets.'),
    ('Persepolis Ceremonial Complex', 'Persepolis', 'Achaemenid dynasty (Darius I)', 'c. 518 BCE onward', 'Iran', 'The ceremonial capital of the ancient Achaemenid Persian Empire, famed for its monumental relief staircases.'),
    ('Hawa Mahal', 'Hawa Mahal', 'Lal Chand Ustad', '1799', 'India', "The 'Palace of Winds' in Jaipur, a honeycomb sandstone facade of 953 small windows."),
    ('Amber Fort', 'Amber Fort', 'Raja Man Singh I', '1592 onward', 'India', 'A hilltop fortress-palace near Jaipur known for its artistic Rajput and Mughal architectural style.'),
    ("Humayun's Tomb", "Humayun's Tomb", 'Mirak Mirza Ghiyas', '1569-1570', 'India', 'A monumental Mughal garden-tomb that served as an architectural precursor to the Taj Mahal.'),
    ('Red Fort of Delhi', 'Red Fort', 'Ustad Ahmad Lahauri', '1638-1648', 'India', 'The main residence of Mughal emperors for nearly 200 years, built of red sandstone.'),
    ('Fatehpur Sikri', 'Fatehpur Sikri', 'Mughal dynasty (Akbar)', '1571-1585', 'India', 'A short-lived Mughal capital city built entirely of red sandstone, later abandoned due to water scarcity.'),
    ('Wat Arun Temple', 'Wat Arun', 'Thai builders (Rama II)', 'early 19th century', 'Thailand', 'A Buddhist temple on the Chao Phraya River famous for its towering porcelain-encrusted spire.'),
    ('Wat Phra Kaew', 'Wat Phra Kaew', 'Thai builders (Rama I)', '1782 onward', 'Thailand', 'The royal temple complex in Bangkok housing the sacred Emerald Buddha.'),
    ('Bagan Temple Plain', 'Bagan', 'Pagan Kingdom (Anawrahta)', '11th-13th century', 'Myanmar', 'A vast plain containing thousands of Buddhist temples and pagodas built by the ancient Pagan Kingdom.'),
    ('Fushimi Inari Shrine Gates', 'Fushimi Inari-taisha', 'Traditional Japanese builders', '711 CE onward', 'Japan', 'A Shinto shrine famous for its thousands of vermillion torii gates winding up a sacred mountain.'),
    ('Osaka Castle', 'Osaka Castle', 'Toyotomi Hideyoshi', '1583 onward', 'Japan', "One of Japan's most famous castles, central to the unification of Japan in the 16th century."),
    ('Gyeongbokgung Palace', 'Gyeongbokgung', 'Joseon dynasty (King Taejo)', '1395', 'Korea', "The largest of Korea's Five Grand Palaces, the primary royal residence of the Joseon dynasty."),
    ('Bulguksa Temple', 'Bulguksa', 'Silla dynasty', '8th century CE', 'Korea', 'A Buddhist temple complex renowned as a masterpiece of Silla-era architecture and stone artistry.'),
    ('Ha Long Bay Karst Formations', 'Ha Long Bay', 'Natural formation (culturally significant)', 'geological', 'Vietnam', 'Thousands of limestone karst islands and islets rising from emerald waters, a UNESCO World Heritage Site.'),
    ('Sydney Harbour Bridge', 'Sydney Harbour Bridge', 'John Bradfield', '1932', 'Australia', "A steel through-arch bridge and iconic landmark of Sydney's harbor skyline."),
    ('CN Tower', 'CN Tower', 'Canadian National (engineers)', '1976', 'Canada', "A telecommunications tower in Toronto that was the world's tallest freestanding structure for over 30 years."),
    ('Corcovado Mountain (Christ the Redeemer site)', 'Corcovado', 'Paul Landowski', '1931', 'Brazil', 'The mountain summit overlooking Rio de Janeiro on which the Christ the Redeemer statue stands.'),
    ('Teatro Colón', 'Teatro Colón', 'Francesco Tamburini and Vittorio Meano', '1908', 'Argentina', "One of the world's great opera houses, renowned for its exceptional acoustics."),
    ('Panama Canal Locks', 'Panama Canal', 'United States Army Corps of Engineers', '1904-1914', 'Panama', 'A monumental engineering feat connecting the Atlantic and Pacific Oceans through a system of locks.'),
    ('Niagara Falls', 'Niagara Falls', 'Natural formation (culturally significant)', 'geological', 'Canada/United States', 'A group of three waterfalls on the Canada-US border, among the most powerful in North America.'),
    ('Hoover Dam', 'Hoover Dam', 'United States Bureau of Reclamation', '1931-1936', 'United States', 'A massive concrete arch-gravity dam on the Colorado River, an icon of Depression-era engineering.'),
    ('Chrysler Building', 'Chrysler Building', 'William Van Alen', '1930', 'United States', 'An Art Deco skyscraper in New York famed for its stainless-steel crown and gargoyle ornaments.'),
    ('One World Trade Center', 'One World Trade Center', 'David Childs (SOM)', '2014', 'United States', 'The tallest building in the Western Hemisphere, built on the site of the original World Trade Center.'),
    ('Biltmore Estate', 'Biltmore Estate', 'Richard Morris Hunt', '1889-1895', 'United States', 'The largest privately owned house in the United States, built in French Renaissance château style.'),
    ('Independence Hall', 'Independence Hall', 'Edmund Woolley and Andrew Hamilton', '1732-1753', 'United States', 'The Philadelphia building where both the Declaration of Independence and US Constitution were debated and signed.'),
    ('Casa Batlló', 'Casa Batlló', 'Antoni Gaudí', '1904-1906', 'Spain', 'A whimsical Gaudí-designed residential building in Barcelona known for its skeletal balconies and dragon-scale roof.'),
    ('Park Güell', 'Park Güell', 'Antoni Gaudí', '1900-1914', 'Spain', "A public park in Barcelona famous for Gaudí's colorful mosaic-tiled structures and organic forms."),
    ('Palace of Fine Arts (San Francisco)', 'Palace of Fine Arts', 'Bernard Maybeck', '1915', 'United States', 'A monumental Beaux-Arts structure built for the 1915 Panama-Pacific Exposition and later rebuilt in permanent materials.'),
    ('Fallingwater', 'Fallingwater', 'Frank Lloyd Wright', '1937-1939', 'United States', "A house built directly over a waterfall, widely regarded as Frank Lloyd Wright's masterpiece."),
    ('Guggenheim Museum Bilbao', 'Guggenheim Museum Bilbao', 'Frank Gehry', '1997', 'Spain', 'A titanium-clad deconstructivist museum that transformed Bilbao into a global architecture destination.'),
    ('Sydney Tower', 'Sydney Tower', 'Donald Crone & Associates', '1981', 'Australia', 'The tallest freestanding structure in Sydney, offering panoramic views over the harbor city.'),
    ('Space Needle', 'Space Needle', 'John Graham & Company', '1962', 'United States', "A futuristic observation tower built for the 1962 Seattle World's Fair, an icon of the Pacific Northwest."),
    ('Willis Tower (Sears Tower)', 'Willis Tower', 'Skidmore, Owings and Merrill', '1973', 'United States', "A bundled-tube skyscraper in Chicago that was the world's tallest building for nearly 25 years."),
    ('Petronas Towers', 'Petronas Towers', 'César Pelli', '1998', 'Malaysia', 'Twin skyscrapers in Kuala Lumpur that were the tallest buildings in the world when completed.'),
    ('Marina Bay Sands', 'Marina Bay Sands', 'Moshe Safdie', '2010', 'Singapore', 'A resort complex famous for its rooftop infinity pool connecting three towers.'),
    ('Shanghai Tower', 'Shanghai Tower', 'Gensler', '2015', 'China', 'A twisting skyscraper that is one of the tallest buildings in the world, engineered for seismic and wind resistance.'),
    ('Taipei 101', 'Taipei 101', 'C.Y. Lee', '2004', 'Taiwan', 'A skyscraper famed for its pagoda-inspired design and massive tuned mass damper for typhoon and earthquake resistance.'),
    ('Millau Viaduct', 'Millau Viaduct', 'Michel Virlogeux and Norman Foster', '2004', 'France', 'The tallest bridge in the world, spanning the Tarn River valley in southern France.'),
    ("Charles La Trobe's Parliament House Canberra", 'Parliament House, Canberra', 'Mitchell/Giurgola', '1988', 'Australia', "Australia's national legislature, distinctively built into a hill and topped by a large flagpole."),
    ('Luxor Temple', 'Luxor Temple', 'Ancient Egyptians (Amenhotep III, Ramesses II)', 'c. 1400 BCE onward', 'Egypt', 'A large ancient Egyptian temple complex, unusually dedicated to the rejuvenation of kingship rather than a single god.'),
    ('Step Pyramid of Djoser', 'Pyramid of Djoser', 'Imhotep', 'c. 2670 BCE', 'Egypt', "Egypt's oldest colossal stone building, considered the world's earliest large-scale cut-stone construction."),
    ('Baths of Diocletian', 'Baths of Diocletian', 'Ancient Romans', '298-306 CE', 'Italy (Rome)', 'One of the largest public bathing complexes of the Roman Empire, partly repurposed as a church by Michelangelo.'),
    ("Diocletian's Palace (Split)", "Diocletian's Palace", 'Ancient Romans (Diocletian)', '295-305 CE', 'Croatia', 'A vast retirement palace for the Roman emperor Diocletian that today forms the core of the city of Split.'),
    ('Segovia Aqueduct', 'Aqueduct of Segovia', 'Ancient Romans', '1st-2nd century CE', 'Spain', 'A remarkably well-preserved Roman aqueduct bridge still standing without mortar in central Spain.'),
    ('Verona Arena', 'Verona Arena', 'Ancient Romans', '30 CE', 'Italy', 'A Roman amphitheater still used today for large-scale opera performances.'),
    ('El Jem Amphitheatre', 'El Jem amphitheatre', 'Ancient Romans', 'c. 238 CE', 'Tunisia', 'One of the best-preserved Roman amphitheaters in the world, rivaling the Colosseum in scale.'),
    ('Leptis Magna Ruins', 'Leptis Magna', 'Ancient Romans (Septimius Severus)', '1st century BCE-3rd century CE', 'Libya', 'One of the most spectacular and unspoiled ruined cities of the Roman Empire.'),
    ('Mesa Verde Cliff Dwellings', 'Mesa Verde National Park', 'Ancestral Puebloans', 'c. 550-1300 CE', 'United States', 'A national park preserving well-preserved Ancestral Puebloan cliff dwellings and mesa-top structures.'),
    ('Uxmal Pyramid of the Magician', 'Uxmal', 'Maya civilization', 'c. 700-1000 CE', 'Mexico', 'A major Maya city renowned for its unusually rounded Pyramid of the Magician and Puuc architectural style.'),
    ('Copán Maya Ruins', 'Copán', 'Maya civilization', '5th-9th century CE', 'Honduras', 'A major Maya city celebrated for its exceptionally detailed carved stelae and hieroglyphic stairway.'),
    ('Teotihuacan Pyramid of the Moon', 'Pyramid of the Moon', 'Teotihuacan civilization', 'c. 100-450 CE', 'Mexico', 'The second-largest pyramid at the ancient city of Teotihuacan, terminus of its great Avenue of the Dead.'),
    ('Sukhothai Historical Park', 'Sukhothai Historical Park', 'Sukhothai Kingdom', '13th-14th century', 'Thailand', "The ruined capital of Thailand's first independent kingdom, known for its distinctive lotus-bud stupas."),
    ('Polonnaruwa Ancient City', 'Polonnaruwa', 'Sinhalese kings', '11th-13th century CE', 'Sri Lanka', 'The well-preserved second ancient capital of Sri Lanka, home to monumental Buddhist temple ruins and rock-carved Buddhas.'),
]

CATEGORY_ASSIGNMENTS.append((MORE_SCULPTURE_BATCH2, "sculpture"))
CATEGORY_ASSIGNMENTS.append((MORE_ARCHITECTURE_BATCH2, "architecture"))




# Real, individually famous historic manuscripts and documents from across
# world cultures and eras -- charters, illuminated gospels, sacred texts,
# scientific notebooks, and founding national documents.
MORE_MANUSCRIPTS_BATCH2: list[tuple] = [
    ("Book of Kells", "Book of Kells", "Unknown Celtic monks", "c. 800 CE", "Ireland", "An elaborately illuminated Gospel manuscript created by Columban monks, renowned as the pinnacle of Insular art."),
    ("Codex Sinaiticus", "Codex Sinaiticus", "Unknown scribes", "c. 330-360 CE", "Byzantine Empire (Egypt)", "One of the oldest surviving complete manuscripts of the Christian Bible, discovered at Saint Catherine's Monastery."),
    ("Domesday Book", "Domesday Book", "Commissioned by William I", "1086", "England", "A vast survey of landholdings and resources across Norman England, still used as a legal record today."),
    ("Diamond Sutra", "Diamond Sutra", "Unknown", "868 CE", "China", "The world's oldest dated printed book, a Buddhist scripture discovered in the Mogao Caves at Dunhuang."),
    ("Voynich Manuscript", "Voynich Manuscript", "Unknown", "early 15th century", "Italy (likely)", "An illustrated codex written in an unidentified script that has defied all attempts at decipherment."),
    ("Gutenberg Bible", "Gutenberg Bible", "Johannes Gutenberg", "c. 1454-1455", "Germany", "The first major book printed in Europe using movable type, marking the start of the print revolution."),
    ("Magna Carta", "Magna Carta", "King John's chancery", "1215", "England", "A charter of rights agreed by King John that established the principle that the monarch is subject to the law."),
    ("United States Declaration of Independence", "United States Declaration of Independence", "Continental Congress (drafted by Thomas Jefferson)", "1776", "United States", "The founding document declaring the thirteen American colonies independent from Great Britain."),
    ("Constitution of the United States", "Constitution of the United States", "Constitutional Convention", "1787", "United States", "The supreme governing document of the United States, the oldest still-functioning written national constitution."),
    ("Dead Sea Scrolls", "Dead Sea Scrolls", "Unknown (likely Essene community)", "c. 3rd century BCE-1st century CE", "Israel/Palestine (Qumran)", "A collection of ancient Jewish manuscripts including the oldest known copies of Hebrew Bible texts."),
    ("Lindisfarne Gospels", "Lindisfarne Gospels", "Eadfrith of Lindisfarne", "c. 700-720 CE", "England", "An illuminated Latin Gospel book produced on Lindisfarne, celebrated for its intricate Insular decoration."),
    ("Nuremberg Chronicle", "Nuremberg Chronicle", "Hartmann Schedel", "1493", "Germany", "One of the best-documented early printed books, an illustrated world history combining biblical and secular chronicle."),
    ("Codex Leicester", "Codex Leicester", "Leonardo da Vinci", "1508-1510", "Italy", "A scientific notebook by Leonardo da Vinci exploring astronomy, water, and geology, now owned by Bill Gates."),
    ("Blue Qur'an", "Blue Qur'an", "Unknown", "c. 9th-10th century", "Tunisia", "A luxurious Qur'an manuscript written in gold Kufic script on rare indigo-dyed parchment."),
    ("Codex Vaticanus", "Codex Vaticanus", "Unknown scribes", "c. 300-325 CE", "Byzantine Empire (Egypt)", "One of the oldest extant manuscripts of the Greek Bible, held in the Vatican Library."),
    ("Codex Alexandrinus", "Codex Alexandrinus", "Unknown scribes", "5th century CE", "Egypt", "A fifth-century manuscript of the Greek Bible that is one of the four great uncial codices."),
    ("Ellesmere Chaucer", "Ellesmere Chaucer", "Geoffrey Chaucer (text); unknown scribe", "c. 1400-1410", "England", "One of the earliest and most famous surviving manuscripts of Chaucer's 'Canterbury Tales'."),
    ("Winchester Bible", "Winchester Bible", "Unknown monks of Winchester", "c. 1160-1175", "England", "The largest surviving 12th-century English illuminated bible, renowned for its lavish decoration."),
    ("Book of Durrow", "Book of Durrow", "Unknown Irish monks", "c. 650-700 CE", "Ireland", "The earliest of the fully decorated Insular Gospel books, a precursor to the Book of Kells."),
    ("Utrecht Psalter", "Utrecht Psalter", "Unknown", "c. 820-835 CE", "France", "A Carolingian psalter famous for its vivid pen-and-ink illustrations of every psalm."),
    ("Book of the Dead", "Book of the Dead", "Various scribes", "c. 1550 BCE onward", "Egypt", "A collection of funerary spells intended to guide the deceased safely through the afterlife."),
    ("Papyrus of Ani", "Papyrus of Ani", "Scribe Ani (attributed)", "c. 1250 BCE", "Egypt", "One of the finest surviving examples of the Egyptian Book of the Dead, richly illustrated on papyrus."),
    ("Turin King List", "Turin King List", "Unknown scribe", "c. 1200 BCE", "Egypt", "A papyrus recording the names of Egyptian pharaohs, a crucial source for ancient Egyptian chronology."),
    ("Dunhuang manuscripts", "Dunhuang manuscripts", "Various scribes", "5th-11th century CE", "China", "A vast trove of religious and secular texts sealed in the Mogao Caves for nearly a millennium."),
    ("Genji Monogatari Emaki", "Genji Monogatari Emaki", "Unknown court artists", "12th century", "Japan", "The oldest surviving illustrated handscroll of 'The Tale of Genji', a landmark of Japanese art."),
    ("Hyakumantō Darani", "Hyakumantō Darani", "Commissioned by Empress Shōtoku", "764-770 CE", "Japan", "Buddhist prayer texts printed and distributed in a million miniature wooden pagodas, among the earliest printed works."),
    ("Jikji", "Jikji", "Compiled by the monk Baegun", "1377", "Korea", "The oldest extant book printed using movable metal type, predating Gutenberg's press."),
    ("Rhind Mathematical Papyrus", "Rhind Mathematical Papyrus", "Scribe Ahmes", "c. 1550 BCE", "Egypt", "One of the best-known sources for ancient Egyptian mathematics, containing problems and solutions."),
    ("Ebers Papyrus", "Ebers Papyrus", "Unknown", "c. 1550 BCE", "Egypt", "One of the oldest and most important medical papyri, cataloguing Egyptian remedies and diagnoses."),
    ("Vergilius Vaticanus", "Vergilius Vaticanus", "Unknown", "c. 400 CE", "Italy", "One of the oldest surviving illustrated manuscripts of classical literature, containing works of Virgil."),
    ("Vienna Dioscurides", "Vienna Dioscurides", "Unknown", "512 CE", "Byzantine Empire", "An early illustrated herbal manuscript based on the work of Dioscorides, prized for its botanical illustrations."),
    ("Golden Haggadah", "Golden Haggadah", "Unknown", "c. 1320", "Spain", "One of the most lavishly illuminated medieval Hebrew manuscripts, used for the Passover Seder."),
    ("Sarajevo Haggadah", "Sarajevo Haggadah", "Unknown", "c. 1350", "Spain", "A richly illuminated Sephardic Haggadah that survived multiple wars, now held in Sarajevo."),
    ("Aleppo Codex", "Aleppo Codex", "Scribe Shlomo ben Buya'a", "c. 930 CE", "Israel", "A medieval manuscript of the Hebrew Bible long regarded as the most authoritative text of the Masoretic tradition."),
    ("Leningrad Codex", "Leningrad Codex", "Scribe Samuel ben Jacob", "1008 CE", "Egypt", "The oldest complete manuscript of the Hebrew Bible in Hebrew, using the Masoretic tradition."),
    ("Great Isaiah Scroll", "Great Isaiah Scroll", "Unknown", "c. 125 BCE", "Israel", "The best-preserved and most complete of the Dead Sea Scrolls, containing the entire Book of Isaiah."),
    ("Codex Mendoza", "Codex Mendoza", "Aztec scribes", "c. 1541", "Mexico", "A pictorial Aztec manuscript commissioned by the Spanish viceroy documenting Aztec history, tribute, and daily life."),
    ("Dresden Codex", "Dresden Codex", "Maya scribes", "11th-12th century", "Mexico/Guatemala", "The oldest surviving book written in the Americas, a Maya manuscript recording astronomical calculations."),
    ("Madrid Codex (Maya)", "Madrid Codex (Maya)", "Maya scribes", "15th century", "Mexico", "One of only four surviving pre-Columbian Maya books, containing almanacs and astronomical tables."),
    ("Popol Vuh", "Popol Vuh", "Unknown K'iche' Maya author(s)", "c. 1701 (transcription)", "Guatemala", "A foundational Maya narrative recounting the mythology and history of the K'iche' people."),
    ("Florentine Codex", "Florentine Codex", "Bernardino de Sahagún with Nahua scribes", "1545-1590", "Mexico", "A monumental bilingual ethnographic encyclopedia documenting Aztec culture, language, and history."),
    ("Très Riches Heures du Duc de Berry", "Très Riches Heures du Duc de Berry", "Limbourg brothers", "1412-1416", "France", "The most celebrated illuminated manuscript of the International Gothic style, famed for its calendar miniatures."),
    ("Luttrell Psalter", "Luttrell Psalter", "Unknown", "c. 1325-1340", "England", "An illuminated psalter renowned for its vivid marginal scenes of medieval rural life."),
    ("Codex Amiatinus", "Codex Amiatinus", "Unknown monks of Wearmouth-Jarrow", "c. 700 CE", "England", "The oldest surviving complete manuscript of the Latin Vulgate Bible, produced in Anglo-Saxon England."),
    ("Emancipation Proclamation", "Emancipation Proclamation", "Abraham Lincoln", "1863", "United States", "The executive order declaring enslaved people in Confederate states to be free."),
    ("United States Bill of Rights", "United States Bill of Rights", "James Madison", "1789/1791", "United States", "The first ten amendments to the US Constitution, guaranteeing fundamental civil liberties."),
    ("Treaty of Waitangi", "Treaty of Waitangi", "British Crown and Māori chiefs", "1840", "New Zealand", "The founding document of New Zealand, establishing a relationship between the British Crown and Māori."),
    ("Japanese Instrument of Surrender", "Japanese Instrument of Surrender", "Government of Japan and Allied Powers", "1945", "Japan", "The document formally ending World War II, signed aboard the USS Missouri in Tokyo Bay."),
    ("Kojiki", "Kojiki", "Ō no Yasumaro", "712 CE", "Japan", "The oldest surviving chronicle of Japanese history and mythology."),
    ("Uthman Quran", "Uthman Quran", "Unknown", "7th century (traditionally attributed)", "Uzbekistan", "An early Kufic Qur'an manuscript traditionally associated with Caliph Uthman, preserved in Tashkent."),
    ("Topkapi Scroll", "Topkapi Scroll", "Unknown", "c. 15th century", "Iran", "A lengthy scroll of geometric patterns used by craftsmen to design Islamic architectural ornamentation."),
    ("Baysonghori Shahnameh", "Baysonghori Shahnameh", "Court of Prince Baysonghor", "1430", "Iran", "One of the most lavishly illustrated manuscripts of Ferdowsi's epic 'Shahnameh'."),
    ("Shahnameh of Shah Tahmasp", "Shahnameh of Shah Tahmasp", "Safavid court workshop", "1520s-1530s", "Iran", "Also known as the Houghton Shahnameh, one of the greatest achievements of Persian manuscript painting."),
    ("Timbuktu Manuscripts", "Timbuktu Manuscripts", "Various West African scholars", "13th-16th century", "Mali", "A vast collection of manuscripts on science, law, and religion attesting to Timbuktu's role as an intellectual center."),
    ("Kebra Nagast", "Kebra Nagast", "Unknown", "14th century (compiled)", "Ethiopia", "The national epic of Ethiopia recounting the origins of the Solomonic dynasty."),
    ("Garima Gospels", "Garima Gospels", "Attributed to Abba Garima", "c. 4th-6th century", "Ethiopia", "Among the oldest surviving illuminated Christian manuscripts in the world."),
    ("Codex Borgia", "Codex Borgia", "Unknown Aztec/Mixtec scribes", "c. 15th century", "Mexico", "A pre-Columbian pictorial manuscript used for divination, renowned for its vivid ritual imagery."),
    ("Codex Zouche-Nuttall", "Codex Zouche-Nuttall", "Mixtec scribes", "c. 14th-15th century", "Mexico", "A pictorial Mixtec manuscript recording the genealogy and conquests of Lord Eight Deer."),
    ("Vindolanda tablets", "Vindolanda tablets", "Roman soldiers and officials", "c. 90-120 CE", "England", "The oldest surviving handwritten documents in Britain, offering a vivid record of life on the Roman frontier."),
    ("Bakhshali manuscript", "Bakhshali manuscript", "Unknown", "c. 3rd-4th century CE (disputed dating)", "Pakistan", "An ancient Indian mathematical text notable for containing one of the earliest uses of a symbol for zero."),
]
CATEGORY_ASSIGNMENTS.append((MORE_MANUSCRIPTS_BATCH2, "manuscript"))

# Real, individually famous historic musical instruments -- named virtuoso
# instruments and iconic instrument types from cultures around the world.
MORE_INSTRUMENTS_BATCH2: list[tuple] = [
    ("Lady Blunt Stradivarius", "Lady Blunt (violin)", "Antonio Stradivari", "1721", "Italy", "An exceptionally well-preserved Stradivarius violin that sold at auction in 2011 for a record price."),
    ("Messiah Stradivarius", "Messiah Stradivarius", "Antonio Stradivari", "1716", "Italy", "One of the best-preserved Stradivarius violins in existence, rarely played and housed at the Ashmolean Museum."),
    ("Vieuxtemps Guarneri", "Vieuxtemps Guarneri", "Giuseppe Guarneri del Gesù", "1741", "Italy", "Regarded by many soloists as one of the finest-sounding violins ever made."),
    ("Hammer Stradivarius", "Hammer Stradivarius", "Antonio Stradivari", "1707", "Italy", "A celebrated Stradivarius violin from the maker's 'golden period' of instrument-making."),
    ("Molitor Stradivarius", "Molitor Stradivarius", "Antonio Stradivari", "1697", "Italy", "A historic violin once reputed to have belonged to Napoleon Bonaparte's family."),
    ("Davidov Stradivarius", "Davidov Stradivarius", "Antonio Stradivari", "1712", "Italy", "A renowned Stradivarius cello later played by Jacqueline du Pré and Yo-Yo Ma."),
    ("Duport Stradivarius", "Duport Stradivarius", "Antonio Stradivari", "1711", "Italy", "A famed Stradivarius cello once played by Napoleon and later owned by Mstislav Rostropovich."),
    ("Il Cannone Guarnerius", "Il Cannone Guarnerius", "Giuseppe Guarneri del Gesù", "1743", "Italy", "The favored violin of virtuoso Niccolò Paganini, nicknamed 'the Cannon' for its powerful tone."),
    ("Servais Stradivarius", "Servais Stradivarius", "Antonio Stradivari", "1701", "Italy", "A renowned Stradivarius cello named for its 19th-century virtuoso owner Adrien-François Servais."),
    ("Theremin", "Theremin", "Leon Theremin", "1920", "Russia", "An early electronic musical instrument played without physical contact, controlled by the performer's hand movements in an electromagnetic field."),
    ("Ondes Martenot", "Ondes Martenot", "Maurice Martenot", "1928", "France", "An early electronic keyboard instrument known for its distinctive wavering tone, used by composers including Messiaen."),
    ("Stroh Violin", "Stroh violin", "Augustus Stroh", "1899", "United Kingdom", "A violin fitted with a metal resonator horn instead of a wooden body, designed for early acoustic recording."),
    ("Sarangi", "Sarangi", "Traditional Indian instrument makers", "centuries-old tradition", "India", "A bowed short-necked string instrument central to Hindustani classical music, closely associated with the human voice."),
    ("Sitar", "Sitar", "Traditional Indian instrument makers", "centuries-old tradition", "India", "A long-necked plucked string instrument with sympathetic strings, central to North Indian classical music."),
    ("Tabla", "Tabla", "Traditional Indian instrument makers", "centuries-old tradition", "India", "A pair of hand drums fundamental to North Indian classical percussion."),
    ("Veena", "Veena", "Traditional Indian instrument makers", "centuries-old tradition", "India", "An ancient plucked string instrument central to South Indian Carnatic classical music."),
    ("Shamisen", "Shamisen", "Traditional Japanese instrument makers", "16th century onward", "Japan", "A three-stringed plucked lute central to Japanese folk and theatrical music, including kabuki and bunraku."),
    ("Koto", "Koto (instrument)", "Traditional Japanese instrument makers", "centuries-old tradition", "Japan", "A long plucked zither with movable bridges, considered the national instrument of Japan."),
    ("Guqin", "Guqin", "Traditional Chinese instrument makers", "over 3,000 years old tradition", "China", "An ancient seven-stringed plucked zither revered in Chinese literati culture for its refined, meditative sound."),
    ("Erhu", "Erhu", "Traditional Chinese instrument makers", "centuries-old tradition", "China", "A two-stringed bowed instrument often called the 'Chinese violin', prominent in traditional and modern Chinese music."),
    ("Pipa", "Pipa", "Traditional Chinese instrument makers", "over 2,000 years old tradition", "China", "A pear-shaped plucked lute with a history dating back over two millennia in China."),
    ("Gamelan", "Gamelan", "Traditional Javanese/Balinese ensembles", "centuries-old tradition", "Indonesia", "A traditional ensemble of tuned percussion instruments, including metallophones and gongs, central to Javanese and Balinese culture."),
    ("Talking Drum", "Talking drum", "Traditional West African instrument makers", "centuries-old tradition", "West Africa", "An hourglass-shaped drum whose pitch can be modulated to mimic the tones and rhythms of spoken language."),
    ("Kora", "Kora (instrument)", "Traditional Mandinka instrument makers", "centuries-old tradition", "West Africa", "A 21-string harp-lute central to the griot musical tradition of West Africa."),
    ("Djembe", "Djembe", "Traditional Mandinka instrument makers", "centuries-old tradition", "West Africa", "A goblet-shaped hand drum known for its wide range of tones, historically central to Mande culture."),
    ("Balalaika", "Balalaika", "Traditional Russian instrument makers", "18th century onward", "Russia", "A triangular-bodied plucked string instrument that became a national symbol of Russian folk music."),
    ("Bagpipes", "Bagpipes", "Traditional Scottish instrument makers", "centuries-old tradition", "Scotland", "A wind instrument using enclosed reeds fed by a constant reservoir of air, iconic to Scottish and Celtic music."),
    ("Alphorn", "Alphorn", "Traditional Swiss instrument makers", "centuries-old tradition", "Switzerland", "A long wooden natural horn traditionally used by herders in the Alps to communicate across valleys."),
    ("Didgeridoo", "Didgeridoo", "Aboriginal Australian instrument makers", "over 1,000 years old tradition", "Australia", "A wind instrument developed by Aboriginal Australians of northern Australia, producing a continuous drone through circular breathing."),
    ("Panpipes", "Pan flute", "Traditional Andean instrument makers", "centuries-old tradition", "Peru/Bolivia", "A set of tuned pipes bound together, central to Andean folk music traditions such as the siku."),
    ("Charango", "Charango", "Traditional Andean instrument makers", "18th century onward", "Bolivia/Peru", "A small Andean lute traditionally built with an armadillo-shell back, central to Andean folk ensembles."),
    ("Hurdy-gurdy", "Hurdy-gurdy", "Traditional European instrument makers", "medieval origin", "France", "A string instrument that produces sound via a hand-cranked, rosined wheel rubbing against the strings."),
    ("Nyckelharpa", "Nyckelharpa", "Traditional Swedish instrument makers", "14th century onward", "Sweden", "A keyed fiddle unique to Swedish folk music, combining bowed strings with a keyboard mechanism."),
    ("Uilleann Pipes", "Uilleann pipes", "Traditional Irish instrument makers", "18th century onward", "Ireland", "A bellows-blown bagpipe regarded as one of the most complex and expressive forms of bagpipe in the world."),
    ("Duduk", "Duduk", "Traditional Armenian instrument makers", "over 1,500 years old tradition", "Armenia", "A double-reed woodwind instrument with a haunting, mournful tone, central to Armenian folk music."),
    ("Oud", "Oud", "Traditional Middle Eastern instrument makers", "centuries-old tradition", "Middle East", "A pear-shaped fretless plucked lute that is a foundational instrument of Arab, Persian, and Turkish classical music."),
    ("Qanun", "Qanun (instrument)", "Traditional Middle Eastern instrument makers", "centuries-old tradition", "Middle East", "A large plucked zither with dozens of strings, widely used in Arab, Turkish, and Persian classical music."),
    ("Wanamaker Organ", "Wanamaker Organ", "Los Angeles Art Organ Company", "1904 (built); installed 1911", "United States", "The largest fully functioning pipe organ in the world, housed in the Wanamaker Building in Philadelphia."),
    ("Boardwalk Hall Auditorium Organ", "Boardwalk Hall Auditorium Organ", "Midmer-Losh Organ Company", "1929-1932", "United States", "The largest pipe organ ever constructed, built for the Atlantic City Convention Hall."),
    ("Marimba", "Marimba", "Traditional Mesoamerican/African instrument makers", "centuries-old tradition", "Guatemala/Mexico", "A wooden percussion keyboard instrument with resonators, considered a national instrument of Guatemala."),
]
CATEGORY_ASSIGNMENTS.append((MORE_INSTRUMENTS_BATCH2, "instrument"))

# Real, individually famous historic photographs that shaped visual culture,
# journalism, science, and public memory.
MORE_PHOTOGRAPHS_BATCH2: list[tuple] = [
    ("View from the Window at Le Gras", "View from the Window at Le Gras", "Nicéphore Niépce", "c. 1826-1827", "France", "Widely regarded as the oldest surviving photograph made in a camera."),
    ("Migrant Mother", "Migrant Mother", "Dorothea Lange", "1936", "United States", "An iconic Depression-era portrait of a destitute pea-picker mother that became a symbol of Farm Security Administration documentary photography."),
    ("Raising the Flag on Iwo Jima", "Raising the Flag on Iwo Jima", "Joe Rosenthal", "1945", "United States", "Depicts US Marines raising the American flag atop Mount Suribachi during the Battle of Iwo Jima, one of the most reproduced photographs in history."),
    ("Tank Man", "Tank Man", "Jeff Widener", "1989", "China", "Shows an unidentified man standing before a column of tanks after the Tiananmen Square protests, an enduring symbol of civil resistance."),
    ("Earthrise", "Earthrise", "William Anders (NASA, Apollo 8)", "1968", "Moon orbit/Earth", "The first photograph of Earth rising over the lunar horizon taken by a human, credited with shifting global environmental consciousness."),
    ("The Blue Marble", "The Blue Marble", "NASA (Apollo 17 crew)", "1972", "Earth/space", "One of the most widely distributed photographs in history, showing a fully illuminated Earth from space."),
    ("V-J Day in Times Square", "V-J Day in Times Square", "Alfred Eisenstaedt", "1945", "United States", "Captures a sailor kissing a woman in Times Square upon the announcement of Japan's surrender ending World War II."),
    ("Napalm Girl", "Napalm Girl", "Nick Ut", "1972", "Vietnam", "Depicts children fleeing a napalm attack during the Vietnam War and became one of the defining images of the conflict."),
    ("Guerrillero Heroico", "Guerrillero Heroico", "Alberto Korda", "1960", "Cuba", "A portrait of Che Guevara that has become one of the most reproduced images in photographic history."),
    ("Lunch atop a Skyscraper", "Lunch atop a Skyscraper", "Charles C. Ebbets (attributed)", "1932", "United States", "Shows ironworkers eating lunch on a girder high above Manhattan during construction of Rockefeller Center."),
    ("The Falling Man", "The Falling Man", "Richard Drew", "2001", "United States", "Depicts a man falling from the World Trade Center during the September 11 attacks, one of the most controversial news photographs ever published."),
    ("The Tetons and the Snake River", "The Tetons and the Snake River", "Ansel Adams", "1942", "United States", "A celebrated black-and-white landscape of Grand Teton National Park, among Adams's most reproduced works."),
    ("Moonrise, Hernandez, New Mexico", "Moonrise, Hernandez, New Mexico", "Ansel Adams", "1941", "United States", "A dramatic photograph of moonrise over a small New Mexico village, one of the best-known images in landscape photography."),
    ("Pillars of Creation", "Pillars of Creation", "NASA/ESA (Hubble Space Telescope)", "1995", "Eagle Nebula/space", "An iconic image of star-forming gas columns in the Eagle Nebula, among the most famous astronomical photographs ever taken."),
    ("Pale Blue Dot", "Pale Blue Dot", "NASA (Voyager 1)", "1990", "Deep space", "A photograph of Earth as a tiny point of light taken from roughly 6 billion kilometers away, inspiring Carl Sagan's famous reflection."),
    ("Dalí Atomicus", "Dalí Atomicus", "Philippe Halsman", "1948", "United States", "A meticulously staged photograph of Salvador Dalí, cats, water, and furniture suspended mid-air."),
    ("The Steerage", "The Steerage", "Alfred Stieglitz", "1907", "United States", "A landmark modernist photograph of steerage-class passengers aboard an ocean liner, celebrated for its formal composition."),
    ("Bloody Saturday", "Bloody Saturday", "H. S. Wong", "1937", "China", "A harrowing image of an injured infant in the bombed ruins of Shanghai's South railway station during the Second Sino-Japanese War."),
    ("The Vulture and the Little Girl", "The Vulture and the Little Girl", "Kevin Carter", "1993", "Sudan", "A Pulitzer Prize-winning and deeply controversial photograph of a starving child during the Sudan famine."),
    ("The Falling Soldier", "The Falling Soldier", "Robert Capa", "1936", "Spain", "A widely debated Spanish Civil War photograph purporting to show a Republican militiaman at the moment of death."),
    ("The Magnificent Eleven", "The Magnificent Eleven", "Robert Capa", "1944", "France", "The small surviving set of photographs Capa took under fire during the D-Day landings at Omaha Beach."),
    ("Situation Room Photograph", "Situation Room (photograph)", "Pete Souza", "2011", "United States", "Depicts President Obama and senior officials watching the raid that killed Osama bin Laden."),
    ("Self-immolation of Thích Quảng Đức", "Self-immolation of Thích Quảng Đức", "Malcolm Browne", "1963", "Vietnam", "Documents the Buddhist monk's public self-immolation in protest of the South Vietnamese government's policies."),
    ("Surgeon's Photograph", "Surgeon's Photograph", "Robert Kenneth Wilson (attributed)", "1934", "Scotland", "The best-known purported image of the Loch Ness Monster, later revealed to be a hoax."),
    ("Einstein Sticking Out His Tongue", "Einstein sticking out his tongue", "Arthur Sasse", "1951", "United States", "A candid photograph of Albert Einstein taken on his 72nd birthday that became one of the most famous images of the 20th century."),
    ("Home of a Rebel Sharpshooter", "Home of a Rebel Sharpshooter", "Alexander Gardner", "1863", "United States", "A staged Civil War battlefield photograph from Gettysburg, among the earliest examples of photographic manipulation."),
    ("Sallie Gardner at a Gallop", "Sallie Gardner at a Gallop", "Eadweard Muybridge", "1878", "United States", "A sequential motion study proving that a galloping horse briefly has all four hooves off the ground, a foundational work in motion photography."),
    ("Boston, as the Eagle and the Wild Goose See It", "Boston, as the Eagle and the Wild Goose See It", "James Wallace Black", "1860", "United States", "The oldest surviving aerial photograph, taken from a hot air balloon over Boston."),
    ("Photo 51", "Photo 51", "Rosalind Franklin and Raymond Gosling", "1952", "United Kingdom", "An X-ray diffraction image of DNA that was crucial evidence in determining the double helix structure."),
    ("Afghan Girl", "Afghan Girl", "Steve McCurry", "1984", "Afghanistan", "A National Geographic cover portrait of a young Afghan refugee, one of the most recognized photographs in the magazine's history."),
    ("Raising a Flag over the Reichstag", "Raising a Flag over the Reichstag", "Yevgeny Khaldei", "1945", "Germany", "A staged Soviet photograph symbolizing the fall of Berlin at the end of World War II in Europe."),
    ("Fire Escape Collapse", "Fire Escape Collapse", "Stanley Forman", "1975", "United States", "A Pulitzer Prize-winning photograph capturing a fire escape collapse in Boston, credited with prompting changes to fire safety codes."),
    ("Saigon Execution", "Saigon Execution", "Eddie Adams", "1968", "Vietnam", "Depicts the summary execution of a Viet Cong prisoner during the Tet Offensive, a defining image of the Vietnam War."),
    ("Le Baiser de l'Hôtel de Ville", "Le Baiser de l'Hôtel de Ville", "Robert Doisneau", "1950", "France", "A widely reproduced photograph of a couple kissing on a Paris street, later revealed to have been staged."),
    ("Behind the Gare Saint-Lazare", "Behind the Gare Saint-Lazare", "Henri Cartier-Bresson", "1932", "France", "A defining example of Cartier-Bresson's 'decisive moment' aesthetic, showing a man leaping over a puddle."),
    ("Le Violon d'Ingres", "Le Violon d'Ingres", "Man Ray", "1924", "France", "A Surrealist photograph of model Kiki de Montparnasse's back altered to resemble a violin."),
    ("Eddington Eclipse Photograph", "Eddington experiment", "Arthur Eddington", "1919", "Príncipe", "Photographic plates of a solar eclipse that provided early observational confirmation of Einstein's general theory of relativity."),
    ("Boulevard du Temple", "Boulevard du Temple", "Louis Daguerre", "1838", "France", "The earliest surviving photograph to include a human being, captured by chance on a busy Paris boulevard."),
    ("Cottingley Fairies", "Cottingley Fairies", "Elsie Wright and Frances Griffiths", "1917", "United Kingdom", "A series of staged photographs purporting to show fairies, later admitted to be faked, that fooled Arthur Conan Doyle."),
    ("Gordon, the Scourged Back", "Gordon (enslaved man)", "McPherson & Oliver (studio)", "1863", "United States", "A widely circulated photograph of a formerly enslaved man's severely scarred back that galvanized abolitionist sentiment."),
    ("First Image of a Black Hole", "M87*", "Event Horizon Telescope Collaboration", "2019", "International (Earth-based telescope array)", "The first-ever direct image of a black hole and its shadow, of the supermassive black hole at the center of galaxy M87."),
    ("Hindenburg Disaster Photograph", "Hindenburg disaster", "Sam Shere", "1937", "United States", "Documents the catastrophic burning of the German airship Hindenburg while attempting to dock in New Jersey."),
    ("Kent State Shootings Photograph", "Kent State shootings", "John Filo", "1970", "United States", "A Pulitzer Prize-winning photograph of a young woman kneeling over a student killed by Ohio National Guard gunfire."),
    ("The Roaring Lion", "The Roaring Lion", "Yousuf Karsh", "1941", "Canada", "A defiant portrait of Winston Churchill taken moments after Karsh removed the prime minister's cigar, among the most reproduced portraits ever made."),
    ("Dewey Defeats Truman", "Dewey Defeats Truman", "Byron Rollins (Associated Press)", "1948", "United States", "Shows a jubilant Harry Truman holding a newspaper that erroneously declared his election defeat."),
    ("East and West Shaking Hands", "East and West Shaking Hands at Laying of Last Rail, Union Pacific Railroad", "Andrew J. Russell", "1869", "United States", "Documents the ceremonial completion of America's first transcontinental railroad at Promontory Summit, Utah."),
    ("Trinity Test Photograph", "Trinity (nuclear test)", "Berlyn Brixner (U.S. Army)", "1945", "United States", "Photographs of the world's first detonation of a nuclear weapon in the New Mexico desert."),
    ("First Photograph from the Surface of Mars", "Viking 1", "NASA", "1976", "Mars", "Captured the first photograph ever taken from the surface of another planet."),
    ("Dovima with Elephants", "Dovima with Elephants", "Richard Avedon", "1955", "France", "A striking high-fashion photograph juxtaposing a model in a Dior gown with circus elephants."),
    ("American Gothic Photograph", "American Gothic (photograph)", "Gordon Parks", "1942", "United States", "A portrait of government cleaning woman Ella Watson posed before an American flag, echoing Grant Wood's painting to comment on racial inequality."),
    ("Earth from the Moon (Lunar Orbiter 1)", "Lunar Orbiter 1", "NASA", "1966", "Moon orbit/Earth", "Captured the first photograph of Earth taken from the vicinity of the Moon."),
    ("The Critic", "The Critic (photograph)", "Weegee", "1943", "United States", "A staged tabloid photograph contrasting a disheveled onlooker with wealthy opera patrons arriving at the Metropolitan Opera."),
    ("A Harvest of Death", "A Harvest of Death", "Timothy H. O'Sullivan", "1863", "United States", "A stark photograph of Confederate dead at Gettysburg, among the first images to bring the human cost of war to the American public."),
    ("Rosa Parks Police Booking Photograph", "Rosa Parks", "Montgomery Police Department", "1956", "United States", "The police booking photograph taken after Rosa Parks's arrest, which became an enduring image of the Civil Rights Movement."),
    ("Robert Cornelius Self-Portrait", "Robert Cornelius", "Robert Cornelius", "1839", "United States", "A self-portrait daguerreotype widely regarded as the earliest surviving photographic portrait of a person."),
    ("Endurance Trapped in Antarctic Ice", "Endurance (1912 ship)", "Frank Hurley", "1915", "Antarctica", "Frank Hurley's photographs of Ernest Shackleton's ship trapped in Antarctic pack ice are among the most celebrated images of the Heroic Age of exploration."),
    ("1927 Solvay Conference Photograph", "1927 Solvay Conference", "Benjamin Couprie", "1927", "Belgium", "A group photograph of the world's leading physicists, including Einstein, Curie, and Bohr, at the fifth Solvay Conference."),
    ("Robert F. Kennedy Assassination Photograph", "Assassination of Robert F. Kennedy", "Boris Yaro", "1968", "United States", "A photograph taken moments after Kennedy was shot at the Ambassador Hotel in Los Angeles."),
    ("USS Arizona Attack Photograph", "USS Arizona", "United States Navy", "1941", "United States", "Photographs of USS Arizona exploding during the attack on Pearl Harbor became defining images of America's entry into World War II."),
    ("The Last Sitting", "The Last Sitting", "Bert Stern", "1962", "United States", "A famous photo series of Marilyn Monroe taken six weeks before her death, published posthumously."),
]
CATEGORY_ASSIGNMENTS.append((MORE_PHOTOGRAPHS_BATCH2, "photograph"))

# Real, individually famous historic textiles, costumes, and tapestries from
# cultures around the world.
MORE_TEXTILES_BATCH2: list[tuple] = [
    ("Bayeux Tapestry", "Bayeux Tapestry", "Unknown (Anglo-Norman)", "c. 1070s", "France/England", "An embroidered narrative chronicling the Norman conquest of England, over 70 meters long."),
    ("The Unicorn Tapestries", "The Hunt of the Unicorn", "Unknown (South Netherlandish)", "c. 1495-1505", "Belgium/Netherlands", "A set of seven tapestries depicting a mythical hunt for a unicorn, rich in medieval symbolism."),
    ("The Lady and the Unicorn", "The Lady and the Unicorn", "Unknown", "late 15th century", "France", "A set of six tapestries, five representing the senses and the sixth inscribed 'À mon seul désir'."),
    ("Overlord Embroidery", "Overlord Embroidery", "Royal School of Needlework", "1968-1974", "United Kingdom", "A modern 34-panel embroidery depicting the planning and execution of the D-Day invasion."),
    ("Apocalypse Tapestry", "Apocalypse Tapestry", "Nicolas Bataille workshop (design by Jean Bondol)", "1377-1382", "France", "A monumental medieval tapestry cycle depicting the Book of Revelation, among the largest surviving medieval tapestries."),
    ("Girona Tapestry", "Girona Tapestry", "Unknown", "c. 11th-12th century", "Spain", "A Romanesque embroidered hanging depicting the biblical story of Creation."),
    ("Ardabil Carpet", "Ardabil Carpet", "Maqsud Kashani", "1539-1540", "Iran", "One of the world's largest and most celebrated Persian carpets, woven for a Safavid shrine."),
    ("Pazyryk Carpet", "Pazyryk Carpet", "Unknown (Scythian)", "c. 5th century BCE", "Russia (Siberia)", "The oldest known surviving pile carpet, preserved in permafrost in a Scythian burial mound."),
    ("Mantle of Roger II", "Mantle of Roger II", "Arab-Norman court workshop, Palermo", "1133-1134", "Sicily (Italy)", "A richly embroidered silk coronation mantle later used in Holy Roman Empire coronation ceremonies."),
    ("Star-Spangled Banner", "Star-Spangled Banner (flag)", "Mary Pickersgill", "1813", "United States", "The garrison flag that flew over Fort McHenry and inspired the United States national anthem."),
    ("Kente Cloth", "Kente cloth", "Ashanti weavers", "centuries-old tradition", "Ghana", "A brightly patterned strip-woven cloth historically associated with Akan royalty and ceremony."),
    ("Huipil", "Huipil", "Maya weavers", "centuries-old tradition", "Guatemala", "A traditional woven blouse worn by indigenous women of Guatemala and southern Mexico, patterned with symbolic motifs."),
    ("Kimono", "Kimono", "Japanese weavers and tailors", "Edo period onward", "Japan", "A traditional T-shaped Japanese garment, historically woven and dyed with elaborate seasonal motifs."),
    ("Quipu", "Quipu", "Inca artisans", "c. 15th-16th century", "Peru", "A knotted cord device used by the Inca Empire to record numerical and administrative information."),
    ("Paracas Textiles", "Paracas culture", "Paracas culture", "c. 500 BCE-200 CE", "Peru", "Elaborately embroidered mantles from ancient Peru, prized for their vivid colors and complex iconography."),
    ("Fayum Mummy Portraits", "Fayum mummy portraits", "Unknown Romano-Egyptian painters", "1st-3rd century CE", "Egypt", "Naturalistic painted portraits attached to mummy wrappings, blending Egyptian funerary tradition with Roman portraiture."),
    ("Shroud of Turin", "Shroud of Turin", "Unknown", "medieval (radiocarbon dated c. 1260-1390)", "Italy", "A linen cloth bearing the faint image of a man, venerated by many as the burial shroud of Jesus Christ."),
    ("Ottoman Imperial Kaftan", "Kaftan", "Ottoman court workshops", "16th-17th century", "Turkey", "Richly patterned silk and metallic-thread robes worn by Ottoman sultans, preserved in the Topkapi Palace collection."),
    ("Coptic Textiles", "Coptic textiles", "Unknown Coptic weavers", "3rd-9th century CE", "Egypt", "Woven and embroidered textiles from early Christian Egypt, prized for their preservation in the dry desert climate."),
    ("Hawaiian Feather Cloak", "ʻAhuʻula", "Native Hawaiian featherworkers", "18th century", "Hawaii, United States", "A ceremonial feather cloak worn by Hawaiian aliʻi (chiefs), made from tens of thousands of individually tied feathers."),
    ("Navajo Chief's Blanket", "Navajo weaving", "Navajo weavers", "19th century", "United States", "Highly prized handwoven wool blankets whose bold geometric patterns became iconic of Navajo textile artistry."),
    ("Kashmir Shawl", "Kashmir shawl", "Kashmiri weavers", "18th-19th century", "India", "Intricately woven pashmina shawls prized across Mughal, Persian, and European courts for their fine wool and detailed paisley patterns."),
    ("Sogdian Silk Textile", "Silk Road", "Sogdian weavers", "7th-8th century CE", "Central Asia", "Richly patterned silk textiles woven by Sogdian merchants and traded extensively along the Silk Road."),
    ("Chilkat Blanket", "Chilkat weaving", "Tlingit weavers", "19th century", "United States/Canada", "A ceremonial woven blanket of the Tlingit people, woven from mountain goat wool and cedar bark in complex formline designs."),
    ("Dalmatic of Charlemagne", "Dalmatic of Charlemagne", "Byzantine or Italian court workshop", "c. 14th-15th century", "Vatican City/Italy", "An ornate liturgical vestment traditionally associated with Charlemagne, embroidered with scenes of Christ in Majesty."),
    ("Chinese Imperial Dragon Robe", "Dragon robe", "Qing court workshops", "18th-19th century", "China", "Richly embroidered silk ceremonial robes bearing imperial dragon motifs, worn by Qing dynasty emperors and nobility."),
    ("Wari Feathered Tunic", "Wari culture", "Wari culture", "c. 600-1000 CE", "Peru", "A tunic covered in thousands of brightly colored feathers, demonstrating the sophisticated textile artistry of the Wari Empire."),
    ("Karaori Noh Robe", "Karaori", "Japanese weavers", "Edo period", "Japan", "An elaborate brocade robe worn by actors in Japanese Noh theater, woven with raised, embroidery-like patterns."),
    ("Napoleon's Coronation Robe", "Coronation of Napoleon I", "Designed by Jean-Baptiste Isabey", "1804", "France", "The richly embroidered velvet and ermine ceremonial robe worn by Napoleon Bonaparte at his imperial coronation."),
    ("Devonshire Hunting Tapestries", "Devonshire Hunting Tapestries", "Unknown (Flemish)", "c. 1425-1450", "Belgium", "A set of large medieval tapestries depicting scenes of falconry, otter hunting, and boar and bear hunting."),
    ("Mawangdui Silk Funeral Banner", "Mawangdui Han tombs", "Unknown", "2nd century BCE", "China", "A painted silk funeral banner from the Mawangdui tombs depicting the journey of the deceased into the afterlife."),
    ("Penacho de Moctezuma", "Penacho de Moctezuma", "Aztec featherworkers", "early 16th century", "Mexico", "An elaborate feather headdress traditionally associated with the Aztec emperor Moctezuma II, now preserved in Vienna."),
    ("Syon Cope", "Syon Cope", "English embroiderers (opus anglicanum)", "c. 1300-1320", "England", "A celebrated example of English medieval ecclesiastical embroidery known as opus anglicanum."),
    ("Shroud of Saint-Josse", "Shroud of Saint-Josse", "Khorasan workshop", "961 CE", "Iran", "A luxurious Persian silk textile that once wrapped the relics of Saint Josse in northern France."),
    ("Coronation Robe of Elizabeth II", "Coronation of Elizabeth II", "Norman Hartnell", "1953", "United Kingdom", "The richly embroidered gown worn by Queen Elizabeth II at her coronation, incorporating floral emblems of the Commonwealth."),
    ("Aso Oke", "Aso oke", "Yoruba weavers", "centuries-old tradition", "Nigeria", "A hand-woven cloth strip textile traditionally worn by the Yoruba people for ceremonial occasions."),
    ("Ikat Textile", "Ikat", "Various Southeast and Central Asian weavers", "centuries-old tradition", "Indonesia/Central Asia", "A resist-dyeing technique that produces distinctively blurred, patterned textiles across many world cultures."),
    ("Toile de Jouy", "Toile de Jouy", "Christophe-Philippe Oberkampf", "18th century", "France", "A distinctive printed cotton textile pattern featuring pastoral scenes that became a hallmark of French decorative arts."),
    ("Opus Anglicanum Vestments", "Opus anglicanum", "English embroiderers", "12th-15th century", "England", "A refined style of English needlework embroidery, prized across medieval Europe for ecclesiastical vestments."),
    ("Adire Cloth", "Adire (textile art)", "Yoruba dyers", "centuries-old tradition", "Nigeria", "A resist-dyed indigo cloth traditionally produced by Yoruba women using tied, stitched, or starch-resist patterns."),
]
CATEGORY_ASSIGNMENTS.append((MORE_TEXTILES_BATCH2, "textile"))

# Real, individually famous historic coins, currency, and seals from
# antiquity through the modern era.
MORE_COINS_BATCH2: list[tuple] = [
    ("Lydian Lion", "Lydian Lion", "Unknown (Kingdom of Lydia)", "c. 600 BCE", "Turkey (Lydia)", "An early electrum coin widely regarded as among the very first coins ever minted."),
    ("Athenian Owl Tetradrachm", "Athenian tetradrachm", "Unknown (Athens mint)", "c. 5th century BCE", "Greece", "A silver coin bearing the owl of Athena that became the dominant trade currency of the ancient Mediterranean."),
    ("Aureus of Julius Caesar", "Aureus", "Roman mint", "44 BCE", "Italy (Roman Republic)", "A gold coin type used by Julius Caesar, among the earliest Roman coins to bear the portrait of a living individual."),
    ("Brasher Doubloon", "Brasher Doubloon", "Ephraim Brasher", "1787", "United States", "A privately minted gold coin by New York goldsmith Ephraim Brasher, among the most valuable coins in American numismatics."),
    ("Byzantine Solidus", "Solidus (coin)", "Byzantine mint", "4th-15th century CE", "Byzantine Empire", "A stable, high-purity gold coin that served as the standard currency of the Byzantine Empire for centuries."),
    ("Ban Liang", "Ban Liang", "Chinese mint (Qin dynasty)", "3rd century BCE", "China", "A round bronze coin with a square hole, standardized under Qin Shi Huang and a template for Chinese coinage for two millennia."),
    ("Spanish Dollar", "Spanish dollar", "Spanish Royal Mint", "16th-19th century", "Spain", "A silver coin, also known as 'pieces of eight,' that became a global trade currency across empires and continents."),
    ("Rai Stones", "Rai stones", "Yapese carvers", "centuries-old tradition", "Yap (Micronesia)", "Large carved limestone discs used as a traditional form of currency on the island of Yap."),
    ("1804 Draped Bust Dollar", "1804 dollar", "United States Mint", "1834 (struck, dated 1804)", "United States", "One of the rarest and most celebrated coins in American numismatics, known as 'the King of American Coins'."),
    ("1933 Double Eagle", "1933 Double Eagle", "United States Mint", "1933", "United States", "A gold coin never officially released for circulation that became the most valuable coin ever sold at auction."),
    ("1943 Copper Cent", "1943 copper cent", "United States Mint", "1943", "United States", "An extremely rare minting error in which a small number of pennies were accidentally struck in copper instead of wartime steel."),
    ("Flowing Hair Dollar", "Flowing Hair dollar", "United States Mint", "1794", "United States", "The first silver dollar coin issued by the United States federal government."),
    ("Eid Mar Denarius", "Eid Mar", "Roman mint (issued by Brutus)", "42 BCE", "Roman Republic", "A silver coin commemorating the assassination of Julius Caesar, among the most historically significant ancient coins."),
    ("Persian Daric", "Daric", "Achaemenid mint", "5th century BCE", "Iran (Persia)", "A gold coin depicting an archer king, minted by the Achaemenid Empire as a standard of trade."),
    ("Gold Stater of Alexander the Great", "Stater", "Macedonian mint", "4th century BCE", "Greece", "A gold coin type minted under Alexander the Great, widely circulated across his vast empire."),
    ("Roman Denarius", "Denarius", "Roman mint", "3rd century BCE-3rd century CE", "Italy (Rome)", "The standard silver coin of ancient Rome for over four centuries, minted in the names of successive emperors."),
    ("Continental Currency Dollar Coin", "Continental Currency dollar coin", "Continental Congress", "1776", "United States", "An early pattern coin produced during the American Revolution, among the first coins associated with the United States."),
    ("Fugio Cent", "Fugio cent", "United States (first federally authorized coin)", "1787", "United States", "The first coin officially authorized by the United States government, reputedly designed with input from Benjamin Franklin."),
    ("Great Seal of the United States", "Great Seal of the United States", "Charles Thomson (design)", "1782", "United States", "The official emblem used to authenticate certain documents issued by the United States federal government."),
    ("Indo-Greek Coinage", "Indo-Greek Kingdom", "Indo-Greek kings", "c. 2nd century BCE", "Afghanistan/Pakistan", "Bilingual coins blending Greek and Indian artistic traditions, minted by the Hellenistic rulers of ancient Bactria and northwest India."),
    ("Chinese Knife Money", "Knife money", "Zhou dynasty mints", "c. 6th-3rd century BCE", "China", "A distinctive knife-shaped bronze currency used in ancient China before the standardization of round coins."),
    ("Chinese Spade Money", "Spade money", "Zhou dynasty mints", "c. 6th-3rd century BCE", "China", "A spade-shaped bronze currency used in ancient China, reflecting the agricultural tool it was modeled after."),
    ("Umayyad Gold Dinar", "Dinar", "Umayyad mint", "696-697 CE", "Syria (Middle East)", "An early Islamic gold coin that established the epigraphic style, replacing figural imagery with Qur'anic inscriptions."),
    ("Venetian Ducat", "Ducat", "Republic of Venice mint", "1284 onward", "Italy", "A gold coin of remarkably stable purity that became a dominant international trade currency for centuries."),
    ("Florentine Florin", "Florin", "Republic of Florence mint", "1252 onward", "Italy", "A gold coin that became one of medieval Europe's most widely trusted and imitated currencies."),
    ("English Noble", "Noble (English coin)", "English Royal Mint", "1344 onward", "England", "A gold coin depicting the king standing in a ship, commemorating English naval power."),
    ("Maria Theresa Thaler", "Maria Theresa thaler", "Austrian mint", "1741 onward", "Austria", "A silver trade coin so trusted that it continued to be minted with the same date long after Maria Theresa's death, circulating widely in Africa and the Middle East."),
    ("Doubloon", "Doubloon", "Spanish colonial mints", "16th-19th century", "Spain", "A Spanish gold coin widely associated with pirate treasure and colonial-era trade across the Americas."),
    ("Great Seal of the Realm", "Great Seal of the Realm", "English Crown workshop", "medieval origin, renewed each reign", "England", "The official seal used to symbolize the sovereign's approval of important state documents in England."),
    ("Egyptian Scarab Seal", "Scarab (artifact)", "Unknown Egyptian craftsmen", "c. 2000-1000 BCE", "Egypt", "Small carved amulets and seals in the shape of a scarab beetle, widely used in ancient Egypt for protection and administration."),
    ("Mesopotamian Cylinder Seal", "Cylinder seal", "Unknown Mesopotamian craftsmen", "c. 3rd millennium BCE", "Iraq (Mesopotamia)", "A small engraved stone cylinder rolled across clay to leave an authenticating impression, used across the ancient Near East."),
    ("Bar Kokhba Revolt Coinage", "Bar Kokhba revolt coinage", "Jewish rebel authorities", "132-135 CE", "Judea (Israel)", "Coins struck by Jewish rebels during the Bar Kokhba revolt against Rome, often overstruck on existing Roman coins."),
    ("Tyrian Shekel", "Tyrian shekel", "Tyre mint", "1st century BCE-1st century CE", "Middle East (Tyre/Judea)", "A high-purity silver coin required for payment of the Jerusalem Temple tax, traditionally identified as the biblical '30 pieces of silver'."),
    ("Wampum", "Wampum", "Native American (Algonquian/Iroquois) artisans", "centuries-old tradition", "North America", "Cylindrical shell beads used by Indigenous peoples of the Northeast for currency, ceremony, and diplomatic record-keeping."),
    ("Anglo-Saxon Sceat", "Sceat", "Anglo-Saxon mints", "c. 7th-8th century CE", "England", "A small silver coin that formed the principal currency of early Anglo-Saxon England before the introduction of the penny."),
    ("Offa's Dinar", "Offa's dinar", "Kingdom of Mercia (imitating an Abbasid dinar)", "774 CE", "England", "A gold coin struck by the Anglo-Saxon King Offa of Mercia in direct imitation of contemporary Abbasid Islamic coinage."),
    ("Croeseid", "Croeseid", "Kingdom of Lydia (under Croesus)", "561-546 BCE", "Turkey (Lydia)", "A bimetallic gold and silver coinage introduced by King Croesus, refining the earlier Lydian Lion coinage."),
    ("Widow's Mite", "Lepton (coin)", "Hasmonean/Herodian mint", "1st century BCE-1st century CE", "Judea (Israel)", "A small bronze coin of low value, traditionally identified as the 'widow's mite' referenced in the biblical Gospels."),
    ("US Trade Dollar", "Trade dollar (United States coin)", "United States Mint", "1873-1885", "United States", "A silver dollar coin minted specifically for use in trade with East Asia."),
    ("Persian Siglos", "Siglos", "Achaemenid mint", "5th century BCE", "Iran (Persia)", "A silver coin depicting an archer king, minted as the standard silver denomination of the Achaemenid Persian Empire."),
]
CATEGORY_ASSIGNMENTS.append((MORE_COINS_BATCH2, "coin"))

# 200 real, individually famous natural history specimens and objects held
# in real museums -- named dinosaur/fossil skeletons, hominin fossils,
# meteorites, gems and mineral specimens, taxidermy icons, Ice Age mummies,
# and extinct-species specimens. This is a brand-new category not previously
# represented in the "World Heritage Treasures" gallery.
NATURAL_HISTORY_BATCH2: list[tuple] = [
    # --- Famous dinosaur and prehistoric reptile specimens ---
    ("Sue the T. rex", "Sue (dinosaur)", "Tyrannosaurus rex", "~67 million years ago (discovered 1990)", "United States (South Dakota)", "The largest and most complete Tyrannosaurus rex skeleton ever found, now the centerpiece of Chicago's Field Museum."),
    ("Stan the T. rex", "Stan (dinosaur)", "Tyrannosaurus rex", "~67 million years ago (discovered 1987)", "United States (South Dakota)", "One of the most complete Tyrannosaurus rex skeletons known, extensively cast and replicated for museums worldwide."),
    ("Scotty the T. rex", "Scotty (dinosaur)", "Tyrannosaurus rex", "~66 million years ago (discovered 1991)", "Canada (Saskatchewan)", "Estimated to be the largest Tyrannosaurus rex by body mass yet found, housed at the Royal Saskatchewan Museum."),
    ("Wankel Rex (Nation's T. rex)", "Wankel Rex", "Tyrannosaurus rex", "~66-67 million years ago (discovered 1988)", "United States (Montana)", "A nearly complete Tyrannosaurus rex skeleton found by rancher Kathy Wankel, now on display at the Smithsonian National Museum of Natural History."),
    ("Trix the T. rex", "Trix (Tyrannosaurus)", "Tyrannosaurus rex", "~67 million years ago (discovered 2013)", "United States (Montana)", "A well-preserved elderly Tyrannosaurus rex specimen, the first T. rex skeleton on permanent display in mainland Europe, at Naturalis Biodiversity Center."),
    ("Dippy the Diplodocus", "Dippy (dinosaur)", "Diplodocus carnegii", "~150 million years ago (cast unveiled 1905)", "United States (Wyoming, original specimen)", "A cast of a Diplodocus skeleton donated by Andrew Carnegie that toured the world's museums and became one of the most famous dinosaur displays ever exhibited."),
    ("Sophie the Stegosaurus", "Sophie (dinosaur)", "Stegosaurus stenops", "~150 million years ago (discovered 2003)", "United States (Wyoming)", "The most complete Stegosaurus skeleton ever found, mounted at the Natural History Museum, London."),
    ("Big Al the Allosaurus", "Big Al (dinosaur)", "Allosaurus fragilis", "~150 million years ago (discovered 1991)", "United States (Wyoming)", "An unusually complete, mostly articulated young Allosaurus skeleton bearing signs of numerous healed injuries, studied by the Museum of the Rockies."),
    ("Leonardo the Brachylophosaurus", "Leonardo (dinosaur)", "Brachylophosaurus canadensis", "~77 million years ago (discovered 2000)", "United States (Montana)", "An exceptionally well-preserved 'dinosaur mummy' with fossilized skin, muscle tissue, and stomach contents, housed at the Great Plains Dinosaur Museum."),
    ("Dueling Dinosaurs Fossil", "Dueling Dinosaurs", "Tyrannosaurus and Triceratops", "~67 million years ago (discovered 2006)", "United States (Montana)", "A remarkably complete pair of skeletons of a Tyrannosaurus and a Triceratops preserved together as though locked in combat."),
    ("Zuul the Ankylosaur", "Zuul (dinosaur)", "Zuul crurivastator", "~75 million years ago (discovered 2014)", "Canada (Montana border region)", "An exceptionally well-preserved armored dinosaur skeleton with fossilized skin and osteoderms intact, held at the Royal Ontario Museum."),
    ("Berlin Specimen of Archaeopteryx", "Archaeopteryx", "Archaeopteryx lithographica", "~150 million years ago (discovered 1874-1876)", "Germany (Solnhofen limestone)", "The most complete and famous of the Archaeopteryx fossils, a crucial transitional form between dinosaurs and birds, held at the Museum für Naturkunde Berlin."),
    ("Giraffatitan Mounted Skeleton", "Giraffatitan", "Giraffatitan brancai", "~150 million years ago (excavated 1909-1913)", "Tanzania", "The tallest mounted dinosaur skeleton in the world, assembled from bones excavated at Tendaguru and displayed at the Museum für Naturkunde Berlin."),
    ("Barosaurus Rearing Mount", "Barosaurus", "Barosaurus lentus", "~150 million years ago (mount installed 1991)", "United States (South Dakota, original specimen)", "A cast skeleton of a rearing Barosaurus defending its young from an Allosaurus, greeting visitors in the rotunda of the American Museum of Natural History."),
    ("Máximo the Titanosaur", "Patagotitan", "Patagotitan mayorum", "~101 million years ago (discovered 2010s)", "Argentina", "A cast skeleton of one of the largest land animals ever discovered, exhibited at Chicago's Field Museum under the nickname 'Máximo'."),
    ("Bernissart Iguanodon Skeletons", "Bernissart Iguanodons", "Iguanodon bernissartensis", "~125 million years ago (discovered 1878)", "Belgium", "A trove of over thirty nearly complete Iguanodon skeletons found in a coal mine, among the first dinosaur skeletons ever mounted upright."),
    ("Megalosaurus Jawbone", "Megalosaurus", "Megalosaurus bucklandii", "~166 million years ago (described 1824)", "United Kingdom (Oxfordshire)", "The lower jaw fragment that became the first dinosaur ever formally named and scientifically described, held at the Oxford University Museum of Natural History."),
    ("Hylaeosaurus Holotype", "Hylaeosaurus", "Hylaeosaurus armatus", "~136 million years ago (discovered 1832)", "United Kingdom (Sussex)", "One of the three original fossils on which Richard Owen founded the group Dinosauria in 1842, held at the Natural History Museum, London."),
    ("Elasmosaurus Holotype", "Elasmosaurus", "Elasmosaurus platyurus", "~80 million years ago (described 1868)", "United States (Kansas)", "A long-necked marine reptile fossil notorious for paleontologist Edward Drinker Cope's initial mistake of placing its skull on the tip of its tail, held at the Academy of Natural Sciences, Philadelphia."),
    ("Yale Apatosaurus Holotype", "Apatosaurus", "Apatosaurus ajax", "~150 million years ago (described 1877)", "United States (Colorado)", "The original skeletal material on which the genus Apatosaurus was named, held at the Yale Peabody Museum of Natural History."),
    ("Marsh's Triceratops Skull", "Triceratops", "Triceratops horridus", "~66-68 million years ago (described 1889)", "United States (Wyoming)", "Among the first Triceratops skulls ever described by paleontologist Othniel Charles Marsh, foundational to identifying the genus."),
    ("Compsognathus Holotype", "Compsognathus", "Compsognathus longipes", "~150 million years ago (described 1859)", "Germany (Solnhofen limestone)", "One of the smallest known non-avian dinosaurs, its finely preserved holotype is held at the Bavarian State Collection for Palaeontology."),
    ("Tiktaalik Fossil", "Tiktaalik", "Tiktaalik roseae", "~375 million years ago (discovered 2004)", "Canada (Ellesmere Island)", "A landmark fossil fish with limb-like fins that illuminated the evolutionary transition of vertebrates from water to land."),
    ("Mary Anning's Ichthyosaur", "Ichthyosaurus", "Ichthyosaurus communis", "~200 million years ago (discovered 1811)", "United Kingdom (Lyme Regis)", "The first complete ichthyosaur skeleton ever recognized by science, found by twelve-year-old fossil collector Mary Anning and her brother Joseph."),
    ("Mary Anning's Plesiosaur", "Plesiosaurus", "Plesiosaurus dolichodeirus", "~200 million years ago (discovered 1823)", "United Kingdom (Lyme Regis)", "The first complete plesiosaur skeleton ever found, unearthed by fossil hunter Mary Anning and central to early debates on extinction."),
    ("Spinosaurus Holotype (Lost)", "Spinosaurus", "Spinosaurus aegyptiacus", "~95-100 million years ago (described 1915, destroyed 1944)", "Egypt", "The original Spinosaurus fossils described by Ernst Stromer were destroyed in an Allied bombing raid on Munich during World War II, a landmark loss in paleontology."),

    # --- Famous hominin and early human fossils ---
    ("Lucy the Australopithecus", "Lucy (Australopithecus)", "Australopithecus afarensis", "~3.2 million years ago (discovered 1974)", "Ethiopia", "A roughly 40-percent-complete hominin skeleton whose discovery transformed understanding of early bipedal human ancestors."),
    ("Ardi the Ardipithecus", "Ardi", "Ardipithecus ramidus", "~4.4 million years ago (discovered 1994)", "Ethiopia", "One of the oldest and most complete hominin skeletons known, revealing an early stage of human evolution that predates Lucy."),
    ("Turkana Boy", "Turkana Boy", "Homo erectus", "~1.5 million years ago (discovered 1984)", "Kenya", "The most complete early human skeleton ever found, belonging to an adolescent Homo erectus male, held by the National Museums of Kenya."),
    ("Peking Man Fossils", "Peking Man", "Homo erectus pekinensis", "~750,000-200,000 years ago (discovered 1929)", "China", "A collection of Homo erectus fossils excavated at Zhoukoudian whose original bones vanished during World War II, leaving only casts and records."),
    ("Taung Child Skull", "Taung Child", "Australopithecus africanus", "~2.8 million years ago (discovered 1924)", "South Africa", "The type specimen of Australopithecus africanus and the first australopithecine ever found, identified by Raymond Dart."),
    ("Mrs. Ples Skull", "Mrs. Ples", "Australopithecus africanus", "~2.1-2.6 million years ago (discovered 1947)", "South Africa", "One of the most complete australopithecine skulls ever found, unearthed at the Sterkfontein Caves."),
    ("Little Foot Skeleton", "Little Foot", "Australopithecus prometheus", "~3.67 million years ago (discovered 1994-1997)", "South Africa", "One of the oldest and most complete australopithecine skeletons ever found, recovered piece by piece from the Sterkfontein Caves."),
    ("Cheddar Man Skeleton", "Cheddar Man", "Homo sapiens", "~10,000 years ago (discovered 1903)", "United Kingdom (Somerset)", "Britain's oldest nearly complete human skeleton, whose DNA revealed that Mesolithic Britons likely had dark skin and blue eyes."),
    ("Old Man of La Chapelle", "Old Man of La Chapelle", "Homo neanderthalensis", "~50,000-60,000 years ago (discovered 1908)", "France", "A near-complete Neanderthal skeleton whose (later disputed) reconstruction as hunched and primitive shaped a century of public imagination about Neanderthals."),
    ("Homo floresiensis Type Skeleton", "Homo floresiensis", "Homo floresiensis", "~60,000-100,000 years ago (discovered 2003)", "Indonesia (Flores)", "Nicknamed the 'Hobbit', this diminutive hominin skeleton revealed a previously unknown, dwarfed human species that survived into relatively recent times."),
    ("Zinjanthropus Skull (Nutcracker Man)", "Paranthropus boisei", "Paranthropus boisei", "~1.75 million years ago (discovered 1959)", "Tanzania (Olduvai Gorge)", "The heavily built skull nicknamed 'Nutcracker Man', discovered by Mary Leakey, that helped establish East Africa as a cradle of human evolution."),
    ("Laetoli Footprints", "Laetoli", "Australopithecus afarensis", "~3.6 million years ago (discovered 1976)", "Tanzania", "A trail of fossilized hominin footprints preserved in volcanic ash, providing direct physical evidence of early upright walking."),
    ("Ida the Primate Fossil", "Darwinius", "Darwinius masillae", "~47 million years ago (discovered 1983, described 2009)", "Germany (Messel Pit)", "An exceptionally well-preserved early primate fossil that drew intense media attention as a claimed 'missing link', now housed at the Natural History Museum Oslo."),

    # --- Famous meteorites ---
    ("Hoba Meteorite", "Hoba meteorite", "Natural specimen", "~80,000 years ago (found 1920)", "Namibia", "The largest known intact meteorite on Earth, an iron mass weighing roughly 60 tonnes that has never been moved from where it fell."),
    ("Estherville Meteorite", "Estherville meteorite", "Natural specimen", "Unknown age (fell 1879)", "United States (Iowa)", "A witnessed mesosiderite meteorite fall whose numerous fragments are held in natural history collections across the United States."),
    ("Allende Meteorite", "Allende meteorite", "Natural specimen", "~4.567 billion years ago (fell 1969)", "Mexico (Chihuahua)", "The largest carbonaceous chondrite meteorite ever found on Earth, containing some of the oldest known solid matter in the solar system."),
    ("Murchison Meteorite", "Murchison meteorite", "Natural specimen", "~4.65 billion years ago (fell 1969)", "Australia (Victoria)", "A carbonaceous chondrite meteorite famous for containing dozens of amino acids and other complex organic compounds of extraterrestrial origin."),
    ("Cape York Meteorite (Ahnighito)", "Cape York meteorite", "Natural specimen", "~10,000 years ago (recovered 1894)", "Greenland", "A massive iron meteorite shower whose largest fragment, Ahnighito, was hauled to New York by explorer Robert Peary and now sits in the American Museum of Natural History."),
    ("Canyon Diablo Meteorite", "Canyon Diablo meteorite", "Natural specimen", "~50,000 years ago (fragments found from 1891)", "United States (Arizona)", "Fragments of the iron meteorite that created Meteor Crater, among the first meteorites used to date the age of the Earth."),
    ("Fukang Meteorite", "Fukang meteorite", "Natural specimen", "Unknown age (found 2000)", "China (Xinjiang)", "A strikingly beautiful pallasite meteorite prized for its translucent olivine crystals embedded in a metallic matrix."),
    ("Esquel Meteorite", "Esquel meteorite", "Natural specimen", "Unknown age (found 1951)", "Argentina", "A large pallasite meteorite renowned for its exceptionally clear, gem-quality olivine crystals."),
    ("Gibeon Meteorite", "Gibeon meteorite", "Natural specimen", "Unknown age (fall witnessed centuries ago; found 1836)", "Namibia", "An iron meteorite shower famous for its fine Widmanstätten crystal patterns, historically used by local Nama people to forge tools."),
    ("Nakhla Meteorite", "Nakhla meteorite", "Natural specimen", "~1.3 billion years ago (fell 1911)", "Egypt", "A Martian meteorite whose 1911 fall was famously (if apocryphally) said to have killed a dog, giving its name to the 'nakhlite' class of Mars rocks."),
    ("Tissint Meteorite", "Tissint meteorite", "Natural specimen", "Unknown age (fell 2011)", "Morocco", "A Martian meteorite whose fresh fall was witnessed and quickly recovered, yielding pristine samples of the Martian surface."),
    ("Chassigny Meteorite", "Chassigny meteorite", "Natural specimen", "~1.3 billion years ago (fell 1815)", "France", "A witnessed Martian meteorite fall that gives its name to the 'chassignite' class of Mars rocks, among the oldest scientifically documented meteorite falls in Europe."),
    ("Peekskill Meteorite", "Peekskill meteorite", "Natural specimen", "Unknown age (fell 1992)", "United States (New York)", "A meteorite whose fiery fall was captured on numerous home videos before it struck a parked car in Peekskill, New York."),
    ("Sikhote-Alin Meteorite", "Sikhote-Alin meteorite", "Natural specimen", "Unknown age (fell 1947)", "Russia", "An enormous iron meteorite shower whose fall produced one of the largest documented meteorite craters fields in recorded history."),
    ("Orgueil Meteorite", "Orgueil meteorite", "Natural specimen", "~4.5 billion years ago (fell 1864)", "France", "A carbonaceous chondrite meteorite of exceptional scientific importance for its pristine, primitive chemical composition."),
    ("Winchcombe Meteorite", "Winchcombe meteorite", "Natural specimen", "Unknown age (fell 2021)", "United Kingdom", "A rare carbonaceous chondrite that fell onto a driveway and was recovered within hours, yielding one of the freshest meteorite samples ever studied."),
    ("Ensisheim Meteorite", "Ensisheim meteorite", "Natural specimen", "Unknown age (fell 1492)", "France (Alsace)", "The oldest meteorite in the Western world with a precisely recorded fall date, witnessed and preserved since the fifteenth century."),
    ("Chelyabinsk Meteor Fragments", "Chelyabinsk meteor", "Natural specimen", "Unknown age (fell 2013)", "Russia", "Fragments of the largest natural object to enter Earth's atmosphere since the 1908 Tunguska event, whose airburst injured over a thousand people."),
    ("Tucson Ring Meteorite", "Tucson Ring meteorite", "Natural specimen", "Unknown age (known since 18th century)", "United States (Arizona)", "A historic iron meteorite known to Spanish colonists in Arizona since the 1700s, now held by the Smithsonian Institution."),
    ("Bacubirito Meteorite", "Bacubirito meteorite", "Natural specimen", "Unknown age (found 1863)", "Mexico (Sinaloa)", "One of the largest meteorites ever found, an elongated iron mass now displayed at the Centro de Ciencias de Sinaloa."),
    ("Mbozi Meteorite", "Mbozi meteorite", "Natural specimen", "Unknown age (documented 1930)", "Tanzania", "A massive iron meteorite left in situ near Mbeya, protected as a national monument."),
    ("Old Woman Meteorite", "Old Woman Meteorite", "Natural specimen", "Unknown age (found 1976)", "United States (California)", "The second-largest meteorite ever found in the United States, discovered in the Old Woman Mountains of the Mojave Desert."),
    ("Zagami Meteorite", "Zagami meteorite", "Natural specimen", "~180 million years ago (fell 1962)", "Nigeria", "A Martian meteorite whose fall was witnessed near the village of Zagami, giving its name to the 'shergottite' subclass it helped define."),
    ("Shergotty Meteorite", "Shergotty meteorite", "Natural specimen", "~165 million years ago (fell 1865)", "India", "The Martian meteorite whose fall in Bihar gave its name to the entire 'shergottite' classification of Mars rocks."),
    ("Norton County Meteorite", "Norton County meteorite", "Natural specimen", "Unknown age (fell 1948)", "United States (Kansas)", "The largest known aubrite meteorite, a rare type composed almost entirely of enstatite."),
    ("Brenham Meteorite", "Brenham meteorite", "Natural specimen", "Unknown age (found 1882)", "United States (Kansas)", "A pallasite meteorite shower prized by collectors for its striking olivine crystal inclusions."),
    ("Toluca Meteorite", "Toluca meteorite", "Natural specimen", "Unknown age (known since pre-Columbian times)", "Mexico", "A large iron meteorite shower discovered near Xiquipilco, valued for its coarse octahedrite crystal structure."),
    ("Odessa Meteorite", "Odessa meteorite", "Natural specimen", "~63,500 years ago (found 1922)", "United States (Texas)", "An iron meteorite shower associated with the Odessa Meteor Crater, one of the first proven impact craters in North America."),
    ("Middlesbrough Meteorite", "Middlesbrough meteorite", "Natural specimen", "Unknown age (fell 1881)", "United Kingdom", "A meteorite that struck near a railway line and became the subject of a notable ownership dispute between the landowner and the railway company."),
    ("Aguas Zarcas Meteorite", "Aguas Zarcas meteorite", "Natural specimen", "Unknown age (fell 2019)", "Costa Rica", "A carbonaceous chondrite meteorite shower prized for its pristine, quickly-recovered fragments rich in organic compounds."),
    ("Tagish Lake Meteorite", "Tagish Lake meteorite", "Natural specimen", "~4.55 billion years ago (fell 2000)", "Canada (British Columbia)", "An extremely primitive carbonaceous chondrite recovered from a frozen lake within days, preserving pristine pre-solar organic material."),
    ("Park Forest Meteorite", "Park Forest meteorite", "Natural specimen", "Unknown age (fell 2003)", "United States (Illinois)", "A meteorite shower that fell over a Chicago suburb, striking several homes and cars and yielding abundant fresh fragments."),
    ("Muonionalusta Meteorite", "Muonionalusta meteorite", "Natural specimen", "~1 million years ago (found 1906)", "Sweden", "One of the oldest known meteorites to have fallen on Earth still recoverable in fragments, prized for its fine Widmanstätten pattern."),
    ("El Chaco Meteorite", "Campo del Cielo", "Natural specimen", "~4,000-5,000 years ago (rediscovered 1969)", "Argentina", "One of the largest fragments of the Campo del Cielo meteorite shower, a massive iron mass left largely in situ in northern Argentina."),
    ("Agpalilik Meteorite", "Agpalilik meteorite", "Natural specimen", "Unknown age (found 1963)", "Greenland", "A large fragment of the Cape York meteorite shower, excavated decades after Ahnighito and now displayed at the Geological Museum in Copenhagen."),

    # --- Famous gems and mineral specimens ---
    ("Steinheim Skull", "Steinheim Skull", "Homo heidelbergensis", "~250,000-350,000 years ago (discovered 1933)", "Germany", "One of the best-preserved archaic human skulls from the Middle Pleistocene, important for understanding the ancestry of Neanderthals."),
    ("Gao-Guenie Meteorite", "Gao-Guenie meteorite", "Natural specimen", "Unknown age (fell 1960)", "Burkina Faso", "A large, widely studied and collected ordinary chondrite meteorite shower recovered across West Africa."),
    ("Star of India Sapphire", "Star of India (gem)", "Natural specimen", "Unknown age (mined centuries ago)", "Sri Lanka", "The largest and one of the most famous star sapphires in the world, displayed at the American Museum of Natural History."),
    ("Patricia Emerald", "Patricia Emerald", "Natural specimen", "Unknown age (found 1920)", "Colombia", "One of the largest gem-quality emerald crystals ever found, notable for its unusual twelve-sided form, held at the American Museum of Natural History."),
    ("Subway Garnet", "Subway Garnet", "Natural specimen", "Unknown age (found 1885)", "United States (New York City)", "A large almandine garnet crystal unearthed during excavation work on a Manhattan street, now in the American Museum of Natural History."),
    ("Hatcher the Triceratops", "Hatcher (dinosaur)", "Triceratops horridus", "~66-68 million years ago (excavated 1888-1891)", "United States (Wyoming)", "A mounted Triceratops skeleton assembled largely from fossils collected by fossil hunter John Bell Hatcher, long displayed at the Smithsonian's National Museum of Natural History."),
    ("Hooker Emerald Brooch Stone", "Hooker Emerald", "Natural specimen", "Unknown age", "Colombia", "A large square-cut Colombian emerald set in a brooch once owned by Janet Annenberg Hooker, donated to the Smithsonian Institution."),
    ("DeYoung Red Diamond", "DeYoung Red Diamond", "Natural specimen", "Unknown age", "South Africa", "One of the largest known red diamonds in the world, donated to the Smithsonian by gem collector Sydney DeYoung."),
    ("Tiffany Diamond", "Tiffany Diamond", "Natural specimen", "Unknown age (found 1877)", "South Africa", "A large fancy yellow diamond famously worn by Audrey Hepburn in publicity photographs for Breakfast at Tiffany's."),
    ("Dom Pedro Aquamarine", "Dom Pedro Aquamarine", "Natural specimen", "Unknown age (found 1980s)", "Brazil", "The largest cut aquamarine in the world, carved into an obelisk shape and held at the Smithsonian's National Museum of Natural History."),
    ("Logan Sapphire", "Logan Sapphire", "Natural specimen", "Unknown age", "Sri Lanka", "One of the largest faceted blue sapphires in existence, part of the Smithsonian's National Gem Collection."),
    ("Bahia Emerald", "Bahia Emerald", "Natural specimen", "Unknown age (found 2001)", "Brazil", "A massive matrix boulder containing thousands of carats of emerald crystals, subject of a decade-long legal ownership dispute."),
    ("Star of Asia Sapphire", "Star of Asia", "Natural specimen", "Unknown age", "Myanmar (Burma)", "A large star sapphire renowned for the sharp six-rayed asterism visible across its dome, part of the Smithsonian gem collection."),
    ("American Golden Topaz", "American Golden Topaz", "Natural specimen", "Unknown age", "Brazil", "One of the largest cut golden topaz gems in the world, displayed at the Smithsonian's National Museum of Natural History."),
    ("De Long Star Ruby", "DeLong Star Ruby", "Natural specimen", "Unknown age", "Myanmar (Burma)", "A large star ruby that was famously stolen in the 1964 Museum of Natural History jewel heist and later recovered."),
    ("Empress of Uruguay Amethyst Geode", "Empress of Uruguay", "Natural specimen", "~135 million years ago (found in Uruguay)", "Uruguay", "One of the largest amethyst geodes in the world, standing over three meters tall, displayed at Chicago's Field Museum."),
    ("Star of Bombay Sapphire", "Star of Bombay", "Natural specimen", "Unknown age", "Sri Lanka", "A famous star sapphire once owned by actress Mary Pickford, later donated to the Smithsonian Institution."),
    ("Rosser Reeves Star Ruby", "Rosser Reeves Star Ruby", "Natural specimen", "Unknown age", "Sri Lanka", "One of the finest and largest star rubies in the world, noted for its exceptionally sharp asterism."),
    ("Chalk Emerald", "Chalk Emerald", "Natural specimen", "Unknown age", "Colombia (origin of rough)", "A large, richly colored emerald donated to the Smithsonian by Mr. and Mrs. O. Roy Chalk."),
    ("Oppenheimer Diamond", "Oppenheimer Diamond", "Natural specimen", "Unknown age (found 1964)", "South Africa", "An uncut yellow diamond crystal notable for retaining its natural octahedral form, displayed at the Smithsonian."),
    ("Portuguese Diamond", "Portuguese Diamond", "Natural specimen", "Unknown age", "Brazil (origin, disputed)", "One of the largest faceted diamonds in the Smithsonian's collection, cut in an emerald shape with unusual blue fluorescence."),
    ("Alma King Rhodochrosite", "Alma King", "Natural specimen", "Unknown age (found 1992)", "United States (Colorado)", "A spectacular rhodochrosite crystal specimen from the Sweet Home Mine, considered among the finest mineral specimens ever found and displayed at the Denver Museum of Nature & Science."),

    # --- Famous taxidermy, mounted, and preserved animal specimens ---
    ("Martha the Last Passenger Pigeon", "Martha (passenger pigeon)", "Passenger pigeon", "Died 1914", "United States", "The last known passenger pigeon, who died in captivity at the Cincinnati Zoo, now preserved at the Smithsonian's National Museum of Natural History."),
    ("Guy the Gorilla", "Guy the Gorilla", "Western lowland gorilla", "1946-1978 (taxidermied after death)", "United Kingdom (born in Africa, lived at London Zoo)", "A beloved western lowland gorilla at London Zoo for over thirty years, now taxidermied and displayed at the Natural History Museum, London."),
    ("Snowflake the Albino Gorilla", "Snowflake (gorilla)", "Western lowland gorilla", "c. 1964-2003 (taxidermied after death)", "Spain (Barcelona Zoo)", "The only known albino gorilla ever documented, a major attraction at Barcelona Zoo and now preserved at the Museu de Ciències Naturals de Barcelona."),
    ("Dolly the Cloned Sheep", "Dolly (sheep)", "Finn-Dorset sheep", "1996-2003 (taxidermied after death)", "United Kingdom (Scotland)", "The first mammal ever cloned from an adult somatic cell, now taxidermied and displayed at the National Museum of Scotland."),
    ("Phar Lap the Racehorse", "Phar Lap", "Thoroughbred racehorse", "1926-1932", "Australia/New Zealand", "A legendary champion racehorse whose skeleton is held at the Museum of New Zealand Te Papa Tongarewa and mounted hide at Melbourne Museum."),
    ("Comanche the Cavalry Horse", "Comanche (horse)", "Horse", "c. 1862-1891 (taxidermied after death)", "United States", "A U.S. Cavalry horse said to be the sole survivor found at the Battle of the Little Bighorn, taxidermied and preserved at the University of Kansas Natural History Museum."),
    ("Balto the Sled Dog", "Balto", "Siberian husky (sled dog)", "1919-1933 (taxidermied after death)", "United States (Alaska)", "The lead sled dog credited with completing the 1925 serum run to Nome, taxidermied and displayed at the Cleveland Museum of Natural History."),
    ("Owney the Postal Dog", "Owney (dog)", "Mixed-breed terrier", "c. 1887-1897 (taxidermied after death)", "United States", "An unofficial mascot of the U.S. Railway Mail Service who traveled widely by mail train, taxidermied and preserved at the Smithsonian National Postal Museum."),
    ("Lonesome George the Tortoise", "Lonesome George", "Pinta Island tortoise", "c. 1910-2012 (taxidermied after death)", "Ecuador (Galápagos Islands)", "The last known individual of the Pinta Island tortoise subspecies, now preserved at the Charles Darwin Research Station."),
    ("Knut the Polar Bear", "Knut (polar bear)", "Polar bear", "2006-2011 (taxidermied after death)", "Germany (born at Berlin Zoo)", "A polar bear cub who became a global media sensation after being reared by zookeepers, now taxidermied at the Museum für Naturkunde Berlin."),
    ("Jumbo the Elephant's Skeleton", "Jumbo", "African bush elephant", "c. 1860-1885", "United Kingdom/United States (born in Sudan)", "A celebrated circus elephant exhibited by P. T. Barnum, whose skeleton is held at the American Museum of Natural History."),
    ("Henry the Colossal Squid", "Colossal squid", "Colossal squid", "Caught 2007", "New Zealand (Ross Sea)", "The largest colossal squid specimen ever recovered intact, preserved and displayed at the Museum of New Zealand Te Papa Tongarewa."),
    ("Archie the Giant Squid", "Giant squid", "Giant squid", "Caught 2004", "United Kingdom (Falkland Islands, specimen)", "A nearly nine-meter-long giant squid preserved in a specially built tank at the Natural History Museum, London, nicknamed 'Archie'."),
    ("Oxford Dodo", "Oxford Dodo", "Dodo", "Died 17th century", "Mauritius (specimen assembled in England)", "The only dodo soft-tissue remains surviving anywhere in the world, held at the Oxford University Museum of Natural History."),
    ("Eclipse the Racehorse Skeleton", "Eclipse (horse)", "Thoroughbred racehorse", "1764-1789", "United Kingdom", "An undefeated 18th-century racehorse whose skeleton has been studied for over two centuries and is preserved at the Royal Veterinary College, London."),
    ("Marengo's Skeleton", "Marengo (horse)", "Arabian horse", "c. 1793-1831", "France (Napoleon's warhorse)", "The skeleton of Napoleon Bonaparte's favored campaign warhorse, preserved at the National Army Museum, London."),
    ("Old Billy the Horse", "Old Billy", "Horse", "1760-1822", "United Kingdom", "Reputed to be the longest-lived horse on record, whose taxidermied head is preserved at Manchester Museum."),

    # --- Ice Age mummies and extinct megafauna ---
    ("Lyuba the Baby Mammoth", "Lyuba (mammoth)", "Woolly mammoth", "~41,800 years ago (discovered 2007)", "Russia (Yamal Peninsula)", "One of the most complete and best-preserved woolly mammoth mummies ever found, held at the Shemanovsky Museum in Salekhard."),
    ("Yuka the Mammoth", "Yuka (mammoth)", "Woolly mammoth", "~39,000 years ago (discovered 2010)", "Russia (Siberia)", "An exceptionally well-preserved woolly mammoth mummy notable for its intact soft tissue, muscle, and even liquid blood."),
    ("Dima the Mammoth Calf", "Dima (mammoth)", "Woolly mammoth", "~40,000 years ago (discovered 1977)", "Russia (Siberia)", "One of the first baby mammoth mummies ever scientifically studied in detail, held at the Zoological Museum in Saint Petersburg."),
    ("Blue Babe the Steppe Bison", "Blue Babe", "Steppe bison", "~36,000 years ago (discovered 1979)", "United States (Alaska)", "A mummified Ice Age steppe bison carcass, its skin tinted blue by mineral reaction, preserved at the University of Alaska Museum of the North."),
    ("Berezovka Mammoth", "Berezovka mammoth", "Woolly mammoth", "~35,000-44,000 years ago (discovered 1900)", "Russia (Siberia)", "One of the first frozen woolly mammoth carcasses recovered with soft tissue intact, mounted at the Zoological Museum of the Russian Academy of Sciences."),
    ("Megatherium Mounted Skeleton", "Megatherium", "Megatherium americanum", "~11,000 years ago (described 1788)", "Argentina", "The skeleton of a giant ground sloth sent to Spain in the 18th century, the first fossil skeleton of a giant extinct mammal ever mounted and studied."),
    ("Irish Elk Skeleton", "Irish elk", "Megaloceros giganteus", "~11,000 years ago (found in Irish peat bogs)", "Ireland", "A giant extinct deer known for its enormous antlers, whose skeletons recovered from Irish peat bogs became icons of extinction science."),
    ("Glyptodon Skeleton", "Glyptodon", "Glyptodon clavipes", "~10,000 years ago", "Argentina", "A car-sized armored mammal related to armadillos, whose mounted shell skeletons are among the most recognizable Ice Age fossils on display."),
    ("Steller's Sea Cow Skeleton", "Steller's sea cow", "Hydrodamalis gigas", "Extinct 1768", "Russia (Commander Islands)", "A giant marine mammal hunted to extinction within decades of its scientific discovery, its skeleton preserved in several natural history museums."),

    # --- Extinct species specimens and taxonomic icons ---
    ("Quagga Mounted Specimen", "Quagga", "Equus quagga quagga", "Extinct 1883", "South Africa", "One of only a handful of mounted quagga specimens surviving worldwide, a partially striped relative of the plains zebra hunted to extinction."),
    ("Thylacine Preserved Specimen", "Thylacine", "Thylacinus cynocephalus", "Last captive died 1936", "Australia", "A preserved specimen of the Tasmanian tiger, a carnivorous marsupial driven to extinction in the 20th century."),
    ("Great Auk Mounted Specimen", "Great auk", "Pinguinus impennis", "Extinct 1844", "United Kingdom/Iceland", "One of the rare surviving mounted specimens of the flightless great auk, hunted to extinction in the mid-19th century."),
    ("Huia Mounted Specimen", "Huia", "Heteralocha acutirostris", "Last confirmed sighting 1907", "New Zealand", "An extinct New Zealand bird notable for the extreme difference in beak shape between males and females, preserved in several museum collections."),
    ("Carolina Parakeet Specimen", "Carolina parakeet", "Conuropsis carolinensis", "Extinct 1918", "United States", "The only parrot species native to the eastern United States, driven to extinction in the early 20th century."),
    ("Labrador Duck Specimen", "Labrador duck", "Camptorhynchus labradorius", "Extinct c. 1878", "North America", "One of the rarest extinct North American birds, known today from only a small number of surviving museum specimens."),
    ("Xerces Blue Butterfly Specimens", "Xerces blue", "Glaucopsyche xerces", "Extinct c. 1943", "United States (San Francisco)", "The first butterfly species in North America documented to go extinct due to urban habitat destruction, preserved in entomological collections."),
    ("Rocky Mountain Locust Specimens", "Rocky Mountain locust", "Melanoplus spretus", "Extinct c. 1902", "United States", "Once forming the largest insect swarms ever recorded, this species vanished entirely within decades, preserved today only as museum specimens."),
    ("Piltdown Man Hoax Specimen", "Piltdown Man", "Fabricated composite forgery", "'Discovered' 1912, exposed 1953", "United Kingdom (Sussex)", "One of the most notorious scientific hoaxes in history, a forged 'missing link' skull assembled from human and orangutan bones, held at the Natural History Museum, London."),
    ("Cardiff Giant", "Cardiff Giant", "Gypsum carving (hoax)", "Carved 1868, 'discovered' 1869", "United States (New York)", "A famous 19th-century hoax 'petrified man' carved from gypsum and buried to be later 'discovered', now displayed at the Farmers' Museum."),

    # --- Aquatic and marine natural history icons ---
    ("Coelacanth Type Specimen", "Coelacanth", "Latimeria chalumnae", "Caught 1938", "South Africa", "The first modern coelacanth ever identified by science, a fish thought extinct for 66 million years, held at the South African Institute for Aquatic Biodiversity."),
    ("Hope the Blue Whale Skeleton", "Hope (blue whale)", "Blue whale", "Beached 1891 (skeleton mounted 2017)", "United Kingdom (Ireland, original stranding)", "A full-sized blue whale skeleton suspended in the entrance hall of the Natural History Museum, London, symbolizing conservation and humanity's relationship with the natural world."),
    ("Ashfall Fossil Beds Rhinoceros Herd", "Ashfall Fossil Beds", "Teleoceras major", "~12 million years ago (discovered 1971)", "United States (Nebraska)", "A mass death assemblage of ancient rhinoceroses and other animals buried by volcanic ash, preserved and exhibited exactly where they died."),
    ("Fenykovi Elephant", "Fenykovi elephant", "African bush elephant", "Shot 1955", "Angola", "The largest African bush elephant ever recorded, taxidermied and displayed in the rotunda of the Smithsonian's National Museum of Natural History."),

    # --- Space and planetary geology specimens ---
    ("Genesis Rock", "Genesis Rock", "Lunar anorthosite", "~4.1-4.5 billion years ago (collected 1971)", "United States (collected on the Moon by Apollo 15)", "A pristine sample of ancient lunar crust collected during the Apollo 15 mission, once thought to date to the Moon's formation."),

    # --- Additional famous dinosaur and prehistoric specimens ---
    ("Black Beauty the T. rex", "Black Beauty (dinosaur)", "Tyrannosaurus rex", "~66 million years ago (discovered 1980)", "Canada (Alberta)", "A Tyrannosaurus rex skeleton whose bones were naturally stained a dark bluish-black by minerals, held at the Royal Tyrrell Museum."),
    ("Jane the Juvenile Tyrannosaur", "Jane (dinosaur)", "Tyrannosaurus rex", "~66 million years ago (discovered 2001)", "United States (Montana)", "One of the most complete juvenile Tyrannosaurus rex skeletons known, central to debates over whether 'Nanotyrannus' is a distinct genus, held at the Burpee Museum of Natural History."),
    ("Bucky the T. rex", "Bucky (dinosaur)", "Tyrannosaurus rex", "~66 million years ago (discovered 1998)", "United States (South Dakota)", "A well-preserved Tyrannosaurus rex skeleton notable for a rare preserved furcula, displayed at the Children's Museum of Indianapolis."),
    ("Big John the Triceratops", "Big John (dinosaur)", "Triceratops horridus", "~66 million years ago (discovered 2014)", "United States (South Dakota)", "The largest known Triceratops skeleton ever assembled, sold at a record-breaking Paris auction in 2021."),
    ("Lane the Triceratops Mummy", "Lane (dinosaur)", "Triceratops", "~66 million years ago (discovered 2004)", "United States (Wyoming)", "An exceptionally well-preserved Triceratops specimen with extensive fossilized skin impressions, exhibited at the Wyoming Dinosaur Center."),
    ("Dakota the Dinosaur Mummy", "Dakota (dinosaur)", "Edmontosaurus", "~66-67 million years ago (discovered 1999)", "United States (North Dakota)", "A remarkably preserved 'dinosaur mummy' with fossilized skin covering much of its body, studied for insights into dinosaur soft-tissue anatomy."),
    ("Dracorex Holotype", "Dracorex", "Dracorex hogwartsia", "~66 million years ago (discovered 2003)", "United States (South Dakota)", "The type specimen of a spike-skulled pachycephalosaur named in honor of the Harry Potter novels, held at the Children's Museum of Indianapolis."),
    ("Sinosauropteryx Holotype", "Sinosauropteryx", "Sinosauropteryx prima", "~125 million years ago (discovered 1996)", "China (Liaoning)", "The first non-avian dinosaur fossil ever found with unambiguous evidence of feather-like filaments, a landmark specimen for understanding dinosaur-bird evolution."),
    ("Microraptor Holotype", "Microraptor", "Microraptor gui", "~120-125 million years ago (discovered 2000s)", "China (Liaoning)", "A small four-winged dinosaur fossil preserved with feather impressions, offering key evidence for the evolution of powered flight."),
    ("Confuciusornis Fossil", "Confuciusornis", "Confuciusornis sanctus", "~125 million years ago (discovered 1993)", "China (Liaoning)", "One of the earliest known beaked birds, preserved in exceptional numbers in the fossil beds of Liaoning Province."),
    ("Barnum Brown's Tyrannosaurus Mount", "Tyrannosaurus", "Tyrannosaurus rex", "~66-68 million years ago (discovered 1902-1908)", "United States (Montana)", "The specimens collected by fossil hunter Barnum Brown that became the basis for the first-ever mounted Tyrannosaurus rex skeleton, unveiled at the American Museum of Natural History in 1915."),
    ("Diplodocus carnegii Holotype", "Diplodocus", "Diplodocus carnegii", "~150 million years ago (discovered 1899)", "United States (Wyoming)", "The original skeleton on which the species Diplodocus carnegii was named, the basis for the many 'Dippy' casts later sent to museums worldwide."),
    ("Anomalocaris Holotype", "Anomalocaris", "Anomalocaris canadensis", "~508 million years ago (described 1892, reassembled 1980s)", "Canada (British Columbia)", "The fossil of the largest known predator of the Cambrian period, recovered from the Burgess Shale and long misidentified before being correctly reassembled."),
    ("Fighting Dinosaurs Fossil", "Fighting Dinosaurs", "Velociraptor and Protoceratops", "~75 million years ago (discovered 1971)", "Mongolia", "A extraordinary fossil capturing a Velociraptor and Protoceratops locked in combat at the moment of their simultaneous burial."),
    ("Andrews Expedition Dinosaur Eggs", "Protoceratops", "Protoceratops andrewsi", "~75 million years ago (discovered 1923)", "Mongolia", "The first dinosaur eggs ever scientifically recognized, found nested near Protoceratops skeletons during Roy Chapman Andrews's American Museum expeditions to the Gobi Desert."),

    # --- Additional famous meteorites ---
    ("Sylacauga Meteorite (Hodges Meteorite)", "Sylacauga meteorite", "Natural specimen", "Unknown age (fell 1954)", "United States (Alabama)", "The only meteorite in modern history confirmed to have struck a person, injuring Ann Hodges as it crashed through her roof."),
    ("Barwell Meteorite", "Barwell meteorite", "Natural specimen", "Unknown age (fell 1965)", "United Kingdom", "The largest recorded meteorite fall in the United Kingdom, scattering fragments across a Leicestershire village."),
    ("Nantan Meteorite", "Nantan meteorite", "Natural specimen", "Unknown age (fell c. 1516, recovered from 1958)", "China (Guangxi)", "A large iron meteorite shower recorded in ancient Chinese chronicles centuries before its fragments were scientifically recovered."),
    ("Vaca Muerta Meteorite", "Vaca Muerta meteorite", "Natural specimen", "Unknown age (found 1861)", "Chile (Atacama Desert)", "A rare mesosiderite meteorite shower found scattered across Chile's Atacama Desert."),
    ("Imilac Meteorite", "Imilac meteorite", "Natural specimen", "Unknown age (found 1822)", "Chile (Atacama Desert)", "A pallasite meteorite prized by collectors for its striking translucent olivine crystals."),
    ("Springwater Meteorite", "Springwater meteorite", "Natural specimen", "Unknown age (found 1931)", "Canada (Saskatchewan)", "A pallasite meteorite shower noted for its finely preserved olivine crystal structure."),
    ("Seymchan Meteorite", "Seymchan meteorite", "Natural specimen", "Unknown age (found 1967)", "Russia (Siberia)", "A pallasite meteorite whose polished slices reveal a striking network of metal and olivine crystal."),
    ("Gebel Kamil Meteorite", "Gebel Kamil meteorite", "Natural specimen", "~5,000 years ago (found 2009)", "Egypt", "An iron meteorite associated with the well-preserved Kamil impact crater in the Egyptian desert."),
    ("Dronino Meteorite", "Dronino meteorite", "Natural specimen", "Unknown age (found 2000)", "Russia", "An unusually porous iron meteorite shower recovered from a peat bog near Moscow."),
    ("Hraschina Meteorite", "Hraschina meteorite", "Natural specimen", "Unknown age (fell 1751)", "Croatia", "The first meteorite fall in Europe to be scientifically investigated and confirmed as having fallen from the sky, held at the Natural History Museum Vienna."),
    ("NWA 7034 (Black Beauty Martian Meteorite)", "NWA 7034", "Natural specimen", "~4.4 billion years ago (found 2011)", "Northwest Africa (Morocco/Western Sahara)", "A Martian meteorite nicknamed 'Black Beauty', notable as the oldest known Martian meteorite and for its high water content."),
    ("Kaidun Meteorite", "Kaidun meteorite", "Natural specimen", "Unknown age (fell 1980)", "Yemen", "An unusually diverse meteorite containing fragments from multiple distinct parent bodies, among the most chemically complex meteorites known."),
    ("Marjalahti Meteorite", "Marjalahti meteorite", "Natural specimen", "Unknown age (fell 1902)", "Russia (Karelia)", "One of the earliest scientifically documented achondrite meteorite falls, contributing to early classification of stony meteorites."),
    ("Johnstown Meteorite", "Johnstown meteorite", "Natural specimen", "Unknown age (fell 1924)", "United States (Colorado)", "A witnessed meteorite fall that helped define the diogenite class of achondrite meteorites thought to originate from the asteroid Vesta."),
    ("Bjurbole Meteorite", "Bjurböle meteorite", "Natural specimen", "Unknown age (fell 1899)", "Finland", "A well-studied stony meteorite fall whose fragments are held in numerous European natural history collections."),
    ("Pultusk Meteorite", "Pułtusk meteorite", "Natural specimen", "Unknown age (fell 1868)", "Poland", "One of the largest recorded meteorite showers by number of individual stones, with an estimated 70,000 fragments recovered."),
    ("L'Aigle Meteorite", "L'Aigle meteorite", "Natural specimen", "Unknown age (fell 1803)", "France", "A witnessed meteorite shower whose scientific investigation by physicist Jean-Baptiste Biot helped convince the scientific establishment that stones truly fall from the sky."),
    ("Krasnojarsk Meteorite", "Krasnojarsk meteorite", "Natural specimen", "Unknown age (found 1749)", "Russia (Siberia)", "The pallasite meteorite studied by naturalist Peter Simon Pallas that gave its name to the entire class of stony-iron pallasite meteorites."),
    ("Ediacara Hills Fossil Beds", "Ediacaran biota", "Natural specimen", "~575-541 million years ago (discovered 1946)", "Australia (South Australia)", "The type locality where the earliest known complex multicellular life forms were first recognized, giving their name to the Ediacaran geological period."),

    # --- Additional famous mineral specimen ---
    ("Alma Rose Rhodochrosite", "Alma Rose (mineral)", "Natural specimen", "Unknown age (found 1965)", "United States (Colorado)", "A large, richly colored rhodochrosite crystal specimen from the Sweet Home Mine, ranked among the finest rhodochrosite specimens ever recovered."),

    # --- Additional famous hominin fossils ---
    ("Neo the Homo naledi Skeleton", "Homo naledi", "Homo naledi", "~236,000-335,000 years ago (discovered 2013-2014)", "South Africa", "One of the most complete Homo naledi skeletons recovered from the Rising Star Cave system, a small-brained hominin species that puzzlingly appears to have deliberately deposited its dead."),
    ("Karabo the Australopithecus sediba", "Australopithecus sediba", "Australopithecus sediba", "~1.98 million years ago (discovered 2008)", "South Africa", "The well-preserved juvenile holotype skeleton of a species that shares features with both older australopithecines and early Homo."),
    ("Shanidar 1 Neanderthal Skeleton", "Shanidar Cave", "Homo neanderthalensis", "~45,000-35,000 years ago (discovered 1957)", "Iraq", "A Neanderthal skeleton from Shanidar Cave whose injuries and possible burial context sparked long-running debate over Neanderthal care for the disabled and ritual burial."),
    ("Selam the Dikika Child", "Dikika", "Australopithecus afarensis", "~3.3 million years ago (discovered 2000)", "Ethiopia", "The remarkably complete skeleton of a roughly three-year-old Australopithecus afarensis child, among the best-preserved early hominin juveniles ever found."),

    # --- Additional famous extinct megafauna and mounted skeletons ---
    ("Peale's Mammoth Skeleton", "Peale's Mammoth", "American mastodon", "~11,000 years ago (excavated 1801)", "United States (New York)", "The first nearly complete mastodon skeleton ever mounted and exhibited, assembled by naturalist Charles Willson Peale for his Philadelphia museum."),
    ("Warren Mastodon Skeleton", "Warren Mastodon", "American mastodon", "~11,000 years ago (excavated 1845)", "United States (New York)", "One of the most complete American mastodon skeletons ever found, long displayed by physician John Collins Warren before entering the American Museum of Natural History."),
    ("Sasha the Woolly Rhinoceros", "Woolly rhinoceros", "Woolly rhinoceros", "~34,000 years ago (discovered 2014)", "Russia (Siberia)", "An exceptionally well-preserved baby woolly rhinoceros mummy, among the best-preserved Ice Age rhinoceros remains ever found."),
    ("Adams Mammoth", "Adams Mammoth", "Woolly mammoth", "~36,000 years ago (discovered 1799)", "Russia (Siberia)", "The first frozen woolly mammoth carcass ever scientifically studied, recovered from Siberian permafrost and displayed at the Zoological Museum of the Russian Academy of Sciences."),

    # --- Additional famous extinct species specimens ---
    ("Moa Mounted Skeleton", "Moa", "Moa", "Extinct c. 1440", "New Zealand", "Mounted skeletons of these giant flightless birds, hunted to extinction by early Maori settlers, are centerpieces of New Zealand's natural history museums."),
    ("Elephant Bird Egg", "Aepyornis", "Aepyornis maximus", "Extinct c. 1000-1200 CE", "Madagascar", "The largest known bird egg, laid by a giant flightless bird that once roamed Madagascar before its extinction."),
    ("Ivory-billed Woodpecker Specimen", "Ivory-billed woodpecker", "Ivory-billed woodpecker", "Last confirmed sighting mid-20th century", "United States", "Museum study skins of one of North America's largest and most sought-after woodpeckers, whose possible extinction remains debated."),
    ("Qiqi the Baiji Dolphin", "Baiji", "Baiji (Yangtze river dolphin)", "1980-2002 (preserved after death)", "China", "The only baiji ever kept in captivity for long-term study, preserved at the Institute of Hydrobiology in Wuhan after the species was declared functionally extinct."),
    ("Golden Toad Specimens", "Golden toad", "Golden toad", "Extinct c. 1989", "Costa Rica", "A brilliantly colored toad endemic to a small Costa Rican cloud forest, among the most iconic amphibian extinctions of the 20th century."),
    ("Last Wild Passenger Pigeon Specimen", "Passenger pigeon", "Passenger pigeon", "Shot 1900", "United States (Ohio)", "Believed to be the last passenger pigeon shot in the wild, preserved as a reminder of a species that once numbered in the billions."),
    ("Thirioux Dodo Skeleton", "Thirioux Dodo", "Dodo", "Extinct late 17th century", "Mauritius", "One of the most complete dodo skeletons ever assembled from a single individual, discovered by amateur naturalist Etienne Thirioux and held at the Mauritius Institute."),
    ("Tsavo Man-Eaters", "Tsavo Man-Eaters", "Lion", "1898 (taxidermied after death)", "Kenya", "Two maneless male lions that killed numerous railway workers during construction of the Uganda Railway, taxidermied and displayed at the Field Museum, Chicago."),
    ("Aurochs Skeleton", "Aurochs", "Aurochs", "Extinct 1627", "Poland", "The skeletal remains of the wild ancestor of domestic cattle, whose last individual died in the Jaktorów Forest in Poland."),
    ("Tarpan Mounted Specimen", "Tarpan", "Tarpan", "Extinct 1909", "Russia/Ukraine", "One of the last known specimens of the European wild horse, preserved in Russian natural history collections."),
    ("Bubal Hartebeest Specimen", "Bubal hartebeest", "Bubal hartebeest", "Extinct 1923", "North Africa", "A North African antelope hunted to extinction in the early 20th century, known today from a small number of museum specimens."),
    ("Sea Mink Specimen", "Sea mink", "Sea mink", "Extinct c. 1894", "United States/Canada (Atlantic coast)", "A large, little-studied mink hunted to extinction for its fur, known today from only a handful of skeletal fragments."),
    ("Caribbean Monk Seal Specimen", "Caribbean monk seal", "Caribbean monk seal", "Extinct c. 1952", "Caribbean Sea", "The only seal species native to the Caribbean, declared extinct in the late 20th century and known today through preserved museum specimens."),
    ("Falkland Islands Wolf Specimen", "Falkland Islands wolf", "Falkland Islands wolf", "Extinct 1876", "Falkland Islands", "The only native land mammal of the Falkland Islands, hunted to extinction and puzzled over by Charles Darwin, who collected one of the surviving museum specimens."),
    ("Bramble Cay Melomys Specimens", "Bramble Cay melomys", "Bramble Cay melomys", "Declared extinct 2019", "Australia", "A small rodent widely cited as the first mammal species driven extinct primarily by human-caused climate change."),
    ("Schomburgk's Deer Specimen", "Schomburgk's deer", "Schomburgk's deer", "Extinct 1938", "Thailand", "A deer species known almost entirely from its distinctively branched antlers preserved in museum collections after its extinction."),
    ("Toolache Wallaby Specimen", "Toolache wallaby", "Toolache wallaby", "Extinct c. 1943", "Australia", "An elegant, swift-moving wallaby driven to extinction in South Australia, preserved today in a small number of museum skins."),
    ("Paradise Parrot Specimen", "Paradise parrot", "Paradise parrot", "Last confirmed sighting 1927", "Australia", "One of Australia's most strikingly colored parrots, presumed extinct after habitat loss, preserved in ornithological collections."),
    ("Heath Hen Specimen", "Heath hen", "Heath hen", "Extinct 1932", "United States (Massachusetts)", "A once-abundant grouse of the eastern United States whose last individual, nicknamed 'Booming Ben', died on Martha's Vineyard."),
    ("Fish-Within-a-Fish Fossil", "Xiphactinus", "Xiphactinus audax", "~89 million years ago (discovered 1952)", "United States (Kansas)", "A famous Cretaceous sea fossil of a giant Xiphactinus that died shortly after swallowing another large fish whole, preserved together at the Sternberg Museum of Natural History."),
]
CATEGORY_ASSIGNMENTS.append((NATURAL_HISTORY_BATCH2, "natural_history"))


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
