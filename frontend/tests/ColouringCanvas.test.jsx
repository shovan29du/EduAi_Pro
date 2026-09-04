import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ColouringCanvas from '../src/components/ColouringCanvas.jsx';
import { ChildProvider } from '../src/contexts/ChildContext.jsx';

function makeContext() {
  return {
    setTransform: vi.fn(),
    fillRect: vi.fn(),
    clearRect: vi.fn(),
    strokeRect: vi.fn(),
    beginPath: vi.fn(),
    closePath: vi.fn(),
    moveTo: vi.fn(),
    lineTo: vi.fn(),
    bezierCurveTo: vi.fn(),
    quadraticCurveTo: vi.fn(),
    stroke: vi.fn(),
    fill: vi.fn(),
    fillText: vi.fn(),
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
    globalCompositeOperation: 'source-over',
    font: '',
    textAlign: '',
    textBaseline: '',
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
  // Cache one mock context per canvas element (rather than a fresh object on
  // every getContext() call) so tests can assert on calls made to a
  // particular canvas -- e.g. fillText calls made while placing text/stickers
  // onto the "Drawing area" canvas across several getContext() lookups.
  const contexts = new WeakMap();
  HTMLCanvasElement.prototype.getContext = vi.fn(function getContext() {
    if (!contexts.has(this)) contexts.set(this, makeContext());
    return contexts.get(this);
  });
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
      '/api/paintings/Shovan',
      expect.objectContaining({ method: 'POST' })
    );
  });

  it('lets a child pick a colouring template, which pre-fills the title and closes the picker', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Templates' }));
    fireEvent.click(screen.getByRole('button', { name: 'Use template Flower' }));

    // Selecting a template starts a fresh painting and closes the picker.
    expect(screen.getByLabelText('Painting title').value).toBe('My Flower');
    expect(screen.queryByRole('button', { name: 'Use template Flower' })).not.toBeInTheDocument();

    // Reopening the picker shows the selection was remembered.
    fireEvent.click(screen.getByRole('button', { name: 'Templates' }));
    expect(screen.getByRole('button', { name: 'Use template Flower' })).toHaveAttribute('aria-pressed', 'true');
  });

  it('shows a layers panel with visibility toggles for background/drawing, plus outline once a template is active', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Layers' }));
    const bgToggle = screen.getByLabelText('Toggle background layer visibility');
    const drawingToggle = screen.getByLabelText('Toggle drawing layer visibility');
    expect(bgToggle.checked).toBe(true);
    expect(drawingToggle.checked).toBe(true);

    fireEvent.click(bgToggle);
    expect(bgToggle.checked).toBe(false);

    expect(screen.queryByLabelText('Toggle outline layer visibility')).not.toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: 'Templates' }));
    fireEvent.click(screen.getByRole('button', { name: 'Use template Star' }));

    expect(screen.getByLabelText('Toggle outline layer visibility')).toBeInTheDocument();
  });

  it('supports reordering the background and drawing layers', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Layers' }));
    const moveBackground = screen.getByRole('button', { name: 'Move background layer' });
    // Initially drawing sits above background in the panel (drawing = top entry = "Send back").
    expect(screen.getByRole('button', { name: 'Move drawing layer' })).toHaveTextContent('Send back');
    expect(screen.getByRole('button', { name: 'Move background layer' })).toHaveTextContent('Bring forward');
    fireEvent.click(moveBackground);
    // After swapping, background should now be the top entry.
    expect(screen.getByRole('button', { name: 'Move background layer' })).toHaveTextContent('Send back');
    expect(screen.getByRole('button', { name: 'Move drawing layer' })).toHaveTextContent('Bring forward');
  });

  it('toggles horizontal and vertical mirror/symmetry mode', () => {
    renderCanvas();
    const mirrorH = screen.getByLabelText('Mirror horizontally');
    const mirrorV = screen.getByLabelText('Mirror vertically');
    expect(mirrorH.checked).toBe(false);
    expect(mirrorV.checked).toBe(false);

    fireEvent.click(mirrorH);
    fireEvent.click(mirrorV);

    expect(mirrorH.checked).toBe(true);
    expect(mirrorV.checked).toBe(true);
  });

  it('lets a child place a text label on the canvas with the Text tool', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Text' }));
    const canvas = screen.getByRole('img', { name: 'Drawing area' });
    fireEvent.pointerDown(canvas, { clientX: 40, clientY: 40 });

    const input = screen.getByLabelText('Text to add to canvas');
    fireEvent.change(input, { target: { value: 'Hi' } });
    fireEvent.keyDown(input, { key: 'Enter' });

    expect(screen.queryByLabelText('Text to add to canvas')).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Undo' })).not.toBeDisabled();
  });

  it('discards the text draft on Escape without adding it to the undo history', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Text' }));
    const canvas = screen.getByRole('img', { name: 'Drawing area' });
    fireEvent.pointerDown(canvas, { clientX: 40, clientY: 40 });

    const input = screen.getByLabelText('Text to add to canvas');
    fireEvent.change(input, { target: { value: 'Nope' } });
    fireEvent.keyDown(input, { key: 'Escape' });

    expect(screen.queryByLabelText('Text to add to canvas')).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Undo' })).toBeDisabled();
  });

  it('offers an emoji sticker library and stamps the selected sticker onto the canvas', () => {
    renderCanvas();
    fireEvent.click(screen.getByRole('button', { name: 'Stickers' }));
    const stickerButtons = screen.getAllByRole('button', { name: /^Sticker / });
    expect(stickerButtons.length).toBeGreaterThanOrEqual(8);

    fireEvent.click(stickerButtons[1]);
    expect(stickerButtons[1]).toHaveAttribute('aria-pressed', 'true');

    const canvas = screen.getByRole('img', { name: 'Drawing area' });
    fireEvent.pointerDown(canvas, { clientX: 60, clientY: 60 });

    expect(screen.getByRole('button', { name: 'Undo' })).not.toBeDisabled();
  });
});
