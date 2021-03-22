#!/usr/bin/node
console.log(factorial(process.argv[2]));

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else {
    if (a === 0) {
      return 1;
    } else {
      return Number(a * factorial(a - 1));
    }
  }
}
