// Merge Sorted Array

var merge = function (nums1, m, nums2, n) {
  if (m === 0) {
    for (let k = 0; k < n; k++) {
      nums1[k] = nums2[k];
    }
  }

  let i = 0,
    j = 0,
    pos = 0;
  while (i < m || j < n) {
    if (j >= n) {
      break;
    }

    if (i >= m) {
      for (j; j < n; j++) {
        nums1[pos] = nums2[j];
        ++pos;
      }
      break;
    }

    if (nums1[pos] < nums2[j]) {
      ++i;
      ++pos;
    } else {
      for (let k = m + n - 2; k >= pos; k--) {
        nums1[k + 1] = nums1[k];
      }
      nums1[pos] = nums2[j];
      ++pos;
      ++j;
    }
  }
};
