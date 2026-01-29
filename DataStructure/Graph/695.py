from collections import deque
from typing import List

# My Solution (with AI correction) - DFS
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        max_area = 0

        def dfs(r: int, c: int) -> int:
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area

# BFS
# Time: O(m * n)
# Space: O(m * n)
class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        
        def bfs(r, c):
            queue = deque([(r,c)])
            grid[r][c] = 0
            res = 1
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 0
                        res += 1
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
                
        return area

# DFS
# Time: O(m * n)
# Space: O(m * n)
class Solution3:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit):
                return 0
        
            visit.add((r, c))
            
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))
        return max_area
