from collections import deque
from typing import List

# BFS
# Time: O(V + E)
# Space: O(V + E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1

        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        res = []
        course_visited = 0

        while queue:
            course = queue.popleft()
            course_visited += 1
            res.append(course)
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return res if course_visited == numCourses else []

# DFS
# Time: O(V + E)
# Space: O(V + E)
class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            graph[course].append(preq)
            
        output = []
        visited, visiting = set(), set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for preq in graph[crs]:
                if not dfs(preq):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
                
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
