from typing import List

# Linear Search
# Time: O(n)
# Space: O(1)
"""
1. Intervals completely before newInterval
    These do not overlap, so we can add them directly to the result.
2. Intervals that overlap with newInterval
    - While there is overlap, we merge them by expanding newInterval:
        - new start = minimum of starts
        - new end = maximum of ends
3. Intervals completely after the merged newInterval
    These also do not overlap, so we add them directly.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []
        
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

# Binary Search
# Time: O(n)
# Space: O(1)
"""
1. Use binary search to find the correct position where newInterval should be inserted based on its start time.
2. After inserting, the list is still sorted by start time.
3. Then we do a normal merge intervals pass:
    - if the current interval does not overlap the last interval in the result, append it
    - otherwise merge them by extending the end
    
Binary search helps us avoid scanning from the beginning just to find the insertion position
"""
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        intervals.insert(left, newInterval)
        
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# Greedy
"""
A greedy approach works because as we scan from left to right, every
interval falls into one of three cases relative to newInterval:
1. Completely after newInterval
    - If newInterval ends before the current interval starts, there will be no overlap with any later interval either.
    - So we can safely place newInterval here and return the answer immediately.
2. Completely before newInterval
    - If the current interval ends before newInterval starts, it can be added to the result unchanged.
3. Overlapping with newInterval
    - If they overlap, we merge them by expanding newInterval to cover
      both ranges

By continuously merging when needed and stopping early when newInterval is placed, we solve it in one pass
"""
class Solution3:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
