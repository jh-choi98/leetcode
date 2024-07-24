// Max Consecutive Ones

/**
 * @param {number[]} nums
 * @return {number}
 */

var findMaxConsecutiveOnes = function (nums) {
  let len = nums.length;
  let max = 0;
  let count = 0;
  for (let i = 0; i < len; ++i) {
    if (nums[i] == 0) {
      count = 0;
      continue;
    }
    ++count;
    max = Math.max(count, max);
  }
  return max;
};
