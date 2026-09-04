// A standard 108-card Uno deck: 4 colours x (one 0, two each of 1-9, two
// Skip, two Reverse, two Draw Two) + 4 Wild + 4 Wild Draw Four.

export const COLORS = ['red', 'yellow', 'green', 'blue'];
export const COLOR_CLASSES = {
  red: 'bg-red-500 text-white',
  yellow: 'bg-yellow-400 text-yellow-900',
  green: 'bg-green-600 text-white',
  blue: 'bg-blue-600 text-white',
  wild: 'bg-gray-900 text-white',
};

let uid = 0;
function nextId() {
  uid += 1;
  return `uno-${uid}`;
}

export function buildUnoDeck() {
  const deck = [];
  for (const color of COLORS) {
    deck.push({ id: nextId(), color, kind: 'number', value: 0 });
    for (let v = 1; v <= 9; v++) {
      deck.push({ id: nextId(), color, kind: 'number', value: v });
      deck.push({ id: nextId(), color, kind: 'number', value: v });
    }
    for (let i = 0; i < 2; i++) {
      deck.push({ id: nextId(), color, kind: 'skip' });
      deck.push({ id: nextId(), color, kind: 'reverse' });
      deck.push({ id: nextId(), color, kind: 'drawTwo' });
    }
  }
  for (let i = 0; i < 4; i++) {
    deck.push({ id: nextId(), color: 'wild', kind: 'wild' });
    deck.push({ id: nextId(), color: 'wild', kind: 'wildDrawFour' });
  }
  return deck;
}

export function cardLabel(card) {
  if (card.kind === 'number') return String(card.value);
  if (card.kind === 'skip') return '🚫';
  if (card.kind === 'reverse') return '🔄';
  if (card.kind === 'drawTwo') return '+2';
  if (card.kind === 'wild') return 'W';
  if (card.kind === 'wildDrawFour') return '+4';
  return '?';
}

export function canPlay(card, topCard, activeColor) {
  if (card.color === 'wild') return true;
  if (card.color === activeColor) return true;
  if (card.kind === 'number' && topCard.kind === 'number') return card.value === topCard.value;
  return card.kind !== 'number' && card.kind === topCard.kind;
}
