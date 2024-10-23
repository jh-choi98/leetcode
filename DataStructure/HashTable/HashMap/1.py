# Two Sum

from typing import List


# Hash Map: two pass
# T: O(n)
# S: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int):
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        return []


# Hash Map: one pass
class Solution2:
    def twoSum(self, nums: List[int], target: int):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []
