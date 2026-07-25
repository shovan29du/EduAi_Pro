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
  { id: 'text', label: 'Text' },
  { id: 'sticker', label: 'Stickers' },
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

const STICKERS = ['🌟', '⭐', '🎈', '🌈', '🦋', '🐱', '🐶', '🌸', '❤️', '🚀', '🍎', '🎵'];

const MAX_HISTORY = 30;
const NIB_ANGLE = (40 * Math.PI) / 180; // fixed calligraphy nib angle

// ── Colouring-book outline templates ────────────────────────────────────────
// Each template draws a simple line-art shape with plain Canvas path calls
// (no external image/SVG asset loading needed -- keeps it synchronous,
// resolution-independent, and trivially testable). Coordinates are derived
// from the logical (CSS-pixel) canvas size passed in, so a template scales
// cleanly to any canvas dimensions.
const TEMPLATES = [
  {
    id: 'flower',
    label: 'Flower',
    draw(ctx, w, h) {
      const cx = w * 0.5;
      const cy = h * 0.42;
      const petalR = Math.min(w, h) * 0.14;
      const dist = petalR * 1.1;
      for (let i = 0; i < 6; i++) {
        const angle = (Math.PI * 2 * i) / 6;
        ctx.beginPath();
        ctx.arc(cx + Math.cos(angle) * dist, cy + Math.sin(angle) * dist, petalR, 0, Math.PI * 2);
        ctx.stroke();
      }
      ctx.beginPath();
      ctx.arc(cx, cy, petalR * 0.6, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx, cy + petalR * 1.4);
      ctx.lineTo(cx, h * 0.88);
      ctx.stroke();
      ctx.beginPath();
      ctx.ellipse(cx - w * 0.09, h * 0.72, w * 0.07, h * 0.035, Math.PI / 4, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.ellipse(cx + w * 0.09, h * 0.8, w * 0.07, h * 0.035, -Math.PI / 4, 0, Math.PI * 2);
      ctx.stroke();
    },
  },
  {
    id: 'house',
    label: 'House',
    draw(ctx, w, h) {
      const x = w * 0.2;
      const y = h * 0.5;
      const bw = w * 0.6;
      const bh = h * 0.35;
      ctx.strokeRect(x, y, bw, bh);
      ctx.beginPath();
      ctx.moveTo(x - w * 0.05, y);
      ctx.lineTo(x + bw / 2, h * 0.22);
      ctx.lineTo(x + bw + w * 0.05, y);
      ctx.closePath();
      ctx.stroke();
      ctx.strokeRect(x + bw * 0.4, y + bh * 0.4, bw * 0.2, bh * 0.6);
      ctx.strokeRect(x + bw * 0.12, y + bh * 0.2, bw * 0.18, bh * 0.3);
      ctx.strokeRect(x + bw * 0.68, y + bh * 0.2, bw * 0.18, bh * 0.3);
      ctx.strokeRect(x + bw * 0.72, h * 0.28, w * 0.05, h * 0.14);
    },
  },
  {
    id: 'star',
    label: 'Star',
    draw(ctx, w, h) {
      const cx = w / 2;
      const cy = h / 2;
      const outerR = Math.min(w, h) * 0.38;
      const innerR = outerR * 0.42;
      ctx.beginPath();
      for (let i = 0; i < 10; i++) {
        const r = i % 2 === 0 ? outerR : innerR;
        const angle = (Math.PI / 5) * i - Math.PI / 2;
        const px = cx + Math.cos(angle) * r;
        const py = cy + Math.sin(angle) * r;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.stroke();
    },
  },
  {
    id: 'fish',
    label: 'Fish',
    draw(ctx, w, h) {
      const cx = w * 0.45;
      const cy = h * 0.5;
      const rx = w * 0.28;
      const ry = h * 0.2;
      ctx.beginPath();
      ctx.ellipse(cx, cy, rx, ry, 0, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx + rx * 0.85, cy);
      ctx.lineTo(cx + rx * 1.5, cy - ry * 0.9);
      ctx.lineTo(cx + rx * 1.5, cy + ry * 0.9);
      ctx.closePath();
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(cx - rx * 0.5, cy - ry * 0.25, Math.min(w, h) * 0.02, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx - rx * 0.1, cy + ry * 0.7);
      ctx.quadraticCurveTo(cx, cy + ry * 1.4, cx + rx * 0.3, cy + ry * 0.8);
      ctx.stroke();
    },
  },
  {
    id: 'butterfly',
    label: 'Butterfly',
    draw(ctx, w, h) {
      const cx = w / 2;
      const cy = h / 2;
      [-1, 1].forEach((side) => {
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.bezierCurveTo(
          cx + side * w * 0.35, cy - h * 0.35,
          cx + side * w * 0.4, cy + h * 0.05,
          cx, cy - h * 0.03
        );
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(cx, cy - h * 0.03);
        ctx.bezierCurveTo(
          cx + side * w * 0.3, cy + h * 0.15,
          cx + side * w * 0.25, cy + h * 0.35,
          cx, cy + h * 0.1
        );
        ctx.stroke();
      });
      ctx.beginPath();
      ctx.moveTo(cx, cy - h * 0.22);
      ctx.lineTo(cx, cy + h * 0.22);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx, cy - h * 0.22);
      ctx.lineTo(cx - w * 0.05, cy - h * 0.32);
      ctx.moveTo(cx, cy - h * 0.22);
      ctx.lineTo(cx + w * 0.05, cy - h * 0.32);
      ctx.stroke();
    },
  },
  {
    id: 'cat',
    label: 'Cat face',
    draw(ctx, w, h) {
      const cx = w / 2;
      const cy = h * 0.55;
      const r = Math.min(w, h) * 0.28;
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx - r * 0.8, cy - r * 0.6);
      ctx.lineTo(cx - r * 1.1, cy - r * 1.6);
      ctx.lineTo(cx - r * 0.1, cy - r * 0.9);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx + r * 0.8, cy - r * 0.6);
      ctx.lineTo(cx + r * 1.1, cy - r * 1.6);
      ctx.lineTo(cx + r * 0.1, cy - r * 0.9);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(cx - r * 0.35, cy - r * 0.1, r * 0.1, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(cx + r * 0.35, cy - r * 0.1, r * 0.1, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx - r * 0.08, cy + r * 0.15);
      ctx.lineTo(cx + r * 0.08, cy + r * 0.15);
      ctx.lineTo(cx, cy + r * 0.28);
      ctx.closePath();
      ctx.stroke();
      [-1, 1].forEach((side) => {
        for (let i = -1; i <= 1; i++) {
          ctx.beginPath();
          ctx.moveTo(cx + side * r * 0.15, cy + r * 0.25 + i * r * 0.1);
          ctx.lineTo(cx + side * r * 0.9, cy + r * 0.15 + i * r * 0.18);
          ctx.stroke();
        }
      });
    },
  },
  {
    id: 'sun',
    label: 'Sun',
    draw(ctx, w, h) {
      const cx = w / 2;
      const cy = h / 2;
      const r = Math.min(w, h) * 0.2;
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.stroke();
      for (let i = 0; i < 8; i++) {
        const angle = (Math.PI * 2 * i) / 8;
        ctx.beginPath();
        ctx.moveTo(cx + Math.cos(angle) * r * 1.3, cy + Math.sin(angle) * r * 1.3);
        ctx.lineTo(cx + Math.cos(angle) * r * 1.9, cy + Math.sin(angle) * r * 1.9);
        ctx.stroke();
      }
    },
  },
  {
    id: 'heart',
    label: 'Heart',
    draw(ctx, w, h) {
      const cx = w / 2;
      const top = h * 0.32;
      const s = Math.min(w, h) * 0.32;
      ctx.beginPath();
      ctx.moveTo(cx, top + s * 0.3);
      ctx.bezierCurveTo(cx, top, cx - s, top, cx - s, top + s * 0.4);
      ctx.bezierCurveTo(cx - s, top + s * 0.9, cx, top + s * 1.1, cx, top + s * 1.5);
      ctx.bezierCurveTo(cx, top + s * 1.1, cx + s, top + s * 0.9, cx + s, top + s * 0.4);
      ctx.bezierCurveTo(cx + s, top, cx, top, cx, top + s * 0.3);
      ctx.closePath();
      ctx.stroke();
    },
  },
  {
    id: 'tree',
    label: 'Tree',
    draw(ctx, w, h) {
      const cx = w / 2;
      ctx.strokeRect(cx - w * 0.04, h * 0.65, w * 0.08, h * 0.25);
      ctx.beginPath();
      ctx.arc(cx, h * 0.4, Math.min(w, h) * 0.24, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(cx - w * 0.15, h * 0.5, Math.min(w, h) * 0.17, 0, Math.PI * 2);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(cx + w * 0.15, h * 0.5, Math.min(w, h) * 0.17, 0, Math.PI * 2);
      ctx.stroke();
    },
  },
  {
    id: 'boat',
    label: 'Boat',
    draw(ctx, w, h) {
      const cx = w / 2;
      const waterY = h * 0.65;
      ctx.beginPath();
      ctx.moveTo(w * 0.2, waterY);
      ctx.lineTo(w * 0.8, waterY);
      ctx.lineTo(w * 0.68, h * 0.82);
      ctx.lineTo(w * 0.32, h * 0.82);
      ctx.closePath();
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx, waterY);
      ctx.lineTo(cx, h * 0.22);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx, h * 0.24);
      ctx.lineTo(cx + w * 0.22, h * 0.5);
      ctx.lineTo(cx, h * 0.5);
      ctx.closePath();
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(w * 0.1, h * 0.9);
      ctx.quadraticCurveTo(w * 0.25, h * 0.85, w * 0.4, h * 0.9);
      ctx.quadraticCurveTo(w * 0.55, h * 0.95, w * 0.7, h * 0.9);
      ctx.quadraticCurveTo(w * 0.85, h * 0.85, w * 0.9, h * 0.9);
      ctx.stroke();
    },
  },
];

