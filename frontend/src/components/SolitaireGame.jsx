import React, { useState } from 'react';
import { shuffle } from '../utils/gameUtils.js';
import { buildDeck, RANKS, SUITS } from '../utils/cardUtils.js';
import GameScoreBadge from './GameScoreBadge.jsx';

// A simplified Klondike Solitaire: single-card-selection UI (no drag and
// drop), but full real rules — foundations build Ace-to-King by suit,
// tableau columns build King-to-Ace in alternating colours, and a
// same-colour/descending run of already-face-up cards can be moved as one
// group by clicking its topmost (highest) card.

function rankIndex(rank) {
  return RANKS.indexOf(rank) + 1; // A=1 ... K=13
}

function dealTableau() {
  const deck = shuffle(buildDeck());
  const tableau = [];
  let cursor = 0;
  for (let col = 0; col < 7; col++) {
    const pile = [];
    for (let i = 0; i <= col; i++) {
      pile.push({ card: deck[cursor], faceUp: i === col });
      cursor++;
    }
    tableau.push(pile);
  }
  const stock = deck.slice(cursor).map((card) => ({ card, faceUp: false }));
  return { tableau, stock, waste: [], foundations: { '♠': [], '♥': [], '♦': [], '♣': [] } };
}

function CardChip({ card, faceUp, selected, onClick, small }) {
  const sizeCls = small ? 'w-12 h-16 text-sm' : 'w-14 h-20 text-base';
  if (!card) {
    return <div className={`${sizeCls} rounded-lg border-2 border-dashed border-gray-300 dark:border-gray-600`} onClick={onClick} />;
  }
  if (!faceUp) {
    return <div className={`${sizeCls} rounded-lg border-2 bg-indigo-600 border-indigo-700 cursor-pointer`} onClick={onClick} />;
  }
  const red = card.suit === '♥' || card.suit === '♦';
  return (
    <div
      onClick={onClick}
      className={`${sizeCls} rounded-lg border-2 bg-white flex flex-col items-center justify-center font-bold cursor-pointer transition-transform hover:-translate-y-1 ${
        selected ? 'border-amber-500 ring-2 ring-amber-400 -translate-y-1' : 'border-gray-300'
      } ${red ? 'text-red-600' : 'text-gray-800'}`}
    >
      <span>{card.rank}</span>
      <span>{card.suit}</span>
    </div>
  );
}

