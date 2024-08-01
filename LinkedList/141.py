# Linked List Cycle


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Floyd's Cycle Finding Algorithm
# T: O(n)
# S: O(1)
class Solution1:
    def hasCycle(self, head: Optional[ListNode]):
        if not head or not head.next:
            return False

        p1 = head
        p2 = head

        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True

        return False


# Hash Table
# T: O(n)
# S: O(n)
class Solution2:
    def hasCycle(self, head: Optional[ListNode]):
        nodes_seen = set()
        cur = head
        while cur:
            if cur in nodes_seen:
                return True
            nodes_seen.add(cur)
            cur = cur.next
        return False
