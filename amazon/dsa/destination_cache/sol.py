# Hasp map + doubly linked list

from typing import Optional


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None
        
class LRUCache:
    def __init__(self, capacity: int):
        """
            I'll assume capacity is positive. If not, I think it's
            better to fail fast because an LRU cache with zero capacity
            is not very useful
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self.capacity = capacity
        
        # To get O(1) lookup by key, I'll use a hash map from key to
        # node
        self.cache = {}
        
        """
            To update recency in O(1), I'll use a doubly linked list.
            The front will represent the most recently used item, and
            the back will represent the least recently used item.
            I'm using dummy head and tail nodes to make insert and
            remove operations simpler, especially for edge cases.
        """
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: Node) -> None:
        """
            This helper removes a node from the linked list in O(1),
            assuming we already have a direct reference to the ndoe
        """
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _insert_at_front(self, node: Node) -> None:
        """
            This helper inserts a node right after the head, which marks
            it as the most recently used item
        """
        first_node = self.head.next
        
        node.prev = self.head
        node.next = first_node
        
        self.head.next = node
        first_node.prev = node
        
    def _move_to_front(self, node: Node) -> None:
        """
            Whenever a key is accessed or updated, it becomes the most
            recently used item, so I remove it from its current position
            and move it to the front
        """
        self._remove(node)
        self._insert_at_front(node)
    
    def get(self, key: int) -> int:
        """
            For get, I first check the hash map. If the key does not
            exist, I'll return -1. In a real system, we could also
            return None depending on the API contract
        """
        if key not in self.cache:
            return -1
        
        """
            If the key exists, accessing it makes it recently used, so I
            move its node to the front before returning the value
        """
        node = self.cache[key]
        self._move_to_front(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
            For put, there are two cases. If the key already exists, I
            update the value and move it to the front.
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return
        
        """
            If this is a new key, I create a new node, add it to the
            hash map, and insert it a the front because it is now the
            most recently used item
        """
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_front(new_node)
        
        """
            If adding this new item makes the cache exceed capacity. I
            evict the least recently used item, which is right before
            the tail
        """
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            
            if lru_node is None or lru_node is self.head:
                raise RuntimeError("No valid LRU node to remove")
            
            self._remove(lru_node)
            del self.cache[lru_node.key]


cache = LRUCache(2)

cache.put(1, 100)
cache.put(2, 200)

print(cache.get(1)) # 100

cache.put(3, 300) # Evicts key 2

print(cache.get(2)) # -1
print(cache.get(3)) # 300
print(cache.get(1)) # 100
