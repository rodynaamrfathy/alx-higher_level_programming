#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2]) || Number(process.argv[2]) === 1) {
  console.log(0);
} else {
  let max = 0;

  // Find the max value in the arguments
  for (let i = 2; i < process.argv.length; i++) {
    if (Number(process.argv[i]) > max) {
      max = Number(process.argv[i]);
    }
  }

  let newlist = [];
  let j = 0;

  // Fill newlist without the max value
  for (let i = 2; i < process.argv.length; i++) {
    if (Number(process.argv[i]) !== max) {
      newlist[j] = Number(process.argv[i]);
      j++;
    }
  }

  max = 0;

  // Find the second largest value in newlist
  for (let i = 0; i < newlist.length; i++) {
    if (max < newlist[i]) {
      max = newlist[i];
    }
  }

  console.log(max);
}
