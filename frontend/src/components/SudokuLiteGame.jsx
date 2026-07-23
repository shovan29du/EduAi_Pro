import React, { useState } from 'react';

export default function SudokuLiteGame({ title, blurb, size, puzzle, solution }) {
  const [grid, setGrid] = useState(() => puzzle.map((row) => [...row]));
  const [selected, setSelected] = useState(null);
  const [message, setMessage] = useState(null);

  function selectCell(r, c) {
    if (puzzle[r][c] !== 0) return;
    setSelected({ r, c });
    setMessage(null);
  }

  function placeNumber(n) {
    if (!selected) return;
    const { r, c } = selected;
    setGrid((g) => {
      const copy = g.map((row) => [...row]);
      copy[r][c] = n;
      return copy;
    });
  }

  function checkSolution() {
    const isComplete = grid.every((row) => row.every((v) => v !== 0));
    if (!isComplete) {
      setMessage('Fill in every cell first.');
      return;
    }
    const isCorrect = grid.every((row, r) => row.every((v, c) => v === solution[r][c]));
    setMessage(isCorrect ? 'Correct — solved! 🎉' : 'Not quite right — check each row, column, and box for repeats.');
  }

  function reset() {
    setGrid(puzzle.map((row) => [...row]));
    setSelected(null);
    setMessage(null);
  }

  return (
    <section aria-label={`${title} sudoku`} className="space-y-3 rounded border p-4 dark:border-gray-700">
      <h3 className="font-semibold">{title}</h3>
      {blurb && <p className="text-sm text-gray-600 dark:text-gray-400">{blurb}</p>}

      <div
        className="inline-grid gap-1"
        style={{ gridTemplateColumns: `repeat(${size}, minmax(0, 1fr))` }}
        role="grid"
        aria-label="Sudoku grid"
      >
        {grid.map((row, r) =>
          row.map((value, c) => {
            const isFixed = puzzle[r][c] !== 0;
            const isSelected = selected && selected.r === r && selected.c === c;
            return (
              <button
                key={`${r}-${c}`}
                type="button"
                onClick={() => selectCell(r, c)}
                disabled={isFixed}
                aria-label={`Row ${r + 1} column ${c + 1}`}
                className={`flex h-9 w-9 items-center justify-center rounded border text-sm font-semibold ${
                  isFixed
                    ? 'bg-gray-200 text-gray-700 dark:bg-gray-700 dark:text-gray-200'
                    : isSelected
                      ? 'border-blue-500 bg-blue-50 dark:bg-blue-950'
                      : 'bg-white dark:bg-gray-900'
                }`}
              >
                {value !== 0 ? value : ''}
              </button>
            );
          })
        )}
      </div>

      <div className="flex flex-wrap gap-2">
        {Array.from({ length: size }, (_, i) => i + 1).map((n) => (
          <button
            key={n}
            type="button"
            onClick={() => placeNumber(n)}
            disabled={!selected}
            className="rounded border px-3 py-1 text-sm"
          >
            {n}
          </button>
        ))}
        <button type="button" onClick={() => placeNumber(0)} disabled={!selected} className="rounded border px-3 py-1 text-sm">
          Clear
        </button>
      </div>

      <div className="flex flex-wrap gap-2">
        <button type="button" onClick={checkSolution} className="rounded border px-3 py-1 text-sm">
          Check solution
        </button>
        <button type="button" onClick={reset} className="rounded border px-3 py-1 text-sm">
          Reset
        </button>
      </div>

      {message && <p className="font-medium">{message}</p>}
    </section>
  );
}
