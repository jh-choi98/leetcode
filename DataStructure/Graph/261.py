"""
A graph is a valid tree if:
    - It has no cycles
    - It is fully connected
"""

# Cycle Detection (DFS)
# adjacent list with list
# Time: O(V + E)
# Space: O(V + E)
"""
Using DFS, we can detect cycles by checking if we visit a node again
from a path other than its parent

Also, a tree with n nodes must have exactly n - 1 edges, otherwise it's valid
"""
from collections import deque
from doctest import TestResults
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        

# Cycle Detection (DFS)
# adjacent list with dictionary
class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        graph = {i: [] for i in range(n)}
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
            
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n
    
# BFS
# Time: O(V + E)
# Space: O(V + E)
"""
Using BFS, we traverse the graph level by level.

If we ever reach a node that was already visited (and is not the parent)
→ a cycle exists. After BFS, if all nodes are visited, the graph is
connected

Also, a tree with n nodes can have at most n - 1 edges
"""
class Solution3:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1: 
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visit = set()
        q = deque([(0, -1)])
        visit.add(0)
        
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
                
        return len(visit) == n

# Disjoint Set Union
# Time: O(V + (E * a(V)))
# Space: O(V)
"""
Using Disjoint Set Union (Union-Find):
- Each node starts in its own component
- When we connect two nodes:
    - If they are already in the same component, adding this edge creates a cycle
    - Otherwise, we merge their components
- In the end, a valid tree must have exactly one connected component

Also, a tree with n nodes can have at most n - 1 edges.


Algorithm
1. If number of edges > n - 1, return false
2. Initialize DSU with n components
3. For each edge (u, v):
    If union(u, v) fails → cycle detected → return false
4. After processing all edges:
    Check if number of components is 1.
5. Return true if only one component exists, else false
"""
class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)
    
    # 무조건 루트를 반환 
    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        
        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True
    
    def components(self):
        return self.comps
        
        
class Solution4:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1
