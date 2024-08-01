class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_back(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def add_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.length += 1

    def add_at_index(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError("Invalid Index")

        new_node = Node(data)

        if index == 0:
            self.add_front(data)
            return
        elif index == self.length - 1:
            self.add_back(data)
            return

        cur = self.head
        prev = None
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1

        new_node.next = cur
        prev.next = new_node
        self.length += 1

    def remove_first(self):
        if not self.head:
            return

        self.head = self.head.next
        self.length -= 1

    def remove_last(self):
        if not self.head:
            return

        if self.length == 1:
            self.remove_first()
            return

        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        self.length -= 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Invalid Index")

        if not self.head:
            return

        if index == 0:
            self.remove_first()
            return

        if index == self.length - 1:
            self.remove_last()
            return

        cur = self.head
        prev = None
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        prev.next = cur.next
        self.length -= 1

    def remove_with_data(self, data):
        if not self.head:
            return

        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if not prev:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                self.length -= 1
                return
            else:
                prev = cur
                cur = cur.next

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

    def search(self, data):
        cur = self.head

        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        def _reverse_recur(cur, prev):
            if not cur:
                return prev
            next_node = cur.next
            cur.next = prev
            return _reverse_recur(next_node, cur)

        self.head = _reverse_recur(self.head, None)


# ll = SinglyLinkedList()

# ll.add_back(1)
# ll.print_list()
# ll.add_back(3)
# ll.print_list()
# ll.add_back(5)
# ll.print_list()

# ll.add_front(0)
# ll.print_list()

# ll.add_front(-1)
# ll.print_list()

# ll.add_front(-2)
# ll.print_list()

# ll.add_at_index(-3, 0)
# ll.print_list()
# ll.add_at_index(6, ll.get_size() - 1)
# ll.print_list()

# ll.add_at_index(2, 5)
# ll.print_list()
# ll.add_at_index(4, 7)
# ll.print_list()

# ll.remove_first()
# ll.print_list()
# print(ll.get_size())

# ll.remove_last()
# ll.print_list()
# print(ll.get_size())

# ll.remove_at_index(3)
# ll.print_list()
# print(ll.get_size())

# ll.remove_with_data(-1)
# ll.print_list()
# print(ll.get_size())

# ll.reverse()
# ll.print_list()
