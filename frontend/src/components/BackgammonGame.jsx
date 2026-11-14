import React, { useState } from 'react';
import { randInt } from '../utils/gameUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

// Real backgammon rules on the standard 24-point board (0-indexed here as
// points 0-23). The player bears off through points 0-5, the computer
// bears off through points 18-23 — the two home boards face each other,
// same as a physical board. Bar entry, hitting blots, doubles giving four
// moves, and the bear-off "highest point" overage rule are all implemented.

function initialPoints() {
  const points = Array(24).fill(null);
  points[23] = { owner: 'player', count: 2 };
  points[12] = { owner: 'player', count: 5 };
  points[7] = { owner: 'player', count: 3 };
  points[5] = { owner: 'player', count: 5 };
  points[0] = { owner: 'cpu', count: 2 };
  points[11] = { owner: 'cpu', count: 5 };
  points[16] = { owner: 'cpu', count: 3 };
  points[18] = { owner: 'cpu', count: 5 };
  return points;
}

function rollDice() {
  const a = randInt(1, 6);
  const b = randInt(1, 6);
  return a === b ? [a, a, a, a] : [a, b];
}

function opponentOf(owner) {
  return owner === 'player' ? 'cpu' : 'player';
}

function canLandOn(points, dest, owner) {
  if (dest < 0 || dest > 23) return false;
  const p = points[dest];
  return !p || p.owner === owner || p.count === 1;
}

function homeRange(owner) {
  return owner === 'player' ? [0, 5] : [18, 23];
}

function allHome(points, bar, owner) {
  if (bar[owner] > 0) return false;
  const [lo, hi] = homeRange(owner);
  for (let i = 0; i < 24; i++) {
    const p = points[i];
    if (p && p.owner === owner && (i < lo || i > hi)) return false;
  }
  return true;
}

function entryIndex(owner, die) {
  return owner === 'player' ? 24 - die : die - 1;
}

function canBearOff(points, owner, from, die) {
  if (owner === 'player') {
    const need = from + 1;
    if (die === need) return true;
    if (die > need) {
      for (let q = from + 1; q <= 5; q++) if (points[q] && points[q].owner === 'player') return false;
      return true;
    }
    return false;
  }
  const need = 24 - from;
  if (die === need) return true;
  if (die > need) {
    for (let q = 18; q < from; q++) if (points[q] && points[q].owner === 'cpu') return false;
    return true;
  }
  return false;
}

function movePoint(points, from, to, owner) {
  const next = points.map((p) => (p ? { ...p } : p));
  let hit = false;
  next[from].count -= 1;
  if (next[from].count === 0) next[from] = null;
  if (next[to] && next[to].owner !== owner) hit = true;
  next[to] = { owner, count: hit ? 1 : (next[to]?.count || 0) + 1 };
  return { points: next, hit };
}

function legalMovesForDie(points, bar, owner, die) {
  const moves = [];
  if (bar[owner] > 0) {
    const dest = entryIndex(owner, die);
    if (canLandOn(points, dest, owner)) moves.push({ from: 'bar', to: dest });
    return moves;
  }
  const dir = owner === 'player' ? -1 : 1;
  const home = allHome(points, bar, owner);
  for (let i = 0; i < 24; i++) {
    const p = points[i];
    if (!p || p.owner !== owner) continue;
    const dest = i + dir * die;
    if (dest >= 0 && dest <= 23 && canLandOn(points, dest, owner)) {
      moves.push({ from: i, to: dest });
    } else if (home && canBearOff(points, owner, i, die)) {
      moves.push({ from: i, to: 'off' });
    }
  }
  return moves;
}

