function generate2(numRows: number): number[][] {
  if (numRows === 1) {
    return [[1]];
  }

  const triangle: number[][] = generate2(numRows - 1);
  const prevRow: number[] = triangle[triangle.length - 1];
  const curRow: number[] = [1];

  for (let i: number = 1; i < prevRow.length; i++) {
    curRow.push(prevRow[i - 1] + prevRow[i]);
  }
  curRow.push(1);
  triangle.push(curRow);
  return triangle;
}
