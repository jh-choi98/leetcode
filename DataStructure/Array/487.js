// Max Consecutive Ones 2

var findMaxConsecutiveOnes = function (nums) {
  if (nums.length === 1) {
    return 1;
  }

  let numsOfOnes = [];
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0 || i === nums.length - 1) {
      if (nums[i] === 1) {
        count++;
      }
      numsOfOnes.push(count);
      count = 0;
      continue;
    }
    count++;
  }

  if (numsOfOnes.length === 1) {
    if (numsOfOnes[0] === nums.length) {
      return numsOfOnes[0];
    }
    return numsOfOnes[0] + 1;
  }

  let max = 0;
  for (let i = 0; i < numsOfOnes.length - 1; i++) {
    if (numsOfOnes[i] + numsOfOnes[i + 1] + 1 > max) {
      max = numsOfOnes[i] + numsOfOnes[i + 1] + 1;
    }
  }

  return max;
};

// Sliding Window
var findMaxConsecutiveOnes2 = function (nums) {
  let longestSeq = 0;
  let left = 0,
    right = 0;
  let numsZeroes = 0; // 현재 윈도우 내에 있는 0의 개수

  while (right < nums.length) {
    if (nums[right] === 0) {
      numsZeroes++;
    }

    // 윈도우 내에 0이 2개 이상 있을 때, 윈도우 축소
    // 윈도우 내에 0이 2개 이상일 때, 윈도우의 왼쪽 경계를 이동하여 0의 개수를 줄인다.
    // 이렇게 하면 최대 하나의 0을 1로 바꿀 수 있는 조건을 유지하면서 최대 연속 1의 개수를 계산할 수 있다.
    while (numsZeroes === 2) {
      if (nums[left] === 0) {
        numsZeroes--;
      }
      left++; // 윈도우 축소
    }

    // longestSeq와 현재 윈도우 길이 비교
    longestSeq = Math.max(longestSeq, right - left + 1);
    right++; // 윈도우 확장
  }
  return longestSeq;
};

// 1. right 포인터를 배열의 처음부터 끝까지 이동시킨다.
// 2. nums[right]가 0이면 numsZeroes를 1 증가시킨다.
// 3. numsZeroes가 2가 되면, 윈도우 내에 0이 2개 있다는 의미이므로,
//    left 포인터를 이동하여 0의 개수가 다시 1이 될 때까지 윈도우를 축소한다.
// 4. 매 반복마다 현재 윈도우의 길이 (right - left + 1)를 계산하여
//    longestSeq와 비교하고 더 큰 값을 longestSeq에 저장합니다.

// Sliding window 기법
// 배열이나 문자열 같은 시퀀스 데이터 구조에서 특정 범위 내의 요소를 효율적으로 처리하는 방법.
// 특히, 연속된 부분 배열(부분 문자열)에서 특정 조건을 만족하는 최대/최소 값을 찾는데 유용
// 윈도우 확장: right 포인터를 오른쪽으로 이동시켜 확장
// 윈도우 축소: left 포인터를 오른쪽으로 이동시켜 축소
// 윈도우 크기: right - left + 1
// 윈도우 내의 요소들이 특정 조건을 만족하는지 체크. 만족하지 않으면 윈도우를 축소 또는
//   확장시켜 조건을 만족시키도록 조정
