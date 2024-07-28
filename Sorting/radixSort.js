// Time complexity: O(n)
// Space complexity: O(n)

function getMax(arr) {
  let max = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

/*
countSort performs counting sort on the given arr based on a specific digit, exp
exp indicates the current digit position.
It updates the count array based on the digit at exp, builds the output array 
    using the count array, and finally copies the sorted values back into the original array
*/
function countSort(arr, exp) {
  // exp: the digit position we are sorting by (1 for units, 10 for tens etc.)
  const output = new Array(arr.length); // holds the sorted elements temporarily
  const count = new Array(10).fill(0); // stores the count of occurrences of each digit (0 - 9)

  // Step 1: Count occurrences of each digit
  for (let i = 0; i < arr.length; i++) {
    count[Math.floor(arr[i] / exp) % 10]++;
    // exp 자리수의 digit을 찾은 뒤 거기에 대응하는 count array의 요소 + 1;
  }

  // transforms 'count' to represent the position of the digit in the output array
  // Step 2: Change count[i] so that count[i] now contains the actual
  //   postion of this digit in the output array
  for (let i = 1; i < 10; i++) {
    count[i] += count[i - 1];
  }

  // Step 3: Build the output array by placing elements in their correct positions
  // We iterate from right to left to maintain stability
  for (let i = arr.length - 1; i >= 0; i--) {
    output[count[Math.floor(arr[i] / exp) % 10] - 1] = arr[i];
    count[Math.floor(arr[i] / exp) % 10]--;
    // ensures that the next occurrence of the same digit will be placed
    // in the next available position to the left
  }

  // Step 4: Copy the sorted elements into the original array
  for (let i = 0; i < arr.length; i++) {
    arr[i] = output[i];
  }
}

// It sorts the array progressively from the least significant digit
//   to the most significant digit
function radixSort(arr) {
  const max = getMax(arr);
  for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {
    countSort(arr, exp);
  }
}
