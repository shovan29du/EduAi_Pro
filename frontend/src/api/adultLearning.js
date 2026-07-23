export async function fetchVirtualMuseum({ query = '', region = '', objectType = '', limit = 120 } = {}) {
  const params = new URLSearchParams({
    q: query,
    region,
    object_type: objectType,
    limit: String(limit),
  });
  const res = await fetch(`/api/virtual-museum?${params.toString()}`);
  if (!res.ok) throw new Error('Could not load the virtual museum');
  return res.json();
}

export async function askAiTutor({ topic, question, mode }) {
  const res = await fetch('/api/ai-tutor', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic, question, mode }),
  });
  if (!res.ok) throw new Error('Could not ask the AI tutor');
  return res.json();
}
