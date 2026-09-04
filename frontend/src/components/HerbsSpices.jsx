import React, { useState, useEffect, useRef } from 'react';

const CATEGORY_LABELS = { herb: 'Herb', spice: 'Spice', spice_blend: 'Spice Blend' };

const thumbCache = {};
function HerbThumbnail({ wikiTitle }) {
  const [src, setSrc] = useState(thumbCache[wikiTitle] || null);
  const mounted = useRef(true);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; }; }, []);
  useEffect(() => {
    if (!wikiTitle || (thumbCache[wikiTitle] && thumbCache[wikiTitle] !== 'loading')) {
      if (thumbCache[wikiTitle]) setSrc(thumbCache[wikiTitle]);
      return;
    }
    thumbCache[wikiTitle] = 'loading';
    fetch(`/api/cuisine/thumbnail?wiki_title=${encodeURIComponent(wikiTitle)}`)
      .then(r => (r.ok ? r.json() : null))
      .then(d => {
        const url = d?.thumbnail_url ?? null;
        thumbCache[wikiTitle] = url || '';
        if (mounted.current && url) setSrc(url);
      })
      .catch(() => { thumbCache[wikiTitle] = ''; });
  }, [wikiTitle]);

  return (
    <div className="h-32 rounded-t-xl overflow-hidden bg-gradient-to-br from-green-200 to-lime-100 dark:from-green-900 dark:to-lime-950 flex items-center justify-center">
      {src ? <img src={src} alt="" className="w-full h-full object-cover" onError={() => setSrc('')} /> : <span className="text-4xl opacity-70">🌿</span>}
    </div>
  );
}

export default function HerbsSpices() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');

  useEffect(() => {
    fetch('/api/cuisine-detail/herbs-spices').then(r => r.json()).then(setData).catch(e => setError(e.message));
  }, []);

  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Herbs &amp; Spices</p><p className="text-sm mt-1">{error}</p>
    </div>
  );
  if (!data) return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">{[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-lime-600 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}</div>
    </div>
  );

  const items = (data.items || []).filter(item =>
    (!category || item.category === category) &&
    (!search || item.name.toLowerCase().includes(search.toLowerCase()))
  );

  return (
    <div className="space-y-5">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: 'linear-gradient(135deg, #65a30d, #4d7c0f)' }}>
        <h1 className="text-3xl font-extrabold drop-shadow-lg">🌿 {data.title}</h1>
        <p className="text-white/90 text-base mt-1 max-w-2xl">{data.description}</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <input type="text" value={search} onChange={e => setSearch(e.target.value)} placeholder="Search herbs & spices..."
          className="flex-1 min-w-[200px] rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-lime-400 dark:text-white" />
        <select value={category} onChange={e => setCategory(e.target.value)}
          className="rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 px-4 py-2 text-sm dark:text-white">
          <option value="">All Types</option>
          <option value="herb">Herbs</option>
          <option value="spice">Spices</option>
          <option value="spice_blend">Spice Blends</option>
        </select>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
        {items.map((item, i) => (
          <div key={i} className="rounded-xl border-2 border-lime-200 dark:border-lime-800 bg-white dark:bg-gray-800 shadow-sm overflow-hidden">
            <HerbThumbnail wikiTitle={item.wiki_title} />
            <div className="p-3">
              <div className="flex items-center justify-between gap-2">
                <p className="font-bold text-gray-800 dark:text-gray-100 text-sm">{item.name}</p>
                <span className="text-[10px] rounded-full px-2 py-0.5 font-semibold bg-lime-100 text-lime-700 dark:bg-lime-900 dark:text-lime-300 whitespace-nowrap">{CATEGORY_LABELS[item.category] || item.category}</span>
              </div>
              <p className="text-xs text-gray-600 dark:text-gray-300 mt-1.5 line-clamp-3">{item.description}</p>
              {item.uses?.length > 0 && (
                <div className="mt-2">
                  <p className="text-[10px] font-bold text-gray-400 uppercase tracking-wide">Common Uses</p>
                  <div className="flex flex-wrap gap-1 mt-1">
                    {item.uses.slice(0, 3).map((u, ui) => (
                      <span key={ui} className="text-[10px] rounded-full px-2 py-0.5 bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300">{u}</span>
                    ))}
                  </div>
                </div>
              )}
              {item.alternatives?.length > 0 && (
                <p className="text-[11px] text-gray-500 dark:text-gray-400 mt-2">🔄 <span className="font-medium">Alt:</span> {item.alternatives.join(', ')}</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
