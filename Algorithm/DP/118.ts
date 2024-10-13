function generate(numRows: number): number[][] {
  const triangle: number[][] = [];

  for (let row_num = 0; row_num < numRows; row_num++) {
    const row: number[] = new Array(row_num + 1).fill(0);
    row[0] = 1;
    row[row_num] = 1;

    for (let j = 1; j < row.length - 1; j++) {
      row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j];
    }

    triangle.push(row);
  }
  return triangle;
}
