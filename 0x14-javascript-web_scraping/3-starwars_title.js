#!/usr/bin/node
// https://swapi-api.alx-tools.com/api/films/:id
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  console.log(err || JSON.parse(body).title);
});
