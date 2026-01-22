from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# dfs - recursive
# Time: O(n)      
# Space: O(n)      
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)
    
# dfs - recursive
# Time: O(n)      
# Space: O(n)
class Solution2:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# dfs - iterative
# Time: O(n)      
# Space: O(n)
class Solution3:
    def maxDepth(self, root):
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# BFS
# Time: O(n)
# Space: O(n)
class Solution4:
    def maxDepth(self, root):
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(depth, max_depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return max_depth
                
# bfs
# 레벨 단위 처리 패턴
# Time: O(n)
# Space: O(n)
class Solution5:
    def maxDepth(self, root):
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
