"""Search for a picture across many free image collections, not only Wikipedia.

Each source is asked the same question; a source that is down, slow or has
nothing is skipped. Every hit carries where it came from and its licence, so
the app can credit it honestly:

* Wikimedia Commons (file search, with author and licence)
* Openverse (openly licensed photos from Flickr, museums, libraries and more)
* The Metropolitan Museum of Art, the Art Institute of Chicago and the Cleveland
  Museum of Art (public-domain / CC0 pictures only)
* NASA Image and Video Library
* Library of Congress (rights are not stated per picture, so the credit says so)

No sign-up or key is needed for any of them.
"""
from __future__ import annotations

import html
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote, quote_plus
from urllib.request import Request, urlopen

HEADERS = {"User-Agent": "EduAI/1.0 (educational; contact@eduai.app)", "Accept": "application/json"}
TIMEOUT = 8
CC0 = "https://creativecommons.org/publicdomain/zero/1.0/"
SKIP_WORDS = ("flag", "logo", "map", "icon", "symbol", "coat of arms", "seal", "signature", "diagram", "pictogram")


def _json(url: str) -> dict:
    with urlopen(Request(url, headers=HEADERS), timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _text(value) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", str(value or "")))).strip()


def _hit(source: str, url: str, title: str, *, creator: str = "", license: str = "", license_url: str = "",
         page: str = "", note: str = "", fallback_url: str = "", text: str = "") -> dict:
    who = creator or source
    line = " · ".join(p for p in (who, license, note) if p)
    return {"source": source, "url": url, "fallback_url": fallback_url, "title": _text(title) or source,
            "text": _text(text)[:600],
            "credit": {"credit": who, "license": license or None, "license_url": license_url or None,
                       "source_url": page or url, "line": line}}


# ── the sources ───────────────────────────────────────────────────────────────
def commons(query: str) -> list[dict]:
    url = ("https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrlimit=8"
           f"&gsrsearch={quote_plus(query + ' filetype:bitmap')}&prop=imageinfo&iiprop=url%7Cmime%7Cextmetadata"
           "&iiurlwidth=900&format=json")
    pages = sorted(((_json(url).get("query") or {}).get("pages") or {}).values(), key=lambda p: p.get("index", 0))
    out = []
    for page in pages:
        title = page.get("title") or ""
        if any(word in title.lower() for word in SKIP_WORDS):
            continue
        info = (page.get("imageinfo") or [{}])[0]
        if info.get("mime") not in ("image/jpeg", "image/png"):
            continue
        meta = info.get("extmetadata") or {}
        value = lambda name: _text((meta.get(name) or {}).get("value"))  # noqa: E731
        out.append(_hit("Wikimedia Commons", info.get("thumburl") or info.get("url"), re.sub(r"^File:|\.\w+$", "", title),
                        creator=value("Artist"), license=value("LicenseShortName"), license_url=value("LicenseUrl"),
                        page=info.get("descriptionurl") or "", text=value("ImageDescription") + " " + value("Categories")))
    return out


def openverse(query: str) -> list[dict]:
    data = _json(f"https://api.openverse.org/v1/images/?q={quote_plus(query)}&page_size=8&mature=false")
    out = []
    for item in data.get("results") or []:
        url = item.get("thumbnail") or item.get("url")
        if not url or any(word in (item.get("title") or "").lower() for word in SKIP_WORDS):
            continue
        lic = " ".join(x for x in ("CC", str(item.get("license") or "").upper(), item.get("license_version") or "") if x) \
            if item.get("license") not in ("cc0", "pdm") else {"cc0": "CC0 1.0", "pdm": "Public Domain Mark"}[item["license"]]
        out.append(_hit(f"Openverse ({item.get('source') or item.get('provider') or 'various'})", url, item.get("title") or "",
                        creator=item.get("creator") or "", license=lic, license_url=item.get("license_url") or "",
                        page=item.get("foreign_landing_url") or "", fallback_url=item.get("url") or "",
                        text=" ".join(str(t.get("name") if isinstance(t, dict) else t) for t in (item.get("tags") or []))))
    return out


def met(query: str) -> list[dict]:
    ids = (_json(f"https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q={quote_plus(query)}")
           .get("objectIDs") or [])[:4]
    out = []
    for oid in ids:
        record = _json(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{int(oid)}")
        url = record.get("primaryImageSmall") or record.get("primaryImage")
        if record.get("isPublicDomain") and url:
            out.append(_hit("The Metropolitan Museum of Art", url, record.get("title") or "",
                            creator=record.get("artistDisplayName") or "The Metropolitan Museum of Art",
                            license="CC0 1.0 (Open Access)", license_url=CC0, page=record.get("objectURL") or "",
                            text=" ".join(str(record.get(k) or "") for k in ("objectName", "culture", "period", "medium", "department"))))
    return out


def chicago(query: str) -> list[dict]:
    data = _json("https://api.artic.edu/api/v1/artworks/search?limit=6&fields=id,title,image_id,is_public_domain,artist_title"
                 f"&q={quote_plus(query)}")
    out = []
    for item in data.get("data") or []:
        if item.get("is_public_domain") and item.get("image_id"):
            out.append(_hit("Art Institute of Chicago", f"https://www.artic.edu/iiif/2/{item['image_id']}/full/843,/0/default.jpg",
                            item.get("title") or "", creator=item.get("artist_title") or "Art Institute of Chicago",
                            license="CC0 1.0 (Open Access)", license_url=CC0, page=f"https://www.artic.edu/artworks/{item['id']}"))
    return out


def cleveland(query: str) -> list[dict]:
    data = _json(f"https://openaccess-api.clevelandart.org/api/artworks/?q={quote_plus(query)}&has_image=1&limit=6")
    out = []
    for item in data.get("data") or []:
        image = ((item.get("images") or {}).get("web") or {}).get("url")
        if image and item.get("share_license_status") == "CC0":
            creators = item.get("creators") or [{}]
            out.append(_hit("Cleveland Museum of Art", image, item.get("title") or "",
                            creator=_text(creators[0].get("description")) or "Cleveland Museum of Art",
                            license="CC0 1.0 (Open Access)", license_url=CC0, page=item.get("url") or "",
                            text=_text(item.get("description")) + " " + _text(item.get("culture")) + " " + _text(item.get("type"))))
    return out


def nasa(query: str) -> list[dict]:
    data = _json(f"https://images-api.nasa.gov/search?q={quote_plus(query)}&media_type=image")
    out = []
    for item in ((data.get("collection") or {}).get("items") or [])[:6]:
        meta = (item.get("data") or [{}])[0]
        links = item.get("links") or []
        if links and links[0].get("href"):
            out.append(_hit("NASA Image and Video Library", links[0]["href"], meta.get("title") or "",
                            creator=meta.get("photographer") or meta.get("center") or "NASA",
                            license="NASA media (generally public domain)",
                            page=f"https://images.nasa.gov/details/{quote(str(meta.get('nasa_id') or ''))}",
                            text=_text(meta.get("description")) + " " + " ".join(meta.get("keywords") or [])))
    return out


def loc(query: str) -> list[dict]:
    data = _json(f"https://www.loc.gov/photos/?q={quote_plus(query)}&fo=json&c=6")
    out = []
    for item in data.get("results") or []:
        images = item.get("image_url") or []
        url = next((u for u in images if str(u).lower().split("?")[0].endswith((".jpg", ".jpeg", ".png"))), None)
        if url:
            if url.startswith("//"):
                url = "https:" + url
            out.append(_hit("Library of Congress", url, item.get("title") or "", creator="Library of Congress",
                            note="check rights before reuse", page=item.get("url") or item.get("id") or "",
                            text=" ".join(str(x) for x in (item.get("subject") or item.get("subjects") or []))))
    return out


SOURCES = {"commons": commons, "openverse": openverse, "met": met, "chicago": chicago, "cleveland": cleveland,
           "nasa": nasa, "loc": loc}
GENERAL = ("commons", "openverse", "nasa", "loc", "met", "chicago", "cleveland")
ARTWORKS = ("met", "chicago", "cleveland", "commons", "openverse", "loc", "nasa")


# ── does the picture fit the lesson? ──────────────────────────────────────────
STOP = set("""a an the of and or for to in on at by with from into over under about as is are was were be been being this that
these those it its their your our you how what why when where which who basics basic introduction intro lesson lessons
guide guides skill skills level levels part parts using use used uses understanding learn learning practice practical
fundamentals foundations foundation overview deep dive study studies theory unit more than not also can will should would
could safe safely rules rule""".split())
STRONG, POSSIBLE = 0.6, 0.3


def tokens(text: str) -> set:
    """The meaningful words of a text, lower-cased with a plural 's' removed."""
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    out = set()
    for word in words:
        if len(word) < 3 or word in STOP:
            continue
        out.add(word[:-1] if len(word) > 4 and word.endswith("s") and not word.endswith("ss") else word)
    return out


def relevance(hit: dict, title: str, description: str = "", context: str = "") -> float:
    """0-1: how well a picture's own words (title, description, tags) fit the lesson's title and description.

    Mostly the share of the lesson title's key words that the picture's text also has, plus a smaller share for
    the lesson description and a small nudge for the subject. It is a check, not a guarantee: the picture's
    title is all most collections give us.
    """
    have = tokens(f"{hit.get('title', '')} {hit.get('text', '')}")
    want = tokens(title)
    if not want:
        return 0.5
    title_share = len(want & have) / len(want)
    desc = tokens(description) - want
    desc_share = min(1.0, len(desc & have) / 4) if desc else 0.0
    subject = 0.1 if tokens(context) & have else 0.0
    return round(min(1.0, title_share * 0.8 + desc_share * 0.3 + subject), 2)


def match_label(score: float) -> str:
    return "Good match" if score >= STRONG else "Possible match" if score >= POSSIBLE else "Weak match"


def search(query: str, order: tuple = GENERAL, per_source: int = 3, log=None, topic: dict | None = None) -> list[dict]:
    """Pictures for `query` from every source, in the order given (a failing source is skipped).

    With `topic` ({title, description, context}) each picture gets a ``score`` and ``match`` label for how well
    it fits the lesson, and the best fits come first.
    """
    query = (query or "").strip()
    if not query:
        return []

    def ask(name):
        try:
            return SOURCES[name](query)[:per_source]
        except Exception as exc:
            if log is not None:
                log.append(f"{name}: {exc}")
            return []

    with ThreadPoolExecutor(max_workers=len(order)) as pool:
        results = list(pool.map(ask, order))
    seen, out = set(), []
    for hits in results:
        for hit in hits:
            if hit["url"] and hit["url"] not in seen:
                seen.add(hit["url"])
                out.append(hit)
    if topic:
        for hit in out:
            hit["score"] = relevance(hit, topic.get("title", ""), topic.get("description", ""), topic.get("context", ""))
            hit["match"] = match_label(hit["score"])
        out.sort(key=lambda h: -h["score"])  # stable: equal scores keep the source order
    return out
