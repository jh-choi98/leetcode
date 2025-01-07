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


class Solution3:
    def strStr(self, haystack: str, needle: str):
        lps = [0] * len(needle)
        prevLPS, i = 0, 1

        # Setting LPS
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

            if j == len(needle):
                return i - len(needle)

        return -1
