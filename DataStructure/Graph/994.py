from collections import deque
from typing import List

# 내 풀이 - Multi source BFS
# visited를 쓸 필요없음
# minutes = -1 로직 직관적이지 않음
# total oranges보다는 fresh oranges 개수 세는게 더 효율적
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        visited = set()
        total_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in (1, 2):
                    total_oranges += 1

                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.append((r, c))

        if total_oranges == 0:
            return 0

        minutes = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                total_oranges -= 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] == 1 and not (nr, nc) in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            minutes += 1
        return minutes if total_oranges == 0 else -1

# Multi-source BFS
# BFS에서 방문 처리는 반드시 큐에 넣는 순간 해야 한다
# Time: O(m * n)
# Space: O(m * n)
class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1
            
        return time if fresh == 0 else -1
