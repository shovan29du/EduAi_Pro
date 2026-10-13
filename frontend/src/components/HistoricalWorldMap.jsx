import React, { useEffect, useState, useMemo } from 'react';
import { MAP_WIDTH, MAP_HEIGHT, project } from '../utils/mapProjection.js';
import { WORLD_LAND_PATH } from '../utils/worldLandPath.js';
import { HISTORICAL_BORDERS } from '../utils/historicalBorders.js';

// A collection of historical locator maps — one per century, browsed as a
// gallery. Each map uses real (modern) continent outlines plus a lat/long
// graticule as its base, the same approach as the current-day World Map,
// plotting the major civilizations/empires of that century at their real
// approximate capital coordinates — paired with that century's key events
// and links to real, famous historical maps where one genuinely exists for
// that era.
//
// Where available, each marker is also overlaid with the real historical
// political border and era-appropriate name of the polity that actually
// held that territory at the time, sourced from the open
// aourednik/historical-basemaps dataset (GPL-3.0) -- see the attribution
// footer. Not every marker has a matching border: some regions in this
// era genuinely weren't organized into a bordered polity (e.g. mobile or
// stateless societies), and a few are gaps in that source dataset; in both
// cases we show no border rather than inventing one.

// Deterministic color per polity name, so the same polity always reads as
// the same color across the few periods it might reappear in, and
// different polities shown together are visually distinguishable.
const BORDER_COLORS = [
  '#b45309', '#15803d', '#1d4ed8', '#7e22ce', '#be123c',
  '#0f766e', '#a16207', '#4338ca', '#c2410c', '#0369a1',
];
function borderColor(name) {
  let hash = 0;
  for (const c of name) hash = (hash * 31 + c.charCodeAt(0)) >>> 0;
  return BORDER_COLORS[hash % BORDER_COLORS.length];
}

function PeriodCard({ period, onOpen }) {
  return (
    <button
      onClick={() => onOpen(period.id)}
      className="text-left rounded-xl border-2 border-amber-200 dark:border-amber-800 bg-gradient-to-br from-amber-50 to-orange-50 dark:from-gray-800 dark:to-gray-900 p-4 hover:shadow-lg transition-shadow"
    >
      <p className="text-3xl mb-1">{period.emoji}</p>
      <p className="font-bold text-gray-800 dark:text-gray-100 leading-snug">{period.label}</p>
      <p className="text-xs text-amber-700 dark:text-amber-400 font-medium mt-0.5">{period.years}</p>
      <p className="text-xs text-gray-500 dark:text-gray-400 mt-2 line-clamp-2">{period.description}</p>
      <p className="text-[11px] text-gray-400 mt-2">
        {period.regions?.length || 0} civilizations · {period.events?.length || 0} events
        {period.famous_maps?.length > 0 ? ` · ${period.famous_maps.length} famous map${period.famous_maps.length > 1 ? 's' : ''}` : ''}
      </p>
    </button>
  );
}

