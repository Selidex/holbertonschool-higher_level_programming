#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let x = 0;
    if (typeof c === 'undefined') { c = 'X'; }
    for (x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
