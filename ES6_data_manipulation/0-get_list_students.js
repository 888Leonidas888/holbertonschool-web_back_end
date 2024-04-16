// Basic list of objects

export default function getListStudents() {
  const listPerson = [];
  const person1 = new Person(1, 'Guillaume', 'San Francisco');
  const person2 = new Person(2, 'James', 'Columbia');
  const person3 = new Person(5, 'Serena', 'San Francisco');

  listPerson.push(person1);
  listPerson.push(person2);
  listPerson.push(person3);

  return listPerson;
}

function Person(id, firstName, location) {
  this.id = id;
  this.firstName = firstName;
  this.location = location;
}
