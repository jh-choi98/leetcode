// Find Numbers with Even Number of Digits

// sol1
function isEvenDigits(num) {
  let count = 0;
  while (num > 0) {
    ++count;
    num = Math.floor(num / 10);
  }
  return count % 2 == 0;
}

var findNumbers1 = function (nums) {
  let count = 0;
  let len = nums.length;
  for (let i = 0; i < len; ++i) {
    if (isEvenDigits(nums[i])) {
      ++count;
    }
  }
  return count;
};

// sol2
var findNumbers2 = function (nums) {
  let count = 0;
  for (let num of nums) {
    let digits = Math.floor(Math.log10(num) + 1);
    if (digits % 2 == 0) {
      ++count;
    }
  }
  return count;
};
