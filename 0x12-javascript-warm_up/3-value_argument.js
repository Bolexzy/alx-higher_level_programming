#!/usr/bin/node
const arg1 = process.argv.slice(2)[0];
console.log(arg1 == null ? 'No argument' : arg1);
