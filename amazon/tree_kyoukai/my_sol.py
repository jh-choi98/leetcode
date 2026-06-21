from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def boundary_traversal(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    def is_leaf(node: TreeNode) -> bool:
        return node.left is None and node.right is None
    
    result = [root.val]
    
    if is_leaf(root):
        return result
    
    node = root.left
    
    while node:
        if not is_leaf(node):
            result.append(node.val)
            
        if node.left:
            node = node.left
        else:
            node = node.right
            
    def add_leaves(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        if is_leaf(node):
            result.append(node.val)
            return
        
        add_leaves(node.left)
        add_leaves(node.right)
        
    add_leaves(root)
    
    right_boundary = []
    node = root.right
    
    while node:
        if not is_leaf(node):
            right_boundary.append(node.val)
        
        if node.right:
            node = node.right
        else:
            node = node.left
            
    result.extend(reversed(right_boundary))
    return result
    
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(boundary_traversal(root))

single = TreeNode(1)

print(boundary_traversal(single))
