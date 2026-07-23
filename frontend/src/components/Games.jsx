import React, { useState } from 'react';
import PhonicsMatchGame from './PhonicsMatchGame.jsx';
import QuizSprintGame from './QuizSprintGame.jsx';
import MemoryMatchGame from './MemoryMatchGame.jsx';
import SequenceRecallGame from './SequenceRecallGame.jsx';
import MathSprintGame from './MathSprintGame.jsx';
import WordScrambleGame from './WordScrambleGame.jsx';
import MCRoundsGame from './MCRoundsGame.jsx';
import SudokuLiteGame from './SudokuLiteGame.jsx';
import ReactionGame from './ReactionGame.jsx';
import { CATEGORIES, GAMES, gamesByCategory, TOTAL_GAMES } from '../data/gameCentreData.js';

const EXTERNAL_COMPONENTS = {
  PhonicsMatchGame,
  QuizSprintGame,
};

function renderGame(game, grade) {
  switch (game.engine) {
    case 'memory':
      return <MemoryMatchGame title={game.data.title} blurb={game.data.blurb} pairs={game.data.pairs} />;
    case 'sequence':
      return <SequenceRecallGame title={game.data.title} blurb={game.data.blurb} tiles={game.data.tiles} />;
    case 'mathsprint':
      return <MathSprintGame title={game.data.title} blurb={game.data.blurb} generate={game.data.generate} />;
    case 'scramble':
      return <WordScrambleGame title={game.data.title} blurb={game.data.blurb} words={game.data.words} />;
    case 'mc':
      return <MCRoundsGame title={game.data.title} blurb={game.data.blurb} rounds={game.data.rounds} />;
    case 'sudoku':
      return (
        <SudokuLiteGame
          title={game.data.title}
          blurb={game.data.blurb}
          size={game.data.size}
          puzzle={game.data.puzzle}
          solution={game.data.solution}
        />
      );
    case 'reaction':
      return (
        <ReactionGame
          title={game.data.title}
          blurb={game.data.blurb}
          target={game.data.target}
          distractorPool={game.data.distractorPool}
          gridSize={game.data.gridSize}
        />
      );
    case 'external': {
      const Component = EXTERNAL_COMPONENTS[game.data.component];
      if (!Component) return null;
      return game.data.component === 'QuizSprintGame' ? <Component grade={grade} /> : <Component />;
    }
    default:
      return null;
  }
}

export default function Games({ grade }) {
  const [categoryId, setCategoryId] = useState(null);
  const [gameId, setGameId] = useState(null);

  const category = CATEGORIES.find((c) => c.id === categoryId) || null;
  const game = GAMES.find((g) => g.id === gameId) || null;

  // ── Single game view ──────────────────────────────────────────────────
  if (game) {
    return (
      <div className="max-w-3xl mx-auto space-y-4">
        <button
          type="button"
          onClick={() => setGameId(null)}
          className="text-sm text-blue-600 hover:underline"
        >
          ← Back to {category ? category.label : 'Game Centre'}
        </button>
        {renderGame(game, grade)}
      </div>
    );
  }

  // ── Category view: list of games within a category ──────────────────
  if (category) {
    const games = gamesByCategory(category.id);
    return (
      <div className="max-w-3xl mx-auto space-y-4">
        <button
          type="button"
          onClick={() => setCategoryId(null)}
          className="text-sm text-blue-600 hover:underline"
        >
          ← All Categories
        </button>
        <h2 className="text-2xl font-bold">
          {category.emoji} {category.label}
        </h2>
        <p className="text-gray-500 dark:text-gray-400 text-sm">{category.desc}</p>
        <p className="text-xs text-gray-400">
          {games.length} game{games.length !== 1 ? 's' : ''} in this category
        </p>
        <div className="grid sm:grid-cols-2 gap-4">
          {games.map((g) => (
            <button
              key={g.id}
              type="button"
              onClick={() => setGameId(g.id)}
              className="text-left rounded-xl border-2 border-blue-200 dark:border-blue-900 bg-gradient-to-br from-blue-50 to-sky-50 dark:from-gray-800 dark:to-gray-900 p-4 hover:shadow-lg transition-shadow"
            >
              <p className="text-2xl mb-1">{g.emoji}</p>
              <p className="font-bold text-gray-800 dark:text-gray-100">{g.title}</p>
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">{g.blurb}</p>
            </button>
          ))}
        </div>
      </div>
    );
  }

  // ── Top-level picker: all categories ─────────────────────────────────
  return (
    <div className="max-w-3xl mx-auto space-y-4">
      <h1 className="text-3xl font-bold text-blue-700 dark:text-blue-300">🎮 Game Centre</h1>
      <p className="text-gray-500 dark:text-gray-400">
        Brain-development games and puzzles — {TOTAL_GAMES} games across {CATEGORIES.length} categories.
      </p>
      <div className="grid sm:grid-cols-2 gap-4">
        {CATEGORIES.map((cat) => {
          const count = gamesByCategory(cat.id).length;
          return (
            <button
              key={cat.id}
              type="button"
              onClick={() => setCategoryId(cat.id)}
              className="text-left rounded-xl border-2 border-blue-200 dark:border-blue-900 bg-gradient-to-br from-blue-50 to-sky-50 dark:from-gray-800 dark:to-gray-900 p-5 hover:shadow-lg transition-shadow"
            >
              <p className="text-3xl mb-2">{cat.emoji}</p>
              <p className="font-bold text-gray-800 dark:text-gray-100">{cat.label}</p>
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">{cat.desc}</p>
              <p className="text-xs text-blue-600 dark:text-blue-400 mt-2">
                {count} game{count !== 1 ? 's' : ''}
              </p>
            </button>
          );
        })}
      </div>
    </div>
  );
}
