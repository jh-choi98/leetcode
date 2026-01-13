from collections import deque
from typing import List

# Topological Sort (Kahn's Algorithm)
# Time: O(V + E)
# Space: O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        visited_count = 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            course = queue.popleft()
            visited_count += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return visited_count == numCourses

# Cycle Detection (DFS)
# Time: O(V + E)
# Space: O(V + E)
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
            
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if graph[course] == []:
                return True
            
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            graph[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
