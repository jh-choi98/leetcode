import heapq
from typing import List

# Max Heap
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            largest = heapq.heappop(max_heap)
            second_largest = heapq.heappop(max_heap)
            if largest != second_largest:
                heapq.heappush(max_heap, largest-second_largest)
        return (-max_heap[0]) if max_heap else 0


# Binary Search
# Time: O(n^2)
# Space: O(1) or O(n)
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)
        
        while n > 1:
            cur = stones.pop() - stones.pop()
            n -= 2
            if cur > 0:
                l, r = 0, n
                while l < r:
                    mid = (l + r) // 2
                    if stones[mid] < cur:
                        l = mid + 1
                    else:
                        r = mid
                pos = l
                n += 1
                stones.append(0)
                for i in range(n - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = cur
        return stones[0] if n > 0 else 0
