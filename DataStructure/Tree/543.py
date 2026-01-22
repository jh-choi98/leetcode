from typing import Optional, Dict, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Brute Force
# Time: O(n^2)
# Space: O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
           return 0
       
        def maxHeight(root: Optional[TreeNode]) -> int:
           if not root:
               return 0
           return 1 + max(maxHeight(root.left), maxHeight(root.right)) 
       
        left_height = maxHeight(root.left)
        right_height = maxHeight(root.right)
        diameter = left_height + right_height
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

# DFS - Recursion
# Time: O(n)
# Space: O(h), where h is the height of the tree
#   - Best: O(logn)
#   - Worst: O(n)
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return res

# DFS - Iterative
# Time: O(n)
# Space: O(n)
"""
For each node, we store in a map:
    - its height
    - its best diameter

After both children are processed, we can compute:
    - height = 1 + max(left_height, right_height)
    - diameter = max(left_height + right_height, left_diameter, right_diameter)
"""
class Solution3:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        mp: Dict[Optional[TreeNode], Tuple[int, int]] = {None: (0, 0)}
        
        while stack:
            node = stack[-1]
            
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_height, left_diameter = mp[node.left]
                right_height, right_diameter = mp[node.right]
                
                mp[node] = (1 + max(left_height, right_height),
                            max(left_height + right_height, left_diameter, right_diameter))
        return mp[root][1]
