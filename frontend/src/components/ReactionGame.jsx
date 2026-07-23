import React, { useEffect, useState } from 'react';
import { sample } from '../utils/gameUtils.js';

const ROUND_SECONDS = 30;

function buildGrid(size, target, distractorPool) {
  const distractor = sample(distractorPool);
  const targetIndex = Math.floor(Math.random() * size);
  return Array.from({ length: size }, (_, i) => (i === targetIndex ? target : distractor));
}

export default function ReactionGame({ title, blurb, target, distractorPool, gridSize = 16 }) {
  const [started, setStarted] = useState(false);
  const [finished, setFinished] = useState(false);
  const [score, setScore] = useState(0);
  const [secondsLeft, setSecondsLeft] = useState(ROUND_SECONDS);
  const [grid, setGrid] = useState(() => buildGrid(gridSize, target, distractorPool));

  useEffect(() => {
    if (!started || finished) return;
    if (secondsLeft <= 0) {
      setFinished(true);
      return;
    }
    const timer = setTimeout(() => setSecondsLeft((s) => s - 1), 1000);
    return () => clearTimeout(timer);
  }, [started, finished, secondsLeft]);

  function start() {
    setStarted(true);
    setFinished(false);
    setScore(0);
    setSecondsLeft(ROUND_SECONDS);
    setGrid(buildGrid(gridSize, target, distractorPool));
  }

  function clickCell(symbol) {
    if (!started || finished) return;
    if (symbol === target) {
      setScore((s) => s + 1);
      setGrid(buildGrid(gridSize, target, distractorPool));
    }
  }

  return (
    <section aria-label={`${title} reaction game`} className="space-y-3 rounded border p-4 dark:border-gray-700">
      <h3 className="font-semibold">{title}</h3>
      {blurb && <p className="text-sm text-gray-600 dark:text-gray-400">{blurb}</p>}

      {!started && (
        <button type="button" onClick={start} className="rounded border px-3 py-1 text-sm">
          Start
        </button>
      )}

      {started && !finished && (
        <div className="space-y-2">
          <p className="text-sm">
            Time left: <span className="font-semibold">{secondsLeft}s</span> · Found:{' '}
            <span className="font-semibold">{score}</span>
          </p>
          <div className="grid grid-cols-4 gap-1">
            {grid.map((symbol, i) => (
              <button
                key={i}
                type="button"
                onClick={() => clickCell(symbol)}
                className="flex h-12 w-12 items-center justify-center rounded border text-xl"
              >
                {symbol}
              </button>
            ))}
          </div>
        </div>
      )}

      {finished && (
        <div className="space-y-2">
          <p className="font-medium">Time's up! You found {score}.</p>
          <button type="button" onClick={start} className="rounded border px-3 py-1 text-sm">
            Play again
          </button>
        </div>
      )}
    </section>
  );
}
