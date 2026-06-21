from typing import Optional

"""
    Time: O(n)
        The traversal is O(n), where n is the number of nodes. The left
        and right boundary walks each take at most the height of the
        tree, and the leaf DFS visits the tree. Overall, each node is
        processed a constant number of times, so the time complexity is
        O(n)
        
    Space: O(h), where h is the height of the tree
        [Not counting the output list]
        The DFS recursion uses O(h) space, where h is the height of the
        tree. The right boundary list can also store up to O(h) nodes.
        So the extra space is O(h), which becomes O(n) in the worst case
        for a skewed tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def boundary_traversal(root: Optional[TreeNode]) -> list[int]:
    """
        I'll handle the empty tree first. If there is no root, the
        boundary is just an empty list
    """
    if not root:
        return []
    
    def is_leaf(node: TreeNode) -> bool:
        return node.left is None and node.right is None
    
    """
        If the root itself is a leaf, I should return it once.
        This avoids adding the root again when I collect leaf nodes.
    """
    if is_leaf(root):
        return [root.val]
    
    result = [root.val]
    
    """
        I'll split the boundary into three parts after the root: left
        boundary, leaf nodes, and reversed right boundary.
        For the left boundary, I start from root.left. I exclude leaves
        because leaves will be added separately
    """
    node = root.left
    
    while node:
        if not is_leaf(node):
            result.append(node.val)
            
        """
            For the left boundary, I prefer going left. If there is no
            left child, I go right
        """
        if node.left:
            node = node.left
        else:
            node = node.right
            
    """
        Next, I'll add all leaf nodes from left to right using DFS.
        Since I already excluded leaves from the left and right
        boundaries, this avoids duplicates
    """
    def add_leaves(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        if is_leaf(node):
            result.append(node.val)
            return
        
        add_leaves(node.left)
        add_leaves(node.right)
        
    add_leaves(root)
        
    """
        For the right boundary, I start from root.right. I collect
        the nodes top-down first, then reverse them at the end
    """
    right_boundary = []
    node = root.right
    
    while node:
        if not is_leaf(node):
            right_boundary.append(node.val)
            
        """
            For the right boundary, I prefer going right.
            If there is no right child, I go left
            This follows the boundary traversal preference, not
            necessarily the path from the rightmost leaf
        """
        if node.right:
            node = node.right
        else:
            node = node.left
            
    """
        The right boundary needs to be added from bottom to top, so
        I reverse the list before appending it to the answer
    """
    result.extend(reversed(right_boundary))
    
    return result

# Simple test:
#
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
#
# Boundary should be:
# root: 1
# left boundary: 2
# leaves: 4, 5, 6, 7
# right boundary reversed: 3
#
# Expected: [1, 2, 4, 5, 6, 7, 3]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(boundary_traversal(root))
# [1, 2, 4, 5, 6, 7, 3]

single = TreeNode(1)

print(boundary_traversal(single))
# [1]
