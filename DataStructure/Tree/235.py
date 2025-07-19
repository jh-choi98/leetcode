from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if not root or not p or not q:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

class Solution2:
    def lowestCommonAncestor(self, root: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
