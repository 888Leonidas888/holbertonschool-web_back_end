// Simple promise

// Forma corta
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}

// Forma larga
// export default function signUpUser(firstName, lastName) {
//   return new Promise((resolve) => {
//     const data = {
//       firstName,
//       lastName,
//     };
//     resolve(data);
//   });
// }
