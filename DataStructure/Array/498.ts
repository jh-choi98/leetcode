// Diagonal Traverse

function findDiagonalOrder(mat: number[][]): number[] {
  let newArr: number[] = [];

  const outLoopLen: number = mat.length;
  const inLoopLen: number = mat[0].length;

  let isUpward: boolean = true;
  let i: number = 0;
  let j: number = 0;

  while (i < outLoopLen && j < inLoopLen) {
    newArr.push(mat[i][j]);
    if (isUpward) {
      if (j == inLoopLen - 1) {
        i += 1;
        isUpward = !isUpward;
      } else if (i == 0) {
        j += 1;
        isUpward = !isUpward;
      } else {
        i -= 1;
        j += 1;
      }
    } else {
      if (i == outLoopLen - 1) {
        j += 1;
        isUpward = !isUpward;
      } else if (j == 0) {
        i += 1;
        isUpward = !isUpward;
      } else {
        i += 1;
        j -= 1;
      }
    }
  }
  return newArr;
}

function findDiagonalOrder2(mat: number[][]): number[] {
  const d: { [key: number]: number[] } = {};
  const outLoopLen: number = mat.length;
  const inLoopLen: number = mat[0].length;

  for (let i: number = 0; i < outLoopLen; i++) {
    for (let j: number = 0; j < inLoopLen; j++) {
      const key = i + j;
      if (!d[key]) {
        d[key] = [];
      }
      d[key].push(mat[i][j]);
    }
  }

  const ans: number[] = [];

  Object.keys(d).forEach((key) => {
    const numKey = parseInt(key); // Object.keys의 리턴값이 문자열 타입이기 때문
    if (numKey % 2 === 0) {
      ans.push(...d[numKey].reverse());
    } else {
      ans.push(...d[numKey]);
    }
  });

  return ans;
}
