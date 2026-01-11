# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        new_root = Node(node.val)
        queue = deque([(node, new_root)])
        visited = {node: new_root}

        while queue:
            cur_node, new_node = queue.popleft()
            for n in cur_node.neighbors:
                n_copy = visited.get(n)
                if not n_copy:
                    n_copy = Node(n.val)
                    visited[n] = n_copy
                    queue.append((n, n_copy))
                new_node.neighbors.append(n_copy)
        return new_root

# BFS
# Time complexity: O(V + E)
# Space complexity: O(V)
class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not Node:
            return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        queue = deque([node])
        
        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    queue.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])
                
        return oldToNew[node]    

# DFS
# Time complexity: O(V + E)
# Space complexity: O(V)
class Solution3:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
