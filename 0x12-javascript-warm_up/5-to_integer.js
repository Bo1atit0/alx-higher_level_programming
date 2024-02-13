#!/usr/bin/node

const firstArg = process.argv[2];

if (firstArg === undefined) {
  console.log('Not a Number');
} else if (isNaN(firstArg)) {
  console.log('Not a Number');
} else {
  const intArg = parseInt(firstArg);
  console.log('My Number:', intArg);
}
