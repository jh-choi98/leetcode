# Palindrome Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create List and Use Two pointers approach
# T: O(n)
# S: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]):
        if not head or not head.next:
            return True

        lArr = []
        cur = head
        i = 0
        while cur:
            lArr.append(cur.val)
            cur = cur.next
            i += 1

        length = len(lArr)

        for i in range(length // 2):
            if lArr[i] != lArr[length - 1 - i]:
                return False

        return True


# class Solution2:
#     def isPalindrome(self, head: Optional[ListNode]):
