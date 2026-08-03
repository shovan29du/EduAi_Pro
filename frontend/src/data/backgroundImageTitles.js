// Wikipedia article titles resolved at runtime (via the existing
// /api/museum/thumbnail proxy) into real, currently-valid thumbnail URLs --
// deliberately not hardcoded image URLs, which would go stale. 60 images
// across 8 categories: space, nature, famous painting (curated to exclude
// nudity), ocean, science, fantasy, abstract, famous natural attraction.
export const BACKGROUND_IMAGE_TITLES = [
  // Space (8)
  'Earthrise',
  'Pillars of Creation',
  'Pale Blue Dot',
  'Crab Nebula',
  'Andromeda Galaxy',
  'Whirlpool Galaxy',
  'Horsehead Nebula',
  'Saturn',
  // Nature (7)
  'Aurora',
  'Amazon rainforest',
  'Sahara',
  'Rainforest',
  'Old-growth forest',
  'Tundra',
  'Bioluminescence',
  // Famous art (8, no nudity)
  'The Starry Night',
  'The Great Wave off Kanagawa',
  'Water Lilies (Monet series)',
  'Sunflowers (Van Gogh series)',
  'The Persistence of Memory',
  'Girl with a Pearl Earring',
  'American Gothic',
  'Mona Lisa',
  // Ocean (7)
  'Great Barrier Reef',
  'Pacific Ocean',
  'Coral reef',
  'Blue hole',
  'Mariana Trench',
  'Deep sea',
  'Bora Bora',
  // Science (7)
  'DNA',
  'International Space Station',
  'Large Hadron Collider',
  'Periodic table',
  'Human brain',
  'Neuron',
  'Electron microscope',
  // Fantasy (8)
  'Dragon',
  'Unicorn',
  'Fairy tale',
  'Castle',
  'Phoenix (mythology)',
  'Mermaid',
  'Elf',
  'Wizard',
  // Abstract (7)
  'Abstract art',
  'Wassily Kandinsky',
  'Piet Mondrian',
  'Jackson Pollock',
  'Composition VIII',
  'Black Square (painting)',
  'Broadway Boogie Woogie',
  // Famous natural attraction (8)
  'Grand Canyon',
  'Yosemite Valley',
  'Mount Everest',
  'Victoria Falls',
  'Niagara Falls',
  'Ha Long Bay',
  'Zhangjiajie National Forest Park',
  'Antelope Canyon',
];
