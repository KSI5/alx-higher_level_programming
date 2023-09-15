#!/usr/bin/node
// computes and prints a factorial

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  return n === 0 ? 1 : n * factorial(n - 1);
}

const input = parseInt(process.argv[2]);
console.log(factorial(input));
