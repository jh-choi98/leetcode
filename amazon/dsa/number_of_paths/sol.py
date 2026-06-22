# Grid DP
"""
    n = number of rows
    m = number of columns
    
    - Time: O(n * m)
        We visit each cell once conceptually, and for each cell we do
        constant work: we add the number of ways from the top and the
        left
        
    - Space: O(m)
        Instead of storing a full n by m DP table, we only keep one row
        of DP values. The input grid itself takes O(n * m) space, but
        the extra space used by the algorithm is O(m)
"""
def count_robot_paths(grid: list[list[int]]) -> int:
    """
        I'll first handle an empty grid. If there is no valid start or
        destination cell, there are no paths
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    """
        I'll assume the grid should be rectangular. If one row has a
        different length, the input is valid
    """
    for row in grid:
        if len(row) != cols:
            raise ValueError("Grid must be rectangular")
        
    """
        Since there are no obstacles, every cell in the first row has
        exactly one way to reach it: keep moving right
        
        dp[col] represents the number of ways to reach the current row
        at column col
    """
    dp = [1] * cols
    
    """
        For the rest of the grid, each cell can be reached from the top
        or from the left. In this 1D DP array, dp[col] is the value from
        the top, and dp[col - 1] is the value from the left
    """
    for row in range(1, rows):
        for col in range(1, cols):
            dp[col] = dp[col] + dp[col - 1]
            # dp[col] = 위에서 내려오는 경로의 수
            # dp[col - 1] = 왼쪽에서 오는 경로의 수
    
    return dp[-1]

# --------------------------------------
# Follow-up: obstacles 있으면?
# --------------------------------------
def count_robot_paths2(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows = len(grid)
    cols = len(grid[0])
    
    for row in grid:
        if len(row) != cols:
            return -1
    
    # If the start or destination is blocked, there is no valid path
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return 0
    
    dp = [0] * cols
    dp[0] = 1
    
    """
        I'll still use DP. For each cell, if it is an obstacle, the
        number of ways to reach it is 0. Otherwise, it is the sum of
        ways from the top and from the left
    """
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # An obstacle blocks all paths through this cell
                dp[col] = 0
            else:
                if col > 0:
                    dp[col] = dp[col] + dp[col - 1]
                    
    return dp[-1]

grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

print(count_robot_paths2(grid))  # 2
