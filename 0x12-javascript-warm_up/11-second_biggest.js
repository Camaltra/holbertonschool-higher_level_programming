#!/usr/bin/node

const arrayArg = process.argv.slice(2);

if (arrayArg.length <= 1) {
  console.log('0');
} else {
  arrayArg.sort();
  console.log(arrayArg[arrayArg.length - 2]);
}
