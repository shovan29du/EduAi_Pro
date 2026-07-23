import React, { useCallback, useEffect, useRef, useState } from 'react';
import { useChild } from '../contexts/ChildContext.jsx';
import { fetchPaintings, savePainting, deletePainting, paintingImageUrl } from '../api/paintings.js';

const DRAW_TOOLS = [
  { id: 'pencil', label: 'Pencil' },
  { id: 'brush', label: 'Brush' },
  { id: 'airbrush', label: 'Airbrush' },
  { id: 'calligraphy', label: 'Calligraphy' },
  { id: 'eraser', label: 'Eraser' },
  { id: 'fill', label: 'Fill' },
  { id: 'eyedropper', label: 'Eyedropper' },
];

const SHAPE_TOOLS = [
  { id: 'line', label: 'Line' },
  { id: 'rectangle', label: 'Rectangle' },
  { id: 'ellipse', label: 'Ellipse' },
];

const ALL_TOOLS = [...DRAW_TOOLS, ...SHAPE_TOOLS];

const PALETTE = [
  '#000000', '#ffffff', '#7f7f7f', '#c0392b', '#e74c3c', '#e67e22',
  '#f1c40f', '#2ecc71', '#1abc9c', '#3498db', '#1d4ed8', '#8e44ad',
  '#d63384', '#a0522d', '#795548',
];

const MAX_HISTORY = 30;
const NIB_ANGLE = (40 * Math.PI) / 180; // fixed calligraphy nib angle

function getPixelIndex(x, y, width) {
  return (y * width + x) * 4;
}

function colorsMatch(data, idx, target, tolerance = 32) {
  return (
    Math.abs(data[idx] - target[0]) <= tolerance &&
    Math.abs(data[idx + 1] - target[1]) <= tolerance &&
    Math.abs(data[idx + 2] - target[2]) <= tolerance &&
    Math.abs(data[idx + 3] - target[3]) <= tolerance
  );
}

function hexToRgba(hex) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return [r, g, b, 255];
}

