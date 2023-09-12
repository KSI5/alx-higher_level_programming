#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is not a positive integer or is equal to 0, create an empty object
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // Print the rectangle using 'X' characters
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
