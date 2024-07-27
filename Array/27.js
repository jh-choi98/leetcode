// Remove element

var removeElement = function (nums, val) {
  let len = nums.length;
  for (let i = 0; i < len; i++) {
    if (nums[i] === val) {
      for (let j = i + 1; j < nums.length; ++j) {
        nums[j - 1] = nums[j];
      }
      --i;
      --len;
      nums[nums.length - 1] = 0;
    }
  }
  return len;
};

var removeElement2 = function (nums, val) {
  let len = nums.length;
  let left = 0;
  for (let i = 0; i < len; i++) {
    if (nums[i] !== val) {
      [nums[left], nums[i]] = [nums[i], nums[left]];
      ++left;
    }
  }
  return left;
};
