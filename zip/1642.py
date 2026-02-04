import heapq
from typing import List

# Max-heap
# Time: O(nlogn)
# Space: O(n)
"""
We can make greedy decisions as we traverse by initially using bricks
for each jump, then retroactively swapping to a ladder when bricks run
out. A max-heap tracks all brick usages so far, allowing us to
efficiently swap the largest brick usage with a ladder when needed. This
ensures ladders always cover the biggest gaps
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff < 0:
                continue
            
            bricks -= diff
            heapq.heappush(heap, -diff) # O(logn)
            
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap) # O(logn)
                
        return len(heights) - 1
            

# Min-heap
# Time: O(logn)
# Space: O(logn)
"""
Instead of tracking brick usages, we can track ladder usages in a
min-heap. We greedily assign ladders to each jump, but once we've used
more than the allowed number of ladders, we convert the smallest ladder
usage back to bricks. This way, ladders always end up covering the
largest jumps

"""
class Solution2:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
                
            heapq.heappush(min_heap, diff)
            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)
                if bricks < 0:
                    return i
                
        return len(heights) - 1
                