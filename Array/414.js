// Third Maximal Number

// Solution1
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
      if (ithMaxCount === 3) {
        return nums[i];
      }
    }
  }

  return nums[0];
};

// Solution2
