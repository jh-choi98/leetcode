class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, i):
        return (i - 1) // 2

    def get_left_child_index(self, i):
        return 2 * i + 1

    def get_right_child_index(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        cur_idx = index
        parent_idx = self.get_parent_index(cur_idx)

        while cur_idx > 0 and self.heap[cur_idx] < self.heap[parent_idx]:
            self.swap(cur_idx, parent_idx)
            cur_idx = parent_idx
            parent_idx = self.get_parent_index(cur_idx)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return min_val

    def heapify_down(self, index):
        cur_idx = index
        left_child_idx = self.get_left_child_index(cur_idx)
        right_child_idx = self.get_right_child_index(cur_idx)
        smallest = cur_idx
        if (
            left_child_idx < len(self.heap)
            and self.heap[left_child_idx] < self.heap[cur_idx]
        ):
            smallest = left_child_idx

        if (
            right_child_idx < len(self.heap)
            and self.heap[right_child_idx] < self.heap[cur_idx]
        ):
            smallest = right_child_idx

        if smallest != cur_idx:
            self.swap(cur_idx, smallest)
            self.heapify_down(smallest)

    def get_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is Empty")
        return self.heap[0]

    def get_size(self):
        return len(self.heap)


heap = MinHeap()
heap.insert(10)
heap.insert(3)
heap.insert(5)
print(heap.get_min())  # 출력: 3
print(heap.extract_min())  # 출력: 3
print(heap.get_min())  # 출력: 5
print(heap.get_size())  # 출력: 2
