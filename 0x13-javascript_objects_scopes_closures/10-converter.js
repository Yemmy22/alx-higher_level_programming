#!/usr/bin/node

exports.converter = function (base) {
  function inner (num) {
    return num.toString(base);
  }
  return inner;
};
/*
 *
 * This works as well.
exports.converter = function (base) {
  return (num) => {
    return num.toString(base);
  };
};
*/
