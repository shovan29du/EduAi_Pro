import React, { useEffect, useState } from 'react';
import { downloadLevel, getDownloads, offlineSupported, removeLevel } from '../utils/offlineLessons.js';

function useOnline() {
  const [online, setOnline] = useState(typeof navigator === 'undefined' ? true : navigator.onLine !== false);
  useEffect(() => {
    const up = () => setOnline(true);
    const down = () => setOnline(false);
    window.addEventListener('online', up);
    window.addEventListener('offline', down);
    return () => { window.removeEventListener('online', up); window.removeEventListener('offline', down); };
  }, []);
  return online;
}

export default function OfflineDownload({ level, levelLabel }) {
  const online = useOnline();
  const [saved, setSaved] = useState(() => getDownloads()[String(level)] || null);
  const [progress, setProgress] = useState(null); // { done, total } while downloading
  const [error, setError] = useState('');

  useEffect(() => { setSaved(getDownloads()[String(level)] || null); setError(''); setProgress(null); }, [level]);

  function save() {
    setError('');
    setProgress({ done: 0, total: 0 });
    downloadLevel(level, { onProgress: (done, total) => setProgress({ done, total }) })
      .then((entry) => setSaved(entry))
      .catch((err) => setError(err.message))
      .finally(() => setProgress(null));
  }

  function remove() {
    removeLevel(level).then(() => setSaved(null));
  }

  const name = levelLabel || `level ${level}`;
  return (
    <div className="space-y-2">
      {!online && (
        <p className="rounded-lg border border-amber-300 bg-amber-50 p-2 text-sm text-amber-800 dark:border-amber-700 dark:bg-amber-950 dark:text-amber-200" role="status">
          You are offline. Lessons you saved are still available.
        </p>
      )}
      {offlineSupported() && (
        <div className="flex flex-wrap items-center gap-3 text-sm">
          {progress ? (
            <span role="status">Saving {name}… {progress.total ? `${progress.done} of ${progress.total} subjects` : ''}</span>
          ) : saved ? (
            <>
              <span className="text-green-700 dark:text-green-400" role="status">
                ✓ {name} is saved for offline use ({saved.subjects} subjects, {new Date(saved.savedAt).toLocaleDateString()})
              </span>
              <button type="button" disabled={!online} onClick={save} className="rounded border px-3 py-1 hover:bg-gray-50 disabled:opacity-50 dark:border-gray-600 dark:hover:bg-gray-800">Update</button>
              <button type="button" onClick={remove} className="rounded border px-3 py-1 hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-800">Remove</button>
            </>
          ) : (
            <button type="button" disabled={!online} onClick={save} className="rounded border border-blue-600 px-3 py-1 text-blue-700 hover:bg-blue-50 disabled:opacity-50 dark:text-blue-300 dark:hover:bg-blue-950">
              ⬇ Save {name} for offline use
            </button>
          )}
        </div>
      )}
      {error && <p className="text-sm text-red-600" role="alert">{error}</p>}
    </div>
  );
}
