#!/usr/bin/node

const arrayArg = process.argv.slice(2);

let secondMax = 0;
if (arrayArg.length > 1) {
  arrayArg.sort();
  secondMax = arrayArg[arrayArg.length - 2];
}
console.log(secondMax);
