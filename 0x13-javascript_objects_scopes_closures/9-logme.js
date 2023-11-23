#!/usr/bin/node

exports.logMe = function (item) {
  for (let i = 0; i < item.length; i++) {
    console.log(`${i}.${item[i]}`);
  }
};
