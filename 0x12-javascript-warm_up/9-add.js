#!/usr/bin/node
function add (a, b) {
  if (a === undefined || b === undefined || isNaN(a) || isNaN(b)) {
    return 'NaN';
  }
  return Number(a) + Number(b);
}
console.log(add(process.argv[2], process.argv[3]));
