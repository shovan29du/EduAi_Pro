import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ColouringCanvas from '../src/components/ColouringCanvas.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

function makeContext() {
  return {
    setTransform: vi.fn(),
    fillRect: vi.fn(),
    strokeRect: vi.fn(),
    beginPath: vi.fn(),
    moveTo: vi.fn(),
    lineTo: vi.fn(),
    stroke: vi.fn(),
    fill: vi.fn(),
    arc: vi.fn(),
    ellipse: vi.fn(),
    save: vi.fn(),
    restore: vi.fn(),
    translate: vi.fn(),
    rotate: vi.fn(),
    drawImage: vi.fn(),
    createRadialGradient: vi.fn(() => ({ addColorStop: vi.fn() })),
    getImageData: vi.fn(() => ({ data: new Uint8ClampedArray(800 * 520 * 4) })),
    putImageData: vi.fn(),
    fillStyle: '',
    strokeStyle: '',
    lineWidth: 0,
    lineCap: '',
    lineJoin: '',
    globalAlpha: 1,
  };
}

function renderCanvas() {
  return render(
    <ChildProvider>
      <ColouringCanvas />
    </ChildProvider>
  );
}

beforeEach(() => {
  localStorage.clear();
  HTMLCanvasElement.prototype.getContext = vi.fn(() => makeContext());
  HTMLCanvasElement.prototype.toDataURL = vi.fn(() => 'data:image/png;base64,fake');
  global.fetch = vi.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({ paintings: [] }) }));
});

describe('ColouringCanvas', () => {
  it('renders all tools (including new brushes and shapes) and switches the active tool', () => {
    renderCanvas();
    const fillButton = screen.getByRole('button', { name: 'Fill', pressed: false });
    fireEvent.click(fillButton);
    expect(screen.getByRole('button', { name: 'Fill', pressed: true })).toBeInTheDocument();

    expect(screen.getByRole('button', { name: 'Airbrush' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Calligraphy' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Eyedropper' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Line' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Rectangle' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Ellipse' })).toBeInTheDocument();
  });

  it('updates colour and brush size controls, and via the palette', () => {
    renderCanvas();
    fireEvent.change(screen.getByLabelText('Colour picker'), { target: { value: '#ff0000' } });
    fireEvent.change(screen.getByLabelText('Brush size'), { target: { value: '15' } });
    expect(screen.getByLabelText('Colour picker').value).toBe('#ff0000');
    expect(screen.getByLabelText('Brush size').value).toBe('15');

    fireEvent.click(screen.getByRole('button', { name: 'Use colour #2ecc71' }));
    expect(screen.getByLabelText('Colour picker').value).toBe('#2ecc71');
  });

  it('triggers a PNG download on save', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Save as PNG' }));
    expect(HTMLCanvasElement.prototype.toDataURL).toHaveBeenCalledWith('image/png');
  });

  it('starts with undo/redo disabled, and enables undo after a stroke', () => {
    renderCanvas();
    expect(screen.getByRole('button', { name: 'Undo' })).toBeDisabled();
    expect(screen.getByRole('button', { name: 'Redo' })).toBeDisabled();

    const canvas = screen.getByRole('img', { name: 'Drawing area' });
    fireEvent.pointerDown(canvas, { clientX: 10, clientY: 10 });
    fireEvent.pointerMove(canvas, { clientX: 20, clientY: 20 });
    fireEvent.pointerUp(canvas);

    expect(screen.getByRole('button', { name: 'Undo' })).not.toBeDisabled();
  });

  it('saves a painting to My Art via the paintings API', async () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Save to My Art' }));
    await waitFor(() => {
      expect(screen.getByText('Saved to My Art!')).toBeInTheDocument();
    });
    expect(global.fetch).toHaveBeenCalledWith(
      '/api/paintings/Parent',
      expect.objectContaining({ method: 'POST' })
    );
  });
});
