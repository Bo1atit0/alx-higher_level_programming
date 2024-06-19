#!/usr/bin/node

// Write a function that increments
// and calls a function.

exports.addMeMaybe = function (number, theFunction) {
    const result = number + 1;
    theFunction = function (nb) {
        return nb = result ;
    }
};