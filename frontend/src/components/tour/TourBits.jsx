import React, { useEffect, useState } from 'react';

export const PLACE_TYPES = {
  attraction: { label: 'Tourist attractions', short: 'Attraction', emoji: '📍', badge: 'bg-amber-100 text-amber-800 border-amber-200' },
  nature: { label: 'Natural wonders', short: 'Natural wonder', emoji: '🌿', badge: 'bg-green-100 text-green-800 border-green-200' },
  museum: { label: 'Museums', short: 'Museum', emoji: '🏛️', badge: 'bg-purple-100 text-purple-800 border-purple-200' },
  architecture: { label: 'Architecture', short: 'Architecture', emoji: '🏰', badge: 'bg-sky-100 text-sky-800 border-sky-200' },
};

const CHIP_COLORS = {
  video: 'bg-red-50 text-red-700 border-red-200 hover:bg-red-100',
  blog: 'bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100',
  photos: 'bg-green-50 text-green-700 border-green-200 hover:bg-green-100',
  map: 'bg-gray-50 text-gray-700 border-gray-200 hover:bg-gray-100',
  earth: 'bg-indigo-50 text-indigo-700 border-indigo-200 hover:bg-indigo-100',
  hotels: 'bg-orange-50 text-orange-700 border-orange-200 hover:bg-orange-100',
  route: 'bg-teal-50 text-teal-700 border-teal-200 hover:bg-teal-100',
};

export function LinkChip({ href, kind, icon, children }) {
  if (!href) return null;
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className={`inline-flex items-center gap-1 rounded-full border px-2.5 py-1 text-xs font-medium transition-colors ${CHIP_COLORS[kind] || CHIP_COLORS.map}`}
    >
      <span aria-hidden="true">{icon}</span>
      {children}
    </a>
  );
}

const thumbCache = {};

