#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
let count = 0;

request(process.argv[2], (err, resp, body) => {
  if (!err) {
    const response = JSON.parse(body).results;

    for (let i = 0; i < response.length; i++) {
      const characters = response[i].characters;
      count = characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }
    console.log(count);
  }
});
