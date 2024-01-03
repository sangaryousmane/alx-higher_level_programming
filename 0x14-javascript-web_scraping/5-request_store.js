#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const filePath = process.argv[3];

request.get(process.argv[2], (err, response, body) => {
  if (err) { console.log(err); } else {
    try {
      fs.writeFileSync(filePath, body, 'utf-8', (error) => {
        if (error) { console.log(error); }
      });
    } catch (error) {
      console.log(error);
    }
  }
});
