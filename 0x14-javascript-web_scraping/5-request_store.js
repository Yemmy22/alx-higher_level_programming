#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length === 4) {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }
    console.log(body);
    fs.writeFile(process.argv[3], body, { encoding: 'utf8' }, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
}
