import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import CodeEditor from '../src/components/CodeEditor.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

// CodeMirror 6 needs real browser layout APIs (getClientRects etc.) that
// jsdom doesn't implement, so it can't actually render/measure in tests.
// Stub it with a plain textarea wired to the same value/onChange contract
// (@uiw/react-codemirror's onChange receives just the new string value) --
// the standard pattern for testing rich-text/code editors under jsdom.
vi.mock('@uiw/react-codemirror', () => ({
  default: ({ value, onChange, ...rest }) => (
    <textarea
      aria-label={rest['aria-label']}
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  ),
}));

beforeEach(() => {
  localStorage.clear();
  global.fetch = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({}) }));
});

describe('CodeEditor', () => {
  it('renders default code and lets the user edit it', () => {
    render(
      <ChildProvider>
        <CodeEditor />
      </ChildProvider>
    );
    const editor = screen.getByLabelText('JavaScript code');
    expect(editor.value).toContain('Hello, world!');
    fireEvent.change(editor, { target: { value: 'console.log(1+1)' } });
    expect(editor.value).toBe('console.log(1+1)');
  });

  it('switches language and loads that language\'s default code plus a starter blurb', () => {
    render(
      <ChildProvider>
        <CodeEditor />
      </ChildProvider>
    );
    fireEvent.click(screen.getByRole('radio', { name: 'Python' }));
    expect(screen.getByLabelText('Python code').value).toContain('Hello, world!');
    expect(screen.getByText(/reads almost like English/i)).toBeInTheDocument();
  });

  it('saves a snippet via the progress API', async () => {
    render(
      <ChildProvider>
        <CodeEditor />
      </ChildProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: 'Save snippet' }));
    await waitFor(() => {
      expect(screen.getByText('Saved!')).toBeInTheDocument();
    });
    expect(global.fetch).toHaveBeenCalledWith(
      '/api/progress/Shovan',
      expect.objectContaining({ method: 'POST' })
    );
  });

  it('opens the snippet browser, lists a saved snippet, and loads it back into the editor', async () => {
    global.fetch = vi.fn((url) => {
      if (url === '/api/progress/Shovan') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            snippets: {
              'snippet-1700000000000': { code: 'print("saved snippet")', language: 'python', savedAt: 1700000000000 },
            },
          }),
        });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(
      <ChildProvider>
        <CodeEditor />
      </ChildProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: /My Snippets/i }));
    await waitFor(() => {
      expect(screen.getByText(/print\("saved snippet"\)/)).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText(/print\("saved snippet"\)/));
    await waitFor(() => {
      expect(screen.getByLabelText('Python code').value).toBe('print("saved snippet")');
    });
  });

  it('deletes a snippet via the DELETE endpoint', async () => {
    global.fetch = vi.fn((url, opts) => {
      if (url === '/api/progress/Shovan') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            snippets: { 'snippet-1': { code: 'x = 1', language: 'python', savedAt: 1 } },
          }),
        });
      }
      if (opts?.method === 'DELETE') {
        return Promise.resolve({ ok: true, json: () => Promise.resolve({ snippets: {} }) });
      }
      return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
    });

    render(
      <ChildProvider>
        <CodeEditor />
      </ChildProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: /My Snippets/i }));
    await waitFor(() => screen.getByText(/x = 1/));

    fireEvent.click(screen.getByRole('button', { name: /Delete snippet/i }));
    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith('/api/progress/Shovan/snippets/snippet-1', expect.objectContaining({ method: 'DELETE' }));
    });
  });
});
