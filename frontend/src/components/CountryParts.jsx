import React from 'react';
import { MAP_WIDTH, MAP_HEIGHT, project } from '../utils/mapProjection.js';
import { WORLD_LAND_PATH } from '../utils/worldLandPath.js';
import { WORLD_COUNTRY_BORDERS } from '../utils/worldCountryBorders.js';

// Pin colours per continent for the World Map view.
export const CONTINENT_COLOR = {
  Africa: '#f59e0b',
  Asia: '#ef4444',
  Europe: '#3b82f6',
  'North America': '#10b981',
  'South America': '#a855f7',
  Oceania: '#06b6d4',
  Antarctica: '#94a3b8',
};

// The full country profile (the former Countries Explorer detail page).
export function CountryProfile({ country: c }) {
  return (
    <div className="rounded-xl overflow-hidden border shadow">
      <div className="bg-gradient-to-r from-blue-600 to-cyan-500 p-6 text-white text-center">
        <div className="text-6xl mb-2">{c.flag_emoji}</div>
        {c.flag_url && (
          <img src={c.flag_url} alt={`Flag of ${c.name}`} className="mx-auto h-16 rounded shadow mt-2" onError={(e) => { e.target.style.display = 'none'; }} />
        )}
        <h2 className="text-2xl font-bold mt-2">{c.name}</h2>
        <p className="opacity-90">{c.continent}</p>
      </div>
      <div className="p-4 grid gap-3 sm:grid-cols-2">
        <Fact label="🏛 Capital" value={c.capital} />
        <Fact label="👥 Population" value={c.population ? Number(c.population).toLocaleString() : '—'} />
        <Fact label="💰 Currency" value={c.currency} />
        <Fact label="🗣 Language" value={c.language} />
        <Fact label="🌍 Continent" value={c.continent} />
        {c.area_km2 && <Fact label="📐 Area" value={`${Number(c.area_km2).toLocaleString()} km²`} />}
        {c.climate && <Fact label="🌤 Climate" value={c.climate} />}
        {c.geography && <Fact label="🗺 Geography" value={c.geography} />}
      </div>
      {c.greeting && (
        <div className="border-t px-4 py-3 bg-blue-50 dark:bg-blue-900/20">
          <p className="text-sm font-medium text-blue-600">Greeting in {c.language}:</p>
          <p className="text-sm italic">"{c.greeting}"</p>
        </div>
      )}
      {c.culture && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-1">🎭 Culture</p>
          <p className="text-sm text-gray-600 dark:text-gray-300">{c.culture}</p>
        </div>
      )}
      {c.landmarks?.length > 0 && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-2">🗼 Major Landmarks</p>
          <div className="flex flex-wrap gap-1">
            {c.landmarks.map(l => <span key={l} className="text-xs px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-200">{l}</span>)}
          </div>
        </div>
      )}
      {c.unesco_sites?.length > 0 && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-2">🏆 UNESCO World Heritage Sites</p>
          <div className="flex flex-wrap gap-1">
            {c.unesco_sites.map(s => <span key={s} className="text-xs px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-800 border border-indigo-200">{s}</span>)}
          </div>
        </div>
      )}
      {c.wildlife?.length > 0 && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-2">🦁 Wildlife</p>
          <div className="flex flex-wrap gap-1">
            {c.wildlife.map(w => <span key={w} className="text-xs px-2 py-0.5 rounded-full bg-green-100 text-green-800 border border-green-200">{w}</span>)}
          </div>
        </div>
      )}
      {c.foods?.length > 0 && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-2">🍽 Traditional Foods</p>
          <div className="flex flex-wrap gap-1">
            {c.foods.map(f => <span key={f} className="text-xs px-2 py-0.5 rounded-full bg-orange-100 text-orange-800 border border-orange-200">{f}</span>)}
          </div>
        </div>
      )}
      {c.festivals?.length > 0 && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-semibold mb-2">🎉 Festivals & Celebrations</p>
          <div className="flex flex-wrap gap-1">
            {c.festivals.map(f => <span key={f} className="text-xs px-2 py-0.5 rounded-full bg-pink-100 text-pink-800 border border-pink-200">{f}</span>)}
          </div>
        </div>
      )}
      {c.fun_fact && (
        <div className="border-t px-4 py-3">
          <p className="text-sm font-medium">💡 Fun Fact</p>
          <p className="text-sm text-gray-600 dark:text-gray-300">{c.fun_fact}</p>
        </div>
      )}
      {c.links && (
        <div className="border-t px-4 py-4">
          <p className="text-sm font-semibold mb-3">🔗 Explore {c.name}</p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <LinkCard href={c.links.google_maps} icon="🗺️" label="Open in Google Maps" color="blue" />
            <LinkCard href={c.links.google_earth} icon="🌐" label="Open in Google Earth" color="green" />
            <LinkCard href={c.links.tourist_attraction_video} icon="🎬" label="Tourist Attraction Video" color="red" />
            <LinkCard href={c.links.video_overview} icon="▶" label="Country Documentary" color="red" />
            <LinkCard href={c.links.virtual_tour_video} icon="🌐" label="Virtual Tour (4K)" color="red" />
            <LinkCard href={c.links.text_wikipedia} icon="📖" label="Wikipedia" color="gray" />
            <LinkCard href={c.links.text_cia_factbook} icon="🏛" label="CIA World Factbook" color="blue" />
            <LinkCard href={c.links.text_britannica} icon="📚" label="Britannica" color="indigo" />
            <LinkCard href={c.links.resource_lonely_planet} icon="✈️" label="Lonely Planet Travel Guide" color="green" />
            <LinkCard href={c.links.resource_nat_geo} icon="🌍" label="National Geographic" color="amber" />
          </div>
        </div>
      )}
    </div>
  );
}

