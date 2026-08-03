export async function sendArkAiMessage(message, history = [], { mode = 'chat', level } = {}) {
  const res = await fetch('/api/ark-ai/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, history, mode, level }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Ark AI could not reply');
  }
  return res.json();
}
