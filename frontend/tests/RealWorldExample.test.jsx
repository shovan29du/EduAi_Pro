import React from 'react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { RealWorldExample } from '../src/components/SubjectLessons.jsx';

const lesson = { id: 'math-g5-l9', title: 'Multiplying Fractions', key_concepts: ['fraction'], reading_material: 'Multiply the tops.' };

afterEach(() => vi.unstubAllGlobals());

describe('RealWorldExample', () => {
  it('loads and shows an example on demand, passing the lesson details', async () => {
    const fetchMock = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({ example: 'A baker doubles a recipe.' }) }));
    vi.stubGlobal('fetch', fetchMock);
    render(<RealWorldExample lesson={lesson} subjectName="Math" levelId="5" />);
    fireEvent.click(screen.getByRole('button', { name: /show a real-world example/i }));
    expect(await screen.findByText('A baker doubles a recipe.')).toBeTruthy();
    const url = String(fetchMock.mock.calls[0][0]);
    expect(url).toContain('/api/lesson-example?');
    expect(url).toContain('title=Multiplying+Fractions');
    expect(url).toContain('lesson_id=math-g5-l9');
    expect(url).toContain('level=5');
  });

  it('shows a clear message when the AI tutor is not configured', async () => {
    vi.stubGlobal('fetch', vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({ example: null, unavailable: true }) })));
    render(<RealWorldExample lesson={lesson} subjectName="Math" levelId="5" />);
    fireEvent.click(screen.getByRole('button', { name: /show a real-world example/i }));
    await waitFor(() => expect(screen.getByRole('status').textContent).toMatch(/API key/));
    expect(screen.getByRole('button', { name: /try again/i })).toBeTruthy();
  });

  it('shows a stored example immediately without calling the API', () => {
    const fetchMock = vi.fn();
    vi.stubGlobal('fetch', fetchMock);
    render(<RealWorldExample lesson={{ ...lesson, real_world_example: 'Slicing a pizza.' }} subjectName="Math" levelId="5" />);
    expect(screen.getByText('Slicing a pizza.')).toBeTruthy();
    expect(fetchMock).not.toHaveBeenCalled();
  });
});
