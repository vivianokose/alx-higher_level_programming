#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // extract arguments and convert to Number

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  let biggest = args[0];
  let secondBiggest = args[1];

  if (secondBiggest > biggest) {
    [biggest, secondBiggest] = [secondBiggest, biggest];
  }

  for (let i = 2; i < args.length; i++) {
    const num = args[i];

    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num !== biggest) {
      secondBiggest = num;
    }
  }

  console.log(secondBiggest);
}

