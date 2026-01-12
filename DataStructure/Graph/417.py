from collections import deque
from typing import List

# Brute Force
# Starting DFS from every cell (slow)
# Time: O(m * n * 4^(m * n))
# Space: O(m * n)
"""
For every (r, c):
- Run DFS exploring all paths that keep going to same or lower heights
- If during DFS we ever step out of the grid:
    - Out of top/left boundary ⇒ it can reach the Pacific
    - Out of bottom/right boundary ⇒ it can reach the Atlantic
- If both oceans are reachable, include (r, c) in the answer

To avoid infinite loops, we temporarily mark the current cell as visited (here by setting it to inf) while exploring, then restore it after backtracking
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        pacific = atlantic = False
        
        def dfs(r, c, prevVal):
            nonlocal pacific, atlantic
            if r < 0 or c < 0:
                pacific = True
                return
            if r >= ROWS or c >= COLS:
                atlantic = True
                return
            if heights[r][c] > prevVal:
                return
            
            tmp = heights[r][c]
            heights[r][c] = float('inf')
            for dx, dy in directions:
                dfs(r + dx, c + dy, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res

# DFS
# Time: O(m * n)
# Space: O(m * n)
"""
Start from the ocean borders and move uphill/flat (to neighbors with
height >= current)

So, we do 2 DFS runs:
    - From all Pacific border cells (top row + left column) → mark all reachable cells in pac
    
    - From all Atlantic border cells (bottom row + right column) → mark all reachable cells in atl
    
Answer = cells that are in both sets
"""
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

# BFS
# Time: O(m * n)
# Space: O(m * n)
class Solution3:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
