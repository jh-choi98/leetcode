from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# Time: O(n)        
# Space: O(n)        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i == length - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# BFS
# Time: O(n)
# Space: O(n)
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        
        while queue:
            right_side = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side:
                res.append(right_side.val)
        return res

# dfs
# Time: O(n)
# Space: O(n)
class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
                
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
            
            