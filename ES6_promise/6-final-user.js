// Handle multiple promises
// import signUser from './4-user-promise';
// import uploadPhoto from './5-photo-reject';

// export default function handleProfileSignup(firstName, lastName, fileName) {
//   return Promise.allSettled([
//     signUser(firstName, lastName),
//     uploadPhoto(fileName),
//   ]).then((r) => r);
// }

import signUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => results.map((result) => (
    result.status === 'fulfilled'
      ? { status: result.status, value: result.value }
      : { status: result.status, value: `Error: ${result.reason.message}` }
  )));
}
