#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2];

if (process.argv.length === 3) {
  request(url + ID, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.error(error);
        }
        console.log(JSON.parse(body).name);
      });
    }
  });
}
