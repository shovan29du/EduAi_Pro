async function get(path) {
  const response = await fetch(`/api/lesson-enrichment${path}`);
  if (!response.ok) throw new Error(`Request failed (${response.status})`);
  return response.json();
}

export const MASTERS_LEVELS = ['M1', 'M2'];
export const isMastersLevel = (level) => MASTERS_LEVELS.includes(String(level || '').toUpperCase());

export const getLessonEnrichment = (level, lessonId) =>
  get(`/${encodeURIComponent(String(level).toUpperCase())}/${encodeURIComponent(lessonId)}`);

export function getRelatedArticle({ title, query }) {
  const params = new URLSearchParams();
  if (title) params.set('title', title);
  if (query) params.set('q', query);
  return get(`/wiki?${params}`);
}
