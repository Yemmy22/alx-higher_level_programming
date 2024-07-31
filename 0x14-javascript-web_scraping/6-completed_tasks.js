#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const temp = {};
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const jsonText = JSON.parse(body);
    for (const task of jsonText) {
      if (task.completed) {
        const key = task.userId;
        if (!temp[key]) {
          temp[key] = 1;
        } else {
          temp[key] += 1;
        }
      }
    }
    console.log(temp);
  });
}
