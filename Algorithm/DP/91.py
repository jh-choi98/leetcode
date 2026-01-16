# Recursion
# Time: O(2^n)
# Space: O(n)
"""
At any index i, you only have two possible decoding choices:
    1. Take one digit (s[i]) → valid if it’s not '0'
    2. Take two digits (s[i:i+2]) → valid if it forms a number between
       10 and 26

So the problem naturally breaks into subproblems:
    “How many ways can I decode the substring starting at index i?”

Key base ideas:
    - If you reach the end of the string → 1 valid decoding
    - If a substring starts with '0' → 0 ways (invalid)
    - Otherwise, sum the ways from:
        - decoding one digit
        - decoding two digits (if valid)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i: int):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or
                    (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)
            return res
        
        return dfs(0)


# DP (Top-Down)
# Time: O(n)
# Space: O(n)
"""
recursion with memoization
Use a dictionary dp where dp[i] = number of ways to decode s[i:]
    - Initialize base cases:
        - dp[len(s)] = 1: empty string has one valid decoding
"""
class Solution2:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        
        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or (
                s[i] == "2" and s[i + 1] in '0123456'
            )):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)


# DP (Bottom-Up)
# Time: O(n)
# Space: O(n)
"""
This is the iterative version of the decoding logic
"""
class Solution3:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                
            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]

# DP (Space Optimized)
# Time: O(n)
# Space: O(1)
class Solution4:
    def numDecodings(self, s: str) -> int:
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1
            
            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp += dp2
            
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
