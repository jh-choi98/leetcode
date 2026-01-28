from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# Time: O(n^2) 
# Space: O(h)
#   - Best: O(logn)
#   - Worst: O(n)
class Solution:
    def getMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        path = root.val + max(left, right)
        return max(0, path)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")
        def dfs(root):
            nonlocal res
            if not root:
                return
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return int(res)

# DFS (Optimal)
# Time: O(n)
# Space: O(h)
#   - Best: O(logn)
#   - Worst: O(n)
class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(node):
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            
            res[0] = max(res[0], node.val + left_max + right_max)
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return res[0]
