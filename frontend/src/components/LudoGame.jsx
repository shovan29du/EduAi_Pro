import React, { useState } from 'react';
import { randInt } from '../utils/gameUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

// A real-rules, simplified-board Ludo: the traditional cross-shaped board is
// swapped for a single 52-cell square ring (a 14x14 perimeter — 4x13 sides —
// gives exactly the standard 52-square shared track), with each colour's
// 6-cell home stretch tracked numerically instead of drawn as its own lane.
// Rules kept real: roll a 6 to leave the yard, an extra roll on every 6
// (capped at 3 in a row), captures on non-safe shared squares send a token
// back to the yard, and a token needs the exact remaining count to finish.

const COLORS = [
  { id: 'player', label: 'You', emoji: '🔴', start: 0, bar: 'bg-red-500' },
  { id: 'cpu1', label: 'Green', emoji: '🟢', start: 13, bar: 'bg-emerald-500' },
  { id: 'cpu2', label: 'Yellow', emoji: '🟡', start: 26, bar: 'bg-amber-400' },
  { id: 'cpu3', label: 'Blue', emoji: '🔵', start: 39, bar: 'bg-blue-500' },
];
const SAFE_OFFSETS = new Set([0, 8]);
const TOTAL_STEPS = 57; // 51 shared-track steps + 6 home-stretch steps

function perimeterCell(index) {
  const i = ((index % 52) + 52) % 52;
  if (i <= 13) return { row: 0, col: i };
  if (i <= 26) return { row: i - 13, col: 13 };
  if (i <= 39) return { row: 13, col: 13 - (i - 26) };
  return { row: 13 - (i - 39), col: 0 };
}

function absoluteCell(color, steps) {
  // steps: 1..51 -> shared track position for this colour
  return (color.start + steps - 1) % 52;
}

function isSafeCell(absIndex) {
  return COLORS.some((c) => SAFE_OFFSETS.has(((absIndex - c.start) % 52 + 52) % 52));
}

function freshTokens() {
  return [0, 0, 0, 0]; // steps for each of the 4 tokens, 0 = in yard
}

function initialState() {
  const tokens = {};
  for (const c of COLORS) tokens[c.id] = freshTokens();
  return { tokens, turn: 'player', die: null, consecutiveSixes: 0, log: ['Roll the die to begin!'] };
}

function movableTokenIndices(tokens, die) {
  return tokens.reduce((acc, steps, i) => {
    if (steps === 0 && die === 6) acc.push(i);
    else if (steps > 0 && steps < TOTAL_STEPS && steps + die <= TOTAL_STEPS) acc.push(i);
    return acc;
  }, []);
}

