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
      }
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
// T: O(n)
// S: O(1)
var thirdMax4 = function (nums) {
  let numsSet = new Set();

  for (let num of nums) {
    if (numsSet.has(num)) {
      continue;
    }

    if (numsSet.size === 3) {
      // Destructing assignment(비구조화 할당): 배열이나 객체의 속성을 분해하여
      // 개별 변수에 할당할 수 있게 해주는 문법
      let [firstElement] = numsSet;
      if (firstElement < num) {
        numsSet.delete(firstElement);
        numsSet.add(num);
      }
    } else {
      numsSet.add(num);
    }

    // Set은 정렬 메소드를 제공하지 않기 때문에 Set을 배열로 변환하여 정렬한 후 다시
    // Set으로 만들기
    numsSet = new Set([...numsSet].sort((a, b) => a - b));
  }

  if (numsSet.size === 3) {
    let [firstElement] = numsSet;
    return firstElement;
  }

  let lastElement = [...numsSet].pop();
  return lastElement;
};

// Solution5
// using 3 Pointer
// T: O(n)
// S: O(1)
var thirdMax5 = function (nums) {
  let firstMax = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;
  let thirdMax = Number.MIN_SAFE_INTEGER;

  for (let num of nums) {
    if (firstMax === num || secondMax === num || thirdMax === num) {
      continue;
    }

    if (firstMax <= num) {
      [thirdMax, secondMax, firstMax] = [secondMax, firstMax, num];
    } else if (secondMax <= num) {
      [thirdMax, secondMax] = [secondMax, num];
    } else if (thirdMax <= num) {
      thirdMax = num;
    }
  }

  if (thirdMax === Number.MIN_SAFE_INTEGER) {
    return firstMax;
  }
  return thirdMax;
};

// Solution6
// using 3 Pointer2 + pair
var thirdMax6 = function (nums) {
  let firstMax = [-1, false];
  let secondMax = [-1, false];
  let thirdMax = [-1, false];

  for (let num of nums) {
    if (
      (firstMax[1] && firstMax[0] === num) ||
      (secondMax[1] && secondMax[0] === num) ||
      (thirdMax[1] && thirdMax[0] === num)
    ) {
      continue;
    }

    if (!firstMax[1] || firstMax[0] < num) {
      thirdMax = secondMax;
      secondMax = firstMax;
      firstMax = [num, true];
    } else if (!secondMax[1] || secondMax[0] < num) {
      thirdMax = secondMax;
      secondMax = [num, true];
    } else if (!thirdMax[1] || thirdMax[0] < num) {
      thirdMax = [num, true];
    }
  }

  if (!thirdMax[1]) {
    return firstMax[0];
  }
  return thirdMax[0];
};

let nums = [3, 2, 1];

console.log(thirdMax4(nums));
