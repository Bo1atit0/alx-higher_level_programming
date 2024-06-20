#!/usr/bin/node

const { list } = require('./100-data.js');

const newValue = list.map(function (x, index) {
  return x * index;
});
console.log(list);
console.log(newValue);
