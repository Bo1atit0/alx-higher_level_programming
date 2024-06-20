#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i;
    const row = 'X'.repeat(this.width);

    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
