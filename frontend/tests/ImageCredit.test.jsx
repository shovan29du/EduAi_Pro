import React from 'react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import ImageCredit from '../src/components/ImageCredit.jsx';

afterEach(() => vi.unstubAllGlobals());
const ok = (body) => Promise.resolve({ ok: true, json: () => Promise.resolve(body) });

describe('ImageCredit', () => {
  it('shows photographer, linked licence and source for a Commons photo', async () => {
    const fetchMock = vi.fn(() => ok({
      known: true, line: 'Jane Doe · CC BY-SA 4.0', artist: 'Jane Doe', license: 'CC BY-SA 4.0',
      license_url: 'https://creativecommons.org/licenses/by-sa/4.0', source_url: 'https://commons.wikimedia.org/wiki/File:Pic1.jpg',
    }));
    vi.stubGlobal('fetch', fetchMock);
    render(<ImageCredit src="https://commons.wikimedia.org/wiki/Special:FilePath/Pic1.jpg" />);
    const caption = await screen.findByTestId('image-credit');
    expect(caption.textContent).toBe('Photo: Jane Doe · CC BY-SA 4.0 · Source');
    expect(screen.getByRole('link', { name: 'CC BY-SA 4.0' }).getAttribute('href')).toBe('https://creativecommons.org/licenses/by-sa/4.0');
    expect(screen.getByRole('link', { name: 'Source' }).getAttribute('rel')).toContain('noopener');
    expect(String(fetchMock.mock.calls[0][0])).toContain('/api/museum/credit?image=');
  });

  it('credits the museum when there is no individual photographer', async () => {
    vi.stubGlobal('fetch', vi.fn(() => ok({
      known: true, line: 'Cleveland Museum of Art · CC0 1.0 (Open Access)', artist: null, license: 'CC0 1.0 (Open Access)',
      license_url: 'https://creativecommons.org/publicdomain/zero/1.0/', source_url: 'https://clevelandart.org/art/1915.534',
    })));
    render(<ImageCredit src="https://openaccess-cdn.clevelandart.org/1915.534/1915.534_web.jpg" />);
    expect((await screen.findByTestId('image-credit')).textContent).toBe('Photo: Cleveland Museum of Art · CC0 1.0 (Open Access) · Source');
  });

  it('renders nothing for placeholders and unknown or failing sources, without a request for placeholders', async () => {
    const fetchMock = vi.fn(() => ok({ known: false }));
    vi.stubGlobal('fetch', fetchMock);
    const { container, rerender } = render(<ImageCredit src="/museum-resource/thumbnails/x.svg" />);
    expect(container.innerHTML).toBe('');
    expect(fetchMock).not.toHaveBeenCalled();
    rerender(<ImageCredit src="https://example.org/pic-unknown.jpg" />);
    await waitFor(() => expect(fetchMock).toHaveBeenCalled());
    expect(container.innerHTML).toBe('');
    vi.stubGlobal('fetch', vi.fn(() => Promise.reject(new Error('offline'))));
    rerender(<ImageCredit src="https://example.org/pic-offline.jpg" />);
    await waitFor(() => expect(container.innerHTML).toBe(''));
  });
});
