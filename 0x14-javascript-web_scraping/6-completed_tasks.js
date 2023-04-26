#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, resp, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const completed = {};

    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed && completed[todos[i].userId] === undefined) {
        completed[todos[i].userId] = 1;
      } else if (todos[i].completed) {
        completed[todos[i].userId] += 1;
      }
    }

    console.log(completed);
  }
});
