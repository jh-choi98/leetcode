# Swap Nodes in Pairs


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# T: O(n)
# S: O(n) if TCO supported, O(1)
class Solution:
    def swapPairs(self, head):
        def swapPairsRecur(cur=head, prev=None):
            if not cur:
                prev.next = None
                return

            if not cur.next:
                prev.next = cur
                return

            next_node = cur.next.next
            cur.next.next = cur
            if prev:
                prev.next = cur.next
            swapPairsRecur(next_node, cur)

        if not head or not head.next:
            return head

        new_head = head.next
        swapPairsRecur(head, None)
        return new_head


"""
1. Start the recursion with head node of the original linked list.

2. Every recursion call is responsible for swapping a pair of nodes.
Let's represent the two nodes to be swapped by firstNode and secondNode.

3. Next recursion is made by calling the function with head of the next pair of nodes.
This call would swap the next two nodes and make further recursive calls
if there are nodes left in the linked list.

4. Once we get the pointer to the remaining swapped list from the recursion call,
we can swap the firstNode and secondNode i.e. the nodes in the current recursive call
and then return the pointer to the secondNode since it will be the new head after swapping.

5. Once all the pairs are swapped in the backtracking step, we would eventually be
returning the pointer to the head of the new swapped list. This head will 
essentially be the second node in the original linked list.
"""


# T: O(n)
# S: O(n)
class Solution2:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node
