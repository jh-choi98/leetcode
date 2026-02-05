from collections import deque
from typing import List

# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        start = (0, 0)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '*':
                    start = (r, c)
                    grid[r][c] = "T"
                    break

        length = 0
        queue = deque([start])
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or 
                    nr >= ROWS or nc >= COLS or 
                    grid[nr][nc] == "X" or grid[nr][nc] == "T"):
                        continue
                    
                    if grid[nr][nc] == "#":
                        return length + 1

                    queue.append((nr, nc))
                    grid[nr][nc] = "T"
            length += 1

        return -1
