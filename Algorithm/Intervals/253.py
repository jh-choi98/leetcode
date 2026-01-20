import heapq
from typing import List
from collections import defaultdict

# Sweep Line Algorithm
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1

        curRooms = 0
        numRooms = 0
        for i in sorted(mp):
            curRooms += mp[i]
            numRooms = max(numRooms, curRooms)
        return numRooms

# Min Heap
# Time: O(nlogn)
# Space: O(n)
"""
To efficiently track room availability, we use a min heap:
    - the heap stores the end times of meetings currently occupying
      rooms
    - the smallest end time is always at the top, representing the room
      that frees up the earliest

As we process meetings in order of start time:
    - if the earliest-ending meeting finishes before the current one starts, we can reuse that room
    - otherwise, we must allocate a new room
    
The maximum size the heap reaches is the number of rooms needed.
"""
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution2:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        # We always need to know which meeting finishes earliest because
        # that is the first room that will become free. A min-heap
        # allows us to access the minimum element (the earliest end
        # time) in O(1) time
        
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap) # O(logn)
            heapq.heappush(min_heap, interval.end) # O(logn)
        
        return len(min_heap)

# Two Pointers
# Time: O(nlogn)
# Space: O(n)
"""
Instead of tracking whole intervals, we can separate the problem into
two simpler timelines:
    - one list of all start times
    - one list of all end times

If we process these timelines in order:
    - whenever a meeting starts before another one ends, we need a new
      room
    - whenever a meeting ends before or at the same time another starts,
      a room becomes free
    
By moving two pointers over the sorted start and end times, we can track
how many meetings are happening at the same time

The maximum number of simultaneous meetings at any moment is exactly the
number of rooms we need
"""
class Solution3:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

# Greedy
# Time: O(nlogn)
# Space: O(n)
"""
Instead of thinking in terms of rooms directly, we can think in terms of
events on a timeline:
    - when a meeting starts, we need one more room
    - when a meeting ends, one room is freed

So the problem reduces to:
    What is the maximum number of meetings happening at the same time?

If we track how the number of active meetings changes over time, the
maximum value we ever reach is exactly the number of rooms we need

This greedy approach works by:
    - converting each meeting into two events(start and end)
    - sorting all events by time
    - sweeping from left to right while counting active meetings
"""
class Solution4:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
            
        time.sort(key=lambda x: (x[0], x[1]))
        
        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res
