# Minimum Index Sum of Two Lists
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        output_hash = {}
        ans = []

        for i in range(len(list1)):
            hashmap[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in hashmap:
                hashmap[list2[j]] += j
                output_hash[list2[j]] = hashmap[list2[j]]

        min_index = len(list1) + len(list2)
        # min_index = float("inf")
        for x in output_hash:
            if min_index > output_hash[x]:
                ans = []
                min_index = output_hash[x]
                ans.append(x)
            elif min_index == output_hash[x]:
                ans.append(x)

        return ans
