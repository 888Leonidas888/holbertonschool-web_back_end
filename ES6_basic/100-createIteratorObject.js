// Iterating through report objects

export default function createIteratorObject(report) {
  const newArray = [];
  Object.values(report.allEmployees).forEach((departament) => {
    newArray.push(...departament);
  });
  return newArray;
}
