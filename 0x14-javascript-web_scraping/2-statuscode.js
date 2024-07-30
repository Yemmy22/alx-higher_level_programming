#!/usr/bin/node

const Request = require('request');

if (process.argv.length === 3) {
  Request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    }
    console.log('code: ' + response.statusCode);
  });
}
