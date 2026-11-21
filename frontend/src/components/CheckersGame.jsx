import React, { useState } from 'react';
import GameScoreBadge from './GameScoreBadge.jsx';

// Standard English draughts: 12 men each on the dark squares of an 8x8
// board, mandatory captures, multi-jump chains, and kinging on the back row.

function initialBoard() {
  const board = Array.from({ length: 8 }, () => Array(8).fill(null));
  for (let r = 0; r < 3; r++) for (let c = 0; c < 8; c++) if ((r + c) % 2 === 1) board[r][c] = { owner: 'cpu', king: false };
  for (let r = 5; r < 8; r++) for (let c = 0; c < 8; c++) if ((r + c) % 2 === 1) board[r][c] = { owner: 'player', king: false };
  return board;
}

function inBounds(r, c) {
  return r >= 0 && r < 8 && c >= 0 && c < 8;
}

function dirsFor(piece) {
  if (piece.king) return [[-1, -1], [-1, 1], [1, -1], [1, 1]];
  return piece.owner === 'player' ? [[-1, -1], [-1, 1]] : [[1, -1], [1, 1]];
}

function capturesFrom(board, r, c) {
  const piece = board[r][c];
  const caps = [];
  for (const [dr, dc] of dirsFor(piece)) {
    const mr = r + dr, mc = c + dc, er = r + 2 * dr, ec = c + 2 * dc;
    if (!inBounds(er, ec)) continue;
    const mid = board[mr][mc];
    if (mid && mid.owner !== piece.owner && !board[er][ec]) {
      caps.push({ from: [r, c], to: [er, ec], captured: [mr, mc] });
    }
  }
  return caps;
}

function simpleMovesFrom(board, r, c) {
  const piece = board[r][c];
  const moves = [];
  for (const [dr, dc] of dirsFor(piece)) {
    const nr = r + dr, nc = c + dc;
    if (inBounds(nr, nc) && !board[nr][nc]) moves.push({ from: [r, c], to: [nr, nc] });
  }
  return moves;
}

function allMovesFor(board, owner) {
  let captures = [];
  let simples = [];
  for (let r = 0; r < 8; r++) {
    for (let c = 0; c < 8; c++) {
      const p = board[r][c];
      if (!p || p.owner !== owner) continue;
      captures = captures.concat(capturesFrom(board, r, c));
      simples = simples.concat(simpleMovesFrom(board, r, c));
    }
  }
  return captures.length > 0 ? captures : simples;
}

function applyMove(board, move) {
  const next = board.map((row) => row.slice());
  const piece = next[move.from[0]][move.from[1]];
  next[move.from[0]][move.from[1]] = null;
  let king = piece.king;
  if (!king) {
    if (piece.owner === 'player' && move.to[0] === 0) king = true;
    if (piece.owner === 'cpu' && move.to[0] === 7) king = true;
  }
  next[move.to[0]][move.to[1]] = { owner: piece.owner, king };
  if (move.captured) next[move.captured[0]][move.captured[1]] = null;
  return next;
}

function countPieces(board, owner) {
  let n = 0;
  for (const row of board) for (const cell of row) if (cell && cell.owner === owner) n++;
  return n;
}

function isExposed(board, owner, square) {
  const opponent = owner === 'player' ? 'cpu' : 'player';
  const oppCaptures = allMovesFor(board, opponent).filter((m) => m.captured);
  return oppCaptures.some((m) => m.captured[0] === square[0] && m.captured[1] === square[1]);
}

function pickCpuMove(board) {
  const moves = allMovesFor(board, 'cpu');
  let best = moves[0];
  let bestScore = -Infinity;
  for (const m of moves) {
    const after = applyMove(board, m);
    let score = m.captured ? 5 : 0;
    const landed = after[m.to[0]][m.to[1]];
    if (landed.king && !board[m.from[0]][m.from[1]].king) score += 3;
    if (isExposed(after, 'cpu', m.to)) score -= 4;
    score += Math.random();
    if (score > bestScore) {
      bestScore = score;
      best = m;
    }
  }
  return best;
}

