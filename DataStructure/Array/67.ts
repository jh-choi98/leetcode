// Bit by Bit Computatioin
function addBinary1(a: string, b: string): string {
  const maxLen = Math.max(a.length, b.length) + 1;
  const aLeadingZeroes = a.padStart(maxLen, "0");
  const bLeadingZeroes = b.padStart(maxLen, "0");
  let newBinStr: string = "";
  let carry = 0;
  for (let i = maxLen - 1; i >= 0; i--) {
    if (i == 0 && carry == 0) break;
    let curResult =
      parseInt(aLeadingZeroes[i]) + parseInt(bLeadingZeroes[i]) + carry;
    if (curResult >= 2) {
      curResult -= 2;
      carry = 1;
    } else {
      carry = 0;
    }
    newBinStr = curResult.toString() + newBinStr;
  }
  return newBinStr;
}

// Bit Manipulation
/*
If an interviewer provides you with two numbers and asks to sum them
up without using the addition operation.

Interview tip for bit manipulation problems
: if you don't know how to start, start by computing XOR for your
input data.

Binary Addition == XOR + AND(1 bit shited left)

1. Convert a and b into integers x and y, x will be used to keep
   an answer, and y for the carry.

2. While carry is nonzero (y != 0):
   - Current answer without carry is XOR of x and y: answer = x^y
   - Current carry is left-shifted AND of x and y: carry = (x & y) << 1
   - Prepare the next loop: x = answer, y = carry
3. Return x in the binary form
*/
function addBinary2(a: string, b: string): string {
  let x = BigInt(`0b${a}`);
  let y = BigInt(`0b${b}`);
  while (y) {
    let answer = x ^ y; // x XOR y
    let carry = (x & y) << BigInt(1);
    x = answer;
    y = carry;
  }
  return x.toString(2);
}
