class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):
        new_node = Node(insertVal)

        if not head:
            new_node.next = new_node
            return new_node

        cur = head
        while cur.val <= cur.next.val and cur.next != head:
            cur = cur.next

        cur = cur.next
        smallest = cur
        while cur.next != smallest:
            if cur.val <= insertVal and insertVal <= cur.next.val:
                temp = cur.next
                cur.next = new_node
                new_node.next = temp
                return head
            cur = cur.next

        cur.next = new_node
        new_node.next = smallest
        return head
