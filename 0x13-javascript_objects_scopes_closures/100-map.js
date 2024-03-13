#!/usr/bin/node
const listobj = require('./100-data');
const list = listobj.list;
const newlst = list.map((num, index) => num * index);
console.log(list);
console.log(newlst);
