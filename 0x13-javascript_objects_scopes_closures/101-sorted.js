#!/usr/bin/node

const { dict } = require('./101-data');

const userByOccurrence = Object.entries(dict).reduce((result, [userId, occurrences]) => {
  if (result[occurrences]) {
    result[occurrences].push(userId);
  } else {
    result[occurrences] = [userId];
  }
  return result;
}, {});

console.log(userByOccurrence);