export default function BackgammonGame({ onComplete, stats }) {
  const [points, setPoints] = useState(initialPoints);
  const [bar, setBar] = useState({ player: 0, cpu: 0 });
  const [borne, setBorne] = useState({ player: 0, cpu: 0 });
  const [dice, setDice] = useState([]);
  const [turn, setTurn] = useState('player');
  const [selected, setSelected] = useState(null);
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('Roll the dice to begin.');

  function finish(playerWon) {
    setFinished(true);
    if (onComplete) {
      onComplete({
        score: playerWon ? 1 : 0,
        maxScore: 1,
        label: `Backgammon — ${playerWon ? 'you bore off all your checkers first!' : 'the computer bore off first'}`,
      });
    }
  }

  function applyMove(move, owner, current) {
    const { points: pts, bar: b, borne: bo } = current;
    if (move.to === 'off') {
      const nextPoints = pts.map((p) => (p ? { ...p } : p));
      nextPoints[move.from].count -= 1;
      if (nextPoints[move.from].count === 0) nextPoints[move.from] = null;
      return { points: nextPoints, bar: b, borne: { ...bo, [owner]: bo[owner] + 1 } };
    }
    let nextBar = b;
    let nextPoints;
    if (move.from === 'bar') {
      nextPoints = pts.map((p) => (p ? { ...p } : p));
      const dest = nextPoints[move.to];
      const hit = dest && dest.owner !== owner;
      nextPoints[move.to] = { owner, count: hit ? 1 : (dest?.count || 0) + 1 };
      nextBar = { ...b, [owner]: b[owner] - 1, ...(hit ? { [opponentOf(owner)]: b[opponentOf(owner)] + 1 } : {}) };
      return { points: nextPoints, bar: nextBar, borne: bo };
    }
    const { points: movedPoints, hit } = movePoint(pts, move.from, move.to, owner);
    nextBar = hit ? { ...b, [opponentOf(owner)]: b[opponentOf(owner)] + 1 } : b;
    return { points: movedPoints, bar: nextBar, borne: bo };
  }

  function rollForPlayer() {
    if (finished || turn !== 'player' || dice.length > 0) return;
    const roll = rollDice();
    setDice(roll);
    setMessage('Pick a checker, then a highlighted destination.');
  }

  function checkWin(state, owner) {
    return state.borne[owner] === 15;
  }

  function finishTurnIfNoMoves(state, owner, remainingDice) {
    const anyMove = remainingDice.some((d) => legalMovesForDie(state.points, state.bar, owner, d).length > 0);
    return !anyMove;
  }

  function selectPoint(idx) {
    if (finished || turn !== 'player' || dice.length === 0) return;
    if (bar.player > 0 && idx !== 'bar') return;
    const from = bar.player > 0 ? 'bar' : idx;
    if (from !== 'bar') {
      const p = points[idx];
      if (!p || p.owner !== 'player') return;
    }
    const uniqueDice = [...new Set(dice)];
    const options = uniqueDice
      .map((d) => ({ d, moves: legalMovesForDie(points, bar, 'player', d).filter((m) => m.from === from) }))
      .filter((o) => o.moves.length > 0);
    if (options.length === 0) {
      setMessage('No legal moves for that checker.');
      return;
    }
    setSelected({ from, options });
  }

  function chooseDestination(to, die) {
    if (!selected) return;
    playerMoveWithDie(to, die);
  }

  function playerMoveWithDie(to, die) {
    const current = { points, bar, borne };
    const move = { from: selected.from, to };
    const next = applyMove(move, 'player', current);
    setPoints(next.points);
    setBar(next.bar);
    setBorne(next.borne);
    const idx = dice.indexOf(die);
    const nextDice = [...dice.slice(0, idx), ...dice.slice(idx + 1)];
    setDice(nextDice);
    setSelected(null);

    if (checkWin(next, 'player')) {
      finish(true);
      return;
    }
    if (nextDice.length === 0 || finishTurnIfNoMoves(next, 'player', nextDice)) {
      setTurn('cpu');
      setMessage("Computer's turn…");
      setTimeout(() => runCpuTurn(next), 500);
    } else {
      setMessage('Pick your next checker.');
    }
  }

  function scoreMove(state, move, die) {
    let s = 0;
    if (move.to === 'off') return 45;
    const dest = state.points[move.to];
    if (dest && dest.owner === 'player') s += 60; // hits a player blot
    const landing = state.points[move.to];
    if (!landing) s += 5;
    else if (landing.owner === 'cpu' && landing.count === 1) s += 8; // makes a point
    if (move.from !== 'bar') {
      const cur = state.points[move.from];
      if (cur && cur.count === 1) s += 6; // clears a blot
    } else {
      s += 20; // entering from the bar is a priority
    }
    return s + Math.random();
  }

  function runCpuTurn(startState) {
    let state = startState;
    let remaining = rollDice();
    // If it's a fresh CPU turn we roll; but this may also be called mid-turn recursively, guard via param.
    runCpuDice(state, remaining);
  }

  function runCpuDice(state, remaining) {
    if (remaining.length === 0) {
      if (checkWin(state, 'cpu')) {
        finish(false);
        return;
      }
      setTurn('player');
      setDice([]);
      setMessage('Your turn — roll the dice.');
      return;
    }
    const uniqueDice = [...new Set(remaining)];
    let best = null;
    let bestScore = -Infinity;
    for (const d of uniqueDice) {
      const moves = legalMovesForDie(state.points, state.bar, 'cpu', d);
      for (const m of moves) {
        const sc = scoreMove(state, m, d);
        if (sc > bestScore) {
          bestScore = sc;
          best = { move: m, die: d };
        }
      }
    }
    if (!best) {
      // No legal moves with any remaining die — forfeit the rest.
      runCpuDice(state, []);
      return;
    }
    const next = applyMove(best.move, 'cpu', state);
    setPoints(next.points);
    setBar(next.bar);
    setBorne(next.borne);
    const idx = remaining.indexOf(best.die);
    const nextRemaining = [...remaining.slice(0, idx), ...remaining.slice(idx + 1)];
    if (checkWin(next, 'cpu')) {
      finish(false);
      return;
    }
    setTimeout(() => runCpuDice(next, nextRemaining), 350);
  }

  function restart() {
    setPoints(initialPoints());
    setBar({ player: 0, cpu: 0 });
    setBorne({ player: 0, cpu: 0 });
    setDice([]);
    setTurn('player');
    setSelected(null);
    setFinished(false);
    setMessage('Roll the dice to begin.');
  }

  const selectedFromIdx = selected ? selected.from : null;
  const highlightedDestinations = selected
    ? [...new Set(selected.options.flatMap((o) => o.moves.map((m) => m.to)))]
    : [];

  return (
    <div className="max-w-3xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🎯 Backgammon</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">
        Race all 15 checkers around and off the board. Hit a lone enemy checker (a blot) to send it to the bar — it must re-enter before moving again.
      </p>

      <div className="flex justify-center gap-6 text-sm font-semibold">
        <span>🔵 You — off: {borne.player}, bar: {bar.player}</span>
        <span>🔴 Computer — off: {borne.cpu}, bar: {bar.cpu}</span>
      </div>

      <div className="bg-amber-800 rounded-xl p-2 mx-auto" style={{ maxWidth: 640 }}>
        <div className="grid grid-cols-12 gap-0.5">
          {Array.from({ length: 12 }, (_, c) => 23 - c).map((idx) => (
            <PointCell
              key={idx}
              idx={idx}
              point={points[idx]}
              selected={selectedFromIdx === idx}
              highlighted={highlightedDestinations.includes(idx)}
              onClick={() => (turn === 'player' && !selected ? selectPoint(idx) : highlightedDestinations.includes(idx) ? chooseDestination(idx, selected.options.find((o) => o.moves.some((m) => m.to === idx)).d) : selectPoint(idx))}
              top
            />
          ))}
        </div>
        <div className="h-3" />
        <div className="grid grid-cols-12 gap-0.5">
          {Array.from({ length: 12 }, (_, c) => c).map((idx) => (
            <PointCell
              key={idx}
              idx={idx}
              point={points[idx]}
              selected={selectedFromIdx === idx}
              highlighted={highlightedDestinations.includes(idx)}
              onClick={() => (turn === 'player' && !selected ? selectPoint(idx) : highlightedDestinations.includes(idx) ? chooseDestination(idx, selected.options.find((o) => o.moves.some((m) => m.to === idx)).d) : selectPoint(idx))}
            />
          ))}
        </div>
      </div>

      {bar.player > 0 && turn === 'player' && dice.length > 0 && (
        <div className="flex justify-center">
          <button
            onClick={() => selectPoint('bar')}
            className={`rounded-lg border-2 px-4 py-2 text-sm font-semibold ${selectedFromIdx === 'bar' ? 'border-amber-500 bg-amber-100' : 'border-indigo-400 bg-indigo-50'}`}
          >
            Enter from bar ({bar.player} waiting)
          </button>
        </div>
      )}

      {selected && selected.options.some((o) => o.moves.some((m) => m.to === 'off')) && (
        <div className="flex justify-center">
          <button
            onClick={() => chooseDestination('off', selected.options.find((o) => o.moves.some((m) => m.to === 'off')).d)}
            className="rounded-lg border-2 border-emerald-500 bg-emerald-50 px-4 py-2 text-sm font-semibold text-emerald-700"
          >
            Bear Off
          </button>
        </div>
      )}

      <div className="flex justify-center gap-2">
        {dice.map((d, i) => (
          <span key={i} className="w-9 h-9 rounded bg-white border-2 border-gray-400 flex items-center justify-center font-bold">
            {d}
          </span>
        ))}
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <div className="flex justify-center gap-3">
        {!finished && turn === 'player' && dice.length === 0 && (
          <button onClick={rollForPlayer} className="rounded-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-6 py-2.5">
            🎲 Roll Dice
          </button>
        )}
        {finished && (
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        )}
      </div>
    </div>
  );
}

function PointCell({ idx, point, selected, highlighted, onClick, top }) {
  return (
    <button
      onClick={onClick}
      className={`h-16 flex flex-col items-center justify-start ${top ? '' : 'justify-end'} ${idx % 2 === 0 ? 'bg-amber-700' : 'bg-amber-600'} ${
        selected ? 'ring-2 ring-inset ring-amber-300' : ''
      } ${highlighted ? 'ring-2 ring-inset ring-emerald-300' : ''}`}
    >
      {point && (
        <span className={`text-[10px] font-bold rounded-full w-5 h-5 flex items-center justify-center mt-0.5 ${point.owner === 'player' ? 'bg-blue-500 text-white' : 'bg-red-500 text-white'}`}>
          {point.count}
        </span>
      )}
    </button>
  );
}
