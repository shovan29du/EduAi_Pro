import React, { useState, useEffect } from 'react';

export default function CookingProblems() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/cuisine-detail/cooking-problems').then(r => r.json()).then(setData).catch(e => setError(e.message));
  }, []);

  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Cooking Problems &amp; Fixes</p><p className="text-sm mt-1">{error}</p>
    </div>
  );
  if (!data) return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">{[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-rose-600 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}</div>
    </div>
  );

  return (
    <div className="space-y-6">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: 'linear-gradient(135deg, #e11d48, #be123c)' }}>
        <h1 className="text-3xl font-extrabold drop-shadow-lg">🛠️ {data.title}</h1>
        <p className="text-white/90 text-base mt-1 max-w-2xl">{data.description}</p>
      </div>

      {data.categories?.map(cat => (
        <div key={cat.id}>
          <h2 className="text-xl font-bold text-gray-700 dark:text-gray-200 mb-3 flex items-center gap-2">
            <span className="text-2xl">{cat.emoji}</span> {cat.label}
          </h2>
          <div className="space-y-3">
            {cat.problems.map((p, i) => (
              <div key={i} className="rounded-xl border-2 border-rose-200 dark:border-rose-800 bg-white dark:bg-gray-800 p-4 shadow-sm">
                <p className="font-bold text-rose-700 dark:text-rose-300 flex items-center gap-2"><span>⚠️</span> {p.problem}</p>
                <ul className="mt-2 space-y-1">
                  {p.fixes.map((fix, fi) => (
                    <li key={fi} className="text-sm text-gray-700 dark:text-gray-300 flex items-start gap-2">
                      <span className="text-emerald-500 font-bold mt-0.5">✓</span>
                      <span>{fix}</span>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
