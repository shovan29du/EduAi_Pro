"""Authored enrichment content for Master's Year 1 and 2 lessons.

`PACKS` maps a subject name to a reference sheet (formulas, a table and
landmark cases). `RULES` are topic entries matched against lesson titles.
Every figure, date and formula here is real and checkable; nothing is invented.
"""


def F(label, expr, note=""):
    return {"label": label, "expr": expr, "note": note}


def Tab(title, headers, *rows):
    return {"title": title, "headers": list(headers), "rows": [list(r) for r in rows]}


def Case(title, when, summary, takeaway, wiki=""):
    return {"title": title, "when": when, "summary": summary, "takeaway": takeaway, "wiki": wiki}


def Pack(tables=(), cases=()):
    """Subject reference sheet: a data table and landmark cases. Equations are
    deliberately not part of it -- they appear only on lessons about a
    quantitative topic (see Rule)."""
    return {"tables": list(tables), "cases": list(cases)}


def Chart(title, kind, x_label, y_label, data, series, note="", log=False, lines=()):
    """kind is 'line', 'bar' or 'scatter'; data is a list of {'x': .., <series>: ..} rows.
    For 'scatter', `series` are drawn as points and `lines` as fitted lines."""
    return {"title": title, "kind": kind, "x_label": x_label, "y_label": y_label,
            "data": data, "series": list(series), "lines": list(lines), "note": note, "log": log}


def Rule(rid, pattern, wiki="", subjects=None, formulas=(), tables=(), cases=(), charts=(), levels=None):
    return {"id": rid, "pattern": pattern, "wiki": wiki, "subjects": list(subjects) if subjects else None,
            "levels": [l.lower() for l in levels] if levels else None,
            "formulas": list(formulas), "tables": list(tables), "cases": list(cases), "charts": list(charts)}


from .packs_tech import PACKS as _T  # noqa: E402
from .packs_business import PACKS as _B  # noqa: E402
from .packs_science import PACKS as _S  # noqa: E402
from .packs_humanities import PACKS as _H  # noqa: E402
from .rules import RULES  # noqa: E402

PACKS = {**_T, **_B, **_S, **_H}
