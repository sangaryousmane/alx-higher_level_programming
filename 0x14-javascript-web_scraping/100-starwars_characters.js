#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      characters.forEach((characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
