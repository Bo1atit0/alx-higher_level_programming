#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
