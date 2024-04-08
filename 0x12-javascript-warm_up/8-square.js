#!/usr/bin/node

let i, j;
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    let square = '';
    for (j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
