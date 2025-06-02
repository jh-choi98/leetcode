from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        offset = (10 ** 4)
        count_list = [0] * 2 * offset
        for num in nums:
            count_list[num + offset] += 1

        hm: dict[int, list[int]] = defaultdict(list)
        for i in range(len(count_list)):
            hm[count_list[i]].append(i - offset)

        res = []
        count_list.sort(reverse=True)
        j = 0
        m = k
        while m > 0:
            for num in hm[count_list[j]]:
                res.append(num)
                m -= 1
            j += len(hm[count_list[j]])
        return res

class Solution2:
    def topKFrequent(self, nums: List[int], k: int):
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(n) == k:
                    return res
