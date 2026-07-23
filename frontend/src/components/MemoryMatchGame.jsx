import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';

function buildCards(pairs) {
  return shuffle(
    pairs.flatMap((pair, i) => [
      { id: `${i}-a`, matchId: i, content: pair[0] },
      { id: `${i}-b`, matchId: i, content: pair[1] },
    ])
  );
}

export default function MemoryMatchGame({ title, blurb, pairs }) {
  const [cards, setCards] = useState(() => buildCards(pairs));
  const [flipped, setFlipped] = useState([]);
  const [matched, setMatched] = useState(new Set());
  const [moves, setMoves] = useState(0);
  const [busy, setBusy] = useState(false);

  const finished = matched.size === pairs.length;

  function flip(card) {
    if (busy || finished) return;
    if (flipped.includes(card.id) || matched.has(card.matchId)) return;

    if (flipped.length === 0) {
      setFlipped([card.id]);
      return;
    }

    const firstCard = cards.find((c) => c.id === flipped[0]);
    setFlipped([flipped[0], card.id]);
    setMoves((m) => m + 1);
    setBusy(true);
    setTimeout(() => {
      if (firstCard.matchId === card.matchId) {
        setMatched((prev) => new Set(prev).add(card.matchId));
      }
      setFlipped([]);
      setBusy(false);
    }, 650);
  }

  function restart() {
    setCards(buildCards(pairs));
    setFlipped([]);
    setMatched(new Set());
    setMoves(0);
    setBusy(false);
  }

  return (
    <section aria-label={`${title} memory match game`} className="space-y-3 rounded border p-4 dark:border-gray-700">
      <h3 className="font-semibold">{title}</h3>
      {blurb && <p className="text-sm text-gray-600 dark:text-gray-400">{blurb}</p>}
      <p className="text-sm">
        Pairs found: <span className="font-semibold">{matched.size}</span> / {pairs.length} · Moves:{' '}
        <span className="font-semibold">{moves}</span>
      </p>
      <div className="grid grid-cols-4 gap-2">
        {cards.map((card) => {
          const isFaceUp = flipped.includes(card.id) || matched.has(card.matchId);
          return (
            <button
              key={card.id}
              type="button"
              onClick={() => flip(card)}
              disabled={matched.has(card.matchId)}
              aria-pressed={isFaceUp}
              className={`flex h-16 items-center justify-center rounded border text-sm font-semibold ${
                matched.has(card.matchId)
                  ? 'border-green-400 bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                  : isFaceUp
                    ? 'border-blue-400 bg-blue-50 dark:bg-blue-950'
                    : 'bg-gray-100 dark:bg-gray-800'
              }`}
            >
              {isFaceUp ? card.content : '❓'}
            </button>
          );
        })}
      </div>
      {finished && (
        <div className="space-y-2">
          <p className="font-medium">Solved in {moves} moves! 🎉</p>
          <button type="button" onClick={restart} className="rounded border px-3 py-1 text-sm">
            Play again
          </button>
        </div>
      )}
    </section>
  );
}
