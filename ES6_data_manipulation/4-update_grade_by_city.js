// Combine

// export default function updateStudentGradeByCity(
//   listStudents,
//   location,
//   newGrades,
// ) {
//   if (Array.isArray(listStudents) && typeof location === 'string' && Array.isArray(newGrades)) {
//     return listStudents
//       .filter((student) => student.location === location)
//       .map((student) => {
//         student.grade = 'N/A';
//         for (let i = 0; i < newGrades.length; ++i) {
//           if (newGrades[i].studentId === student.id) {
//             student.grade = newGrades[i].grade;
//           }
//         }
//         return student;
//       });
//   }
// }

export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  // Verificar que los parámetros sean válidos
  if (!Array.isArray(listStudents) || typeof city !== 'string' || !Array.isArray(newGrades)) {
    throw new Error('Los parámetros no son válidos.');
  }

  // Filtrar estudiantes por ciudad y actualizar calificaciones
  return listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
      const grade = matchingGrade ? matchingGrade.grade : 'N/A';
      return { ...student, grade };
    });
}
