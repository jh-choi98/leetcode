# Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Use Length - Two passes
# T: O(n)
# S: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        if not head.next:
            head = None
            return

        cur = head
        len = 0

        while cur:
            cur = cur.next
            len += 1

        if len == n:
            head = head.next
            return head

        cur = head
        prev = None
        count = 0

        while count != (len - n):
            prev = cur
            cur = cur.next
            count += 1

        prev.next = cur.next
        return head


# One pass - Keeping certain distance
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        if not head.next:
            return None

        left = head
        right = head
        for i in range(n):
            right = right.next

        prev = None
        while right:
            prev = left
            left = left.next
            right = right.next

        if not prev:
            head = head.next
            return head

        prev.next = left.next
        return head
