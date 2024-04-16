#!/usr/bin/node
const baseSquare = require('./5-square');

module.exports = class Square extends baseSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
