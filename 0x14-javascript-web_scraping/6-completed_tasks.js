#!/usr/bin/node

const axios = require('axios');

const API_URL = process.argv[2];

async function getAllDoneTaskById (API_URL) {
  const finalList = {};
  let userId = 1;
  let finishedTask = 0;
  await axios.get(API_URL)
    .then((res) => {
      if (res.status === 200) {
        for (const task of res.data) {
          if (userId !== task.userId) {
            finalList[String(userId)] = finishedTask;
            userId++;
            finishedTask = 0;
          }
          if (task.completed) {
            finishedTask++;
          }
        }
        finalList[String(userId)] = finishedTask;
      }
      console.log(finalList);
    })
    .catch((err) => {
      console.error(err);
    });
}

getAllDoneTaskById(API_URL);
