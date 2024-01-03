#!/usr/bin/node

const request = require('request');

const url = `${process.argv[2]}`;

request.get(url, (err, response, body) => {
  if (err) { console.log(err); } else {
    try {
      const data = JSON.parse(body);
      let wedgeCount = 0;
      const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
      data.results.forEach((film) => {
        if (film.characters.includes(wedge)) {
          wedgeCount++;
        }
      });
      console.log(wedgeCount);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
