from collections import deque
from typing import List

# BFS (multi-source + 가장자리 시작)
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque()
        visited = set()
        
        for r in range(ROWS):
            if board[r][0] == 'O' and not (r, 0) in visited:
                queue.append((r, 0))
                visited.add((r, 0))
            
            if board[r][COLS - 1] == 'O' and not (r, COLS - 1) in visited:
                queue.append((r, COLS - 1))
                visited.add((r, COLS - 1))
            
        for c in range(COLS):
            if board[0][c] == 'O' and not (0, c) in visited:
                queue.append((0, c))
                visited.add((0, c))
            
            if board[ROWS - 1][c] == 'O' and not (ROWS - 1, c) in visited:
                queue.append((ROWS - 1, c))
                visited.add((ROWS - 1, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    board[nr][nc] == 'O' and 
                    (nr, nc) not in visited):
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'

# BFS (multi-source + 가장자리 시작)
# Time: O(m * n)
# Space: O(1)
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if ((r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O'):
                    queue.append((r, c))
                    board[r][c] = "T"
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    board[nr][nc] == 'O'):
                    board[nr][nc] = 'T'
                    queue.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

# DFS
# Time: O(m * n)
# Space: O(m * n)
class Solution3:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            
        for r in range(ROWS):
            if board[r][0] == 'O':
                capture(r, 0)
            if board[r][COLS - 1] == 'O':
                capture(r, COLS - 1)
                
        for c in range(COLS):
            if board[0][c] == 'O':
                capture(0, c)
            if board[ROWS - 1][c] == 'O':
                capture(ROWS - 1, c)
                
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
