#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  const s = '#';
  for (i = 0; i < Number(process.argv[2]); i++) {
    console.log(s.repeat(Number(process.argv[2])));
  }
}
