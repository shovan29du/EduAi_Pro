import React, { useState, useEffect } from 'react';

export default function IngredientAlternatives() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/cuisine-detail/ingredient-alternatives').then(r => r.json()).then(setData).catch(e => setError(e.message));
  }, []);

  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Ingredient Alternatives</p><p className="text-sm mt-1">{error}</p>
    </div>
  );
  if (!data) return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">{[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-cyan-600 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}</div>
    </div>
  );

  return (
    <div className="space-y-6">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: 'linear-gradient(135deg, #0e7490, #155e75)' }}>
        <h1 className="text-3xl font-extrabold drop-shadow-lg">🔄 {data.title}</h1>
        <p className="text-white/90 text-base mt-1 max-w-2xl">{data.description}</p>
      </div>

      {data.categories?.map(cat => (
        <div key={cat.id}>
          <h2 className="text-xl font-bold text-gray-700 dark:text-gray-200 mb-3 flex items-center gap-2">
            <span className="text-2xl">{cat.emoji}</span> {cat.label}
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {cat.items.map((item, i) => (
              <div key={i} className={`rounded-xl border-2 p-4 bg-white dark:bg-gray-800 shadow-sm ${cat.id === 'halal_substitutes' ? 'border-emerald-200 dark:border-emerald-800' : 'border-cyan-200 dark:border-cyan-800'}`}>
                <p className="font-bold text-gray-800 dark:text-gray-100">{item.ingredient}</p>
                {item.alternatives?.length > 0 && (
                  <div className="flex flex-wrap gap-1.5 mt-2">
                    {item.alternatives.map((alt, ai) => (
                      <span key={ai} className={`text-xs rounded-full px-2.5 py-0.5 font-medium ${cat.id === 'halal_substitutes' ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900 dark:text-emerald-300' : 'bg-cyan-100 text-cyan-700 dark:bg-cyan-900 dark:text-cyan-300'}`}>→ {alt}</span>
                    ))}
                  </div>
                )}
                {item.notes && <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">{item.notes}</p>}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
