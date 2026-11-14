#!/usr/bin/env python3
"""Attach real historical political-border data to each region marker in
the History Atlas (backend/data/historical_maps/historical_maps.json).

Data source: aourednik/historical-basemaps (GPL-3.0), a real, sourced
dataset of world political boundaries at 54 historical snapshot years
(-123000 to 2010), each feature carrying the era-appropriate name of the
polity that held that territory at that time.

For each of this app's 52 century periods, this script:
  1. Picks the nearest available snapshot year to that period's midpoint.
  2. For every region marker in that period, finds which polity polygon
     (if any) contains that marker's lat/lng in the matched year's data.
  3. Projects the matched polygon to an SVG path using the exact same
     equirectangular projection already used by HistoricalWorldMap.jsx
     and mapProjection.js (x=(lng+180)/360*1000, y=(90-lat)/180*500),
     decimated for bundle size.
  4. Records the real historical polity name alongside the path, so the
     frontend can both draw the border and label it with the name used
     in that era -- distinct from (and a useful complement to) this
     project's existing curated "name" field, which is often an
     archaeological-culture label rather than a political one.

Regions with no containing polygon (common for stateless/hunter-gatherer
contexts, or simply gaps in the source dataset) are left without a
border rather than guessing one -- consistent with this project's
no-fabrication rule.

Downloads via the GeoJSON files already cached in /tmp/hb_cache by the
companion fetch step (see session notes); re-run with FETCH=1 to
re-download if that cache is gone.

Writes:
    frontend/src/utils/historicalBorders.js

Re-run after editing:
    python3 backend/scripts/build_historical_borders.py
"""
from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
HISTORICAL_MAPS_PATH = BASE_DIR / "data" / "historical_maps" / "historical_maps.json"
FRONTEND_OUT_PATH = BASE_DIR.parent / "frontend" / "src" / "utils" / "historicalBorders.js"
CACHE_DIR = Path("/tmp/hb_cache")
INDEX_URL = "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/index.json"
GEOJSON_BASE = "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/"

MAP_WIDTH = 1000
MAP_HEIGHT = 500

AVAILABLE_YEARS = [
    -123000, -10000, -8000, -5000, -4000, -3000, -2000, -1500, -1000, -700,
    -500, -400, -323, -300, -200, -100, -1, 100, 200, 300, 400, 500, 600,
    700, 800, 900, 1000, 1100, 1200, 1279, 1300, 1400, 1492, 1500, 1530,
    1600, 1650, 1700, 1715, 1783, 1800, 1815, 1878, 1880, 1900, 1914, 1920,
    1930, 1938, 1945, 1960, 1994, 2000, 2010,
]


def parse_mid_year(years_str: str) -> float:
    s = years_str.replace("–", "-").replace("c.", "").strip()
    is_bce = "BCE" in s
    nums = [int(n) for n in re.findall(r"\d+", s)]
    mid = (nums[0] + nums[1]) / 2 if len(nums) == 2 else float(nums[0])
    return -mid if is_bce else mid


def nearest_year(target: float) -> int:
    return min(AVAILABLE_YEARS, key=lambda y: abs(y - target))


