import heapq
from typing import List

# nums의 모든 숫자를 다 가지고 있다. 하지만 이 문제의 요구사항은 k번째로
# 큰 숫자만 보여달라는 것. 그래서 이 구현은 효율적이지 못함. 만약 모든
# 숫자를 다 보관하는 것이 필요했다면 다른 data structure를 사용했을 것
# Time: O(nlogk)
# Space: O(n)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.target = k
        heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        kth_largest_num = heapq.nlargest(self.target, self.nums)[-1]
        return kth_largest_num

# Sorting
# Time: O(nlogn)
# Space: O(n)
class KthLargest2:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
    
    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]

# Min-Heap
# Time: 
#   - __init__: O(nlogn)
#   - add: O(logk)
# Space: O(k)
class KthLargest3:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(logk)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(logk)
        return self.minHeap[0] # O(1)
