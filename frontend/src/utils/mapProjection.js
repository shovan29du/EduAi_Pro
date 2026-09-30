// Shared equirectangular projection helpers for the Countries Explorer's
// schematic locator maps (current-day World Map and the Historical World Map).

export const MAP_WIDTH = 1000;
export const MAP_HEIGHT = 500;

// Real latitude/longitude -> SVG x/y on a MAP_WIDTH x MAP_HEIGHT canvas.
export function project(lat, lng) {
  const x = ((lng + 180) / 360) * MAP_WIDTH;
  const y = ((90 - lat) / 180) * MAP_HEIGHT;
  return { x, y };
}
