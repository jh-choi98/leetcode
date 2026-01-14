from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
                return 0
            
        memo = {}
            
        def recur(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return nums[0]
            if n <= 1:
                return max(nums[0], nums[1])
            
            result = max(recur(n - 1), nums[n] + recur(n - 2))
            memo[n] = result
            return result

        return recur(len(nums) - 1)

# Recursion
# Time: O(2^n)
# Space: O(n)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        return dfs(0)
    
# DP (Top-Down) with memoization (list)
# Time: O(n)
# Space: O(n)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        
        return dfs(0)

# DP (Bottom-Up)
# Time: O(n)
# Space: O(n)
class Solution4:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]

# DP (Space Optimized)
"""
We do not actually need a full DP array

At any house, we only care about:
    - the best result up to the previous house
    - the best result up to the house before that
    
So instead of storing everything, we just keep two variables and update them as we move forward
"""
class Solution5:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
