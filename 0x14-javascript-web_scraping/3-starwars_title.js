#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, response, body) => {

	if (err)
		console.log(err);
	else {
		try {
			const movies = JSON.parse(body);
			console.log(`${movies.title}`)
		} catch(parsedError) {
			console.log(parsedError);
		}
	}
});
