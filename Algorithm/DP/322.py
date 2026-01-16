from typing import List
from collections import deque

# Recursion
# Time: O(n^t)
#   where n is the length of the array 'coins' and
#   t is the given 'amount'
# Space: O(n)
"""
For a given amount, we try every coin:
    - Pick one coin
    - Solve the remaining subproblem (amount - coin)
    - Take the minimum coins needed among all choices
We explore all possible combinations, which leads to many repeated subproblems and exponential time
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX_VAL = amount + 1
        
        def dfs(amount):
            if amount == 0:
                return 0
            
            res = MAX_VAL
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res
        minCoins = dfs(amount)
        return -1 if minCoins >= MAX_VAL else minCoins

# DP (Top-Down)
# The optimized version of the brute-force recursion using memoization
# Time: O(n * t)
# Space: O(n)
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX_VAL = amount + 1
        memo = {}
        
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = MAX_VAL
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = coin
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= MAX_VAL else minCoins

# DP (Bottom-Up)
# Time: O(n * t)
# Space: O(n)
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != (amount + 1) else -1

# BFS
# Time: O(n * t)
# Space: O(n)
"""
Think of each amount as a node in a graph
    - From a current amount x, you can go to x + coin for every coin
    - Each edge represents using one coin
    - We want the minimum number of coins, which means the shortest path
      from 0 to amount
      
This makes the problem a shortest path in an unweighted graph, so
Breadth First Search (BFS) is a natural fit
"""
class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0
        
        while queue:
            res += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    queue.append(nxt)
                    
        return -1
