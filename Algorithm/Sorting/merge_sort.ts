const mergeSort = (arr: number[]): number[] => {
  if (arr.length <= 1) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const leftHalf: number[] = mergeSort(arr.slice(0, mid));
  const rightHalf: number[] = mergeSort(arr.slice(mid));

  return merge(leftHalf, rightHalf);
};

const merge = (left: number[], right: number[]): number[] => {
  let i = 0,
    j = 0;
  const sortedArr: number[] = [];
  while (i < left.length && j < right.length) {
    // if (left[i] < right[j]) {
    //   sortedArr.push(left[i]);
    //   i += 1;
    // } else {
    //   sortedArr.push(right[j]);
    //   j += 1;
    // }
    sortedArr.push(left[i] < right[j] ? left[i++] : right[j++]);
  }

  return [...sortedArr, ...left.slice(i), ...right.slice(j)];
};

function main() {
  const arr = [7, 6, 5, 4, 3, 2, 1];
  console.log(mergeSort(arr));
}

main();
