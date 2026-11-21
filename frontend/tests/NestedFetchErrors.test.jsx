import React from 'react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import StemLab from '../src/components/StemLab.jsx';
import VirtualMuseum from '../src/components/VirtualMuseum.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

afterEach(() => vi.unstubAllGlobals());

const json = (body, ok = true) => Promise.resolve({ ok, status: ok ? 200 : 500, json: () => Promise.resolve(body) });

describe('nested loaders show an error instead of loading forever', () => {
  it('StemLab discipline view reports a failed request', async () => {
    vi.stubGlobal('fetch', vi.fn((url) => {
      if (String(url) === '/api/stem-lab') {
        return json({
          description: 'Experiments',
          disciplines: [{ id: 'physics', label: 'Physics', emoji: '⚡', colour: '#3366ff', description: 'Forces', experiment_count: 3 }],
        });
      }
      return json({ detail: 'boom' }, false);
    }));
    render(<StemLab />);
    fireEvent.click(await screen.findByText('Physics'));
    const alert = await screen.findByRole('alert');
    expect(alert.textContent).toMatch(/could not load/i);
    expect(screen.queryByText(/loading experiments/i)).toBeNull();
  });

  it('Virtual Museum gallery view reports a failed request', async () => {
    vi.stubGlobal('fetch', vi.fn((url) => {
      const u = String(url);
      if (u.endsWith('/museum')) {
        return json({ title: 'Museum', description: 'd', total_objects: 1, galleries: [{ id: 'ancient_world', label: 'Ancient World', emoji: '🏛️', object_count: 1 }] });
      }
      if (u.includes('/museum/featured')) return json({}, false);
      return json({ detail: 'boom' }, false);
    }));
    render(<ChildProvider><VirtualMuseum /></ChildProvider>);
    fireEvent.click(await screen.findByText('Ancient World'));
    const alert = await screen.findByRole('alert');
    expect(alert.textContent).toMatch(/could not load/i);
  });
});
