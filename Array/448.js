// Find All Numbers Disappeared in an Array

// T: O(n)
// S: O(n)
var findDisappearedNumbers = function (nums) {
  const len = nums.length;
  let set = new Set();
  for (let i = 1; i <= len; i++) {
    set.add(i);
  }

  for (let i = 0; i < len; i++) {
    set.delete(nums[i]);
  }

  return [...set];
};

// T: O(n)
// S: O(1)
var findDisappearedNumbers2 = function (nums) {
  let newNums = new Array();

  for (let i = 0; i < nums.length; i++) {
    if (nums[Math.abs(nums[i]) - 1] > 0) {
      nums[Math.abs(nums[i]) - 1] *= -1;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      newNums.push(i + 1);
    }
  }

  return newNums;
};
