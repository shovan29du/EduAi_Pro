import React, { useState, useEffect, useRef } from 'react';

const thumbCache = {};
function TechniqueThumbnail({ wikiTitle }) {
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
    <div className="h-28 rounded-t-xl overflow-hidden bg-gradient-to-br from-teal-200 to-cyan-100 dark:from-teal-900 dark:to-cyan-950 flex items-center justify-center">
      {src ? <img src={src} alt="" className="w-full h-full object-cover" onError={() => setSrc('')} /> : <span className="text-4xl opacity-70">🔥</span>}
    </div>
  );
}

export default function CookingTechniques() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/cuisine-detail/techniques').then(r => r.json()).then(setData).catch(e => setError(e.message));
  }, []);

  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Cooking Techniques</p><p className="text-sm mt-1">{error}</p>
    </div>
  );
  if (!data) return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">{[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-teal-500 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}</div>
    </div>
  );

  return (
    <div className="space-y-6">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: 'linear-gradient(135deg, #0d9488, #0f766e)' }}>
        <h1 className="text-3xl font-extrabold drop-shadow-lg">🔥 {data.title}</h1>
        <p className="text-white/90 text-base mt-1 max-w-2xl">{data.description}</p>
      </div>

      {data.categories?.map(cat => (
        <div key={cat.id}>
          <h2 className="text-xl font-bold text-gray-700 dark:text-gray-200 mb-3 flex items-center gap-2">
            <span className="text-2xl">{cat.emoji}</span> {cat.label}
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {cat.techniques.map((t, i) => (
              <div key={i} className="rounded-xl border-2 border-teal-200 dark:border-teal-800 bg-white dark:bg-gray-800 shadow-sm overflow-hidden">
                <TechniqueThumbnail wikiTitle={t.links?.picture_wiki_title} />
                <div className="p-4">
                  <p className="font-bold text-teal-700 dark:text-teal-300">{t.name}</p>
                  <p className="text-sm text-gray-600 dark:text-gray-300 mt-1.5 leading-relaxed">{t.description}</p>
                  {t.example_dishes?.length > 0 && (
                    <div className="flex flex-wrap gap-1.5 mt-3">
                      {t.example_dishes.map((d, di) => (
                        <span key={di} className="text-[11px] rounded-full px-2.5 py-0.5 font-medium bg-teal-100 text-teal-700 dark:bg-teal-900 dark:text-teal-300">{d}</span>
                      ))}
                    </div>
                  )}
                  {t.related_recipes?.length > 0 && (
                    <div className="mt-3">
                      <p className="text-[10px] font-bold text-gray-400 uppercase tracking-wide">Recipes Using This</p>
                      <div className="flex flex-wrap gap-1.5 mt-1">
                        {t.related_recipes.map(r => (
                          <span key={r.id} className="text-[11px] rounded-full px-2.5 py-0.5 font-medium bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300">{r.name}</span>
                        ))}
                      </div>
                    </div>
                  )}
                  {t.links && (
                    <div className="flex flex-wrap gap-2 mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                      <a href={t.links.video} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full border text-[11px] font-medium bg-red-100 text-red-700 border-red-200 hover:opacity-80">▶ Video</a>
                      <a href={t.links.text_guide} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full border text-[11px] font-medium bg-indigo-100 text-indigo-700 border-indigo-200 hover:opacity-80">📖 Guide</a>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
