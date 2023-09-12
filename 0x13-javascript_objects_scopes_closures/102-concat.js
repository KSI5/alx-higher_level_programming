#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: ./concat-files.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1}: ${err.message}`);
    process.exit(1);
  }

  // Read the content of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate the content of the source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFile}: ${err.message}`);
        process.exit(1);
      }

      console.log(`Concatenated data written to ${destinationFile}`);
    });
  });
});
