#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let argArray = process.argv.slice(2);
  argArray = argArray.sort().map(Number);

  const Largest = argArray[argArray.length - 1];

  for (let i = 0; argArray[i + 1] !== undefined; i++) {
    if (argArray[i + 1] === Largest) {
      console.log(argArray[i]); break;
    }
  }
}
