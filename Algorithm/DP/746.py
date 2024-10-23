from typing import List


# DP: Bottom-up (Tabulation)
# T: O(n)
# S: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


# DP: Bottom-up (Tabulation)
# T: O(n)
# S: O(n)
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]):
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        min_cost = [0] * (len(cost) + 1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, len(cost) + 1):
            one_step = min_cost[i - 1] + cost[i - 1]
            two_step = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[-1]


# DP: Top-down (Recursion + Memoization)
# T: O(n)
# S: O(n)
class Solution3:
    def minCostClimbingStairs(self, cost: List[int]):
        def climb(i):
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0

            # Check if we have already calculated climb(i)
            if i in memo:
                return memo[i]

            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + climb(i - 1)
            down_two = cost[i - 2] + climb(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return climb(len(cost))
