import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import AppearanceSettings from '../src/components/AppearanceSettings.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

function renderSettings() {
  return render(
    <ChildProvider>
      <AppearanceSettings />
    </ChildProvider>
  );
}

describe('AppearanceSettings Ark AI key', () => {
  it('shows the offline prompt and saves a new key', async () => {
    let configured = false;
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/settings/anthropic-key' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve(
            configured
              ? { configured: true, source: 'settings', masked: 'sk-ant...-key' }
              : { configured: false, source: 'none', masked: '' }
          ),
        });
      }
      if (u === '/api/settings/anthropic-key' && options.method === 'POST') {
        const body = JSON.parse(options.body);
        expect(body.api_key).toBe('sk-ant-my-key');
        configured = true;
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ configured: true, source: 'settings', masked: 'sk-ant...-key' }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    renderSettings();
    expect(await screen.findByText('Ark AI is offline — add your API key below to turn it on.')).toBeInTheDocument();

    fireEvent.change(screen.getByPlaceholderText('sk-ant-...'), { target: { value: 'sk-ant-my-key' } });
    fireEvent.click(screen.getByText('Save key'));

    await waitFor(() => {
      expect(screen.getByText(/Connected \(sk-ant\.\.\.-key\)/)).toBeInTheDocument();
    });
  });

  it('shows a validation error when saving without a key', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      if (String(url) === '/api/settings/anthropic-key' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ configured: false, source: 'none', masked: '' }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    renderSettings();
    await screen.findByText('Ark AI is offline — add your API key below to turn it on.');
    fireEvent.click(screen.getByText('Save key'));

    expect(await screen.findByText('Paste your Anthropic API key first.')).toBeInTheDocument();
  });

  it('shows a connected status from an environment variable without a remove button', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      if (String(url) === '/api/settings/anthropic-key' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ configured: true, source: 'env', masked: 'sk-ant...abcd' }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    renderSettings();
    expect(await screen.findByText(/Connected \(sk-ant\.\.\.abcd, from environment variable\)/)).toBeInTheDocument();
    expect(screen.queryByText('Remove key')).not.toBeInTheDocument();
  });

  it('removes a saved key', async () => {
    let configured = true;
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/settings/anthropic-key' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve(
            configured
              ? { configured: true, source: 'settings', masked: 'sk-ant...abcd' }
              : { configured: false, source: 'none', masked: '' }
          ),
        });
      }
      if (u === '/api/settings/anthropic-key' && options.method === 'DELETE') {
        configured = false;
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ configured: false, source: 'none', masked: '' }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    renderSettings();
    await screen.findByText('Remove key');
    fireEvent.click(screen.getByText('Remove key'));

    await waitFor(() => {
      expect(screen.getByText('Ark AI is offline — add your API key below to turn it on.')).toBeInTheDocument();
    });
  });
});

const ALL_PROVIDERS = [
  'anthropic', 'openai', 'gemini', 'grok', 'groq', 'mistral',
  'together', 'perplexity', 'fireworks', 'deepseek', 'openrouter',
];

function unconfiguredProviderList() {
  return ALL_PROVIDERS.map((provider) => ({
    provider, label: provider, configured: false, source: 'none', masked: '',
  }));
}

describe('AppearanceSettings other model providers', () => {
  it('lists every other provider and saves an OpenAI key', async () => {
    let openaiConfigured = false;
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/settings/anthropic-key') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ configured: false, source: 'none', masked: '' }) });
      }
      if (u === '/api/settings/api-keys' && (!options.method || options.method === 'GET')) {
        const providers = unconfiguredProviderList().map((p) =>
          p.provider === 'openai' && openaiConfigured
            ? { ...p, configured: true, source: 'settings', masked: 'sk-ope...5.1x' }
            : p
        );
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers }) });
      }
      if (u === '/api/settings/api-keys/openai' && options.method === 'POST') {
        const body = JSON.parse(options.body);
        expect(body.api_key).toBe('sk-openai-key');
        openaiConfigured = true;
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ provider: 'openai', label: 'OpenAI', configured: true, source: 'settings', masked: 'sk-ope...5.1x' }),
        });
      }
      if (u === '/api/settings/preferred-model') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ model_id: '', model: null }) });
      }
      if (u === '/api/ark-ai/models') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ models: [] }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    renderSettings();
    expect(await screen.findByText('OpenAI')).toBeInTheDocument();
    expect(screen.getByText('Google Gemini')).toBeInTheDocument();
    expect(screen.getByText('xAI (Grok)')).toBeInTheDocument();
    expect(screen.getByText('OpenRouter')).toBeInTheDocument();

    // OpenAI is the first provider row and shares the generic "sk-..." placeholder with DeepSeek.
    fireEvent.change(screen.getAllByPlaceholderText('sk-...')[0], { target: { value: 'sk-openai-key' } });
    fireEvent.click(screen.getAllByText('Save')[0]);

    await waitFor(() => {
      expect(screen.getByText('✓ sk-ope...5.1x')).toBeInTheDocument();
    });
  });

  it('only lists models from providers with a configured key, and picking one sets it as preferred', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      const u = String(url);
      if (u === '/api/settings/anthropic-key') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ configured: false, source: 'none', masked: '' }) });
      }
      if (u === '/api/settings/api-keys' && (!options.method || options.method === 'GET')) {
        const providers = unconfiguredProviderList().map((p) =>
          p.provider === 'groq' ? { ...p, configured: true, source: 'settings', masked: 'gsk_...abcd' } : p
        );
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ providers }) });
      }
      if (u === '/api/settings/preferred-model' && (!options.method || options.method === 'GET')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ model_id: '', model: null }) });
      }
      if (u === '/api/settings/preferred-model' && options.method === 'POST') {
        const body = JSON.parse(options.body);
        expect(body.model_id).toBe('groq:llama-3.3-70b-versatile');
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ model_id: 'groq:llama-3.3-70b-versatile', model: { id: 'groq:llama-3.3-70b-versatile' } }),
        });
      }
      if (u === '/api/ark-ai/models') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            models: [
              { id: 'claude:claude-opus-4-8', name: 'Claude Opus 4.8', provider: 'Claude', raw: 'claude-opus-4-8' },
              { id: 'groq:llama-3.3-70b-versatile', name: 'Llama 3.3 70B', provider: 'Groq', raw: 'llama-3.3-70b-versatile' },
              { id: 'openai:gpt-5.1', name: 'GPT-5.1', provider: 'Openai', raw: 'gpt-5.1' },
            ],
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    renderSettings();
    await screen.findByText('OpenAI');

    const select = await screen.findByLabelText('Preferred model');
    // Only the Groq model (the one provider with a configured key) should be selectable --
    // Claude and OpenAI (unconfigured) are excluded.
    expect(screen.getByRole('option', { name: 'Llama 3.3 70B (Groq)' })).toBeInTheDocument();
    expect(screen.queryByRole('option', { name: /GPT-5.1/ })).not.toBeInTheDocument();
    expect(screen.queryByRole('option', { name: /Claude Opus/ })).not.toBeInTheDocument();

    fireEvent.change(select, { target: { value: 'groq:llama-3.3-70b-versatile' } });

    await waitFor(() => {
      expect(select.value).toBe('groq:llama-3.3-70b-versatile');
    });
  });
});
