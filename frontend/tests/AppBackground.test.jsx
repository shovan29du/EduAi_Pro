import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, waitFor } from '@testing-library/react';
import AppBackground from '../src/components/AppBackground.jsx';
import { BACKGROUND_IMAGE_TITLES } from '../src/data/backgroundImageTitles.js';

describe('AppBackground', () => {
  it('renders just the base layer when no thumbnails resolve', async () => {
    global.fetch = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) }));
    const { container } = render(<AppBackground />);
    await waitFor(() => expect(global.fetch).toHaveBeenCalled());
    expect(container.querySelector('[style]')).toBeNull();
  });

  it('applies the first resolved thumbnail as a background image', async () => {
    global.fetch = vi.fn((url) => {
      const u = String(url);
      if (u.includes('The%20Starry%20Night')) {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: 'https://example.com/starry-night.jpg' }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ thumbnail_url: null }) });
    });
    const { container } = render(<AppBackground />);
    await waitFor(() => {
      const layer = container.querySelector('[style]');
      expect(layer).not.toBeNull();
      expect(layer.style.backgroundImage).toContain('https://example.com/starry-night.jpg');
    });
  });

  it('does not crash when fetch rejects for every title', async () => {
    global.fetch = vi.fn(() => Promise.reject(new Error('network down')));
    const { container } = render(<AppBackground />);
    await waitFor(() => expect(global.fetch).toHaveBeenCalled());
    expect(container.querySelector('[aria-hidden="true"]')).not.toBeNull();
  });

  it('has 60 unique background image titles', () => {
    expect(BACKGROUND_IMAGE_TITLES).toHaveLength(60);
    expect(new Set(BACKGROUND_IMAGE_TITLES).size).toBe(60);
  });
});
