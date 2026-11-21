import React, { useState } from 'react';
import GameScoreBadge from './GameScoreBadge.jsx';

const ROWS = 6;
const COLS = 7;
const SEARCH_DEPTH = 4; // Shallow alpha-beta search — plenty strong on a 7x6 board.

function emptyBoard() {
  return Array.from({ length: ROWS }, () => Array(COLS).fill(null));
}

function dropRow(board, col) {
  for (let r = ROWS - 1; r >= 0; r--) {
    if (!board[r][col]) return r;
  }
  return -1;
}

function checkWinner(board) {
  const dirs = [[0, 1], [1, 0], [1, 1], [1, -1]];
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const p = board[r][c];
      if (!p) continue;
      for (const [dr, dc] of dirs) {
        let count = 1;
        for (let k = 1; k < 4; k++) {
          const rr = r + dr * k, cc = c + dc * k;
          if (rr < 0 || rr >= ROWS || cc < 0 || cc >= COLS || board[rr][cc] !== p) break;
          count++;
        }
        if (count >= 4) return p;
      }
    }
  }
  if (board.every((row) => row.every((c) => c))) return 'draw';
  return null;
}

function validCols(board) {
  const cols = [];
  for (let c = 0; c < COLS; c++) if (!board[0][c]) cols.push(c);
  return cols;
}

function scoreWindow(window, player) {
  const opp = player === 'O' ? 'X' : 'O';
  const mine = window.filter((c) => c === player).length;
  const theirs = window.filter((c) => c === opp).length;
  const empty = window.filter((c) => !c).length;
  if (mine === 4) return 100000;
  if (theirs === 4) return -100000;
  if (mine === 3 && empty === 1) return 50;
  if (theirs === 3 && empty === 1) return -60;
  if (mine === 2 && empty === 2) return 10;
  return 0;
}

function evaluate(board, player) {
  let score = 0;
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS - 3; c++) score += scoreWindow([board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3]], player);
  }
  for (let c = 0; c < COLS; c++) {
    for (let r = 0; r < ROWS - 3; r++) score += scoreWindow([board[r][c], board[r + 1][c], board[r + 2][c], board[r + 3][c]], player);
  }
  for (let r = 0; r < ROWS - 3; r++) {
    for (let c = 0; c < COLS - 3; c++) score += scoreWindow([board[r][c], board[r + 1][c + 1], board[r + 2][c + 2], board[r + 3][c + 3]], player);
  }
  for (let r = 3; r < ROWS; r++) {
    for (let c = 0; c < COLS - 3; c++) score += scoreWindow([board[r][c], board[r - 1][c + 1], board[r - 2][c + 2], board[r - 3][c + 3]], player);
  }
  return score;
}

function drop(board, col, player) {
  const row = dropRow(board, col);
  const next = board.map((r) => r.slice());
  next[row][col] = player;
  return next;
}

function alphabeta(board, depth, alpha, beta, maximizing) {
  const result = checkWinner(board);
  if (result === 'O') return { score: 1000000 + depth };
  if (result === 'X') return { score: -1000000 - depth };
  if (result === 'draw') return { score: 0 };
  if (depth === 0) return { score: evaluate(board, 'O') };

  const cols = validCols(board);
  let bestCol = cols[Math.floor(cols.length / 2)];
  if (maximizing) {
    let value = -Infinity;
    for (const col of cols) {
      const next = drop(board, col, 'O');
      const { score } = alphabeta(next, depth - 1, alpha, beta, false);
      if (score > value) {
        value = score;
        bestCol = col;
      }
      alpha = Math.max(alpha, value);
      if (alpha >= beta) break;
    }
    return { score: value, col: bestCol };
  }
  let value = Infinity;
  for (const col of cols) {
    const next = drop(board, col, 'X');
    const { score } = alphabeta(next, depth - 1, alpha, beta, true);
    if (score < value) {
      value = score;
      bestCol = col;
    }
    beta = Math.min(beta, value);
    if (alpha >= beta) break;
  }
  return { score: value, col: bestCol };
}

export default function ConnectFourGame({ onComplete, stats }) {
  const [board, setBoard] = useState(emptyBoard);
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('You are red. Drop a disc into a column.');
  const [thinking, setThinking] = useState(false);

  function finish(result) {
    setFinished(true);
    let score, label;
    if (result === 'X') {
      score = 1;
      label = 'Connect Four — you won!';
      setMessage('🎉 Four in a row — you win!');
    } else if (result === 'draw') {
      score = 0.5;
      label = 'Connect Four — a draw';
      setMessage('The board filled up — a draw.');
    } else {
      score = 0;
      label = 'Connect Four — the computer won';
      setMessage('The computer connected four first.');
    }
    if (onComplete) onComplete({ score, maxScore: 1, label });
  }

  function cpuMove(current) {
    setThinking(true);
    setTimeout(() => {
      const { col } = alphabeta(current, SEARCH_DEPTH, -Infinity, Infinity, true);
      const next = drop(current, col, 'O');
      setBoard(next);
      setThinking(false);
      const result = checkWinner(next);
      if (result) finish(result);
      else setMessage('Your move.');
    }, 250);
  }

  function dropDisc(col) {
    if (finished || thinking) return;
    if (dropRow(board, col) < 0) return;
    const next = drop(board, col, 'X');
    setBoard(next);
    const result = checkWinner(next);
    if (result) {
      finish(result);
      return;
    }
    cpuMove(next);
  }

  function restart() {
    setBoard(emptyBoard());
    setFinished(false);
    setThinking(false);
    setMessage('You are red. Drop a disc into a column.');
  }

  return (
    <div className="max-w-lg mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🔴 Connect Four</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Get four discs in a row — horizontally, vertically, or diagonally — before the computer does.</p>

      <div className="flex gap-1 justify-center">
        {Array.from({ length: COLS }, (_, c) => (
          <button
            key={c}
            disabled={finished || thinking || dropRow(board, c) < 0}
            onClick={() => dropDisc(c)}
            className="w-9 h-7 rounded bg-indigo-100 dark:bg-indigo-900 disabled:opacity-30 text-xs font-bold text-indigo-700 dark:text-indigo-300 hover:bg-indigo-200"
          >
            ▼
          </button>
        ))}
      </div>

      <div className="bg-blue-700 rounded-xl p-2 inline-block mx-auto">
        <div className="grid gap-1" style={{ gridTemplateColumns: `repeat(${COLS}, minmax(0, 1fr))` }}>
          {board.map((row, r) =>
            row.map((cell, c) => (
              <div
                key={`${r}-${c}`}
                className={`w-9 h-9 rounded-full flex items-center justify-center ${
                  cell === 'X' ? 'bg-red-500' : cell === 'O' ? 'bg-amber-400' : 'bg-blue-900'
                }`}
              />
            ))
          )}
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-3 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {thinking ? 'Computer is thinking…' : message}
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
