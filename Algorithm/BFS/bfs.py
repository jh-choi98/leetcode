from collections import deque

# Example 1: BFS on a Graph (Adjacency List)
def bfs_graph(g, start):
    """
    BFS traversal on a graph represented as adjacency list
    
    Args:
        g: Dictionary where keys are nodes and values are lists of
        neighbors
        start: Starting node for BFS
        
    Returns:
        List of nodes in BFS order
        
    T: O(V + E)
    S: O(V)
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in g.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return result


# Example 2: BFS to Find Shortest Path
def bfs_shortest_path(g, start, end):
    """
    Find shortest path between two nodes using BFS
    
    Returns:
        Shortest path as a list, or None if no path exists
        
    T: O(V^2 + E) in worst case
        탐색 자체는 O(V+E)지만, new_path = path + [neighbor]가 길이
        O(경로길이)만큼 매번 복사된다. 최악에서는 경로 길이들의 합이 O(V^2)까지 커질 수 있어 전체가
        O(V^2 + E)가 된다.
    S: O(V^2) in worst case 
        visited is O(V), but the queue stores many (node, path) pairs, and those path lists can collectively occupy O(V^2) space in the worst case
    """
    if start == end:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in g.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                
                if neighbor == end:
                    return new_path
                
                visited.add(neighbor)
                queue.append((neighbor, new_path))
    return None

# Better version
def bfs_shortest_path2(g, start, end):
    """
    Problem: the previous version is inefficient because new_path = path
    + [neighbor] copies the entire path list for every new node it
    explores. This degrades the performance to O(V^2) for both time and
    space complexity
    
    Soltuion:
        - Store only nodes in the queue
            The queue should only contain the nodes to visit, not the
            entire path to them
        - Use a predecessor map: A dict is used to keep track of the
          path
        - Reconstruct the path
            After the BFS finds the end node, work backward from end to
            start using the map to build the shortest path
    T: O(V + E)
    S: O(V)
    """
    if start == end:
        return [start]
    
    queue = deque([start])
    visited = set([start])
    
    # A dictionary to store the path history
    predecessors = {start: None}
    
    path_found = False
    while queue:
        node = queue.popleft()
        
        if node == end:
            path_found = True
            break
        
        for neighbor in g.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessors[neighbor] = node
                queue.append(neighbor)
                
    if path_found:
        path = []
        cur = end
        while cur:
            path.append(cur)
            cur = predecessors[cur]
        return path[::-1]
    
    return None
            
# Example 3: BFS on a Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def bfs_tree_level_order(root):
    """
    Returns:
        List of lists, where each inner list contains nodes at that
        level
        
    T: O(V + E)
    S: O(V)
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        cur_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            cur_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(cur_level)
    
    return result
            
# Example 4: BFS on a 2D Grid (Matrix)
def bfs_grid(grid, start_row, start_col):
    """
    Returns:
        Number of cells visited
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col)])
    visited.add((start_row, start_col))
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count = 0
    
    while queue:
        row, col = queue.popleft()
        count += 1
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_coord = (new_row, new_col)
            
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                new_coord not in visited and
                grid[new_row][new_col] == 1): # Assuming 1 means accessible
                visited.add(new_coord)
                queue.append(new_coord)
                
    return count
    
# Example 5: BFS to Find Distance to All Nodes
def bfs_all_distances(graph, start):
    """
    Find shortest distance from start node to all other nodes
    
    Returns:
        Dictionary with distances to all reachable nodes
    """
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        cur_distance = distances[node]
        
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = cur_distance + 1
                queue.append(neighbor)
                
    return distances

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
