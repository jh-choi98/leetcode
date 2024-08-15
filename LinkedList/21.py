# Merge Two Sorted Lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iteration
# T: O(n + m)
# S: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if not list1:
            return list2
        if not list2:
            return list1

        cur1 = list1
        cur2 = list2
        new_list = None

        if list1.val >= list2.val:
            new_list = cur2
            cur2 = cur2.next
        else:
            new_list = cur1
            cur1 = cur1.next
        cur3 = new_list
        while True:
            if not cur1:
                cur3.next = cur2
                break
            if not cur2:
                cur3.next = cur1
                break

            if cur1.val >= cur2.val:
                cur3.next = cur2
                cur2 = cur2.next
            else:
                cur3.next = cur1
                cur1 = cur1.next
            cur3 = cur3.next

        return new_list


# Iteration with prehead
# T: O(n + m)
# S: O(1)
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return prehead.next


# Recursion
# T: O(n + m)
# S: O(n + m)
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
