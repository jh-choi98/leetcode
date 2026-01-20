from collections import Counter, deque
import heapq
from typing import List

# Max Heap
# Time: O(m), where m is the number of tasks
# Space: O(1)
"""
- Keep a max-heap of tasks by their remaining count (most frequent on
  top)
- At each time unit, we take the most frequent available task and run it
- After running a task, it goes into a cooldown queue with the time when
  it will be available again (current time + n)
- When a task's cooldown finishes, we push it back into the heap so it
  canbe scheduled again
- If the heap is empty but some tasks are still in cooldown, we can jump
  the current time forward to the next time when a task becomes available
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        max_heap = [-freq for freq in frequencies.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_queue = deque() # pairs of [-cnt, idleTime]
        while max_heap or cooldown_queue:
            time += 1

            if not max_heap:
                time = cooldown_queue[0][1]
            else:
                freq = 1 + heapq.heappop(max_heap) # 작업을 하나 처리했으니 개수를 줄인다. (cnt는 음수. 그래서 +1을 해야 숫자가 줄어듦)
                if freq:
                    cooldown_queue.append([freq, time + n])

            if cooldown_queue and cooldown_queue[0][1] == time: # 휴게실에서 복귀
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
        return time

# Greedy
# Time: O(m), where m is the number of tasks
# Space: O(1)
"""
The task with the highest frequency determines the minimum needed
structure of the schedule

Total Time = len(tasks) + idle_slots

- Basically, the most frequent task sets the lower bound because of the
  mandatory cooling intervals
- Use the other tasks to fill up the idle slots. If they overflow, the schedule just naturally gets longer
"""
class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        
        frequencies.sort()
        
        max_freq = frequencies[25]
        idle_slots = (max_freq - 1) * n
        
        for i in range(24, -1, -1):
            idle_slots -= min(max_freq - 1, frequencies[i])
            
        return max(0, idle_slots) + len(tasks)
        
# Math
# Time: O(m), where m is the number of tasks
# Space: O(1)
"""
The task with the highest frequency determines the minimum needed
structure of the schedule

If a task appears max_freq times, these copies must be at least n units
apart

This creates (max_freq - 1) gaps, and each gap must have a length of (n
+ 1) slots (the task itself + n cooldowns)

If multiple tasks share this maximum frequency (maxCount tasks), they
all occupy the final row of the structure

So the minimal time required to schedule all tasks without violating
cooldown rules is: 
    (max_freq - 1) * (n + 1) + maxCount

However, if the number of tasks is larger than this calculated time,
then simply performing all tasks takes longer

Thus, the actual answer must be: max(len(tasks), time)
"""
class Solution3:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        
        max_freq = max(frequencies)
        max_count = 0
        for freq in frequencies:
            max_count += 1 if freq == max_freq else 0

        time = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), time)
