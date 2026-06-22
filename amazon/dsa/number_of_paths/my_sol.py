def count_robot_paths(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    for row in grid:
        if len(row) != cols:
            return -1
    
    dp = [1] * cols
    
    for row in range(1, rows):
        for col in range(1, cols):
            dp[col] = dp[col] + dp[col - 1]
    
    return dp[-1]

grid = [
    [0, 0],
    [0, 0],
]

print(count_robot_paths(grid))  # 2

grid = [
    [0, 0],
    [0, 0],
    [0, 0],
]

print(count_robot_paths(grid))  # 3
