#!/usr/bin/node
// Check if the first argument exists and print it, or "No argument" if not

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
