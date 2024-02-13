#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (process.argv.length !== 3) {
  console.log('NaN');
} else {
  const arg = parseInt(process.argv[2]);
  const result = factorial(arg);
  console.log(result);
}
