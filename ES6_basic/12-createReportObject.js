// Let's create a report object

export default function createReportObject(employeesList) {
  const allEmployees = {};
  for (const departament in employeesList) {
    allEmployees[departament] = employeesList[departament];
  }
  const newObj = {
    allEmployees,
    getNumberOfDepartments(n) {
      return Object.keys(n).length;
    },
  };
  return newObj;
}
