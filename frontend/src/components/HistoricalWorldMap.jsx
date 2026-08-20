import React, { useEffect, useState, useMemo } from 'react';
import { MAP_WIDTH, MAP_HEIGHT, project } from '../utils/mapProjection.js';

// A second, historical locator map: the same schematic (graticule, not
// coastlines) approach as the current-day World Map, but plotting the major
// civilizations/empires of a chosen historical era at their real approximate
// capital coordinates — paired with that era's key events and links to real,
// famous historical maps.

export default function HistoricalWorldMap() {
  const [periods, setPeriods] = useState([]);
  const [periodId, setPeriodId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeRegion, setActiveRegion] = useState(null);

  useEffect(() => {
    fetch('/api/historical-map')
      .then((r) => r.json())
      .then((d) => {
        const list = d.periods || [];
        setPeriods(list);
        if (list.length > 0) setPeriodId(list[0].id);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const period = useMemo(() => periods.find((p) => p.id === periodId) || null, [periods, periodId]);

  if (loading) {
    return <div className="rounded-xl border p-6 text-center text-sm text-gray-400">Loading historical map…</div>;
  }
  if (!period) return null;

  return (
    <div className="space-y-3">
      <div className="rounded-xl bg-gradient-to-r from-amber-600 to-orange-500 p-4 text-white">
        <h2 className="text-xl font-bold">🕰️ World History Atlas</h2>
        <p className="text-sm opacity-90">From ancient times to today — explore how the map of the world changed, era by era.</p>
      </div>

      <label className="block text-sm font-medium" htmlFor="historical-period-select">
        Choose a time period
      </label>
      <select
        id="historical-period-select"
        value={period.id}
        onChange={(e) => { setPeriodId(e.target.value); setActiveRegion(null); }}
        className="w-full rounded-lg border px-3 py-2 dark:bg-gray-800"
      >
        {periods.map((p) => (
          <option key={p.id} value={p.id}>
            {p.emoji} {p.label} ({p.years})
          </option>
        ))}
      </select>

      <div className="rounded-xl border overflow-hidden">
        <div className="bg-amber-50 dark:bg-amber-950 border-b px-4 py-3">
          <p className="font-bold">{period.emoji} {period.label} <span className="font-normal text-sm text-gray-500">— {period.years}</span></p>
          <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{period.description}</p>
        </div>

        <div className="bg-amber-50/60 dark:bg-slate-900">
          <svg viewBox={`0 0 ${MAP_WIDTH} ${MAP_HEIGHT}`} className="w-full h-auto select-none" role="img" aria-label={`Map of major civilizations during: ${period.label}`}>
            <rect x="0" y="0" width={MAP_WIDTH} height={MAP_HEIGHT} className="fill-amber-50 dark:fill-slate-800" />
            {[-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150].map((lng) => {
              const { x } = project(0, lng);
              return <line key={lng} x1={x} y1={0} x2={x} y2={MAP_HEIGHT} className="stroke-amber-200 dark:stroke-slate-700" strokeWidth="1" />;
            })}
            {[-60, -30, 0, 30, 60].map((lat) => {
              const { y } = project(lat, 0);
              return <line key={lat} x1={0} y1={y} x2={MAP_WIDTH} y2={y} className={lat === 0 ? 'stroke-amber-300 dark:stroke-slate-600' : 'stroke-amber-200 dark:stroke-slate-700'} strokeWidth={lat === 0 ? 1.5 : 1} />;
            })}
            <rect x="0" y="0" width={MAP_WIDTH} height={MAP_HEIGHT} fill="none" className="stroke-amber-300 dark:stroke-slate-600" strokeWidth="1.5" />
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
        <p className="text-[11px] text-gray-400 text-center py-1">
          A schematic locator map (latitude/longitude grid, not political borders) — tap a marker for details.
        </p>

        {activeRegion && (
          <div className="border-t px-4 py-3 bg-amber-50 dark:bg-amber-950/40">
            {(() => {
              const r = period.regions.find((x) => x.name === activeRegion);
              return (
                <>
                  <p className="font-semibold text-sm">{r.name}</p>
                  <p className="text-sm text-gray-600 dark:text-gray-300">{r.note}</p>
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
      </div>
    </div>
  );
}
