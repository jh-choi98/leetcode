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

        
    