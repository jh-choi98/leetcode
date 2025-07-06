# Remove Nth Node From End of List
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# T: O(n)
# S: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        slow = fast = head
        prev = None

        delay = n
        while fast:
            if n <= 0:
                prev = slow
                slow = slow.next
            fast = fast.next
            n -= 1

        target = slow
        if prev:
            prev.next = target.next
        else:
            head = target.next

        slow.next = None
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

class Solution3:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        while n > 0 and r:
            r = r.next
            n -= 1
            
        while r:
            l = l.next
            r = r.next
            
        l.next = l.next.next
        return head
