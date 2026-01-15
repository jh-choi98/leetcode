from typing import List

# DP (Bottom-Up w/ Space Optimization)
# Time: O(n)
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def get_max(nums):
            one, two = 0, 0
            for i in range(len(nums)):
                tmp = two
                two = max(one + nums[i], two)
                one = tmp
            return two
        
        return max(get_max(nums[:-1]), get_max(nums[1:]))

# Recursion
# Time: O(2^n)
# Space: O(n)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            return max(dfs(i + 1, flag),
                       nums[i] + dfs(i + 2, flag or i == 0))
        
        return max(dfs(0, True), dfs(1, False))

# DP(Top-Down)
# 시작하는 인덱스가 0이든 N이든, "답을 모르니 가서 구해와!"라고 시키는
# 방식이면 무조건 Top-Down
# 값이 없어서 구하러 내려가는 것
# Time: O(n)
# Space: O(n)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [[-1] * 2 for _ in range(len(nums))]
        
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != - 1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or (i == 0)))
            
            return memo[i][flag]
            
        return max(dfs(0, True), dfs(1, False))

# DP (Bottom-Up)
# "이제 i를 구할 차례네. 아까 구해둔 i-1 결과 어딨지? 가져와서 쓰자."
# 이미 값이 있어서 가져다 쓰는 것
# Time: O(n)
# Space: O(n)
class Solution4:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
                return max(nums[0], nums[1])
        
        def helper(nums: List[int]) -> int:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
            return dp[-1]
        
        return max(helper(nums[:-1]), helper(nums[1:]))
