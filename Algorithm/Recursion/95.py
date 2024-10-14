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