function rgbaToHex(r, g, b) {
  const toHex = (n) => n.toString(16).padStart(2, '0');
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

function floodFill(ctx, startX, startY, fillColor) {
  const canvas = ctx.canvas;
  const { width, height } = canvas;
  const imageData = ctx.getImageData(0, 0, width, height);
  const data = imageData.data;

  const startIdx = getPixelIndex(startX, startY, width);
  const target = [data[startIdx], data[startIdx + 1], data[startIdx + 2], data[startIdx + 3]];
  if (colorsMatch(data, startIdx, fillColor, 0)) return;

  const stack = [[startX, startY]];
  while (stack.length) {
    const [x, y] = stack.pop();
    if (x < 0 || x >= width || y < 0 || y >= height) continue;
    const idx = getPixelIndex(x, y, width);
    if (!colorsMatch(data, idx, target)) continue;

    data[idx] = fillColor[0];
    data[idx + 1] = fillColor[1];
    data[idx + 2] = fillColor[2];
    data[idx + 3] = fillColor[3];

    stack.push([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]);
  }
  ctx.putImageData(imageData, 0, 0);
}

export default function ColouringCanvas() {
  const { child } = useChild();
  const containerRef = useRef(null);
  const canvasRef = useRef(null);
  const baseSnapshotRef = useRef(null); // offscreen canvas: pixels before an in-progress shape/stroke
  const drawingRef = useRef(false);
  const lastPointRef = useRef(null);
  const shapeStartRef = useRef(null);
  const dprRef = useRef(1);
  const sizeRef = useRef({ width: 800, height: 520 });
  const undoStackRef = useRef([]);
  const redoStackRef = useRef([]);

  const [tool, setTool] = useState('pencil');
  const [color, setColor] = useState('#1d4ed8');
  const [brushSize, setBrushSize] = useState(6);
  const [canUndo, setCanUndo] = useState(false);
  const [canRedo, setCanRedo] = useState(false);
  const [gallery, setGallery] = useState([]);
  const [galleryOpen, setGalleryOpen] = useState(false);
  const [activePaintingId, setActivePaintingId] = useState(null);
  const [title, setTitle] = useState('My Painting');
  const [status, setStatus] = useState('');

  const isShapeTool = SHAPE_TOOLS.some((s) => s.id === tool);

  // ── Canvas setup: size to container, scale for device pixel ratio ────────
  const applyCanvasSize = useCallback((logicalWidth, logicalHeight, preserveContent) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const dpr = window.devicePixelRatio || 1;

    let previous = null;
    if (preserveContent && canvas.width > 0 && canvas.height > 0) {
      previous = document.createElement('canvas');
      previous.width = canvas.width;
      previous.height = canvas.height;
      previous.getContext('2d').drawImage(canvas, 0, 0);
    }

    canvas.width = Math.max(1, Math.round(logicalWidth * dpr));
    canvas.height = Math.max(1, Math.round(logicalHeight * dpr));
    canvas.style.width = `${logicalWidth}px`;
    canvas.style.height = `${logicalHeight}px`;

    dprRef.current = dpr;
    sizeRef.current = { width: logicalWidth, height: logicalHeight };

    const ctx = canvas.getContext('2d');
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (previous) {
      ctx.drawImage(previous, 0, 0, previous.width, previous.height, 0, 0, canvas.width, canvas.height);
    }

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    if (!baseSnapshotRef.current) baseSnapshotRef.current = document.createElement('canvas');
    baseSnapshotRef.current.width = canvas.width;
    baseSnapshotRef.current.height = canvas.height;
  }, []);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    // Initial size
    const rect = container.getBoundingClientRect();
    const width = Math.max(240, Math.round(rect.width) || 800);
    const height = Math.max(240, Math.min(640, Math.round(width * 0.62)));
    applyCanvasSize(width, height, false);
    pushHistory();

    if (typeof ResizeObserver === 'undefined') return undefined;

    let frame = null;
    const observer = new ResizeObserver((entries) => {
      const entry = entries[0];
      if (!entry) return;
      if (frame) cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const w = Math.max(240, Math.round(entry.contentRect.width));
        const h = Math.max(240, Math.min(640, Math.round(w * 0.62)));
        const { width: curW, height: curH } = sizeRef.current;
        if (Math.abs(curW - w) < 2 && Math.abs(curH - h) < 2) return;
        applyCanvasSize(w, h, true);
      });
    });
    observer.observe(container);

    return () => {
      observer.disconnect();
      if (frame) cancelAnimationFrame(frame);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [applyCanvasSize]);

  // ── Undo / redo history (PNG snapshots so it survives resizes) ───────────
  function pushHistory() {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const snapshot = canvas.toDataURL('image/png');
    const stack = undoStackRef.current;
    stack.push(snapshot);
    if (stack.length > MAX_HISTORY) stack.shift();
    redoStackRef.current = [];
    setCanUndo(stack.length > 1);
    setCanRedo(false);
  }

  function restoreSnapshot(dataUrl) {
    return new Promise((resolve) => {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');
      const img = new Image();
      img.onload = () => {
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        ctx.setTransform(dprRef.current, 0, 0, dprRef.current, 0, 0);
        resolve();
      };
      img.onerror = () => resolve();
      img.src = dataUrl;
    });
  }

  async function handleUndo() {
    const undoStack = undoStackRef.current;
    if (undoStack.length <= 1) return;
    const current = undoStack.pop();
    redoStackRef.current.push(current);
    const previous = undoStack[undoStack.length - 1];
    await restoreSnapshot(previous);
    setCanUndo(undoStack.length > 1);
    setCanRedo(true);
  }

  async function handleRedo() {
    const redoStack = redoStackRef.current;
    if (!redoStack.length) return;
    const next = redoStack.pop();
    undoStackRef.current.push(next);
    await restoreSnapshot(next);
    setCanUndo(true);
    setCanRedo(redoStack.length > 0);
  }

  useEffect(() => {
    function handleKeydown(e) {
      const meta = e.ctrlKey || e.metaKey;
      if (!meta) return;
      const key = e.key.toLowerCase();
      if (key === 'z' && !e.shiftKey) {
        e.preventDefault();
        handleUndo();
      } else if (key === 'y' || (key === 'z' && e.shiftKey)) {
        e.preventDefault();
        handleRedo();
      }
    }
    window.addEventListener('keydown', handleKeydown);
    return () => window.removeEventListener('keydown', handleKeydown);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // ── Pointer position helpers ──────────────────────────────────────────────
  function getPos(e) {
    const rect = canvasRef.current.getBoundingClientRect();
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  }

  function toPixelCoords(pos) {
    const dpr = dprRef.current;
    return {
      x: Math.min(canvasRef.current.width - 1, Math.max(0, Math.floor(pos.x * dpr))),
      y: Math.min(canvasRef.current.height - 1, Math.max(0, Math.floor(pos.y * dpr))),
    };
  }

  function snapshotBase() {
    const canvas = canvasRef.current;
    const base = baseSnapshotRef.current;
    base.width = canvas.width;
    base.height = canvas.height;
    base.getContext('2d').drawImage(canvas, 0, 0);
  }

  function restoreBaseInPlace(ctx) {
    const canvas = canvasRef.current;
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.drawImage(baseSnapshotRef.current, 0, 0);
    ctx.restore();
  }

  // ── Freehand brush strokes ─────────────────────────────────────────────
  function strokeSegment(ctx, from, to) {
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    if (tool === 'eraser') {
      ctx.strokeStyle = '#ffffff';
      ctx.globalAlpha = 1;
      ctx.lineWidth = brushSize * 1.6;
    } else if (tool === 'brush') {
      ctx.strokeStyle = color;
      ctx.globalAlpha = 0.92;
      ctx.lineWidth = brushSize * 2;
    } else {
      ctx.strokeStyle = color;
      ctx.globalAlpha = 1;
      ctx.lineWidth = brushSize;
    }
    ctx.beginPath();
    ctx.moveTo(from.x, from.y);
    ctx.lineTo(to.x, to.y);
    ctx.stroke();
    ctx.globalAlpha = 1;
  }

  function airbrushDab(ctx, point) {
    const radius = brushSize * 1.8;
    const [r, g, b] = hexToRgba(color);
    const gradient = ctx.createRadialGradient(point.x, point.y, 0, point.x, point.y, radius);
    gradient.addColorStop(0, `rgba(${r},${g},${b},0.35)`);
    gradient.addColorStop(1, `rgba(${r},${g},${b},0)`);
    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.arc(point.x, point.y, radius, 0, Math.PI * 2);
    ctx.fill();
  }

  function airbrushSegment(ctx, from, to) {
    const dist = Math.hypot(to.x - from.x, to.y - from.y);
    const steps = Math.max(1, Math.round(dist / (brushSize * 0.4)));
    for (let i = 0; i <= steps; i++) {
      const t = i / steps;
      airbrushDab(ctx, { x: from.x + (to.x - from.x) * t, y: from.y + (to.y - from.y) * t });
    }
  }

  function calligraphyStamp(ctx, point) {
    const length = brushSize * 2.2;
    const thickness = Math.max(2, brushSize * 0.55);
    ctx.save();
    ctx.translate(point.x, point.y);
    ctx.rotate(NIB_ANGLE);
    ctx.fillStyle = color;
    ctx.fillRect(-length / 2, -thickness / 2, length, thickness);
    ctx.restore();
  }

  function calligraphySegment(ctx, from, to) {
    const dist = Math.hypot(to.x - from.x, to.y - from.y);
    const steps = Math.max(1, Math.round(dist / (brushSize * 0.3)));
    for (let i = 0; i <= steps; i++) {
      const t = i / steps;
      calligraphyStamp(ctx, { x: from.x + (to.x - from.x) * t, y: from.y + (to.y - from.y) * t });
    }
  }

  // ── Shape preview (drag to draw, committed on release) ──────────────────
  function drawShapePreview(ctx, start, current) {
    restoreBaseInPlace(ctx);
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = brushSize;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    if (tool === 'line') {
      ctx.beginPath();
      ctx.moveTo(start.x, start.y);
      ctx.lineTo(current.x, current.y);
      ctx.stroke();
    } else if (tool === 'rectangle') {
      const x = Math.min(start.x, current.x);
      const y = Math.min(start.y, current.y);
      const w = Math.abs(current.x - start.x);
      const h = Math.abs(current.y - start.y);
      ctx.strokeRect(x, y, w, h);
    } else if (tool === 'ellipse') {
      const cx = (start.x + current.x) / 2;
      const cy = (start.y + current.y) / 2;
      const rx = Math.abs(current.x - start.x) / 2;
      const ry = Math.abs(current.y - start.y) / 2;
      ctx.beginPath();
      ctx.ellipse(cx, cy, Math.max(rx, 0.01), Math.max(ry, 0.01), 0, 0, Math.PI * 2);
      ctx.stroke();
    }
  }

  // ── Pointer handlers ──────────────────────────────────────────────────────
  function handlePointerDown(e) {
    const canvas = canvasRef.current;
    canvas.setPointerCapture?.(e.pointerId);
    const ctx = canvas.getContext('2d');
    const pos = getPos(e);

    if (tool === 'fill') {
      const px = toPixelCoords(pos);
      floodFill(ctx, px.x, px.y, hexToRgba(color));
      pushHistory();
      return;
    }

    if (tool === 'eyedropper') {
      const px = toPixelCoords(pos);
      const data = ctx.getImageData(px.x, px.y, 1, 1).data;
      setColor(rgbaToHex(data[0], data[1], data[2]));
      return;
    }

    drawingRef.current = true;
    lastPointRef.current = pos;
    snapshotBase();

    if (isShapeTool) {
      drawShapePreview(ctx, pos, pos);
    } else if (tool === 'airbrush') {
      airbrushDab(ctx, pos);
    } else if (tool === 'calligraphy') {
      calligraphyStamp(ctx, pos);
    } else {
      strokeSegment(ctx, pos, pos);
    }
  }

  function handlePointerMove(e) {
    if (!drawingRef.current) return;
    const ctx = canvasRef.current.getContext('2d');
    const pos = getPos(e);

    if (isShapeTool) {
      drawShapePreview(ctx, shapeStartRef.current || pos, pos);
      return;
    }

    const from = lastPointRef.current || pos;
    if (tool === 'airbrush') {
      airbrushSegment(ctx, from, pos);
    } else if (tool === 'calligraphy') {
      calligraphySegment(ctx, from, pos);
    } else {
      strokeSegment(ctx, from, pos);
    }
    lastPointRef.current = pos;
  }

  function handlePointerDownWrapped(e) {
    const pos = getPos(e);
    shapeStartRef.current = pos;
    handlePointerDown(e);
  }

  function handlePointerUp() {
    if (!drawingRef.current) return;
    drawingRef.current = false;
    lastPointRef.current = null;
    pushHistory();
  }

  function handleClear() {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.setTransform(dprRef.current, 0, 0, dprRef.current, 0, 0);
    pushHistory();
  }

  function handleSave() {
    const canvas = canvasRef.current;
    const link = document.createElement('a');
    link.download = 'my-artwork.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  }

  // ── "My Art" gallery (server-persisted per child) ────────────────────────
  const loadGallery = useCallback(async () => {
    try {
      const body = await fetchPaintings(child);
      setGallery(body.paintings || []);
    } catch {
      setGallery([]);
    }
  }, [child]);

  useEffect(() => {
    loadGallery();
  }, [loadGallery]);

  async function handleSaveToGallery() {
    const canvas = canvasRef.current;
    setStatus('Saving…');
    try {
      const record = await savePainting(child, {
        id: activePaintingId,
        title,
        image: canvas.toDataURL('image/png'),
      });
      setActivePaintingId(record.id);
      setStatus('Saved to My Art!');
      loadGallery();
    } catch {
      setStatus('Could not save right now.');
    }
    setTimeout(() => setStatus(''), 2500);
  }

  async function handleOpenPainting(record) {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    try {
      const img = new Image();
      await new Promise((resolve, reject) => {
        img.onload = resolve;
        img.onerror = reject;
        img.src = `${paintingImageUrl(child, record.id)}?t=${Date.now()}`;
      });
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      ctx.setTransform(dprRef.current, 0, 0, dprRef.current, 0, 0);
      setActivePaintingId(record.id);
      setTitle(record.title);
      pushHistory();
      setGalleryOpen(false);
    } catch {
      setStatus('Could not open that painting.');
    }
  }

  async function handleDeletePainting(record) {
    try {
      await deletePainting(child, record.id);
      if (activePaintingId === record.id) setActivePaintingId(null);
      loadGallery();
    } catch {
      setStatus('Could not delete right now.');
    }
  }

  function handleNewPainting() {
    setActivePaintingId(null);
    setTitle('My Painting');
    handleClear();
  }

  return (
    <section aria-label="Digital painting studio" className="rounded border p-4 dark:border-gray-700">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-bold">Colouring &amp; Painting Studio</h2>
        <button
          type="button"
          onClick={() => setGalleryOpen((v) => !v)}
          aria-expanded={galleryOpen}
          className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
        >
          {galleryOpen ? 'Close My Art' : 'My Art'}
        </button>
      </div>

      {galleryOpen && (
        <div role="region" aria-label="My Art gallery" className="mb-3 rounded border p-2 dark:border-gray-700">
          <div className="mb-2 flex items-center justify-between">
            <span className="text-sm font-semibold">Saved paintings</span>
            <button
              type="button"
              onClick={handleNewPainting}
              className="rounded border px-2 py-1 text-xs focus:outline focus:outline-2 focus:outline-blue-500"
            >
              Start new painting
            </button>
          </div>
          {gallery.length === 0 ? (
            <p className="text-sm text-gray-500 dark:text-gray-400">No saved paintings yet.</p>
          ) : (
            <ul className="flex flex-wrap gap-2">
              {gallery.map((record) => (
                <li key={record.id} className="w-28 rounded border p-1 dark:border-gray-600">
                  <button
                    type="button"
                    onClick={() => handleOpenPainting(record)}
                    className="block w-full focus:outline focus:outline-2 focus:outline-blue-500"
                    aria-label={`Open painting ${record.title}`}
                  >
                    <img
                      src={paintingImageUrl(child, record.id)}
                      alt={record.title}
                      className="mb-1 h-16 w-full rounded border object-cover"
                    />
                    <span className="block truncate text-xs">{record.title}</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => handleDeletePainting(record)}
                    aria-label={`Delete painting ${record.title}`}
                    className="mt-1 w-full rounded border px-1 text-xs text-red-600 focus:outline focus:outline-2 focus:outline-blue-500 dark:text-red-400"
                  >
                    Delete
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}

      <div className="mb-3 flex flex-wrap items-center gap-3">
        <div role="group" aria-label="Drawing tool" className="flex flex-wrap gap-1">
          {ALL_TOOLS.map((t) => (
            <button
              key={t.id}
              type="button"
              aria-pressed={tool === t.id}
              onClick={() => setTool(t.id)}
              className={`rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500 ${
                tool === t.id ? 'bg-blue-600 text-white' : ''
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>
      </div>

      <div className="mb-3 flex flex-wrap items-center gap-3">
        <label className="flex items-center gap-1">
          <span className="text-sm">Colour</span>
          <input
            type="color"
            aria-label="Colour picker"
            value={color}
            onChange={(e) => setColor(e.target.value)}
          />
        </label>

        <div role="group" aria-label="Colour palette" className="flex flex-wrap gap-1">
          {PALETTE.map((swatch) => (
            <button
              key={swatch}
              type="button"
              aria-label={`Use colour ${swatch}`}
              aria-pressed={color === swatch}
              onClick={() => setColor(swatch)}
              style={{ backgroundColor: swatch }}
              className={`h-6 w-6 rounded border focus:outline focus:outline-2 focus:outline-blue-500 ${
                color === swatch ? 'ring-2 ring-blue-500' : ''
              }`}
            />
          ))}
        </div>

        <label className="flex items-center gap-1">
          <span className="text-sm">Size</span>
          <input
            type="range"
            min="1"
            max="30"
            aria-label="Brush size"
            value={brushSize}
            onChange={(e) => setBrushSize(Number(e.target.value))}
          />
        </label>
      </div>

      <div className="mb-3 flex flex-wrap items-center gap-2">
        <button
          type="button"
          onClick={handleUndo}
          disabled={!canUndo}
          aria-label="Undo"
          className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500 disabled:opacity-40"
        >
          ↶ Undo
        </button>
        <button
          type="button"
          onClick={handleRedo}
          disabled={!canRedo}
          aria-label="Redo"
          className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500 disabled:opacity-40"
        >
          ↷ Redo
        </button>
        <button
          type="button"
          onClick={handleClear}
          className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
        >
          Clear
        </button>
        <label className="flex items-center gap-1 text-sm">
          <span className="sr-only">Painting title</span>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            aria-label="Painting title"
            className="w-32 rounded border px-2 py-1 text-sm dark:bg-gray-800 dark:border-gray-600"
            placeholder="Painting title"
          />
        </label>
        <button
          type="button"
          onClick={handleSaveToGallery}
          className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
        >
          Save to My Art
        </button>
        <button
          type="button"
          onClick={handleSave}
          className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
        >
          Save as PNG
        </button>
        {status && (
          <span role="status" className="text-sm text-green-600 dark:text-green-400">
            {status}
          </span>
        )}
      </div>

      <div ref={containerRef} className="w-full">
        <canvas
          ref={canvasRef}
          role="img"
          aria-label="Drawing area"
          className="touch-none rounded border bg-white"
          onPointerDown={handlePointerDownWrapped}
          onPointerMove={handlePointerMove}
          onPointerUp={handlePointerUp}
          onPointerCancel={handlePointerUp}
          onPointerLeave={handlePointerUp}
        />
      </div>
    </section>
  );
}
