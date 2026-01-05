from typing import Dict

class WordNode:
    def __init__(self):
        self.children: Dict[str, "WordNode"] = {}
        self.is_end: bool = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            child = node.children.get(c)
            if child is None:
                child = WordNode()
                node.children[c] = child
            node = child
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: WordNode, i: int):
            cur = node

            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_end
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
