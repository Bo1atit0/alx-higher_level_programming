#!/usr/bin/node

const sQuare = require('./5-square');

class Square extends sQuare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i;
      const row = 'C'.repeat(this.width);

      for (i = 0; i < this.width; i++) {
        console.log(row);
      }
    }
  }
}
module.exports = Square;
