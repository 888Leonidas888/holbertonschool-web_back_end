// Basic list of objects

export default function getListStudents() {
  return [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
}

// class Student {
//   constructor(id, firstName, location) {
//     this.id = id;
//     this.firstName = firstName;
//     this.location = location;
//   }
// }

// export default function getListStudents() {
//   return [
//     new Student(1, 'Guillaume', 'San Francisco'),
//     new Student(2, 'James', 'Columbia'),
//     new Student(5, 'Serena', 'San Francisco'),
//   ];
// }
