# Climbing Stairs


# T: O(n)
# S: O(n)
class Solution:
    def climbStairs(self, n):
        cache = {}

        def climbStairs_recur(n):
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            result = climbStairs_recur(n - 1) + climbStairs_recur(n - 2)
            cache[n] = result
            return result

        return climbStairs_recur(n)
