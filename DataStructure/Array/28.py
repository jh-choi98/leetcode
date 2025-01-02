# 28. Find the Index of the First Occurrence in a String


# Solution 1
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
