// Iterating through report objects

export default function createIteratorObject(report) {
  var newArray = [];
  Object.values(report.allEmployees).forEach((departament) => {
    newArray.push(...departament);
  });
  return newArray;
}
