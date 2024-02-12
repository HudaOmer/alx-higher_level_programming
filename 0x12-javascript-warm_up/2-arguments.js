#!/usr/bin/node
const Argc = process.argv.length;
if (Argc == 2)
  consol.log('No argument');
else if (Argc == 3)
  consol.log('Argument found');
else
  consol.log('Arguments found');
