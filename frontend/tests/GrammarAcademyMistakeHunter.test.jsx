import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import GrammarAcademy from '../src/components/GrammarAcademy.jsx';

const overview = {
  title: 'English Grammar',
  description: 'Learn English grammar.',
  levels: {
    beginner: { label: 'Beginner', lessons: [] },
    elementary: { label: 'Elementary', lessons: [] },
    intermediate: { label: 'Intermediate', lessons: [] },
    advanced: { label: 'Advanced', lessons: [] },
  },
};

const exercise = {
  passage: 'Yesterday, me and my friend goes to the park.',
  mistakes: [
    { wrong: 'me and my friend goes', correct: 'my friend and I went', explanation: 'Subject pronoun and agreement.' },
  ],
};

function mockFetch() {
  return vi.fn((url, options = {}) => {
    const u = String(url);
    if (u === '/api/grammar') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(overview) });
    }
    if (u === '/api/grammar/mistake-hunt' && options.method === 'POST') {
      return Promise.resolve({ ok: true, json: () => Promise.resolve(exercise) });
    }
    if (u.startsWith('/api/levels')) {
      return Promise.resolve({ ok: true, json: () => Promise.resolve({ levels: [] }) });
    }
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

beforeEach(() => {
  global.fetch = mockFetch();
});

describe('GrammarAcademy Mistake Hunter', () => {
  it('switches into Mistake Hunter mode without waiting on the grammar curriculum fetch', async () => {
    render(<GrammarAcademy />);
    fireEvent.click(await screen.findByText('🕵️ Mistake Hunter'));
    expect(await screen.findByText('Generate exercise')).toBeInTheDocument();
  });

  it('generates a mistake-hunting exercise and reveals the answer key', async () => {
    render(<GrammarAcademy />);
    fireEvent.click(await screen.findByText('🕵️ Mistake Hunter'));
    fireEvent.click(await screen.findByText('Generate exercise'));

    expect(await screen.findByText(/Yesterday, me and my friend goes to the park\./)).toBeInTheDocument();
    expect(screen.queryByText('my friend and I went')).not.toBeInTheDocument();

    fireEvent.click(screen.getByText('Reveal answer key'));

    expect(await screen.findByText('my friend and I went')).toBeInTheDocument();
    expect(screen.getByText('Subject pronoun and agreement.')).toBeInTheDocument();
  });

  it('can switch back to Browse Lessons mode', async () => {
    render(<GrammarAcademy />);
    fireEvent.click(await screen.findByText('🕵️ Mistake Hunter'));
    await screen.findByText('Generate exercise');

    fireEvent.click(screen.getByText('📚 Browse Lessons'));

    expect(await screen.findByText('English Grammar')).toBeInTheDocument();
  });
});
