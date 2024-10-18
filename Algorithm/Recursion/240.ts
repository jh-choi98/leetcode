// Search a 2D Matrix 2
// Recursion - Decrease and Conquer
function searchMatrix(mat: number[][], target: number): boolean {
  const height = mat.length;
  const width = mat[0].length;
  function search(curRow: number, curCol: number): boolean {
    if (curRow >= height || curCol < 0) {
      return false;
    }

    if (mat[curRow][curCol] === target) {
      return true;
    }

    if (mat[curRow][curCol] > target) {
      return search(curRow, curCol - 1);
    } else {
      return search(curRow + 1, curCol);
    }
  }

  return search(0, width - 1);
}
