export default function cleanSet(set, startString) {
  let txt = '';
  const filteredValues = Array.from(set).filter((value) => value.startsWith(startString));
  if (startString !== '') {
    txt = filteredValues
      .map((value) => value.substring(startString.length))
      .join('-');
  }
  return txt;
}
