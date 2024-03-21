// class HolbertonCourse

export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateString(name);
    this._length = this._validateNumber(length);
    this._students = this._validateArray(students);
  }

  get name() {
    return this._name;
  }

  set name(name) {
    this._name = name;
  }

  get length() {
    return this._length;
  }

  set length(length) {
    this._length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    this._students = students;
  }

  _validateString(value) {
    if (typeof value !== "string") {
      throw new TypeError("Name must be a string");
    }
    return value;
  }

  _validateNumber(value) {
    if (typeof value !== "number") {
      throw new TypeError("Length must be a number");
    }

    return value;
  }

  _validateArray(value) {
    if (!Array.isArray(value)) {
      throw new TypeError("Students must be a array");
    }

    return value;
  }
}
