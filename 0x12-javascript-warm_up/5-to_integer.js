#!/usr/bin/node
/* This script prints My number: <first argument converted in
 * integer> if the first argument can be converted to an integer
 */ 

const args = process.argv.slice(2);
const arg1 = parseInt(args[0], 10);

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg1}`);
}
