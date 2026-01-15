# Brute Force
# Time: O(n^3)
# Space: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i: j + 1]
                    resLen = j - i + 1
        return res
    
# DP (Bottom-Up)
# Time: O(n^2)
# Space: O(n^2)
"""
Let:
    dp[i][j] = true if the substring s[i..j] is a palindrome
    
A substring s[i..j] is a palindrome when:
    1. The end characters match: s[i] == s[j]
    2. And the inside part is also a palindrome: dp[i+1][j-1]
        - Special small cases: if the length is 1, 2, or 3 (j - i <= 2),
        then matching ends is enough because the middle is empty or a
        single char
        
We fill dp from bottom to top (i from n-1 down to 0) so that when we
compute dp[i][j], the value dp[i+1][j-1] is already known

While filling, we keep track of the best (longest) palindrome seen so far
"""
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
                        
        return s[resIdx: resIdx + resLen]
         
# Two Pointers
# Time: O(n^2)
# Space: O(1)
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        return s[resIdx: resIdx + resLen]
    