from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
   
# DFS
# Time: O(V + E)
# Space: O(V)   
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)

# BFS
# Time: O(V + E)
# Space: O(V)  
class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            cur = queue.popleft()
            for nei in node.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                old_to_new[cur].neighbors.append(old_to_new[nei])
                
        return old_to_new[node]
