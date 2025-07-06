from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(r1, r2):
            if not r1 and not r2:
                return True

            if not r1 or not r2 or r1.val != r2.val:
                return False

            return isEqual(r1.left, r2.left) and isEqual(r1.right, r2.right)

        if not root:
            return False

        if isEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
class Solution2:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(s, t):
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            return False
        
        if not subRoot: return True
        if not root: return False
        
        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        