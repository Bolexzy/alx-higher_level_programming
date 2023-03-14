#!/usr/bin/node
const arg2 = parseInt(process.argv[2], 10);
if (isNaN(arg2)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg2; i++) {
    let row = '';
    for (let j = 0; j < arg2; j++) row += 'X';
    console.log(row);
  }
}
