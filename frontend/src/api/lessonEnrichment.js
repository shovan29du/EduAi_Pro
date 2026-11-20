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

export function getRelatedArticle({ title, query, context }) {
  const params = new URLSearchParams();
  if (title) params.set('title', title);
  if (query) params.set('q', query);
  if (context) params.set('ctx', context);
  return get(`/wiki?${params}`);
}
