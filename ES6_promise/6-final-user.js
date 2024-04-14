// Handle multiple promises
// import signUser from './4-user-promise';
// import uploadPhoto from './5-photo-reject';

// export default function handleProfileSignup(firstName, lastName, fileName) {
//   return Promise.allSettled([
//     signUser(firstName, lastName),
//     uploadPhoto(fileName),
//   ]).then((r) => r);
// }

// 6-final-user.js
import signUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => {
    return results.map((result) => {
      if (result.status === 'fulfilled') {
        return {
          status: result.status,
          value: result.value,
        };
      } else {
        return {
          status: result.status,
          value: `Error: ${result.reason.message}`,
        };
      }
    });
  });
}
