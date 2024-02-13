#!/usr/bin/node

if (process.argv.length === 2 || parseInt(process.argv.length) === 3) {
  console.log(0);
} else {
  let i;
  let largest = parseInt(process.argv[2]);
  let secondLargest = parseInt(process.argv[process.argv.length - 1]);

  for (i = 1; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > largest) {
      secondLargest = largest;
      largest = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > secondLargest && parseInt(process.argv[i] !== largest)) {
      secondLargest = parseInt(process.argv[i]);
    }
  }
  console.log(secondLargest);
}
