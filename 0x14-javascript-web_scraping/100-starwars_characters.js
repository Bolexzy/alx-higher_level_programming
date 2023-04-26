#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi.dev/api/films/${filmId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
