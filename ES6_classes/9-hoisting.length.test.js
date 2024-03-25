// import { listOfStudents } from './9-hoisting.js';

// console.log(listOfStudents);

// const listPrinted = listOfStudents.map(
//   (student) => student.fullStudentDescription
// );

// console.log(listPrinted);

// test #1
import listOfStudents from './9-hoisting.js';

test('listOfStudents has the correct length', () => {
  expect(listOfStudents.length).toBe(5);
});