function PeriodDetail({ period, periods, onSelectPeriod, onBack }) {
  const [activeRegion, setActiveRegion] = useState(null);
  const borders = HISTORICAL_BORDERS[period.id] || [];

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between gap-2">
        <button onClick={onBack} className="text-sm text-amber-700 dark:text-amber-400 hover:underline">
          ← All Centuries
        </button>
        <select
          aria-label="Jump to a different time period"
          value={period.id}
          onChange={(e) => { onSelectPeriod(e.target.value); setActiveRegion(null); }}
          className="rounded-lg border px-2 py-1 text-sm dark:bg-gray-800"
        >
          {periods.map((p) => (
            <option key={p.id} value={p.id}>{p.emoji} {p.label} ({p.years})</option>
          ))}
        </select>
      </div>

      <div className="rounded-xl border-2 border-amber-300 dark:border-slate-600 overflow-hidden">
        <div className="bg-amber-50 dark:bg-amber-950 border-b px-4 py-3">
          <p className="font-bold">{period.emoji} {period.label} <span className="font-normal text-sm text-gray-500">— {period.years}</span></p>
          <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{period.description}</p>
        </div>

        <div className="bg-amber-50/60 dark:bg-slate-900">
          <svg viewBox={`0 0 ${MAP_WIDTH} ${MAP_HEIGHT}`} className="w-full h-auto select-none" role="img" aria-label={`Map of major civilizations during: ${period.label}`}>
            <rect x="0" y="0" width={MAP_WIDTH} height={MAP_HEIGHT} className="fill-amber-50 dark:fill-slate-800" />
            <path d={WORLD_LAND_PATH} className="fill-amber-200/80 dark:fill-slate-700 stroke-amber-400 dark:stroke-slate-500" strokeWidth="0.75" />
            {[-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150].map((lng) => {
              const { x } = project(0, lng);
              return <line key={lng} x1={x} y1={0} x2={x} y2={MAP_HEIGHT} className="stroke-amber-200 dark:stroke-slate-700" strokeWidth="1" />;
            })}
            {[-60, -30, 0, 30, 60].map((lat) => {
              const { y } = project(lat, 0);
              return <line key={lat} x1={0} y1={y} x2={MAP_WIDTH} y2={y} className={lat === 0 ? 'stroke-amber-300 dark:stroke-slate-600' : 'stroke-amber-200 dark:stroke-slate-700'} strokeWidth={lat === 0 ? 1.5 : 1} />;
            })}
            <rect x="0" y="0" width={MAP_WIDTH} height={MAP_HEIGHT} fill="none" className="stroke-amber-300 dark:stroke-slate-600" strokeWidth="1.5" />
            {borders.map((b) => {
              const color = borderColor(b.polity_name);
              return (
                <g key={b.polity_name}>
                  <path d={b.path} fill={color} fillOpacity={0.14} stroke={color} strokeWidth="1.5" strokeDasharray="3 2" />
                  {b.label_x != null && (
                    <text
                      x={b.label_x}
                      y={b.label_y}
                      fontSize="9"
                      fontWeight="600"
                      textAnchor="middle"
                      fill={color}
                      style={{ paintOrder: 'stroke', stroke: 'white', strokeWidth: 2.5 }}
                    >
                      {b.polity_name}
                    </text>
                  )}
                </g>
              );
            })}
            {period.regions.map((r) => {
              const { x, y } = project(r.lat, r.lng);
              const isActive = activeRegion === r.name;
              return (
                <g key={r.name} transform={`translate(${x}, ${y})`} onClick={() => setActiveRegion(isActive ? null : r.name)} className="cursor-pointer">
                  <circle r={isActive ? 6 : 4.5} className="fill-amber-600" stroke="white" strokeWidth="1" />
                  <text x="7" y="3" fontSize="11" className="fill-amber-900 dark:fill-amber-200" style={{ paintOrder: 'stroke', stroke: 'white', strokeWidth: 3 }}>
                    {r.name.split('(')[0].trim()}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>
        <p className="text-[11px] text-gray-400 text-center py-1 px-2">
          Today's coastlines, with real historical political borders where available (dashed, from{' '}
          <a href="https://github.com/aourednik/historical-basemaps" target="_blank" rel="noopener noreferrer" className="underline">
            historical-basemaps
          </a>
          , GPL-3.0) — tap a marker for details.
        </p>

        {activeRegion && (
          <div className="border-t px-4 py-3 bg-amber-50 dark:bg-amber-950/40">
            {(() => {
              const r = period.regions.find((x) => x.name === activeRegion);
              const border = borders.find((b) => b.region_names.includes(r.name));
              return (
                <>
                  <p className="font-semibold text-sm">{r.name}</p>
                  {border && (
                    <p className="text-xs text-amber-700 dark:text-amber-400 mt-0.5">
                      Known in this era as: <span className="font-semibold">{border.polity_name}</span>
                    </p>
                  )}
                  <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{r.note}</p>
                  {r.description && (
                    <p className="text-sm text-gray-600 dark:text-gray-300 mt-2">{r.description}</p>
                  )}
                </>
              );
            })()}
          </div>
        )}

        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-2">📜 Key Events</p>
          <ul className="space-y-1.5">
            {period.events.map((ev) => (
              <li key={ev.year + ev.event} className="text-sm flex gap-2">
                <span className="shrink-0 font-semibold text-amber-700 dark:text-amber-400 w-32">{ev.year}</span>
                <span className="text-gray-600 dark:text-gray-300">{ev.event}</span>
              </li>
            ))}
          </ul>
        </div>

        {period.famous_maps?.length > 0 && (
          <div className="border-t px-4 py-4">
            <p className="text-sm font-semibold mb-3">🗺️ Famous Maps of This Era</p>
            <div className="grid gap-2 sm:grid-cols-2">
              {period.famous_maps.map((m) => (
                <a
                  key={m.name}
                  href={m.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="rounded-lg border px-3 py-2 hover:bg-amber-50 dark:hover:bg-amber-950/40 transition-colors"
                >
                  <p className="text-sm font-semibold text-amber-700 dark:text-amber-400">
                    {m.name} <span className="ml-1 opacity-50 text-xs">↗</span>
                  </p>
                  <p className="text-xs text-gray-400">{m.year}</p>
                  <p className="text-xs text-gray-600 dark:text-gray-300 mt-1">{m.description}</p>
                </a>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default function HistoricalWorldMap() {
  const [periods, setPeriods] = useState([]);
  const [periodId, setPeriodId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetch('/api/historical-map')
      .then((r) => r.json())
      .then((d) => {
        setPeriods(d.periods || []);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const period = useMemo(() => periods.find((p) => p.id === periodId) || null, [periods, periodId]);

  const filtered = useMemo(() => {
    const q = search.trim().toLowerCase();
    if (!q) return periods;
    return periods.filter((p) => p.label.toLowerCase().includes(q) || p.years.toLowerCase().includes(q));
  }, [periods, search]);

  if (loading) {
    return <div className="rounded-xl border p-6 text-center text-sm text-gray-400">Loading historical maps…</div>;
  }

  return (
    <div className="space-y-4">
      <div className="rounded-xl bg-gradient-to-r from-amber-600 to-orange-500 p-4 text-white">
        <h1 className="text-xl font-bold">🕰️ World History Atlas</h1>
        <p className="text-sm opacity-90">A collection of {periods.length} world maps, one per century, from ancient times to today.</p>
      </div>

      {period ? (
        <PeriodDetail period={period} periods={periods} onSelectPeriod={setPeriodId} onBack={() => setPeriodId(null)} />
      ) : (
        <>
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by era or year, e.g. 'Rome' or '1500'…"
            aria-label="Search historical periods"
            className="w-full rounded-lg border px-3 py-2 dark:bg-gray-800"
          />
          <p className="text-xs text-gray-500">{filtered.length} time period{filtered.length !== 1 ? 's' : ''}</p>
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {filtered.map((p) => (
              <PeriodCard key={p.id} period={p} onOpen={setPeriodId} />
            ))}
          </div>
          {filtered.length === 0 && (
            <p className="text-center text-gray-500 py-8">No time periods match your search.</p>
          )}
        </>
      )}
    </div>
  );
}
