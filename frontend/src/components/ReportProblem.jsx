import React, { useEffect, useState } from 'react';
import { submitReport } from '../api/reports.js';

export const REPORT_CATEGORIES = [
  ['wrong_information', 'Something is incorrect'],
  ['broken_link', 'A link or video does not work'],
  ['wrong_or_missing_image', 'Picture is wrong or missing'],
  ['typo', 'Spelling or grammar mistake'],
  ['inappropriate', 'Not suitable for learners'],
  ['other', 'Something else'],
];

export default function ReportProblem({ kind, itemId, title, context = '', reporter = '' }) {
  const [open, setOpen] = useState(false);
  const [category, setCategory] = useState('wrong_information');
  const [message, setMessage] = useState('');
  const [status, setStatus] = useState('idle'); // idle | sending | sent | error
  const [error, setError] = useState('');

  // A different lesson/object gets a fresh form.
  useEffect(() => {
    setOpen(false);
    setMessage('');
    setStatus('idle');
    setError('');
  }, [kind, itemId]);

  function send(event) {
    event.preventDefault();
    if (category === 'other' && message.trim().length < 3) {
      setStatus('error');
      setError('Please describe the problem.');
      return;
    }
    setStatus('sending');
    submitReport({ kind, item_id: String(itemId), title: title || '', context, category, message, reporter })
      .then(() => setStatus('sent'))
      .catch((err) => { setStatus('error'); setError(err.message); });
  }

  if (status === 'sent') {
    return <p className="mt-4 text-sm text-green-700 dark:text-green-400" role="status">Thank you — your report was sent.</p>;
  }

  if (!open) {
    return (
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="mt-4 text-sm text-gray-500 underline hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
      >
        ⚑ Report a problem
      </button>
    );
  }

  return (
    <form onSubmit={send} className="mt-4 rounded-xl border p-4 text-sm dark:border-gray-700" aria-label="Report a problem">
      <p className="font-semibold">Report a problem with “{title}”</p>
      <label className="mt-3 block">
        <span className="block text-gray-600 dark:text-gray-300">What is wrong?</span>
        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="mt-1 w-full rounded-lg border px-3 py-2 dark:border-gray-600 dark:bg-gray-800"
        >
          {REPORT_CATEGORIES.map(([value, label]) => <option key={value} value={value}>{label}</option>)}
        </select>
      </label>
      <label className="mt-3 block">
        <span className="block text-gray-600 dark:text-gray-300">Details{category === 'other' ? '' : ' (optional)'}</span>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          maxLength={2000}
          rows={3}
          className="mt-1 w-full rounded-lg border px-3 py-2 dark:border-gray-600 dark:bg-gray-800"
        />
      </label>
      {status === 'error' && <p className="mt-2 text-red-600" role="alert">{error}</p>}
      <div className="mt-3 flex gap-2">
        <button type="submit" disabled={status === 'sending'} className="rounded-lg bg-indigo-600 px-4 py-2 font-medium text-white hover:bg-indigo-700 disabled:opacity-50">
          {status === 'sending' ? 'Sending…' : 'Send report'}
        </button>
        <button type="button" onClick={() => setOpen(false)} className="rounded-lg border px-4 py-2 dark:border-gray-600">Cancel</button>
      </div>
    </form>
  );
}
