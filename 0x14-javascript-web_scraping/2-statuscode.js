#!/usr/bin/node

const Request = require('request')

if (process.argv.length === 3) {
	response = new Request(process.argv[2], (error, response, body) => {
		console.log('code: ' + response.statusCode);
	});
};
