#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w < 1) || (h < 1)) {
      w = undefined;
      h = undefined;
    } else if ((w === undefined) || (h === undefined)) {
      w = undefined;
      h = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
