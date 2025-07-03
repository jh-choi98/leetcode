from typing import List

# T: O(n)
# Searching both sides -> inefficient
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinRecur(l, r):
            if l == r:
                return nums[l]

            if nums[l] > nums[r]:
                mid = (l + r) // 2

                left = findMinRecur(l, mid)
                right = findMinRecur(mid + 1, r)
                return min(left, right)
            else:
                return nums[l]
        return findMinRecur(0, len(nums) - 1)

# T: O(logn)
# Recursion    
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        def findMinRecur(l, r):
            if l == r:
                return nums[l]

            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                return findMinRecur(mid + 1, r)
            else:
                return findMinRecur(l, mid)

        return findMinRecur(0, len(nums) - 1)

# T: O(logn)
# Loop
class Solution3:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
