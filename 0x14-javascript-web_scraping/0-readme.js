#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (error, data) {
  console.log(error || data);
});
