#!/usr/bin/node
/* This script prints arguments passed to it. */

const args = process.argv.slice(2);
const firstArg = args[0];

console.log(firstArg || 'No argument');
