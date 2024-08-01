# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Hash Table
# T: O(n)
# S: O(n)
class Solution:
    def detectCycle(self, head: Optional[ListNode]):
        nodes_seen = set()
        cur = head
        while cur:
            if cur in nodes_seen:
                return cur
            nodes_seen.add(cur)
            cur = cur.next
        return


# class Solution2:
#     def detectCycle(self, head: Optional[ListNode]):