export default function CheckersGame({ onComplete, stats }) {
  const [board, setBoard] = useState(initialBoard);
  const [turn, setTurn] = useState('player');
  const [selected, setSelected] = useState(null);
  const [forcedFrom, setForcedFrom] = useState(null);
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('You (red) move first — captures are mandatory when available.');

  function finish(playerWon) {
    setFinished(true);
    if (onComplete) {
      onComplete({
        score: playerWon ? 1 : 0,
        maxScore: 1,
        label: `Checkers — ${playerWon ? 'you won!' : 'the computer won'}`,
      });
    }
  }

  function afterPlayerMove(nextBoard, move) {
    setBoard(nextBoard);
    if (move.captured) {
      const chain = capturesFrom(nextBoard, move.to[0], move.to[1]);
      if (chain.length > 0) {
        setSelected(move.to);
        setForcedFrom(move.to);
        setMessage('Capture again with the same piece!');
        return;
      }
    }
    setSelected(null);
    setForcedFrom(null);
    const cpuMoves = allMovesFor(nextBoard, 'cpu');
    if (cpuMoves.length === 0 || countPieces(nextBoard, 'cpu') === 0) {
      finish(true);
      return;
    }
    setTurn('cpu');
    setMessage("Computer's turn…");
    setTimeout(() => runCpu(nextBoard), 400);
  }

  function runCpu(current) {
    let cb = current;
    let guard = 0;
    while (guard < 12) {
      guard++;
      const move = pickCpuMove(cb);
      cb = applyMove(cb, move);
      if (move.captured) {
        const chain = capturesFrom(cb, move.to[0], move.to[1]);
        if (chain.length > 0) continue;
      }
      break;
    }
    setBoard(cb);
    const playerMoves = allMovesFor(cb, 'player');
    if (playerMoves.length === 0 || countPieces(cb, 'player') === 0) {
      finish(false);
      return;
    }
    setTurn('player');
    setMessage('Your move.');
  }

  function clickCell(r, c) {
    if (finished || turn !== 'player') return;
    const legal = allMovesFor(board, 'player').filter((m) => !forcedFrom || (m.from[0] === forcedFrom[0] && m.from[1] === forcedFrom[1]));
    if (!selected) {
      const piece = board[r][c];
      if (piece && piece.owner === 'player' && legal.some((m) => m.from[0] === r && m.from[1] === c)) {
        setSelected([r, c]);
      }
      return;
    }
    if (forcedFrom && (selected[0] !== forcedFrom[0] || selected[1] !== forcedFrom[1])) return;
    const move = legal.find((m) => m.from[0] === selected[0] && m.from[1] === selected[1] && m.to[0] === r && m.to[1] === c);
    if (move) {
      afterPlayerMove(applyMove(board, move), move);
      return;
    }
    if (!forcedFrom) {
      const piece = board[r][c];
      if (piece && piece.owner === 'player' && legal.some((m) => m.from[0] === r && m.from[1] === c)) {
        setSelected([r, c]);
      } else {
        setSelected(null);
      }
    }
  }

  function restart() {
    setBoard(initialBoard());
    setTurn('player');
    setSelected(null);
    setForcedFrom(null);
    setFinished(false);
    setMessage('You (red) move first — captures are mandatory when available.');
  }

  const legalForSelected = selected
    ? allMovesFor(board, 'player').filter((m) => m.from[0] === selected[0] && m.from[1] === selected[1])
    : [];

  return (
    <div className="max-w-lg mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🔴 Checkers</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Move diagonally onto dark squares. Jump an adjacent enemy piece to capture it — captures are mandatory, and you can chain multiple jumps.</p>

      <div className="bg-amber-900 rounded-xl p-1 mx-auto" style={{ width: 'min(90vw, 360px)' }}>
        <div className="grid grid-cols-8">
          {board.map((row, r) =>
            row.map((cell, c) => {
              const dark = (r + c) % 2 === 1;
              const isSelected = selected && selected[0] === r && selected[1] === c;
              const isTarget = legalForSelected.some((m) => m.to[0] === r && m.to[1] === c);
              return (
                <button
                  key={`${r}-${c}`}
                  onClick={() => clickCell(r, c)}
                  disabled={!dark || finished}
                  className={`aspect-square flex items-center justify-center ${dark ? 'bg-amber-700' : 'bg-amber-100'} ${isSelected ? 'ring-2 ring-inset ring-amber-300' : ''}`}
                >
                  {cell && (
                    <span
                      className={`block w-4/5 h-4/5 rounded-full border-2 flex items-center justify-center text-xs font-bold ${
                        cell.owner === 'player' ? 'bg-red-600 border-red-800 text-red-100' : 'bg-gray-800 border-black text-gray-200'
                      }`}
                    >
                      {cell.king ? '♛' : ''}
                    </span>
                  )}
                  {!cell && isTarget && <span className="w-2 h-2 rounded-full bg-emerald-400" />}
                </button>
              );
            })
          )}
        </div>
      </div>

      <div className="flex justify-center gap-6 text-sm font-semibold">
        <span>🔴 You: {countPieces(board, 'player')}</span>
        <span>⚫ Computer: {countPieces(board, 'cpu')}</span>
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
