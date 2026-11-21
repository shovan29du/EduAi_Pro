async function get(path) {
  const response = await fetch(`/api/lesson-enrichment${path}`);
  if (!response.ok) throw new Error(`Request failed (${response.status})`);
  return response.json();
}

// School Grades 6-10, College 1-2, Undergraduate 1-4 and Master's 1-2 (earlier grades are not enriched).
export const ENRICHED_LEVELS = ['6', '7', '8', '9', '10', 'C1', 'C2', 'UG1', 'UG2', 'UG3', 'UG4', 'M1', 'M2'];
export const isEnrichedLevel = (level) => ENRICHED_LEVELS.includes(String(level || '').toUpperCase());

export const getLessonEnrichment = (level, lessonId) =>
  get(`/${encodeURIComponent(String(level).toUpperCase())}/${encodeURIComponent(lessonId)}`);

export function getRelatedArticle({ title, query, context, key }) {
  const params = new URLSearchParams();
  if (title) params.set('title', title);
  if (query) params.set('q', query);
  if (context) params.set('ctx', context);
  if (key) params.set('key', key);
  return get(`/wiki?${params}`);
}

// ── The owner's own picture for a lesson (Download / Upload), kept in the database ──
async function readError(response, fallback) {
  try {
    const body = await response.json();
    return typeof body.detail === 'string' ? body.detail : fallback;
  } catch {
    return fallback;
  }
}

export async function downloadLessonPicture({ key, title, context, wikiTitle }) {
  const response = await fetch('/api/lesson-picture/download', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ key, title, context: context || '', wiki_title: wikiTitle || '' }),
  });
  if (!response.ok) throw new Error(await readError(response, 'Could not download a picture.'));
  return response.json();
}

export async function uploadLessonPicture(key, file) {
  const response = await fetch(`/api/lesson-picture?key=${encodeURIComponent(key)}`, {
    method: 'PUT',
    headers: { 'Content-Type': file.type, 'X-Filename': encodeURIComponent(file.name) },
    body: file,
  });
  if (!response.ok) throw new Error(await readError(response, 'Could not upload the picture.'));
  return response.json();
}
