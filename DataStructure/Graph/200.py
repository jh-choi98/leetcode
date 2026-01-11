from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            grid[r][c] = '0'

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
        return count
