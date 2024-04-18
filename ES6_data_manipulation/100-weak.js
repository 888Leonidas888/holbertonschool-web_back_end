// 100-weak.js

// Creamos una instancia de WeakMap
const weakMap = new WeakMap();

// Exportamos la instancia de WeakMap
export { weakMap };

// Definimos la función queryAPI
export function queryAPI(endpoint) {
  // Verificamos si ya hay una cuenta para el endpoint en el WeakMap
  let count = weakMap.get(endpoint) || 0;

  // Incrementamos la cuenta
  count++;

  // Actualizamos el contador en el WeakMap
  weakMap.set(endpoint, count);

  // Si el número de consultas es mayor o igual a 5, lanzamos un error
  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }

  // Retornamos el contador actual
  return count;
}
