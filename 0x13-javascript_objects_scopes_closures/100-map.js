#!/usr/bin/node
const list = require('./100-data');

console.log(list);
list.map((v) => (v * list[v]));

module.exports = list;
