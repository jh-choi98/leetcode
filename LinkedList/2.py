# Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# T: O(n)
# S: O(n)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        num1 = 0
        num2 = 0
        cur1 = l1
        cur2 = l2

        exp = 1
        while cur1:
            num1 = num1 + exp * cur1.val
            cur1 = cur1.next
            exp *= 10

        exp = 1
        while cur2:
            num2 = num2 + exp * cur2.val
            cur2 = cur2.next
            exp *= 10
        sum = num1 + num2

        if sum == 0:
            new_node = ListNode(0)
            return new_node

        prehead = ListNode(-1)
        cur = prehead
        while sum > 0:
            new_node = ListNode(sum % 10)
            cur.next = new_node
            cur = cur.next
            sum = sum // 10

        return prehead.next
