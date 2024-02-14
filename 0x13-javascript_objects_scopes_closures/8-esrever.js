#!/usr/bin/node

exports.esrever = function (list) {
  const reverselist = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reverselist[j] = list[i];
    j++;
  }
  return reverselist;
};
