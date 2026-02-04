from typing import List

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children: List[Node] = children if children else []
        
def maxNonAdjacentTreeSum(root) -> int:
    if not root:
        return 0
    
    def dfs(node: Node) -> tuple[int, int]:
        if not node:
            return (0, 0)
        
        include_cur = node.value
        exclude_cur = 0
        
        for child in node.children:
            include_child, exclude_child = dfs(child)
            
            include_cur += exclude_child
            exclude_cur += max(include_child, exclude_child)
        
        return (include_cur, exclude_cur)

    result = dfs(root)
    return max(result)

# ---------------------------------------
child_of_2 = Node(3)
child_of_3 = Node(1)

node_2 = Node(2,[child_of_2])
node_3 = Node(3,[child_of_3])

root = Node(3, [node_2, node_3])

print(f"Maximum Sum: {maxNonAdjacentTreeSum(root)}")
        
