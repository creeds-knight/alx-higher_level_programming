#!/usr/bin/node
const { argv } = require('node:process');
function isInt (n) {
  return (Number(n) === n && n % 1 === 0);
}
function isFloat (n) {
  return (Number(n) === n && n % 1 !== 0);
}
if (argv.length !== 3) {
  console.log('Not a number');
} else {
  const arg = Number(argv[2]);
  if (isNaN(arg)) {
    console.log('Not a number');
  } else if (isInt(arg)) {
    console.log('My number: ' + arg);
  } else if (isFloat(arg)) {
    console.log('My number: ' + arg);
  } else {
    console.log('Not a number');
  }
}
