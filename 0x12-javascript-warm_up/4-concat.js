#!/usr/bin/node
/* This prints two args passed to it and concat it with "is" */

const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

console.log(`${arg1} is ${arg2}`);
