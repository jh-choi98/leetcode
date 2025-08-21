# Example 1: DFS using Recursion
def dfs_recursive(graph, node, visited=None):
    """
    Args:
        graph: Dictionary where keys are nodes and values are lists of
        neighbors
        node: Current node being visited
        visited: Set of visited nodes
        
    Returns:
        List of nodes in DFS order
        
    T: O(V + E)
    S: O(V)
    """
    if not visited:
        visited = set()
        
    visited.add(node)
    result = [node]
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
            
    return result


# Example 2: DFS using Stack (Iterative)
def dfs_iterative(graph, start):
    """
    Returns:
        List of nodes in DFS order
        
    T: O(V + E)
    S: O(V)
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Reverse to maintain left-to-right order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return result

# Example 3: DFS to Find Path Between Two Nodes (not necessarily shortest)
def dfs_find_path(graph, start, end, path=None):
    """
    Returns:
        Path from start to end, or None if no path exists
        
    T: O(V + E)
    S: O(V^2). Copy overhead for path is huge (1 + 2 + ... + k = O(K^2))
    """
    if not path:
        path = []
        
    path = path + [start]
    
    if start == end:
        return path
    
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs_find_path(graph, neighbor, end, path)
            if new_path:
                return new_path
    
    return None

def dfs_find_path_optimized(graph, start, end, path=None):
    visited = set()
    path = []
    
    def _dfs_helper(cur_node):
        path.append(cur_node)
        visited.add(cur_node)
        
        if cur_node == end:
            return list(path)
        
        for neighbor in graph.get(cur_node, []):
            if neighbor not in visited:
                result = _dfs_helper(neighbor)
                if result:
                    return result    
        path.pop() # 목표 노드를 찾지 못했을 때 해당 노드 제거
        return None
    
    return _dfs_helper(start)
        
# Example 4: DFS to Find All Paths
def dfs_all_paths(graph, start, end, path=None):
    """
    BFS는 최단 경로 탐색에는 유리하지만, 모든 경로를 나열하려면 큐에
    너무 많은 경로를 동시에 저장해야해서 비효율적이다 -> DFS
    
    Returns:
        List of all possible paths from start to end
    """
    if not path:
        path = []
        
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_paths = dfs_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)
            
    return paths
    
        
def dfs_all_paths_optimized(graph, start, end):
    all_paths = []
    path = []
    visited = set()
    
    def _dfs_util(node):
        path.append(node)
        visited.add(node)
        
        if node == end:
            all_paths.append(list(path))
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    _dfs_util(neighbor)
        path.pop()
        visited.remove(node)
        
    _dfs_util(start)
    return all_paths

# Example 5: DFS on Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def dfs_tree_preorder(root):
    """
    Preorder: Root -> Left -> Right
    """
    if not root:
        return []
    
    result = [root.val]
    result.extend(dfs_tree_preorder(root.left))
    result.extend(dfs_tree_preorder(root.right))
    return result

def dfs_tree_inorder(root):
    """
    Inorder: Left -> Root -> Right
    """
    if not root:
        return []
    
    result = []
    result.extend(dfs_tree_inorder(root.left))
    result.append(root.val)
    result.extend(dfs_tree_inorder(root.right))
    return result

def dfs_tree_postorder(root):
    """
    Postorder: Left -> Right -> Root
    """
    if not root:
        return []
    
    result = []
    result.extend(dfs_tree_postorder(root.left))
    result.extend(dfs_tree_postorder(root.right))
    result.append(root.val)
    return result

# Example 6: DFS on 2D Grid
def dfs_grid(grid, row, col, visited=None):
    """
    DFS traversal on a 2D grid
    
    Args:
        grid: 2D list representing the grid
        row, col: Current position
        visited: Set of visited positions
        
    Returns:
        Number of connected cells
    """
    if not visited:
        visited = set()
        
    if (row < 0 or row >= len(grid) or
        col < 0 or col >= len(grid[0]) or
        (row, col) in visited or
        grid[row][col] == 0): # Assuming 0 means not accessible
        return 0
    
    visited.add((row, col))
    count = 1
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dr, dc in directions:
        count += dfs_grid(grid, row + dr, col + dc, visited)
        
    return count
    
# Example 7: DFS for Cycle Detection
def has_cycle(graph):
    """
    Detect if an undirected graph has a cycle using DFS
    
    Args:
        graph: Dictionary representation of undirected graph
    
    Returns:
        True if cycle exists, False otherwise
    """
    visited = set()
    
    def dfs_cycle(node, parent):
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs_cycle(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
            
        return False
    
    for node in graph:
        if node not in visited:
            if dfs_cycle(node, None):
                return True
            
    return False

# Example 8: DFS for Topological Sort
def topological_sort(graph):
    """
    Topological sorting using DFS (for DAG - Directed Acyclic Graph)
    
    Args:
        graph: Dictionary representation of directed graph
    
    Returns:
        List of nodes in topological order
        
    Topological sort (위상 정렬)
    : an ordering of the vertices in a DAG s.t. for every directed edge
    u -> v, u comes before v in the ordering
    => it produces a linear order of tasks that respects dependency constraints    
    """
    visited = set()
    stack = []
    
    def dfs_topo(node):
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_topo(neighbor)
        
        stack.append(node)
        
    for node in graph:
        if node not in visited:
            dfs_topo(node)
            
    return stack[::-1]
        
# Example 9: DFS with Backtracking (N-Queens Problem)
def solve_n_queens(n):
    """
    N-Queens problem
    : Place N queens on an N × N chessboard s.t. no two queens attack each other.
    
    Args:
        n: Size of the board
        
    Returns:
        List of all possible solutions
    """
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
            
        return True
            
    def dfs_queens(board, row):
        if row == n:
            return [[''.join(r) for r in board]]
        
        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solutions.extend(dfs_queens(board, row + 1))
                board[row][col] = '.' # Backtrack
        return solutions
                
    board = [['.' for _ in range(n)] for _ in range(n)]
    return dfs_queens(board, 0)
    
