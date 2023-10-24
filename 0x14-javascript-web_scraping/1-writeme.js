#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the first argument
const content = process.argv[3]; // Get the string to write from the second argument

if (!filePath || !content) {
  console.error('Usage: node 1-writeme.js <file_path> <content>');
  process.exit(1);
}

// Write the content to the specified file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred while writing
  }
});
