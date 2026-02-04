from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        BFS in graph
        level search pattern
        starts from target
        """

        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1

        if "0000" == target:
            return 0

        num_map = {
            "0": ["9", "1"],
            "1": ["0", "2"],
            "2": ["1", "3"],
            "3": ["2", "4"],
            "4": ["3", "5"],
            "5": ["4", "6"],
            "6": ["5", "7"],
            "7": ["6", "8"],
            "8": ["7", "9"],
            "9": ["8", "0"],
        }

        visited = set()
        queue = deque(["0000"])
        visited.add("0000")
        turns = 0

        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                for i in range(4):
                    for j in range(2):
                        next_num = num[:i] + num_map[num[i]][j] + num[i+1:]
                        if next_num in visited:
                            continue
                        if next_num not in deadends_set:
                            queue.append(next_num)
                            visited.add(next_num)
                        if next_num == target:
                            return turns + 1
            turns += 1
        
        return -1

# BFS
# Time: O(d^n + m)
# Space: O(d^n)
# Where d is the number of digits, n is the number of wheels, and m is
# the number of deadends
class Solution2:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
            
        queue = deque([("0000", 0)])
        visited = set(deadends)
        
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))
                    
        return -1

# BFS
# Time: O(d^n + m)
# Space: O(d^n)
# Where d is the number of digits, n is the number of wheels, and m is
# the number of deadends
class Solution3:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        queue = deque(["0000"])
        visited.add("0000")
        steps = 0
        
        while queue:
            step += 1
            for _ in range(len(queue)):
                lock = queue.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        next_lock = lock[:i] + digit + lock[i + 1:]
                        if next_lock in visited:
                            continue
                        if next_lock == target:
                            return steps
                        queue.append(next_lock)
                        visited.add(next_lock)
        return -1

# Bidirectional BFS
"""
Standard BFS explores outward from the start, which can lead to
exploring many states before reaching a distant target. Bidirectional
BFS improves this by searching from both ends simultaneously: one
frontier starts at "0000" and another at the target. When they meet,
we've found the shortest path.

The key optimization is to always expand the smaller frontier. This
balances the search and reduces the total number of states explored,
especially when the search space branches heavily in one direction.
"""
class Solution4:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        begin = {"0000"}
        end = {target}
        steps = 0
        
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                
            step += 1
            temp = set()
            for lock in begin:
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        next_lock = lock[:i] + digit + lock[i+1:]
                        
                        if next_lock in end:
                            return steps
                        if next_lock in visited:
                            continue
                        visited.add(next_lock)
                        temp.add(next_lock)
            begin = temp
            
        return -1
