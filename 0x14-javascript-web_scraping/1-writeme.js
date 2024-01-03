#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

try {
  fs.writeFileSync(filePath, process.argv[3], 'utf-8');
} catch (error) {
  console.log(error);
}
