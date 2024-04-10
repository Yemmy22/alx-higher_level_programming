#!/usr/bin/node

if (!process.argv[2]) {
/* This could also be written as:
 * if (process.argv[2] === undefined)
 */
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
