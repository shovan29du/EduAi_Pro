import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import LevelSelector from '../src/components/LevelSelector.jsx';

beforeEach(() => {
  global.fetch = vi.fn(() =>
    Promise.resolve({ ok: false })
  );
});

describe('LevelSelector', () => {
  it('renders every school grade and the new college/undergraduate/master\'s levels', async () => {
    render(<LevelSelector level="1" onChange={() => {}} />);

    await waitFor(() => {
      expect(screen.getByLabelText('Select academic level')).toBeInTheDocument();
    });

    for (const label of ['Grade 1', 'Grade 10', 'College Level 1', 'College Level 2']) {
      expect(screen.getByText(label)).toBeInTheDocument();
    }
    for (let year = 1; year <= 4; year++) {
      expect(screen.getByText(`Undergraduate Year ${year}`)).toBeInTheDocument();
    }
    expect(screen.getByText("Master's Year 1")).toBeInTheDocument();
    expect(screen.getByText("Master's Year 2")).toBeInTheDocument();
  });

  it('calls onChange with the selected level id', async () => {
    const onChange = vi.fn();
    render(<LevelSelector level="1" onChange={onChange} />);
    const select = await screen.findByLabelText('Select academic level');
    fireEvent.change(select, { target: { value: 'UG2' } });
    expect(onChange).toHaveBeenCalledWith('UG2');
  });
});
