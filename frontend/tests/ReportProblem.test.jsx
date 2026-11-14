import React from 'react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ReportProblem from '../src/components/ReportProblem.jsx';
import ProblemReportsPanel from '../src/components/ProblemReportsPanel.jsx';

afterEach(() => vi.unstubAllGlobals());
const ok = (body) => Promise.resolve({ ok: true, json: () => Promise.resolve(body) });

describe('ReportProblem', () => {
  it('sends the chosen category and details for the item', async () => {
    const fetchMock = vi.fn(() => ok({ id: 'abc' }));
    vi.stubGlobal('fetch', fetchMock);
    render(<ReportProblem kind="museum_object" itemId="wc_0076" title="Andorra Painting" context="world_visual_arts" />);
    fireEvent.click(screen.getByRole('button', { name: /report a problem/i }));
    fireEvent.change(screen.getByRole('combobox'), { target: { value: 'wrong_or_missing_image' } });
    fireEvent.change(screen.getByRole('textbox'), { target: { value: 'Shows a flag' } });
    fireEvent.click(screen.getByRole('button', { name: /send report/i }));
    expect((await screen.findByRole('status')).textContent).toMatch(/report was sent/i);
    const [url, options] = fetchMock.mock.calls[0];
    expect(url).toBe('/api/reports');
    expect(JSON.parse(options.body)).toMatchObject({
      kind: 'museum_object', item_id: 'wc_0076', title: 'Andorra Painting',
      category: 'wrong_or_missing_image', message: 'Shows a flag', context: 'world_visual_arts',
    });
  });

  it('requires details for "Something else" and shows server errors', async () => {
    const fetchMock = vi.fn(() => Promise.resolve({ ok: false, status: 500, json: () => Promise.resolve({ detail: 'Server is busy' }) }));
    vi.stubGlobal('fetch', fetchMock);
    render(<ReportProblem kind="lesson" itemId="l1" title="Fractions" />);
    fireEvent.click(screen.getByRole('button', { name: /report a problem/i }));
    fireEvent.change(screen.getByRole('combobox'), { target: { value: 'other' } });
    fireEvent.click(screen.getByRole('button', { name: /send report/i }));
    expect(screen.getByRole('alert').textContent).toMatch(/describe the problem/i);
    expect(fetchMock).not.toHaveBeenCalled();
    fireEvent.change(screen.getByRole('textbox'), { target: { value: 'The table is cut off' } });
    fireEvent.click(screen.getByRole('button', { name: /send report/i }));
    await waitFor(() => expect(screen.getByRole('alert').textContent).toMatch(/server is busy/i));
  });
});

describe('ProblemReportsPanel', () => {
  it('lists open reports and marks one resolved', async () => {
    const report = { id: 'r1', kind: 'lesson', item_id: 'math-g5-l1', title: 'Percentages', category: 'typo', message: 'Typo', status: 'open', created_at: '2026-11-13T10:00:00+00:00' };
    const fetchMock = vi.fn((url, options = {}) => {
      if (options.method === 'PATCH') return ok({ ...report, status: 'resolved' });
      return ok({ reports: fetchMock.mock.calls.some(([, o]) => o?.method === 'PATCH') ? [] : [report], open_count: 1 });
    });
    vi.stubGlobal('fetch', fetchMock);
    render(<ProblemReportsPanel />);
    expect(await screen.findByText(/Lesson: Percentages/)).toBeTruthy();
    expect(String(fetchMock.mock.calls[0][0])).toBe('/api/reports?status=open');
    fireEvent.click(screen.getByRole('button', { name: /mark resolved/i }));
    expect(await screen.findByText(/no open reports/i)).toBeTruthy();
    const patch = fetchMock.mock.calls.find(([, o]) => o?.method === 'PATCH');
    expect(patch[0]).toBe('/api/reports/r1');
  });
});
