#!/usr/bin/node

let argumentsCount = 0;

exports.logMe = function (item) {
  console.log(`${argumentsCount}: ${item}`);
  argumentsCount++;
};
