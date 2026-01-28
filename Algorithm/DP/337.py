from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
       
# Recursion
# Time: O(2^n)
# Space: O(h)
#   - Best: O(logn)
#   - Worst: O(n)
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
            
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
            
        return max(res, self.rob(root.left) + self.rob(root.right))

# DP (Memoization)
# Time: O(n)
# Space: O(n)
class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {None: 0}
        
        def dfs(node):
            if node in cache:
                return cache[node]
            
            cache[node] = node.val
            if node.left:
                cache[node] += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                cache[node] += dfs(node.right.left) + dfs(node.right.right)
            
            cache[node] = max(cache[node], max(dfs(node.left), dfs(node.right)))
                
            return cache[node]

        return dfs(root)

# DP (Optimal)
# Time: O(n)
# Space: O(n)
"""
Instead of caching all nodes, we can return two values from each
subtree: 
    the maximum if we rob this node, and the maximum if we skip it.
This eliminates the need for a hash map.
"""
class Solution3:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            
            with_node = node.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)
            
            return [with_node, without_root]
        
        return max(dfs(root))
