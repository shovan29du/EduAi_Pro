import React, { useState } from 'react';
import GameScoreBadge from './GameScoreBadge.jsx';

// Standard 2-player Kalah: 6 pits per side + 1 store each, 4 seeds per pit.
// Board layout, index 0-13: 0-5 = player pits, 6 = player store,
// 7-12 = computer pits, 13 = computer store.
const PLAYER_PITS = [0, 1, 2, 3, 4, 5];
const PLAYER_STORE = 6;
const CPU_PITS = [7, 8, 9, 10, 11, 12];
const CPU_STORE = 13;

function initialBoard() {
  const board = Array(14).fill(4);
  board[PLAYER_STORE] = 0;
  board[CPU_STORE] = 0;
  return board;
}

function oppositePit(i) {
  return 12 - i;
}

function sow(board, pit, owner) {
  const next = board.slice();
  let seeds = next[pit];
  next[pit] = 0;
  let i = pit;
  const skipStore = owner === 'player' ? CPU_STORE : PLAYER_STORE;
  while (seeds > 0) {
    i = (i + 1) % 14;
    if (i === skipStore) continue;
    next[i] += 1;
    seeds -= 1;
  }
  const ownPits = owner === 'player' ? PLAYER_PITS : CPU_PITS;
  const ownStore = owner === 'player' ? PLAYER_STORE : CPU_STORE;
  // Landing the last seed in your own empty pit captures it plus the opposite pit.
  if (ownPits.includes(i) && next[i] === 1) {
    const opp = oppositePit(i);
    if (next[opp] > 0) {
      next[ownStore] += next[opp] + 1;
      next[i] = 0;
      next[opp] = 0;
    }
  }
  const extraTurn = i === ownStore;
  return { board: next, extraTurn };
}

function sideEmpty(board, pits) {
  return pits.every((p) => board[p] === 0);
}

function finalizeIfOver(board) {
  if (sideEmpty(board, PLAYER_PITS) || sideEmpty(board, CPU_PITS)) {
    const next = board.slice();
    for (const p of PLAYER_PITS) {
      next[PLAYER_STORE] += next[p];
      next[p] = 0;
    }
    for (const p of CPU_PITS) {
      next[CPU_STORE] += next[p];
      next[p] = 0;
    }
    return next;
  }
  return board;
}

export default function MancalaGame({ onComplete, stats }) {
  const [board, setBoard] = useState(initialBoard);
  const [turn, setTurn] = useState('player');
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('Pick a pit on your side to sow its seeds.');

  function finish(finalBoard) {
    setFinished(true);
    const p = finalBoard[PLAYER_STORE];
    const c = finalBoard[CPU_STORE];
    let score, label;
    if (p > c) {
      score = 1;
      label = `Mancala — you won ${p}-${c}`;
      setMessage(`🎉 You win ${p}-${c}!`);
    } else if (p < c) {
      score = 0;
      label = `Mancala — the computer won ${c}-${p}`;
      setMessage(`The computer wins ${c}-${p}.`);
    } else {
      score = 0.5;
      label = `Mancala — a ${p}-${c} tie`;
      setMessage(`It's a tie, ${p}-${c}!`);
    }
    if (onComplete) onComplete({ score, maxScore: 1, label });
  }

  function afterMove(next, owner, extraTurn) {
    const closed = finalizeIfOver(next);
    setBoard(closed);
    if (closed !== next) {
      finish(closed);
      return;
    }
    if (extraTurn) {
      setMessage(owner === 'player' ? 'You land in your store — go again!' : 'Computer landed in its store — it goes again.');
      if (owner === 'cpu') setTimeout(() => runCpu(closed), 400);
      return;
    }
    if (owner === 'player') {
      setTurn('cpu');
      setMessage("Computer's turn…");
      setTimeout(() => runCpu(closed), 400);
    } else {
      setTurn('player');
      setMessage('Your move.');
    }
  }

  function runCpu(current) {
    const options = CPU_PITS.filter((p) => current[p] > 0);
    if (options.length === 0) {
      finish(finalizeIfOver(current));
      return;
    }
    // Prefer a move that lands exactly in the store (extra turn), else the pit with the most seeds.
    const simulated = options.map((p) => ({ p, ...sow(current, p, 'cpu') }));
    const withExtraTurn = simulated.find((m) => m.extraTurn);
    const chosen = withExtraTurn || simulated.reduce((a, b) => (current[b.p] > current[a.p] ? b : a));
    afterMove(chosen.board, 'cpu', chosen.extraTurn);
  }

  function clickPit(pit) {
    if (finished || turn !== 'player' || !PLAYER_PITS.includes(pit) || board[pit] === 0) return;
    const { board: next, extraTurn } = sow(board, pit, 'player');
    afterMove(next, 'player', extraTurn);
  }

  function restart() {
    setBoard(initialBoard());
    setTurn('player');
    setFinished(false);
    setMessage('Pick a pit on your side to sow its seeds.');
  }

  return (
    <div className="max-w-lg mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🌰 Mancala</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Sow seeds counter-clockwise. Land your last seed in your store for an extra turn, or in an empty pit of yours to capture.</p>

      <div className="rounded-xl bg-amber-100 dark:bg-amber-950 border border-amber-300 dark:border-amber-800 p-3 space-y-3">
        <div className="flex items-center gap-2">
          <div className="w-12 h-20 rounded-lg bg-amber-300 dark:bg-amber-800 flex items-center justify-center font-bold text-lg">{board[CPU_STORE]}</div>
          <div className="grid grid-cols-6 gap-1 flex-1">
            {[...CPU_PITS].reverse().map((p) => (
              <div key={p} className="aspect-square rounded-full bg-amber-200 dark:bg-amber-900 flex items-center justify-center font-semibold text-sm">
                {board[p]}
              </div>
            ))}
          </div>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-12 h-20" />
          <div className="grid grid-cols-6 gap-1 flex-1">
            {PLAYER_PITS.map((p) => (
              <button
                key={p}
                disabled={finished || turn !== 'player' || board[p] === 0}
                onClick={() => clickPit(p)}
                className="aspect-square rounded-full bg-amber-300 dark:bg-amber-800 hover:bg-amber-400 disabled:opacity-50 flex items-center justify-center font-semibold text-sm"
              >
                {board[p]}
              </button>
            ))}
          </div>
          <div className="w-12 h-20 rounded-lg bg-amber-300 dark:bg-amber-800 flex items-center justify-center font-bold text-lg">{board[PLAYER_STORE]}</div>
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      {finished && (
        <div className="flex justify-center">
          <button onClick={restart} className="rounded-full bg-gray-500 hover:bg-gray-600 text-white font-semibold px-6 py-2.5">
            Play Again
          </button>
        </div>
      )}
    </div>
  );
}
