# N-th Tribonacci Number


# DP: bottom-up
# T: O(n)
# S: O(1)
class Solution:
    def tribonacci(self, n: int):
        one, two, three = 0, 1, 1
        if n < 2:
            return n

        for _ in range(n - 2):
            temp1 = three
            three = one + two + three
            one = two
            two = temp1
        return three


# DP: bottom-up
# T: O(n)
# S: O(n)
class Solution2:
    def tribonacci(self, n: int):
        if n < 3:
            return 1 if n else 0
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]


# DP: top-down
# T: O(n)
# S: O(n)
class Solution3:
    def tribonacci(self, n: int):
        memo = {}

        def tribo(n: int):
            if n < 2:
                return n
            if n == 2:
                return 1
            if n in memo:
                return memo[n]
            result = tribo(n - 1) + tribo(n - 2) + tribo(n - 3)
            memo[n] = result
            return result

        return tribo(n)
