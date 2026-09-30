import React, { useState, useEffect } from 'react';

const API = '/api/cuisine';

function LoadingDots() {
  return (
    <div className="flex justify-center items-center py-16">
      <div className="flex gap-2">
        {[0, 1, 2].map(i => (
          <div key={i} className="w-3 h-3 rounded-full bg-orange-500 animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />
        ))}
      </div>
    </div>
  );
}

function QuizSection({ quiz, colour }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  if (!quiz || quiz.length === 0) return null;
  const score = submitted ? quiz.reduce((acc, q, i) => acc + (answers[i] === q.answer ? 1 : 0), 0) : 0;

  return (
    <div className="mt-6 rounded-2xl border-2 p-5" style={{ borderColor: colour, backgroundColor: colour + '0d' }}>
      <h3 className="text-xl font-bold mb-4 flex items-center gap-2" style={{ color: colour }}>🧠 Quick Quiz</h3>
      {submitted && (
        <div className={`mb-4 rounded-xl p-4 text-center font-bold text-lg ${score === quiz.length ? 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300' : score >= quiz.length / 2 ? 'bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300' : 'bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300'}`}>
          {score === quiz.length ? '🏆 Perfect score!' : `${score}/${quiz.length} correct`}
        </div>
      )}
      <div className="space-y-5">
        {quiz.map((q, qi) => (
          <div key={qi} className="bg-white dark:bg-gray-800 rounded-xl p-4 shadow-sm">
            <p className="font-semibold text-gray-800 dark:text-gray-100 mb-3">
              <span className="font-bold" style={{ color: colour }}>Q{qi + 1}. </span>{q.q}
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {q.options.map((opt, oi) => {
                let cls = 'rounded-lg border-2 px-3 py-2 text-sm font-medium cursor-pointer transition-all ';
                if (submitted) {
                  if (oi === q.answer) cls += 'border-green-500 bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200';
                  else if (answers[qi] === oi) cls += 'border-red-400 bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200';
                  else cls += 'border-gray-200 bg-gray-50 text-gray-500 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400';
                } else {
                  cls += answers[qi] === oi ? 'text-white' : 'border-gray-200 bg-gray-50 text-gray-700 hover:border-opacity-70 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-200';
                }
                return (
                  <button key={oi} disabled={submitted} onClick={() => !submitted && setAnswers(a => ({ ...a, [qi]: oi }))}
                    className={cls} style={answers[qi] === oi && !submitted ? { backgroundColor: colour, borderColor: colour } : {}}>
                    <span className="font-bold mr-1">{String.fromCharCode(65 + oi)}.</span> {opt}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </div>
      <div className="mt-4 flex gap-3">
        {!submitted ? (
          <button onClick={() => Object.keys(answers).length >= quiz.length && setSubmitted(true)}
            disabled={Object.keys(answers).length < quiz.length}
            className="px-6 py-2.5 rounded-full font-bold text-white transition-all disabled:opacity-40" style={{ backgroundColor: colour }}>
            Submit Answers
          </button>
        ) : (
          <button onClick={() => { setAnswers({}); setSubmitted(false); }}
            className="px-6 py-2.5 rounded-full font-bold text-white bg-gray-500 hover:bg-gray-600 transition-all">
            Try Again
          </button>
        )}
      </div>
    </div>
  );
}

function CuisineDetail({ cuisine, onBack }) {
  const colour = cuisine.colour || '#e67e22';
  return (
    <div className="space-y-6">
      <div className="rounded-2xl p-6 text-white shadow-xl" style={{ background: `linear-gradient(135deg, ${colour}, ${colour}cc)` }}>
        <button onClick={onBack} className="mb-4 flex items-center gap-1 text-white/80 hover:text-white text-sm font-semibold transition-colors">
          ← Back to all cuisines
        </button>
        <div className="flex items-center gap-4">
          <span className="text-7xl drop-shadow-lg">{cuisine.emoji}</span>
          <div>
            <h2 className="text-3xl font-extrabold drop-shadow">{cuisine.label}</h2>
            <p className="text-white/90 text-lg mt-1">{cuisine.description}</p>
            {cuisine.region && <span className="inline-block mt-2 bg-white/20 rounded-full px-3 py-1 text-sm">📍 {cuisine.region}</span>}
          </div>
        </div>
      </div>

      {cuisine.history && (
        <div className="rounded-xl border-2 p-4 bg-white dark:bg-gray-800" style={{ borderColor: colour + '40' }}>
          <h3 className="text-lg font-bold mb-2 flex items-center gap-2" style={{ color: colour }}>📜 History</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300 leading-relaxed">{cuisine.history}</p>
        </div>
      )}

      {cuisine.famous_dishes?.length > 0 && (
        <div>
          <h3 className="text-lg font-bold text-gray-700 dark:text-gray-200 mb-3 flex items-center gap-2"><span>🍽️</span> Famous Dishes</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {cuisine.famous_dishes.map((d, i) => (
              <div key={i} className="rounded-xl border-2 p-4 bg-white dark:bg-gray-800 shadow-sm" style={{ borderColor: colour + '60' }}>
                <p className="font-bold text-gray-800 dark:text-gray-100">{d.name}</p>
                {d.origin && <p className="text-xs font-semibold mt-0.5" style={{ color: colour }}>📍 {d.origin}</p>}
                {d.description && <p className="text-xs text-gray-600 dark:text-gray-300 mt-1">{d.description}</p>}
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {cuisine.key_ingredients?.length > 0 && (
          <div>
            <h3 className="text-sm font-bold text-gray-700 dark:text-gray-200 mb-2 flex items-center gap-2"><span>🧂</span> Key Ingredients</h3>
            <div className="flex flex-wrap gap-2">
              {cuisine.key_ingredients.map((ing, i) => (
                <span key={i} className="text-xs rounded-full px-3 py-1 font-medium border" style={{ borderColor: colour, color: colour }}>{ing}</span>
              ))}
            </div>
          </div>
        )}
        {cuisine.cooking_techniques?.length > 0 && (
          <div>
            <h3 className="text-sm font-bold text-gray-700 dark:text-gray-200 mb-2 flex items-center gap-2"><span>🔥</span> Cooking Techniques</h3>
            <div className="flex flex-wrap gap-2">
              {cuisine.cooking_techniques.map((t, i) => (
                <span key={i} className="text-xs rounded-full px-3 py-1 font-medium text-white" style={{ backgroundColor: colour }}>{t}</span>
              ))}
            </div>
          </div>
        )}
      </div>

      {cuisine.cultural_notes && (
        <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-4">
          <h3 className="font-semibold text-indigo-800 dark:text-indigo-200 mb-1">🌍 Culture &amp; Dining Customs</h3>
          <p className="text-sm text-indigo-900 dark:text-indigo-100">{cuisine.cultural_notes}</p>
        </div>
      )}

      {cuisine.fun_facts?.length > 0 && (
        <div className="rounded-xl bg-yellow-50 dark:bg-yellow-950 border border-yellow-200 dark:border-yellow-800 p-4">
          <h3 className="font-semibold text-yellow-800 dark:text-yellow-200 mb-2">💡 Fun Facts</h3>
          <ul className="text-sm text-yellow-900 dark:text-yellow-100 list-disc pl-5 space-y-1">
            {cuisine.fun_facts.map((f, i) => <li key={i}>{f}</li>)}
          </ul>
        </div>
      )}

      <QuizSection quiz={cuisine.quiz} colour={colour} />
    </div>
  );
}

export default function CuisineCentre() {
  const [overview, setOverview] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [detail, setDetail] = useState(null);
  const [loading, setLoading] = useState(true);
  const [detailLoading, setDetailLoading] = useState(false);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetch(API).then(r => r.json()).then(data => { setOverview(data); setLoading(false); }).catch(e => { setError(e.message); setLoading(false); });
  }, []);

  useEffect(() => {
    if (!selectedId) return;
    setDetailLoading(true);
    setDetail(null);
    fetch(`${API}/${selectedId}`).then(r => r.json()).then(data => { setDetail(data); setDetailLoading(false); }).catch(e => { setError(e.message); setDetailLoading(false); });
  }, [selectedId]);

  if (loading) return <LoadingDots />;
  if (error) return (
    <div className="rounded-xl border border-red-300 bg-red-50 dark:bg-red-950 p-6 text-red-700 dark:text-red-300">
      <p className="font-bold">Could not load Cuisine Centre</p>
      <p className="text-sm mt-1">{error}</p>
    </div>
  );

  if (selectedId) {
    return (
      <div>
        {detailLoading && <LoadingDots />}
        {detail && <CuisineDetail cuisine={detail} onBack={() => { setSelectedId(null); setDetail(null); }} />}
      </div>
    );
  }

  const cuisines = (overview?.cuisines || []).filter(c =>
    !search || c.label.toLowerCase().includes(search.toLowerCase()) || (c.description || '').toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6">
      <div className="relative rounded-3xl overflow-hidden shadow-2xl" style={{ background: 'linear-gradient(135deg, #f97316, #ea580c, #c2410c)' }}>
        <div className="relative p-8 text-white">
          <div className="flex items-center gap-3 mb-2">
            <span className="text-5xl">🍽️</span><span className="text-5xl">🍜</span><span className="text-5xl">🍛</span><span className="text-5xl">🍣</span><span className="text-5xl">🥘</span>
          </div>
          <h1 className="text-4xl font-extrabold drop-shadow-lg">Cuisine &amp; Food Resource Centre</h1>
          <p className="text-white/90 text-lg mt-1 max-w-2xl">{overview?.description}</p>
          <p className="text-white/70 text-xs mt-2">Adult edition — no content restrictions beyond keeping every recipe pork-free (beef, lamb, or mutton used instead).</p>
        </div>
      </div>

      <div className="relative">
        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">🔍</span>
        <input type="text" value={search} onChange={e => setSearch(e.target.value)} placeholder="Search cuisines..."
          className="w-full rounded-full border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 pl-9 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400 dark:text-white" />
      </div>

      {cuisines.length === 0 ? (
        <div className="text-center py-10 text-gray-500 dark:text-gray-400">
          <p className="text-4xl mb-2">🔍</p>
          <p className="font-semibold">No cuisines found for "{search}"</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {cuisines.map(c => (
            <button key={c.id} onClick={() => setSelectedId(c.id)}
              className="group relative rounded-2xl p-5 text-left shadow-md hover:shadow-xl transition-all hover:-translate-y-1 border-2 bg-white dark:bg-gray-800"
              style={{ borderColor: c.colour + '60' }}>
              <div className="absolute top-0 left-0 right-0 h-1.5 rounded-t-2xl" style={{ backgroundColor: c.colour }} />
              <div className="flex items-start gap-3">
                <span className="text-4xl group-hover:scale-110 transition-transform">{c.emoji}</span>
                <div className="flex-1 min-w-0">
                  <p className="font-bold text-gray-800 dark:text-gray-100 truncate" style={{ color: c.colour }}>{c.label}</p>
                  {c.region && <p className="text-[11px] text-gray-400">{c.region}</p>}
                </div>
              </div>
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-2 line-clamp-3">{c.description}</p>
              <div className="mt-3 text-xs font-bold text-center rounded-full py-1 text-white transition-opacity" style={{ backgroundColor: c.colour }}>Explore →</div>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
