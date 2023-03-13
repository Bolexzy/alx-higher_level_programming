#!/usr/bin/node
// Retrieve the command line arguments
const len = process.argv.slice(2).length;
console.log(len === 0 ? 'No argument' : len === 1 ? 'Argument found' : 'Arguments found');
