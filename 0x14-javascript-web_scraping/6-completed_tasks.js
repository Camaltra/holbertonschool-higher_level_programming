#!/usr/bin/node

const axios = require('axios');

const API_URL = process.argv[2];

async function getAllDoneTaskById (API_URL) {
  const finalList = {};
  let val;
  await axios.get(API_URL)
    .then((res) => {
      for ([, val] of Object.entries(res.data)) {
        if (val.completed === true) {
          if (finalList[val.userId] === undefined) {
            finalList[val.userId] = 0;
          }
          finalList[val.userId] += 1;
        }
      }
      console.log(finalList);
    })
    .catch((err) => {
      console.error(err);
    });
}

getAllDoneTaskById(API_URL);
