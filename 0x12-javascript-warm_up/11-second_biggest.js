#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let i;
  let largest = parseInt(process.argv[2]);
  let secondLargest = parseInt(process.argv[process.argv.length - 1]);

  for (i = 1; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}
