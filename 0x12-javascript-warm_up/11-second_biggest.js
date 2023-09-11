#!/usr/bin/node
// Find the second largest integer among the provided arguments.
const mySol = process.argv;
if (mySol.length <= 3) {
	  console.log(0);
} else {
	  console.log(mySol.sort((x, y) => y - x).slice(3)[0]);
}
