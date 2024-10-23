from typing import List
from collections import defaultdict


# T: O(n)
# S: O(1)
class Solution:
    def singleNumber(self, nums: List[int]):
        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]

            if nums[i] != nums[i + 1]:
                return nums[i]


# Hash Map
# T: O(n)
# S: O(n)
class Solution2:
    def singleNumber(self, nums: List[int]):
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for x in hashmap:
            if hashmap[x] == 1:
                return x


# Hash Map - defaultdict
# T: O(n)
# S: O(n)
class Solution3:
    def singleNumber(self, nums: List[int]):
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        for key in hashmap:
            if hashmap[key] == 1:
                return key


class Solution4:
    def singleNumber(self, nums: List[int]):
        a = 0
        for i in nums:
            a ^= i
        return a


# 같은 숫자를 두 번 XOR하면 0이 된다: x ^ x = 0
# 0과 숫자를 XOR하면 그 숫자가 그대로 남는다: 0 ^ x = x
"""
a ^= i <==> a = a ^ i

a = 5      # 5는 2진수로 0101
i = 3      # 3은 2진수로 0011

a    = 0101 (5)
i    = 0011 (3)
----------------
a ^ i = 0110 (6)

따라서, a ^= i는 a에 6을 저장
"""
