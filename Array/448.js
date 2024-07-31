// Find All Numbers Disappeared in an Array

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
