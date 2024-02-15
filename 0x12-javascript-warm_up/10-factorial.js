#!/usr/bin/node
function factorial (num) {
  if (num < 0) {
    return (-1);
  }
  if (num === 1 || num === 0 || num === undefined || isNaN(num)) {
    return 1;
  }
  return factorial(Number(num) - 1) * Number(num);
}
console.log(factorial(process.argv[2]));
