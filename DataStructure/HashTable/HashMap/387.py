class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = len(s)
        counter_hash = {}
        index_hash = {}
        for i in range(len(s)):
            if s[i] not in counter_hash:
                counter_hash[s[i]] = 1
                index_hash[s[i]] = i
            else:
                counter_hash[s[i]] += 1

        for char in counter_hash:
            if counter_hash[char] == 1:
                index = min(index, index_hash[char])
        if index == len(s):
            index = -1
        return index
