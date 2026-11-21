import { describe, it, expect } from 'vitest';
import { tabColorTheme } from '../src/utils/tabColors.js';

describe('tabColorTheme', () => {
  it('returns the same theme for the same tab name every time', () => {
    const a = tabColorTheme('Library');
    const b = tabColorTheme('Library');
    expect(a).toEqual(b);
  });

  it('returns an active and inactive class string', () => {
    const theme = tabColorTheme('Museum');
    expect(typeof theme.active).toBe('string');
    expect(typeof theme.inactive).toBe('string');
    expect(theme.active.length).toBeGreaterThan(0);
    expect(theme.inactive.length).toBeGreaterThan(0);
  });

  it('assigns different colors to at least some different tab names', () => {
    const names = ['Subjects', 'Library', 'Search', 'Favourites', 'AI Tutor', 'Languages', 'Grammar', 'Museum'];
    const themes = new Set(names.map((name) => tabColorTheme(name).active));
    expect(themes.size).toBeGreaterThan(1);
  });
});
