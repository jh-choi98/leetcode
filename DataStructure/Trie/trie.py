from typing import Dict, Optional

class TrieNode:
    __slots__ = ("children", "is_end")
    """
    used to explicitly declare data members for instances of the class
    
    - Prevents the creation of a dynamic __dict__ for each instance,
      saving memory
    - Restricts the attributes that instances of TrieNode can have only
      children and is_end
    - Can improve performance for classes with many instances, like
      nodes in a trie
      
    In summary, it makes your TrieNode objects smaller and faster by
    limiting their attributes
    """
    
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {} # Forward reference; interpret it as the class TrieNode once it's fully defined
        self.is_end: bool = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            child = node.children.get(ch)
            if child is None:
                child = TrieNode()
                node.children[ch] = child
            node = child
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node and node.is_end)
    
    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
        
    def erase(self, word: str) -> bool:
        """
        Remove 'word' if present. Returns True iff the word existed.
        Avoids an extra O(L) pass by not calling search() first.
        """
        def _erase(node: TrieNode, i: int):
            if i == len(word):
                if not node.is_end:
                   return False, False # (can_del_here, found)
                node.is_end = False
                return len(node.children) == 0, True
            
            ch = word[i]
            child = node.children.get(ch)
            if child is None:
                return False, False
            
            should_del_child, found = _erase(child, i + 1)
            if should_del_child:
                del node.children[ch]
            
            can_del_here = (not node.is_end) and (len(node.children) == 0)
            return can_del_here, found
        
        _, found = _erase(self.root, 0)
        return found
                
    def _find_node(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node
