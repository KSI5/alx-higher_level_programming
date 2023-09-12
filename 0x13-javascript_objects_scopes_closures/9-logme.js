#!/usr/bin/node

let count = 0; // Initialize a count variable to keep track of the number of arguments printed

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
