#!/usr/bin/node

const { dict } = require('./101-data.js');

const computeDict = {};
for (const n in dict) {
  if (computeDict[dict[n]] === undefined) { computeDict[dict[n]] = []; }
  computeDict[dict[n]].push(n);
}
console.log(computeDict);
