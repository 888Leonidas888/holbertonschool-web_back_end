import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
console.log(building.sqft);
console.log(building.floors);
console.log(building.evacuationWarningMessage());
// import SkyHighBuilding from './6-sky_high.js';

// test("SkyHighBuilding is implemented correctly", () => {
//     const building = new SkyHighBuilding(200, 65);
  
//     expect(building.sqft).toBe(200);
//     expect(building.floors).toBe(65);
  
//     expect(typeof building.evacuationWarningMessage).toBe("function");
//     expect(building.evacuationWarningMessage()).toBe("Evacuate slowly the 65 floors");
// });