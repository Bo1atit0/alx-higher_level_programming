#!/usr/bin/node

exports.logMe = function (item) {
  if (!this.count) {
    this.count = 0;
  } else {
    console.log(`${this.count}: ${item}`);
    this.count++;
  }
};
