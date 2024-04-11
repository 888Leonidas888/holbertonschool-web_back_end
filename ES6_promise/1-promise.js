// Don't make a promise...if you know you can't keep it

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      const result = {
        status: 200,
        body: 'Success',
      };
      resolve(result);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
