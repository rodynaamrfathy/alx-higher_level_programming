#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let p = '';
    for (let i = 0; i < this.height; i++) {
      p += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(p);
    }
  }
}

module.exports = Square;
