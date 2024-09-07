// Remove Duplicates from Sorted Array

// Solution1
var removeDuplicates = function (nums) {
  let len = nums.length;
  let temp = nums[0];

  for (let i = 1; i < len; i++) {
    if (nums[i] === temp) {
      for (let j = i; j < len - 1; j++) {
        nums[j] = nums[j + 1];
      }
      nums[nums.length - 1] = 0;
      --len;
      --i;
    } else {
      temp = nums[i];
    }
  }
  return len;
};

// Solution2
var removeDuplicates2 = function (nums) {
  let numsSet = new Set(nums);
  let newNums = [...numsSet];
  for (let i = 0; i < newNums.length; i++) {
    nums[i] = newNums[i];
  }
  return newNums.length;
};

// Solution3
var removeDuplicates3 = function (nums) {
  if (nums.length === 0) {
    return 0;
  }

  let k = 1;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[k - 1]) {
      nums[k] = nums[i];
      k++;
    }
  }
  return k;
};
