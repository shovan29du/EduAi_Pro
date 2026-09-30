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

  it('opens the Quine Museum, lists quines, and loads one into the editor', async () => {
    global.fetch = vi.fn((url) => {
      if (url === '/api/quines') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            quines: [
              { language: 'python', label: 'Python', source: 'print(\'quine\')', verified: true },
              { language: 'ruby', label: 'Ruby', source: 'eval$s=1', verified: true },
            ],
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
    fireEvent.click(screen.getByRole('button', { name: /Quine Museum/i }));
    await waitFor(() => {
      expect(screen.getByRole('button', { name: 'Python' })).toBeInTheDocument();
    });
    expect(screen.getByRole('button', { name: 'Ruby' })).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: 'Python' }));
    await waitFor(() => {
      expect(screen.getByLabelText('Python code').value).toBe("print('quine')");
    });
  });

  it('renders a live preview iframe for HTML/CSS and updates it on Run', async () => {
    render(
      <ChildProvider>
        <CodeEditor />
      </ChildProvider>
    );
    fireEvent.click(screen.getByRole('radio', { name: 'HTML/CSS' }));
    expect(screen.getByText('Press Run to see the preview…')).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: '▶ Run' }));

    await waitFor(() => {
      const iframe = document.querySelector('iframe[title="HTML preview"]');
      expect(iframe).toBeInTheDocument();
      expect(iframe.getAttribute('srcdoc')).toContain('Hello, world!');
    });
  });

  it('opens the CSS Art Gallery, lists pieces, and loads one as HTML/CSS into the editor', async () => {
    global.fetch = vi.fn((url) => {
      if (url === '/api/css-art') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            pieces: [
              { id: 'rotating-cube', title: 'Rotating Cube', author: null },
              { id: 'saturn', title: 'Saturn', author: null },
            ],
          }),
        });
      }
      if (url === '/api/css-art/rotating-cube') {
        return Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            id: 'rotating-cube', title: 'Rotating Cube', author: null,
            source: '<!doctype html><html><body>cube art</body></html>',
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
    fireEvent.click(screen.getByRole('button', { name: /CSS Art Gallery/i }));
    await waitFor(() => {
      expect(screen.getByRole('button', { name: 'Rotating Cube' })).toBeInTheDocument();
    });
    expect(screen.getByRole('button', { name: 'Saturn' })).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: 'Rotating Cube' }));
    await waitFor(() => {
      expect(screen.getByLabelText('HTML/CSS code').value).toBe('<!doctype html><html><body>cube art</body></html>');
    });
  });
});
