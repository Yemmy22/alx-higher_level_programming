#!/usr/bin/node

const Request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const episode = process.argv[2];

if (process.argv.length === 3) {
  Request(baseUrl + episode, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const film = JSON.parse(body);
    console.log(film.title);
  });
}
