# Validate Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        def validate(node, left_bound, right_bound):
            if not node:
                return True

            if not (left_bound < node.val and node.val < right_bound):
                return False

            return validate(node.left, left_bound, node.val) and validate(
                node.right, node.val, right_bound
            )

        return validate(root, float("-inf"), float("inf"))
