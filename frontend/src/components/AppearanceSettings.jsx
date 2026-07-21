import React from 'react';
import { useChild } from '../contexts/ChildContext.jsx';
import { STREAMING_PLATFORMS, LEARNING_PLATFORMS } from '../data/platforms.js';

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

      <PlatformSettings />
    </section>
  );
}
