import React, { useEffect, useState } from 'react';
import { useChild } from '../contexts/ChildContext.jsx';
import { STREAMING_PLATFORMS, LEARNING_PLATFORMS } from '../data/platforms.js';
import {
  getAnthropicKeyStatus, saveAnthropicKey, clearAnthropicKey,
  listApiKeyStatus, saveProviderKey, clearProviderKey,
  getPreferredModel, setPreferredModel,
} from '../api/settings.js';
import { listArkAiModels } from '../api/arkAi.js';

const OTHER_PROVIDERS = [
  { slug: 'openai', label: 'OpenAI', rawProvider: 'Openai', placeholder: 'sk-...' },
  { slug: 'gemini', label: 'Google Gemini', rawProvider: 'Gemini', placeholder: 'AIza...' },
  { slug: 'grok', label: 'xAI (Grok)', rawProvider: 'Grok', placeholder: 'xai-...' },
  { slug: 'groq', label: 'Groq', rawProvider: 'Groq', placeholder: 'gsk_...' },
  { slug: 'mistral', label: 'Mistral', rawProvider: 'Mistral', placeholder: '...' },
  { slug: 'together', label: 'Together AI', rawProvider: 'Together', placeholder: '...' },
  { slug: 'perplexity', label: 'Perplexity', rawProvider: 'Perplexity', placeholder: 'pplx-...' },
  { slug: 'fireworks', label: 'Fireworks AI', rawProvider: 'Fireworks', placeholder: 'fw_...' },
  { slug: 'deepseek', label: 'DeepSeek', rawProvider: 'Deepseek', placeholder: 'sk-...' },
  { slug: 'openrouter', label: 'OpenRouter', rawProvider: 'OpenRouter (free)', placeholder: 'sk-or-...' },
];

const FONT_FAMILIES = [
  { value: '', label: 'Default' },
  { value: "'Comic Sans MS', cursive", label: 'Comic Sans' },
  { value: "Georgia, serif", label: 'Georgia (serif)' },
  { value: "'Trebuchet MS', sans-serif", label: 'Trebuchet (sans-serif)' },
  { value: "'Courier New', monospace", label: 'Courier (monospace)' },
  { value: "'OpenDyslexic', 'Comic Sans MS', cursive", label: 'OpenDyslexic (accessibility)' },
  { value: "'Arial', sans-serif", label: 'Arial (clean)' },
  { value: "'Verdana', sans-serif", label: 'Verdana (wide letters)' },
];


const THEMES = [
  { value: 'default', label: 'Default' },
  { value: 'sunshine', label: '☀️ Sunshine' },
  { value: 'ocean', label: '🌊 Ocean' },
  { value: 'forest', label: '🌳 Forest' },
  { value: 'bubblegum', label: '🍬 Bubblegum' },
  { value: 'dark', label: '🌙 Dark Mode' },
  { value: 'high-contrast', label: '⚡ High Contrast' },
  { value: 'sepia', label: '📜 Sepia (warm)' },
];

const COLORBLIND_THEMES = [
  { value: '', label: 'None (default)' },
  { value: 'deuteranopia', label: '🔵 Deuteranopia (red-green)', filter: 'url(#deuteranopia)' },
  { value: 'protanopia', label: '🔴 Protanopia (red-blind)', filter: 'url(#protanopia)' },
  { value: 'tritanopia', label: '🟡 Tritanopia (blue-yellow)', filter: 'url(#tritanopia)' },
];

const FONT_SIZES = [
  { value: 'small', label: 'Small' },
  { value: 'medium', label: 'Medium' },
  { value: 'large', label: 'Large' },
  { value: 'x-large', label: 'Extra Large' },
  { value: 'xx-large', label: 'XX-Large' },
];

