# Copy List with Random Pointer


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# T: O(n)
# S: O(n)
class MySolution:
    def copyRandomList(self, head):
        random_dict = {}

        def createCopiedList(head):
            if not head:
                return None
            new_node = Node(head.val)
            new_node.next = createCopiedList(head.next)
            random_dict[head] = new_node
            return new_node

        def linkRandomList(head, new_head):
            if not head:
                return None
            new_head.random = random_dict.get(head.random)
            linkRandomList(head.next, new_head.next)

        new_head = createCopiedList(head)
        linkRandomList(head, new_head)
        return new_head


# T: O(n)
# S: O(n)
class Solution2:
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head):
        if not head:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        new_node = Node(head.val)
        self.visitedHash[head] = new_node

        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node
