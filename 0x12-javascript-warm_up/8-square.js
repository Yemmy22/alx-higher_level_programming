#!/usr/bin/node

const arg = Number(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let j = 0;
    let line = '';

    while (j < arg) {
      line += 'X';
      j++;
    }
    console.log(line);
  }
}
