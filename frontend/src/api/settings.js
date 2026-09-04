export async function getAnthropicKeyStatus() {
  const res = await fetch('/api/settings/anthropic-key');
  if (!res.ok) throw new Error('Could not check Ark AI key status');
  return res.json();
}

export async function saveAnthropicKey(apiKey) {
  const res = await fetch('/api/settings/anthropic-key', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ api_key: apiKey }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Could not save the API key');
  }
  return res.json();
}

export async function clearAnthropicKey() {
  const res = await fetch('/api/settings/anthropic-key', { method: 'DELETE' });
  if (!res.ok) throw new Error('Could not remove the API key');
  return res.json();
}

export async function listApiKeyStatus() {
  const res = await fetch('/api/settings/api-keys');
  if (!res.ok) throw new Error('Could not check model provider key status');
  const body = await res.json();
  return body.providers;
}

export async function saveProviderKey(provider, apiKey) {
  const res = await fetch(`/api/settings/api-keys/${provider}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ api_key: apiKey }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Could not save the API key');
  }
  return res.json();
}

export async function clearProviderKey(provider) {
  const res = await fetch(`/api/settings/api-keys/${provider}`, { method: 'DELETE' });
  if (!res.ok) throw new Error('Could not remove the API key');
  return res.json();
}

export async function getPreferredModel() {
  const res = await fetch('/api/settings/preferred-model');
  if (!res.ok) throw new Error('Could not check the preferred model');
  return res.json();
}

export async function setPreferredModel(modelId) {
  const res = await fetch('/api/settings/preferred-model', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model_id: modelId }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || 'Could not set the preferred model');
  }
  return res.json();
}
