#!/usr/bin/node

// Print "My number: <first argument as an integer>" if the first argument is convertible to an integer.

const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
	  console.log(`My number: ${number}`);
} else {
	  console.log("Not a number");
}
