#!/usr/bin/node
const { argv } = require('node:process');
function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return factorial(n - 1) * n;
}
if (argv.length === 2) {
  const res = factorial(1);
  console.log(res);
} else {
  const arg = Number(argv[2]);
  if (isNaN(arg)) {
    const res = factorial(1);
    console.log(res);
  } else {
    const res = factorial(arg);
    console.log(res);
  }
}
