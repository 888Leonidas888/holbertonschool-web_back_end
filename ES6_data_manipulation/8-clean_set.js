export default function cleanSet(set, startString) {
  const filteredValues = Array.from(set).filter((value) => value.startsWith(startString));
  return filteredValues
    .map((value) => value.substring(startString.length))
    .join('-');
}
