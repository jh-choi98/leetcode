from collections import deque

# Example 1: BFS on a Graph (Adjacency List)
def bfs_graph(graph, start):
    """
    BFS traversal on a graph represented as adjacency list
    
    Args:
        graph: Dictionary where keys are nodes and values are lists of neighbors
        start: Starting node for BFS
    
    Returns:
        List of nodes in BFS order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Explore all neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


# Example 2: BFS to Find Shortest Path
def bfs_shortest_path(graph, start, end):
    """
    Find shortest path between two nodes using BFS
    
    Args:
        graph: Dictionary representation of graph
        start: Starting node
        end: Target node
    
    Returns:
        Shortest path as a list, or None if no path exists
    """
    if start == end:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                
                if neighbor == end:
                    return new_path
                
                visited.add(neighbor)
                queue.append((neighbor, new_path))
    
    return None  # No path found


# Example 3: BFS on a Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_tree_level_order(root):
    """
    Level-order traversal of binary tree using BFS
    
    Args:
        root: Root node of binary tree
    
    Returns:
        List of lists, where each inner list contains nodes at that level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


# Example 4: BFS on a 2D Grid (Matrix)
def bfs_grid(grid, start_row, start_col):
    """
    BFS traversal on a 2D grid/matrix
    
    Args:
        grid: 2D list representing the grid
        start_row, start_col: Starting position
    
    Returns:
        Number of cells visited
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col)])
    visited.add((start_row, start_col))
    
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count = 0
    
    while queue:
        row, col = queue.popleft()
        count += 1
        
        # Explore all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check boundaries and if not visited
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited and
                grid[new_row][new_col] == 1):  # Assuming 1 means accessible
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
    
    return count


# Example 5: BFS to Find Distance to All Nodes
def bfs_all_distances(graph, start):
    """
    Find shortest distance from start node to all other nodes
    
    Args:
        graph: Dictionary representation of graph
        start: Starting node
    
    Returns:
        Dictionary with distances to all reachable nodes
    """
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    
    return distances


# Test Examples
if __name__ == "__main__":
    # Test Graph BFS
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("BFS Traversal:", bfs_graph(graph, 'A'))
    # Output: ['A', 'B', 'C', 'D', 'E', 'F']
    
    print("Shortest Path A to F:", bfs_shortest_path(graph, 'A', 'F'))
    # Output: ['A', 'C', 'F']
    
    print("Distances from A:", bfs_all_distances(graph, 'A'))
    # Output: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}
    
    # Test Binary Tree BFS
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Level Order Traversal:", bfs_tree_level_order(root))
    # Output: [[1], [2, 3], [4, 5]]
    
    # Test Grid BFS
    grid = [
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Cells visited from (0,0):", bfs_grid(grid, 0, 0))
    # Output: 4 (visits cells connected to starting position)