function PlatformGroup({ title, platforms, connectedPlatforms, togglePlatform }) {
  return (
    <div className="mb-4">
      <p className="mb-2 text-sm font-medium">{title}</p>
      <div className="flex flex-col gap-2">
        {platforms.map((p) => (
          <div key={p.id} className="flex items-center justify-between gap-3 rounded border px-3 py-2 dark:border-gray-700">
            <label className="flex items-center gap-2 text-sm">
              <input
                type="checkbox"
                checked={!!connectedPlatforms[p.id]}
                onChange={() => togglePlatform(p.id)}
              />
              <span>{p.emoji} {p.label}</span>
            </label>
            {connectedPlatforms[p.id] && (
              <a
                href={p.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-medium text-blue-600 hover:underline dark:text-blue-400"
              >
                Sign in on {p.label} ↗
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

function PlatformSettings() {
  const { connectedPlatforms, togglePlatform } = useChild();
  return (
    <div className="mt-6 border-t pt-4 dark:border-gray-700">
      <h3 className="mb-1 text-base font-bold">🔗 Streaming &amp; Learning Platforms</h3>
      <p className="mb-3 text-xs text-gray-500">
        Tell us which platforms you already have an account with. EduAi_Pro never asks for or stores
        a password for these services — checking a box just helps us point you at the right place.
        Every "Sign in" link opens that provider's own real site, where you log in directly with them.
      </p>
      <PlatformGroup
        title="Streaming"
        platforms={STREAMING_PLATFORMS}
        connectedPlatforms={connectedPlatforms}
        togglePlatform={togglePlatform}
      />
      <PlatformGroup
        title="Learning"
        platforms={LEARNING_PLATFORMS}
        connectedPlatforms={connectedPlatforms}
        togglePlatform={togglePlatform}
      />
    </div>
  );
}

function ArkAiKeySettings() {
  const [status, setStatus] = useState(null);
  const [apiKey, setApiKey] = useState('');
  const [error, setError] = useState(null);
  const [saving, setSaving] = useState(false);

  function loadStatus() {
    getAnthropicKeyStatus()
      .then(setStatus)
      .catch(() => setStatus({ configured: false, source: 'none', masked: '' }));
  }

  useEffect(() => {
    loadStatus();
  }, []);

  async function handleSave(e) {
    e.preventDefault();
    setError(null);
    if (!apiKey.trim()) {
      setError('Paste your Anthropic API key first.');
      return;
    }
    setSaving(true);
    try {
      await saveAnthropicKey(apiKey.trim());
      setApiKey('');
      loadStatus();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  }

  async function handleRemove() {
    setError(null);
    try {
      await clearAnthropicKey();
      loadStatus();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="mt-6 border-t pt-4 dark:border-gray-700">
      <h3 className="mb-1 text-base font-bold">🤖 Ark AI Connection</h3>
      <p className="mb-3 text-xs text-gray-500">
        Ark AI needs an Anthropic API key (from{' '}
        <a href="https://console.anthropic.com/" target="_blank" rel="noopener noreferrer" className="text-blue-600 underline dark:text-blue-400">
          console.anthropic.com
        </a>
        ) to answer for real instead of showing the offline message. This is a separate,
        metered API key — not your claude.ai subscription login — and it's stored only on
        this computer, never uploaded anywhere.
      </p>

      {status?.configured ? (
        <div className="mb-3 flex flex-wrap items-center gap-2 text-sm">
          <span className="rounded bg-green-100 px-2 py-1 text-green-800 dark:bg-green-950 dark:text-green-200">
            ✓ Connected ({status.masked}{status.source === 'env' ? ', from environment variable' : ''})
          </span>
          {status.source === 'settings' && (
            <button
              type="button"
              onClick={handleRemove}
              className="rounded border px-2 py-1 text-xs focus:outline focus:outline-2 focus:outline-blue-500"
            >
              Remove key
            </button>
          )}
        </div>
      ) : (
        <p className="mb-3 rounded bg-amber-50 px-2 py-1 text-sm text-amber-800 dark:bg-amber-950 dark:text-amber-200">
          Ark AI is offline — add your API key below to turn it on.
        </p>
      )}

      <form onSubmit={handleSave} className="flex flex-wrap items-end gap-2">
        <label className="flex flex-1 min-w-64 flex-col text-sm font-medium">
          {status?.configured ? 'Replace API key' : 'Anthropic API key'}
          <input
            type="password"
            value={apiKey}
            onChange={(e) => setApiKey(e.target.value)}
            placeholder="sk-ant-..."
            autoComplete="off"
            className="mt-1 rounded border px-2 py-1 dark:bg-gray-800 dark:text-white"
          />
        </label>
        <button
          type="submit"
          disabled={saving}
          className="rounded border px-3 py-1 focus:outline focus:outline-2 focus:outline-blue-500 disabled:opacity-50"
        >
          {saving ? 'Saving…' : 'Save key'}
        </button>
      </form>
      {error && (
        <p role="alert" className="mt-2 text-red-600">
          {error}
        </p>
      )}
    </div>
  );
}

function ProviderKeyRow({ provider, status, onSaved }) {
  const [value, setValue] = useState('');
  const [error, setError] = useState(null);
  const [busy, setBusy] = useState(false);

  async function handleSave(e) {
    e.preventDefault();
    setError(null);
    if (!value.trim()) {
      setError('Paste an API key first.');
      return;
    }
    setBusy(true);
    try {
      await saveProviderKey(provider.slug, value.trim());
      setValue('');
      onSaved();
    } catch (err) {
      setError(err.message);
    } finally {
      setBusy(false);
    }
  }

  async function handleRemove() {
    setError(null);
    try {
      await clearProviderKey(provider.slug);
      onSaved();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <li className="rounded border p-2 dark:border-gray-700">
      <form onSubmit={handleSave} className="flex flex-wrap items-end gap-2">
        <label className="flex flex-1 min-w-48 flex-col text-sm font-medium">
          {provider.label}
          {status?.configured ? (
            <span className="mt-1 rounded bg-green-100 px-2 py-1 text-xs text-green-800 dark:bg-green-950 dark:text-green-200">
              ✓ {status.masked}
            </span>
          ) : (
            <input
              type="password"
              value={value}
              onChange={(e) => setValue(e.target.value)}
              placeholder={provider.placeholder}
              autoComplete="off"
              className="mt-1 rounded border px-2 py-1 dark:bg-gray-800 dark:text-white"
            />
          )}
        </label>
        {status?.configured ? (
          <button
            type="button"
            onClick={handleRemove}
            className="rounded border px-2 py-1 text-xs focus:outline focus:outline-2 focus:outline-blue-500"
          >
            Remove
          </button>
        ) : (
          <button
            type="submit"
            disabled={busy}
            className="rounded border px-2 py-1 text-xs focus:outline focus:outline-2 focus:outline-blue-500 disabled:opacity-50"
          >
            {busy ? 'Saving…' : 'Save'}
          </button>
        )}
      </form>
      {error && (
        <p role="alert" className="mt-1 text-xs text-red-600">
          {error}
        </p>
      )}
    </li>
  );
}

function OtherModelProviders() {
  const [statuses, setStatuses] = useState({});
  const [models, setModels] = useState([]);
  const [preferred, setPreferred] = useState(null);
  const [modelError, setModelError] = useState(null);

  function loadStatuses() {
    listApiKeyStatus()
      .then((list) => {
        const byProvider = {};
        list.forEach((p) => {
          byProvider[p.provider] = p;
        });
        setStatuses(byProvider);
      })
      .catch(() => {});
  }

  function loadPreferred() {
    getPreferredModel().then(setPreferred).catch(() => {});
  }

  useEffect(() => {
    loadStatuses();
    loadPreferred();
    listArkAiModels()
      .then((data) => setModels(data.models || []))
      .catch(() => {});
  }, []);

  const configuredRawProviders = new Set(
    OTHER_PROVIDERS.filter((p) => statuses[p.slug]?.configured).map((p) => p.rawProvider)
  );
  const selectableModels = models.filter((m) => configuredRawProviders.has(m.provider));

  async function handlePickModel(e) {
    const modelId = e.target.value;
    setModelError(null);
    try {
      const result = await setPreferredModel(modelId);
      setPreferred(result);
    } catch (err) {
      setModelError(err.message);
    }
  }

  return (
    <div className="mt-6 border-t pt-4 dark:border-gray-700">
      <h3 className="mb-1 text-base font-bold">🌐 Other model providers</h3>
      <p className="mb-3 text-xs text-gray-500">
        Ark AI's model library lists every major provider — add an API key for any of them
        here to make it genuinely callable, then choose it below as Ark AI's preferred model.
        Claude stays the default whenever no preferred model is set, or if the chosen provider
        is temporarily unavailable.
      </p>
      <ul className="grid gap-2 sm:grid-cols-2">
        {OTHER_PROVIDERS.map((provider) => (
          <ProviderKeyRow key={provider.slug} provider={provider} status={statuses[provider.slug]} onSaved={loadStatuses} />
        ))}
      </ul>

      <label className="mt-4 flex flex-col text-sm font-medium">
        Preferred model
        <select
          value={preferred?.model_id || ''}
          onChange={handlePickModel}
          className="mt-1 rounded border px-2 py-1 dark:bg-gray-800 dark:text-white"
        >
          <option value="">Claude (default)</option>
          {selectableModels.map((m) => (
            <option key={m.id} value={m.id}>
              {m.name} ({m.provider})
            </option>
          ))}
        </select>
      </label>
      {selectableModels.length === 0 && (
        <p className="mt-1 text-xs text-gray-500">Add a provider key above to unlock its models here.</p>
      )}
      {modelError && (
        <p role="alert" className="mt-2 text-red-600">
          {modelError}
        </p>
      )}
    </div>
  );
}

export default function AppearanceSettings() {
  const { appearance, updateAppearance } = useChild();

  function handleThemeChange(theme) {
    updateAppearance({ theme, bgColor: '', fontColor: '' });
  }

  function handleReset() {
    updateAppearance({ bgColor: '', fontColor: '', fontFamily: '', fontSize: 'medium', theme: 'default' });
  }

  return (
    <section aria-label="Appearance settings" className="rounded border p-4 dark:border-gray-700">
      <h2 className="mb-3 text-lg font-bold">Appearance</h2>

      <div className="mb-4">
        <p className="mb-2 text-sm font-medium">Theme</p>
        <div className="flex flex-wrap gap-2" role="radiogroup" aria-label="Theme presets">
          {THEMES.map((t) => (
            <button
              key={t.value}
              type="button"
              role="radio"
              aria-checked={appearance.theme === t.value && !appearance.bgColor}
              onClick={() => handleThemeChange(t.value)}
              className={`rounded border px-3 py-1 focus:outline focus:outline-2 focus:outline-blue-500 ${
                appearance.theme === t.value && !appearance.bgColor ? 'bg-blue-600 text-white' : ''
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>
      </div>

      <div className="mb-4 flex flex-wrap gap-6">
        <label className="flex flex-col text-sm font-medium">
          Background colour
          <input
            type="color"
            aria-label="Background colour"
            value={appearance.bgColor || '#ffffff'}
            onChange={(e) => updateAppearance({ bgColor: e.target.value })}
            className="mt-1 h-9 w-16 rounded border"
          />
        </label>
        <label className="flex flex-col text-sm font-medium">
          Font colour
          <input
            type="color"
            aria-label="Font colour"
            value={appearance.fontColor || '#000000'}
            onChange={(e) => updateAppearance({ fontColor: e.target.value })}
            className="mt-1 h-9 w-16 rounded border"
          />
        </label>
      </div>

      <div className="mb-4 flex flex-wrap gap-6">
        <label className="flex flex-col text-sm font-medium">
          Font type
          <select
            value={appearance.fontFamily || ''}
            onChange={(e) => updateAppearance({ fontFamily: e.target.value })}
            className="mt-1 rounded border px-2 py-1 dark:bg-gray-800 dark:text-white"
          >
            {FONT_FAMILIES.map((f) => (
              <option key={f.label} value={f.value}>
                {f.label}
              </option>
            ))}
          </select>
        </label>
        <label className="flex flex-col text-sm font-medium">
          Font size
          <select
            value={appearance.fontSize || 'medium'}
            onChange={(e) => updateAppearance({ fontSize: e.target.value })}
            className="mt-1 rounded border px-2 py-1 dark:bg-gray-800 dark:text-white"
          >
            {FONT_SIZES.map((f) => (
              <option key={f.value} value={f.value}>
                {f.label}
              </option>
            ))}
          </select>
        </label>
      </div>

      <div className="mb-4">
        <p className="mb-2 text-sm font-medium">Colour-Blind Assistance</p>
        <p className="text-xs text-gray-500 mb-2">Applies a visual filter to adjust colours for different types of colour vision.</p>
        <div className="flex flex-wrap gap-2" role="radiogroup" aria-label="Colour-blind themes">
          {COLORBLIND_THEMES.map((t) => (
            <button
              key={t.value}
              type="button"
              role="radio"
              aria-checked={appearance.colorBlindTheme === t.value}
              onClick={() => updateAppearance({ colorBlindTheme: t.value })}
              className={`rounded border px-3 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500 ${
                appearance.colorBlindTheme === t.value ? 'bg-blue-600 text-white' : ''
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>
      </div>

      <button
        type="button"
        onClick={handleReset}
        className="rounded border px-3 py-1 focus:outline focus:outline-2 focus:outline-blue-500"
      >
        Reset to default
      </button>

      <ArkAiKeySettings />
      <OtherModelProviders />
      <PlatformSettings />
    </section>
  );
}
