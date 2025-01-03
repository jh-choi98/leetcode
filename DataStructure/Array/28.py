# 28. Find the Index of the First Occurrence in a String


# Solution 1: Brute Force Algorithm with While
class Solution:
    def strStr(self, haystack: str, needle: str):
        h_index = 0
        n_index = 0

        h_len = len(haystack)
        n_len = len(needle)

        while h_index < h_len:
            if needle[n_index] == haystack[h_index] and n_index == n_len - 1:
                return h_index - (n_len - 1)
            elif needle[n_index] == haystack[h_index]:
                h_index += 1
                n_index += 1
            else:
                h_index -= n_index - 1
                n_index = 0

        return -1


# Solution 2: Brute Force Algorithm with For
class Solution2:
    def strStr(self, haystack: str, needle: str):
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
