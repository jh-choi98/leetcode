// Third Maximal Number
import MinHeap from "./minHeap.js";

// Solution1
// using Quick Sort
// T: O(nlogn)
// S: O(1)
function quickSort(arr, left = 0, right = arr.length - 1) {
  if (left < right) {
    const pivotIndex = partition(arr, left, right);

    quickSort(arr, left, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, right);
  }
  return arr;
}

function partition(arr, left, right) {
  let pivot = arr[right];
  let i = left - 1;
  for (let j = left; j < right; j++) {
    if (arr[j] > pivot) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  [arr[i + 1], arr[right]] = [arr[right], arr[i + 1]];

  return i + 1;
}

var thirdMax1 = function (nums) {
  quickSort(nums);
  if (nums.length < 3) {
    return nums[0];
  }

  let ithMaxCount = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[i - 1]) {
      ithMaxCount++;
    }

    if (ithMaxCount === 3) {
      return nums[i];
    }
  }

  return nums[0];
};

// Solution2
// using STL sort function
// T: O(nlogn)
// S: O(1)
var thirdMax2 = function (nums) {
  nums.sort((a, b) => b - a); // non-increasing order (O(nlogn))
  let elemCounted = 1;
  let prevElem = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[index] !== prevElem) {
      elemCounted += 1;
      prevElem = nums[i];
    }

    if (elemCounted === 3) {
      return nums[i];
    }
  }

  return nums[0];
};

// Solution3
// using Min Heap
// T: O(n)
// S: O(1)
/* Pseudo Code 
1. Initialize variables:
 - minHeap: a min heap to keep the smallest element on top
 - taken: a hash set to track inserted numbers in min heap
2. Iterate on all numbers of nums array:
 - If the current number is already in the min heap, we skip it.
 - If the min heap has three numbers in it, and if the current number is greater than 
   the smallest in the min heap, then remove the smallest number and 
   push the current number in both the min heap and the hash set.
 - Otherwise, if the min heap has less than three elements, 
   then just push the current number in the min heap and the hash set.
3. If the min heap has less than three elements at the end, return the maximum element 
   among all elements present in the min heap, which will be the largest number of 
   the nums array.
4. Otherwise, return the top element of the min heap, which will be the third largest number. 
*/

var thirdMax3 = function (nums) {
  let minHeap = new MinHeap();
  let taken = new Set();

  for (let i = 0; i < nums.length; ++i) {
    if (taken.has(nums[i])) {
      continue;
    }

    if (minHeap.getSize() === 3) {
      if (minHeap.getMin() < nums[i]) {
        taken.delete(minHeap.extractMin());
        minHeap.insert(nums[i]);
        taken.add(nums[i]);
      }
    } else {
      minHeap.insert(nums[i]);
      taken.add(nums[i]);
    }
  }

  if (minHeap.getSize() !== 3) {
    return minHeap.heap[minHeap.getSize() - 1];
  }

  return minHeap.getMin();
};
// Solution4
// using Ordered Set

// Solution5
// using 3 Pointer

// Solution6
// using 3 Pointer2

let nums = [3, 2, 1];

console.log(thirdMax3(nums));
