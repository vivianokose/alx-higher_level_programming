#!/usr/bin/node
function add (i, j) {
  console.log(i + j);
}

let firstArg = process.argv[2];
let secondArg = process.argv[3];

firstArg = parseInt(firstArg);
secondArg = parseInt(secondArg);

add(firstArg, secondArg);
