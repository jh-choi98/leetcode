import heapq
from typing import List

# Max Heap
# Time: O(n + klogn)
# Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        
        return -(heapq.heappop(max_heap))

# Min Heap
# Time: O(n + (n - k)O(logn))
# Space: O(1)
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        i = len(nums) - k
        while i > 0:
            heapq.heappop(nums)
            i -= 1
        return heapq.heappop(nums)
