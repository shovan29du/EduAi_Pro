export async function getLessonExample({ lessonId, title, subject, level, summary, concepts }) {
  const params = new URLSearchParams({ title, subject: subject || '' });
  if (lessonId) params.set('lesson_id', lessonId);
  if (level) params.set('level', String(level));
  if (summary) params.set('summary', summary.slice(0, 400));
  if (concepts?.length) params.set('concepts', concepts.slice(0, 8).join(','));
  const response = await fetch(`/api/lesson-example?${params}`);
  if (!response.ok) throw new Error(`Request failed (${response.status})`);
  return response.json();
}