export default function SolitaireGame({ onComplete, stats }) {
  const [state, setState] = useState(dealTableau);
  const [selected, setSelected] = useState(null); // { colIndex, cardIndex } | 'waste' | null
  const [message, setMessage] = useState('Move cards from Ace up by suit to the foundations.');
  const [finished, setFinished] = useState(false);

  const foundationCount = () => Object.values(state.foundations).reduce((sum, pile) => sum + pile.length, 0);

  function finishGame(reason) {
    const count = foundationCount();
    setFinished(true);
    setMessage(reason);
    if (onComplete) {
      onComplete({ score: count, maxScore: 52, label: `Solitaire — ${count}/52 cards home` });
    }
  }

  function drawStock() {
    if (finished) return;
    if (state.stock.length > 0) {
      const [top, ...rest] = state.stock;
      setState((s) => ({ ...s, stock: rest, waste: [...s.waste, { card: top.card, faceUp: true }] }));
    } else if (state.waste.length > 0) {
      setState((s) => ({
        ...s,
        stock: s.waste.slice().reverse().map((w) => ({ card: w.card, faceUp: false })),
        waste: [],
      }));
    }
    setSelected(null);
  }

  function getMovingGroup() {
    if (!selected) return null;
    if (selected === 'waste') {
      const top = state.waste[state.waste.length - 1];
      return top ? { cards: [top.card], from: 'waste' } : null;
    }
    const pile = state.tableau[selected.colIndex];
    const cards = pile.slice(selected.cardIndex).map((p) => p.card);
    return { cards, from: 'tableau', colIndex: selected.colIndex, cardIndex: selected.cardIndex };
  }

  function tryFoundation(suit) {
    const group = getMovingGroup();
    if (!group || group.cards.length !== 1) return;
    const card = group.cards[0];
    if (card.suit !== suit) return;
    const pile = state.foundations[suit];
    const topRank = pile.length ? rankIndex(pile[pile.length - 1].rank) : 0;
    if (rankIndex(card.rank) !== topRank + 1) {
      setMessage('That card cannot go on that foundation yet.');
      setSelected(null);
      return;
    }
    applyMove(group, { foundations: { ...state.foundations, [suit]: [...pile, card] } });
  }

  function tryTableau(targetCol) {
    const group = getMovingGroup();
    if (!group) return;
    const first = group.cards[0];
    const destPile = state.tableau[targetCol];
    const top = destPile[destPile.length - 1];
    const valid = top
      ? top.faceUp && rankIndex(top.card.rank) === rankIndex(first.rank) + 1 && (top.card.suit === '♥' || top.card.suit === '♦') !== (first.suit === '♥' || first.suit === '♦')
      : rankIndex(first.rank) === 13;
    if (!valid) {
      setMessage('That card cannot go on that pile.');
      setSelected(null);
      return;
    }
    if (group.from === 'tableau' && group.colIndex === targetCol) {
      setSelected(null);
      return;
    }
    const newTableau = state.tableau.map((pile, i) =>
      i === targetCol ? [...pile, ...group.cards.map((card) => ({ card, faceUp: true }))] : pile
    );
    applyMove(group, { tableau: newTableau });
  }

  function applyMove(group, patch) {
    let tableau = patch.tableau || state.tableau;
    let waste = state.waste;
    if (group.from === 'waste') {
      waste = state.waste.slice(0, -1);
    } else if (group.from === 'tableau' && !patch.tableau) {
      tableau = state.tableau.map((pile, i) => (i === group.colIndex ? pile.slice(0, group.cardIndex) : pile));
    } else if (group.from === 'tableau' && patch.tableau) {
      tableau = patch.tableau.map((pile, i) => (i === group.colIndex ? state.tableau[i].slice(0, group.cardIndex) : pile));
    }
    // Flip the newly exposed top card of the source column, if any.
    tableau = tableau.map((pile) => {
      if (pile.length === 0) return pile;
      const last = pile[pile.length - 1];
      if (!last.faceUp) return [...pile.slice(0, -1), { ...last, faceUp: true }];
      return pile;
    });
    const foundations = patch.foundations || state.foundations;
    const newState = { ...state, tableau, waste, foundations };
    setState(newState);
    setSelected(null);

    const total = Object.values(foundations).reduce((sum, p) => sum + p.length, 0);
    if (total === 52) {
      setFinished(true);
      setMessage('🎉 You cleared the whole deck!');
      if (onComplete) onComplete({ score: 52, maxScore: 52, label: 'Solitaire — cleared the whole deck!' });
    } else {
      setMessage('Nice move!');
    }
  }

  function clickTableauCard(colIndex, cardIndex) {
    if (finished) return;
    const pile = state.tableau[colIndex];
    const entry = pile[cardIndex];
    if (!entry) {
      if (selected) tryTableau(colIndex);
      return;
    }
    if (!entry.faceUp) {
      if (cardIndex === pile.length - 1 && !selected) {
        setState((s) => ({
          ...s,
          tableau: s.tableau.map((p, i) => (i === colIndex ? [...p.slice(0, -1), { ...entry, faceUp: true }] : p)),
        }));
      }
      return;
    }
    if (selected && selected.colIndex === colIndex && selected.cardIndex === cardIndex) {
      setSelected(null);
      return;
    }
    if (selected) {
      tryTableau(colIndex);
      return;
    }
    setSelected({ colIndex, cardIndex });
  }

  function clickWaste() {
    if (finished || state.waste.length === 0) return;
    setSelected(selected === 'waste' ? null : 'waste');
  }

  function clickFoundation(suit) {
    if (finished || !selected) return;
    tryFoundation(suit);
  }

  function restart() {
    setState(dealTableau());
    setSelected(null);
    setFinished(false);
    setMessage('Move cards from Ace up by suit to the foundations.');
  }

  return (
    <div className="max-w-3xl mx-auto space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100">🂡 Solitaire</h2>
        <GameScoreBadge stats={stats} />
      </div>

      <div className="flex items-start justify-between gap-4">
        <div className="flex gap-2">
          <div onClick={drawStock} className="cursor-pointer">
            <CardChip card={state.stock[0]?.card} faceUp={false} />
            <p className="text-[10px] text-center text-gray-400 mt-1">Stock ({state.stock.length})</p>
          </div>
          <div>
            <CardChip
              card={state.waste[state.waste.length - 1]?.card}
              faceUp={state.waste.length > 0}
              selected={selected === 'waste'}
              onClick={clickWaste}
            />
            <p className="text-[10px] text-center text-gray-400 mt-1">Waste</p>
          </div>
        </div>
        <div className="flex gap-2">
          {SUITS.map((suit) => (
            <div key={suit}>
              <CardChip
                card={state.foundations[suit][state.foundations[suit].length - 1]}
                faceUp={state.foundations[suit].length > 0}
                onClick={() => clickFoundation(suit)}
              />
              <p className="text-[10px] text-center text-gray-400 mt-1">{suit}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="rounded-xl bg-indigo-50 dark:bg-indigo-950 border border-indigo-200 dark:border-indigo-800 p-2 text-center text-sm text-indigo-800 dark:text-indigo-200">
        {message}
      </div>

      <div className="grid grid-cols-7 gap-2">
        {state.tableau.map((pile, colIndex) => (
          <div key={colIndex} className="space-y-[-52px] flex flex-col items-center">
            {pile.length === 0 && <CardChip small onClick={() => tryTableau(colIndex)} />}
            {pile.map((entry, cardIndex) => (
              <div key={cardIndex} style={{ marginTop: cardIndex === 0 ? 0 : 24 }}>
                <CardChip
                  small
                  card={entry.card}
                  faceUp={entry.faceUp}
                  selected={selected && selected.colIndex === colIndex && cardIndex >= selected.cardIndex}
                  onClick={() => clickTableauCard(colIndex, cardIndex)}
                />
              </div>
            ))}
          </div>
        ))}
      </div>

      <div className="flex justify-center gap-3">
        <button onClick={() => finishGame(`Ended with ${foundationCount()}/52 cards home.`)} className="rounded-full bg-gray-400 hover:bg-gray-500 text-white text-sm font-semibold px-4 py-2">
          Finish &amp; Score
        </button>
        {finished && (
          <button onClick={restart} className="rounded-full bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold px-4 py-2">
            Play Again
          </button>
        )}
      </div>
    </div>
  );
}
