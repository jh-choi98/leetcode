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
        if index < 0 or index >= self.length:
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

    # def remove_first():

    # def remove_last():

    # def remove_at_index():

    # def remove_with_data():

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

    # def search():

    # def reverse():


ll = SinglyLinkedList()

ll.add_back(1)
ll.print_list()
ll.add_back(3)
ll.print_list()
ll.add_back(5)
ll.print_list()

ll.add_front(0)
ll.print_list()

ll.add_front(-1)
ll.print_list()

ll.add_front(-2)
ll.print_list()

ll.add_at_index(-3, 0)
ll.print_list()
ll.add_at_index(6, ll.get_size() - 1)
ll.print_list()

ll.add_at_index(2, 5)
ll.print_list()
ll.add_at_index(4, 7)
ll.print_list()
