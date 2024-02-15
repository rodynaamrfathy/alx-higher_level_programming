#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let s = '';
  for (let i = 0; i < x; i++) {
    s += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(s);
  }
}
