from collections import defaultdict
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        n = len(intervals)
        i = 0
        res = []
        prev = None

        while i < n:
            if not res or i == 0:
                res.append(intervals[i])
                i += 1
                continue
            
            prev = res[-1]
            if intervals[i][0] <= prev[1]:
                prev[1] = max(intervals[i][1], prev[1])
            else:
                res.append(intervals[i])
            i += 1

        return res

# Sorting
# Time: O(n * log(n))
# Space: O(1)
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        
        for start, end in intervals:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

# Sweep Line Algorithm
# Time: O(n * log(n))
# Space: O(n)
"""
This approach treats each interval as a pair of events on a number line:
    - An interval starts at start
    - An interval ends at end

Instead of merging intervals directly, we track how many intervals are
currently active as we move from left to right along with the number
line

The key idea:
    - when the number of active intervals goes from 0 -> positive, a
      merged interval starts
    - when it goes from positive -> 0, a merged interval ends

By recording how the count changes at each boundary and sweeping through
them in order, we can reconstruct all merged intervals
"""
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
            
        res = []
        interval = []
        have = 0
        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res
    
# Greedy
# Time: O(n + m)
# Space: O(n)
# where n is the length of the array and m is the maximum start value
# among all the intervals
class Solution4:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res
