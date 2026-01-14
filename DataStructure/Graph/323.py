from collections import deque
from typing import List

# BFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0

        for node in range(n):
            if node not in visited:
                count += 1
                visited.add(node)
                q = deque([node])
                while q:
                    cur = q.popleft()
                    for nei in graph[cur]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
        return count


# Disjoint Set Union
class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)
    
    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        self.comps -= 1

        return True

    def get_components(self):
        return self.comps

class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)

        return dsu.get_components()
    
# DFS
class Solution3:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        count = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count += 1
        return count
