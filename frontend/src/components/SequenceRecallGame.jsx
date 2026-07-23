import React, { useState } from 'react';
import { sample } from '../utils/gameUtils.js';

const FLASH_MS = 550;
const GAP_MS = 250;

export default function SequenceRecallGame({ title, blurb, tiles }) {
  const [started, setStarted] = useState(false);
  const [sequence, setSequence] = useState([]);
  const [userIndex, setUserIndex] = useState(0);
  const [phase, setPhase] = useState('idle'); // idle | showing | input | gameover
  const [activeTile, setActiveTile] = useState(null);
  const [best, setBest] = useState(0);

  function playSequence(seq) {
    setPhase('showing');
    setUserIndex(0);
    seq.forEach((tileId, i) => {
      const start = i * (FLASH_MS + GAP_MS);
      setTimeout(() => setActiveTile(tileId), start);
      setTimeout(() => setActiveTile(null), start + FLASH_MS);
    });
    setTimeout(() => setPhase('input'), seq.length * (FLASH_MS + GAP_MS) + 150);
  }

  function start() {
    const first = [sample(tiles).id];
    setSequence(first);
    setStarted(true);
    setBest(0);
    playSequence(first);
  }

  function handleTileClick(tileId) {
    if (phase !== 'input') return;
    if (tileId === sequence[userIndex]) {
      const nextIndex = userIndex + 1;
      if (nextIndex === sequence.length) {
        setBest((b) => Math.max(b, sequence.length));
        const extended = [...sequence, sample(tiles).id];
        setSequence(extended);
        setTimeout(() => playSequence(extended), 500);
        setPhase('showing');
      } else {
        setUserIndex(nextIndex);
      }
    } else {
      setBest((b) => Math.max(b, sequence.length - 1));
      setPhase('gameover');
    }
  }

  function restart() {
    setStarted(false);
    setPhase('idle');
    setSequence([]);
    setUserIndex(0);
    setActiveTile(null);
  }

  return (
    <section aria-label={`${title} pattern recall game`} className="space-y-3 rounded border p-4 dark:border-gray-700">
      <h3 className="font-semibold">{title}</h3>
      {blurb && <p className="text-sm text-gray-600 dark:text-gray-400">{blurb}</p>}

      {!started && (
        <button type="button" onClick={start} className="rounded border px-3 py-1 text-sm">
          Start
        </button>
      )}

      {started && phase !== 'gameover' && (
        <div className="space-y-2">
          <p className="text-sm">
            {phase === 'showing' ? 'Watch the pattern…' : `Your turn — repeat the pattern (round ${sequence.length})`}
          </p>
          <div className="grid grid-cols-4 gap-2">
            {tiles.map((tile) => (
              <button
                key={tile.id}
                type="button"
                disabled={phase !== 'input'}
                onClick={() => handleTileClick(tile.id)}
                className={`flex h-16 items-center justify-center rounded border text-lg font-semibold ${tile.className} ${
                  activeTile === tile.id ? 'ring-4 ring-offset-2 ring-black/60 dark:ring-white/60' : ''
                }`}
              >
                {tile.label}
              </button>
            ))}
          </div>
        </div>
      )}

      {phase === 'gameover' && (
        <div className="space-y-2">
          <p className="font-medium">Game over! Longest pattern remembered: {best}.</p>
          <button type="button" onClick={restart} className="rounded border px-3 py-1 text-sm">
            Play again
          </button>
        </div>
      )}
    </section>
  );
}
