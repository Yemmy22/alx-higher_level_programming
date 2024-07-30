#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const string = process.argv[3];

if (process.argv.length === 4) {
  fs.writeFile(filepath, string, { encoding: 'utf8' }, function (err) {
    if (err) {
      console.error(err);
    }
  });
}
