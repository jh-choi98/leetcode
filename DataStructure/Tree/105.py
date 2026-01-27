from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # O(n)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # O(n)
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # O(n)
        return root
    
# Hash Map + DFS
# Time: O(n)
# Space: O(n)
"""
In the basic DFS approach, we search for the root's position in inorder
using linear search, which takes O(n) time per node. 

By precomputing a hash map from values to their indices in inorder, we
can find the root's position in O(1) time.

We also avoid creating new arrays by passing indices that define the
current subarray boundaries.
"""
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)

# DFS (Optimal) - GG
# Time: O(n)
# Space: O(n)
"""
We can avoid the hash map entirely by using a limit-based approach.
Instead of explicitly finding the root's position, we pass a "limit"
value that tells us when to stop building the left subtree. When we
encounter the limit value in inorder, we know the left subtree is
complete. The preorder index tells us which node to create next, and the
inorder index tells us when we have finished a subtree.
"""
class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))
