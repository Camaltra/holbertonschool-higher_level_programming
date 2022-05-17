#!/usr/bin/node

const fs = require('fs');

const pathFile = process.argv[2];
const content = process.argv[3];

fs.writeFile(`./${pathFile}`, content, { flag: 'w+' }, err => {
  if (err) {
    console.error(err);
  }
});
