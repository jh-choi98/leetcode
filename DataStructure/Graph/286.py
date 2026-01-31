from collections import deque
from typing import List

# Multi Source BFS
# Time: O(m * n)
# Space: O(m * n)
"""
Instead of running BFS from every empty room, run BFS once starting from
all treasures (0 cells) at the same time

** Common Pitfalls **
Starting BFS from Empty Rooms Instead of Treasures
: A common mistake is to run BFS from each empty room to find the
nearest treasure, resulting in O((m * n) ^ 2) time complexity. The optimal
approach is multi-source BFS starting from all treasures simultaneously,
which processes each cell exactly once.
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def addCell(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            queue.append([r, c])
            
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        