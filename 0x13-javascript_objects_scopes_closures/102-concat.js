#!/usr/bin/node
// Take and concat two files to an existing one
const args = process.argv.slice(2);
const fs = require("fs");
const first = fs.readFileSync('./' + args[0]);
const second = fs.readFileSync('./' + args[1]);
console.log(fs.writeFileSync('./' + args[2], first + second));

