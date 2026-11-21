import React, { useState } from 'react';
import { randInt } from '../utils/gameUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

// A classic 100-square snakes & ladders layout (one common real board).
const LADDERS = { 4: 25, 13: 46, 33: 49, 42: 63, 50: 69, 62: 81, 74: 92 };
const SNAKES = { 27: 5, 40: 3, 43: 18, 54: 31, 66: 45, 76: 58, 89: 53, 99: 41 };

function applySquare(pos) {
  if (LADDERS[pos]) return LADDERS[pos];
  if (SNAKES[pos]) return SNAKES[pos];
  return pos;
}

export default function SnakesAndLaddersGame({ onComplete, stats }) {
  const [positions, setPositions] = useState({ player: 0, cpu: 0 });
  const [turn, setTurn] = useState('player');
  const [die, setDie] = useState(null);
  const [log, setLog] = useState(['Roll the die to start racing to square 100!']);
  const [finished, setFinished] = useState(false);

  function pushLog(line) {
    setLog((l) => [line, ...l].slice(0, 6));
  }

  function finish(winner) {
    setFinished(true);
    if (onComplete) {
      onComplete({
        score: winner === 'player' ? 1 : 0,
        maxScore: 1,
        label: `Snakes & Ladders — ${winner === 'player' ? 'you reached 100 first!' : 'the computer reached 100 first'}`,
      });
    }
  }

  function moveAndReport(who, from, roll) {
    let to = from + roll;
    if (to > 100) to = from; // must roll the exact amount to finish
    const landed = applySquare(to);
    if (landed > to) pushLog(`${who === 'player' ? 'You' : 'Computer'} climbed a ladder to ${landed}!`);
    else if (landed < to) pushLog(`${who === 'player' ? 'You' : 'Computer'} slid down a snake to ${landed}.`);
    else pushLog(`${who === 'player' ? 'You' : 'Computer'} rolled a ${roll}, now on ${landed}.`);
    return landed;
  }

  function rollForPlayer() {
    if (finished || turn !== 'player' || die !== null) return;
    const roll = randInt(1, 6);
    setDie(roll);
    const to = moveAndReport('player', positions.player, roll);
    const next = { ...positions, player: to };
    setPositions(next);
    if (to === 100) {
      finish('player');
      return;
    }
    setTimeout(() => cpuTurn(next), 500);
  }

  function cpuTurn(current) {
    const roll = randInt(1, 6);
    const to = moveAndReport('cpu', current.cpu, roll);
    const next = { ...current, cpu: to };
    setPositions(next);
    setDie(null);
    setTurn('player');
    if (to === 100) finish('cpu');
  }

  function restart() {
    setPositions({ player: 0, cpu: 0 });
    setTurn('player');
    setDie(null);
    setLog(['Roll the die to start racing to square 100!']);
    setFinished(false);
  }

  return (
    <div className="max-w-lg mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🐍 Snakes &amp; Ladders</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Race to square 100. Ladders climb you up, snakes send you back down.</p>

      <div className="grid grid-cols-2 gap-3 text-center">
        <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3">
          <p className="text-xs font-semibold text-indigo-600">🔵 You</p>
          <p className="text-2xl font-bold text-indigo-800 dark:text-indigo-200">{positions.player}</p>
        </div>
        <div className="rounded-xl bg-rose-50 dark:bg-rose-950 border border-rose-200 dark:border-rose-800 p-3">
          <p className="text-xs font-semibold text-rose-600">🔴 Computer</p>
          <p className="text-2xl font-bold text-rose-800 dark:text-rose-200">{positions.cpu}</p>
        </div>
      </div>

      <div className="w-full bg-gray-100 dark:bg-gray-800 rounded-full h-3 relative overflow-hidden">
        <div className="absolute inset-y-0 left-0 bg-indigo-500 h-full" style={{ width: `${positions.player}%` }} />
      </div>
      <div className="w-full bg-gray-100 dark:bg-gray-800 rounded-full h-3 relative overflow-hidden">
        <div className="absolute inset-y-0 left-0 bg-rose-500 h-full" style={{ width: `${positions.cpu}%` }} />
      </div>

      <div className="rounded-xl bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-3 space-y-1 max-h-32 overflow-y-auto">
        {log.map((line, i) => (
          <p key={i} className="text-xs text-gray-600 dark:text-gray-300">{line}</p>
        ))}
      </div>

      <div className="flex justify-center">
        {!finished ? (
          <button
            onClick={rollForPlayer}
            disabled={turn !== 'player' || die !== null}
            className="rounded-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 text-white font-bold px-6 py-3 text-lg"
          >
            🎲 Roll
          </button>
        ) : (
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        )}
      </div>
    </div>
  );
}