// Photo for a place: Wikipedia lead image by name, else a Commons search
// (resolved and cached server-side by GET /api/museum/thumbnail).
export function PlaceThumbnail({ name, country, type }) {
  const key = `${name}|${country}`;
  const [src, setSrc] = useState(thumbCache[key] || null);

  useEffect(() => {
    if (thumbCache[key] !== undefined) { setSrc(thumbCache[key] || null); return undefined; }
    let active = true;
    const params = new URLSearchParams({ wiki_title: name, q: `${name} ${country}` });
    fetch(`/api/museum/thumbnail?${params}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        const url = d?.thumbnail_url || '';
        thumbCache[key] = url;
        if (active) setSrc(url || null);
      })
      .catch(() => { thumbCache[key] = ''; });
    return () => { active = false; };
  }, [key, name, country]);

  const emoji = PLACE_TYPES[type]?.emoji || '📍';
  return (
    <div className="flex h-28 w-full items-center justify-center overflow-hidden rounded-t-xl bg-gradient-to-br from-sky-100 to-indigo-100 dark:from-slate-700 dark:to-slate-800">
      {src
        ? <img src={src} alt="" loading="lazy" className="h-full w-full object-cover" onError={() => setSrc(null)} />
        : <span className="text-4xl opacity-70" aria-hidden="true">{emoji}</span>}
    </div>
  );
}

export function PlaceCard({ place, country }) {
  const meta = PLACE_TYPES[place.type] || PLACE_TYPES.attraction;
  const links = place.links || {};
  return (
    <li className="overflow-hidden rounded-xl border bg-white shadow-sm dark:border-gray-700 dark:bg-gray-900">
      <PlaceThumbnail name={place.name} country={country} type={place.type} />
      <div className="space-y-2 p-3">
        <div>
          <h4 className="font-semibold leading-tight">{place.name}</h4>
          <span className={`mt-1 inline-block rounded-full border px-2 py-0.5 text-[11px] ${meta.badge}`}>{meta.emoji} {meta.short}</span>
        </div>
        <div className="flex flex-wrap gap-1.5">
          <LinkChip href={links.video} kind="video" icon="▶">Video</LinkChip>
          <LinkChip href={links.blog} kind="blog" icon="📝">Blog</LinkChip>
          <LinkChip href={links.photos} kind="photos" icon="📷">Photos</LinkChip>
          <LinkChip href={links.map} kind="map" icon="🗺️">Map</LinkChip>
          <LinkChip href={links.earth} kind="earth" icon="🌐">3D</LinkChip>
        </div>
      </div>
    </li>
  );
}

export function CityCard({ city }) {
  const links = city.links || {};
  return (
    <li className="space-y-2 rounded-xl border bg-white p-3 shadow-sm dark:border-gray-700 dark:bg-gray-900">
      <h4 className="font-semibold">
        🏙️ {city.name}
        {city.is_capital && <span className="ml-2 rounded-full bg-blue-100 px-2 py-0.5 text-[11px] font-medium text-blue-700">Capital</span>}
      </h4>
      <div className="flex flex-wrap gap-1.5">
        <LinkChip href={links.earth_3d} kind="earth" icon="🌐">3D city tour (Google Earth)</LinkChip>
        <LinkChip href={links.map} kind="map" icon="🗺️">Google Maps</LinkChip>
        <LinkChip href={links.video} kind="video" icon="▶">Walking tour video</LinkChip>
        <LinkChip href={links.blog} kind="blog" icon="📝">City guide blog</LinkChip>
        <LinkChip href={links.photos} kind="photos" icon="📷">Photos</LinkChip>
        <LinkChip href={links.hotels} kind="hotels" icon="🏨">Hotels</LinkChip>
      </div>
    </li>
  );
}

const KIND_ICON = { coastal: '🌊', mountain: '⛰️', desert: '🏜️', 'cross-country': '🛣️', scenic: '🏞️', historic: '🏛️', island: '🏝️', arctic: '❄️', safari: '🦁', outback: '🦘' };

export function RoadTripCard({ trip }) {
  const links = trip.links || {};
  return (
    <li className="space-y-2 rounded-xl border bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-900">
      <div className="flex flex-wrap items-start justify-between gap-2">
        <div>
          <h4 className="text-base font-semibold">🚗 {trip.name}</h4>
          <p className="text-xs text-gray-500">{trip.country_names.join(' · ')}</p>
        </div>
        <span className="rounded-full border bg-gray-50 px-2 py-0.5 text-[11px] capitalize text-gray-600 dark:bg-gray-800 dark:text-gray-300">
          {KIND_ICON[trip.kind] || '🛣️'} {trip.kind}
        </span>
      </div>
      <p className="text-sm font-medium">
        {trip.start}{trip.end !== trip.start ? ` → ${trip.end}` : ' (loop)'}
      </p>
      <dl className="grid grid-cols-3 gap-2 text-xs">
        <div><dt className="text-gray-500">Distance</dt><dd className="font-semibold">about {trip.km.toLocaleString()} km</dd></div>
        <div><dt className="text-gray-500">Time</dt><dd className="font-semibold">{trip.duration}</dd></div>
        <div><dt className="text-gray-500">Best time</dt><dd className="font-semibold">{trip.best_time}</dd></div>
      </dl>
      <p className="text-sm text-gray-700 dark:text-gray-300">{trip.summary}</p>
      <div className="flex flex-wrap gap-1">
        {trip.highlights.map((h) => (
          <span key={h} className="rounded-full border border-amber-200 bg-amber-50 px-2 py-0.5 text-[11px] text-amber-800">{h}</span>
        ))}
      </div>
      <p className="rounded-lg bg-yellow-50 p-2 text-xs text-yellow-900 dark:bg-yellow-950 dark:text-yellow-200">💡 {trip.tip}</p>
      <div className="flex flex-wrap gap-1.5">
        <LinkChip href={links.route} kind="route" icon="🧭">Route in Google Maps</LinkChip>
        <LinkChip href={links.video} kind="video" icon="▶">Drive video</LinkChip>
        <LinkChip href={links.blog} kind="blog" icon="📝">Blog</LinkChip>
        <LinkChip href={links.photos} kind="photos" icon="📷">Photos</LinkChip>
        <LinkChip href={links.earth} kind="earth" icon="🌐">Start in 3D</LinkChip>
      </div>
    </li>
  );
}
