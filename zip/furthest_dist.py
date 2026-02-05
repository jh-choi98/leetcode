"""
if cur_building >= next_building -> can move
else:
    sandbags -> diff = next - cur
    or 
    spring  -> 1
    
    
    
Greedy + MinHeap

use spring first

after using all springs

replace the used spring to sandbags

to keep the number of sandbags to be replace
-> minHeap

Time: O(Llogn) where L is the number of buildings, n is the nubmer of
springs
Space: O(n) where n is the number of springs used
"""

import heapq
from typing import List


def find_farthest_point(heights: List[int], n: int, m: int) -> int:
    min_heap = []
    
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        
        heapq.heappush(min_heap, diff)
        if len(min_heap) > n:
            m -= heapq.heappop(min_heap)
            if m < 0:
                return i
    
    return len(heights) - 1
        

"""
I considered using Dynamic Programming, but the state space would be too
large.
If we define the state as dp[index][springs_remaining], the time
complexity becomes O(L * N), where L is the number of buildings and N is
the number of springs.
Since N can be as large as L, this results in an O(L^2) complexity.
In contrast, the Min-Heap approach runs in O(Llog N), which is much more
efficient for large inputs.
"""
