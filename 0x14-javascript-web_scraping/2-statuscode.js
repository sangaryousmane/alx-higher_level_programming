#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) { console.log('Error: ', err); } else { console.log('code: ', response.statusCode); }
});
