#!/usr/bin/node

const fs = require('fs');

const pathFile = process.argv[2];

fs.readFile(`./${pathFile}`, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
