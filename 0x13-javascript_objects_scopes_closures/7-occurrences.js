#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const obj = {};
  for (const element of list) {
    if (obj[element]) {
      obj[element]++;
    } else {
      obj[element] = 1;
    }
  }
  if (obj[searchElement]) {
    return obj[searchElement];
  } else {
    return 0;
  }
};
