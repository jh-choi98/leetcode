# Flatten a multi-level doubly linked list


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


"""
The flatten operation is basically preorder DFS traversal.
We could consider the child pointer as the left pointer in binary tree.
Similarly, the next pointer can be considered as the right pointer 
in binary tree.
"""


# Recursion
# T: O(n)
# S: O(n)
class Solution:
    def flatten(self, head: "Optional[Node]"):
        if not head:
            return head

        # To ensure the prev pointer is never none.
        # Also called sentinel node
        prehead = Node(None, None, head, None)
        self.flatten_dfs(prehead, head)

        # detach the prehead from the real head
        prehead.next.prev = None
        return prehead.next

    def flatten_dfs(self, prev, cur):
        # cur is a pointer to the sub-list that we would like to platten
        # prev is a pointer to the element that should precede the cur
        # return the tail of the flatten list
        if not cur:
            return prev

        # As in the preorder DFS, we take care of the current state
        # first before looking into the children
        cur.prev = prev
        prev.next = cur

        # the cur.next would be tempered in the recursive function
        tempNext = cur.next

        # go ahead to flatten the left subtree and return the tail
        # element to the flattened sublist
        tail = self.flatten_dfs(cur, cur.child)
        # don't need a child anymore
        cur.child = None

        # With the tail element of the previous sublist, we then flatten
        # the right subtree
        return self.flatten_dfs(tail, tempNext)
