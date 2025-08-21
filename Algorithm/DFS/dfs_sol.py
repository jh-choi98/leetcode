# Example 1: DFS using Recursion (Most Common)
def dfs_recursive(graph, node, visited=None):
    """
    DFS traversal using recursion
    
    Args:
        graph: Dictionary where keys are nodes and values are lists of neighbors
        node: Current node being visited
        visited: Set of visited nodes
    
    Returns:
        List of nodes in DFS order
    """
    if visited is None:
        visited = set()
    
    visited.add(node)
    result = [node]
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


# Example 2: DFS using Stack (Iterative)
def dfs_iterative(graph, start):
    """
    DFS traversal using explicit stack
    
    Args:
        graph: Dictionary representation of graph
        start: Starting node
    
    Returns:
        List of nodes in DFS order
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()  # Pop from end (LIFO)
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add all unvisited neighbors to stack
            # Reverse to maintain left-to-right order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


# Example 3: DFS to Find Path Between Two Nodes
def dfs_find_path(graph, start, end, path=None):
    """
    Find a path between two nodes using DFS (not necessarily shortest)
    
    Args:
        graph: Dictionary representation of graph
        start: Starting node
        end: Target node
        path: Current path being explored
    
    Returns:
        Path from start to end, or None if no path exists
    """
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return path
    
    for neighbor in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
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
        path.pop()
        return None
    return _dfs_helper(start)


# Example 4: DFS to Find All Paths
def dfs_all_paths(graph, start, end, path=None):
    """
    Find all possible paths between two nodes using DFS
    
    Args:
        graph: Dictionary representation of graph
        start: Starting node
        end: Target node
        path: Current path being explored
    
    Returns:
        List of all possible paths from start to end
    """
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
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
    Preorder traversal of binary tree (Root → Left → Right)
    """
    if not root:
        return []
    
    result = [root.val]
    result.extend(dfs_tree_preorder(root.left))
    result.extend(dfs_tree_preorder(root.right))
    return result

def dfs_tree_inorder(root):
    """
    Inorder traversal of binary tree (Left → Root → Right)
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
    Postorder traversal of binary tree (Left → Right → Root)
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
    DFS traversal on a 2D grid/matrix
    
    Args:
        grid: 2D list representing the grid
        row, col: Current position
        visited: Set of visited positions
    
    Returns:
        Number of connected cells
    """
    if visited is None:
        visited = set()
    
    # Check boundaries and if cell is valid
    if (row < 0 or row >= len(grid) or 
        col < 0 or col >= len(grid[0]) or
        (row, col) in visited or
        grid[row][col] == 0):
        return 0
    
    visited.add((row, col))
    count = 1
    
    # Explore all 4 directions
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
                # Found a visited node that's not the parent
                return True
        
        return False
    
    # Check all components (graph might be disconnected)
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
    """
    visited = set()
    stack = []
    
    def dfs_topo(node):
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_topo(neighbor)
        
        # Add to stack after visiting all descendants
        stack.append(node)
    
    # Visit all nodes
    for node in graph:
        if node not in visited:
            dfs_topo(node)
    
    return stack[::-1]  # Reverse to get correct order


# Example 9: DFS with Backtracking (N-Queens Problem)
def solve_n_queens(n):
    """
    Solve N-Queens problem using DFS with backtracking
    
    Args:
        n: Size of the board (n x n)
    
    Returns:
        List of all possible solutions
    """
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def dfs_queens(board, row):
        if row == n:
            # Found a valid solution
            return [[''.join(row) for row in board]]
        
        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solutions.extend(dfs_queens(board, row + 1))
                board[row][col] = '.'  # Backtrack
        
        return solutions
    
    board = [['.' for _ in range(n)] for _ in range(n)]
    return dfs_queens(board, 0)


# Test Examples
if __name__ == "__main__":
    # Test Graph DFS
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS Recursive:", dfs_recursive(graph, 'A'))
    # Output: ['A', 'B', 'D', 'E', 'F', 'C']
    
    print("DFS Iterative:", dfs_iterative(graph, 'A'))
    # Output: ['A', 'B', 'D', 'E', 'F', 'C']
    
    print("Path A to F:", dfs_find_path(graph, 'A', 'F'))
    # Output: ['A', 'C', 'F'] or another valid path
    
    print("All paths A to F:", dfs_all_paths(graph, 'A', 'F'))
    # Output: All possible paths
    
    # Test Binary Tree DFS
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Preorder:", dfs_tree_preorder(root))   # [1, 2, 4, 5, 3]
    print("Inorder:", dfs_tree_inorder(root))     # [4, 2, 5, 1, 3]
    print("Postorder:", dfs_tree_postorder(root)) # [4, 5, 2, 3, 1]
    
    # Test Cycle Detection
    cyclic_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    print("Has cycle:", has_cycle(cyclic_graph))  # True
    
    # Test Topological Sort
    dag = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    print("Topological order:", topological_sort(dag))
    # Output: ['B', 'D', 'A', 'C', 'E', 'F'] or another valid order
