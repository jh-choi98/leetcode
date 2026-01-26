from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder Traversal
# Time: O(h + k)
# Space: O(h + k)  
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

# Recursive DFS (Optimal)
# Time: O(h + k)
# Space: O(h)
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val
        
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)
            
        dfs(root)
        return res

# Iterative DFS (Optimal)
class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return 0
