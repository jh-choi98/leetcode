from typing import Optional


class TicTacToe:
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Board size must be positive")
        
        self.n = size
        
        # Board is needed to validate whether a cell is already occupied
        self.board: list[list[Optional[str]]] = [[None for _ in range(size)] for _ in range(size)]
        
        # Counter-based optimization for O(1) win checking
        self.rows = [0] * size
        self.cols = [0] * size
        self.main_diag = 0
        self.anti_diag = 0
        
        self.moves_count = 0
        self.winnder = None
        
    def make_move(self, row: int, col: int, player: str) -> str:
        if player not in ("X", "O"):
            raise ValueError("Player must be either X or O")
        
        if self.winnder is not None:
            raise ValueError("Game is already over")
        
        if not self._is_in_bounds(row, col):
            raise ValueError("Move is outside the board")
        
        if self.board[row][col] is not None:
            raise ValueError("Cell is already occupied")
        
        self.board[row][col] = player
        self.moves_count += 1
        
        value = 1 if player == "X" else -1
        
        self.rows[row] += value
        self.cols[col] += value
        
        if row == col:
            self.main_diag += value
            
        if row + col == self.n - 1:
            self.anti_diag += value
            
        if self.check_win(row, col):
            self.winner = player
            return "WIN"
        
        if self.is_tie():
            return "TIE"
        
        return "ONGOING"
    
    def check_win(self, row: int, col: int) -> bool:
        return (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.main_diag) == self.n
            or abs(self.anti_diag) == self.n
        )
        
    def is_tie(self) -> bool:
        return self.moves_count == self.n * self.n and self.winner is None
    
    def _is_in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n

