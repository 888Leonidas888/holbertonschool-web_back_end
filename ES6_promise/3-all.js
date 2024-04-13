// Handle multiple successful promises

import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([responsePhoto, responseUser]) => {
      console.log(
        responsePhoto.body,
        responseUser.firstName,
        responseUser.lastName
      );
    })
    .catch((error) => {
      console.log('Signup system offline');
    });
}
