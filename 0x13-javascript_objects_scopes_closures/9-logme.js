#!/usr/bin/node
let noprinted = 0;

exports.logMe = function (item) {
  console.log(noprinted + ': ' + item);
  noprinted++;
};
