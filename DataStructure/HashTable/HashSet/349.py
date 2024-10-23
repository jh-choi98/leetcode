# Intersection of Two Arrays

from typing import List


# T: O(n)
# S: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        for item in set1:
            if item in set2:
                ans.append(item)

        return ans
