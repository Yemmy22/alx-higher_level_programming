#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const argArray = process.argv.slice(2);
  for (let i = 0; argArray[i] !== undefined; i++) {
    let temp;
    for (let j = i + 1; argArray[j] !== undefined; j++) {
      if (Number(argArray[j]) < Number(argArray[i])) {
        temp = Number(argArray[j]);
        argArray[j] = Number(argArray[i]);
        argArray[i] = temp;
      } else {
        argArray[i] = Number(argArray[i]);
        argArray[j] = Number(argArray[j]);
      }
    }
  }

  const Largest = argArray[argArray.length - 1];
  for (let i = 0; argArray[i + 1] !== undefined; i++) {
    if (argArray[i + 1] === Largest) {
      console.log(argArray[i]); break;
    }
  }
}
