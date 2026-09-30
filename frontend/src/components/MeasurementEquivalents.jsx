import React, { useState, useEffect } from 'react';

export default function MeasurementEquivalents() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/cuisine-detail/measurement-equivalents').then(r => r.json()).then(setData).catch(e => setError(e.message));
  }, []);

  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Measurement Equivalents</p><p className="text-sm mt-1">{error}</p>
    </div>
  );
  if (!data) return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">{[0, 1, 2].map(i => <div key={i} className="w-3 h-3 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}</div>
    </div>
  );

  return (
    <div className="space-y-6">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: 'linear-gradient(135deg, #4f46e5, #4338ca)' }}>
        <h1 className="text-3xl font-extrabold drop-shadow-lg">📏 {data.title}</h1>
        <p className="text-white/90 text-base mt-1 max-w-2xl">{data.description}</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
        {data.tables?.map(table => (
          <div key={table.id} className="rounded-xl border-2 border-indigo-200 dark:border-indigo-800 bg-white dark:bg-gray-800 shadow-sm overflow-hidden">
            <div className="px-4 py-3 bg-indigo-50 dark:bg-indigo-950 border-b border-indigo-200 dark:border-indigo-800">
              <h2 className="font-bold text-indigo-800 dark:text-indigo-200 flex items-center gap-2">
                <span className="text-xl">{table.emoji}</span> {table.label}
              </h2>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <tbody>
                  {table.rows.map((row, i) => (
                    <tr key={i} className={i % 2 === 0 ? 'bg-white dark:bg-gray-800' : 'bg-indigo-50/50 dark:bg-indigo-950/40'}>
                      <td className="px-4 py-2 font-medium text-gray-700 dark:text-gray-200">{row.from}</td>
                      <td className="px-4 py-2 text-indigo-600 dark:text-indigo-300 font-semibold">= {row.to}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
