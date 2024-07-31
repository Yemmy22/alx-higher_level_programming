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
    const orderedCharacters = [];
    characters.forEach((character, index) => {
      request(character, (error, response, body) => {
        if (error) {
          console.error(error);
        }
        const data = JSON.parse(body).name;
        orderedCharacters[index] = data;
        if (orderedCharacters.filter(name => name !== undefined).length === characters.length) {
          orderedCharacters.forEach(name => {
            console.log(name);
          });
        }
      });
    });
  });
}
