# Intersection of Two Arrays II
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):
        hm1 = {}
        hm2 = {}
        ans = []
        for num in nums1:
            if num not in hm1:
                hm1[num] = 1
            else:
                hm1[num] += 1

        for num in nums2:
            if num not in hm2:
                hm2[num] = 1
            else:
                hm2[num] += 1

        for x in hm1:
            if x in hm2:
                for _ in range(min(hm1[x], hm2[x])):
                    ans.append(x)

        return ans


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]):
        hm = {}
        ans = []

        for num in nums1:
            hm[num] = hm.get(num, 0) + 1

        for num in nums2:
            if num in hm and hm[num] > 0:
                ans.append(num)
                hm[num] -= 1

        return ans
