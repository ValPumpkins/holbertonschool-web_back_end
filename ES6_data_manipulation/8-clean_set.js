export default function cleanSet(set, startString) {
  const string = [];

  if (
    typeof set !== 'object'
    || typeof startString !== 'string'
    || startString.length === 0
  ) {
    return '';
  }

  for (const value of set) {
    if (value && value.startsWith(startString)) {
      string.push(value.slice(startString.length));
    }
  }

  return string.join('-');
}
