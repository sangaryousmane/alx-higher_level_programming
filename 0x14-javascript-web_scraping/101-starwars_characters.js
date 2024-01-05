#!/usr/bin/node

const request = require('request');
const movieEndPoint = `https://swapi.dev/api/films/${parseInt(process.argv[2], 10)}/`;

request(movieEndPoint, (err, response, body) => {
  if (!err) {
    try {
      const data = JSON.parse(body);
      const characters = data.characters;

      characters.forEach((url) => {
        request.get(url, (urlErr, res, body) => {
          if (!urlErr) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    } catch (error) {
      console.log(`Can't process url: ${movieEndPoint}`);
    }
  }
});
