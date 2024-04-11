// Catch me if you can!

// export default function handleResponseFromAPI(promise) {
//     return new Promise((resolve, reject) => {
//         const result = {
//             status: 200,
//             body: 'success',
//         };
//         if (promise) {
//             console.log('Got a response from the API');
//             resolve(result);
//         } else {
//             console.log('Got a response from the API');
//       reject(new Error());
//     }
// });
// }

export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      const response = {
        status: 200,
        body: 'success',
      };
      return response;
    })
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
