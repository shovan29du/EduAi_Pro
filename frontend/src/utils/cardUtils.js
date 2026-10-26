// Shared standard 52-card deck helpers for War, Go Fish, and Solitaire.

export const SUITS = ['♠', '♥', '♦', '♣'];
export const RED_SUITS = new Set(['♥', '♦']);
export const RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

// War/high-card ordering: Ace is high.
export function rankValue(rank) {
  if (rank === 'A') return 14;
  if (rank === 'K') return 13;
  if (rank === 'Q') return 12;
  if (rank === 'J') return 11;
  return parseInt(rank, 10);
}

export function buildDeck() {
  const deck = [];
  for (const suit of SUITS) {
    for (const rank of RANKS) {
      deck.push({ id: `${rank}${suit}`, rank, suit, red: RED_SUITS.has(suit) });
    }
  }
  return deck;
}

export function cardLabel(card) {
  return `${card.rank}${card.suit}`;
}
