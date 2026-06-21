"""
- n by n
- win conditions:
    - row
    - col
    - one of the two diagnals
- tie
    - board filled and no winner

class Tictactoe
- board

- rows
- cols
- main_diag
- anti_diag
- moves_count

- winner

- _is_in_bound
- check_win

- make_move


"""

from typing import Optional


class TicTacToe:
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Invalid size")
        
        self.n = size
        
        self.board: list[list[Optional[str]]] = [[None for _ in range(size)] for _ in range(size)]
        self.rows = [0] * size
        self.cols = [0] * size
        self.main_diag = 0
        self.anti_diag = 0
        self.moves_count = 0
        
        self.winner = None
    
    def _is_in_bound(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n
    
    def _is_tie(self) -> bool:
        return (self.moves_count == (self.n * self.n) and self.winner is None)
    
    def check_win(self, row: int, col: int) -> bool:
        return (
            abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.main_diag) == self.n or 
            abs(self.anti_diag) == self.n
        )
        
    def make_move(self, row: int, col: int, player: str) -> str:
        if player not in ("X", "O"):
            raise ValueError("Invalid player")
        
        if self.winner is not None:
            raise ValueError("Game already over")
        
        if not self._is_in_bound(row, col):
            raise ValueError("Invalid move")
        
        if self.board[row][col] is not None:
            raise ValueError("This cell already occupied")
        
        value = 1 if player == "X" else 1
        
        self.board[row][col] = player
        self.rows[row] += value
        self.cols[col] += value
        self.moves_count += 1
        
        if row == col:
            self.main_diag += value
        
        if row + col == self.n - 1:
            self.anti_diag += value
            
        if self.check_win(row, col):
            self.winner = player
            return "WIN"
        
        if self._is_tie():
            return "TIE"
        
        return "ONGOING"
        
        
