from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            group = 1
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
                group += 1
            chars[insert] = chars[i]
            insert += 1
            if group > 1:
                string = str(group)
                chars[insert:insert+len(string)] = list(string)
                insert += len(string)
            i += group
        return insert

class Solution2:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        group = 1
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i-1]:
                group += 1
            else:
                chars[insert] = chars[i - 1]
                insert += 1
                if group > 1:
                    for c in str(group):
                        chars[insert] = c
                        insert += 1
                group = 1
        return insert
