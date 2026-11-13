async function request(path, options) {
  const response = await fetch(`/api/lesson-example${path}`, options);
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(typeof body.detail === 'string' ? body.detail : `Request failed (${response.status})`);
  }
  return response.json();
}

const post = (path, body) => request(path, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body),
});

export function getLessonExample({ lessonId, title, subject, level, summary, concepts }) {
  const params = new URLSearchParams({ title, subject: subject || '' });
  if (lessonId) params.set('lesson_id', lessonId);
  if (level) params.set('level', String(level));
  if (summary) params.set('summary', summary.slice(0, 400));
  if (concepts?.length) params.set('concepts', concepts.slice(0, 8).join(','));
  return request(`?${params}`);
}

export const getExampleQuiz = ({ example, title, subject, level }) =>
  post('/quiz', { example, title: title || '', subject: subject || '', level: level ? String(level) : '' });

export const getPendingExamples = (level, limit = 20) =>
  request(`/pending?level=${encodeURIComponent(level)}&limit=${limit}`);

export const reviewExample = ({ level, lessonId, action, example = '' }) =>
  post('/review', { level: String(level), lesson_id: lessonId, action, example });

export const pregenerateExamples = ({ level, subject = '', limit = 10 }) =>
  post('/pregenerate', { level: String(level), subject, limit });