const OUTLINE_COLOR = '#64748b';
const OUTLINE_BOUNDARY_COLOR = 'rgba(100,116,139,0.55)';

function outlineLineWidth(w, h) {
  return Math.max(3, Math.min(w, h) * 0.014);
}

function drawTemplateOutline(ctx, template, w, h, strokeStyle, lineWidth) {
  ctx.save();
  ctx.strokeStyle = strokeStyle;
  ctx.lineWidth = lineWidth;
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  template.draw(ctx, w, h);
  ctx.restore();
}

// Small preview icon for the template picker -- draws the same vector shape
// at thumbnail scale so children can see what they're choosing.
function TemplateThumb({ template }) {
  const ref = useRef(null);
  useEffect(() => {
    const canvas = ref.current;
    const ctx = canvas && canvas.getContext('2d');
    if (!ctx) return;
    if (ctx.clearRect) ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawTemplateOutline(ctx, template, canvas.width, canvas.height, '#475569', 2);
  }, [template]);
  return (
    <canvas
      ref={ref}
      width={64}
      height={44}
      aria-hidden="true"
      className="rounded border bg-white"
    />
  );
}

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
  const canvasRef = useRef(null); // the editable "drawing" layer
  const backgroundCanvasRef = useRef(null); // bottom layer: flat colour backdrop
  const outlineCanvasRef = useRef(null); // top layer: protected template line-art
  const baseSnapshotRef = useRef(null); // offscreen canvas: pixels before an in-progress shape/stroke
  const drawingRef = useRef(false);
  const lastPointRef = useRef(null);
  const shapeStartRef = useRef(null);
  const dprRef = useRef(1);
  const sizeRef = useRef({ width: 800, height: 520 });
  const undoStackRef = useRef([]);
  const redoStackRef = useRef([]);
  const activeTemplateIdRef = useRef(null);
  const textCancelledRef = useRef(false);

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

  // Templates & layers
  const [templatesOpen, setTemplatesOpen] = useState(false);
  const [layersOpen, setLayersOpen] = useState(false);
  const [activeTemplateId, setActiveTemplateId] = useState(null);
  const [layerVisible, setLayerVisible] = useState({ background: true, drawing: true, outline: true });
  const [layerOrder, setLayerOrder] = useState(['background', 'drawing']); // bottom -> top

  // Symmetry / mirror mode
  const [mirrorH, setMirrorH] = useState(false);
  const [mirrorV, setMirrorV] = useState(false);

  // Sticker tool
  const [selectedSticker, setSelectedSticker] = useState(STICKERS[0]);

  // Text tool
  const [textDraft, setTextDraft] = useState(null); // { x, y } in logical canvas coords
  const [textValue, setTextValue] = useState('');

  const isShapeTool = SHAPE_TOOLS.some((s) => s.id === tool);

  useEffect(() => {
    activeTemplateIdRef.current = activeTemplateId;
  }, [activeTemplateId]);

  // ── Canvas setup: size all three layers to container, scale for DPR ──────
  const applyCanvasSize = useCallback((logicalWidth, logicalHeight, preserveContent) => {
    const canvas = canvasRef.current;
    const bgCanvas = backgroundCanvasRef.current;
    const outlineCanvas = outlineCanvasRef.current;
    const container = containerRef.current;
    if (!canvas || !bgCanvas || !outlineCanvas) return;
    const dpr = window.devicePixelRatio || 1;

    let previousDrawing = null;
    if (preserveContent && canvas.width > 0 && canvas.height > 0) {
      previousDrawing = document.createElement('canvas');
      previousDrawing.width = canvas.width;
      previousDrawing.height = canvas.height;
      previousDrawing.getContext('2d').drawImage(canvas, 0, 0);
    }

    const pxWidth = Math.max(1, Math.round(logicalWidth * dpr));
    const pxHeight = Math.max(1, Math.round(logicalHeight * dpr));

    [canvas, bgCanvas, outlineCanvas].forEach((c) => {
      c.width = pxWidth;
      c.height = pxHeight;
      c.style.width = `${logicalWidth}px`;
      c.style.height = `${logicalHeight}px`;
    });
    if (container) container.style.height = `${logicalHeight}px`;

    dprRef.current = dpr;
    sizeRef.current = { width: logicalWidth, height: logicalHeight };

    // Background layer: flat fill, always simply redrawn (no scaling artefacts).
    const bgCtx = bgCanvas.getContext('2d');
    bgCtx.setTransform(1, 0, 0, 1, 0, 0);
    bgCtx.fillStyle = '#ffffff';
    bgCtx.fillRect(0, 0, bgCanvas.width, bgCanvas.height);

    // Drawing layer: transparent by default, preserve/scale prior strokes.
    const ctx = canvas.getContext('2d');
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (previousDrawing) {
      ctx.drawImage(previousDrawing, 0, 0, previousDrawing.width, previousDrawing.height, 0, 0, canvas.width, canvas.height);
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    // Outline layer: vector-redraw the active template at the new size (if any).
    const outlineCtx = outlineCanvas.getContext('2d');
    outlineCtx.setTransform(1, 0, 0, 1, 0, 0);
    outlineCtx.clearRect(0, 0, outlineCanvas.width, outlineCanvas.height);
    outlineCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const activeTemplate = TEMPLATES.find((t) => t.id === activeTemplateIdRef.current);
    if (activeTemplate) {
      drawTemplateOutline(outlineCtx, activeTemplate, logicalWidth, logicalHeight, OUTLINE_COLOR, outlineLineWidth(logicalWidth, logicalHeight));
    }

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

  // ── Undo / redo history (PNG snapshots of the drawing layer only) ────────
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
        ctx.clearRect(0, 0, canvas.width, canvas.height);
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
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(baseSnapshotRef.current, 0, 0);
    ctx.restore();
  }

  // ── Symmetry / mirror mode ────────────────────────────────────────────────
  // Returns an array of point-transform functions: always includes the
  // identity transform, plus a horizontal and/or vertical reflection (and
  // their combination) depending on which toggles are on -- up to 4x
  // kaleidoscope-style symmetry. Operates in logical (CSS-pixel) space, which
  // is what every drawing primitive below already works in.
  function getMirrorTransforms() {
    const { width, height } = sizeRef.current;
    let arr = [(p) => p];
    if (mirrorH) {
      const base = arr;
      arr = base.concat(base.map((t) => (p) => {
        const q = t(p);
        return { x: width - q.x, y: q.y };
      }));
    }
    if (mirrorV) {
      const base = arr;
      arr = base.concat(base.map((t) => (p) => {
        const q = t(p);
        return { x: q.x, y: height - q.y };
      }));
    }
    return arr;
  }

  // Same idea, but in raw pixel space (for the Fill tool, which operates
  // directly on ImageData rather than through the DPR-scaled ctx transform).
  function getMirrorPixelTransforms() {
    const canvas = canvasRef.current;
    let arr = [(p) => p];
    if (mirrorH) {
      const base = arr;
      arr = base.concat(base.map((t) => (p) => {
        const q = t(p);
        return { x: canvas.width - 1 - q.x, y: q.y };
      }));
    }
    if (mirrorV) {
      const base = arr;
      arr = base.concat(base.map((t) => (p) => {
        const q = t(p);
        return { x: q.x, y: canvas.height - 1 - q.y };
      }));
    }
    return arr;
  }

  // ── Freehand brush strokes ─────────────────────────────────────────────
  function strokeSegment(ctx, from, to) {
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    if (tool === 'eraser') {
      // The drawing layer is transparent, so erasing means punching a hole
      // in it (revealing whatever layer sits underneath) rather than
      // painting white over it.
      ctx.save();
      ctx.globalCompositeOperation = 'destination-out';
      ctx.strokeStyle = 'rgba(0,0,0,1)';
      ctx.globalAlpha = 1;
      ctx.lineWidth = brushSize * 1.6;
      ctx.beginPath();
      ctx.moveTo(from.x, from.y);
      ctx.lineTo(to.x, to.y);
      ctx.stroke();
      ctx.restore();
      return;
    }
    if (tool === 'brush') {
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

    getMirrorTransforms().forEach((t) => {
      const s = t(start);
      const c = t(current);
      if (tool === 'line') {
        ctx.beginPath();
        ctx.moveTo(s.x, s.y);
        ctx.lineTo(c.x, c.y);
        ctx.stroke();
      } else if (tool === 'rectangle') {
        const x = Math.min(s.x, c.x);
        const y = Math.min(s.y, c.y);
        const w = Math.abs(c.x - s.x);
        const h = Math.abs(c.y - s.y);
        ctx.strokeRect(x, y, w, h);
      } else if (tool === 'ellipse') {
        const cx = (s.x + c.x) / 2;
        const cy = (s.y + c.y) / 2;
        const rx = Math.abs(c.x - s.x) / 2;
        const ry = Math.abs(c.y - s.y) / 2;
        ctx.beginPath();
        ctx.ellipse(cx, cy, Math.max(rx, 0.01), Math.max(ry, 0.01), 0, 0, Math.PI * 2);
        ctx.stroke();
      }
    });
  }

  // ── Text tool ──────────────────────────────────────────────────────────
  function openTextEditorAt(pos) {
    textCancelledRef.current = false;
    setTextDraft({ x: pos.x, y: pos.y });
    setTextValue('');
  }

  function cancelText() {
    textCancelledRef.current = true;
    setTextDraft(null);
    setTextValue('');
  }

  function commitText() {
    if (textCancelledRef.current) {
      textCancelledRef.current = false;
      return;
    }
    const value = textValue.trim();
    const pos = textDraft;
    setTextDraft(null);
    setTextValue('');
    if (!value || !pos) return;
    const ctx = canvasRef.current.getContext('2d');
    const fontSize = 14 + brushSize * 3;
    ctx.font = `bold ${fontSize}px "Comic Sans MS", "Segoe UI", sans-serif`;
    ctx.fillStyle = color;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    getMirrorTransforms().forEach((t) => {
      const p = t(pos);
      ctx.fillText(value, p.x, p.y);
    });
    pushHistory();
  }

  // ── Sticker tool ───────────────────────────────────────────────────────
  function placeSticker(pos) {
    const ctx = canvasRef.current.getContext('2d');
    const size = 18 + brushSize * 4;
    ctx.font = `${size}px "Segoe UI Emoji", "Apple Color Emoji", sans-serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    getMirrorTransforms().forEach((t) => {
      const p = t(pos);
      ctx.fillText(selectedSticker, p.x, p.y);
    });
    pushHistory();
  }

  // ── Pointer handlers ──────────────────────────────────────────────────────
  function handlePointerDown(e) {
    const canvas = canvasRef.current;
    canvas.setPointerCapture?.(e.pointerId);
    const ctx = canvas.getContext('2d');
    const pos = getPos(e);

    if (tool === 'fill') {
      const px = toPixelCoords(pos);
      getMirrorPixelTransforms().forEach((t) => {
        const tp = t(px);
        floodFill(ctx, tp.x, tp.y, hexToRgba(color));
      });
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

    const transforms = getMirrorTransforms();
    if (isShapeTool) {
      drawShapePreview(ctx, pos, pos);
    } else if (tool === 'airbrush') {
      transforms.forEach((t) => airbrushDab(ctx, t(pos)));
    } else if (tool === 'calligraphy') {
      transforms.forEach((t) => calligraphyStamp(ctx, t(pos)));
    } else {
      transforms.forEach((t) => strokeSegment(ctx, t(pos), t(pos)));
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
    const transforms = getMirrorTransforms();
    if (tool === 'airbrush') {
      transforms.forEach((t) => airbrushSegment(ctx, t(from), t(pos)));
    } else if (tool === 'calligraphy') {
      transforms.forEach((t) => calligraphySegment(ctx, t(from), t(pos)));
    } else {
      transforms.forEach((t) => strokeSegment(ctx, t(from), t(pos)));
    }
    lastPointRef.current = pos;
  }

  function handlePointerDownWrapped(e) {
    if (!layerVisible.drawing) return;
    const pos = getPos(e);
    if (tool === 'text') {
      openTextEditorAt(pos);
      return;
    }
    if (tool === 'sticker') {
      placeSticker(pos);
      return;
    }
    shapeStartRef.current = pos;
    handlePointerDown(e);
  }

  function handlePointerUp() {
    if (!drawingRef.current) return;
    drawingRef.current = false;
    lastPointRef.current = null;
    pushHistory();
  }

  // ── Templates: bake a faint copy of the outline into the drawing layer so
  // the Fill tool has real pixel boundaries to stop at, even though the
  // crisp visible line-art lives on its own protected overlay layer.
  function bakeBoundaryOntoDrawing(ctx, templateOverride) {
    const template = templateOverride !== undefined
      ? templateOverride
      : TEMPLATES.find((t) => t.id === activeTemplateIdRef.current);
    if (!template) return;
    const { width, height } = sizeRef.current;
    drawTemplateOutline(ctx, template, width, height, OUTLINE_BOUNDARY_COLOR, outlineLineWidth(width, height) * 0.6);
  }

  function handleSelectTemplate(templateId) {
    const template = TEMPLATES.find((t) => t.id === templateId) || null;
    activeTemplateIdRef.current = template ? template.id : null;
    setActiveTemplateId(template ? template.id : null);
    setLayerVisible((v) => ({ ...v, outline: true }));

    const canvas = canvasRef.current;
    const outlineCanvas = outlineCanvasRef.current;
    const dpr = dprRef.current;
    const { width, height } = sizeRef.current;

    const dctx = canvas.getContext('2d');
    dctx.setTransform(1, 0, 0, 1, 0, 0);
    dctx.clearRect(0, 0, canvas.width, canvas.height);
    dctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const octx = outlineCanvas.getContext('2d');
    octx.setTransform(1, 0, 0, 1, 0, 0);
    octx.clearRect(0, 0, outlineCanvas.width, outlineCanvas.height);
    octx.setTransform(dpr, 0, 0, dpr, 0, 0);

    if (template) {
      drawTemplateOutline(octx, template, width, height, OUTLINE_COLOR, outlineLineWidth(width, height));
      bakeBoundaryOntoDrawing(dctx, template);
      setTitle(`My ${template.label}`);
    } else {
      setTitle('My Painting');
    }

    setActivePaintingId(null);
    pushHistory();
    setTemplatesOpen(false);
  }

  // ── Layers panel ───────────────────────────────────────────────────────
  function toggleLayerVisible(key) {
    setLayerVisible((v) => ({ ...v, [key]: !v[key] }));
  }

  function moveLayer() {
    setLayerOrder((prev) => [...prev].reverse());
  }

  function handleClear() {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.setTransform(dprRef.current, 0, 0, dprRef.current, 0, 0);
    bakeBoundaryOntoDrawing(ctx);
    pushHistory();
  }

  // ── Compositing: flatten the visible layers (in layer order, outline
  // always on top) into one offscreen canvas for export / saving. ─────────
  function buildCompositeCanvas() {
    const canvas = canvasRef.current;
    const bgCanvas = backgroundCanvasRef.current;
    const outlineCanvas = outlineCanvasRef.current;
    const out = document.createElement('canvas');
    out.width = canvas.width;
    out.height = canvas.height;
    const ctx = out.getContext('2d');
    layerOrder.forEach((key) => {
      if (key === 'background' && layerVisible.background) ctx.drawImage(bgCanvas, 0, 0);
      if (key === 'drawing' && layerVisible.drawing) ctx.drawImage(canvas, 0, 0);
    });
    if (activeTemplateId && layerVisible.outline) ctx.drawImage(outlineCanvas, 0, 0);
    return out;
  }

  function handleSave() {
    const composite = buildCompositeCanvas();
    const link = document.createElement('a');
    link.download = 'my-artwork.png';
    link.href = composite.toDataURL('image/png');
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
    const composite = buildCompositeCanvas();
    setStatus('Saving…');
    try {
      const record = await savePainting(child, {
        id: activePaintingId,
        title,
        image: composite.toDataURL('image/png'),
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
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      ctx.setTransform(dprRef.current, 0, 0, dprRef.current, 0, 0);
      // A saved painting is a flattened composite -- drop any active
      // template so a stale outline doesn't sit on top of it, and make
      // sure both remaining layers are visible again.
      activeTemplateIdRef.current = null;
      setActiveTemplateId(null);
      const outlineCanvas = outlineCanvasRef.current;
      if (outlineCanvas) {
        const octx = outlineCanvas.getContext('2d');
        octx.setTransform(1, 0, 0, 1, 0, 0);
        octx.clearRect(0, 0, outlineCanvas.width, outlineCanvas.height);
        octx.setTransform(dprRef.current, 0, 0, dprRef.current, 0, 0);
      }
      setLayerVisible((v) => ({ ...v, background: true, drawing: true }));
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
    handleSelectTemplate(null);
  }

  return (
    <section aria-label="Digital painting studio" className="rounded border p-4 dark:border-gray-700">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-bold">Colouring &amp; Painting Studio</h2>
        <div className="flex flex-wrap gap-2">
          <button
            type="button"
            onClick={() => setTemplatesOpen((v) => !v)}
            aria-expanded={templatesOpen}
            className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
          >
            {templatesOpen ? 'Close Templates' : 'Templates'}
          </button>
          <button
            type="button"
            onClick={() => setLayersOpen((v) => !v)}
            aria-expanded={layersOpen}
            className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
          >
            {layersOpen ? 'Close Layers' : 'Layers'}
          </button>
          <button
            type="button"
            onClick={() => setGalleryOpen((v) => !v)}
            aria-expanded={galleryOpen}
            className="rounded border px-2 py-1 text-sm focus:outline focus:outline-2 focus:outline-blue-500"
          >
            {galleryOpen ? 'Close My Art' : 'My Art'}
          </button>
        </div>
      </div>

      {templatesOpen && (
        <div role="region" aria-label="Templates gallery" className="mb-3 rounded border p-2 dark:border-gray-700">
          <div className="mb-2 flex items-center justify-between">
            <span className="text-sm font-semibold">Colouring templates</span>
            <button
              type="button"
              onClick={() => handleSelectTemplate(null)}
              aria-pressed={activeTemplateId === null}
              className="rounded border px-2 py-1 text-xs focus:outline focus:outline-2 focus:outline-blue-500"
            >
              Blank canvas
            </button>
          </div>
          <div className="flex flex-wrap gap-2">
            {TEMPLATES.map((tpl) => (
              <button
                key={tpl.id}
                type="button"
                onClick={() => handleSelectTemplate(tpl.id)}
                aria-pressed={activeTemplateId === tpl.id}
                aria-label={`Use template ${tpl.label}`}
                className={`flex w-20 flex-col items-center gap-1 rounded border p-1 text-xs focus:outline focus:outline-2 focus:outline-blue-500 ${
                  activeTemplateId === tpl.id ? 'ring-2 ring-blue-500' : ''
                }`}
              >
                <TemplateThumb template={tpl} />
                <span>{tpl.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {layersOpen && (
        <div role="region" aria-label="Layers panel" className="mb-3 rounded border p-2 dark:border-gray-700">
          <p className="mb-2 text-sm font-semibold">Layers</p>
          <ul className="space-y-1">
            {activeTemplateId && (
              <li className="flex items-center justify-between gap-2 rounded border px-2 py-1 text-sm dark:border-gray-600">
                <label className="flex items-center gap-2">
                  <input
                    type="checkbox"
                    checked={layerVisible.outline}
                    onChange={() => toggleLayerVisible('outline')}
                    aria-label="Toggle outline layer visibility"
                  />
                  Outline (template) — always on top
                </label>
              </li>
            )}
            {[...layerOrder].reverse().map((key, idx) => (
              <li key={key} className="flex items-center justify-between gap-2 rounded border px-2 py-1 text-sm dark:border-gray-600">
                <label className="flex items-center gap-2">
                  <input
                    type="checkbox"
                    checked={layerVisible[key]}
                    onChange={() => toggleLayerVisible(key)}
                    aria-label={`Toggle ${key} layer visibility`}
                  />
                  {key === 'background' ? 'Background' : 'Drawing'}
                </label>
                <button
                  type="button"
                  onClick={moveLayer}
                  aria-label={`Move ${key} layer`}
                  className="rounded border px-2 py-0.5 text-xs focus:outline focus:outline-2 focus:outline-blue-500"
                >
                  {idx === 0 ? '↓ Send back' : '↑ Bring forward'}
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

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

      {tool === 'sticker' && (
        <div role="group" aria-label="Sticker picker" className="mb-3 flex flex-wrap gap-1">
          {STICKERS.map((s) => (
            <button
              key={s}
              type="button"
              aria-label={`Sticker ${s}`}
              aria-pressed={selectedSticker === s}
              onClick={() => setSelectedSticker(s)}
              className={`h-8 w-8 rounded border text-lg focus:outline focus:outline-2 focus:outline-blue-500 ${
                selectedSticker === s ? 'ring-2 ring-blue-500' : ''
              }`}
            >
              {s}
            </button>
          ))}
        </div>
      )}

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

        <div role="group" aria-label="Symmetry mode" className="flex items-center gap-2">
          <span className="text-sm">Mirror</span>
          <label className="flex items-center gap-1 text-sm">
            <input
              type="checkbox"
              checked={mirrorH}
              onChange={(e) => setMirrorH(e.target.checked)}
              aria-label="Mirror horizontally"
            />
            ↔
          </label>
          <label className="flex items-center gap-1 text-sm">
            <input
              type="checkbox"
              checked={mirrorV}
              onChange={(e) => setMirrorV(e.target.checked)}
              aria-label="Mirror vertically"
            />
            ↕
          </label>
        </div>
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

      <div
        ref={containerRef}
        className="relative w-full overflow-hidden rounded border"
        style={{
          backgroundImage:
            'repeating-conic-gradient(#e5e7eb 0% 25%, #ffffff 0% 50%)',
          backgroundSize: '16px 16px',
        }}
      >
        <canvas ref={backgroundCanvasRef} aria-hidden="true" className="absolute left-0 top-0" style={{ zIndex: layerOrder.indexOf('background') + 1, display: layerVisible.background ? 'block' : 'none' }} />
        <canvas
          ref={canvasRef}
          role="img"
          aria-label="Drawing area"
          className="absolute left-0 top-0 touch-none"
          style={{ zIndex: layerOrder.indexOf('drawing') + 1, display: layerVisible.drawing ? 'block' : 'none' }}
          onPointerDown={handlePointerDownWrapped}
          onPointerMove={handlePointerMove}
          onPointerUp={handlePointerUp}
          onPointerCancel={handlePointerUp}
          onPointerLeave={handlePointerUp}
        />
        <canvas
          ref={outlineCanvasRef}
          aria-hidden="true"
          className="absolute left-0 top-0"
          style={{ zIndex: 3, pointerEvents: 'none', display: activeTemplateId && layerVisible.outline ? 'block' : 'none' }}
        />
        {tool === 'text' && textDraft && (
          <input
            autoFocus
            type="text"
            value={textValue}
            onChange={(e) => setTextValue(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter') {
                e.preventDefault();
                commitText();
              } else if (e.key === 'Escape') {
                e.preventDefault();
                cancelText();
              }
            }}
            onBlur={commitText}
            aria-label="Text to add to canvas"
            className="absolute z-20 rounded border bg-white px-1 text-sm shadow dark:bg-gray-800"
            style={{
              left: Number.isFinite(textDraft.x) ? textDraft.x : 0,
              top: Number.isFinite(textDraft.y) ? Math.max(0, textDraft.y - 12) : 0,
              minWidth: 80,
            }}
          />
        )}
      </div>
    </section>
  );
}
