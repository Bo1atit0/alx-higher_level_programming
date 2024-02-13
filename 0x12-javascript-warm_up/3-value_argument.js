#!/usr/bin/node

const argsLent = process.argv.length - 2;

if (argsLent === 0) {
  console.log('No argument');
} else if (argsLent === 1) {
  console.log(process.argv[2]);
}
