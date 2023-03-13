#!/usr/bin/node
const arg2 = parseInt(process.argv[2], 10);
console.log(isNaN(arg2) ? 'Not a number' : `My number: ${arg2}`);
