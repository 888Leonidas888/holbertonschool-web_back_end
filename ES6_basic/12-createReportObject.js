// Let's create a report object

export default function createReportObject(employeesList) {
  const allEmployees = {};
  Object.keys(employeesList).forEach((departament) => {
    allEmployees[departament] = employeesList[departament];
  });
  const newObj = {
    allEmployees,
    getNumberOfDepartments(n) {
      return Object.keys(n).length;
    },
  };
  return newObj;
}
