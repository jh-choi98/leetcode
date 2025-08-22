# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            
            if left < node.val and node.val < right:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            
            return False
        return valid(root, -inf, inf)
