import { fetchJsonWithOffline, isLevelSaved } from '../utils/offlineLessons.js';

export async function fetchLevels() {
  const res = await fetch('/api/levels');
  if (!res.ok) throw new Error('Could not load levels');
  return res.json();
}

export async function fetchLevel(levelId) {
  const res = await fetch(`/api/level/${levelId}`);
  if (!res.ok) throw new Error(`Level ${levelId} not available`);
  return res.json();
}

// Overview and subject data fall back to the copy saved for offline use when
// the network or server is unreachable (see utils/offlineLessons.js).
export async function fetchLevelOverview(levelId) {
  const result = await fetchJsonWithOffline(`/api/level/${encodeURIComponent(levelId)}/overview`, { keep: isLevelSaved(levelId) });
  if (!result.ok) throw new Error(`Level ${levelId} not available`);
  return result.data;
}

export async function fetchLevelSubject(levelId, subjectName) {
  const result = await fetchJsonWithOffline(
    `/api/level/${encodeURIComponent(levelId)}/subjects/${encodeURIComponent(subjectName)}`,
    { keep: isLevelSaved(levelId) },
  );
  if (!result.ok) throw new Error(`${subjectName} is not available at level ${levelId}`);
  return result.data;
}

export async function searchLevel(levelId, query) {
  const res = await fetch(`/api/level/${levelId}/search?q=${encodeURIComponent(query)}`);
  if (!res.ok) throw new Error(`Search failed for level ${levelId}`);
  return res.json();
}
