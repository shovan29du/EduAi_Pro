import React, { useCallback, useEffect, useState } from 'react';
import { listReports, setReportStatus } from '../api/reports.js';
import { REPORT_CATEGORIES } from './ReportProblem.jsx';

const CATEGORY_LABELS = Object.fromEntries(REPORT_CATEGORIES);
const KIND_LABELS = { lesson: 'Lesson', museum_object: 'Museum object', stem_experiment: 'STEM experiment', other: 'Other' };

export default function ProblemReportsPanel() {
  const [reports, setReports] = useState(null);
  const [showResolved, setShowResolved] = useState(false);
  const [error, setError] = useState('');

  const load = useCallback(() => {
    listReports(showResolved ? '' : 'open')
      .then((data) => { setReports(data.reports); setError(''); })
      .catch((err) => setError(err.message));
  }, [showResolved]);

  useEffect(() => { load(); }, [load]);

  function mark(id, status) {
    setReportStatus(id, status).then(load).catch((err) => setError(err.message));
  }

  return (
    <section className="mt-8 rounded-xl border p-4 dark:border-gray-700" aria-label="Problem reports">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h3 className="text-lg font-semibold">⚑ Problem reports</h3>
        <label className="flex items-center gap-2 text-sm">
          <input type="checkbox" checked={showResolved} onChange={(e) => setShowResolved(e.target.checked)} />
          Show resolved
        </label>
      </div>
      {error && <p className="mt-2 text-sm text-red-600" role="alert">{error}</p>}
      {!error && reports === null && <p className="mt-2 text-sm text-gray-500">Loading…</p>}
      {reports?.length === 0 && <p className="mt-2 text-sm text-gray-500">No {showResolved ? '' : 'open '}reports.</p>}
      <ul className="mt-3 space-y-3">
        {(reports || []).map((r) => (
          <li key={r.id} className="rounded-lg border p-3 text-sm dark:border-gray-700">
            <p className="font-medium">
              {KIND_LABELS[r.kind] || r.kind}: {r.title || r.item_id}
              {r.status === 'resolved' && <span className="ml-2 rounded bg-green-100 px-1.5 py-0.5 text-xs text-green-700">resolved</span>}
            </p>
            <p className="text-xs text-gray-500">
              {CATEGORY_LABELS[r.category] || r.category} · {r.item_id}{r.context ? ` · ${r.context}` : ''}
              {r.reporter ? ` · from ${r.reporter}` : ''} · {new Date(r.created_at).toLocaleString()}
            </p>
            {r.message && <p className="mt-1 whitespace-pre-line">{r.message}</p>}
            <button
              type="button"
              onClick={() => mark(r.id, r.status === 'open' ? 'resolved' : 'open')}
              className="mt-2 rounded border px-3 py-1 text-xs hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-800"
            >
              {r.status === 'open' ? 'Mark resolved' : 'Reopen'}
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}
