// Filter

export default function getStudentsByLocation(listStudents, location) {
  let tempArray = '';
  if (Array.isArray(listStudents) && typeof location === 'string') {
    tempArray = listStudents.filter((student) => student.location === location);
  }
  return tempArray;
}
