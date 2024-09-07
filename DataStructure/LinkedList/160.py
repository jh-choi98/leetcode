# Intersection of Two Linked Lists


# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Hash Set
# T: O(n)
# S: O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodes_set = set()
        curA = headA
        while curA:
            nodes_set.add(curA)
            curA = curA.next

        curB = headB
        while curB:
            if curB in nodes_set:
                return curB
            curB = curB.next

        return None


# Two-pointer
# T: O(n)
# S: O(1)
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        curA = headA
        lenA = 0
        while curA:
            lenA += 1
            curA = curA.next
        curA = headA

        curB = headB
        lenB = 0
        while curB:
            lenB += 1
            curB = curB.next
        curB = headB

        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenA < lenB:
            for i in range(lenB - lenA):
                curB = curB.next

        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None


# Two-pointer2
# T: O(n)
# S: O(1)
"""
If we say that c is the shared part, a is exclusive part of list A and
b is exclusive part of list B, then we can have one pointer 
that goes over a + c + b and the other that goes over b + c + a.

One pointer is essentially measuring the length of the longer list, 
and the other is measuring the length of the shorter list, and then 
placing the start pointer for the longer list. Then both are stepping 
through the list together.
"""


class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        return pA
