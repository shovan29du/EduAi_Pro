import React, { useState } from 'react';
import GameScoreBadge from './GameScoreBadge.jsx';

const SIZE = 8;
const DIRS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

// Corners and edges are worth more than open interior squares — a standard,
// simple Othello heuristic (no deep search needed to be a fair opponent).
const WEIGHTS = [
  [100, -20, 10, 5, 5, 10, -20, 100],
  [-20, -50, -2, -2, -2, -2, -50, -20],
  [10, -2, 1, 1, 1, 1, -2, 10],
  [5, -2, 1, 1, 1, 1, -2, 5],
  [5, -2, 1, 1, 1, 1, -2, 5],
  [10, -2, 1, 1, 1, 1, -2, 10],
  [-20, -50, -2, -2, -2, -2, -50, -20],
  [100, -20, 10, 5, 5, 10, -20, 100],
];

function initialBoard() {
  const board = Array.from({ length: SIZE }, () => Array(SIZE).fill(null));
  board[3][3] = 'O';
  board[3][4] = 'X';
  board[4][3] = 'X';
  board[4][4] = 'O';
  return board;
}

function flipsFor(board, r, c, player) {
  if (board[r][c]) return [];
  const opp = player === 'X' ? 'O' : 'X';
  let allFlips = [];
  for (const [dr, dc] of DIRS) {
    let rr = r + dr, cc = c + dc;
    const line = [];
    while (rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE && board[rr][cc] === opp) {
      line.push([rr, cc]);
      rr += dr;
      cc += dc;
    }
    if (line.length && rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE && board[rr][cc] === player) {
      allFlips = allFlips.concat(line);
    }
  }
  return allFlips;
}

function validMoves(board, player) {
  const moves = [];
  for (let r = 0; r < SIZE; r++) {
    for (let c = 0; c < SIZE; c++) {
      const flips = flipsFor(board, r, c, player);
      if (flips.length) moves.push({ r, c, flips });
    }
  }
  return moves;
}

function applyMove(board, move, player) {
  const next = board.map((row) => row.slice());
  next[move.r][move.c] = player;
  for (const [fr, fc] of move.flips) next[fr][fc] = player;
  return next;
}

function counts(board) {
  let x = 0, o = 0;
  for (const row of board) for (const cell of row) {
    if (cell === 'X') x++;
    else if (cell === 'O') o++;
  }
  return { x, o };
}

export default function ReversiGame({ onComplete, stats }) {
  const [board, setBoard] = useState(initialBoard);
  const [turn, setTurn] = useState('X');
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('You are black (⚫). Flip white discs by trapping them.');

  const { x, o } = counts(board);
  const playerMoves = validMoves(board, 'X');

  function finish(finalBoard) {
    const { x: fx, o: fo } = counts(finalBoard);
    setFinished(true);
    let score, label;
    if (fx > fo) {
      score = 1;
      label = `Reversi — you won ${fx}-${fo}`;
      setMessage(`🎉 You win ${fx}-${fo}!`);
    } else if (fx < fo) {
      score = 0;
      label = `Reversi — the computer won ${fo}-${fx}`;
      setMessage(`The computer wins ${fo}-${fx}.`);
    } else {
      score = 0.5;
      label = `Reversi — a ${fx}-${fo} tie`;
      setMessage(`It's a tie, ${fx}-${fo}!`);
    }
    if (onComplete) onComplete({ score, maxScore: 1, label });
  }

  function bestMoveFor(currentBoard, player) {
    const moves = validMoves(currentBoard, player);
    let best = moves[0];
    let bestScore = -Infinity;
    for (const m of moves) {
      const after = applyMove(currentBoard, m, player);
      let s = WEIGHTS[m.r][m.c] + m.flips.length;
      const { x: ax, o: ao } = counts(after);
      s += (player === 'O' ? ao - ax : ax - ao) * 0.1;
      if (s > bestScore) {
        bestScore = s;
        best = m;
      }
    }
    return best;
  }

  function nextTurnAfter(currentBoard, justMoved) {
    const other = justMoved === 'X' ? 'O' : 'X';
    const otherMoves = validMoves(currentBoard, other);
    if (otherMoves.length > 0) {
      setTurn(other);
      if (other === 'O') runCpu(currentBoard);
      else setMessage('Your move.');
      return;
    }
    const selfMoves = validMoves(currentBoard, justMoved);
    if (selfMoves.length > 0) {
      setMessage(`No moves for ${other === 'O' ? 'the computer' : 'you'} — turn skipped.`);
      setTurn(justMoved);
      if (justMoved === 'O') runCpu(currentBoard);
      return;
    }
    finish(currentBoard);
  }

  function runCpu(currentBoard) {
    setTimeout(() => {
      const move = bestMoveFor(currentBoard, 'O');
      const next = applyMove(currentBoard, move, 'O');
      setBoard(next);
      nextTurnAfter(next, 'O');
    }, 300);
  }

  function clickCell(r, c) {
    if (finished || turn !== 'X') return;
    const move = playerMoves.find((m) => m.r === r && m.c === c);
    if (!move) return;
    const next = applyMove(board, move, 'X');
    setBoard(next);
    nextTurnAfter(next, 'X');
  }

  function restart() {
    setBoard(initialBoard());
    setTurn('X');
    setFinished(false);
    setMessage('You are black (⚫). Flip white discs by trapping them.');
  }

  return (
    <div className="max-w-lg mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">⚫ Reversi</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Sandwich the computer's discs to flip them to your colour. Most discs when the board fills wins.</p>

      <div className="flex justify-center gap-6 text-sm font-semibold">
        <span>⚫ You: {x}</span>
        <span>⚪ Computer: {o}</span>
      </div>

      <div className="bg-emerald-700 rounded-xl p-2 mx-auto" style={{ width: 'min(90vw, 360px)' }}>
        <div className="grid grid-cols-8 gap-0.5">
          {board.map((row, r) =>
            row.map((cell, c) => {
              const isMove = turn === 'X' && !finished && playerMoves.some((m) => m.r === r && m.c === c);
              return (
                <button
                  key={`${r}-${c}`}
                  onClick={() => clickCell(r, c)}
                  disabled={!isMove}
                  className={`aspect-square rounded-sm flex items-center justify-center ${isMove ? 'bg-emerald-500' : 'bg-emerald-600'}`}
                >
                  {cell && <span className={`block w-4/5 h-4/5 rounded-full ${cell === 'X' ? 'bg-gray-900' : 'bg-white'}`} />}
                  {!cell && isMove && <span className="w-2 h-2 rounded-full bg-emerald-200" />}
                </button>
              );
            })
          )}
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
