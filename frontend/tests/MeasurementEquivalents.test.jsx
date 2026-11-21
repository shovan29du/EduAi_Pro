import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import MeasurementEquivalents from '../src/components/MeasurementEquivalents.jsx';

const data = {
  title: 'Measurement Equivalents',
  description: 'Standard kitchen conversion tables.',
  tables: [
    { id: 'volume', label: 'Volume', emoji: '🥄', rows: [{ from: '1 teaspoon', to: '5 ml' }] },
    { id: 'oven_temperature', label: 'Oven Temperature', emoji: '🔥', rows: [{ from: '350°F', to: '177°C / Gas Mark 4' }] },
  ],
};

function mockFetch() {
  return vi.fn((url) => {
    const u = String(url);
    if (u === '/api/cuisine-detail/measurement-equivalents') return Promise.resolve({ ok: true, json: () => Promise.resolve(data) });
    return Promise.resolve({ ok: true, json: () => Promise.resolve({}) });
  });
}

describe('MeasurementEquivalents', () => {
  it('shows conversion tables', async () => {
    global.fetch = mockFetch();
    render(<MeasurementEquivalents />);
    expect(await screen.findByText('Volume')).toBeInTheDocument();
    expect(screen.getByText('1 teaspoon')).toBeInTheDocument();
    expect(screen.getByText(/5 ml/)).toBeInTheDocument();
    expect(screen.getByText('Oven Temperature')).toBeInTheDocument();
  });
});
