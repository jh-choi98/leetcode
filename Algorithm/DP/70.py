# Climbing Stairs

"""
# of ways to reach ith step = # of ways to reach (i-1)th step
                            + # of (i-2)th step
"""


# DP - bottom-up
# T: O(n)
# S: O(1)
# 진짜 지리는 방법....
class Solution:
    def climbStairs(self, n):
        one, two = 1, 1
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


# DP - bottom-up
# T: O(n)
# S: O(n) using extra space
class Solution2:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# DP - top-down
# T: O(n)
# S: O(n)
class Solution3:
    def climbStairs(self, n):
        cache = {}

        def climb(n):
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            result = climb(n - 1) + climb(n - 2)
            cache[n] = result
            return result

        return climb(n)
