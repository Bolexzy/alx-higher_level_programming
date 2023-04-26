#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi.dev/api/films/${filmId}/`;

function printCharacter (characters, pos) {
  request(characters[pos], (err, resp, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (pos < characters.length - 1) {
        printCharacter(characters, pos + 1);
      }
    }
  });
}

request(url, (err, resp, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacter(characters, 0);
  }
});
