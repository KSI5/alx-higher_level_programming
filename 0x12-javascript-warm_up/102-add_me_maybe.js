#!/usr/bin/node
// Increment a value and invoke a function.
 exports.addMeMaybe = function (number, theFunction) {
   return theFunction(number += 1);
   };
