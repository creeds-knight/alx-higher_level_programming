#!/usr/bin/node
// A script that reads and prints content of a file

const fs = require('node:fs');

const args = process.argv;

const filePath = args[2];

if (!filePath) {
  console.log('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

fs.readfile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
