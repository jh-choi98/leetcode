# Hash map + Doubly linked list

from typing import Optional


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None
        
class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            return ValueError("Capacity must be positive")
        
        self.capacity = capacity
        
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _insert_at_front(self, node: Node) -> None:
        first_node = self.head.next
        
        node.prev = self.head
        node.next = first_node
        
        self.head.next = node
        first_node.prev = node
        
    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._insert_at_front(node)
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_front(new_node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            
            if lru_node is None or lru_node is self.head:
                raise RuntimeError("No valid LRU node to remove")
            
            self._remove(lru_node)
            del self.cache[lru_node.key]
        
cache = LRUCache(2)

cache.put(1, 100)
cache.put(2, 200)

print(cache.get(1))

cache.put(3, 300)

print(cache.get(2))
