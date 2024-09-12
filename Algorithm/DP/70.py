# Climbing Stairs

"""
# of ways to reach ith step = # of ways to reach (i-1)th step
                            + # of (i-2)th step
"""


# T: O(n)
# S: O(n)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
