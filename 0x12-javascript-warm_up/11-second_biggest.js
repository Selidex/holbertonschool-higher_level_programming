#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  let i = 2;
  const ary = [];
  for (i = 2; i < process.argv.length; i++) {
    ary.push(Number(process.argv[i]));
  }
  ary.sort(function (a, b) { return b - a; });
  console.log(ary[1]);
}
