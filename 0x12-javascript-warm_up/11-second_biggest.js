#!/usr/bin/node
const { argv } = require('node:process');
let max = 0;
let secMax = 0;
for (let i = 0; i < argv.length; i++) {
  const num = Number(argv[i]);
  if (num > max) {
    secMax = max;
    max = num;
  }
}
console.log(secMax);
