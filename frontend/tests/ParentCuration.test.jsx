import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ParentCuration from '../src/components/ParentCuration.jsx';

beforeEach(() => {
  global.fetch = vi.fn((url) => {
    if (url.startsWith('/api/web-search')) {
      return Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve([
            { title: 'Free Math Game', url: 'https://example.com/math-game', description: 'A fun math game.' },
          ]),
      });
    }
    if (url === '/api/curate-resource') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ safe: true }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('ParentCuration', () => {
  it('searches the web and lists results for review', async () => {
    render(<ParentCuration standard={1} />);
    fireEvent.change(screen.getByLabelText('Search query'), { target: { value: 'math games' } });
    fireEvent.click(screen.getByRole('button', { name: 'Search web' }));

    await waitFor(() => {
      expect(screen.getByText('Free Math Game')).toBeInTheDocument();
    });
    expect(global.fetch).toHaveBeenCalledWith('/api/web-search?q=math%20games');
  });

  it('requires a subject before adding a resource', async () => {
    render(<ParentCuration standard={1} />);
    fireEvent.change(screen.getByLabelText('Search query'), { target: { value: 'math games' } });
    fireEvent.click(screen.getByRole('button', { name: 'Search web' }));
    await waitFor(() => screen.getByText('Free Math Game'));

    fireEvent.click(screen.getByRole('button', { name: 'Add to syllabus' }));
    await waitFor(() => {
      expect(screen.getByText('Enter a subject name before adding a resource.')).toBeInTheDocument();
    });
  });

  it('adds a reviewed resource to the syllabus via curate-resource', async () => {
    render(<ParentCuration standard={1} />);
    fireEvent.change(screen.getByLabelText('Search query'), { target: { value: 'math games' } });
    fireEvent.click(screen.getByRole('button', { name: 'Search web' }));
    await waitFor(() => screen.getByText('Free Math Game'));

    fireEvent.change(screen.getByLabelText('Subject'), { target: { value: 'Math' } });
    fireEvent.click(screen.getByRole('button', { name: 'Add to syllabus' }));

    await waitFor(() => {
      expect(screen.getByRole('button', { name: 'Added ✓' })).toBeInTheDocument();
    });
    expect(global.fetch).toHaveBeenCalledWith(
      '/api/curate-resource',
      expect.objectContaining({ method: 'POST' })
    );
  });
});

function selectFile() {
  const input = document.querySelector('input[name="bookFile"]');
  const file = new File(['some book text'], 'botany.txt', { type: 'text/plain' });
  Object.defineProperty(input, 'files', { value: [file] });
  fireEvent.change(input);
}

describe('ParentCuration book upload topic linking', () => {
  it('shows which lesson topics Ark AI linked the book to', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      if (url === '/api/upload-safe-book' && options.method === 'POST') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            filename: 'botany.txt', status: 'accepted', type: 'txt',
            summary: 'A short summary about photosynthesis.',
            added_resource: { safe: true },
            topics_linked: ['Photosynthesis'],
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ParentCuration standard={11} />);
    fireEvent.change(screen.getByPlaceholderText('e.g. World Literature'), { target: { value: 'Science' } });
    selectFile();
    fireEvent.click(screen.getByText('Upload & summarize'));

    expect(await screen.findByText('Added to syllabus ✓')).toBeInTheDocument();
    expect(screen.getByText(/Ark AI linked this book to 1 topic: Photosynthesis/)).toBeInTheDocument();
  });

  it('does not show topic-linking text when nothing matched', async () => {
    global.fetch = vi.fn((url, options = {}) => {
      if (url === '/api/upload-safe-book' && options.method === 'POST') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            filename: 'botany.txt', status: 'accepted', type: 'txt',
            summary: 'A short summary.', added_resource: { safe: true }, topics_linked: [],
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(<ParentCuration standard={11} />);
    fireEvent.change(screen.getByPlaceholderText('e.g. World Literature'), { target: { value: 'Science' } });
    selectFile();
    fireEvent.click(screen.getByText('Upload & summarize'));

    expect(await screen.findByText('Added to syllabus ✓')).toBeInTheDocument();
    expect(screen.queryByText(/Ark AI linked this book/)).not.toBeInTheDocument();
  });
});
