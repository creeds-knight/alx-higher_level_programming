#!/usr/bin/node
exports.esrever = function (list) {
  let left = 0;
  let right = list.length - 1;
  while (left < right) {
    const tmp = list[left];
    list[left] = list[right];
    list[right] = tmp;
    left++;
    right--;
  }
  return list;
};
