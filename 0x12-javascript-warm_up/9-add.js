#!/usr/bin/node

function add (a, b) {
  const result = a + b;

  return result;
}

if (isNaN(process.argv[2])) {
  console.log('NaN');
} else if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  const sum = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
  console.log(sum);
}
