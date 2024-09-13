# Maximum Depth of Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        def maxDepth_recur(root, depth):
            if not root:
                return depth

            left_max = maxDepth_recur(root.left, depth + 1)
            right_max = maxDepth_recur(root.right, depth + 1)
            return max(left_max, right_max)

        return maxDepth_recur(root, 0)


class Solution2:
    def maxDepth(self, root):
        if not root:
            return 0

        left_max = self.maxDepth(root.left) + 1
        right_max = self.maxDepth(root.right) + 1

        return max(left_max, right_max)
