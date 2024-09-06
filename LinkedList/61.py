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
