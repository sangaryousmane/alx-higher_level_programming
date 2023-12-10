#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) { console.log(0); } else if (args.length === 1) { console.log(0); } else {
  let max = parseInt(args[0]);
  let secondMax = parseInt(args[1]);

  if (secondMax > max) { [max, secondMax] = [secondMax, max]; }

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax) { secondMax = num; }
  }
  console.log(secondMax);
}
