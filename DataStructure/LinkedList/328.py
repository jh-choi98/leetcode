# Odd Even Linked List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]):
        if not head or not head.next or not head.next.next:
            return head

        oddCur = head
        evenCur = head.next
        evenHead = evenCur
        cur = head.next.next
        isOdd = True

        while cur:
            if isOdd:
                oddCur.next = cur
                oddCur = oddCur.next
            else:
                evenCur.next = cur
                evenCur = evenCur.next

            isOdd = not isOdd
            cur = cur.next

        evenCur.next = None
        oddCur.next = evenHead
        return head


class Solution2:
    def oddEvenList(self, head: Optional[ListNode]):
        if not head:
            return None

        odd = head
        evenHead = head.next
        even = evenHead

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head