def fetch_index() -> dict:
    index_path = CACHE_DIR / "index.json"
    if index_path.exists():
        return json.loads(index_path.read_text(encoding="utf-8"))
    req = urllib.request.Request(INDEX_URL, headers={"User-Agent": "EduAI/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    index_path.write_bytes(data)
    return json.loads(data)


def fetch_geojson(filename: str) -> dict:
    cache_path = CACHE_DIR / filename
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    req = urllib.request.Request(GEOJSON_BASE + filename, headers={"User-Agent": "EduAI/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(data)
    return json.loads(data)


def point_in_ring(lng: float, lat: float, ring: list) -> bool:
    """Standard ray-casting point-in-polygon test for a single linear ring."""
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if ((yi > lat) != (yj > lat)) and (
            lng < (xj - xi) * (lat - yi) / (yj - yi + 1e-15) + xi
        ):
            inside = not inside
        j = i
    return inside


def point_in_polygon(lng: float, lat: float, polygon: list) -> bool:
    """polygon = [exterior_ring, hole_ring, hole_ring, ...] (GeoJSON Polygon)."""
    if not polygon:
        return False
    if not point_in_ring(lng, lat, polygon[0]):
        return False
    for hole in polygon[1:]:
        if point_in_ring(lng, lat, hole):
            return False
    return True


def point_in_geometry(lng: float, lat: float, geometry: dict) -> bool:
    gtype = geometry.get("type")
    coords = geometry.get("coordinates")
    if gtype == "Polygon":
        return point_in_polygon(lng, lat, coords)
    if gtype == "MultiPolygon":
        return any(point_in_polygon(lng, lat, poly) for poly in coords)
    return False


def project(lng: float, lat: float) -> tuple[float, float]:
    x = (lng + 180) / 360 * MAP_WIDTH
    y = (90 - lat) / 180 * MAP_HEIGHT
    return round(x, 2), round(y, 2)


TARGET_POINTS_PER_RING = 60


def decimate(points: list, every: int) -> list:
    if len(points) <= every * 3:
        return points
    out = points[::every]
    if out[-1] != points[-1]:
        out.append(points[-1])
    return out


def ring_to_path(ring: list) -> str:
    every = max(1, round(len(ring) / TARGET_POINTS_PER_RING))
    pts = decimate(ring, every)
    cmds = []
    for i, pt in enumerate(pts):
        lng, lat = pt[0], pt[1]
        x, y = project(lng, lat)
        cmds.append(f"{'M' if i == 0 else 'L'}{x} {y}")
    cmds.append("Z")
    return " ".join(cmds)


def ring_area(ring: list) -> float:
    """Rough shoelace area in degrees^2, used to drop tiny specks (small
    islands, slivers) from very fragmented MultiPolygons to control size."""
    area = 0.0
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i][0], ring[i][1]
        x2, y2 = ring[(i + 1) % n][0], ring[(i + 1) % n][1]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


def ring_centroid(ring: list) -> tuple[float, float]:
    """Simple vertex-average centroid (good enough for label placement,
    not a true area centroid)."""
    n = len(ring)
    lng = sum(pt[0] for pt in ring) / n
    lat = sum(pt[1] for pt in ring) / n
    return lng, lat


def geometry_to_path_and_label(geometry: dict, min_area: float = 0.05) -> tuple[str, tuple[float, float] | None]:
    gtype = geometry.get("type")
    coords = geometry.get("coordinates")
    polygons = coords if gtype == "MultiPolygon" else [coords] if gtype == "Polygon" else []
    # Keep the largest ring always (even if small, e.g. a single-island
    # polity), plus any other ring above the area threshold.
    rings_with_area = []
    for poly in polygons:
        for ring in poly:
            rings_with_area.append((ring_area(ring), ring))
    if not rings_with_area:
        return "", None
    rings_with_area.sort(key=lambda t: t[0], reverse=True)
    largest_ring = rings_with_area[0][1]
    kept = [largest_ring] + [r for a, r in rings_with_area[1:] if a >= min_area]
    path = " ".join(ring_to_path(ring) for ring in kept)
    label_lng, label_lat = ring_centroid(largest_ring)
    label_x, label_y = project(label_lng, label_lat)
    return path, (label_x, label_y)


def find_containing_feature(lng: float, lat: float, features: list) -> dict | None:
    for feature in features:
        geom = feature.get("geometry")
        if geom and point_in_geometry(lng, lat, geom):
            return feature
    return None


def main() -> None:
    index = fetch_index()
    fname_by_year = {y["year"]: y["filename"] for y in index["years"]}

    data = json.loads(HISTORICAL_MAPS_PATH.read_text(encoding="utf-8"))

    geojson_cache: dict[int, dict] = {}
    result: dict[str, list] = {}
    matched = 0
    unmatched = 0

    for period in data["periods"]:
        mid = parse_mid_year(period["years"])
        year = nearest_year(mid)
        if year not in geojson_cache:
            fn = fname_by_year[year]
            geojson_cache[year] = fetch_geojson(fn)
        features = geojson_cache[year]["features"]

        # Dedup within this period: several region markers can fall inside
        # the same polity (e.g. three Roman cities all inside "Roman
        # Empire"), in which case the border should be drawn once, labeled
        # once, and list every region marker it covers -- not repeated
        # per-marker.
        territories: dict[str, dict] = {}  # polity_name -> {polity_name, year, path, region_names}
        for region in period["regions"]:
            feature = find_containing_feature(region["lng"], region["lat"], features)
            name = None
            if feature is not None:
                name = feature["properties"].get("NAME") or feature["properties"].get("ABBREVN")
            if feature is None or not name:
                unmatched += 1
                continue
            matched += 1
            if name not in territories:
                path, label = geometry_to_path_and_label(feature["geometry"])
                territories[name] = {
                    "polity_name": name,
                    "year": year,
                    "path": path,
                    "label_x": label[0] if label else None,
                    "label_y": label[1] if label else None,
                    "region_names": [],
                }
            territories[name]["region_names"].append(region["name"])

        result[period["id"]] = list(territories.values())

    print(f"Matched {matched} / {matched + unmatched} region markers to a real, named historical polity.")

    # Build the frontend JS data file.
    js_lines = [
        "// Real historical political-border overlays for the History Atlas, one per",
        "// region marker (where a containing polity was found for that era).",
        "//",
        "// Source: aourednik/historical-basemaps (GPL-3.0)",
        "// https://github.com/aourednik/historical-basemaps",
        "// Historical boundaries are approximate and the subject of ongoing",
        "// scholarly debate for many regions/eras; treat as illustrative, not",
        "// authoritative, consistent with that project's own disclaimer.",
        "//",
        "// Generated by backend/scripts/build_historical_borders.py -- do not",
        "// hand-edit; re-run the script instead.",
        "",
        "export const HISTORICAL_BORDERS = " + json.dumps(result, ensure_ascii=False, separators=(",", ":")) + ";",
        "",
    ]
    FRONTEND_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    FRONTEND_OUT_PATH.write_text("\n".join(js_lines), encoding="utf-8")
    print(f"Wrote {FRONTEND_OUT_PATH} ({FRONTEND_OUT_PATH.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
