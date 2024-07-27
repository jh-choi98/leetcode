// Sort Array by Parity

var sortArrayByParity = function (nums) {
  let evenIdx = 0;
  const len = nums.length;
  for (let i = 0; i < len; i++) {
    if (nums[i] % 2 === 0) {
      [nums[evenIdx], nums[i]] = [nums[i], nums[evenIdx]];
      evenIdx++;
    }
  }
  return nums;
};