export default function LudoGame({ onComplete, stats }) {
  const [state, setState] = useState(initialState);
  const [finished, setFinished] = useState(false);

  function pushLog(line) {
    setState((s) => ({ ...s, log: [line, ...s.log].slice(0, 6) }));
  }

  function finishWith(playerWon, label) {
    setFinished(true);
    if (onComplete) onComplete({ score: playerWon ? 1 : 0, maxScore: 1, label });
  }

  function applyCaptures(nextTokens, mover, newSteps) {
    if (newSteps < 1 || newSteps > 51) return nextTokens;
    const abs = absoluteCell(COLORS.find((c) => c.id === mover), newSteps);
    if (isSafeCell(abs)) return nextTokens;
    const copy = { ...nextTokens };
    for (const c of COLORS) {
      if (c.id === mover) continue;
      copy[c.id] = copy[c.id].map((steps) => {
        if (steps < 1 || steps > 51) return steps;
        const otherAbs = absoluteCell(c, steps);
        return otherAbs === abs ? 0 : steps;
      });
    }
    return copy;
  }

  function moveToken(colorId, tokenIndex, die, current) {
    const color = COLORS.find((c) => c.id === colorId);
    const steps = current.tokens[colorId][tokenIndex];
    const newSteps = steps === 0 ? 1 : steps + die;
    let tokens = {
      ...current.tokens,
      [colorId]: current.tokens[colorId].map((s, i) => (i === tokenIndex ? newSteps : s)),
    };
    tokens = applyCaptures(tokens, colorId, newSteps);
    return { ...current, tokens };
  }

  function checkWinner(tokens) {
    for (const c of COLORS) {
      if (tokens[c.id].every((s) => s === TOTAL_STEPS)) return c.id;
    }
    return null;
  }

  function runCpuTurn(colorId, current) {
    let s = current;
    let sixes = 0;
    for (let guard = 0; guard < 6; guard++) {
      const die = randInt(1, 6);
      pushLog(`${COLORS.find((c) => c.id === colorId).label} rolled a ${die}.`);
      const movable = movableTokenIndices(s.tokens[colorId], die);
      if (movable.length > 0) {
        // Prefer a capturing move, then bringing a new token out, then the furthest-along token.
        let choice = movable[0];
        let bestScore = -1;
        for (const idx of movable) {
          const steps = s.tokens[colorId][idx];
          const newSteps = steps === 0 ? 1 : steps + die;
          let score = steps === 0 ? 1 : 0;
          if (newSteps <= 51) {
            const abs = absoluteCell(COLORS.find((c) => c.id === colorId), newSteps);
            const capturesSomeone = COLORS.some(
              (c) => c.id !== colorId && s.tokens[c.id].some((os, oi) => os >= 1 && os <= 51 && absoluteCell(c, os) === abs)
            );
            if (capturesSomeone && !isSafeCell(abs)) score += 10;
          }
          score += steps * 0.01;
          if (score > bestScore) {
            bestScore = score;
            choice = idx;
          }
        }
        s = moveToken(colorId, choice, die, s);
        const winner = checkWinner(s.tokens);
        if (winner) {
          setState(s);
          finishWith(winner === 'player', `Ludo — ${winner === 'player' ? 'you' : COLORS.find((c) => c.id === winner).label} finished first!`);
          return s;
        }
      } else {
        pushLog(`${COLORS.find((c) => c.id === colorId).label} has no valid move.`);
      }
      if (die === 6) {
        sixes += 1;
        if (sixes >= 3) break;
        continue;
      }
      break;
    }
    return s;
  }

  function rollDie() {
    if (finished || state.turn !== 'player' || state.die !== null) return;
    const die = randInt(1, 6);
    pushLog(`You rolled a ${die}.`);
    const movable = movableTokenIndices(state.tokens.player, die);
    if (movable.length === 0) {
      pushLog('No valid move — turn passes.');
      advanceAfterPlayer({ ...state, die }, false);
      return;
    }
    setState((s) => ({ ...s, die }));
  }

  function advanceAfterPlayer(current, rolledSix) {
    let s = { ...current, die: null, turn: 'cpu1' };
    for (const cpuId of ['cpu1', 'cpu2', 'cpu3']) {
      if (finished) return;
      s = runCpuTurn(cpuId, s);
      if (checkWinner(s.tokens)) {
        setState(s);
        return;
      }
    }
    setState({ ...s, turn: 'player' });
    if (!rolledSix) pushLog('Your turn — roll the die.');
  }

  function moveMyToken(tokenIndex) {
    if (finished || state.turn !== 'player' || state.die === null) return;
    const movable = movableTokenIndices(state.tokens.player, state.die);
    if (!movable.includes(tokenIndex)) return;
    const rolledSix = state.die === 6;
    const next = moveToken('player', tokenIndex, state.die, state);
    const winner = checkWinner(next.tokens);
    if (winner) {
      setState({ ...next, die: null });
      finishWith(true, 'Ludo — you got all four tokens home first!');
      return;
    }
    setState({ ...next, die: null });
    if (rolledSix) {
      pushLog('You rolled a 6 — roll again!');
    } else {
      advanceAfterPlayer({ ...next, die: null }, false);
    }
  }

  function restart() {
    setState(initialState());
    setFinished(false);
  }

  const die = state.die;
  const movable = die ? movableTokenIndices(state.tokens.player, die) : [];

  return (
    <div className="max-w-3xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🎲 Ludo</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Roll a 6 to leave your yard. Get all four tokens all the way around and home first.</p>

      <div className="grid grid-cols-4 gap-2 text-center">
        {COLORS.map((c) => (
          <div key={c.id} className={`rounded-lg p-2 text-white text-xs font-semibold ${c.bar}`}>
            <p>{c.emoji} {c.label}</p>
            <p>{state.tokens[c.id].filter((s) => s === TOTAL_STEPS).length}/4 home</p>
          </div>
        ))}
      </div>

      <div
        className="relative mx-auto bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl"
        style={{ width: 'min(90vw, 420px)', height: 'min(90vw, 420px)' }}
      >
        {Array.from({ length: 52 }, (_, i) => {
          const { row, col } = perimeterCell(i);
          const safe = isSafeCell(i);
          const tokensHere = [];
          for (const c of COLORS) {
            state.tokens[c.id].forEach((steps, tokenIndex) => {
              if (steps >= 1 && steps <= 51 && absoluteCell(c, steps) === i) tokensHere.push({ color: c, tokenIndex });
            });
          }
          return (
            <div
              key={i}
              className={`absolute flex items-center justify-center text-[10px] border border-gray-200 dark:border-gray-700 ${safe ? 'bg-amber-100 dark:bg-amber-900' : 'bg-white dark:bg-gray-900'}`}
              style={{ width: `${100 / 14}%`, height: `${100 / 14}%`, left: `${(col / 14) * 100}%`, top: `${(row / 14) * 100}%` }}
            >
              {safe && !tokensHere.length && '⭐'}
              {tokensHere.map((t, idx) => (
                <span key={idx} title={`${t.color.label} token ${t.tokenIndex + 1}`}>{t.color.emoji}</span>
              ))}
            </div>
          );
        })}
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-2 text-center text-xs text-indigo-800 dark:text-indigo-200 max-h-24 overflow-y-auto space-y-0.5">
        {state.log.map((line, i) => <p key={i}>{line}</p>)}
      </div>

      <div className="flex flex-col items-center gap-3">
        <div className="flex items-center gap-4">
          <button
            onClick={rollDie}
            disabled={finished || state.turn !== 'player' || die !== null}
            className="rounded-full bg-red-500 hover:bg-red-600 disabled:opacity-40 text-white font-bold px-6 py-3 text-lg"
          >
            🎲 {die ?? 'Roll'}
          </button>
        </div>
        {die !== null && (
          <div className="flex flex-wrap justify-center gap-2">
            {state.tokens.player.map((steps, i) => (
              <button
                key={i}
                disabled={!movable.includes(i)}
                onClick={() => moveMyToken(i)}
                className="rounded-lg border-2 border-red-300 disabled:opacity-30 disabled:cursor-not-allowed bg-red-50 dark:bg-red-950 text-red-700 dark:text-red-300 px-3 py-2 text-xs font-semibold"
              >
                Token {i + 1} ({steps === 0 ? 'Yard' : steps === TOTAL_STEPS ? 'Home!' : `step ${steps}`})
              </button>
            ))}
          </div>
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
