#!/usr/bin/node
const list = require('./100-data');

console.log(list);
list.map((v, index) => (v * index));
console.log(list)
module.exports = list;
