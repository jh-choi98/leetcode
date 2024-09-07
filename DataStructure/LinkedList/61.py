# Rotate List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# T: O(n)
# S: O(n)
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        node_map = {}
        cur = head
        len = 0

        while cur:
            node_map[len] = cur
            cur = cur.next
            len += 1

        new_head = head
        rotateCounter = 0
        origin_last_index = len - 1
        total_rotate = k % len

        while rotateCounter != total_rotate:
            cur_last_index = origin_last_index - rotateCounter
            node_map[cur_last_index].next = new_head
            new_head = node_map[cur_last_index]
            node_map[
                cur_last_index - 1 if cur_last_index - 1 >= 0 else origin_last_index
            ].next = None
            rotateCounter += 1

        return new_head


# T: O(n)
# S: O(1)
class Solution2:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head
