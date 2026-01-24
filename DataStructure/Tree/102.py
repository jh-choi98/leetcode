from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS with (level by level)
# Time: O(n)
# Space: O(n)       
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        results = []

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

            results.append(cur_level)
        return results

# DFS
# Time: O(n)
# Space: O(n)
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return res
