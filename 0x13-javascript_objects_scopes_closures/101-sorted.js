#!/usr/bin/node
const objDct = require('./101-data');
const nums = objDct.dict;
const objGroup = Object.entries(nums).reduce((acc, [userid, occurance]) => {
  if (!acc[occurance]) {
    acc[occurance] = [];
  }
  acc[occurance].push(userid);
  return acc;
}, {});
console.log(objGroup);
