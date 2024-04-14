// Throw an error

export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}

//  Usando el operador ternaria
// export default function divideFunction(numerator, denominator) {
//   return denominator === 0
//     ? (() => {
//         throw new Error('cannot divide by 0');
//       })()
//     : numerator / denominator;
// }
