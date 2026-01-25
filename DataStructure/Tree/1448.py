# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# Time: O(n)     
# Space: O(h), where h is the height of the tree   
#   - Best: O(logn)
#   - Worst: O(n)  
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            elif node.val >= max_val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, max_val) + dfs(node.right, max_val)
        
        return dfs(root,root.val)

# DFS
# Time: O(n)     
# Space: O(h), where h is the height of the tree   
#   - Best: O(logn)
#   - Worst: O(n) 
class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res
        
        return dfs(root, root.val)

# BFS
# Time: O(n)
# Space: O(n)
class Solution3:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque([(root, root.val)])
        
        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                res += 1
                max_val = node.val
            if node.left:
                queue.append((node.left, max_val))
            if node.right:
                queue.append((node.right, max_val))
        return res
