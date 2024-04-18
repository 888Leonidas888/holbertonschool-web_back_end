// More map data structure

export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  map.forEach((v, k) => (v === 1 ? map.set(k, 100) : null));
}
