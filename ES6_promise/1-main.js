import getFullResponseFromAPI from './1-promise';

console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));

// getFullResponseFromAPI(false)
//   .then((r) => {
//     console.log(r);
//   })
//   .catch((err) => {
//     console.log(err.message);
//   });
