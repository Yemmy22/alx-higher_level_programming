#!/usr/bin/node

let fs = require('fs')
const filepath = process.argv[2]
let string = process.argv[3]

if (process.argv.length === 4) {
	fs.writeFile(filepath, string, encoding='utf8', function (err, fd) {
		if (err) {
			console.error(err);
		};

	});
};
