import React, { useState, useEffect } from 'react';

export default function FoodHistory() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/cuisine-detail/food-history').then(r => r.json()).then(setData).catch(e => setError(e.message));
  }, []);

  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Food History</p><p className="text-sm mt-1">{error}</p>
    </div>
  );
  if (!data) return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">{[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-amber-500 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}</div>
    </div>
  );

  return (
    <div className="space-y-6">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: 'linear-gradient(135deg, #b45309, #92400e)' }}>
        <h1 className="text-3xl font-extrabold drop-shadow-lg">📜 {data.title}</h1>
        <p className="text-white/90 text-base mt-1 max-w-2xl">{data.description}</p>
      </div>

      <div className="relative pl-6 border-l-4 border-amber-300 dark:border-amber-700 space-y-6">
        {data.timeline?.map(item => (
          <div key={item.id} className="relative">
            <div className="absolute -left-[31px] top-1 w-4 h-4 rounded-full bg-amber-500 border-4 border-white dark:border-gray-900" />
            <div className="rounded-xl border-2 border-amber-200 dark:border-amber-800 bg-white dark:bg-gray-800 p-4 shadow-sm">
              <span className="text-xs font-bold text-amber-600 dark:text-amber-400">{item.era}</span>
              <h3 className="text-lg font-bold text-gray-800 dark:text-gray-100 mt-0.5">{item.title}</h3>
              <p className="text-sm text-gray-600 dark:text-gray-300 mt-2 leading-relaxed">{item.summary}</p>
              {item.regions?.length > 0 && (
                <div className="flex flex-wrap gap-1.5 mt-3">
                  {item.regions.map((r, i) => (
                    <span key={i} className="text-[11px] rounded-full px-2.5 py-0.5 font-medium bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300">🌍 {r}</span>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
