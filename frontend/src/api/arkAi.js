export async function sendArkAiMessage(message, history = [], { agent = 'teacher', level, context = '' } = {}) {
  const res = await fetch('/api/ark-ai/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, history, agent, level, context }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Ark AI could not reply');
  }
  return res.json();
}

export async function listArkAiPrompts(query = '', tag = '') {
  const params = new URLSearchParams();
  if (query) params.set('q', query);
  if (tag) params.set('tag', tag);
  const res = await fetch(`/api/ark-ai/prompts?${params.toString()}`);
  if (!res.ok) throw new Error('Could not load the Ark AI prompt library');
  return res.json();
}

export async function listArkAiModels() {
  const res = await fetch('/api/ark-ai/models');
  if (!res.ok) throw new Error('Could not load the Ark AI model catalog');
  return res.json();
}

export async function listArkAiTools(query = '', category = '', kind = '') {
  const params = new URLSearchParams();
  if (query) params.set('q', query);
  if (category) params.set('category', category);
  if (kind) params.set('kind', kind);
  const res = await fetch(`/api/ark-ai/tools?${params.toString()}`);
  if (!res.ok) throw new Error('Could not load the Ark AI tools directory');
  return res.json();
}
