// Full literal Tailwind class strings (not interpolated) so the JIT
// compiler's content scanner picks every one of them up at build time.
const TAB_COLOR_THEMES = [
  { active: 'bg-rose-600 border-rose-600 text-white', inactive: 'border-rose-300 bg-rose-50 text-rose-700 dark:border-rose-700 dark:bg-rose-950 dark:text-rose-300' },
  { active: 'bg-orange-600 border-orange-600 text-white', inactive: 'border-orange-300 bg-orange-50 text-orange-700 dark:border-orange-700 dark:bg-orange-950 dark:text-orange-300' },
  { active: 'bg-amber-600 border-amber-600 text-white', inactive: 'border-amber-300 bg-amber-50 text-amber-700 dark:border-amber-700 dark:bg-amber-950 dark:text-amber-300' },
  { active: 'bg-lime-600 border-lime-600 text-white', inactive: 'border-lime-300 bg-lime-50 text-lime-700 dark:border-lime-700 dark:bg-lime-950 dark:text-lime-300' },
  { active: 'bg-emerald-600 border-emerald-600 text-white', inactive: 'border-emerald-300 bg-emerald-50 text-emerald-700 dark:border-emerald-700 dark:bg-emerald-950 dark:text-emerald-300' },
  { active: 'bg-teal-600 border-teal-600 text-white', inactive: 'border-teal-300 bg-teal-50 text-teal-700 dark:border-teal-700 dark:bg-teal-950 dark:text-teal-300' },
  { active: 'bg-cyan-600 border-cyan-600 text-white', inactive: 'border-cyan-300 bg-cyan-50 text-cyan-700 dark:border-cyan-700 dark:bg-cyan-950 dark:text-cyan-300' },
  { active: 'bg-sky-600 border-sky-600 text-white', inactive: 'border-sky-300 bg-sky-50 text-sky-700 dark:border-sky-700 dark:bg-sky-950 dark:text-sky-300' },
  { active: 'bg-blue-600 border-blue-600 text-white', inactive: 'border-blue-300 bg-blue-50 text-blue-700 dark:border-blue-700 dark:bg-blue-950 dark:text-blue-300' },
  { active: 'bg-indigo-600 border-indigo-600 text-white', inactive: 'border-indigo-300 bg-indigo-50 text-indigo-700 dark:border-indigo-700 dark:bg-indigo-950 dark:text-indigo-300' },
  { active: 'bg-violet-600 border-violet-600 text-white', inactive: 'border-violet-300 bg-violet-50 text-violet-700 dark:border-violet-700 dark:bg-violet-950 dark:text-violet-300' },
  { active: 'bg-fuchsia-600 border-fuchsia-600 text-white', inactive: 'border-fuchsia-300 bg-fuchsia-50 text-fuchsia-700 dark:border-fuchsia-700 dark:bg-fuchsia-950 dark:text-fuchsia-300' },
  { active: 'bg-pink-600 border-pink-600 text-white', inactive: 'border-pink-300 bg-pink-50 text-pink-700 dark:border-pink-700 dark:bg-pink-950 dark:text-pink-300' },
  { active: 'bg-red-600 border-red-600 text-white', inactive: 'border-red-300 bg-red-50 text-red-700 dark:border-red-700 dark:bg-red-950 dark:text-red-300' },
];

function hashString(value) {
  let hash = 0;
  for (let i = 0; i < value.length; i += 1) {
    hash = (hash * 31 + value.charCodeAt(i)) >>> 0;
  }
  return hash;
}

/** Deterministic color theme per tab name, so a given tab (e.g. "Library")
 * always gets the same color regardless of which tab list/role renders it. */
export function tabColorTheme(tabName) {
  const index = hashString(tabName) % TAB_COLOR_THEMES.length;
  return TAB_COLOR_THEMES[index];
}

const TAB_ICONS = {
  Dashboard: '📊',
  Subjects: '🎓',
  Library: '📖',
  Search: '🔍',
  Favourites: '⭐',
  'Ark AI Tutor': '🤖',
  Languages: '🗣️',
  Grammar: '✍️',
  Vocabulary: '🔤',
  'STEM Lab': '🔬',
  'Non-Fiction': '📰',
  'Practical Skills': '🛠️',
  Museum: '🏛️',
  'World Lit': '📚',
  Biographies: '🧑‍🎓',
  'Survival Skills': '🏕️',
  'Other Subjects': '🧩',
  'Sports Centre': '🏅',
  'Cuisine Centre': '🍽️',
  Tools: '🧮',
  Countries: '🌍',
  Assessment: '📝',
  Colouring: '🎨',
  'Code Editor': '💻',
  'Music & Instruments': '🎵',
  Karaoke: '🎤',
  'World Cinema': '🎬',
  Games: '🎮',
  Chess: '♟️',
  'Study Coach': '🧭',
  Appearance: '🖌️',
  'Resource Tab': '🗂️',
  Users: '👤',
};

const DEFAULT_TAB_ICON = '✨';

/** Small visual identity per tab (Google Arts & Culture-style category
 * chips); falls back to a generic sparkle for any tab not explicitly
 * mapped so a new/renamed tab never renders blank. */
export function tabIcon(tabName) {
  return TAB_ICONS[tabName] || DEFAULT_TAB_ICON;
}
