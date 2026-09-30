import React, { useState } from 'react';
import GameScoreBadge from './GameScoreBadge.jsx';

const LINES = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8],
  [0, 3, 6], [1, 4, 7], [2, 5, 8],
  [0, 4, 8], [2, 4, 6],
];

function winnerOf(board) {
  for (const [a, b, c] of LINES) {
    if (board[a] && board[a] === board[b] && board[a] === board[c]) return board[a];
  }
  if (board.every((c) => c)) return 'draw';
  return null;
}

// Perfect-play minimax — the board is tiny (9 cells) so a full search is cheap.
function minimax(board, player) {
  const w = winnerOf(board);
  if (w === 'X') return { score: -1 };
  if (w === 'O') return { score: 1 };
  if (w === 'draw') return { score: 0 };

  const moves = [];
  for (let i = 0; i < 9; i++) {
    if (board[i]) continue;
    const next = board.slice();
    next[i] = player;
    const result = minimax(next, player === 'O' ? 'X' : 'O');
    moves.push({ index: i, score: result.score });
  }
  const best = player === 'O'
    ? moves.reduce((a, b) => (b.score > a.score ? b : a))
    : moves.reduce((a, b) => (b.score < a.score ? b : a));
  return best;
}

function emptyBoard() {
  return Array(9).fill(null);
}

export default function TicTacToeGame({ onComplete, stats }) {
  const [board, setBoard] = useState(emptyBoard);
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('You are X. Take the first move.');

  function finish(result) {
    setFinished(true);
    let score, label;
    if (result === 'X') {
      score = 1;
      label = 'Tic-Tac-Toe — you won!';
      setMessage('🎉 You win!');
    } else if (result === 'draw') {
      score = 0.5;
      label = 'Tic-Tac-Toe — a draw';
      setMessage("It's a draw — the computer plays perfectly!");
    } else {
      score = 0;
      label = 'Tic-Tac-Toe — the computer won';
      setMessage('The computer wins this time.');
    }
    if (onComplete) onComplete({ score, maxScore: 1, label });
  }

  function playCpu(current) {
    const best = minimax(current, 'O');
    const next = current.slice();
    next[best.index] = 'O';
    setBoard(next);
    const result = winnerOf(next);
    if (result) finish(result);
    else setMessage('Your move.');
  }

  function clickCell(i) {
    if (finished || board[i]) return;
    const next = board.slice();
    next[i] = 'X';
    setBoard(next);
    const result = winnerOf(next);
    if (result) {
      finish(result);
      return;
    }
    setTimeout(() => playCpu(next), 250);
  }

  function restart() {
    setBoard(emptyBoard());
    setFinished(false);
    setMessage('You are X. Take the first move.');
  }

  return (
    <div className="max-w-md mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">⭕ Tic-Tac-Toe</h2>
        <GameScoreBadge stats={stats} />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-400">Three in a row wins. The computer plays perfectly — a draw is a good result!</p>

      <div className="grid grid-cols-3 gap-2 w-full max-w-[280px] mx-auto">
        {board.map((cell, i) => (
          <button
            key={i}
            disabled={finished || !!cell}
            onClick={() => clickCell(i)}
            className="aspect-square rounded-lg border-2 border-indigo-200 dark:border-indigo-800 bg-white dark:bg-gray-800 flex items-center justify-center text-4xl font-bold disabled:cursor-not-allowed"
          >
            <span className={cell === 'X' ? 'text-indigo-600' : 'text-rose-500'}>{cell}</span>
          </button>
        ))}
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