// A schematic, accurately-projected locator map (latitude/longitude graticule,
// not real coastlines) — every pin sits at its country's real capital-city
// coordinates. It's the index; the actual accurate map imagery comes from
// clicking through to the real Google Maps / Google Earth links.
export function WorldMap({ countries, pinCode, setPinCode, pinnedCountry, onOpenDetail }) {
  const meridians = [-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150];
  const parallels = [-60, -30, 0, 30, 60];

  return (
    <div className="space-y-2">
      <div className="rounded-xl border-2 border-sky-300 dark:border-slate-600 overflow-hidden bg-sky-50 dark:bg-slate-900">
        <svg viewBox={`0 0 ${MAP_WIDTH} ${MAP_HEIGHT}`} className="w-full h-auto select-none" role="img" aria-label="World map of country capitals">
          <rect x="0" y="0" width={MAP_WIDTH} height={MAP_HEIGHT} className="fill-sky-100 dark:fill-slate-800" />
          <path d={WORLD_LAND_PATH} className="fill-emerald-200/80 dark:fill-slate-700 stroke-emerald-500/70 dark:stroke-slate-500" strokeWidth="0.75" />
          {countries.map((c) => {
            const borderPath = WORLD_COUNTRY_BORDERS[c.code];
            if (!borderPath) return null;
            const isActive = pinCode === c.code;
            return (
              <path
                key={`border-${c.code}`}
                d={borderPath}
                fill={isActive ? (CONTINENT_COLOR[c.continent] || '#64748b') : 'none'}
                fillOpacity={isActive ? 0.25 : 0}
                className={isActive ? 'stroke-amber-500 dark:stroke-amber-400' : 'stroke-emerald-700/40 dark:stroke-slate-400/40'}
                strokeWidth={isActive ? 1.5 : 0.5}
                pointerEvents="none"
              />
            );
          })}
          {meridians.map((lng) => {
            const { x } = project(0, lng);
            return <line key={lng} x1={x} y1={0} x2={x} y2={MAP_HEIGHT} className="stroke-sky-200 dark:stroke-slate-700" strokeWidth="1" />;
          })}
          {parallels.map((lat) => {
            const { y } = project(lat, 0);
            return <line key={lat} x1={0} y1={y} x2={MAP_WIDTH} y2={y} className={lat === 0 ? 'stroke-sky-300 dark:stroke-slate-600' : 'stroke-sky-200 dark:stroke-slate-700'} strokeWidth={lat === 0 ? 1.5 : 1} />;
          })}
          <rect x="0" y="0" width={MAP_WIDTH} height={MAP_HEIGHT} fill="none" className="stroke-sky-300 dark:stroke-slate-600" strokeWidth="1.5" />
          {countries.map((c) => {
            const { x, y } = project(c.coordinates.lat, c.coordinates.lng);
            const isActive = pinCode === c.code;
            return (
              <g
                key={c.code}
                transform={`translate(${x}, ${y})`}
                onClick={() => setPinCode(isActive ? null : c.code)}
                className="cursor-pointer"
              >
                <circle r={isActive ? 6 : 4} fill={CONTINENT_COLOR[c.continent] || '#64748b'} stroke="white" strokeWidth="1" />
                {isActive && <circle r="10" fill="none" stroke={CONTINENT_COLOR[c.continent] || '#64748b'} strokeWidth="1.5" opacity="0.6" />}
              </g>
            );
          })}
        </svg>
      </div>
      <p className="text-[11px] text-gray-400 text-center">
        A schematic locator map with simplified political borders (about 30 of the smallest nations are too small to show as a separate shape at this scale) — pins mark each capital's real coordinates. Tap a pin, then open it in Google Maps or Google Earth for the real view.
      </p>

      {pinnedCountry && (
        <div className="rounded-xl border bg-white dark:bg-gray-900 p-4 flex flex-col sm:flex-row sm:items-center gap-3 shadow">
          <div className="flex items-center gap-3 flex-1 min-w-0">
            <span className="text-3xl">{pinnedCountry.flag_emoji}</span>
            <div className="min-w-0">
              <p className="font-semibold truncate">{pinnedCountry.name}</p>
              <p className="text-xs text-gray-500 truncate">{pinnedCountry.capital} · {pinnedCountry.continent}</p>
            </div>
          </div>
          <div className="flex flex-wrap gap-2">
            <LinkCard href={pinnedCountry.links?.google_maps} icon="🗺️" label="Google Maps" color="blue" />
            <LinkCard href={pinnedCountry.links?.google_earth} icon="🌐" label="Google Earth" color="green" />
            <button
              onClick={() => onOpenDetail(pinnedCountry.code)}
              className="flex items-center gap-2 px-3 py-2 rounded-lg border text-xs font-medium bg-gray-50 border-gray-200 text-gray-700 hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
            >
              🧭 Open Virtual Tour
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export function Fact({ label, value }) {
  return (
    <div className="rounded-lg bg-gray-50 p-3 dark:bg-gray-800">
      <p className="text-xs text-gray-500">{label}</p>
      <p className="font-semibold">{value || '—'}</p>
    </div>
  );
}

const COLOR_MAP = {
  red: 'bg-red-50 border-red-200 text-red-700 hover:bg-red-100',
  gray: 'bg-gray-50 border-gray-200 text-gray-700 hover:bg-gray-100',
  blue: 'bg-blue-50 border-blue-200 text-blue-700 hover:bg-blue-100',
  indigo: 'bg-indigo-50 border-indigo-200 text-indigo-700 hover:bg-indigo-100',
  green: 'bg-green-50 border-green-200 text-green-700 hover:bg-green-100',
  amber: 'bg-amber-50 border-amber-200 text-amber-700 hover:bg-amber-100',
};

export function LinkCard({ href, icon, label, color = 'gray' }) {
  if (!href) return null;
  return (
    <a href={href} target="_blank" rel="noopener noreferrer"
      className={`flex items-center gap-2 px-3 py-2 rounded-lg border text-xs font-medium transition-colors ${COLOR_MAP[color] || COLOR_MAP.gray}`}>
      <span>{icon}</span>
      <span className="truncate">{label}</span>
      <span className="ml-auto opacity-50">↗</span>
    </a>
  );
}
