import React, { useCallback, useEffect, useState } from 'react';
import { getPendingExamples, pregenerateExamples, reviewExample } from '../api/lessonExamples.js';

const LEVELS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'C1', 'C2', 'UG1', 'UG2', 'UG3', 'UG4', 'M1', 'M2'];

export default function ExampleReviewPanel() {
  const [level, setLevel] = useState('5');
  const [queue, setQueue] = useState(null);
  const [drafts, setDrafts] = useState({});
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);

  const load = useCallback(() => {
    setQueue(null);
    getPendingExamples(level)
      .then((data) => { setQueue(data); setError(''); })
      .catch((err) => setError(err.message));
  }, [level]);

  useEffect(() => { load(); }, [load]);

  function act(item, action) {
    setBusy(true);
    reviewExample({ level, lessonId: item.lesson_id, action, example: drafts[item.lesson_id] ?? '' })
      .then(() => { setMessage(action === 'approve' ? 'Approved — students will now see this text.' : 'Rejected.'); load(); })
      .catch((err) => setError(err.message))
      .finally(() => setBusy(false));
  }

  function draftMore() {
    setBusy(true);
    setMessage('');
    pregenerateExamples({ level, limit: 10 })
      .then((out) => {
        setMessage(out.unavailable
          ? 'The AI tutor is unavailable — add your Anthropic API key in Settings first.'
          : `Drafted ${out.created} example${out.created === 1 ? '' : 's'}; ${out.remaining} lessons still have none.`);
        load();
      })
      .catch((err) => setError(err.message))
      .finally(() => setBusy(false));
  }

  return (
    <section className="mt-8 rounded-xl border p-4 dark:border-gray-700" aria-label="Review lesson examples">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h3 className="text-lg font-semibold">✔ Review lesson examples</h3>
        <div className="flex items-center gap-2 text-sm">
          <label htmlFor="review-level">Level</label>
          <select id="review-level" value={level} onChange={(e) => setLevel(e.target.value)} className="rounded border px-2 py-1 dark:border-gray-600 dark:bg-gray-800">
            {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
          </select>
          <button type="button" disabled={busy} onClick={draftMore} className="rounded bg-indigo-600 px-3 py-1 text-white hover:bg-indigo-700 disabled:opacity-50">
            Draft 10 more
          </button>
        </div>
      </div>
      {queue && <p className="mt-1 text-xs text-gray-500">{queue.vetted_count} reviewed · {queue.pending_count} waiting for review</p>}
      {message && <p className="mt-2 text-sm text-green-700" role="status">{message}</p>}
      {error && <p className="mt-2 text-sm text-red-600" role="alert">{error}</p>}
      {queue?.items.length === 0 && <p className="mt-2 text-sm text-gray-500">Nothing is waiting for review at this level.</p>}
      <ul className="mt-3 space-y-3">
        {(queue?.items || []).map((item) => (
          <li key={item.lesson_id} className="rounded-lg border p-3 text-sm dark:border-gray-700">
            <p className="font-medium">{item.subject}: {item.title} <span className="text-xs font-normal text-gray-500">({item.lesson_id})</span></p>
            {item.flags.length > 0 && <p className="text-xs text-amber-700">Check: {item.flags.join('; ')}</p>}
            <textarea
              aria-label={`Example for ${item.title}`}
              value={drafts[item.lesson_id] ?? item.example}
              onChange={(e) => setDrafts((d) => ({ ...d, [item.lesson_id]: e.target.value }))}
              rows={4}
              className="mt-2 w-full rounded-lg border px-3 py-2 dark:border-gray-600 dark:bg-gray-800"
            />
            <div className="mt-2 flex gap-2">
              <button type="button" disabled={busy} onClick={() => act(item, 'approve')} className="rounded bg-emerald-600 px-3 py-1 text-white hover:bg-emerald-700 disabled:opacity-50">Approve</button>
              <button type="button" disabled={busy} onClick={() => act(item, 'reject')} className="rounded border px-3 py-1 hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-800 disabled:opacity-50">Reject</button>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}
