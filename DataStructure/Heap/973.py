from collections import defaultdict
import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_distance_from_origin(x, y):
            return math.sqrt((x)**2 + (y)**2)

        dist_coord_map = defaultdict(list)
        dist_min_heap = []
        for i in range(len(points)):
            dist = cal_distance_from_origin(points[i][0], points[i][1])
            heapq.heappush(dist_min_heap, dist)
            dist_coord_map[dist].append(points[i])
        
        res = []
        while k > 0:
            cur_dist = heapq.heappop(dist_min_heap)
            cur_coords = dist_coord_map[cur_dist]
            res.extend(cur_coords)
            k -= len(cur_coords)
        return res

# Sorting
# Time: O(nlogn)
# Space: O(1)
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]

# Min Heap
# Time: O(n + klogn)
# Space: O(n)
class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points: # O(n)
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist, x, y])
        heapq.heapify(min_heap) # O(n)
        res = []
        while k > 0: # O(klogn)
            dist, x, y = heapq.heappop(min_heap) # O(logn)
            res.append([x, y])
            k -= 1
        return res

# Max Heap
# Time:O(nlogk)
# Space: O(k)
class Solution4:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(max_heap, [dist, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        while max_heap:
            dist, x, y = heapq.heappop(max_heap)
            res.append([x, y])
        return res
