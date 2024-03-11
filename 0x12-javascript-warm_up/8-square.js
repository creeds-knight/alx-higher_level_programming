#!/usr/bin/node
const { argv } = require('node:process');
const arg = Number(argv[2]);
if (argv.length === 3 && arg) {
  for (let i = 0; i < arg; i++) {
    let line = '';
    for (let m = 0; m < arg; m++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
