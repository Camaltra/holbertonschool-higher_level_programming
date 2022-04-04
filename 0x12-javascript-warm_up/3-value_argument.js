#!/usr/bin/node

const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('No argument');
} else {
  myArgs.forEach((x, i) => console.log(x));
}
