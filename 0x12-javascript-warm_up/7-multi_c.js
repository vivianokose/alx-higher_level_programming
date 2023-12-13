#!/usr/bin/node
let firstArg = process.argv[2];
if (!firstArg || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  firstArg = parseInt(firstArg);
  for (let k = 0; k < firstArg; k++) {
    console.log('C is fun');
  }
}
