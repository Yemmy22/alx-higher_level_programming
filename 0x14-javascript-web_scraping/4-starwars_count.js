#!/usr/bin/node

const request = require('request');
const ID = '18';

if (process.argv.length === 3) {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }

    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      for (const character of film.characters) {
        if (character.includes(ID)) {
          count++;
        }
      }
    }
    console.log(count);
  });
}
