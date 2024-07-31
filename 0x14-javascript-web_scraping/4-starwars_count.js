#!/usr/bin/node

const request = require('request');
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/';
const ID = 18;

if (process.argv.length === 3) {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }

    const results = JSON.parse(body).results;
    let count = 0;
    for (const i of results) {
      for (const j of i.characters) {
        if (j === characterUrl + ID + '/') {
          count++;
        }
      }
    }
    console.log(count);
  });
}
