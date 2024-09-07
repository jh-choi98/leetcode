class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_back(self, data):
        if not self.head:
            self.add_front(data)
            return

        new_node = Node(data)
        self.length += 1

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def add_front(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_at_index(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError("Invalid Index")

        if index == 0:
            self.add_front(data)
            return

        if index == self.length:
            self.add_back(data)
            return

        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        new_node = Node(data, cur, cur.prev)
        cur.prev.next = new_node
        cur.prev = new_node
        self.length += 1

    def remove_first(self):
        if not self.head:
            return

        self.length -= 1

        if self.length == 1:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def remove_last(self):
        if not self.head:
            return

        if self.length == 1:
            self.remove_first()
            return

        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Invalid Index")

        if index == 0 or index == self.length - 1:
            self.remove_first()
            return

        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1

        cur.prev.next = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        self.length -= 1

    def remove_with_data(self, data):
        if not self.head:
            return

        cur = self.head
        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.remove_first()
                elif cur == self.tail:
                    self.remove_last()
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    self.length -= 1
                return
            cur = cur.next

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next

    def reverse(self):
        cur = self.head
        self.tail = self.head

        while cur:
            prev = cur.prev
            cur.prev = cur.next
            cur.next = prev
            if not cur.prev:
                self.head = cur
            cur = cur.prev

    def get_size(self):
        return self.length

    def print_list(self):
        cur = self.head
        while cur:
            if cur.next:
                print(cur.data, end=" -> ")
            else:
                print(cur.data)
            cur = cur.next


def test_doubly_linked_list():
    dll = DoublyLinkedList()

    # 1. Add to front and back
    print("Adding elements to the list:")
    dll.add_front(10)
    dll.add_back(20)
    dll.add_back(30)
    dll.add_front(5)
    dll.print_list()  # Expected: 5 -> 10 -> 20 -> 30
    print(f"Size: {dll.get_size()}")  # Expected: 4

    # 2. Add at index
    print("\nAdding elements at specific indexes:")
    dll.add_at_index(15, 2)
    dll.add_at_index(25, 4)
    dll.print_list()  # Expected: 5 -> 10 -> 15 -> 20 -> 25 -> 30
    print(f"Size: {dll.get_size()}")  # Expected: 6

    # 3. Remove first and last elements
    print("\nRemoving first and last elements:")
    dll.remove_first()
    dll.remove_last()
    dll.print_list()  # Expected: 10 -> 15 -> 20 -> 25
    print(f"Size: {dll.get_size()}")  # Expected: 4

    # 4. Remove at index
    print("\nRemoving elements at specific indexes:")
    dll.remove_at_index(1)
    dll.print_list()  # Expected: 10 -> 20 -> 25
    print(f"Size: {dll.get_size()}")  # Expected: 3

    # 5. Remove by data value
    print("\nRemoving element with specific data:")
    dll.remove_with_data(20)
    dll.print_list()  # Expected: 10 -> 25
    print(f"Size: {dll.get_size()}")  # Expected: 2

    # 6. Search for elements
    print("\nSearching for elements:")
    node = dll.search(10)
    print(f"Found node with data: {node.data}")  # Expected: 10
    node = dll.search(100)
    print(f"Found node with data: {node}")  # Expected: None

    # 7. Reverse the list
    print("\nReversing the list:")
    dll.reverse()
    dll.print_list()  # Expected: 25 -> 10
    print(f"Size: {dll.get_size()}")  # Expected: 2

    # 8. Final state of the list
    print("\nFinal state of the list:")
    dll.print_list()  # Expected: 25 -> 10
    print(f"Size: {dll.get_size()}")  # Expected: 2


if __name__ == "__main__":
    test_doubly_linked_list()
