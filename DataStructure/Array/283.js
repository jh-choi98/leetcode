// Move Zeroes

// Solution1
var moveZeroes = function (nums) {
  const len = nums.length;
  if (len === 0 || len === 1) {
    return nums;
  }

  let k = 0;
  for (let i = 0; i < len; ++i) {
    if (nums[i] !== 0) {
      nums[k] = nums[i];
      k++;
    }
  }

  for (let i = k; i < len; ++i) {
    nums[i] = 0;
  }

  return nums;
};

// Solution2
var moveZeroes2 = function (nums) {
  const len = nums.length;
  if (len === 0 || len === 1) {
    return nums;
  }

  let k = 0;
  for (let i = 0; i < len; ++i) {
    if (nums[i] !== 0) {
      [nums[i], nums[k]] = [nums[k], nums[i]];
      k++;
    }
  }

  return nums;
};
