#!/usr/bin/node
const Square1 = require('./5-square.js');
class Square extends Square1 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let i = 0; i < this.width; i++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
