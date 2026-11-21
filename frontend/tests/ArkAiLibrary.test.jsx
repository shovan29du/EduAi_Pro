import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ArkAiLibrary from '../src/components/ArkAiLibrary.jsx';

const prompts = [
  { id: 'p1', name: 'Research Agent', tag: 'ai', prompt: 'You are an expert in research.' },
  { id: 'p2', name: 'Code Reviewer', tag: 'code', prompt: 'You are an expert in code review.' },
];

const models = [
  { id: 'claude:claude-opus-4-8', name: 'Claude Opus 4.8', provider: 'Claude', raw: 'claude-opus-4-8' },
  { id: 'openai:gpt-5', name: 'GPT-5', provider: 'Openai', raw: 'gpt-5' },
];

const tools = [
  { id: 'vscode', name: 'Visual Studio Code', category: 'Coding', kind: 'software', note: 'Free code editor.', url: 'https://code.visualstudio.com/' },
  { id: 'memory', name: 'Memory', category: 'Personal', kind: 'plugin', note: 'Recall saved facts.', url: '' },
];

beforeEach(() => {
  global.fetch = vi.fn((url) => {
    const u = String(url);
    if (u.startsWith('/api/ark-ai/prompts/')) {
      const id = u.split('/').pop();
      const found = prompts.find((p) => p.id === id);
      return found
        ? Promise.resolve({ ok: true, json: () => Promise.resolve(found) })
        : Promise.resolve({ ok: false, status: 404, json: () => Promise.resolve({ detail: 'not found' }) });
    }
    if (u.startsWith('/api/ark-ai/prompts')) {
      const params = new URL(u, 'http://localhost').searchParams;
      const q = (params.get('q') || '').toLowerCase();
      const tag = params.get('tag') || '';
      let filtered = prompts;
      if (q) filtered = filtered.filter((p) => p.name.toLowerCase().includes(q) || p.prompt.toLowerCase().includes(q));
      if (tag) filtered = filtered.filter((p) => p.tag === tag);
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ prompts: filtered, tags: ['ai', 'code'] }) });
    }
    if (u.startsWith('/api/ark-ai/models')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ models }) });
    }
    if (u.startsWith('/api/ark-ai/tools')) {
      const params = new URL(u, 'http://localhost').searchParams;
      const kind = params.get('kind') || '';
      let filtered = tools;
      if (kind) filtered = filtered.filter((t) => t.kind === kind);
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ tools: filtered, categories: ['Coding', 'Personal'], kinds: ['software', 'plugin'] }),
      });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
});

describe('ArkAiLibrary', () => {
  it('shows the prompt library by default and expands a prompt', async () => {
    render(<ArkAiLibrary />);
    expect(await screen.findByText('Research Agent')).toBeInTheDocument();
    expect(screen.getByText('Code Reviewer')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Research Agent'));
    expect(await screen.findByText('You are an expert in research.')).toBeInTheDocument();
  });

  it('filters prompts by search query', async () => {
    render(<ArkAiLibrary />);
    await screen.findByText('Research Agent');

    fireEvent.change(screen.getByPlaceholderText('Search prompts…'), { target: { value: 'code' } });

    await waitFor(() => {
      expect(screen.queryByText('Research Agent')).not.toBeInTheDocument();
      expect(screen.getByText('Code Reviewer')).toBeInTheDocument();
    });
  });

  it('calls onUsePrompt with the full prompt text', async () => {
    const onUsePrompt = vi.fn();
    render(<ArkAiLibrary onUsePrompt={onUsePrompt} />);
    await screen.findByText('Research Agent');

    fireEvent.click(screen.getByText('Research Agent'));
    await screen.findByText('You are an expert in research.');
    fireEvent.click(screen.getByText('Use as Ark AI context'));

    expect(onUsePrompt).toHaveBeenCalledWith('You are an expert in research.');
  });

  it('shows the model catalog grouped by provider with an accuracy disclaimer', async () => {
    render(<ArkAiLibrary />);
    fireEvent.click(screen.getByRole('tab', { name: 'Models' }));

    expect(await screen.findByText(/Claude \(1\)/)).toBeInTheDocument();
    expect(screen.getByText('Claude Opus 4.8')).toBeInTheDocument();
    expect(screen.getByText(/only ever calls Claude/)).toBeInTheDocument();
  });

  it('shows the tools directory with links', async () => {
    render(<ArkAiLibrary />);
    fireEvent.click(screen.getByRole('tab', { name: 'Tools' }));

    expect(await screen.findByText('Visual Studio Code')).toBeInTheDocument();
    expect(screen.getByText('Visual Studio Code').closest('a')).toHaveAttribute('href', 'https://code.visualstudio.com/');
    expect(screen.getByText('Memory')).toBeInTheDocument();
  });
});
