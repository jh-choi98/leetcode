from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs_inorder(node):
            if not node or len(res) == k:
                return
            dfs_inorder(node.left)
            res.append(node.val)
            dfs_inorder(node.right)

        dfs_inorder(root)
        return res[k - 1]

class Soltuion2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right
            
        return 0
