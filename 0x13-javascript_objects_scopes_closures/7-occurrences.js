#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    count += list[i] === searchElement ? 1 : 0;
  }
  return count;
};
