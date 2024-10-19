from typing import List


# T: O(n)
# S: O(1)
# DP - bottom-up
class Solution:
    def rob(self, nums: List[int]):
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# T: O(n)
# S: O(n)
# DP - top-down
class Solution2:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]):
        self.memo = {}

        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # No more houses left to examine
        if i >= len(nums):
            return 0
        # Return cached value
        if i in self.memo:
            return self.memo[i]

        # Recursive relation evaluation to get the optimal answer
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = ans
        return ans


# T: O(n)
# S: O(n)
# DP - bottom-up
class Solution3:
    def rob(self, nums: List[int]):
        # special handling for empty case
        if not nums:
            return 0

        n = len(nums)
        maxRobbed = [0 for _ in range(n + 1)]

        # base case
        maxRobbed[n], maxRobbed[n - 1] = 0, nums[n - 1]

        for i in range(n - 2, -1, -1):
            maxRobbed[i] = max(maxRobbed[i + 1], maxRobbed[i + 2] + nums[i])

        return maxRobbed[0]
