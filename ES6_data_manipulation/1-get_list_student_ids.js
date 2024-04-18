// export default function getListStudentIds(listStudents) {
//     if (Array.isArray(listStudents)) {
//         return listStudents.map((student) => student.id);
//     } else {
//         return [];
//     }
// }

export default function getListStudentIds(listStudents) {
  return Array.isArray(listStudents)
    ? listStudents.map((student) => student.id)
    : [];
}
