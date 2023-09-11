#!/usr/bin/node

// This script checks the number of command-line arguments and prints a message accordingly.
 const args = process.argv;

 if (args.length === 2) {
   console.log("No argument");
   } else if (args.length === 3) {
     console.log("Argument found");
     } else {
       console.log("Arguments found");
       }

