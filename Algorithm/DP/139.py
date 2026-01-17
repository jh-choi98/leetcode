from typing import List

# Recursion
# Time: O(t * m^n)
# Space: O(n)
# Where n is the length of the string s, m is the number of words in
# wordDict and t is the maximum length of any word in wordDict
"""
At every index i in the string, we want to decide:
    Can the suffix starting at index i be segmented into valid
    dictionary words?

The recursive idea is:
    - Try every word in wordDict
    - If a word matches the string starting at position i
    - Recursively check whether the remaining substring (starting at i +
      len(word)) can also be broken successfully

If any path reaches the end of the string, the answer is true
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i: int) -> bool:
            if i == len(s):
                return True
            
            for w in wordDict:
                if((i + len(w)) <= len(s) and 
                   s[i:i + len(w)] == w):
                    if dfs(i + len(w)):
                        return True
            return False
        
        return dfs(0)

# Recursion (Hash Set)
# Time: O((n * 2^n) + m)
# Space: O(n + m*t)
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        def dfs(i):
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False
        
        return dfs(0)

# DP (Top-Down)
# Time: O(n * m * t)
# Space: O(n)
# An optimized version of recursion using memoization
class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                    s[i : i + len(w)] == w):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)

# DP (Hash Set)
# Time: O((t^2 * n) + m)
# Space: O(n + (m*t))
"""
A top-down dynamic programming solution with pruning

Key ideas:
    - Checking every possible substring is expensive.
    - A word can only be as long as the maximum word length in wordDict.
    - Use a Hash Set for O(1) word lookup.
    - Use memoization so each index in the string is solved only once.
    
So we:
    - Limit how far we try to split from each index
    - Cache results for indices to avoid repeated work
    
This turns exponential recursion into efficient DP.
"""
class Solution4:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))
            
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)

# DP (Bottom-Up)
# Time: O(t * m * n)
# Space: O(n)
class Solution5:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i:i+len(s)] == w):
                    dp[i] = dp[i+len(w)]
                
                if dp[i]:
                    break
        return dp[0]
