#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  for (let i = 0; i < (list.length) / 2; i++) {
    temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }
  return list;
};
