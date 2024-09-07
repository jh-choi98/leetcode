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
