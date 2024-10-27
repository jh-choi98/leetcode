# Counting Bits

from typing import List


# 근본 없는 풀이
# T: O(nlogn)
# S: O(n)
class Solution:
    def countBits(self, n: int):
        memo = {}
        ans = []

        def find_cloest_power_of_two(n):
            power = 1
            while power * 2 < n:
                power *= 2
            return power

        def count(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            if n & (n - 1) == 0:
                memo[n] = 1
                return 1
            result = 1 + count(n - find_cloest_power_of_two(n))
            return result

        for i in range(n + 1):
            ans.append(count(i))
        return ans


# DP: bottom-up
# T: O(n)
# S: O(n)
# P(x) = P(x/2) + (x mod 2)
class Solution2:
    def countBits(self, n: int):
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = ans[i >> 2] + (i & 1)
            # i >> 1: i를 오른쪽으로 한 비트 시프트 (same as i // 2)
        return ans


# DP: bottom-up
# T: O(n)
# S: O(n)
# P(x) = P(x&(x−1)) + 1
class Solution3:
    def countBits(self, n: int):
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = ans[n & (n - 1)] + 1
            # n & (n - 1): n의 이진수에서 가장 오른쪽(LSB)에 있는 1을 제거
            # 1 한 개를 제외했으니 다시 1을 더해준다.
            # 이전 계산을 이용하기 위해서
