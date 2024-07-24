// Solution1: using quick sort
// Time complexity: O(nlog n) (O(n^2) in worst case)
// Space complexity: O(n)

function quickSort(arr, left = 0, right = arr.length - 1) {
  if (left < right) {
    const pivotIndex = partition(arr, left, right);

    quickSort(arr, left, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, right);
  }
  return arr;
}

function partition(arr, left, right) {
  const pivot = arr[right];
  let i = left - 1;

  for (let j = left; j < right; j++) {
    if (arr[j] < pivot) {
      ++i;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  [arr[i + 1], arr[right]] = [arr[right], arr[i + 1]];
  return i + 1;
}

var sortedSquares1 = function (nums) {
  const len = nums.length;
  let newArr = new Array(len);

  for (let i = 0; i < len; ++i) {
    newArr[i] = Math.pow(nums[i], 2);
  }

  return quickSort(newArr);
};

// ***********************************************
// Solution 2: using radix sort
// Time complexity: O(n)
// Space complexity: O(n)

class Solution2 {
  getMax(arr) {
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
  countSort(arr, exp) {
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
  radixSort(arr) {
    const max = this.getMax(arr);
    for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {
      this.countSort(arr, exp);
    }
  }

  sortedSquares(nums) {
    for (let i = 0; i < nums.length; i++) {
      nums[i] *= nums[i];
    }
    this.radixSort(nums);
    return nums;
  }
}

// ***********************************************
// Solution3: using sort function
// Time complexity: O(nlogn)
// Space complexity: O(1)

var sortedSquares3 = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    nums[i] *= nums[i];
  }
  nums.sort((a, b) => a - b);
  return nums;
};

// ***********************************************
// Solution4: using two pointers
// Time complexity: O(n)
// Space complexity: O(n)

var sortedSquares4 = function (nums) {
  const len = nums.length;
  const ans = new Array(len);
  let start = 0;
  let end = len - 1;

  for (let i = n - 1; i >= 0; i--) {
    if (Math.abs(nums[start]) >= Math.abs(nums[end])) {
      ans[i] = nums[start] * nums[start];
      start++;
    } else {
      ans[i] = nums[end] * nums[end];
      end--;
    }
  }
  return ans;
};
