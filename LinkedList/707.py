# Design Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1

        return cur.data

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head
        while cur:
            cur = cur.next

        cur.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        new_node = Node(val)
        count = 0
        cur = self.head
        prev = None

        while count < index:
            prev = cur
            cur = cur.next
            count += 1

        new_node.next = cur
        prev.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        count = 0
        cur = self.head
        prev = None
        while count < index:
            prev = cur
            cur = cur.next
            count += 1

        prev.next = cur.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
