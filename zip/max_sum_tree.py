from typing import List, Tuple

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
        
"""
Returns the maximum sum in a tree
    - choose cur_node
        - cannot choose its children
    - not chosse cur_node
        - max(choosing its children, not choosing its children)
Time: O(n)
Space: O(h), where h is the height of the tree
    - Best: O(logkn)
    - Worst: O(n)
DP
"""
# class Node:
#     def __init__(self, value, children=None):
#         self.value = value
#         self.children: List[Node] = children if children else []
        
def find_max_sum(root: Node) -> int:
    if not root:
        return 0
    
    def dfs(node: Node) -> Tuple[int, int]:
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


"""
Follow-up: How would you handle a forest (multiple disconnected trees)?
Explain how you would identify components and compute the overall result

1. Identify roots:
    - Create a set of all children nodes by iterating through the input
      list
    - Any node NOT in the children set is a Root
    - Time: O(n) | Space: O(n)

2. Compute totla sum:
    - Run find_max_sum() for each root.
    - Sum up the results

Time: O(n) since we visit every node exactly once across all trees
Space: O(n) for the children set + Recursion stack O(h_max)

Since three edges are directed (parent -> child), running BFS form an
arbitrary node might not reach the root. Instead, I will use a HashSet
to store all nodes that are referenced as children. Then, iterating
through the input list, any node that is not in this set is a root
"""
def find_max_sum_forest(nodes: List[Node]) -> int:
    children_set = set()
    
    for node in nodes:
        for child in node.children:
            children_set.add(child)
            
    max_sum = 0
    
    for node in nodes:
        if node not in children_set:
            max_sum += find_max_sum(node)
            
    return max_sum
