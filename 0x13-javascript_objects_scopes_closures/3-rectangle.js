#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = 0;
    const s = 'X';
    for (x = 0; x < this.height; x++) {
      console.log(s.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
