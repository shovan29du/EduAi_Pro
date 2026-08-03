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
