import React, { useState, useEffect } from 'react';

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
              <div key={i} className="rounded-xl border-2 border-teal-200 dark:border-teal-800 bg-white dark:bg-gray-800 p-4 shadow-sm">
                <p className="font-bold text-teal-700 dark:text-teal-300">{t.name}</p>
                <p className="text-sm text-gray-600 dark:text-gray-300 mt-1.5 leading-relaxed">{t.description}</p>
                {t.example_dishes?.length > 0 && (
                  <div className="flex flex-wrap gap-1.5 mt-3">
                    {t.example_dishes.map((d, di) => (
                      <span key={di} className="text-[11px] rounded-full px-2.5 py-0.5 font-medium bg-teal-100 text-teal-700 dark:bg-teal-900 dark:text-teal-300">{d}</span>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
