# Unique Binary Search Trees 2
"""
n-th Catalan Number (C_n)
The n-th Catalan number gives # of distinct binary search trees
that can be formed with n unique values.
So, time and space complexity of generating BSTs are both O(C_n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Approaches
1. Recursion: recursively construct left and right subtrees and
    combine them with each root
2. Dynamic Programming: use DP to store the result of subproblems (subtrees)
    and utilize them for constructing unique BSTs
    
Approach Differences
: the recursive approach constructs the trees from scratch every time,
while the DP approach reuses previously computed subtrees to avoid redundant work
"""

"""
Recursion
1. Base Case: if the start index is greater than the end index, return
a list containing None. This represents an empty tree and serves as
the base case for the recursion.

2. Choose Root: for every number(i) in the range from start to end,
consider i as the root of the tree.

3. Generate Left Subtrees: recursively call the function to generate
all possible left subtrees using numbers from start to i-1.

4. Generate Right Subtrees: recursively call the function to generate
all possible right subtrees using from i+1 to end.

5. Combine Subtrees: for each combination of left and right subtrees,
create a new tree with i as the root and the corresponding left and right
subtrees. Append this tree to the list of all possible trees.

6. Return Trees: finally, return the lsit of all trees generated.
"""


class Solution:
    def generateTrees(self, n: int):
        def generateTrees_recur(start, end):
            if start > end:
                return [
                    None,
                ]

            all_trees = []
            for i in range(start, end + 1):
                # generate all possible left subtrees
                left_trees = generateTrees_recur(start, i - 1)
                # generate all possible right subtrees
                right_trees = generateTrees_recur(i + 1, end)

                # combine left and right subtrees with the cur node as root
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees

        # handle edge case for n == 0
        return generateTrees_recur(1, n) if n else []


"""
Dynamic Programming

1. Initialization: create a DP table dp where dp[i] will store 
all the unique BSTs with i nodes. Initialize dp[0] whith a single None
value representing an empty tree.

2. Iterate over # of nodes: for every number 'nodes' from 1 to n, iterate
and construct all possible trees with 'nodes' number of nodes.

3. Choose root: for every possible root value within the current 'nodes',
iterate and use the root to build trees.

4. Use previously computed subtrees: for the chosen root, use the previously
computed dp[root - 1] for left subtrees and dp[nodes - root] for right subtrees

5. Clone right subtree: since the right subtree's values will be affected by
the choice of the root, clone the right subtree with an offset equal to
the root value. The clone function handles this.

6. Combine subtrees: create a new tree by combining the current root with
the left and right subtrees. Append this tree to dp[nodes].

7. Return result: finally return the trees stored in dp[n] 
"""


class Solution2:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        # List Comprehension: 파이썬에서 리스트를 간결하고 효율적으로 생성하는 문법
        # ['expression (리스트에 들어갈 요소)' for 'item (반복 변수)' in 'iterable' if 'condition']
        dp = [[] for _ in range(n + 1)]  # n+1개의 빈 리스트를 요소로 가지는 리스트
        dp[0].append(None)
        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                for left_tree in dp[root - 1]:
                    for right_tree in dp[nodes - root]:
                        root_node = TreeNode(root)
                        root_node.left = left_tree
                        root_node.right = self.clone(right_tree, root)
                        dp[nodes].append(root_node)
        return dp[n]

    def clone(self, n: TreeNode, offset: int):
        if n:
            node = TreeNode(n.val + offset)
            node.lfet = self.clone(n.left, offset)
            node.right = self.clone(n.right, offset)
            return node
        return None
