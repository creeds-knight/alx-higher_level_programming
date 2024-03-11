#!/usr/bin/node
const { argv } = require('node:process');
function add (a, b) {
  return a + b;
}
const m = Number(argv[2]);
const n = Number(argv[3]);
const res = add(m, n);
console.log(res);
